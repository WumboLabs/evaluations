# WumboLabs evaluation records — Gemma 4 12B IT

Canonical public evidence for WumboLabs testing of **Gemma 4 12B IT** (Google) — profile `gemma-4-12b-llamacpp-qat-q4-0`.

- **Tested artifact:** google/gemma-4-12b-it-qat-q4_0-gguf (QAT UD-Q4_K_XL packaging)
- **Runtime / hardware:** llama.cpp CUDA (WumboJetsII RTX 5070 12GB)
- **Profile status:** current (current-WELP recharacterization **READY_WITH_GUARDRAILS**, 2026-09-12/13; historical practical-use events preserved)

## Findings (bounded)

Current-WELP recharacterization (2026-09-12/13): **READY_WITH_GUARDRAILS** — 12/12 frozen quality screen, reasoning/coding/tools PASS, 72.92 tok/s decode, text-profile context envelope COMPLETE (8K–128K VALIDATED incl. two-seed useful-context at 99.5% near-full occupancy; 262,144 native maximum FIT_LIMIT on 12GB; no official extensions). Reliability guardrails: 11/20 and 10/20 on the 20-task mechanical corpus across two seeds (verbosity/token-cap truncation, git-safety advisory weakness). Multimodal lane SUPPORTED_NOT_CHARACTERIZED (text-only characterization). LocalMaxxing MEASURED_NOT_SUBMITTED. The historical practical-use result (259.2/300, 2026-06-21), core-v1/agent-backend-v1 runs, honesty-ladder smoke, and LMX speed records remain valid historical evidence below.

## Contents

| File | Content |
|---|---|
| [`EVIDENCE-SUMMARY.md`](EVIDENCE-SUMMARY.md) | per-event evidence summaries |
| [`events/`](events/) | one public-safe evidence derivative per testing event |
| [`reports/`](reports/) | public-safe scientific report derivatives (current-WELP recharacterization) |
| [`website-publication.json`](website-publication.json) | public-safe website export (`wumbolabs-labs-publication/1`) |
| [`summaries/`](summaries/) | public-safe machine summaries (LocalMaxxing disposition) |
| [`profile.json`](profile.json) | profile identity descriptor (schema `wumbolabs-eval-profile/1`) |
| [`provenance.json`](provenance.json) | retained-source identity + SHA-256 for every published claim |

## Shared comparison evidence

This repository carries the canonical public copy of a shared multi-model
comparison report. Related model repositories link here instead of duplicating it:

- [`shared/compare-gemma4-family-wumbolabs-practical-v024-scored.md`](compare-gemma4-family-wumbolabs-practical-v024-scored.md) — byte-identical public-safe LLMGauge comparison report (canonical copy for shared event practical-use-comparison-2026-06-21)
- [`shared/compare-wumbolabs-practical-v025-plus-grug.md`](compare-wumbolabs-practical-v025-plus-grug.md) — byte-identical public-safe LLMGauge comparison report (canonical copy for shared event practical-use-comparison-2026-07-04)

## Claim boundary

All evidence here is benchmark-only, practical-use, or specialized testing. It is NOT:
a WELP characterization, a universal model ranking, or a production-readiness proof.
Results are bounded by the tested artifact, runtime, hardware, suite, and settings.

## License / attribution

The evaluated model weights remain under their upstream license; no weights are
redistributed here. The evaluation evidence in this repository is WumboLabs work
product.
