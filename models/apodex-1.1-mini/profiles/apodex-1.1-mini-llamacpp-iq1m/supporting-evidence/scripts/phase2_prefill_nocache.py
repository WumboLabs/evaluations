#!/usr/bin/env python3
"""Phase 2 prefill measurement with prompt caching explicitly disabled
(--no-cache-prompt instance). Frozen rule technique: explicit cache disable.
5 measured reps, unique [tag-seed] content, processed-token cross-check."""
import json, os, random, statistics, time, urllib.request

PORT = int(os.environ.get("WLEP_PORT", "18451"))
OUT = os.path.dirname(os.path.abspath(__file__)) + "/../results"
WORDS = ("harbor lantern meadow quartz ember thistle cobalt juniper slate marigold "
         "cinder willow granite zephyr amber tundra saffron basalt clover driftwood").split()

def post(payload):
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/v1/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.loads(r.read())

def one_run(seed, target_tokens):
    r = random.Random(seed)
    n_words = max(16, int(target_tokens * 0.75))
    user = (f"[tag-{seed}] Ignore the text above. Reply with exactly the word OK "
            f"and nothing else.\n" + " ".join(r.choice(WORDS) for _ in range(n_words)))
    t0 = time.perf_counter()
    resp = post({"messages": [{"role": "user", "content": user}],
                 "max_tokens": 8, "temperature": 0.2, "top_p": 0.95, "seed": seed,
                 "chat_template_kwargs": {"enable_thinking": False}})
    wall = time.perf_counter() - t0
    u = resp["usage"]; tim = resp.get("timings", {})
    return {"kind": "prefill_nocache", "seed": seed,
            "prompt_tokens_reported": u["prompt_tokens"],
            "prompt_tokens_cached": u.get("prompt_tokens_details", {}).get("cached_tokens"),
            "gen_tokens": u["completion_tokens"], "wall_s": round(wall, 4),
            "prompt_ms": tim.get("prompt_ms"), "prompt_per_second": tim.get("prompt_per_second"),
            "predicted_ms": tim.get("predicted_ms"),
            "finish_reason": resp["choices"][0]["finish_reason"]}

records = []
records.append({**one_run(9101, 4096), "warmup": True})
vals = []
for rep, s in enumerate([43, 53, 63, 73, 83]):
    rec = one_run(s, 4096); rec["rep"] = rep
    rec["implied_tps_crosscheck"] = round(rec["prompt_tokens_reported"] / (rec["prompt_ms"] / 1000), 1) if rec.get("prompt_ms") else None
    records.append(rec); print(json.dumps(rec))
    vals.append(rec)
with open(f"{OUT}/phase2_prefill_nocache_raw.jsonl", "w") as f:
    for rec in records:
        f.write(json.dumps(rec) + "\n")
pps = [r["prompt_per_second"] for r in vals if r.get("prompt_per_second")]
summary = {"n_valid": len(pps), "values": pps,
           "mean": round(statistics.mean(pps), 2), "median": round(statistics.median(pps), 2),
           "stdev": round(statistics.stdev(pps), 2)}
json.dump(summary, open(f"{OUT}/phase2_prefill_nocache_summary.json", "w"), indent=1)
print(json.dumps(summary))
