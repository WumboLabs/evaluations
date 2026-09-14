# Publication policy — `qwen3.8-27b` (-> WumboLabs/eval-qwen3.8-27b)

## Artifact classification

### PUBLIC (allowlist only)
- `README.md`, `MODEL.md`, model/revision manifest, policy, allowlist, release manifest, and `.gitignore`
- `reports/`
- `manifests/`
- LocalMaxxing public IDs/status in `README.md`
- `evidence/inventory/` (hashes/comparisons text)
- `notes/continuation-notes.md`

### EXCLUDED_INITIAL_RELEASE / DO_NOT_PUBLISH
- `sources/` — excluded wholesale; no per-file redaction review was performed
- `runtime/`, `logs/`, `telemetry/`, `models/`, raw evidence directories, raw host telemetry, local caches, credentials, and all symlinked artifact targets
- `evaluations/sharp-dflash/`, `notes/resource-incidents.md`, and OMP working material

## Model binaries
No model GGUF weights are stored under this campaign root; `models/` is a relative symlink into `models/<slug>/artifacts/` (qwen holds only `inventory.md` plus evidence symlinks). Symlink targets MUST be excluded from any public repo tree. See `model-manifest.json` for SHA-256 provenance only.

## Secret scan
Publication-surface scans are recorded in `migration/secret_scan.json`; no secret values are recorded in publication reports. `sources/` is excluded wholesale for the initial release.

## LocalMaxxing
APPROVED speed x2 (cmt3jngze0njfmv0133xpneeu, cmt3jp2cn0njpmv01t5u8m6wd); benchmark suite APPROVED/PUBLIC; ref cmsv68xl3085ims01w8aeacig.

## WumboCore
Classification for this model's Lab Record: `COMPLETED_DEEP_EVALUATION`, with guarded/limited deployment suitability under the tested configuration; not recommended as an unguarded daily driver or unattended autonomous agent.
