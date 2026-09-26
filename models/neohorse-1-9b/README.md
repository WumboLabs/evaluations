<!-- Generated from registry metadata — do not hand-edit. -->

# NeoHorse-1-9B

**Classification:** READY_WITH_GUARDRAILS

**Recommended profile:** `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off`

**Context:** First fresh-model WELP campaign under the model-agentic snapshot (case C: both reasoning profiles required and measured on the same frozen task set). Both profiles classify READY_WITH_GUARDRAILS (R-C6/R-C7) with divergent dimension shapes, published independently and never averaged: Reasoning On (publisher default) SEMANTIC=ACCEPTABLE with reasoning-driven budget exhaustion (7/60 truncated) and R7 negative; Reasoning Off SEMANTIC=STRONG with 1.000 completion, R7 pass, reliability gate ADVANCE, but a truthful-reporting FAIL in Repository Repair. Useful context 65536 both profiles (FIT_LIMIT beyond on 12 GB). Agentic: 2 of 3 task classes scored (Research PASS; Repository FAIL on a false verification claim); the System class is INTEGRATION_BLOCKED by a deterministic frozen-harness defect (cause recorded, WELP unmodified).

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/neohorse-1-9b/)

## Profiles

- [neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on](profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on/) — current; llama.cpp (upstream); TokenRhythm/NeoHorse-1-9B-GGUF@ddcb4c93 :: NeoHorse-1-9B-Q8_0.gguf (sha256 519869730bda973ec50bb3ac42cd874569e5f3a57c3e0d5d23a2b5040e93310f)
- [neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off](profiles/neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-off/) — current-alternate; llama.cpp (upstream); TokenRhythm/NeoHorse-1-9B-GGUF@ddcb4c93 :: NeoHorse-1-9B-Q8_0.gguf (sha256 519869730bda973ec50bb3ac42cd874569e5f3a57c3e0d5d23a2b5040e93310f)

## Testing history

- 2026-09-25 — [First fresh-model WELP campaign under the model-agentic snapshot: full Model science of the publisher-default Reasoning On profile; case C measured (Reasoning Off sibling required)](events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/) — READY_WITH_GUARDRAILS; [neohorse-1-9b-rtx5070-welp-reasoning-on-20260925](events/neohorse-1-9b-rtx5070-welp-reasoning-on-20260925/REPORT.md)
- 2026-09-25 — [Full WELP characterization of the Reasoning Off deployment profile: independent setup/calibration, same frozen task set, dual-profile completion of the case-C model](events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/) — READY_WITH_GUARDRAILS; [neohorse-1-9b-rtx5070-welp-reasoning-off-20260925](events/neohorse-1-9b-rtx5070-welp-reasoning-off-20260925/REPORT.md)
- 2026-09-25 — [First fresh-model WELP Agentic event: dual-adapter qualification, three required task classes with two scored (1 PASS / 1 FAIL) and the system class INTEGRATION_BLOCKED by a deterministic frozen-harness defect](events/neohorse-1-9b-rtx5070-welp-agentic-20260925/) — READY_WITH_GUARDRAILS; [neohorse-1-9b-rtx5070-welp-agentic-20260925](events/neohorse-1-9b-rtx5070-welp-agentic-20260925/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
