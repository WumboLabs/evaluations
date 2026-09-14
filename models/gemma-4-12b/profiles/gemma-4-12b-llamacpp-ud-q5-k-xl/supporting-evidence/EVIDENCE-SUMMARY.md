# Evidence summary — Gemma 4 12B IT (`gemma-4-12b-llamacpp-ud-q5-k-xl`)

## 2026-06-21 — 12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable)

Maturity: **PRACTICAL_USE**. Gemma 4 12B IT QAT UD-Q4_K_XL scored 259.2/300 (4.32 avg, 73.45 tok/s) vs UD-Q5_K_XL 254.0/300 (4.23); QAT Q4 selected as best overall practical variant. Shared report also tested Gemmable 4 12B MTP Q4_K_M (119.8/300) on the same suite — that model carries its own Evaluation page.

## 2026-07-04 — LMX speed runs across four Gemma 4 12B quants

Maturity: **BENCHMARK_ONLY**. LMX local speed evidence: Q4_K_M 72.11, UD-Q5_K_XL 62.76, UD-Q6_K_XL 51.26 tok/s out (llama.cpp). Archaeology additionally cites Q8_0 test and NVFP4 conversion-attempt records (weights since removed).
