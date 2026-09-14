# WumboLabs evaluation records — Gemmable 4 12B MTP

Canonical public evidence for WumboLabs testing of **Gemmable 4 12B MTP** (Mia-AiLab (Gemma 4 12B MTP derivative)) — profile `gemmable-4-12b-llamacpp-q4km`.

- **Tested artifact:** Mia-AiLab/Gemmable-4-12B-MTP-GGUF Q4_K_M
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current (practical-use benchmark evidence; not a WELP characterization)

## Findings (bounded)

Scored 119.8/300 (2.0 avg) on wumbolabs-practical-use-v1 at 8k with 10 failure labels led by unsupported claims — well behind the Gemma 4 12B variants on the same shared suite. Agent-backend and fake-tool answer-only probes were also run. LMX local speed 71.24 tok/s out. Negative practical result retained honestly; not a general model-quality verdict.

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
