# WumboLabs evaluation records — Qwen3.8-9B (Empero)

Canonical public evidence for WumboLabs testing of **Qwen3.8-9B (Empero)** (empero-ai (Qwen3.8 derivative)) — profile `qwen3.8-9b-empero-vendor-battery`.

- **Tested artifact:** empero-ai/Qwen3.8-9B-GGUF@760121cd70bb4c36b2b5ec58eb765e0df5987efe (Q8_0) + base Q4 lane
- **Runtime / hardware:** llama.cpp / vLLM (WumboJetsII RTX 5070 12GB)
- **Profile status:** specialized surface (vendor-alignment battery; not a WELP characterization)

## Findings (bounded)

LLMGauge vendor-alignment qualification battery on the 9B artifact (Q8_0 full generic-core lane plus base Q4 agent-backend lane at vendor 8192). Specialized benchmark evidence; no quality verdict is claimed.

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
