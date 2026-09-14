#!/usr/bin/env python3
"""WELP Phase 3 practical viability — campaign ornith-1.5-9b.

Contract: welp-practical-viability 0.1.4-draft (sha256 4c5de7fe…), 30 tasks.
Scorer: pf01 revision 2 (sha256 d5dedf5b…), selftest 60/60 PASS before use.
Baseline reasoning state: REASONING_OFF — server launched --reasoning off AND
every request sends chat_template_kwargs.enable_thinking=false; every raw row
must show reasoning_content null (frozen pass3-starvation guard).
Seeds 42, 43, 44; T=0.2 top_p=0.95 per contract sampling_default.
"""
import json, os, sys, time, urllib.request

PORT = int(os.environ.get("WELP_PORT", "8931"))
BASE = os.path.dirname(os.path.abspath(__file__)) + "/.."
CONTRACT = f"{BASE}/../../welp/contracts/welp-practical-viability-0.1.3-draft.json"  # version field = 0.1.4-draft
OUT = f"{BASE}/results/phase3_raw.jsonl"
SEEDS = [42, 43, 44]

C = json.load(open(CONTRACT))
assert C["version"] == "0.1.4-draft", C["version"]

def chat(payload):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/v1/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())

rows = []
if os.path.exists(OUT):
    rows = [json.loads(l) for l in open(OUT)]
done = {(r["id"], r["seed"]) for r in rows}

for seed in SEEDS:
    for t in C["tasks"]:
        if (t["id"], seed) in done:
            continue
        payload = {"messages": [{"role": "user", "content": t["prompt"]}],
                   "max_tokens": t["max_tokens"], "temperature": 0.2, "top_p": 0.95,
                   "seed": seed, "chat_template_kwargs": {"enable_thinking": False}}
        t0 = time.perf_counter()
        resp = chat(payload)
        wall = time.perf_counter() - t0
        msg = resp["choices"][0]["message"]
        rows.append({"id": t["id"], "seed": seed, "output": msg.get("content"),
                     "reasoning_content": msg.get("reasoning_content"),
                     "finish_reason": resp["choices"][0]["finish_reason"],
                     "usage": resp["usage"], "wall_s": round(wall, 4)})
        with open(OUT, "a") as f:
            f.write(json.dumps(rows[-1]) + "\n")
        print(t["id"], seed, repr((msg.get("content") or "")[:50]), flush=True)

# guard: thinking-starvation / reasoning leak
leak = [r for r in rows if r.get("reasoning_content")]
starved = [r for r in rows if r["finish_reason"] == "length" and not (r["output"] or "").strip()]
print(f"rows={len(rows)} reasoning_leak={len(leak)} empty_length={len(starved)}")
if leak or starved:
    print("GUARD FAIL — pass must be invalidated per frozen pass3 precedent", file=sys.stderr)
    sys.exit(2)
