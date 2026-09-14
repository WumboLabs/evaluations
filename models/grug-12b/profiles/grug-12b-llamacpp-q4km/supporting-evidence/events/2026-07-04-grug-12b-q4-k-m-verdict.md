# Grug-12B Q4_K_M — LLMGauge Practical-Use Verdict

Date: 2026-07-04
Hardware: WumboJetsII, RTX 5070 12GB
Runtime: llama.cpp CUDA
Suite: wumbolabs-practical-use-v1
Context: 8192
Max tokens: 1200
Temperature: 0.2
Result dir: results/grug_12b_q4_k_m-v025-wumbolabs-practical-8k
Comparison report: results/compare-wumbolabs-practical-v025-plus-grug.md

## Result

Grug-12B Q4_K_M is structurally viable and scored well enough to include in the practical-use comparison, but it is not a replacement for Gemma 4 12B QAT as the current 12GB practical default.

## Score

Manual score total: 243.6 / 300
Average: 4.06 / 5
Verdicts: 4 pass, 2 mixed
Failure labels: unsupported_claim x2

Prompt scores:
- linux/arch-nvidia-update-advice: 3.72, mixed
- coding/python-log-parser: 3.96, pass
- docker/compose-review: 4.31, pass
- honesty/unknown-package: 4.50, pass
- summarization/technical-run-summary: 4.25, pass
- local-llm/consumer-gpu-advice: 3.62, mixed

## Performance

Average generation: 66.65 tok/s
Average prompt eval: 1657.38 tok/s
Peak VRAM: 8485 MiB
Minimum VRAM headroom: 3742 MiB

## Comparison Position

Current practical-use ranking by manual score:
1. Gemma 4 12B QAT — 259.2 / 300, avg 4.32
2. Grug-12B Q4_K_M — 243.6 / 300, avg 4.06
3. Mellum2 Instruct — 239.9 / 300, avg 4.00
4. Qwen3.6 35B-A3B — 233.9 / 300, avg 3.90
5. Mellum2 Thinking — 232.8 / 300, avg 3.88
6. Qwen3 14B Q4_K_M — 228.4 / 300, avg 3.81

## Interpretation

Grug is a credible Gemma-family alternate. It performs strongest on honesty and Docker review, and it avoids the severe fake-tool/package behavior seen in weaker candidates. However, it does not beat Gemma 4 12B QAT on total quality score, generation speed, or VRAM efficiency.

Compared with Gemma QAT:
- Lower score: 243.6 vs 259.2
- Slower generation: 66.65 tok/s vs 73.45 tok/s
- Higher VRAM: 8485 MiB vs 7539 MiB
- Lower headroom: 3742 MiB vs 4688 MiB

Compared with Mellum2 Instruct:
- Better manual score: 243.6 vs 239.9
- Much slower generation: 66.65 tok/s vs 255.95 tok/s
- Similar VRAM footprint: 8485 MiB vs 8415 MiB

## Verdict

Keep Gemma 4 12B QAT as the current 12GB practical default.

Keep Mellum2 Instruct as the speed candidate.

Keep Grug-12B Q4_K_M as a credible Gemma-family alternate and public comparison entry, but not as the default recommendation.
