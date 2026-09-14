# Publication policy — `qwen35-4b` (WumboLabs/eval-qwen3.5-4b)

## Artifact classification

### PUBLIC (allowlist only)
- `README.md`, `EVIDENCE-SUMMARY.md`, `reports/**`, `website-publication.json`, `MODEL.md`,
  `model-manifest.json`, this policy, the allowlist, the release manifest, and `.gitignore`

### DO_NOT_PUBLISH (default)
- `sources/`, `runtime/`, `logs/`, `telemetry/`, `models/`, caches, credentials,
  raw prompt logs, host telemetry, and anything not explicitly allowlisted.

## Model binaries
No model weights are stored in this repository. `model-manifest.json` records
the tested artifact identity (description + SHA-256) for provenance only.

## Secret scan
All publication files were scanned for credential-like material and local
absolute paths before publication; no secret values are recorded here.

## LocalMaxxing
SUBMITTED
— submission `cmtwcmm3207eqps01w7fubuuw`
— APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); verifiedRun false reflects a client capture limitation, recorded honestly; actual prompt tokens 266 (endpoint usage)

## Claim boundary
Comfortable-fit BF16 text control, READY_WITH_GUARDRAILS on the RTX 5070: 32K default / 64K guarded, 67.9 tok/s short decode, 7/7 constrained quality and 20/20 reliability. 2026-09-11 context-envelope completion (append-only follow-up in `reports/`): MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES — native 262,144 FIT_LIMIT (f16 primary lower bound; q4_0 alternate measured admission failure), YaRN 1,010,000 FIT_LIMIT at every representable KV precision, highest measured/admitted near-full primary context 65,536 (not the absolute runtime maximum; 98,304 projected below the frozen safety floor and not launched); strict useful-context gate FAILED 0/4 at near-full occupancy while planted-target retrieval was perfect; free-form grounding cautions apply.
Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings. Canonical
scientific authority is the local WELP campaign evidence for
`qwen35-4b-rtx5070-baseline-2026-09-09` and the append-only completion campaign
`qwen35-4b-rtx5070-context-completion-2026-09-11` (authoritative for context claims).
