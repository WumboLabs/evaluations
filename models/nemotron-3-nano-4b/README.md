<!-- Generated from registry metadata — do not hand-edit. -->

# Nemotron 3 Nano 4B

**Classification:** READY_WITH_GUARDRAILS

**Recommended profile:** `nemotron-3-nano-4b-llamacpp-q4km`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 131,072 tokens; Model-card native maximum: 262,144 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

practical_default_tokens: 32768; guarded_tokens: 131072; native_maximum_tokens: 262144; extension_mechanism: "none — source-backed absence on both official model cards (the family 1M claim belongs to the 30B-A3B MoE sibling; the GGUF header value 1,048,576 is converter metadata, not a card claim)"; envelope_complete: true; native_maximum_disposition: "VALIDATED — capacity admitted, near-full performance measured (uncached prefill ~2,877 tok/s, decode ~79-81 tok/s, 7,268 MiB VRAM), strict useful-context PASS at both required seeds (42, 314159)"; exact_max_dispositions: {"native_262144": "VALIDATED at both seeds at >=99.48% near-full occupancy with depth-placement errors <= 0.21 pp", "official_extensions": "NONE exist (source-backed absence); nothing to disposition beyond the native maximum"}; useful_context_finding: "All five useful-context fields (exact retrieval, synthesis, decoy resistance, absent-information grounding, instruction/output compliance) passed the strict aggregate at every tested rung — 8,192 / 32,768 / 131,072 / 262,144 — including both native-maximum seeds. The tested frozen near-full context fixture passes strictly; this is not proof of universal long-document reasoning on arbitrary material"; notes: "Hybrid Mamba-2 memory model measured: 4 attention layers carry context-linear KV (~16 KiB/token f16); the 38 Mamba-2 layers carry a fixed context-independent recurrent state (~100-300 MiB). The full 262,144 slot fits in 7,268 MiB with 4,546 MiB free"

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/nemotron-3-nano-4b/)

## Profiles

- [nemotron-3-nano-4b-llamacpp-q4km](profiles/nemotron-3-nano-4b-llamacpp-q4km/) — current; llama.cpp; NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf (sole official quant; upstream rev ba223d14e45525f7fae81db77ea8cabeb2fc6c25)

## Testing history

- 2026-09-11 — [Current-WELP recharacterization](events/welp-recharacterization-2026-09-11/) — READY_WITH_GUARDRAILS; [welp-recharacterization-2026-09-11](events/welp-recharacterization-2026-09-11/REPORT.md)
- 2026-08-25 — [Initial evaluation (protocol development, PROTOCOL_BLOCKED)](events/initial-evaluation-2026-08-25/) — PARTIAL_PROTOCOL_DEVELOPMENT; [initial-evaluation-2026-08-25](events/initial-evaluation-2026-08-25/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
