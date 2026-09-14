<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3.5-4B

**Classification:** No model-level classification published

**Recommended profile:** `qwen35-4b-llamacpp-bf16`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 65,536 tokens; Model-card native maximum: 262,144 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

practical_default_tokens: 32768; guarded_tokens: 65536; native_maximum_tokens: 262144; extension_mechanism: "YaRN factor 4.0 (officially advertised to 1,010,000 tokens)"; envelope_complete: true; native_maximum_disposition: "FIT_LIMIT - native maximum 262,144 on the BF16/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision"; exact_max_dispositions: {"native_262144_f16_primary": "FIT_LIMIT — arithmetic lower bound: weights + f16 KV = 16,215.7 MiB > 12,227 MiB total VRAM", "native_262144_q4_0_alternate": "FIT_LIMIT — measured admission failure (compute buffer 1,330.28 MiB cudaMalloc OOM with weights+KV resident)", "yarn_1010000": "FIT_LIMIT — exceeds total VRAM at every representable KV precision; mechanism representation separately confirmed (freq_scale 0.25)"}; highest_measured_admitted: {"primary_f16_tokens": 65536, "note": "highest measured/admitted near-full primary rung; 98,304 projected below the frozen 1,024 MiB operational floor and therefore not launched; exact physical ceiling between the two values not bracketed"}; useful_context_finding: "At 99.4-99.5% near-full occupancy both rechecked rungs retrieve all five planted values exactly at 2/25/50/75/95% depths (max placement error 0.092 pp) and resist the decoy, while deterministically dropping the auxiliary synthesis/absent/checksum output instructions; strict useful-context gate FAILED at both rungs, both seeds"; notes: "32K default and 64K guarded profile both reevaluated at the current WELP near-full standard and confirmed; occupied 32K performance 6.6-6.7 s TTFT / 60.3 tok/s decode; 64K 15.2 s TTFT / 54.1-54.4 tok/s decode"

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen35-4b/)

## Profiles

- [qwen35-4b-llamacpp-bf16](profiles/qwen35-4b-llamacpp-bf16/) — current; llama.cpp; Qwen3.5-4B-BF16.gguf (text-only conversion; Unsloth rev e87f176479d0855a907a41277aca2f8ee7a09523)

## Testing history

- 2026-09-11 — [Context envelope completion](events/context-envelope-completion-2026-09-11-qwen35-4b/) — READY_WITH_GUARDRAILS; [context-envelope-completion-2026-09-11-qwen35-4b](events/context-envelope-completion-2026-09-11-qwen35-4b/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
