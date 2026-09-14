#!/usr/bin/env python3
"""WELP Phase 2 performance characterization — campaign ornith-1.5-9b.

Harness lineage: apodex-1.1-mini phase2_perf_v3 + phase2_prefill_nocache
(frozen techniques). This runtime's cache metrics are TRUSTED
(toolchain/runtime_capabilities.json), so prefill uses a dedicated
--no-cache-prompt instance AND the processed-token cross-check.

Protocol: 2 decode warmups; 5 measured decode reps (long-form story,
1024 max tokens, thinking OFF); 5 measured prefill reps on port 8932
(--no-cache-prompt, 4096-token unique [tag-seed] prompts); unique content
per rep; full distribution reported; any early-termination or unverified
prefill rep invalidated in-place (Invalid Run Handling).
"""
import json, os, random, statistics, time, urllib.request, subprocess

PORT = int(os.environ.get("WELP_PORT", "8931"))
PORT_NC = int(os.environ.get("WELP_PORT_NC", "8932"))
OUT = os.path.dirname(os.path.abspath(__file__)) + "/../results"
os.makedirs(OUT, exist_ok=True)

WORDS = ("harbor lantern meadow quartz ember thistle cobalt juniper slate marigold "
         "cinder willow granite zephyr amber tundra saffron basalt clover driftwood").split()

DECODE_PROMPT = ("Write a detailed short story about a lighthouse keeper and a "
                 "storm. Write freely until the story is complete; aim for at "
                 "least 600 words.")

def post(port, payload):
    req = urllib.request.Request(f"http://127.0.0.1:{port}/v1/chat/completions",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=1200) as r:
        return json.loads(r.read())

def one_run(kind, seed, prompt_tokens_target, gen_tokens, port):
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
    resp = post(port, payload)
    wall = time.perf_counter() - t0
    u = resp["usage"]; tim = resp.get("timings", {})
    return {"kind": kind, "seed": seed, "port": port,
            "prompt_tokens_reported": u["prompt_tokens"],
            "prompt_tokens_cached": u.get("prompt_tokens_details", {}).get("cached_tokens"),
            "gen_tokens": u["completion_tokens"], "wall_s": round(wall, 4),
            "prompt_ms": tim.get("prompt_ms"), "prompt_per_second": tim.get("prompt_per_second"),
            "predicted_ms": tim.get("predicted_ms"), "predicted_per_second": tim.get("predicted_per_second"),
            "finish_reason": resp["choices"][0]["finish_reason"],
            "text_preview": resp["choices"][0]["message"]["content"][:80]}

STAGE = os.environ.get("WELP_STAGE", "all")
records = []
RAW = f"{OUT}/phase2_raw.jsonl"
if os.path.exists(RAW):
    records = [json.loads(l) for l in open(RAW)]

def save():
    with open(RAW, "w") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")

if STAGE in ("decode", "all"):
    records.append({**one_run("warmup_decode", 9001, 200, 64, PORT), "warmup": True})
    records.append({**one_run("warmup_decode", 9002, 200, 64, PORT), "warmup": True})
    for rep, s in enumerate([42, 52, 62, 72, 82]):
        rec = one_run("decode_tps", s, 200, 1024, PORT); rec["rep"] = rep
        records.append(rec); print(json.dumps({k: rec[k] for k in ("kind","seed","gen_tokens","predicted_per_second","finish_reason")}))
    save()
if STAGE in ("prefill", "all"):
    for rep, s in enumerate([43, 53, 63, 73, 83]):
        rec = one_run("prefill_4k", s, 4096, 8, PORT_NC); rec["rep"] = rep
        rec["implied_tps_crosscheck"] = round(rec["prompt_tokens_reported"] / (rec["prompt_ms"] / 1000), 1) if rec.get("prompt_ms") else None
        records.append(rec); print(json.dumps({k: rec.get(k) for k in ("kind","seed","prompt_tokens_reported","prompt_tokens_cached","prompt_per_second")}))
    save()

# invalidation rules
for rec in records:
    if rec["kind"].startswith("warmup"):
        continue
    if rec["kind"] == "decode_tps" and rec["gen_tokens"] < 500:
        rec["invalidated"] = True; rec["invalidation_reason"] = f"early termination ({rec['gen_tokens']} tokens)"
    if rec["kind"] == "prefill_4k":
        if (rec.get("prompt_tokens_cached") or 0) > 0:
            rec["invalidated"] = True; rec["invalidation_reason"] = "cache reuse on no-cache instance"
        elif rec.get("prompt_ms") and rec.get("implied_tps_crosscheck") and rec["implied_tps_crosscheck"] < 100:
            rec["invalidated"] = True; rec["invalidation_reason"] = f"prefill processing unverified (implied {rec['implied_tps_crosscheck']} t/s)"
save()

dec = [r for r in records if r["kind"] == "decode_tps" and not r.get("invalidated")]
pre = [r for r in records if r["kind"] == "prefill_4k" and not r.get("invalidated")]
summary = {}
for name, rows, key in (("decode_tps", dec, "predicted_per_second"), ("prefill_4k", pre, "prompt_per_second")):
    vals = [r[key] for r in rows]
    summary[name] = {"n_valid": len(vals), "values": [round(v, 2) for v in vals],
                     "mean": round(statistics.mean(vals), 2) if vals else None,
                     "median": round(statistics.median(vals), 2) if vals else None,
                     "stdev": round(statistics.stdev(vals), 2) if len(vals) > 1 else None}
ttfts = [(r["prompt_ms"], r["predicted_ms"] / r["gen_tokens"]) for r in dec
         if r.get("prompt_ms") and r.get("predicted_ms") and r.get("gen_tokens")]
summary["ttft_decode_ms"] = {
    "prompt_ms_mean": round(statistics.mean(t[0] for t in ttfts), 2) if ttfts else None,
    "first_token_est_ms": round(statistics.mean(t[0] + t[1] for t in ttfts), 2) if ttfts else None,
    "note": "prompt_ms from server timings; first-token estimate = prompt_ms + mean inter-token time"}
json.dump(summary, open(f"{OUT}/phase2_summary.json", "w"), indent=1)
print(json.dumps(summary, indent=1))
