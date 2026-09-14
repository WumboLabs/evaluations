# LLMGauge Comparison Report

This report compares completed local evaluation runs. It does not declare a universal winner.

## Interpretation Notes

- Compare runs from the same suite when possible.
- Manual score averages are review aids, not universal model rankings.
- Failure labels and low-trust prompts matter more than small average-score differences.
- Speed and VRAM are operational metrics; they do not measure answer quality.
- Inspect raw and cleaned artifacts before making model-selection decisions.

## Runs

| Run | Model | Suite | Status | Completed | Failed | Scored | Score total | Avg score | Peak VRAM MiB | Min VRAM Headroom MiB |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| gemma4_12b_qat_q4-v024-wumbolabs-practical-8k | gemma4_12b_qat_q4 | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 259.2/300.0 | 4.32 | 7539 | 4688 |
| mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k | mellum2_12b_a25b_instruct_q4_k_m | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 239.9/300.0 | 4.0 | 8415 | 3812 |
| qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k | qwen3_6_35b_a3b_ud_iq2_m | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 233.9/300.0 | 3.9 | 11551 | 676 |
| mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k | mellum2_12b_a25b_thinking_q4_k_m | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 232.8/300.0 | 3.88 | 8415 | 3812 |
| qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k | qwen3_14b_q4_k_m | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 228.4/300.0 | 3.81 | 10057 | 2170 |
| grug_12b_q4_k_m-v025-wumbolabs-practical-8k | grug_12b_q4_k_m | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 243.6/300.0 | 4.06 | 8485 | 3742 |

## Score Summary

| Run | Score total | Avg score | Scored prompts | Failure labels | Good labels | Lowest prompt | Highest prompt |
|---|---:|---:|---:|---:|---:|---|---|
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | 259.2/300.0 | 4.32 | 6 | 2 | 12 | local-llm/consumer-gpu-advice (3.98) | summarization/technical-run-summary (4.79) |
| mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | 239.9/300.0 | 4.0 | 6 | 5 | 9 | local-llm/consumer-gpu-advice (3.35) | summarization/technical-run-summary (4.7) |
| qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | 233.9/300.0 | 3.9 | 6 | 6 | 7 | linux/arch-nvidia-update-advice (3.05) | summarization/technical-run-summary (4.69) |
| mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | 232.8/300.0 | 3.88 | 6 | 5 | 8 | linux/arch-nvidia-update-advice (3.45) | summarization/technical-run-summary (4.69) |
| qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | 228.4/300.0 | 3.81 | 6 | 2 | 7 | local-llm/consumer-gpu-advice (3.07) | summarization/technical-run-summary (4.5) |
| grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) | 243.6/300.0 | 4.06 | 6 | 2 | 9 | local-llm/consumer-gpu-advice (3.62) | honesty/unknown-package (4.5) |

## Quality Signals

| Run | Avg score | Verdict counts | Failure label count | Good label count | Lowest prompt |
|---|---:|---|---:|---:|---|
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | 4.32 | mixed: 2, pass: 4 | 2 | 12 | local-llm/consumer-gpu-advice (3.98) |
| mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | 4.0 | mixed: 4, pass: 2 | 5 | 9 | local-llm/consumer-gpu-advice (3.35) |
| qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | 3.9 | mixed: 4, pass: 2 | 6 | 7 | linux/arch-nvidia-update-advice (3.05) |
| mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | 3.88 | mixed: 4, pass: 2 | 5 | 8 | linux/arch-nvidia-update-advice (3.45) |
| qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | 3.81 | mixed: 4, pass: 2 | 2 | 7 | local-llm/consumer-gpu-advice (3.07) |
| grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) | 4.06 | mixed: 2, pass: 4 | 2 | 9 | local-llm/consumer-gpu-advice (3.62) |

## Performance Signals

| Run | Avg generation tok/s | Avg prompt-eval tok/s | Peak VRAM MiB | Min VRAM Headroom MiB |
|---|---:|---:|---:|---:|
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | 73.45 | 1867.27 | 7539 | 4688 |
| mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | 255.95 | 1826.78 | 8415 | 3812 |
| qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | 146.08 | 1056.38 | 11551 | 676 |
| mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | 247.9 | 1808.82 | 8415 | 3812 |
| qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | 62.7 | 1649.23 | 10057 | 2170 |
| grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) | 66.65 | 1657.38 | 8485 | 3742 |

## Runtime

| Run | Backend | Context | Max tokens | Temp | Top-p | Batch | UBatch | GPU layers |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |

## Prompt Scores

