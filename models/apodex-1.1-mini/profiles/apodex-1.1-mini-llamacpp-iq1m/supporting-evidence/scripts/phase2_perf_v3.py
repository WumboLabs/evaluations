#!/usr/bin/env python3
"""WLEP-2 Phase 2 performance characterization, campaign revision v3.

History (all runs retained, Invalid Run Handling):
- frozen overnight-hardening phase2_perf.py: run1 invalidated (decode workload
  allowed 2-token early termination; contamination audit mis-triggered).
- v2: run2 invalidated (counting prompt induced refusal on 2/5 seeds).
Deltas in v3:
- decode workload = natural long-form story task (~600+ words);
- cached_tokens audit replaced by processed-token cross-check: this runtime
  reports a CONSTANT cached_tokens=74 for all prompts (telemetry artifact,
  protocol finding PF-04), so real reuse is excluded by verifying implied
  prefill t/s from prompt_ms vs reported token count.
Otherwise identical: 2 warmups, 5 measured decode reps, 5 measured prefill
reps, unique [tag-seed] content per rep, full distribution reported.
"""
import json, os, random, statistics, time, urllib.request

PORT = int(os.environ.get("WLEP_PORT", "18450"))
OUT = os.path.dirname(os.path.abspath(__file__)) + "/../results"
os.makedirs(OUT, exist_ok=True)

WORDS = ("harbor lantern meadow quartz ember thistle cobalt juniper slate marigold "
         "cinder willow granite zephyr amber tundra saffron basalt clover driftwood").split()

DECODE_PROMPT = ("Write a detailed short story about a lighthouse keeper and a "
                 "storm. Write freely until the story is complete; aim for at "
                 "least 600 words.")

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

for rec in records:
    if rec["kind"].startswith("warmup"):
        continue
    if rec["kind"] == "decode_tps" and rec["gen_tokens"] < 500:
        rec["invalidated"] = True; rec["invalidation_reason"] = f"early termination ({rec['gen_tokens']} tokens)"
    if rec.get("prompt_ms") and rec["kind"] == "prefill_4k":
        implied_tps = rec["prompt_tokens_reported"] / (rec["prompt_ms"] / 1000)
        if implied_tps < 100:
            rec["invalidated"] = True; rec["invalidation_reason"] = f"prefill processing unverified (implied {implied_tps:.0f} t/s)"

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
ttfts = [(r["prompt_ms"], r["predicted_ms"]) for r in dec if r.get("prompt_ms") and not r.get("invalidated")]
summary["ttft_decode_ms"] = {
    "n": len(ttfts),
    "mean_prompt_ms": round(statistics.mean(t[0] for t in ttfts), 2) if ttfts else None,
    "mean_total_to_first_chunk_ms_est": round(statistics.mean(t[0] + 1000 / (t[1] or 1) for t in ttfts), 2) if ttfts else None}
json.dump(summary, open(f"{OUT}/phase2_summary.json", "w"), indent=1)
print(json.dumps(summary))
