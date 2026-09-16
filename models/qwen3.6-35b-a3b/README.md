<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3.6-35B-A3B

**Classification:** LIMITED_ROLE_ONLY

**Recommended profile:** `qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv`

**Context:** practical_default_tokens: 32768; guarded_tokens: 16384; native_maximum_tokens: 262144; envelope_complete: true; native_maximum_disposition: "FIT_LIMIT on the current RTX 5070 12GB/q8_0-KV text profile: measured ~12.9 KiB/token KV growth and 512 MiB reserve make 262,144 exceed available VRAM; nearest measured boundary 32,768 VALIDATED"; exact_max_dispositions: {"native_262144": "FIT_LIMIT on this hardware/profile", "yarn_1010000": "FIT_LIMIT on this hardware/profile"}; highest_measured_admitted: {"tokens": 32768, "note": "tight-fit only; 433 MiB remaining after near-full request; no concurrent GPU workload"}; useful_context_finding: "Two 32K seeds pass all required 2/25/50/75/95% depths at 99.48-99.49% usable occupancy (31,961-31,964 tokens)"; notes: "Canonical validated maximum is 32K; guarded practical limit is 16K. Official model is multimodal, but current --no-mmproj text profile is SUPPORTED_NOT_CHARACTERIZED for vision. Reliability is 9/20 in each seed including Git safety 0/1."

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen3-6-35b-a3b/)

## Profiles

- [qwen3.6-35b-a3b-llamacpp-ud-iq2-m](profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m/) — historical; llama.cpp; unsloth Qwen3.6-35B-A3B UD-IQ2_M GGUF (11,522,702,304-byte fingerprint)
- [qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv](profiles/qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv/) — current; llama.cpp; Qwen3.6-35B-A3B-UD-IQ2_M.gguf (11,522,702,304-byte UD-IQ2_M; sha256 2be7ef1ed7e1af8b10d3829102cf9a6c2bd5ddb64d675b4ece23a60799403d43)

## Testing history

- 2026-09-15 — [Current-WELP recharacterization](events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/) — LIMITED_ROLE_ONLY; [qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15](events/qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
- 2026-07-22 — [LLMGauge v0.71 practical re-run](events/qwen36-35b-practical-v071-2026-07-22/) — BENCHMARK_ONLY (TOOL_VERSION_RERUN); [qwen36-35b-practical-v071-2026-07-22](events/qwen36-35b-practical-v071-2026-07-22/REPORT.md)
- 2026-07-15 — [Fit-ladder E2E (LLMGauge feature validation)](events/qwen36-35b-fit-ladder-e2e-2026-07-15/) — SPECIALIZED_TEST / TOOL_FEATURE_VALIDATION; [qwen36-35b-fit-ladder-e2e-2026-07-15](events/qwen36-35b-fit-ladder-e2e-2026-07-15/REPORT.md)
- 2026-07-04 — [12B practical pool comparison v025 + Grug](../../shared-events/practical-use-comparison-2026-07-04/) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical); [gemma4-12b-practical-pool-v025-2026-07-04](../../shared-events/practical-use-comparison-2026-07-04/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
