<!-- Generated from registry metadata — do not hand-edit. -->

# Gemma 4 E4B

**Classification:** READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL

**Recommended profile:** `gemma4-e4b-llamacpp-qat-q4-0`

**Context:** practical_default_tokens: 32768; guarded_tokens: 131072; native_maximum_tokens: 131072; envelope_complete: true; native_maximum_disposition: "Exact native 131,072: measured FAILED on the strict aggregate useful-context gate while near-full performance itself was valid (both seeds 99.50% occupancy, TTFT ~38 s, decode ~79 tok/s, zero errors) and five-needle target retrieval stayed perfect (10/10 across ALL rungs including the exact maximum)"; notes: "Strict aggregate gate FAILED at every rung; divergence is explicit — content retrieval is perfect everywhere (decoy resistance 10/10), while strict output/instruction compliance is the failure surface (absent-field fills a present value instead of NOT_SPECIFIED; JSON tail truncation from 16K upward). No official context extensions exist for E4B (source-backed absence)."

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/gemma4-e4b/)

## Profiles

- [gemma4-e4b-llamacpp-qat-q4-0](profiles/gemma4-e4b-llamacpp-qat-q4-0/) — current; llama.cpp; gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release)

## Testing history

- 2026-09-10 — [Initial evaluation (full characterization)](events/initial-evaluation-2026-09-10-gemma4/) — READY_WITH_GUARDRAILS / CLOSED_WELP_CROSS_FAMILY_CONTROL; [initial-evaluation-2026-09-10-gemma4](events/initial-evaluation-2026-09-10-gemma4/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
