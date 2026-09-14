<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3.8-27B

**Classification:** COMPLETED_DEEP_EVALUATION

**Recommended profile:** `qwen38-27b-exl3-h1`

**Context:** practical_default_tokens: 65536; envelope_complete: true; native_maximum_disposition: "FIT_LIMIT - exact native maximum 262,144 on the accepted H1 ExLlamaV3 surface: requires 12,530 MiB at ready (8,178 MiB context-independent + 262,144 x 17,408 B/token KV) versus 12,227 MiB total card VRAM; nearest measured boundary 98,304 VALIDATED. Official YaRN 1,000,000 extension INTEGRATION_BLOCKED on the accepted surface (runtime 1.4.6 has the YaRN implementation but exposes no supported activation without editing the protected artifact config) and independently FIT_LIMIT (cache alone ~16.6 GiB, ~1.36x total card VRAM)"; tested_surfaces: ["65,536 near-full VALIDATED (2 seeds, 99.5% occupancy, strict useful-context 2/2)", "98,304 near-full VALIDATED (2 seeds, 99.49-99.52% occupancy, strict useful-context 2/2)", "131,072 / 196,608 / 262,144 FIT_LIMIT by frozen fit accounting", "official YaRN extension maximum 1,000,000 INTEGRATION_BLOCKED (no supported activation on the accepted surface without editing the protected artifact config; independently impossible: ~16.6 GiB cache alone)"]; headline_performance: "near-full prefill 606 tok/s at 65,536 and 537 tok/s at 98,304; full-occupancy decode 56-62 tok/s; near-full TTFT 107 s (65,536) and 181 s (98,304)"; guarded_tokens: 98304; native_maximum_tokens: 262144; extension_mechanism: "YaRN factor 4.0 (officially advertised to 1,000,000 tokens)"; exact_max_dispositions: {"native_262144": "FIT_LIMIT - hard lower-bound accounting under the frozen H1 profile (required-at-ready 12,530 MiB > 12,227 MiB total); nearest measured boundary 98,304 VALIDATED; rungs 131,072 and 196,608 FIT_LIMIT by the same accounting", "yarn_1000000": "INTEGRATION_BLOCKED on the accepted surface (no supported faithful activation path for the required rope_parameters on the pinned artifact/runtime); independently FIT_LIMIT (cache alone ~16.6 GiB)"}; highest_measured_admitted: {"tokens": 98304, "note": "highest measured/admitted near-full rung (= guarded boundary); 65,536 anchor also revalidated; above 98,304 the accepted H1 profile is FIT_LIMIT on this 12 GB card"}; useful_context_finding: "Strict useful-context aggregate 4/4 requests (2 rungs x 2 seeds) at >=99.4% occupancy: exact retrieval 5/5, synthesis, decoy resistance, absent-information grounding, and instruction compliance all 4/4 per rung; all 20 target-field observations at 2/25/50/75/95% depths within +/-0.036 pp"; notes: "near-full performance (client streaming proxies): 65,536 anchor ~606 tok/s prefill, 61-62 tok/s decode, ~107 s TTFT; 98,304 ~537 tok/s prefill, 56-57 tok/s decode, ~181 s TTFT"

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen38-27b/)

## Profiles

- [qwen38-27b-exl3-h1](profiles/qwen38-27b-exl3-h1/) — current; ExLlamaV3; Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3)
- [qwen38-27b-llamacpp-ud-q2-k-xl](profiles/qwen38-27b-llamacpp-ud-q2-k-xl/) — historical; llama.cpp; Unsloth Qwen3.8-27B UD-Q2_K_XL GGUF (Unsloth rev 27af057ecb382ddfea5d12837360a8980560e3ed)

## Testing history

- 2026-09-12 — [Context envelope completion](events/context-envelope-completion-2026-09-12/) — GUARDED / MODEL-CARD CONTEXT ENVELOPE COMPLETE; [context-envelope-completion-2026-09-12](events/context-envelope-completion-2026-09-12/REPORT.md)
- 2026-09-09 — [H1 deployment / canonical promotion](events/h1-canonical-promotion-2026-09-09/) — COMPLETE / CURRENT_CANONICAL_H1_PROFILE; [h1-canonical-promotion-2026-09-09](events/h1-canonical-promotion-2026-09-09/REPORT.md)
- 2026-08-21 — [Initial evaluation (deep evaluation, historical llama.cpp)](events/initial-evaluation-2026-08-21/) — COMPLETED_DEEP_EVALUATION; [initial-evaluation-2026-08-21](events/initial-evaluation-2026-08-21/REPORT.md)
- 2026-08-20 — [llama.cpp quant/variant showdown runs (LLMGauge era)](events/qwen38-27b-quant-showdowns-2026-08-20/) — PROFILE_OPTIMIZATION (historical llama.cpp lane; superseded by ExLlamaV3 H1); [qwen38-27b-quant-showdowns-2026-08-20](events/qwen38-27b-quant-showdowns-2026-08-20/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
