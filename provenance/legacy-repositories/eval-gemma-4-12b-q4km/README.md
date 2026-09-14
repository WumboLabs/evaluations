# WumboLabs evaluation records — Gemma 4 12B IT

Canonical public evidence for WumboLabs testing of **Gemma 4 12B IT** (Google) — profile `gemma-4-12b-llamacpp-q4km`.

- **Tested artifact:** ggml-org/gemma-4-12b-it-GGUF Q4_K_M
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** benchmark-only surface

## Findings (bounded)

Benchmark-only surface: LMX local speed evidence 72.11 tok/s out (llama.cpp). No quality suite was run on this quant.

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
