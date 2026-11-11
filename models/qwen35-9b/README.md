<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3.5-9B

**Classification:** No model-level classification published

**Recommended profile:** `qwen35-9b-llamacpp-q8`

**Context:** Practical default: 16,384 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

practical_default_tokens: 32768; guarded_tokens: 65536; native_maximum_tokens: 262144; extension_mechanism: "YaRN factor 4.0 (officially advertised to 1,010,000 tokens)"; envelope_complete: true; native_maximum_disposition: "FIT_LIMIT - native maximum 262,144 on the Q8_0/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision"; exact_max_dispositions: {"native_262144_f16_primary": "FIT_LIMIT — arithmetic lower bound: weights + f16 KV = 16,237.0 MiB > 12,227 MiB total VRAM", "native_262144_q4_0_alternate": "FIT_LIMIT — measured admission failure (compute buffer 1,336.28 MiB cudaMalloc OOM with weights + 2,304.00 MiB q4_0 KV resident)", "yarn_1010000": "FIT_LIMIT — exceeds total VRAM at every representable KV precision; mechanism representation separately confirmed (freq_scale 0.25)"}; highest_measured_admitted: {"primary_f16_tokens": 65536, "note": "highest measured/admitted near-full primary rung; 98,304 projected below the frozen 1,024 MiB operational floor and therefore not launched; exact physical ceiling between the two values not bracketed"}; useful_context_finding: "At 99.49-99.56% near-full occupancy both rechecked rungs retrieve all five planted values exactly at 2/25/50/75/95% depths (max placement error 0.104 pp), resist the decoy, retain synthesis and the checksum instruction, but emit the absent-information value under the wrong key name; strict useful-context gate FAILED at both rungs, both seeds. Compared with the same-family 4B control (which dropped synthesis/absent/checksum entirely), 9B retains more auxiliary instructions at the same occupancy; two model sizes do not establish causality"; notes: "32K default and 64K guarded profile both reevaluated at the current WELP near-full standard and confirmed; occupied 32K performance 7.8 s TTFT / 60.0 tok/s decode; 64K 17.5 s TTFT / 54.1 tok/s decode"

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen35-9b/)

## Profiles

- [qwen35-9b-llamacpp-q8](profiles/qwen35-9b-llamacpp-q8/) — current; llama.cpp; Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth rev 3885219b6810b007914f3a7950a8d1b469d598a5)
- [qwen35-9b-r9700-hip-on-2026-10-22](profiles/qwen35-9b-r9700-hip-on-2026-10-22/) — current; llama.cpp (HIP); Q4_K_M (Unsloth publisher GGUF) :: revision unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8 :: sha256 03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8
- [qwen35-9b-rtx5070-cuda-on-2026-11-06](profiles/qwen35-9b-rtx5070-cuda-on-2026-11-06/) — current; llama.cpp (CUDA); Q4_K_M (Unsloth publisher GGUF) :: revision unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8 :: sha256 03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8
- [qwen35-9b-rtx5070-cuda-lc-on-2026-11-06](profiles/qwen35-9b-rtx5070-cuda-lc-on-2026-11-06/) — current; llama.cpp (CUDA); Q4_K_M (Unsloth publisher GGUF) :: revision unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8 :: sha256 03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8
- [qwen35-9b-rtx5070-cuda-atu-on-2026-11-06](profiles/qwen35-9b-rtx5070-cuda-atu-on-2026-11-06/) — current; llama.cpp (CUDA); Q4_K_M (Unsloth publisher GGUF) :: revision unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8 :: sha256 03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8
- [qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08](profiles/qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08/) — current; llama.cpp (CUDA); Q4_K_M (Unsloth publisher GGUF) :: revision unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8 :: sha256 03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8

## Testing history

- 2026-11-08 — [Qwen3.5-9B runtime performance (RTX 5070 CUDA, deployment-attributed)](events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08](events/qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08/REPORT.md)
- 2026-11-06 — [Qwen3.5-9B scored Agentic M3 — research and repository (genuine negatives)](events/qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06](events/qwen35-9b-rtx5070-cuda-m3-scored-remaining-2026-11-06/REPORT.md)
- 2026-11-06 — [Qwen3.5-9B scored Agentic M3 — readiness and system (RTX 5070 CUDA, thinking-on)](events/qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06](events/qwen35-9b-rtx5070-cuda-m3-scored-2026-11-06/REPORT.md)
- 2026-11-06 — [Qwen3.5-9B advanced tool-use specialist (RTX 5070 CUDA, thinking-on)](events/qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06](events/qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06/REPORT.md)
- 2026-11-06 — [Qwen3.5-9B advanced reasoning specialist (RTX 5070 CUDA, thinking-on)](events/qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06](events/qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06/REPORT.md)
- 2026-11-06 — [Qwen3.5-9B advanced long-context specialist (RTX 5070 CUDA, thinking-on)](events/qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06](events/qwen35-9b-rtx5070-cuda-advanced-long-context-2026-11-06/REPORT.md)
- 2026-11-06 — [Qwen3.5-9B advanced coding specialist (RTX 5070 CUDA, thinking-on)](events/qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06/) — NOT_ASSIGNED; [qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06](events/qwen35-9b-rtx5070-cuda-advanced-coding-2026-11-06/REPORT.md)
- 2026-10-22 — [Qwen3.5-9B reference Model/Core baseline (Radeon R9700 HIP, thinking-on)](events/qwen35-9b-r9700-hip-m2-geometry-2026-10-22/) — NOT_ASSIGNED; [qwen35-9b-r9700-hip-m2-geometry-2026-10-22](events/qwen35-9b-r9700-hip-m2-geometry-2026-10-22/REPORT.md)
- 2026-09-11 — [Context envelope completion](events/context-envelope-completion-2026-09-11-qwen35-9b/) — READY_WITH_GUARDRAILS; [context-envelope-completion-2026-09-11-qwen35-9b](events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
