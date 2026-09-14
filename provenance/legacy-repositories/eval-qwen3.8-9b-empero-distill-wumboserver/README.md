# WumboLabs evaluation records — Qwen3.8-9B (Empero Distill)

Canonical public evidence for WumboLabs testing of **Qwen3.8-9B (Empero Distill)** (empero-ai (Qwen3.8 derivative)) — profile `qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver`.

- **Tested artifact:** empero-ai/Qwen3.8-9B-Distill-GGUF Q4_K_M / Q5_K_M / Q6_K
- **Runtime / hardware:** llama.cpp on WumboServer (NVIDIA RTX 2060 SUPER 8GB)
- **Profile status:** benchmark-only surface (hardware-lane evidence; not a WumboJetsII WELP result)

## Findings (bounded)

Hardware-lane quant ladder: admission benchmark (Q5), Q6 fit boundary, Q5 serving campaign, and LocalMaxxing reconciliation. Reference LMX numbers: 9B Q4_K_M 60.4 tok/s out at 5.37 GB peak VRAM, 177 W. Not comparable to WumboJetsII RTX 5070 results.

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
