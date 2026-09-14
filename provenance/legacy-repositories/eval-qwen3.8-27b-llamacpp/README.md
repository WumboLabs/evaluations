# eval-qwen3.8-27b-llamacpp

Canonical WumboLabs evaluation repository for the **historical llama.cpp
tested profile** of Qwen3.8-27B
(`qwen38-27b-llamacpp-ud-q2-k-xl`: Unsloth UD-Q2_K_XL GGUF on llama.cpp
b10449, WumboJetsII / RTX 5070 12GB).

Established 2026-09-12 by the WumboLabs model/profile/event publication-identity
milestone. The evidence in `reports/`, `manifests/`, `MODEL.md`,
`model-manifest.json`, and the inventory metadata was imported **byte-identical**
from `WumboLabs/eval-qwen3.8-27b` (the original publication repository, commit
`54b14b3` era, where the historical evaluation was first published and where it
remains preserved). See [MIGRATION.md](MIGRATION.md) for the per-file
provenance and SHA-256 verification record.

## Contents (evidence events)

- **initial-evaluation-2026-08-21** — complete WELP end-to-end deep evaluation
  (campaign 2026-08-14..21). Classification `COMPLETED_DEEP_EVALUATION`;
  guarded/limited deployment suitability; strong reviewed local
  coding/technical assistant. Historical model-role findings (reliability,
  strict interfaces, native tools, bounded 64K context) are canonical HERE for
  the model and are not superseded by the current serving profile.

## Profile identity

- `profile.json` — `wumbolabs-eval-profile/1` descriptor for this profile.
- Current status: `historical` — the current canonical serving profile is the
  ExLlamaV3 H1 surface, canonical at
  [eval-qwen3.8-27b-exl3-h1](https://github.com/WumboLabs/eval-qwen3.8-27b-exl3-h1).
- Original mixed repository (preserved historical archive):
  [eval-qwen3.8-27b](https://github.com/WumboLabs/eval-qwen3.8-27b).

> Manual scores and reviews are bounded evidence, not universal quality
> rankings. This repository contains reproducibility metadata and reports, not
> model artifacts, raw telemetry, runtime trees, or acquisition sources.
