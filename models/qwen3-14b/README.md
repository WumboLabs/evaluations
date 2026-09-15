<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3-14B

**Classification:** READY_WITH_GUARDRAILS

**Recommended profile:** `qwen3-14b-llamacpp-q4km-q8kv`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 32,768 tokens; Model-card native maximum: 32,768 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

native_maximum_tokens: 32768; native_maximum_disposition: "VALIDATED — near-full performance (99.2-99.6% occupancy, 2 reps) and useful-context PASS at two seeds (99.47% occupancy) plus the 2026-09-15 five-depth completion (2/25/50/75/95% placements inside the preferred 0.25pp bound, max error 0.160/0.087 pp) on the canonical q8_0-KV surface"; practical_default_tokens: 32768; guarded_tokens: 32768; envelope_complete: true; notes: "Native rungs 8K/16K/32K VALIDATED. Official YaRN extension (factor 4.0, exact max 131,072) is FIT_LIMIT on 12GB: measured cudaMalloc OOM at q8_0 KV (10,880 MiB request) and at the lowest dtype q4_0 (5,760 MiB request); nearest measured boundary 32,768. Attribution: RTX 5070 12GB, not the model."

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen3-14b/)

## Profiles

- [qwen3-14b-llamacpp-q4km](profiles/qwen3-14b-llamacpp-q4km/) — benchmark-only; llama.cpp; unsloth/Qwen3-14B-GGUF Q4_K_M
- [qwen3-14b-ollama-q4km-wumbo](profiles/qwen3-14b-ollama-q4km-wumbo/) — practical-use; Ollama; unsloth/Qwen3-14B-GGUF Q4_K_M (custom qwen3-14b-wumbo Ollama tag; 9,001,753,376-byte weights fingerprint)
- [qwen3-14b-llamacpp-q4km-q8kv](profiles/qwen3-14b-llamacpp-q4km-q8kv/) — current; llama.cpp; unsloth/Qwen3-14B-GGUF Q4_K_M (9,001,753,376-byte Q4_K_M; sha256 712c0791d5124d3dd6d1e4968de1201207afeae49c6e10fbeb9c58fe00c58555)

## Testing history

- 2026-09-14 — [Current-WELP recharacterization](events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/) — READY_WITH_GUARDRAILS; [qwen3-14b-rtx5070-welp-recharacterization-2026-09-14](events/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/REPORT.md)
- 2026-07-15 — [Fit-ladder success-fallback E2E (LLMGauge feature validation)](events/qwen3-14b-fit-ladder-2026-07-15/) — SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION; [qwen3-14b-fit-ladder-2026-07-15](events/qwen3-14b-fit-ladder-2026-07-15/REPORT.md)
- 2026-07-05 — [LMX speed run](events/qwen3-14b-lmx-speed-2026-07-05/) — BENCHMARK_ONLY (LMX local speed); [qwen3-14b-lmx-speed-2026-07-05](events/qwen3-14b-lmx-speed-2026-07-05/REPORT.md)
- 2026-07-04 — [12B practical pool comparison v025 + Grug](../../shared-events/practical-use-comparison-2026-07-04/) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical); [gemma4-12b-practical-pool-v025-2026-07-04](../../shared-events/practical-use-comparison-2026-07-04/REPORT.md)
- 2026-05-07 — [Practical daily-driver evaluation (Ollama era, qwen3-14b-wumbo tag)](events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/) — PRACTICAL_USE / PRE_WELP_HISTORICAL; [qwen3-14b-wumbo-daily-evaluation-2026-05-07](events/qwen3-14b-wumbo-daily-evaluation-2026-05-07/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
