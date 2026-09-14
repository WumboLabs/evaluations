# WumboLabs evaluation records — Qwen3.6-35B-A3B

Canonical public evidence for WumboLabs testing of **Qwen3.6-35B-A3B** (Alibaba (Qwen team)) — profile `qwen3.6-35b-a3b-llamacpp-ud-iq2-m`.

- **Tested artifact:** unsloth Qwen3.6-35B-A3B UD-IQ2_M GGUF (11,522,702,304-byte fingerprint)
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current (practical-use benchmark evidence; not a WELP characterization)

## Findings (bounded)

Scored 233.9/300 (3.9 avg) on wumbolabs-practical-use-v1 at 8k (shared v025 pool comparison) with a tight 12GB fit: 11,551 MiB peak VRAM, 676 MiB minimum headroom. Re-run under LLMGauge v0.71 for tool-version continuity; also the payload for the fit-ladder E2E (32k/16k/8k attempts). Practical-use benchmark evidence only.

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
