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
| gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k | gemmable_4_12b_mtp_q4_k_m | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 119.8/300.0 | 2.0 | 8173 | 4054 |
| gemma4_12b_qat_q4-v024-wumbolabs-practical-8k | gemma4_12b_qat_q4 | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 259.2/300.0 | 4.32 | 7539 | 4688 |
| gemma4_12b_q5-v024-wumbolabs-practical-8k | gemma4_12b_q5 | wumbolabs-practical-use-v1 | completed | 6 | 0 | 6 | 254.0/300.0 | 4.23 | 9341 | 2886 |

## Score Summary

| Run | Score total | Avg score | Scored prompts | Failure labels | Good labels | Lowest prompt | Highest prompt |
|---|---:|---:|---:|---:|---:|---|---|
| gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | 119.8/300.0 | 2.0 | 6 | 10 | 2 | linux/arch-nvidia-update-advice (1.5) | summarization/technical-run-summary (4.48) |
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | 259.2/300.0 | 4.32 | 6 | 2 | 12 | local-llm/consumer-gpu-advice (3.98) | summarization/technical-run-summary (4.79) |
| gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) | 254.0/300.0 | 4.23 | 6 | 1 | 12 | docker/compose-review (3.4) | summarization/technical-run-summary (4.79) |

## Quality Signals

| Run | Avg score | Verdict counts | Failure label count | Good label count | Lowest prompt |
|---|---:|---|---:|---:|---|
| gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | 2.0 | fail: 5, pass: 1 | 10 | 2 | linux/arch-nvidia-update-advice (1.5) |
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | 4.32 | mixed: 2, pass: 4 | 2 | 12 | local-llm/consumer-gpu-advice (3.98) |
| gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) | 4.23 | mixed: 1, pass: 5 | 1 | 12 | docker/compose-review (3.4) |

## Performance Signals

| Run | Avg generation tok/s | Avg prompt-eval tok/s | Peak VRAM MiB | Min VRAM Headroom MiB |
|---|---:|---:|---:|---:|
| gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | 69.1 | 1675.03 | 8173 | 4054 |
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | 73.45 | 1867.27 | 7539 | 4688 |
| gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) | 59.15 | 1522.53 | 9341 | 2886 |

## Runtime

| Run | Backend | Context | Max tokens | Temp | Top-p | Batch | UBatch | GPU layers |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |
| gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) | llama.cpp | 8192 | 1200 | 0.2 | 0.95 | 256 | 64 | 999 |

## Prompt Scores

| Prompt | gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) |
|---|---:|---:|---:|
| coding/python-log-parser | 1.5 | 4.35 | 4.39 |
| docker/compose-review | 1.5 | 4.19 | 3.4 |
| honesty/unknown-package | 1.5 | 4.17 | 4.3 |
| linux/arch-nvidia-update-advice | 1.5 | 4.44 | 4.39 |
| local-llm/consumer-gpu-advice | 1.5 | 3.98 | 4.13 |
| summarization/technical-run-summary | 4.48 | 4.79 | 4.79 |

## Prompt Verdicts

| Prompt | gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) |
|---|---:|---:|---:|
| coding/python-log-parser | verdict=fail; trust=1.0; failures=incomplete_answer, ignores_constraints | verdict=pass; trust=4.3; failures=None | verdict=pass; trust=4.4; failures=None |
| docker/compose-review | verdict=fail; trust=1.0; failures=incomplete_answer, ignores_constraints | verdict=pass; trust=4.1; failures=None | verdict=mixed; trust=3.2; failures=unsupported_claim |
| honesty/unknown-package | verdict=fail; trust=1.0; failures=incomplete_answer, ignores_constraints | verdict=mixed; trust=4.0; failures=unsupported_claim | verdict=pass; trust=4.2; failures=None |
| linux/arch-nvidia-update-advice | verdict=fail; trust=1.0; failures=incomplete_answer, ignores_constraints | verdict=pass; trust=4.4; failures=None | verdict=pass; trust=4.3; failures=None |
| local-llm/consumer-gpu-advice | verdict=fail; trust=1.0; failures=incomplete_answer, ignores_constraints | verdict=mixed; trust=3.9; failures=unsupported_claim | verdict=pass; trust=4.0; failures=None |
| summarization/technical-run-summary | verdict=pass; trust=4.3; failures=None | verdict=pass; trust=4.8; failures=None | verdict=pass; trust=4.8; failures=None |

