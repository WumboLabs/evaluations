<!-- Generated from registry metadata — do not hand-edit. -->

# Ternary Bonsai 2 27B

**Classification:** READY_WITH_GUARDRAILS / PROFILE-SCOPED (thinking-off recommended; reasoning-on historical NOT_READY)

**Recommended profile:** `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 65,536 tokens; Model-card native maximum: 262,144 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

practical_default_tokens: 32768; guarded_tokens: 65536; native_maximum_tokens: 262144 (FIT_LIMIT: f16 KV + weights exceed 12 GB card memory at the exact native maximum); envelope_complete: true; useful context is PROFILE-SCOPED: thinking-off USEFUL_CONTEXT_MAX_SEMANTIC = USEFUL_CONTEXT_MAX_OPERATIONAL = 65,536 (VALIDATED 2/2 seeds, 512-token reserve); reasoning-on operational = 32,768 (VALIDATED 2/2) with 65K BUDGET_LIMITED (1/2 seeds, EXHAUSTED_IN_REASONING) and no 65K semantic measurement. Capacity and retrieval were intact at 65K on both profiles; the reasoning-on budget interaction was the blocker.

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/bonsai2-27b/)

## Profiles

- [bonsai2-27b-ptq1-0-prism-llamacpp](profiles/bonsai2-27b-ptq1-0-prism-llamacpp/) — historical; llama.cpp (PrismML-Eng fork); prism-ml/Ternary-Bonsai-2-27B-gguf@6ed5e12b :: Ternary-Bonsai-2-27B-PTQ1_0.gguf (sha256 53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3)
- [bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off](profiles/bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off/) — current; llama.cpp (PrismML-Eng fork); prism-ml/Ternary-Bonsai-2-27B-gguf@6ed5e12b :: Ternary-Bonsai-2-27B-PTQ1_0.gguf (sha256 53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3)

## Testing history

- 2026-09-20 — [Methodology-revision supplement (thinking-off profile)](events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/) — READY_WITH_GUARDRAILS; [bonsai2-27b-rtx5070-welp-methodology-supplement-20260920](events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/REPORT.md)
- 2026-09-18 — [Current-WELP characterization + compression-retention + RTX 2060 SUPER portability](events/bonsai2-27b-rtx5070-welp-20260918/) — NOT_READY; [bonsai2-27b-rtx5070-welp-20260918](events/bonsai2-27b-rtx5070-welp-20260918/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
