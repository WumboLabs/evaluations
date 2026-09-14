# Evidence summary — Qwen3-14B (`qwen3-14b-llamacpp-q4km`)

## 2026-07-05 — LLMGauge practical-use comparison (v025 pool)

Maturity: **PRACTICAL_USE**. Qwen3-14B Q4_K_M scored 228.4/300 (3.81 avg) on wumbolabs-practical-use-v1 (8k).

## 2026-07-15 — Fit-ladder success-fallback E2E (LLMGauge feature validation)

Maturity: **SPECIALIZED_TEST**. LLMGauge fit-ladder feature E2E used Qwen3-14B Q4_K_M as payload (32k -> 8k fallback). Primary subject: LLMGauge feature behavior; retained as model-adjacent evidence.

## 2026-07-05 — LMX speed run

Maturity: **BENCHMARK_ONLY**. LMX local speed evidence: 66.57 tok/s out (llama.cpp Q4_K_M). Archaeology retention review separately records 63.74 tok/s full-CUDA-offload in the May-era recorded benchmark.
