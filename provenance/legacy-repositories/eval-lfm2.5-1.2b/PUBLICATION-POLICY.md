# Publication policy — `lfm2.5-1.2b-qad` (-> WumboLabs/eval-lfm2.5-1.2b)

## Artifact classification

### PUBLIC (safe to publish as text)
- README.md
- report.md
- MODEL.md
- model-manifest.json
- PUBLICATION-POLICY.md
- publication-policy.json
- profiles/
- prompts/ (WumboLabs-authored test prompts)
- results/
- summaries/
- scripts/
- diagnostics/ (aggregate only)
### EXCLUDED_INITIAL_RELEASE / DO_NOT_PUBLISH
- sources/ (EXCLUDED_INITIAL_RELEASE; excluded wholesale; no per-file source review performed)
- coding-sandboxes/ (sandbox internals - review)
- telemetry/ raw host paths
### LOCAL_ONLY (never published - local tooling/binaries/caches)
- models/ (symlink -> ../../models/lfm2.5-1.2b/artifacts, never tracked)
- logs/

## Model binaries
No model GGUF weights are stored under this campaign root; `models/` is a relative symlink into `models/<slug>/artifacts/` (qwen holds only `inventory.md` plus evidence symlinks). Symlink targets MUST be excluded from any public repo tree. See `model-manifest.json` for SHA-256 provenance only.

## Secret scan
2026-08-26 pattern scan — CLEAN, zero matches. `sources/` is excluded wholesale from the initial public release; no per-file source review was performed.

## LocalMaxxing
NOT_APPLICABLE (no speed-test submission).

## WumboCore
Classification for this model's Lab Record: PARTIAL.
