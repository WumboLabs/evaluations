# WumboLabs evaluation records — Mellum2 12B-A2.5B (Instruct)

Canonical public evidence for WumboLabs testing of **Mellum2 12B-A2.5B (Instruct)** (JetBrains) — profile `mellum2-12b-a2.5b-llamacpp-q4km-instruct`.

- **Tested artifact:** JetBrains/Mellum2-12B-A2.5B-Instruct-GGUF-Q4_K_M
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current specialized surface (agent-backend fit test; not a WELP characterization)

## Findings (bounded)

64k agent-backend fit CONFIRMED (5/5 complete, 251.0-257.2 tok/s generation, 1603.1-2187.6 tok/s prompt eval, 9203 MiB peak VRAM, 3024 MiB headroom). Manual review: preferred over Thinking (overall trust 3.7/5), extremely fast and 64k-stable, but NOT safe for unsupervised shell/systemd operations. Practical-use score 239.9/300. LMX local speed 261.41 tok/s out. This is a specialized agent-backend test, not a general model-quality verdict.

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
