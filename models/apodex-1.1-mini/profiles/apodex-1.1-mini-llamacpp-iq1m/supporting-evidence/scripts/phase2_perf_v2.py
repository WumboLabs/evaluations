#!/usr/bin/env python3
"""WLEP-2 Phase 2 performance characterization, campaign revision v2.

Delta vs frozen overnight-hardening phase2_perf.py (documented, hash-recorded):
- unique [tag-N] moved to PROMPT START so even prefix-cache hits cannot occur
  (run1 audit flagged a 74-token static chat-template prefix on every rep);
- decode workload forces >=~512 generated tokens (run1 let a compliant model
  answer "OK" after 2 tokens);
- otherwise identical: 2 warmups, 5 measured decode reps, 5 measured prefill
  reps, unique content per rep, mean/median/stddev reporting, no cherry-picking.
"""
import json, os, random, statistics, sys, time, urllib.request

PORT = int(os.environ.get("WLEP_PORT", "18450"))
OUT = os.path.dirname(os.path.abspath(__file__)) + "/../results"
os.makedirs(OUT, exist_ok=True)

WORDS = ("harbor lantern meadow quartz ember thistle cobalt juniper slate marigold "
         "cinder willow granite zephyr amber tundra saffron basalt clover driftwood").split()

DECODE_PROMPT = ("Write the integers from 1 to 300 inclusive, one per line, "
                 "each line formatted exactly as 'N: step'. Do not summarize.")

def post(path, payload):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}{path}",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.loads(r.read())

def one_run(kind, seed, prompt_tokens_target, gen_tokens):
    r = random.Random(seed)
    n_words = max(16, int(prompt_tokens_target * 0.75))
    body_words = " ".join(r.choice(WORDS) for _ in range(n_words))
    if kind == "decode_tps":
        user = f"[tag-{seed}] {DECODE_PROMPT}"
    else:
        user = (f"[tag-{seed}] Ignore the text above. Reply with exactly the word OK "
                f"and nothing else.\n{body_words}")
    payload = {"messages": [{"role": "user", "content": user}],
               "max_tokens": gen_tokens, "temperature": 0.2, "top_p": 0.95,
               "seed": seed, "chat_template_kwargs": {"enable_thinking": False}}
    t0 = time.perf_counter()
    resp = post("/v1/chat/completions", payload)
    wall = time.perf_counter() - t0
    u = resp["usage"]
    tim = resp.get("timings", {})
    return {"kind": kind, "seed": seed,
            "prompt_tokens_reported": u["prompt_tokens"],
            "prompt_tokens_cached": u.get("prompt_tokens_details", {}).get("cached_tokens"),
            "gen_tokens": u["completion_tokens"],
            "wall_s": round(wall, 4),
            "prompt_ms": tim.get("prompt_ms"), "prompt_per_second": tim.get("prompt_per_second"),
            "predicted_ms": tim.get("predicted_ms"), "predicted_per_second": tim.get("predicted_per_second"),
            "finish_reason": resp["choices"][0]["finish_reason"],
            "text_preview": resp["choices"][0]["message"]["content"][:80]}

records = []
for s in (9001, 9002):
    records.append({"invalidated": False, **one_run("warmup_decode", s, 200, 64)})
records.append({**one_run("warmup_prefill", 9101, 4096, 8), "warmup": True})
for rep, s in enumerate([42, 52, 62, 72, 82]):
    rec = one_run("decode_tps", s, 200, 1024); rec["rep"] = rep
    records.append(rec); print(json.dumps(rec))
for rep, s in enumerate([43, 53, 63, 73, 83]):
    rec = one_run("prefill_4k", s, 4096, 8); rec["rep"] = rep
    records.append(rec); print(json.dumps(rec))
# audits
for rec in records:
    if rec["kind"].startswith("warmup"): continue
    cached = rec.get("prompt_tokens_cached")
    if cached not in (None, 0):
        rec["invalidated"] = True; rec["invalidation_reason"] = f"prefix-cache reuse ({cached} tokens)"
    if rec["kind"] == "decode_tps" and rec["gen_tokens"] < 500:
        rec["invalidated"] = True; rec["invalidation_reason"] = f"early termination ({rec['gen_tokens']} tokens)"
with open(f"{OUT}/phase2_raw.jsonl", "w") as f:
    for rec in records:
        f.write(json.dumps(rec) + "\n")

dec = [r for r in records if r["kind"] == "decode_tps" and not r.get("invalidated")]
pre = [r for r in records if r["kind"] == "prefill_4k" and not r.get("invalidated")]
summary = {}
for name, rows, key in (("decode_tps", dec, "predicted_per_second"), ("prefill_4k", pre, "prompt_per_second")):
    vals = [r[key] for r in rows]
    summary[name] = {"n_valid": len(vals), "values": vals,
                     "mean": round(statistics.mean(vals), 2) if vals else None,
                     "median": round(statistics.median(vals), 2) if vals else None,
                     "stdev": round(statistics.stdev(vals), 2) if len(vals) > 1 else None}
ttfts = [r["prompt_ms"] + r["predicted_ms"] for r in dec if r.get("prompt_ms")]
summary["ttft_decode_ms"] = {"n": len(ttfts), "mean": round(statistics.mean(ttfts), 2) if ttfts else None}
json.dump(summary, open(f"{OUT}/phase2_summary.json", "w"), indent=1)
print(json.dumps(summary))
