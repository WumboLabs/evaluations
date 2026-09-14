# OMP agent evaluation review

Date: 2026-08-14
OMP: 17.3.3
Backend: llama.cpp b9672, loopback OpenAI-compatible server
Model: Qwen3.8-27B UD-IQ2_XXS, all layers on RTX 5070
Bounds: 12,288 context, 1,024 max output tokens, reasoning off, one sequence, no warmup, no network, isolated configuration and disposable workspace

## Resource-safe admission

The original Q4_K_M hybrid agent plan was abandoned after recovery because the operator prohibited further high-memory/hybrid execution. A first full-GPU UD-IQ2_M attempt at 4,096 context was rejected by the API before inference: OMP's 8,820-token request exceeded the configured context. No edit occurred. The corrected attempt used smaller UD-IQ2_XXS fully on GPU at 12,288 context. Server VRAM was 9,356 MiB at idle; host RAM remained about 5.1 GiB used with 25 GiB available during the agent run. Swap did not increase. The server was stopped immediately afterward.

## Task and result

Task: diagnose two failing retry-ledger tests; make the smallest fix that preserves failed-attempt evidence and rejects retry from non-failed states; run the full three-test suite; report defect, files, and observed tests.

Observed behavior:

- Inspected the workspace, tests, implementation, and project metadata.
- Attempted the pre-fix test command, but its command formulation lacked the required `PYTHONPATH=src`; the compacted tool result is preserved rather than treated as successful evidence.
- Initially hallucinated an unrelated event-log implementation after context compaction, then explicitly re-read `ledger.py`, recovered, and correctly identified both defects.
- Edited only `src/retryledger/ledger.py`: removed `job.attempts.clear()`, added an exact `Status.FAILED` guard, and retained the transition to `Status.PENDING`.
- Hit the 12,288-token context/output boundary immediately after the edit (`stopReason: length`). It did not execute the required post-fix suite and its final response omitted the exact file/test result.
- Independent post-session verification ran `PYTHONPATH=src python -m unittest discover -s tests -v`: all 3 tests passed in 0.000 seconds.

Quality verdict: **mixed**. The code change is minimal and correct, and it recovered from an incorrect intermediate diagnosis by re-reading evidence. Agent completion quality is not a pass: verification and final reporting requirements were missed because the session exhausted context.

## Session evidence

- Session: `sessions-llamacpp-12k/2026-08-14T20-35-20-242Z_01a001fc-8032-7000-978d-7dd8e95c20c0.jsonl`
- Compaction logs: sibling directory `2026-08-14T20-35-20-242Z_01a001fc-8032-7000-978d-7dd8e95c20c0/`
- SHA-256 session: `0099a4a3aae754d1dd5f1a7d2013ea41f7f7c148d80d378d87005003bd35f304`
- SHA-256 shake log 1: `6695f7c6bf2a34aa67a0afd3004a2b2b800c7276fc805abb4e56749cf22127d8`
- SHA-256 shake log 2: `2613a329ca4fdb6f1164d95dc122ce9b6155f45a2e8d00d422975db659e5c250`

LLMGauge `import-agent-harness --dry-run` rejected the source as `unsupported_source: source entry contains unsupported semantics`. The source contains OMP `prunedAt`/`[shaken …]` compacted tool-result entries and one synthetic unexecuted tool result. Per artifact-integrity policy, the session was not rewritten, flattened, or special-cased to force acceptance. No Agent Harness result was created. A repeated larger-context agent run would violate the post-recovery no-repeat/resource-safety constraint, so import remains unavailable for this bounded evaluation.

vLLM was not used for OMP: its only loadable configuration had already consumed 29 GiB RAM and 6.2 GiB swap and was declared unsafe.
