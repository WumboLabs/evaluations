<!-- Generated from registry metadata — do not hand-edit. -->

# Ling 3.0 Tiny

**Classification:** NOT_READY

**Recommended profile:** `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`

**Context:** Native 131,072-token context (config + GGUF measured); 262,144 advertised extension via YaRN x2.0 (model card, EXTERNAL_REPORTED; mechanism qualified on the pinned runtime). Measured on the 12 GB card with official Q8_0 (9,142 MiB at the native max): 32,768 configured practical context; Controlled Context coverage COMPLETE 28/28 across 8,192..262,144 at near-full occupancy (max placement error 0.374 pp), capability VALIDATED at the practical rung, useful-context maximum 262,144 both lanes by the frozen rule with a measured seed-dependent dip at 131,072/196,608 (native max PARTIAL). YaRN extension cells measured on mechanism-qualified arms. Classification NOT_READY (R-C3): SEMANTIC_CAPABILITY WEAK (reasoning starvation + strict-JSON fence wrapping; R7/R8 DO_NOT_ADVANCE), BUDGET_DISCIPLINE GOOD, CONTEXT_USABILITY VALIDATED, INTEGRATION_QUALITY CLEAN.

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/ling-3-0-tiny/)

## Profiles

- [ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment](profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment/) — current; llama.cpp (upstream); inclusionAI/Ling-3.0-tiny-GGUF@01b850e2 :: Ling-3.0-tiny-Q8_0.gguf (sha256 9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6)
- [ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off](profiles/ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/) — current-alternate; llama.cpp (upstream); inclusionAI/Ling-3.0-tiny-GGUF@01b850e2 :: Ling-3.0-tiny-Q8_0.gguf (sha256 9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6)

## Testing history

- 2026-09-25 — [Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference)](events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/) — NOT_READY; [ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925](events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/REPORT.md)
- 2026-09-25 — [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model](events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/) — NOT_READY; [ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925](events/ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925/REPORT.md)
- 2026-09-24 — [Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0)](events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/) — NOT_READY; [ling-3-0-tiny-rtx5070-welp-characterization-20260924](events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
