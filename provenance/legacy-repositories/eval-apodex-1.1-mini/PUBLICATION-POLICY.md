# Publication policy — `apodex-1.1-mini` (-> WumboLabs/eval-apodex-1.1-mini)

## Artifact classification

### PUBLIC (safe to publish as text)
- README.md
- report.md
- MODEL.md
- model-manifest.json
- PUBLICATION-POLICY.md
- publication-policy.json
- WLEP-CONFORMANCE.md
- protocol-findings.md
- contracts/
- scorers/
- protocol-snapshot/
- publication/
- results/
- summaries/
- localmaxxing/ (IDs/status/performance/repro summary only)
- scripts/ (commands)
- calibration/
### EXCLUDED_INITIAL_RELEASE / DO_NOT_PUBLISH
- sources/ (EXCLUDED_INITIAL_RELEASE; excluded wholesale; no per-file source review performed)
- omp/ (OMP session internals)
### LOCAL_ONLY (never published - local tooling/binaries/caches)
- models/ (symlink -> ../../models/apodex-1.1-mini/artifacts, never tracked)
- runtime/ (bundled llama.cpp incl. ggml-vocab tokenizer files)
- logs/
- telemetry/ raw host paths
- private machine identifiers

## Model binaries
No model GGUF weights are stored under this campaign root; `models/` is a relative symlink into `models/<slug>/artifacts/` (qwen holds only `inventory.md` plus evidence symlinks). Symlink targets MUST be excluded from any public repo tree. See `model-manifest.json` for SHA-256 provenance only.

## Secret scan
2026-08-26 pattern scan — CLEAN, zero matches. `sources/` is excluded wholesale from the initial public release; no per-file source review was performed.

## LocalMaxxing
APPROVED speed (182.31 t/s, cmt9ijytg00xali017f46xk25); accidental duplicate cmt9imzoz00xfli01g5tzz3kx disclosed; benchmark suites NOT_SUBMITTED (early Phase-3 stop).

## WumboCore
Classification for this model's Lab Record: READY.
