# Publication policy — `qwen35-9b` (WumboLabs/eval-qwen3.5-9b)

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
— submission `cmtwcn79807eups01faxxmyr1`
— APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); verifiedRun false reflects a client capture limitation; actual prompt tokens 266 (endpoint usage)

## Claim boundary
Medium-fit Q8_0 quantized control (BF16 cannot fit), READY_WITH_GUARDRAILS: 32K default / 64K guarded, 66.7 tok/s short decode, 7/7 constrained quality and 20/20 reliability. 2026-09-11 context-envelope completion (append-only follow-up in `reports/`): MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES — native 262,144 FIT_LIMIT (f16 primary lower bound; q4_0 alternate measured admission failure), YaRN 1,010,000 FIT_LIMIT at every representable KV precision, highest measured/admitted near-full primary context 65,536 (not the absolute runtime maximum; 98,304 projected below the frozen safety floor and not launched); at near-full occupancy planted-target retrieval is perfect while the strict useful-context gate FAILED 0/4 (absent-information value correct but returned under the wrong key name); free-form grounding cautions apply.
Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings. Canonical
scientific authority is the local WELP campaign evidence for
`qwen35-9b-rtx5070-baseline-2026-09-09` and the append-only completion campaign
`qwen35-9b-rtx5070-context-completion-2026-09-11` (authoritative for context claims).
