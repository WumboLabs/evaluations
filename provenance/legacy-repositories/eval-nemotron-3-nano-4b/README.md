# nemotron-3-nano-4b

WumboLabs model-evaluation records for NVIDIA Nemotron 3 Nano 4B
(WumboJetsII host). This repository holds two evidence generations; neither
rewrites the other.

## Historical evaluation (2026-08-25) — preserved

- **Verdict:** PROTOCOL_BLOCKED at Phase 3 gate decision (12/12 screen; WELP defines no advancement threshold — finding F-01). Phases 0–2 passed: clean load/serve, ~178 t/s decode, ~6.5k t/s prefill. No generalization to a model review.
- **Full report:** `report.md` · machine index: `model-manifest.json`
- **Model binaries:** `models/` -> `../../models/nemotron-3-nano-4b/artifacts/` (compat symlink)
- **Publication:** see `PUBLICATION-POLICY.md` before any public exposure

## Current-WELP recharacterization (2026-09-11) — append-only follow-up

- **Outcome:** PASS — NEMOTRON3_NANO_4B_RTX5070_RECHARACTERIZED under the
  current WELP protocol, whose deterministic phase gates resolve the
  historical F-01 blockage.
- **Classification:** READY_WITH_GUARDRAILS (reliability is the guardrail:
  strong transport/runtime and bounded quality behavior alongside measurable
  adversarial hallucination/evidence-discipline defects).
- **Context envelope:** COMPLETE — native maximum **262,144 VALIDATED** at
  ≥99.49% near-full occupancy with the strict useful-context aggregate
  passing at both required seeds; official extensions: none (source-backed
  absence). Practical default 32,768 / guarded 131,072.
- **Architecture (corrected):** dense hybrid Mamba-2/MLP with 4 attention
  layers (`nemotron_h`) — not MoE; the MoE sibling is Nemotron 3 Nano
  30B-A3B.
- **Full report:**
  [`reports/nemotron3-nano-4b-welp-recharacterization-2026-09-11.md`](reports/nemotron3-nano-4b-welp-recharacterization-2026-09-11.md)
  · machine-readable publication export:
  [`website-publication.json`](website-publication.json)
- **LocalMaxxing:** SUBMITTED, origin VERIFIED_EXISTING
  (`cmt86gy1j000eli01ca3cwwn0`); zero new submissions.
