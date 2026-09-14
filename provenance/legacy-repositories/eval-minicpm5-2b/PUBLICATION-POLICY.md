# Publication policy — `minicpm5-2b` (WumboLabs/eval-minicpm5-2b)

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
— submission `cmtwcna5907f0ps01sfiwd60a`
— APPROVED, origin NEW (localmaxxing-backfill-2026-09-10); benchmarked on the canonical practical stack (BF16, vLLM contained runtime, 32K default — not the 131K fp8 boundary); actual prompt tokens 252 (endpoint usage); verifiedRun false reflects a client capture limitation

## Claim boundary
Official BF16 full-precision characterization on a contained vLLM runtime, READY_WITH_GUARDRAILS: 32K default / 64K guarded, complete 131K model-card envelope (98K highest BF16-KV rung; exact 131K FIT_LIMIT on BF16-KV and strict-gate FAILED on the authorized fp8-KV surface), 118.6 tok/s decode, thinking/coding/tools PASS, 20/20 reliability.
Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings. Canonical
scientific authority is the local WELP campaign evidence for `minicpm5-2b-rtx5070-welp-characterization-2026-09-10`.
