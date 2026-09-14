# WumboLabs evaluation records — Qwen3.8-2B (Empero)

Canonical public evidence for WumboLabs testing of **Qwen3.8-2B (Empero)** (empero-ai (Qwen3.8 derivative)) — profile `qwen3.8-2b-empero-vllm-bf16`.

- **Tested artifact:** empero-ai/Qwen3.8-2B-GGUF (+ BF16)
- **Runtime / hardware:** llama.cpp / vLLM (WumboJetsII RTX 5070 12GB)
- **Profile status:** specialized surface (vendor-alignment battery; not a WELP characterization)

## Findings (bounded)

LLMGauge vendor-alignment qualification battery: full agent-backend-v1, coding-core-v1, core-v1, generic-core-v1, and practical suites at the vendor 8192 context, plus configured-context default probing from 4096 through 262144. Primary subject is LLMGauge vendor alignment; the model results are retained as specialized benchmark evidence. No quality verdict is claimed.

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
