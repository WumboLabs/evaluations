# WumboLabs evaluation records — Grug 12B

Canonical public evidence for WumboLabs testing of **Grug 12B** (kai-os) — profile `grug-12b-llamacpp-q4km`.

- **Tested artifact:** kai-os/Grug-12B-GGUF Q4_K_M
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current (practical-use benchmark evidence; not a WELP characterization)

## Findings (bounded)

Scored 243.6/300 (4.06 avg; 4 pass, 2 mixed) on wumbolabs-practical-use-v1 at 8k — structurally viable, but not a replacement for Gemma 4 12B QAT as the tested 12GB practical default. 66.65 tok/s avg generation, 8485 MiB peak VRAM. Honesty smoke and provenance-refresh re-run retained; LMX local speed 69.24 tok/s out.

## Contents

| File | Content |
|---|---|
| [`EVIDENCE-SUMMARY.md`](EVIDENCE-SUMMARY.md) | per-event evidence summaries |
| [`events/`](events/) | one public-safe evidence derivative per testing event |
| [`profile.json`](profile.json) | profile identity descriptor (schema `wumbolabs-eval-profile/1`) |
| [`provenance.json`](provenance.json) | retained-source identity + SHA-256 for every published claim |

## Claim boundary

All evidence here is benchmark-only, practical-use, or specialized testing. It is NOT:
a WELP characterization, a universal model ranking, or a production-readiness proof.
Results are bounded by the tested artifact, runtime, hardware, suite, and settings.

## License / attribution

The evaluated model weights remain under their upstream license; no weights are
redistributed here. The evaluation evidence in this repository is WumboLabs work
product.
