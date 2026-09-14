# WumboLabs evaluation records — Qwen2.5-3B Instruct

Canonical public evidence for WumboLabs testing of **Qwen2.5-3B Instruct** (Alibaba (Qwen team)) — profile `qwen2.5-3b-vllm-bf16`.

- **Tested artifact:** Qwen/Qwen2.5-3B-Instruct BF16
- **Runtime / hardware:** vLLM (WumboJetsII RTX 5070 12GB)
- **Profile status:** benchmark-only surface (cross-runtime methodology lane)

## Findings (bounded)

vLLM BF16 lane of the LLMGauge cross-runtime comparison (agent-backend-v1 at 8k incl. failed-command-recovery probe) plus a vLLM runtime-fingerprint smoke. Benchmark-only methodology-lane evidence; the canonical comparison report lives in the llama.cpp F16 lane repository.

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
