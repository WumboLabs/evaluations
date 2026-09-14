# WumboLabs evaluation records — Qwen3-14B

Canonical public evidence for WumboLabs testing of **Qwen3-14B** (Alibaba (Qwen team)) — profile `qwen3-14b-llamacpp-q4km`.

- **Tested artifact:** unsloth/Qwen3-14B-GGUF Q4_K_M
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current (practical-use benchmark evidence; not a WELP characterization)

## Findings (bounded)

Scored 228.4/300 (3.81 avg) on wumbolabs-practical-use-v1 at 8k (shared v025 pool comparison); LMX local speed 66.57 tok/s out. Also served as the payload for the LLMGauge fit-ladder success-fallback E2E. Practical-use benchmark evidence only.

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
