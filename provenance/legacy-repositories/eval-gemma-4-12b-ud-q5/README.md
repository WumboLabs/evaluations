# WumboLabs evaluation records — Gemma 4 12B IT

Canonical public evidence for WumboLabs testing of **Gemma 4 12B IT** (Google) — profile `gemma-4-12b-llamacpp-ud-q5-k-xl`.

- **Tested artifact:** unsloth/gemma-4-12b-it-GGUF UD-Q5_K_XL
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current-alternate (practical-use benchmark evidence; not a WELP characterization)

## Findings (bounded)

Second-strongest 12B Gemma variant tested: 254.0/300 manual practical score (4.23 avg) on wumbolabs-practical-use-v1 at 8k, behind the QAT Q4_0 artifact on the same suite; LMX local speed 62.76 tok/s out. Practical-use benchmark evidence only.

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
