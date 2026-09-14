# Publication policy — `gemma4-e4b` (WumboLabs/eval-gemma4-e4b)

## Artifact classification

### PUBLIC (allowlist only)
- `README.md`, `EVIDENCE-SUMMARY.md`, `website-publication.json`, `MODEL.md`,
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
— submission `cmtwgcs7c097sps01sdq9ihbu`
— SUBMITTED once, origin NEW, service APPROVED (in-campaign, 2026-09-11); verifiedRun null — the service returned no verification state and the client could not transmit verification fields; recorded honestly, not claimed as verified; actual prompt tokens 77 (endpoint usage); tokSPrefill 1,322.5

## Claim boundary
Official Google QAT Q4_0 + mmproj on llama.cpp, READY_WITH_GUARDRAILS: 32K default / 131K guarded with the full card envelope complete; perfect five-needle retrieval through the exact 131,072 maximum while the strict aggregate gate FAILED at every rung. Vision, multi-image, ASR, AST and bounded video PASS; OCR TESTED_LIMITED; reliability 20/20 completion, 14/20 exactness.
Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings. Canonical
scientific authority is the local WELP campaign evidence for `gemma4-e4b-rtx5070-welp-characterization-2026-09-10`.