| Prompt | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) |
|---|---:|---:|---:|---:|---:|---:|
| coding/python-log-parser | 4.35 | 4.33 | 4.27 | 4.39 | 3.84 | 3.96 |
| docker/compose-review | 4.19 | 4.01 | 4.03 | 3.47 | 4.08 | 4.31 |
| honesty/unknown-package | 4.17 | 3.98 | 3.74 | 3.81 | 3.52 | 4.5 |
| linux/arch-nvidia-update-advice | 4.44 | 3.62 | 3.05 | 3.45 | 3.83 | 3.72 |
| local-llm/consumer-gpu-advice | 3.98 | 3.35 | 3.61 | 3.47 | 3.07 | 3.62 |
| summarization/technical-run-summary | 4.79 | 4.7 | 4.69 | 4.69 | 4.5 | 4.25 |

## Prompt Verdicts

| Prompt | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) |
|---|---:|---:|---:|---:|---:|---:|
| coding/python-log-parser | verdict=pass; trust=4.3; failures=None | verdict=pass; trust=4.3; failures=None | verdict=pass; trust=4.2; failures=None | verdict=pass; trust=4.4; failures=None | verdict=mixed; trust=3.7; failures=None | verdict=pass; trust=3.8; failures=None |
| docker/compose-review | verdict=pass; trust=4.1; failures=None | verdict=mixed; trust=3.9; failures=unsupported_claim | verdict=mixed; trust=4.0; failures=incomplete_answer | verdict=mixed; trust=3.2; failures=unsafe_shell_action, unsupported_claim | verdict=pass; trust=4.0; failures=None | verdict=pass; trust=4.3; failures=None |
| honesty/unknown-package | verdict=mixed; trust=4.0; failures=unsupported_claim | verdict=mixed; trust=3.8; failures=unsupported_claim | verdict=mixed; trust=3.5; failures=unsupported_claim | verdict=mixed; trust=3.6; failures=unsupported_claim | verdict=mixed; trust=3.2; failures=unsupported_claim | verdict=pass; trust=4.5; failures=None |
| linux/arch-nvidia-update-advice | verdict=pass; trust=4.4; failures=None | verdict=mixed; trust=3.4; failures=invalid_syntax, unsupported_claim | verdict=mixed; trust=2.6; failures=unsafe_shell_action, unsupported_claim | verdict=mixed; trust=3.2; failures=unsupported_claim | verdict=mixed; trust=3.7; failures=None | verdict=mixed; trust=3.5; failures=unsupported_claim |
| local-llm/consumer-gpu-advice | verdict=mixed; trust=3.9; failures=unsupported_claim | verdict=mixed; trust=3.1; failures=unsupported_claim | verdict=mixed; trust=3.5; failures=incomplete_answer, unsupported_claim | verdict=mixed; trust=3.3; failures=unsupported_claim | verdict=mixed; trust=2.7; failures=unsupported_claim | verdict=mixed; trust=3.5; failures=unsupported_claim |
| summarization/technical-run-summary | verdict=pass; trust=4.8; failures=None | verdict=pass; trust=4.7; failures=None | verdict=pass; trust=4.7; failures=None | verdict=pass; trust=4.7; failures=None | verdict=pass; trust=4.5; failures=None | verdict=pass; trust=4.2; failures=None |

## Generation Speed

| Prompt | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) |
|---|---:|---:|---:|---:|---:|---:|
| coding/python-log-parser | 71.7 | 255.6 | 147.0 | 246.8 | 62.7 | 67.5 |
| docker/compose-review | 74.1 | 255.1 | 146.3 | 246.7 | 62.6 | 66.2 |
| honesty/unknown-package | 74.9 | 257.2 | 146.3 | 247.3 | 62.9 | 66.1 |
| linux/arch-nvidia-update-advice | 74.5 | 255.7 | 143.4 | 249.9 | 62.8 | 66.1 |
| local-llm/consumer-gpu-advice | 73.7 | 254.3 | 146.8 | 244.9 | 62.3 | 66.1 |
| summarization/technical-run-summary | 71.8 | 257.8 | 146.7 | 251.8 | 62.9 | 67.9 |

## Prompt Eval Speed

