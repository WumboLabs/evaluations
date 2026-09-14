# Qwen3.8-27B OMP Follow-up Addendum

**Date:** 2026-08-14
**Host:** WumboJetsII
**Overall evaluation status:** **PARTIAL** (unchanged)
**Follow-up OMP verdict:** **bounded autonomous completion pass**

## Decision

The retained llama.cpp matrix, context tests, practical LLMGauge runs, and vLLM safety rejection already answer the model-placement and runtime questions. Repeating them would add risk without resolving an evidence gap. The only useful follow-up was a second, smaller OMP task designed to complete comfortably below the prior 12,288-token compaction boundary.

No additional model benchmark was run.

## Configuration

| Component | Follow-up setting |
|---|---|
| Model | Qwen3.8-27B UD-IQ2_XXS GGUF |
| Runtime | llama-server 9672 (`74ade5274`) |
| Placement | All GPU layers; one slot |
| Context | 12,288 tokens |
| Sampling | Temperature 0; top-p 1 |
| Attention | Flash attention on |
| Reasoning | Off; `enable_thinking=false` |
| OMP | 17.3.4, non-interactive |
| Enabled OMP tools | `read`, `edit`, `bash` only |
| OMP output limit | 1,024 tokens per response |
| LLMGauge | 0.72.0, unchanged source and contracts |

The disposable workspace contained one 13-line Python implementation and three `unittest` cases. The defect was a boundary guard: `tail_window` rejected negative sizes but not zero. The prompt required inspection, failure reproduction, the smallest fix, the complete test suite, and an exact final report.

## OMP Result

Baseline behavior was deterministic: two tests passed and `test_rejects_zero_size` failed because no `ValueError` was raised.

The agent:

1. Inspected the prompt, workspace, implementation, and tests.
2. Ran `python3 -m unittest discover -v`; it correctly treated the resulting zero-test exit as invalid rather than as a pass.
3. Corrected the invocation to the workspace's only test module and reproduced the zero-size failure.
4. Changed only `windowing.py`, replacing `if size < 0` with `if size <= 0`.
5. Ran all three module tests and observed `OK`.
6. Reported the defect, exact file and line-level change, unchanged public signature, and observed test result.

Independent verification then ran:

```text
python -m unittest discover -s tests -v
```

All three tests passed. The preserved session has 32 JSONL entries, a normal `session_exit`, and no `prunedAt`, `[shaken ...]`, `__synthetic`, or `assistant_stop_length` marker. The final server request ended with `truncated = 0`; the slot held 9,782 tokens, below the 12,288-token limit.

Verdict: this is a complete bounded OMP pass. It does not replace the prior mixed larger-task result; together they show that UD-IQ2_XXS can complete a small one-file agent task when the tool surface and context demand are tightly bounded.

## Resource Safety

| Sample | Available RAM | Swap used | GPU memory | GPU utilization |
|---|---:|---:|---:|---:|
| Preflight | 25,375,084,544 B | 1,275,498,496 B | 1,018 / 12,227 MiB | 5% |
| Model loaded | 25,033,977,856 B | 1,275,404,288 B | 10,385 / 12,227 MiB | 4% |
| During inference | 24,924,893,184 B | 1,275,355,136 B | 10,448 / 12,227 MiB | 100% |
| Agent complete | 24,058,781,696 B | 1,277,210,624 B | 10,478 / 12,227 MiB | 11% |
| Server stopped | 26,160,832,512 B | 1,276,391,424 B | 1,091 / 12,227 MiB | 5% |

Minimum available RAM was 24,058,781,696 bytes. Swap used changed by 892,928 bytes from preflight to post-stop, with no material growth or thrashing. Useful GPU activity was present during inference. The workload remained far from the 85% RAM stop threshold and is classified resource-safe.

## LLMGauge Agent Harness Compatibility

Both unchanged import attempts failed:

```text
uv run llmgauge import-agent-harness SOURCE RESULT_DIR --dry-run
uv run llmgauge import-agent-harness SOURCE RESULT_DIR
```

Observed result:

```text
Agent Harness import failed (unsupported_source): source entry contains unsupported semantics
```

The exact incompatibility is the OMP 17.3.4 `model_change` entry on session line 3. It contains `resolvedModelIsFallback: false`; LLMGauge 0.72.0 permits only `model` and `role` beyond common entry fields for that entry type. No other unsupported top-level entry fields were found.

The source was not rewritten and neither schema nor importer was changed. No result directory was created, so `validate-result` was not applicable. This rejection is independent of the prior compacted-session rejection: the new source has no compaction or synthetic-result marker.

## Conclusion Changes

- **Changed:** OMP evidence now includes one complete, autonomous, resource-safe bounded task in addition to the earlier mixed larger task.
- **Unchanged:** Q4_K_M at 38 GPU layers and 8K, reasoning off, remains the best measured quality/balance configuration.
- **Unchanged:** UD-IQ2_M full GPU at 4K remains the best measured speed configuration.
- **Unchanged:** UD-IQ2_XXS full GPU at 12,288 context remains the agent-tested safe placement.
- **Unchanged:** vLLM remains operationally unsafe on this 32 GB host.
- **Unchanged:** Overall status remains **PARTIAL** because no LLMGauge Agent Harness result exists and the rejected vLLM surfaces remain intentionally unfilled.

## Evidence

Canonical follow-up directory: [`../evidence/omp-followup-2026-08-14/`](../evidence/omp-followup-2026-08-14/)

Key artifacts:

- `sessions/2026-08-14T21-29-27-928Z_01a0022e-0e78-7000-a859-eeecc187bb2b.jsonl` — raw OMP v3 session.
- `baseline-test.txt` — one expected pre-fix failure.
- `omp-output.txt` — complete non-interactive OMP output.
- `independent-test.txt` — independent three-test pass.
- `server.log` and `server-command.txt` — llama.cpp runtime evidence.
- `resource-samples.txt` — preflight, loaded, active, completion, and recovery samples.
- `final-safety-state.txt` — final RAM, swap, GPU, process, and required repository-status checks.
- `llmgauge-import-dry-run.txt`, `llmgauge-import.txt`, and `llmgauge-import-analysis.txt` — unchanged importer attempts and exact incompatibility.
- `sha256.txt` — SHA-256 manifest for the follow-up package.

## Remaining Limitations and Next Step

This is one deliberately simple, one-file task with a restricted tool set. It establishes bounded completion, not broad repository autonomy. Agent Harness compatibility remains unmeasured because the current preserved OMP schema is rejected before import.

Recommended next step: make OMP 17.3.4 `model_change` compatibility with LLMGauge 0.72.0 a separate tooling issue. After an explicitly reviewed contract change, retry import against this preserved session without rerunning the model or altering the evidence. No further 27B workload is justified on this host for the current evaluation.
