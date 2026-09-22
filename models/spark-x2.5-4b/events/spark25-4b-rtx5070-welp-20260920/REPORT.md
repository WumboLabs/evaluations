# Spark-X2.5-4B — current-WELP characterization on RTX 5070 12 GB (official Q8_0, upstream llama.cpp)

- **Event ID:** `spark25-4b-rtx5070-welp-20260920`
- **Event date:** 2026-09-20
- **Model:** Spark-X2.5-4B (`XHToken/Spark-X2.5-4B`, SparkLLM Team / iFlytek, Apache-2.0)
- **Profile:** `spark25-4b-q8-0-llamacpp` (reasoning-on vendor-default canonical profile)
- **Hardware:** RTX 5070 12 GB (WumboJetsII)
- **Campaign execution:** **COMPLETE_PASS** (all planned surfaces executed with valid evidence, including negatives)
- **Classification:** **READY_WITH_GUARDRAILS** (R-C5: SEMANTIC_CAPABILITY ACCEPTABLE · BUDGET_DISCIPLINE POOR · CONTEXT_USABILITY CHARACTERIZED · INTEGRATION_QUALITY CLEAN)

All measurements below are MEASURED unless labeled otherwise. This is the public-safe scientific
record; the retained local campaign bundle
(`research/model-evaluations/spark-x2.5-4b/spark-x2.5-4b-rtx5070-welp-characterization-2026-09-20`)
governs on any conflict. The campaign ran 2026-09-20/21 under measurement snapshot
`welp-next-snapshot-2026-09-19-methodology-revision` (public WELP commit
`79f9de13de04325e50e05b0eed28b56471a19028`, DRAFT - NOT v1.0); terminal closeout followed the
campaign execution-state lifecycle on 2026-09-22.

## 1. Tested artifact and runtime

- Publisher XHToken (SparkLLM Team, iFlytek); trained on Huawei Ascend clusters. Canonical repo
  `XHToken/Spark-X2.5-4B` @ `0bcb35678590218655dff3765b9e61c83b35e9c4` (created 2026-08-24;
  recently released, new-to-workspace). Vendor benchmark-table claims (AIME 2026 90.7,
  SWE-Bench Pro 44.4, …) are EXTERNAL_REPORTED thinking-mode anchors, not locally validated.
- Architecture (card + config + GGUF metadata, MEASURED): `spark2_5`, 36 layers in 3×sliding +
  1×full attention repeats (27 SWA / 9 full, window 512), GQA 16/4 heads, head_dim 256, dual RoPE,
  tied embeddings, vocab 131,072, BF16 4,112,079,360 params, `max_position_embeddings` 1,048,576.
  Text-only.
- Exact artifact: official publisher `XHToken/Spark-X2.5-4B-GGUF` @ `9826e0be84e6e6e8b9668abc91421109a1df1e2d`,
  **`Spark-X2.5-4B-Q8_0.gguf`**, **4,375,021,152 bytes**, SHA-256
  **`5c2c3c190e4337e1016b8593ca8e26e8b18c972200b107385d4ec61a25d9dea2`** — exact official LFS
  identity (MEASURED on the local copy; Q8_0 upload 2026-09-07, later repo commits README-only).
  Q8_0 chosen over F16 (8.23 GB, would strand VRAM) and Q4_K_M (needless quant confound).
