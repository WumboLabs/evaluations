# Bonsai 2 27B — current-WELP characterization on RTX 5070 12 GB (PrismML PTQ1_0, llama.cpp fork)

- **Event ID:** `bonsai2-27b-rtx5070-welp-20260918`
- **Event date:** 2026-09-18
- **Model:** Ternary Bonsai 2 27B (`prism-ml/Ternary-Bonsai-2-27B-gguf`, PrismML)
- **Profile:** `bonsai2-27b-ptq1-0-prism-llamacpp` (reasoning-on vendor default; immutable historical profile)
- **Hardware:** RTX 5070 12 GB (primary); RTX 2060 SUPER 8 GB (portability supplement)
- **Outcome:** **PASS — scientific completion** under its recorded WELP snapshot
- **Classification:** **NOT_READY** for unguarded daily-driver/agent duty under the default reasoning-on profile
- **Supplements:** compression-retention study vs a practical Qwen3.8-27B reference; RTX 2060 SUPER portability

All measurements below are MEASURED unless labeled otherwise. This is the public-safe scientific
record; the retained local campaign bundle (`research/model-evaluations/bonsai-2-27b/bonsai-2-27b-rtx5070-welp-characterization-2026-09-18`)
governs on any conflict. A 2026-09-20 methodology-revision supplement characterizes a separate
thinking-off profile (`bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`, READY_WITH_GUARDRAILS);
this event is unchanged by it.

## 1. Tested artifact and runtime

- Exact artifact: `Ternary-Bonsai-2-27B-PTQ1_0.gguf`, **5,946,648,928 bytes**, SHA-256
  **`53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3`** — exact official LFS
  identity (`prism-ml/Ternary-Bonsai-2-27B-gguf` @ `6ed5e12bf84b7a63069882c91dd9e9218647d17b`,
  Apache-2.0, PrismML launch 2026-09-17).
- Pack: PTQ1_0 (GGML type 143, **1.75 bpw ternary, group 128**), Hadamard-rotated basis
  (`prism.hadamard.*`, normalized sylvester-walsh-hadamard, block 1024). Base lineage:
  Qwen3.8-27B (`general.architecture=qwen35`, 64 blocks ≈ 75% linear attention,
  n_ctx_train 262,144 MEASURED from file).
- Runtime: **PrismML-Eng/llama.cpp `9a9394a895b96003ca842a6041cb28ac49a108f7`**
  (release `prism-b10709-9a9394a`, GPG-verified), isolated SM120 build; the same source built
  SM75 for the RTX 2060 SUPER lane. **Stock llama.cpp never executed any PTQ1_0 science.**
- Semantic admission: PTQ1_0 recognized (402 ternary tensors), Hadamard metadata consumed,
  coherent generation, known-answer factual + reasoning smoke, strict JSON, absent-evidence
  grounding — all PASS, deterministic re-runs, 0 CUDA/OOM/Xid.

## 2. Canonical profile and performance (RTX 5070)

Full GPU residency (`-ngl 99`), FA on, FP16 KV, single slot, vendor instruct sampler
(0.7/0.8/20/presence 1.5), default context **32,768** (guarded 65,536), reasoning ON (vendor
xhigh default).

- llama-bench canonical arm (5 reps): **pp512 586.54 ± 2.52; tg128 59.22 ± 0.10 tok/s**.
- Short TTFT (uncached) median 278.7 ms; ~3.6K-token prompt TTFT 6,366 ms (prefill 568.7 tok/s).
- Near-full prefill curve 575 → 520 tok/s (8K→64K); full-occupancy decode 55 → 42 tok/s.
  Prefill, not decode, is the practical bottleneck on Blackwell for PTQ1_0.
- Vendor 5090 throughput claims (120.5 tg128) are EXTERNAL_REPORTED anchors, not quality evidence.

## 3. Quality, capabilities, reliability

| Surface | Result |
|---|---|
| Quality screen (frozen 12-task, temp 0) | **12/12** |
| Reliability (frozen 20-task × seeds 42/314159, default thinking) | **4/20, 3/20**; finish=length 19/20, 20/20 — xhigh thinking exhausts frozen 140–256-token caps; traces coherent (budget exhaustion, not fabrication) |
| Diagnostics | per-request budget ignored (19/20 identical outputs); effort medium + server budget ineffective; enable_thinking=false: 8/20 |
| Reasoning probe / coding / native tools / structured interfaces | PASS; coding is budget-bound at canonical cap (thinking-off 400-cap PASS, 1500-cap thinking-on PASS) |

