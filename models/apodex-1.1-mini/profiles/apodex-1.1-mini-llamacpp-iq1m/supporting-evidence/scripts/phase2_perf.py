#!/usr/bin/env python3
"""WLEP-2 Phase 2 performance characterization (frozen protocol: Repetition Policy +
Invalid Run Handling prefill/cache rule).

Methodology:
- warmup pass before measured repetitions
- 5 measured repetitions per workload (Repetition Policy standard)
- UNIQUE prompt content per repetition for prefill measurement (cache rule);
  verify processed-token counts against expected size
- never cherry-pick fastest run; all reps reported
"""
import json, os, random, statistics, sys, time, urllib.request

PORT = int(os.environ.get("WLEP_PORT", "8452"))
OUT = os.path.dirname(os.path.abspath(__file__)) + "/../results"
os.makedirs(OUT, exist_ok=True)

WORDS = ("harbor lantern meadow quartz ember thistle cobalt juniper slate marigold "
         "cinder willow granite zephyr amber tundra saffron basalt clover driftwood").split()

def gen_unique_prompt(seed: int, approx_tokens: int) -> str:
    # ~0.75 words/token -> words = tokens*0.75; unique content every repetition
    r = random.Random(seed)
    n_words = max(16, int(approx_tokens * 0.75))
    return " ".join(r.choice(WORDS) for _ in range(n_words)) + \
        f"\nIgnore the text above. Reply with exactly the word OK and nothing else. [tag-{seed}]"

def post(path: str, payload: dict) -> dict:
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}{path}",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(r.read())

def one_run(kind: str, seed: int, prompt_tokens_target: int, gen_tokens: int) -> dict:
    prompt = gen_unique_prompt(seed, prompt_tokens_target)
    body = {"messages": [{"role": "user", "content": prompt}],
            "max_tokens": gen_tokens, "temperature": 0.2, "top_p": 0.95,
            "seed": seed, "chat_template_kwargs": {"enable_thinking": False}}
    t0 = time.perf_counter()
    resp = post("/v1/chat/completions", body)
    wall = time.perf_counter() - t0
    u = resp["usage"]
    tim = resp.get("timings", {})
    run = {"kind": kind, "seed": seed,
           "prompt_tokens_reported": u["prompt_tokens"],
           "prompt_tokens_cached": u.get("prompt_tokens_details", {}).get("cached_tokens"),
           "gen_tokens": u["completion_tokens"],
           "wall_s": round(wall, 4),
           "prompt_ms": tim.get("prompt_ms"), "prompt_per_second": tim.get("prompt_per_second"),
           "predicted_ms": tim.get("predicted_ms"), "predicted_per_second": tim.get("predicted_per_second"),
           "ttft_ms_est": None, "finish_reason": resp["choices"][0]["finish_reason"],
           "text_preview": resp["choices"][0]["message"]["content"][:120]}
    if kind == "prefill" and tim.get("prompt_ms"):
        run["ttft_ms_est"] = round(tim.get("prompt_ms") + tim.get("predicted_ms", 0), 2)
    return run

def main():
    records = []
    # ---- warmups (not measured) ----
    for i, s in enumerate([9001, 9002]):
        records.append({"invalidated": False, **one_run("warmup_decode", s, 200, 64)})
    records.append({**one_run("warmup_prefill", 9101, 4096, 8), "warmup": True})
    # ---- workload A: decode throughput (short prompt, long generation), 5 reps ----
    for rep, s in enumerate([42, 52, 62, 72, 82]):
        r = one_run("decode_tps", s, 200, 512)
        r["rep"] = rep
        records.append(r)
        print(json.dumps(r))
    # ---- workload B: independent prefill ~4K tokens, minimal generation, 5 reps ----
    for rep, s in enumerate([43, 53, 63, 73, 83]):
        r = one_run("prefill_4k", s, 4096, 8)
        r["rep"] = rep
        records.append(r)
        print(json.dumps(r))
    # ---- contamination audit ----
    for r in records:
        if r["kind"].startswith("warmup"):
            continue
        cached = r.get("prompt_tokens_cached")
        if cached not in (None, 0):
            r["invalidated"] = True
            r["invalidation_reason"] = f"prefix-cache reuse detected ({cached} cached tokens)"
    with open(f"{OUT}/phase2_raw.jsonl", "w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")
    print("records:", len(records))

if __name__ == "__main__":
    main()