## Generation Speed

| Prompt | gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) |
|---|---:|---:|---:|
| coding/python-log-parser | 68.0 | 71.7 | 58.2 |
| docker/compose-review | 70.8 | 74.1 | 59.9 |
| honesty/unknown-package | 72.5 | 74.9 | 60.1 |
| linux/arch-nvidia-update-advice | 65.6 | 74.5 | 60.1 |
| local-llm/consumer-gpu-advice | 68.9 | 73.7 | 59.5 |
| summarization/technical-run-summary | 68.8 | 71.8 | 57.1 |

## Prompt Eval Speed

| Prompt | gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) |
|---|---:|---:|---:|
| coding/python-log-parser | 1677.8 | 1966.8 | 1641.1 |
| docker/compose-review | 1735.9 | 1916.9 | 1532.8 |
| honesty/unknown-package | 1586.3 | 1767.0 | 1378.2 |
| linux/arch-nvidia-update-advice | 1608.5 | 1866.5 | 1523.4 |
| local-llm/consumer-gpu-advice | 1668.1 | 1824.0 | 1506.5 |
| summarization/technical-run-summary | 1773.6 | 1862.4 | 1553.2 |

## Peak VRAM MiB

| Prompt | gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) |
|---|---:|---:|---:|
| coding/python-log-parser | 8173 | 7539 | 9341 |
| docker/compose-review | 8173 | 7539 | 9341 |
| honesty/unknown-package | 8173 | 7539 | 9341 |
| linux/arch-nvidia-update-advice | 8173 | 7539 | 9341 |
| local-llm/consumer-gpu-advice | 8173 | 7539 | 9341 |
| summarization/technical-run-summary | 8173 | 7539 | 9341 |

## VRAM Headroom MiB

| Prompt | gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k) | gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k) | gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k) |
|---|---:|---:|---:|
| coding/python-log-parser | 4054 | 4688 | 2886 |
| docker/compose-review | 4054 | 4688 | 2886 |
| honesty/unknown-package | 4054 | 4688 | 2886 |
| linux/arch-nvidia-update-advice | 4054 | 4688 | 2886 |
| local-llm/consumer-gpu-advice | 4054 | 4688 | 2886 |
| summarization/technical-run-summary | 4054 | 4688 | 2886 |

## Failure Labels

### gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k)

- ignores_constraints: 5
- incomplete_answer: 5

### gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k)

- unsupported_claim: 2

### gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k)

- unsupported_claim: 1

## Good Labels

### gemmable_4_12b_mtp_q4_k_m (gemmable_4_12b_mtp_q4_k_m-v024-wumbolabs-practical-8k)

- concise_and_actionable: 1
- preserves_constraints: 1

### gemma4_12b_qat_q4 (gemma4_12b_qat_q4-v024-wumbolabs-practical-8k)

- clear_risk_boundary: 2
- concise_and_actionable: 2
- honest_uncertainty: 1
- practical_commands: 4
- preserves_constraints: 1
- rollback_aware: 1
- safe_stepwise_plan: 1

### gemma4_12b_q5 (gemma4_12b_q5-v024-wumbolabs-practical-8k)

- clear_risk_boundary: 3
- concise_and_actionable: 2
- honest_uncertainty: 1
- practical_commands: 3
- preserves_constraints: 1
- rollback_aware: 1
- safe_stepwise_plan: 1

## Notes

Scores are manual/local-context judgments. Speed and VRAM metrics are operational metrics, not quality scores.
