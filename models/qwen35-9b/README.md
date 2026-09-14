<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3.5-9B

**Classification:** No model-level classification published

**Recommended profile:** `qwen35-9b-llamacpp-q8`

**Context:** practical_default_tokens: 32768; guarded_tokens: 65536; native_maximum_tokens: 262144; extension_mechanism: "YaRN factor 4.0 (officially advertised to 1,010,000 tokens)"; envelope_complete: true; native_maximum_disposition: "FIT_LIMIT - native maximum 262,144 on the Q8_0/f16 primary surface (arithmetic lower bound) and on the authorized q4_0-KV alternate surface (measured admission failure); official YaRN 1,010,000 maximum FIT_LIMIT at every representable KV precision"; exact_max_dispositions: {"native_262144_f16_primary": "FIT_LIMIT — arithmetic lower bound: weights + f16 KV = 16,237.0 MiB > 12,227 MiB total VRAM", "native_262144_q4_0_alternate": "FIT_LIMIT — measured admission failure (compute buffer 1,336.28 MiB cudaMalloc OOM with weights + 2,304.00 MiB q4_0 KV resident)", "yarn_1010000": "FIT_LIMIT — exceeds total VRAM at every representable KV precision; mechanism representation separately confirmed (freq_scale 0.25)"}; highest_measured_admitted: {"primary_f16_tokens": 65536, "note": "highest measured/admitted near-full primary rung; 98,304 projected below the frozen 1,024 MiB operational floor and therefore not launched; exact physical ceiling between the two values not bracketed"}; useful_context_finding: "At 99.49-99.56% near-full occupancy both rechecked rungs retrieve all five planted values exactly at 2/25/50/75/95% depths (max placement error 0.104 pp), resist the decoy, retain synthesis and the checksum instruction, but emit the absent-information value under the wrong key name; strict useful-context gate FAILED at both rungs, both seeds. Compared with the same-family 4B control (which dropped synthesis/absent/checksum entirely), 9B retains more auxiliary instructions at the same occupancy; two model sizes do not establish causality"; notes: "32K default and 64K guarded profile both reevaluated at the current WELP near-full standard and confirmed; occupied 32K performance 7.8 s TTFT / 60.0 tok/s decode; 64K 17.5 s TTFT / 54.1 tok/s decode"

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen35-9b/)

## Profiles

- [qwen35-9b-llamacpp-q8](profiles/qwen35-9b-llamacpp-q8/) — current; llama.cpp; Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth rev 3885219b6810b007914f3a7950a8d1b469d598a5)

## Testing history

- 2026-09-11 — [Context envelope completion](events/context-envelope-completion-2026-09-11-qwen35-9b/) — READY_WITH_GUARDRAILS; [context-envelope-completion-2026-09-11-qwen35-9b](events/context-envelope-completion-2026-09-11-qwen35-9b/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
