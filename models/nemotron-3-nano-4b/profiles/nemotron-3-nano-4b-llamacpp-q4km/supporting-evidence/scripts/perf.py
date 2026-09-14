#!/usr/bin/env python3
"""WLEP Phase 2 performance characterization.
Warmup + N measured reps per workload; reports individual repetitions + mean/median/stddev.
Never cherry-picks fastest run."""
import json, statistics, sys, time, urllib.request

BASE = "http://127.0.0.1:8471"
REPS = 5  # provisional WLEP repetition policy
OUT = sys.argv[1] if len(sys.argv) > 1 else "results/performance/performance.json"

def complete(payload):
    req = urllib.request.Request(BASE + "/v1/chat/completions",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=600) as r:
        body = json.loads(r.read())
    wall = time.perf_counter() - t0
    return body, wall

# Workload A: decode-bound (short prompt, ~256 generated tokens)
WORKLOAD_A = {"model": "nemotron-3-nano-4b-q4km", "temperature": 0,
              "messages": [{"role": "user", "content": "Count from 1 to 200, one number per line."}],
              "max_tokens": 512}
# Workload B: prefill-bound (~1500-token prompt, short generation)
import random
FILLER_WORDS = ("fox river stone cloud bridge lantern harbor meadow signal zephyr "
                 "copper meadow anchor velvet summit orbit thistle granite ember "
                 "willow cobalt prairie falcon marble juniper quartz beacon ").split()

def _unique_filler(n_words):
    rng = random.Random(random.getrandbits(128))
    return " ".join(rng.choice(FILLER_WORDS) for _ in range(n_words))

def workload_b():
    # Entire prompt body unique per rep: defeats KV prefix caching so prompt_ms
    # reflects real prefill of all tokens.
    content = (_unique_filler(2100) +
               "\n\nIgnore the word list above. What is 6 * 7? Reply with only the number."
               + f"\n[run-nonce-{random.getrandbits(64)}]")
    return {"model": "nemotron-3-nano-4b-q4km", "temperature": 0,
            "messages": [{"role": "user", "content": content}], "max_tokens": 16}

results = {}
for name, mk in [("decode_bound", lambda: WORKLOAD_A), ("prefill_bound", workload_b)]:
    body, _ = complete(mk())   # warmup
    print(f"{name} warmup ok")
    runs = []
    for i in range(REPS):
        b, wall = complete(mk())
        t = b.get("timings", {})
        usage = b.get("usage", {})
        runs.append({
            "rep": i + 1, "wall_s": round(wall, 4),
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
            "ttft_s": t.get("prompt_ms", 0) / 1000 if t else None,
            "prompt_tok_s": t.get("prompt_per_second"),
            "predict_tok_s": t.get("predicted_per_second"),
            "finish_reason": b["choices"][0]["finish_reason"],
            "raw_timings_present": bool(t),
        })
        print(json.dumps(runs[-1]))
    def agg(key):
        vals = [r[key] for r in runs if r[key] is not None]
        if not vals: return None
        return {"mean": round(statistics.mean(vals), 3),
                "median": round(statistics.median(vals), 3),
                "stdev": round(statistics.stdev(vals), 3) if len(vals) > 1 else 0,
                "min": min(vals), "max": max(vals)}
    results[name] = {
        "workload": {"note": "decode_bound: fixed short prompt; prefill_bound: unique random-word prompt per rep (~2600 tokens), max_tokens 16"},
        "repetitions": runs,
        "aggregate_wall_s": agg("wall_s"),
        "aggregate_ttft_s": agg("ttft_s"),
        "aggregate_prompt_tok_s": agg("prompt_tok_s"),
        "aggregate_predict_tok_s": agg("predict_tok_s"),
    }

import subprocess
vr = subprocess.run(["nvidia-smi", "--query-gpu=memory.used,temperature.gpu,power.draw",
                     "--format=csv,noheader"], capture_output=True, text=True).stdout.strip()
out = {"phase": 2, "reps_configured": REPS, "warmups": 2, "measured_runs": REPS * 2,
       "sampling": {"temperature": 0, "note": "greedy for deterministic perf measurement"},
       "gpu_after": vr, "server_endpoint": BASE, "results": results,
       "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
json.dump(out, open(OUT, "w"), indent=2)
print("wrote", OUT)
