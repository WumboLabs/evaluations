# WumboLabs evaluation records — Qwen3-14B

Canonical public evidence for WumboLabs testing of **Qwen3-14B** (Alibaba (Qwen team)) — profile `qwen3-14b-ollama-q4km-wumbo`.

- **Tested artifact:** unsloth/Qwen3-14B-GGUF Q4_K_M (custom qwen3-14b-wumbo Ollama tag; 9,001,753,376-byte weights fingerprint)
- **Runtime / hardware:** Ollama (Vulkan, later CUDA) on WumboJetsII RTX 5070 12GB
- **Profile status:** historical (pre-WELP practical-use evidence, May 2026)

## Findings (bounded)

Historical pre-WELP practical evaluation of the custom qwen3-14b-wumbo Ollama tag: judged good enough for daily local technical-assistant use with conservative Docker/systemd/Arch tooling behavior and mandatory command review; 4096-context working guidance. A recorded May-era benchmark measured 63.74 tok/s generation with full CUDA offload. Practical-use evidence only; no WELP characterization exists.

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
