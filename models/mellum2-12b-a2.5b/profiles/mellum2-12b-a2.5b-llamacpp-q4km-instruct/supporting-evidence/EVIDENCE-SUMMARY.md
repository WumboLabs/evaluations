# Evidence summary — Mellum2 12B-A2.5B (Instruct) (`mellum2-12b-a2.5b-llamacpp-q4km-instruct`)

## 2026-06-17 — Agent backend fit test (64k, Instruct + Thinking)

Maturity: **SPECIALIZED_TEST**. Instruct + Thinking Q4_K_M through LLMGauge agent-backend-v1 at 64k on WumboJetsII. 64k fit confirmed (Instruct 5/5 complete, 251.0-257.2 tok/s out, 9203 MiB peak VRAM). Manual scores: Instruct preferred (overall trust 3.7/5) over Thinking; neither safe for unsupervised shell/systemd operations. Not a general model-quality verdict.

## 2026-06-21 — 12B practical-use comparison (v024/v025 pool)

Maturity: **PRACTICAL_USE**. Shared multi-model practical-use comparison pool (wumbolabs-practical-use-v1, 8k): Instruct 239.9/300 (4.0), Thinking 232.8/300 (3.88).

## 2026-06-17 — Fake-tool honesty runs (64k)

Maturity: **SPECIALIZED_TEST**. Fake-tool honesty probes at 64k for both Mellum2 variants; feeding the agent-backend manual scores.

## 2026-07-04 — LocalMaxxing LMX speed runs (Instruct + Thinking)

Maturity: **BENCHMARK_ONLY**. LMX local speed evidence: Instruct 261.41 tok/s out; Thinking 265.47 tok/s out (llama.cpp, Q4_K_M). Measured locally; submission disposition covered by the 2026-09-10 backfill scope for canonical profiles only.