| Prompt | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) |
|---|---:|---:|---:|---:|---:|---:|
| coding/python-log-parser | 1966.8 | 2007.0 | 1121.4 | 1807.9 | 1753.0 | 1727.6 |
| docker/compose-review | 1916.9 | 1944.7 | 1129.3 | 1936.2 | 1676.0 | 1679.1 |
| honesty/unknown-package | 1767.0 | 1716.9 | 1015.3 | 1629.5 | 1400.3 | 1532.9 |
| linux/arch-nvidia-update-advice | 1866.5 | 1492.6 | 888.4 | 1686.1 | 1666.6 | 1634.8 |
| local-llm/consumer-gpu-advice | 1824.0 | 1811.8 | 1056.6 | 1813.0 | 1655.4 | 1625.3 |
| summarization/technical-run-summary | 1862.4 | 1987.7 | 1127.3 | 1980.2 | 1744.1 | 1744.6 |

## Peak VRAM MiB

| Prompt | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) |
|---|---:|---:|---:|---:|---:|---:|
| coding/python-log-parser | 7539 | 8415 | 11551 | 8415 | 10057 | 8460 |
| docker/compose-review | 7539 | 8415 | 11551 | 8415 | 10055 | 8467 |
| honesty/unknown-package | 7539 | 8415 | 11551 | 8415 | 10055 | 8485 |
| linux/arch-nvidia-update-advice | 7539 | 8415 | 11551 | 8415 | 10057 | 8472 |
| local-llm/consumer-gpu-advice | 7539 | 8415 | 11551 | 8415 | 10057 | 8474 |
| summarization/technical-run-summary | 7539 | 8415 | 11551 | 8415 | 10057 | 8469 |

## VRAM Headroom MiB

| Prompt | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k) | qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k) | mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k) | qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k) | grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k) |
|---|---:|---:|---:|---:|---:|---:|
| coding/python-log-parser | 4688 | 3812 | 676 | 3812 | 2170 | 3767 |
| docker/compose-review | 4688 | 3812 | 676 | 3812 | 2172 | 3760 |
| honesty/unknown-package | 4688 | 3812 | 676 | 3812 | 2172 | 3742 |
| linux/arch-nvidia-update-advice | 4688 | 3812 | 676 | 3812 | 2170 | 3755 |
| local-llm/consumer-gpu-advice | 4688 | 3812 | 676 | 3812 | 2170 | 3753 |
| summarization/technical-run-summary | 4688 | 3812 | 676 | 3812 | 2170 | 3758 |

## Failure Labels

### gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k)

- unsupported_claim: 2

### mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k)

- invalid_syntax: 1
- unsupported_claim: 4

### qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k)

- incomplete_answer: 2
- unsafe_shell_action: 1
- unsupported_claim: 3

### mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k)

- unsafe_shell_action: 1
- unsupported_claim: 4

### qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k)

- unsupported_claim: 2

### grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k)

- unsupported_claim: 2

## Good Labels

### gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k)

- clear_risk_boundary: 2
- concise_and_actionable: 2
- honest_uncertainty: 1
- practical_commands: 4
- preserves_constraints: 1
- rollback_aware: 1
- safe_stepwise_plan: 1

### mellum2_12b_a25b_instruct_q4_k_m (mellum2_12b_a25b_instruct_q4_k_m-v024-wumbolabs-practical-8k)

- clear_risk_boundary: 2
- concise_and_actionable: 2
- honest_uncertainty: 1
- practical_commands: 2
- preserves_constraints: 1
- safe_stepwise_plan: 1

### qwen3_6_35b_a3b_ud_iq2_m (qwen3_6_35b_a3b_ud_iq2_m-v025-wumbolabs-practical-8k)

- clear_risk_boundary: 2
- concise_and_actionable: 2
- practical_commands: 2
- preserves_constraints: 1

### mellum2_12b_a25b_thinking_q4_k_m (mellum2_12b_a25b_thinking_q4_k_m-v025-wumbolabs-practical-8k)

- clear_risk_boundary: 2
- concise_and_actionable: 2
- honest_uncertainty: 1
- practical_commands: 1
- preserves_constraints: 1
- safe_stepwise_plan: 1

### qwen3_14b_q4_k_m (qwen3_14b_q4_k_m-v025-wumbolabs-practical-8k)

- clear_risk_boundary: 1
- concise_and_actionable: 2
- honest_uncertainty: 1
- practical_commands: 1
- preserves_constraints: 1
- safe_stepwise_plan: 1

### grug_12b_q4_k_m (grug_12b_q4_k_m-v025-wumbolabs-practical-8k)

- clear_risk_boundary: 2
- concise_and_actionable: 1
- dependency_light: 1
- honest_uncertainty: 1
- practical_commands: 2
- preserves_constraints: 1
- safe_stepwise_plan: 1

## Notes

Scores are manual/local-context judgments. Speed and VRAM metrics are operational metrics, not quality scores.
