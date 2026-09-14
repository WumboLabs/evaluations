#!/usr/bin/env python3
"""Generic WLEP module runner: any raw-model module contract against a local llama-server.

Usage:
  run_module.py <base_url> <label> <seeds=42,43,44> <contract.json> [mode] [sampling.json]

Modes:
  plain      (default) single-turn chat completions
  tools      native tool-call loop with deterministic mock execution
  reasoning  runs each task twice per seed: reasoning OFF then ON (enable_thinking kwargs)

Writes <outdir>/<label>.raw.jsonl next to the contract.
"""
from __future__ import annotations
import json, sys, time, urllib.request
from pathlib import Path

BASE, LABEL = sys.argv[1], sys.argv[2]
SEEDS = [int(s) for s in sys.argv[3].split(",")]
CONTRACT_PATH = Path(sys.argv[4])
MODE = sys.argv[5] if len(sys.argv) > 5 else "plain"
OVERRIDE = json.load(open(sys.argv[6])) if len(sys.argv) > 6 else {}

C = json.load(open(CONTRACT_PATH))
OUTDIR = CONTRACT_PATH.parent.parent / "calibration"
OUTDIR.mkdir(exist_ok=True)
OUT = OUTDIR / f"{LABEL}.raw.jsonl"

if MODE == "tools":
    sys.path.insert(0, str(CONTRACT_PATH.parent.parent / "harness"))
    import mock_tools  # noqa: E402

CORPUS_TEXT = ""
if "corpus" in C:
    cpath = CONTRACT_PATH.parent / C["corpus"]["path"].split("/")[-1]
    if not cpath.exists():
        cpath = CONTRACT_PATH.parent.parent / "corpus" / Path(C["corpus"]["path"]).name
    corpus = json.load(open(cpath))
    CORPUS_TEXT = "\n\n".join(
        f"[{d['doc_id']} {sec['section_id']}] {sec['text']}"
        for d in corpus["documents"] for sec in d["sections"])

def post(payload):
    req = urllib.request.Request(BASE + "/v1/chat/completions",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=300) as r:
        body = json.loads(r.read())
    return body, time.perf_counter() - t0

def sampling(seed, max_tokens):
    p = {"temperature": C["sampling_default"]["temperature"],
         "top_p": C["sampling_default"]["top_p"],
         "seed": seed,
         "max_tokens": max(max_tokens, int(OVERRIDE.get("budget_min", 0)))}
    for k in ("top_k", "repeat_penalty", "presence_penalty", "min_p"):
        if k in OVERRIDE:
            p[k] = OVERRIDE[k]
    return p

def template_kwargs(reasoning=None):
    ctk = OVERRIDE.get("chat_template_kwargs", {"enable_thinking": False})
    if MODE == "reasoning" and reasoning is not None:
        ctk = dict(ctk)
        ctk["enable_thinking"] = reasoning == "on"
    return ctk

def run_plain(task, seed):
    messages = [dict(m) for m in task["messages"]]
    if CORPUS_TEXT:
        messages[-1] = dict(messages[-1])
        messages[-1]["content"] = "DOCUMENTS:\n" + CORPUS_TEXT + "\n\nREQUEST: " + messages[-1]["content"]
    payload = {"messages": messages, **sampling(seed, task["max_tokens"]),
               "chat_template_kwargs": template_kwargs()}
    b, wall = post(payload)
    msg = b["choices"][0]["message"]
    return {"id": task["id"], "seed": seed, "output": msg.get("content") or "",
            "finish_reason": b["choices"][0]["finish_reason"], "usage": b.get("usage", {}),
            "timings": b.get("timings", {}), "wall_s": round(wall, 3),
            "reasoning_mode": "off" if MODE != "reasoning" else "off"}

def run_reasoning(task, seed):
    rows = []
    for mode in ("off", "on"):
        payload = {"messages": task["messages"], **sampling(seed, C.get("pins", {}).get("output_cap_per_side_tokens", 400)),
                   "chat_template_kwargs": template_kwargs(mode)}
        try:
            b, wall = post(payload)
            msg = b["choices"][0]["message"]
            rows.append({"id": task["id"], "seed": seed, "reasoning_mode": mode,
                "output": msg.get("content") or "", "reasoning_content": msg.get("reasoning_content"),
                "finish_reason": b["choices"][0]["finish_reason"], "usage": b.get("usage", {}),
                "timings": b.get("timings", {}), "wall_s": round(wall, 3), "error": None})
        except Exception as exc:
            rows.append({"id": task["id"], "seed": seed, "reasoning_mode": mode,
                "output": "", "error": repr(exc), "finish_reason": "ERROR"})
    return rows

def run_tools(task, seed):
    messages = [{"role": "user", "content": task["user"]}]
    trace = []
    for turn in range(task.get("max_turns", 3)):
        payload = {"messages": messages, "tools": C["tool_catalog"],
                   **sampling(seed, task.get("max_tokens_per_turn", 320)),
                   "chat_template_kwargs": template_kwargs()}
        try:
            b, wall = post(payload)
        except Exception as exc:
            trace.append({"turn": turn, "error": repr(exc)})
            break
        msg = b["choices"][0]["message"]
        calls = msg.get("tool_calls") or []
        trace.append({"turn": turn, "content": msg.get("content") or "",
                      "tool_calls": [{"name": c.get("function", {}).get("name"),
                                      "arguments_raw": c.get("function", {}).get("arguments")}
                                     for c in calls],
                      "finish_reason": b["choices"][0]["finish_reason"],
                      "usage": b.get("usage", {}), "wall_s": round(wall, 3)})
        if not calls:
            break
        messages.append({"role": "assistant",
                         "content": msg.get("content") or "",
                         "tool_calls": msg["tool_calls"]})
        results = []
        for c in calls:
            name = c.get("function", {}).get("name")
            try:
                args = json.loads(c.get("function", {}).get("arguments") or "{}")
                if not isinstance(args, dict):
                    raise ValueError("arguments not an object")
            except Exception as exc:
                results.append({"role": "tool", "tool_call_id": c.get("id"), "name": name,
                                "content": json.dumps({"error": f"ARGUMENT_PARSE_ERROR: {exc}"})})
                continue
            result = mock_tools.execute(name, args)
            results.append({"role": "tool", "tool_call_id": c.get("id"), "name": name,
                            "content": json.dumps(result)})
        messages.extend(results)
    return {"id": task["id"], "seed": seed, "trace": trace}

n = 0
with open(OUT, "w") as f:
    for seed in SEEDS:
        for task in C["tasks"]:
            try:
                if MODE == "tools":
                    row = run_tools(task, seed)
                elif MODE == "reasoning":
                    for r in run_reasoning(task, seed):
                        f.write(json.dumps(r) + "\n"); n += 1
                    continue
                else:
                    row = run_plain(task, seed)
            except Exception as exc:
                row = {"id": task["id"], "seed": seed, "error": repr(exc), "finish_reason": "ERROR"}
            f.write(json.dumps(row) + "\n")
            f.flush()
            n += 1
print(f"{LABEL}[{MODE}]: {n} rows written to {OUT}")
