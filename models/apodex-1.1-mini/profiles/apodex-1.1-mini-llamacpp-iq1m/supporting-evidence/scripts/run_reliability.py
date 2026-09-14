#!/usr/bin/env python3
"""Run the wlep-reliability contract against a local llama-server.

Usage: run_reliability.py <base_url> <model_label> <seeds=42,43,44> [sampling_override.json]
Writes reliability/calibration/<label>.raw.jsonl
sampling_override.json (optional): {"temperature":..,"top_p":..,"top_k":..,
  "repeat_penalty":..,"presence_penalty":..,"chat_template_kwargs":{...}}
"""
from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE.parent / "contracts" / "wlep-reliability-0.1.0-draft.json"
OUTDIR = HERE.parent / "calibration"
if len(sys.argv) > 4:
    OVERRIDE = json.load(open(sys.argv[4]))

TEMPLATE_KWARGS = OVERRIDE.get("chat_template_kwargs", {"enable_thinking": False})
BASE, LABEL = sys.argv[1], sys.argv[2]
SEEDS = [int(s) for s in (sys.argv[3] if len(sys.argv) > 3 else "42,43,44").split(",")]

C = json.load(open(CONTRACT))
OUTDIR.mkdir(exist_ok=True)
OUT = OUTDIR / f"{LABEL}.raw.jsonl"



def gen(task: dict, seed: int) -> dict:
    payload = {
        "messages": task["messages"],
        "temperature": OVERRIDE.get("temperature", C["sampling_default"]["temperature"]),
        "top_p": OVERRIDE.get("top_p", C["sampling_default"]["top_p"]),
        "seed": seed,
                "max_tokens": max(task["max_tokens"], OVERRIDE.get("budget_min", 0)),
    }
    for k in ("top_k", "repeat_penalty", "presence_penalty", "min_p"):
        if k in OVERRIDE:
            payload[k] = OVERRIDE[k]
    ctk = dict(TEMPLATE_KWARGS)
    if ctk:
        payload["chat_template_kwargs"] = ctk
    req = urllib.request.Request(BASE + "/v1/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=300) as r:
        body = json.loads(r.read())
    return body, time.perf_counter() - t0


n = 0
with open(OUT, "w") as f:
    for seed in SEEDS:
        for task in C["tasks"]:
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
            f.write(json.dumps(row) + "\n")
            f.flush()
            n += 1
print(f"{LABEL}: {n} generations written to {OUT}")
