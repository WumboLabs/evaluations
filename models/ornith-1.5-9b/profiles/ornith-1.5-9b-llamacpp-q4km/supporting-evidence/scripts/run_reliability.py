#!/usr/bin/env python3
"""WELP Phase 4 reliability runner — campaign ornith-1.5-9b.

Contract: welp-reliability 0.1.0-draft tasks (frozen wlep-reliability-0.1.0-draft.json,
sha256 cf42d2fa…, 54 tasks x 7 categories). Scorer revision selftested separately.
Baseline REASONING_OFF (server --reasoning off + enable_thinking=false per request).
budget_min_tokens=384 floor applied to every task max_tokens.
Resume-safe: appends, skips (id, seed) already present.
"""
import json, os, sys, time, urllib.request

PORT = int(os.environ.get("WELP_PORT", "8931"))
BASE = os.path.dirname(os.path.abspath(__file__)) + "/.."
C = json.load(open(f"{BASE}/contracts/wlep-reliability-0.1.0-draft.json"))
OUT = f"{BASE}/results/reliability_raw.jsonl"
SEEDS = [int(s) for s in os.environ.get("WELP_SEEDS", "42,43,44").split(",")]
BUDGET_MIN = 384

def gen(task, seed):
    payload = {"messages": task["messages"],
               "temperature": C["sampling_default"]["temperature"],
               "top_p": C["sampling_default"]["top_p"],
               "seed": seed,
               "max_tokens": max(task["max_tokens"], BUDGET_MIN),
               "chat_template_kwargs": {"enable_thinking": False}}
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/v1/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read()), time.perf_counter() - t0

rows = []
if os.path.exists(OUT):
    rows = [json.loads(l) for l in open(OUT)]
done = {(r["id"], r["seed"]) for r in rows}
n = 0
with open(OUT, "a") as f:
    for seed in SEEDS:
        for task in C["tasks"]:
            if (task["id"], seed) in done:
                continue
            try:
                b, wall = gen(task, seed)
                msg = b["choices"][0]["message"]
                row = {"id": task["id"], "seed": seed,
                       "output": msg.get("content") or "",
                       "reasoning_content": msg.get("reasoning_content"),
                       "finish_reason": b["choices"][0]["finish_reason"],
                       "usage": b.get("usage", {}), "wall_s": round(wall, 4)}
            except Exception as exc:
                row = {"id": task["id"], "seed": seed, "output": "", "error": repr(exc),
                       "finish_reason": "ERROR"}
            f.write(json.dumps(row) + "\n"); f.flush(); n += 1
leak = sum(1 for r in map(json.loads, open(OUT)) if r.get("reasoning_content"))
print(f"{n} generations written to {OUT}; reasoning_leak={leak}")