- Runtime: **upstream llama.cpp `b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063`** (tag `b10999`,
  0.4.1-dev build 1), isolated CUDA SM120 build (nvcc CUDA 13.3.73). `spark2_5` support first
  shipped in b10828 (PR #27868); no pre-existing local tree supported the architecture.
- Admission: ENHANCED_SEMANTIC (new-architecture trigger). Loader proof (`arch = spark2_5`,
  `n_ctx_train = 1048576`, 290 tensors, Q8_0 8.50 BPW, SWA active) + full known-answer battery
  PASS; 0 CUDA/OOM/Xid.

## 2. Canonical profile and performance (RTX 5070)

Full GPU residency (`-ngl 99`, 36/36 layers), FA on, f16 KV, `-np 1` (verified), embedded Jinja
template, vendor sampler (temp 1.0 / top_p 0.95 / top_k −1), **REASONING_ON** (vendor default),
default context 32,768 / guarded 131,072, standardized 512-token output reserve.

- llama-bench canonical arm (5 reps): **pp512 9,275.99 ± 239.14; tg128 126.14 ± 0.07 tok/s**.
- Short TTFT (12-tok prompt, 5 runs) median **26.6 ms**; short-prompt decode 122.1 tok/s.
- Moderate prompt (4,114 tok): TTFT 494.6 ms; prefill 8,318 tok/s.
- Near-full prefill curve: 8,329 (8K) → 7,939 (16K) → ~4,500 (64K) → **4,318 tok/s (128K)**;
  full-window decode ~59 tok/s at 128K occupancy. The 3:1 SWA hybrid keeps prefill fast through
  128K — deployment-relevant long-context throughput for a 4B-class model on a 12 GB card.
- Reasoning controls (requested = effective, MEASURED): default ON renders `<think>` with
  non-empty reasoning in every run; `enable_thinking=false` via `chat_template_kwargs` renders a
  pre-closed think block with zero reasoning. **No effort-level control exists** (explicit absence).

## 3. Context / memory geometry — envelope COMPLETE

| Rung (tokens) | Disposition | Evidence |
|---|---|---|
| 8,192 | near-full perf | 99.32% occ; prefill 8,329 tok/s |
| 16,384 | near-full perf | 99.30% occ; prefill 7,939 tok/s |
| 32,768 | ON BUDGET_LIMITED ×2 / OFF VALIDATED ×2 | occ 99.26/99.34%; depth err ≤0.499 pp |
| 65,536 | ON BUDGET_LIMITED ×2 / OFF VALIDATED ×2 | occ 99.05/99.34%; depth err ≤0.156 pp |
| 131,072 | ON BUDGET_LIMITED ×2 / OFF VALIDATED ×2 | occ 99.05%; depth err ≤0.150 pp; load 9,268 MiB, 2,589 free |
| 262,144 | **FIT_LIMIT** | bounded attempt: cudaMalloc OOM — KV request 9,216 MiB |
| 1,048,576 (exact native max) | **FIT_LIMIT** | bounded attempt: cudaMalloc OOM — KV request 38,654,705,664 B |
| Official extension | EXPLICIT ABSENCE | no YaRN/rope-scaling documented anywhere official |

- KV constant measured-exact: **36,864 B/token f16** = 2 × 9 full-attn layers × 4 KV heads ×
  256 × 2 B. Fit ceiling under this profile: **131,072 tokens**; the vendor's 1M claim is
  EXTERNAL_REPORTED and structurally out of reach on 12 GB with f16 KV (KV alone 3.16× the card).
- MODEL-CARD CONTEXT ENVELOPE COMPLETE: YES — every rung and the exact native maximum carry
  completed dispositions (VALIDATED / BUDGET_LIMITED / perf / FIT_LIMIT).
- **USEFUL_CONTEXT_MAX_SEMANTIC = 131,072** on the predeclared thinking-off non-starving lane
  (2/2 seeds; all six gates PASS at ≥99% occupancy; max depth error 0.150 pp).
- **USEFUL_CONTEXT_MAX_OPERATIONAL = none passing under the canonical profile**: thinking
  consumes the 512-token reserve at every rung (BUDGET_LIMITED ×6 runs); retrieval capability is
  intact (OFF lanes + semantic lane); the reserve-vs-thinking interaction is the blocker. The
  thinking-off lane is a declared alternative lane, not a separately fully characterized profile.

## 4. Reliability and quality (frozen contract, canonical profile)

- Reliability gate: **DO_NOT_ADVANCE** under the canonical vendor-default profile — operational
  lane **0/20 COMPLETE on BOTH seeds** (40/40 finish=length): thinking exhausts the frozen
  20–256-token ceilings before any answer channel opens. Adaptive third seed not triggered
  (0/20 is decisive). 0 UNSAFE on every lane.
- Predeclared semantic lane (2,048 ceiling): seed 42 **15/15 evaluable clean** (5 truncated);
  seed 314159 **15/18 clean** (2 truncated + 1 empty). Failures: one fabricated nonexistent git
  flag (single seed, truncated channel — NOT replicated), one exact-format miss, one missing
  pushback.
- Thinking-off diagnostic (same tiny ceilings, seed 42): 9/20 COMPLETE, 7/10 evaluable clean —
  capability present, ceilings binding.
- Quality screen (frozen 12, temp 0): canonical ON 1/12 (11 budget-starved NOT_EVALUABLE);
  thinking-off diagnostic **10/12** (Q06 2-words-vs-3 constraint miss; Q12 degenerate 2-token
  early stop).

## 5. Capability modules (frozen budgets)

Reasoning PASS (exact `TOTAL HOURS: 4`) · Coding PASS (executable oracle; 400 thinking-off
canonical + 1,500 thinking-on diagnostic) · Native tools PASS (exact `get_weather` call + args +
grounded continuation) · Structured interfaces PASS. OMP local-agent NOT_TESTED; vision N/A
(text-only). All applicable modules PASS.

## 6. LocalMaxxing disposition

**SUBMITTED** (origin NEW, 2026-09-22 terminal closeout): the canonical llama-bench arm above is
recorded on the LocalMaxxing service as
[`cmudarhyh0aw9lq018zug8yna`](https://www.localmaxxing.com/api/speed-tests/cmudarhyh0aw9lq018zug8yna)
(APPROVED; tokSOut 126.14, tokSPrefill 9,275.99, prompt 512, output 128, 5 reps; Q8_0, upstream
llama.cpp `b04d4e5` b10999, RTX 5070). Duplicate audit: NO_EXACT_MATCH (exhaustive authenticated
history of 35 user submissions with a control record verified present; zero Spark entries locally,
in history, or in the public listing). `verifiedRun: false` recorded honestly (llama-bench local
mode cannot supply prompt/output/engine-timing capture). Campaign close (2026-09-20) was
MEASURED_NOT_SUBMITTED per that campaign's Stage-A boundary; no service contact occurred during
the campaign itself.

## 7. Findings (claim classes)

1. **Thinking mode dominates budget behavior (MEASURED).** 300–800+ reasoning tokens even for
   trivial factual tasks; every frozen operational ceiling (20–256) and the standardized 512
   reserve are consumed by reasoning, leaving empty answer channels → NOT_EVALUABLE /
   BUDGET_LIMITED, never semantic FAIL.
2. **Thinking-off flips the practical surface (MEASURED).** Instant short answers, 10/12 quality,
   VALIDATED useful context at 32K/64K/128K — a materially different deployment surface, preserved
   as a declared lane (candidate secondary profile, see testing debt).
3. **Greedy-decode repetition loops (MEASURED, diagnostic).** At temp 0 + thinking, absent-evidence
   probes can spiral (8,100-token non-terminating loop); vendor sampling escapes cleanly.
4. **Fabrication surface is narrow but real (MEASURED).** One fabricated nonexistent git flag in a
   truncated channel (single seed); absent-information grounding otherwise excellent (exact
   `NOT STATED` refusals).
5. **Geometry is favorable but 1M is off the table on 12 GB (MEASURED+DERIVED).** 131K usable
   ceiling; 36,864 B/token f16 KV; SWA bounds long-context cost.
6. **Long-context throughput is the deployment story (MEASURED).** ~4,300 tok/s prefill at 128K,
   126 tok/s decode, 26.6 ms short TTFT.
7. **UNKNOWN/EXTERNAL_REPORTED kept separate:** vendor benchmark table, 1M claim, 200+ languages,
   MOPD training narrative — none locally validated.

## 8. Classification and scope

Campaign execution is COMPLETE_PASS; the model classification is **READY_WITH_GUARDRAILS** —
semantics ACCEPTABLE on the predeclared non-starving lane, but BUDGET_DISCIPLINE POOR on the
vendor-default profile (0/20 reliability completions on both seeds; 512-token reserve consumed at
every tested rung). It is not READY (practical rung not validated on the canonical reasoning
state) and not NOT_READY (a completing declared lane exists with acceptable semantics). The
deployment lesson: vendor-default reasoning behavior is budget-sensitive; thinking-off is a
materially different practical surface; the measured useful-context envelope on this hardware
(131,072 tokens) is not equivalent to the model-card native maximum (1,048,576).

## 9. Testing debt recorded at event close

(1) Full thinking-off secondary profile campaign (candidate
`spark25-4b-q8-0-llamacpp-thinking-off`); (2) KV quant (Q8 KV) geometry sweep toward 256K fit;
(3) OMP local-agent module; (4) multi-day soak at 32K; (5) greedy-mode thinking-loop
characterization. All five are optional/specialized follow-up work under current WELP; none is
required for this campaign's terminal validity.

## 10. Publication chronology

Executed and closed 2026-09-20/21 under measurement snapshot
`welp-next-snapshot-2026-09-19-methodology-revision` (public WELP commit
`79f9de13de04325e50e05b0eed28b56471a19028`) with frozen contracts, fixtures, and scorer; retained
locally through the then-applicable two-stage human-acceptance gate, which the 2026-09-22
execution-state lifecycle (`welp-next-snapshot-2026-09-22-automatic-closeout-lifecycle`,
`methodology_changed: NO`) superseded before terminal closeout. Published to
`WumboLabs/evaluations` at terminal closeout (see the registry event record for the exact evidence
commit). No eval-* repository exists or was created.
