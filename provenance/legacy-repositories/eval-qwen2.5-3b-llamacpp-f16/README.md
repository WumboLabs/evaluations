# WumboLabs evaluation records — Qwen2.5-3B Instruct

Canonical public evidence for WumboLabs testing of **Qwen2.5-3B Instruct** (Alibaba (Qwen team)) — profile `qwen2.5-3b-llamacpp-f16`.

- **Tested artifact:** Qwen2.5-3B-Instruct F16 GGUF (6,178,317,312-byte fingerprint)
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** benchmark-only surface (cross-runtime methodology lane)

## Findings (bounded)

llama.cpp F16 lane of the LLMGauge cross-runtime comparison against vLLM BF16 (agent-backend-v1 at 8k incl. a second failed-command-recovery probe). Primary subject is cross-runtime methodology; the Qwen2.5-3B measurements are retained as its benchmark-only evidence. An Arch-era quant-lab record set (F16/Q8_0/Q6_K/Q5_K_M/Q4_K_M/IQ4_XS) is additionally cited by the 2026-08-14 model archaeology.

## Contents

| File | Content |
|---|---|
| [`EVIDENCE-SUMMARY.md`](EVIDENCE-SUMMARY.md) | per-event evidence summaries |
| [`events/`](events/) | one public-safe evidence derivative per testing event |
| [`profile.json`](profile.json) | profile identity descriptor (schema `wumbolabs-eval-profile/1`) |
| [`provenance.json`](provenance.json) | retained-source identity + SHA-256 for every published claim |

## Shared comparison evidence

This repository carries the canonical public copy of a shared multi-model
comparison report. Related model repositories link here instead of duplicating it:

- [`shared/compare-qwen25-3b-f16-vs-vllm-bf16-8k.md`](compare-qwen25-3b-f16-vs-vllm-bf16-8k.md) — byte-identical public-safe LLMGauge cross-runtime comparison report (canonical copy)

## Claim boundary

All evidence here is benchmark-only, practical-use, or specialized testing. It is NOT:
a WELP characterization, a universal model ranking, or a production-readiness proof.
Results are bounded by the tested artifact, runtime, hardware, suite, and settings.

## License / attribution

The evaluated model weights remain under their upstream license; no weights are
redistributed here. The evaluation evidence in this repository is WumboLabs work
product.
