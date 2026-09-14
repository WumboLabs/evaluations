#!/usr/bin/env python3
"""Run the WLEP practical viability contract against a local server.
Usage: run_calibration.py <base_url> <model_label> <seeds=42,43,44>
Writes calibration/<label>.raw.jsonl"""
import json, sys, time, urllib.request

CONTRACT = json.load(open("contracts/wlep-practical-viability-0.1.2-draft.json"))
BASE, LABEL = sys.argv[1], sys.argv[2]
SEEDS = [int(s) for s in (sys.argv[3] if len(sys.argv) > 3 else "42").split(",")]
OUT = f"calibration/{LABEL}.raw.jsonl"

def gen(task, seed):
    payload = {"model": "calibration", "temperature": CONTRACT["sampling_default"]["temperature"],
               "top_p": CONTRACT["sampling_default"]["top_p"], "seed": seed,
               "max_tokens": task["max_tokens"],
               "messages": [{"role": "user", "content": task["prompt"]}]}
    req = urllib.request.Request(BASE + "/v1/chat/completions",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=180) as r:
        body = json.loads(r.read())
    return body, time.perf_counter() - t0

n = 0
with open(OUT, "w") as f:
    for seed in SEEDS:
        for task in CONTRACT["tasks"]:
            try:
                b, wall = gen(task, seed)
                msg = b["choices"][0]["message"]
                row = {"id": task["id"], "seed": seed,
                       "output": msg.get("content") or "",
                       "reasoning_content": msg.get("reasoning_content"),
                       "finish_reason": b["choices"][0]["finish_reason"],
                       "usage": b.get("usage", {}), "wall_s": round(wall, 4)}
            except Exception as e:
                row = {"id": task["id"], "seed": seed, "output": "",
                       "error": repr(e), "finish_reason": "ERROR"}
            f.write(json.dumps(row) + "\n"); f.flush()
            n += 1
print(f"{LABEL}: {n} generations written to {OUT}")
