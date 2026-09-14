# eval-qwen3.8-27b-exl3-h1

Canonical WumboLabs evaluation repository for the **current canonical ExLlamaV3
H1 serving profile** of Qwen3.8-27B
(`qwen38-27b-exl3-h1`: `Qwen3.8-27B-SC_2.20bpw_H3_V3` EXL3 on ExLlamaV3 1.4.6,
H1 recurrent history, WumboJetsII / RTX 5070 12GB).

Established 2026-09-12 by the WumboLabs model/profile/event publication-identity
milestone. The evidence here was imported **byte-identical** from
`WumboLabs/eval-qwen3.8-27b` (the original publication repository, where it
remains preserved): the H1 profile evidence from commit `cc5a435` and the
context-envelope completion appended exactly as published at commit `78e8ebf`.
See [MIGRATION.md](MIGRATION.md) for per-file provenance and SHA-256
verification.

## Contents (evidence events, append-only)

- **h1-canonical-promotion-2026-09-09** — E18H candidate validation + E18I
  canonical promotion (`PASS — E18I_H1_CANONICAL_PROMOTION_COMPLETE`).
  [`reports/h1-canonical-profile-update.md`](reports/h1-canonical-profile-update.md)
- **context-envelope-completion-2026-09-12** — model-card context envelope
  COMPLETE on this surface (`PASS — QWEN38_27B_CONTEXT_ENVELOPE_COMPLETED`):
  65,536 default revalidated; 98,304 guarded boundary VALIDATED; native
  262,144 FIT_LIMIT on this 12 GB surface; official YaRN 1,000,000
  INTEGRATION_BLOCKED on the accepted surface and independently FIT_LIMIT.
  [`reports/qwen38-27b-context-envelope-completion-2026-09-12.md`](reports/qwen38-27b-context-envelope-completion-2026-09-12.md)
- `website-publication.json` — machine-readable record
  (`wumbolabs-labs-publication/1`), representing the context-envelope
  completion generation exactly as published.

## Profile identity

- `profile.json` — `wumbolabs-eval-profile/1` descriptor for this profile
  (status `current`).
- Historical llama.cpp profile of this model (historical model-role findings):
  [eval-qwen3.8-27b-llamacpp](https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp).
- Original mixed repository (preserved historical archive):
  [eval-qwen3.8-27b](https://github.com/WumboLabs/eval-qwen3.8-27b).

> H1 is canonical only for this exact artifact/runtime and text-only
> width1/batch1 surface. Historical model-role findings belong to the
> historical stack and are not superseded by this profile. Reports are bounded
> evidence, not universal quality rankings.
