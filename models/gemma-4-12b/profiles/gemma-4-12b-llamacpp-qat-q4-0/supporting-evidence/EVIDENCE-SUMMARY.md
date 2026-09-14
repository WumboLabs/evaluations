# Evidence summary — Gemma 4 12B IT (`gemma-4-12b-llamacpp-qat-q4-0`)

## 2026-09-12/13 — Current-WELP recharacterization (RTX 5070 12GB)

Maturity: **CURRENT_WELP**. PASS — **READY_WITH_GUARDRAILS**. Full report: [`reports/gemma4-12b-welp-recharacterization-2026-09-12.md`](reports/gemma4-12b-welp-recharacterization-2026-09-12.md).

Gemma 4 12B IT recharacterized under the current WumboLabs Evaluation
Lifecycle Protocol on the canonical practical profile: Unsloth
UD-Q4_K_XL packaging of the Google QAT Q4_0 lineage (SHA-256
`90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e`,
7,366,423,360 bytes, source revision `fc034cfff751157913579611efad8462ac1be606`),
served by llama.cpp b9672 (74ade5274, CUDA SM120) with full GPU residency.

- Quality: 12/12 frozen mechanical screen (frozen scorer, temp 0).
- Capabilities: reasoning (thinking mode), executable coding, and
  tool-calling with grounded continuation all PASS.
- Performance: pp512 3,201 tok/s; tg128 72.92 tok/s (5-rep bench);
  near-full prefill degrades 2,855 → 1,397 tok/s across the ladder.
- Reliability (20-task mechanical corpus, 2 seeds): 11/20 and 10/20.
  Guardrails: verbosity/token-cap truncation, git-safety advisory
  weakness, uncertainty and sycophancy weakness.
- Context envelope COMPLETE (text profile): native rungs 8K/16K/32K/
  64K/128K VALIDATED with near-full performance; useful-context at
  131,072 passes all five gates at both seeds at 99.5% near-full
  occupancy. The exact native maximum 262,144 is **FIT_LIMIT** on a
  12 GB card (measured admission failure + KV-slope accounting; nearest
  measured boundary 131,072). No official extension mechanisms are
  documented by the upstream model cards.
- Practical default 32,768 (~8.4 GiB VRAM); guarded 131,072.
- Multimodal (image/audio/video via mmproj) is officially supported but
  **SUPPORTED_NOT_CHARACTERIZED**: this campaign characterized the
  canonical TEXT profile only; no model-wide multimodal claim is made.
- LocalMaxxing: MEASURED_NOT_SUBMITTED (canonical-profile local
  benchmark pp512 3,201 / tg128 72.92 tok/s; live submission is
  human-gated and did not occur).


## 2026-06-21 — 12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable)

Maturity: **PRACTICAL_USE**. Gemma 4 12B IT QAT UD-Q4_K_XL scored 259.2/300 (4.32 avg, 73.45 tok/s) vs UD-Q5_K_XL 254.0/300 (4.23); QAT Q4 selected as best overall practical variant. Shared report also tested Gemmable 4 12B MTP Q4_K_M (119.8/300) on the same suite — that model carries its own Evaluation page.

## 2026-06-16 — Early core-v1 + agent-backend-v1 scored runs (QAT Q4)

Maturity: **BENCHMARK_ONLY**. QAT Q4 completed core-v1 (8/8, manual score 308/400) and agent-backend-v1 (2048 ctx) during LLMGauge v0.16 validation.

## 2026-06-20 — Honesty ladder smoke (QAT Q4)

Maturity: **SPECIALIZED_TEST**. Honesty-ladder smoke runs against the QAT Q4 practical profile.

## 2026-07-04 — LMX speed runs across four Gemma 4 12B quants

Maturity: **BENCHMARK_ONLY**. LMX local speed evidence: Q4_K_M 72.11, UD-Q5_K_XL 62.76, UD-Q6_K_XL 51.26 tok/s out (llama.cpp). Archaeology additionally cites Q8_0 test and NVFP4 conversion-attempt records (weights since removed).
