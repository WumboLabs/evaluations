<!-- Generated from registry metadata — do not hand-edit. -->

# Gemma 4 12B IT

**Classification:** READY_WITH_GUARDRAILS

**Recommended profile:** `gemma-4-12b-llamacpp-qat-q4-0`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 131,072 tokens; Model-card native maximum: 262,144 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

native_maximum_tokens: 262144; native_maximum_disposition: "FIT_LIMIT — measured: one bounded admission attempt failed with CUDA OOM (compute buffer) and KV-slope accounting (17.4 KiB/token) proves the point cannot fit with required reserve on 12GB; nearest measured boundary 131,072"; practical_default_tokens: 32768; guarded_tokens: 131072; envelope_complete: true; notes: "Native rungs 8K/16K/32K/64K/128K VALIDATED (near-full performance; useful-context at 131,072 with 2 seeds, all gates passing at 99.5% occupancy). Official extensions: NONE documented on official cards (EXTERNAL_REPORTED)."

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/gemma-4-12b/)

## Profiles

- [gemma-4-12b-llamacpp-qat-q4-0](profiles/gemma-4-12b-llamacpp-qat-q4-0/) — current; llama.cpp; google/gemma-4-12b-it-qat-q4_0-gguf (QAT UD-Q4_K_XL packaging)
- [gemma-4-12b-llamacpp-ud-q6-k-xl](profiles/gemma-4-12b-llamacpp-ud-q6-k-xl/) — benchmark-only; llama.cpp; unsloth/gemma-4-12b-it-GGUF UD-Q6_K_XL
- [gemma-4-12b-llamacpp-q4km](profiles/gemma-4-12b-llamacpp-q4km/) — benchmark-only; llama.cpp; ggml-org/gemma-4-12b-it-GGUF Q4_K_M
- [gemma-4-12b-llamacpp-ud-q5-k-xl](profiles/gemma-4-12b-llamacpp-ud-q5-k-xl/) — practical-use; llama.cpp; unsloth/gemma-4-12b-it-GGUF UD-Q5_K_XL

## Testing history

- 2026-09-12 — [Current-WELP recharacterization](events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/) — READY_WITH_GUARDRAILS; [gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12](events/gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12/REPORT.md)
- 2026-07-04 — [12B practical pool comparison v025 + Grug](../../shared-events/practical-use-comparison-2026-07-04/) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical); [gemma4-12b-practical-pool-v025-2026-07-04](../../shared-events/practical-use-comparison-2026-07-04/REPORT.md)
- 2026-07-04 — [LMX speed runs across four Gemma 4 12B quants](events/gemma4-12b-lmx-speed-2026-07-04/) — BENCHMARK_ONLY (LMX local speed); [gemma4-12b-lmx-speed-2026-07-04](events/gemma4-12b-lmx-speed-2026-07-04/REPORT.md)
- 2026-06-21 — [12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable)](../../shared-events/practical-use-comparison-2026-06-21/) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical); [gemma4-12b-practical-use-family-2026-06-21](../../shared-events/practical-use-comparison-2026-06-21/REPORT.md)
- 2026-06-21 — [Honesty ladder smoke (QAT Q4)](events/gemma4-12b-honesty-ladder-2026-06-21/) — SPECIALIZED_TEST / UNSCORED_SMOKE; [gemma4-12b-honesty-ladder-2026-06-21](events/gemma4-12b-honesty-ladder-2026-06-21/REPORT.md)
- 2026-06-16 — [Early core-v1 + agent-backend-v1 scored runs (QAT Q4)](events/gemma4-12b-core-agent-v016-2026-06-16/) — BENCHMARK_ONLY; [gemma4-12b-core-agent-v016-2026-06-16](events/gemma4-12b-core-agent-v016-2026-06-16/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