Reliability gate fails under the frozen contract → **NOT_READY**, replicated across two seeds
and five bounded re-configurations. Failure mode: budget-vs-reasoning interaction (Mellum2
Thinking precedent), not garbage output; 0 UNSAFE.

## 4. Context envelope — COMPLETE

| Rung | Disposition |
|---|---|
| 8,192 / 16,384 / 32,768 | VALIDATED near-full ×2 (99.38–99.63% occupancy); 32K also **useful-context 2/2 seeds** |
| 65,536 | near-full perf ×2 PASS; useful-context FAILED 1/2 (frozen 512-token reserve exhausted in thinking; correct facts visible in trace; thinking-off diagnostic passed all gates in 40 tokens) |
| 98,304 / 131,072 / 262,144 (exact native max) | FIT_LIMIT (measured-anchored memory accounting; no launch) |
| Official extension | EXPLICIT ABSENCE pinned (PrismML advertises native 262,144 only) |

**USEFUL_CONTEXT_MAX = 32,768** under the frozen contract. PRACTICAL_PROFILE = 32K default /
65K guarded. Every rung and exact maximum carries a completed disposition.

## 5. LocalMaxxing disposition

**SUBMITTED** (origin NEW, 2026-09-21 terminal closeout): the canonical llama-bench arm above
is recorded on the LocalMaxxing service as
[`cmuajqjjd09y4lq01wrf8ht0j`](https://www.localmaxxing.com/api/speed-tests/cmuajqjjd09y4lq01wrf8ht0j)
(APPROVED; tokSOut 59.22, tokSPrefill 586.54, prompt 512, output 128, 5 reps; PTQ1_0,
PrismML fork `9a9394a8`, RTX 5070). Duplicate audit: NO_EXACT_MATCH (all pre-existing service
entries for this model are PQ2_0 on RTX 3090/2080 Ti hardware). `verifiedRun: false` recorded
honestly (llama-bench local mode cannot supply prompt/output/engine-timing capture).
Campaign close (2026-09-18) was MEASURED_NOT_SUBMITTED per that campaign's boundary; no
service contact occurred during the campaign itself.

## 6. Compression-retention supplement (vs practical Qwen3.8-27B reference)

Paired mechanical study, 48 instances, Bonsai PTQ1_0 vs the practical UD-Q2_K_XL Qwen3.8
reference (NOT "full precision"): 31 PRESERVED_CORRECT, 5 DEGRADED_TO_WRONG (2 truly semantic),
4 IMPROVED, 8 BOTH_WRONG (cap-truncation parity). No retention percentage manufactured;
PrismML's 98.2% vendor claim remains EXTERNAL_REPORTED and incomparable method-for-method.

## 7. RTX 2060 SUPER portability supplement

Same artifact (SHA-verified) + same pinned fork source (SM75 build): full-GPU residency at 8K,
pp512 250.6 / tg128 19.9 tok/s, 16K fit-edge capacity, 12/12 semantic-parity agreement
(9 byte-identical), zero errors. Practical single-user assistant on 8 GB Turing: YES at 8K;
long-context/throughput: NO.

## 8. Classification and scope

**NOT_READY** applies to the reasoning-on profile under the prior snapshot: practical
recommendation is guarded enthusiast deployment only (32K context, reasoning disabled or
strictly bounded, never trust strict one-shot outputs or nonexistent-API claims without
verification). The 2026-09-20 supplement adds the separately profiled thinking-off result
(READY_WITH_GUARDRAILS); neither profile represents "Bonsai 2" universally.

## 9. Testing debt recorded at event close

reliability budget-parity re-run; 64K useful re-validation under an accepted budget policy;
bounded PQ2_0 packing comparison; OMP agent module; vision module. (The first two were
resolved by the 2026-09-20 methodology-revision supplement.)

## 10. Publication chronology

Executed and closed 2026-09-18 under its recorded per-campaign protocol snapshot
`welp-next-snapshot-2026-09-18-bonsai-2-27b-rtx5070-welp-characterization`
(WELP `9e3f0afbdfb767148f1612e307bb0150dbe23302`) with the campaign's frozen contracts;
retained locally through the human science gate; published to `WumboLabs/evaluations` at the
human publication gate (see the registry event record for the exact evidence commit). No
eval-* repository exists or was created.
