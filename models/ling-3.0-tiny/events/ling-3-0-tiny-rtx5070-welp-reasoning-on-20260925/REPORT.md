# Ling 3.0 Tiny — Reasoning On Re-derivation (RTX 5070)

Artifact role: PRIMARY SCIENTIFIC REPORT
Campaign: `ling-3.0-tiny-rtx5070-welp-reasoning-on-2026-09-25`
Status: CURRENT — campaign execution **COMPLETE_PASS** (reuse/re-derivation
event; no new inference); terminal model classification **NOT_READY (R-C3)**,
re-derived and validator-approved under
`welp-next-snapshot-2026-09-25-reasoning-profiles`.

Run fingerprint: 2026-09-25; ZERO new scored requests — every behavioral byte
is the retained, hash-bound evidence of the source event
`ling-3.0-tiny-rtx5070-welp-characterization-2026-09-24`; classification,
gate and context summary re-derived from those bytes by `harness/bundle.py`.

## Executive summary

This event completes the **Reasoning On** side of the Ling-3.0-tiny
reasoning-profiles validation under the new methodology
(`welp-reasoning-topology-0.1.0-draft`, case C). The source event's complete
Reasoning On campaign (COMPLETE_PASS / NOT_READY under the
context-outcome-repair snapshot) remains immutable; per the reuse policy, its
retained raw evidence is scientifically compatible with the new methodology
for the same effective reasoning state, so nothing was rerun "merely to
populate a new schema". The classification was **re-derived, not
grandfathered**: `harness/bundle.py evaluate_bundle` re-derived
**NOT_READY (R-C3)** — SEMANTIC_CAPABILITY=WEAK · BUDGET_DISCIPLINE=GOOD ·
CONTEXT_USABILITY=VALIDATED · INTEGRATION_QUALITY=CLEAN — from the retained
bytes, and the full validator (including reasoning-profile rules R18-R21)
accepts the event.

## Identity

| Field | Value |
|---|---|
| Reasoning profile | Reasoning On (`reasoning-on`); requested ON, effective ON (retained reverify) |
| Topology | case C; publisher/default = Reasoning On; this is the default-profile event |
| Profile ID | `ling-3-0-tiny` profile `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment` (unchanged from the source event) |
| Reasoning group | `ling-3-0-tiny-reasoning-profiles` — sibling: Reasoning Off event `ling-3-0-tiny-rtx5070-welp-reasoning-off-20260925` (complete) |
| Artifact / runtime / hardware | identical to the sibling; explicitly marked profile-invariant records |
| WELP snapshot | `welp-next-snapshot-2026-09-25-reasoning-profiles` @ `193cb64` (DRAFT / NOT v1.0) |

## Reuse dispositions (full matrix: `REUSE-MIGRATION.md`)

- REUSE: all retained behavioral evidence (80 reliability rows, 28 context
  cells, capability runs, quality screens, blinded reviews, performance
  arms) — byte-identical, hash-bound copies with per-section provenance
  records in the evidence document.
- RE-DERIVED: gate, context summary and classification (required by the
  policy; never grandfathered).
- INCOMPARABLE: any Reasoning Off evidence — deliberately absent (validator
  R19 rejects cross-profile behavioral binding).
- MUST_RERUN: none — the methodology adds reasoning-profile identity, not new
  measurement requirements for this state.

## Classification (re-derived)

**NOT_READY (R-C3)** — equal to the source event's verdict, now derived under
the new snapshot from retained bytes with reasoning-profile identity.
Dimensions: SEMANTIC_CAPABILITY=WEAK (reasoning-budget starvation of the
semantic lane, 14/40 truncations) · BUDGET_DISCIPLINE=GOOD ·
CONTEXT_USABILITY=VALIDATED (practical rung 32768; useful-context maximum
262144 with measured seed-dependent dips at 128K/192K) ·
INTEGRATION_QUALITY=CLEAN.

## Comparison pointer

The per-profile comparison (verdict, dimensions, budget discipline, context,
modules, performance, deployment guidance) lives in the sibling Reasoning Off
campaign's `REPORT.md` and `COMPARISON.md` at the model level. This event and
the sibling are independent profiles; no averaged model-level verdict exists.

## LocalMaxxing

`SUBMITTED` / `VERIFIED_EXISTING` — the engine-native benchmark record
`cmugffasg0dohlq01bekesaf0` (APPROVED) covers both reasoning profiles because
the benchmark does not exercise the reasoning control; re-verified live at
closeout.

## Testing debt

- REQUIRED CURRENT-WELP: zero.
- OPTIONAL/SPECIALIZED: none added by this event beyond the sibling's list.
- NOT_APPLICABLE: none.

## Protocol findings

Zero new findings: this event performed no inference and modified no
methodology. METHODOLOGY_DEFECT: 0. (The methodology motivation — missing
historical Reasoning Off characterization — is documented by the new
snapshot, not counted as a finding here.)
