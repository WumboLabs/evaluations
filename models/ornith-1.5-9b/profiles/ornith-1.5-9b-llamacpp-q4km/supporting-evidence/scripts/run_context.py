#!/usr/bin/env python3
"""wlep-context runner+scorer: token-targeted rungs with live tokenizer verification.

Usage: run_context.py <base_url> <model_label> <seeds=42,43,44> <rungs=4096,16384>
Writes phase6-context/calibration/<label>.raw.jsonl and .scored.json
"""
import json, statistics as st, sys, time, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from context_gen import build  # noqa

BASE, LABEL = sys.argv[1], sys.argv[2]
SEEDS = [int(s) for s in sys.argv[3].split(",")]
RUNGS = [int(r) for r in sys.argv[4].split(",")]
OUT = Path(__file__).parent / "calibration"
OUT.mkdir(exist_ok=True)

def post(path, payload):
    req = urllib.request.Request(BASE + path, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())

def tokenize(text):
    try:
        return post("/tokenize", {"content": text}).get("tokens")
    except Exception:
        return None

rows = []
for rung in RUNGS:
    for seed in SEEDS:
        d = build(rung, seed)
        toks = tokenize(d["prompt"])
        actual = len(toks) if toks is not None else None
        # deterministic two-pass refinement: rescale filler to converge on rung
        if actual:
            d2 = build(max(256, int(rung * rung / actual)), seed)
            t2 = tokenize(d2["prompt"])
            if t2 and abs(len(t2) - rung) < abs(actual - rung):
                d, toks, actual = d2, t2, len(t2)
        payload = {"messages": [{"role": "user", "content": d["prompt"]}],
                   "temperature": 0.2, "top_p": 0.95, "seed": seed,
                   "max_tokens": 160, "chat_template_kwargs": {"enable_thinking": False}}
        t0 = time.perf_counter()
        try:
            b = post("/v1/chat/completions", payload)
            text = b["choices"][0]["message"]["content"] or ""
            finish = b["choices"][0]["finish_reason"]
        except Exception as e:
            text, finish = "", f"ERROR:{e}"
        wall = round(time.perf_counter() - t0, 2)
        low = text.lower()
        checks = {}
        for k, needle in (("B", d["expected"]["B"]), ("M", d["expected"]["M"]), ("E", d["expected"]["E"])):
            checks[k] = needle.lower() in low
        checks["ABSENT"] = ("not_specified" in low) and d["expected"]["A"].lower() in low
        rows.append({"rung": rung, "seed": seed, "tokens_target": rung, "tokens_actual": actual,
                     "token_delta_pct": round(abs(actual - rung) / rung * 100, 1) if actual else None,
                     "checks": {k: bool(v) for k, v in checks.items()},
                     "passed": all(checks.values()), "finish": finish, "wall_s": wall,
                     "output_preview": text[:200]})
with open(OUT / f"{LABEL}.raw.jsonl", "w") as f:
    for r in rows: f.write(json.dumps(r) + "\n")
# rung verdicts per failure-confirmation rule: rung passes unless >=2 of 3 seeds fail
summary = {}
for rung in RUNGS:
    rs = [r for r in rows if r["rung"] == rung]
    fails = [r for r in rs if not r["passed"]]
    summary[str(rung)] = {"seeds_passed": sum(1 for r in rs if r["passed"]),
                          "verdict": ("FAIL_CONFIRMED" if len(fails) >= 2 else "PASS") if len(rs) >= 3 else ("FAIL_CONFIRMED" if not fails else "INCONCLUSIVE_LT3SEEDS"),
                          "mean_tokens_actual": round(st.mean([r["tokens_actual"] or 0 for r in rs])) if rs else None,
                          "max_token_delta_pct": max((r["token_delta_pct"] or 0) for r in rs)}
json.dump(summary, open(OUT / f"{LABEL}.scored.json", "w"), indent=2)
print(json.dumps(summary, indent=1))
