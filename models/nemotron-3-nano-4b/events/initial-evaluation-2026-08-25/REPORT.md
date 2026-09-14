# Nemotron 3 Nano 4B — WumboLabs Model Evaluation Report

**Campaign:** `nemotron-3-nano-4b-welp-validation` (first deliberate WELP validation campaign)
**Date:** 2026-08-25 · **Operator:** supervising agent (single, no subagents)

---

## 1. Model identity (Phase 0)

| Field | Value |
|---|---|
| Repository | nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF |
| Revision (pinned live) | `ba223d14e45525f7fae81db77ea8cabeb2fc6c25` |
| File | NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf |
| Bytes / SHA-256 | 2,837,072,864 / `be5d9a656a51922f24f1f09a759cebb694e1f5d9728bf0ef9f8c972c5a0b5ef2` |
| Local path | models/NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf |
| License | NVIDIA Nemotron Open Model License |
| Acquisition | `hf download`, 2026-08-25T01:35Z |
| Template | GGUF-embedded ChatML + `<think>`; reasoning control = template kwarg `enable_thinking` (default ON) |

## 2. Runtime & hardware

| Field | Value |
|---|---|
| Runtime | llama.cpp build 10449, commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd` |
| Binary | ~/Projects/local-llm/llama.cpp-current/bin/llama-server |
| GPU | RTX 5070 12 GB (SM120), driver 610.57.04, stock 250 W |
| Host | Ryzen 7 9800X3D, Fedora 44, kernel 7.1.9 |
| Profile | CUDA0, full residency (`-ngl 999`), configured context `-c 32768`, parallel=1, FA on |

## 3. Exact WELP snapshot

HiveMindVault HEAD `5db5a637c6bd64dc38f22ac6a00b2a046ee7e333` (clean). Per-note SHA-256 in `protocol-snapshot/manifest.json`. Protocol unchanged during run.

## 4. Phases reached & gate outcomes

| Phase | Gate | Outcome |
|---|---|---|
| 0 Provenance | — | PASS |
| 1 Admission (hard) | PASS | Loads; full GPU residency verified (615→3969 MiB); clean inference/termination; no Xid/OOM; non-degenerate output |
| 2 Performance | PASS* | *criterion interpreted (F-02) |
| 3 Practical Viability | **PROTOCOL_BLOCKED** | 12/12 screen but protocol defines no advancement threshold (F-01) |
| 4–10, OMP-21B | NOT RUN | Stopped per campaign rule: do not march through later phases after an undecidable gate |

## 5. Performance (Phase 2)

Warmup + 5 measured reps each, greedy, full distributions in `results/performance/performance.json`.

- **Decode:** ~178 tok/s mean (512-token generations)
- **Prefill:** ~6,500 tok/s at ~2,600-token prompts (~0.40 s TTFT)
- **TTFT short prompt:** ~30 ms
- Fresh `llama-bench -p 512 -n 128`: ~180 tok/s out, 65 ms TTFT (also used as the LocalMaxxing-compatible submission artifact)

Methodology note: two earlier prefill passes were invalidated by llama.cpp KV prefix caching and discarded; final run uses unique prompts per repetition.

## 6. Practical viability evidence (Phase 3 screen)

12 tasks across instruction following, strict output, extraction, structured JSON, technical knowledge, false-premise rejection, uncertainty behavior, simple reasoning: **12/12**, mechanical scoring, scorer spot-checked on boundary cases (P09/P10). Raw outputs: `results/practical/raw.jsonl`. This is screening evidence, not a gate pass — see §8.

## 7. Reasoning findings

Bounded observations only (dedicated module not reached): default mode emits `<think>` traces then answers; `enable_thinking=false` yields direct correct answers (e.g., "17 × 23" → "391"). Producer's reasoning-off benchmark framing is therefore operationally reproducible on this runtime.

## 8. Stop reason

**PROTOCOL_BLOCKED at Phase 3 gate decision.** The model showed no failing behavior; WELP's documented material contains no Phase 3 advancement threshold (explicitly deferred to Protocol Open Questions #1), so no deterministic PASS/FAIL could be produced without inventing a rule, which the campaign forbids.

## 9. OMP integration

- **21A connectivity smoke:** SUCCESS — OMP 18.0.4 connected to the local server via implicit llama.cpp discovery (`LLAMA_CPP_BASE_URL=http://127.0.0.1:8471`), isolated profile, zero user-config mutation. Integration result only; not a model result.
- **21B agent module:** not run (viability/reliability precondition unestablishable).

## 10. Producer-claim classifications

See `results/producer_claims.json`. Summary: reasoning control REPRODUCED; official llama.cpp support PARTIALLY_REPRODUCED; architecture facts PARTIALLY_REPRODUCED; all benchmark numbers (RULER 128k=91.2, IFEval/IFBench/Orak/HaluEval), 262K context, edge/agentic suitability, BF16-recovery: INCONCLUSIVE (methodology unavailable or phases unreached).

## 11. Operational failures

- Two perf.py script defects (fixed in place) and two cache-polluted prefill measurement passes — recorded in execution accounting.
- OMP first smoke attempt with a JSON provider overlay failed (model not found); resolved via documented llama.cpp discovery.
- No GPU faults, no Xid/reset/GSP/channel events, no crashes.

## 12. Limitations

Single-seed practical screen; reliability, context quality, coding, tools, agent behavior, and soak were NOT TESTED / NOT REACHED (phases 4–10). LLMGauge never invoked (no phase mandated it). Results must not be generalized to a model review.

**Context wording correction:** the server was successfully *configured* with a 32K context window (`-c 32768`) and inference ran within it. Useful 32K context behavior was **not evaluated**, because the WELP context phase (Phase 6) was never reached. Configured/allocated context is not evidence of useful context.

## 13. Scope of conclusions (no deployment recommendation)

The campaign stopped at the Phase-3 gate decision; no role/profile or deployment recommendation is supported by this evidence. What the reached phases establish only:

- the model loaded cleanly and served stably across the tested phases;
- performance was measured (§5);
- the Phase-3 screening result was measured: 12/12 (§6);
- OMP connectivity was demonstrated (§9);
- the reasoning-control mechanism was boundedly observed (§7).

Reliability, capability-module, context-quality, variance, soak, and agent-capability claims are explicitly NOT TESTED.

## 14. Execution counts

From `summaries/execution_counts.json`:

| Count | Value |
|---|---|
| Speed warmups | 8 |
| Measured speed repetitions | 31 |
| Admission generations | 3 |
| Practical tasks (unique) | 12 |
| Practical generations | 12 (seed 42) |
| Reasoning observations | 2 mode observations; dedicated module not reached |
| OMP connectivity attempts | 1 successful turn (+1 failed provider-resolution attempt, no inference) |
| Context-related calls | 0 (Phase 6 not reached) |
| Producer-claim checks | 0 benchmark reproductions attempted (all classified from reachability) |
| Soak requests | 0 |
| **Total approx. local generations** | **55** |
| Mechanically scored outputs | 12 |
| Manually reviewed outputs | 3 (scorer spot-checks P09/P10 + admission smoke) |

**Invalidated/discarded executions: 26** — two full perf.py passes polluted by llama.cpp KV prefix caching (identical repeated prompts silently inflated prefill throughput), plus two aborted script attempts. All remain recorded in execution accounting; none contribute to reported statistics. The valid measured set is the final perf pass plus the fresh llama-bench run.

## 15. WELP conformance summary

| Item | Value |
|---|---|
| Protocol snapshot | HiveMindVault HEAD `5db5a637c6bd64dc38f22ac6a00b2a046ee7e333` (clean); per-note SHA-256 in `protocol-snapshot/manifest.json` |
| Phases entered | 0, 1, 2, 3 |
| Phases passed | 0 (provenance), 1 (hard gate), 2 (*criterion interpreted) |
| Progression stopped at | Phase-3 gate decision |
| Early-stop behavior | Worked as intended — halted at first undecidable gate; no compute spent proving later failures |
| Protocol ambiguities found | 9 |
| Undocumented decisions required | 4 |
| Scorer defects | 0 found |
| Schema/artifact deficiencies | execution-counts schema unspecified; canonical contracts absent |
| Bespoke exceptions | OMP integration executed as handoff-level provisional requirement outside WELP phases |
| Protocol changed during testing | **NO** |
| Rule silently invented | **NO** |
| Documented phase order followed | YES |
| OMP integration documentation status | Absent from vault at snapshot time (finding F-05) |
| Final WELP verdict | `PROTOCOL BLOCKED BEFORE COMPLETE EVALUATION` |

## 16. Protocol findings

Full text: `protocol-findings.md`.

| ID | Area | Observation | Operational consequence | Disposition |
|---|---|---|---|---|
| F-01 | Phase 3 gate | No deterministic advancement threshold exists ("NOT finalized"; Open Question #1) | Campaign PROTOCOL_BLOCKED with a 12/12 screen that could not become a gate decision; later phases unreached | Open — human decision required |
| F-02 | Phase 2 criterion | No defined pass/fail condition for characterization phase | PASS recorded as "completed per standard" (interpretation) | Open — declare informational or define criteria |
| F-03 | Test contracts | No canonical contracts; campaign authored its own v0 contract | Cross-model comparability invariant cannot hold | Open — promote Practical Quality contract to versioned fixture |
| F-04 | Context rungs | "Predefined context rungs" referenced but never defined | Agents reaching Phase 6 must invent rungs | Open — publish default ladder or pre-campaign decision rule |
| F-05 | OMP module | OMP integration requirement (21A/21B) absent from vault | Executed as handoff-level override, outside WELP phases | Resolved this milestone — added to vault |
| F-06 | Publication routing | LocalMaxxing layer missing from Publication Routing note | Fourth publication destination unrecorded | Resolved this milestone — added to vault |
| F-07 | Producer wording | Card says reasoning controlled "via a system prompt" but documented mechanism is the `enable_thinking` template kwarg | An agent following card prose searches for an unspecified system prompt | Producer-side fix; WELP captures effective mechanism from artifact |
| F-08 | Scorer validation | No proactive scorer-validation requirement; spot-checks were incidental | Wrong scorers could persist undetected | Open — add bounded manual-review requirement |
| F-09 | Accounting schema | `execution_counts.json` "should eventually exist" without field schema | Cross-campaign aggregation unstable | Open — freeze minimal schema |

## 17. LocalMaxxing status

Record: `summaries/localmaxxing.json`.

| Stage | Status |
|---|---|
| Authentication | NOT_SUBMITTED — no API key available in environment |
| Model identity resolution | RESOLVED — nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF · Q4_K_M · rev `ba223d14…` |
| Speed-test dry run | DRY_RUN_VALID (measurement plan written) |
| Speed-test measurement | LOCAL_ONLY → measured: fresh llama-bench `-p 512 -n 128`, ~180 tok/s out, 65 ms TTFT; validate-local: valid |
| Speed-test submission / ID | SUBMISSION_BLOCKED on missing credentials; no submission ID |
| Benchmark-suite submissions | NOT_APPLICABLE — supported suites were outside reached WLEP phases; nothing submitted |
| LocalMaxxing Report | NOT_CREATED — campaign stopped at Phase 3; per workflow no report was manufactured for an incomplete evaluation. A draft derived only from validated evidence exists (`publication/localmaxxing_report_draft.md`) and is UNSUBMITTED |
| Report ID / URL | none |

## 18. Publication routing (this campaign)

- **Obsidian:** methodology/process findings only (F-01..F-09) — routed via this milestone's vault update; no model evidence duplicated.
- **GitHub:** publication bundle ready locally at `publication/`; not published (campaign is not a completed full model review).
- **LocalMaxxing:** speed run submission-ready, blocked on API key; report intentionally not created (Phase-3 stop). Statuses in §17 are canonical.
- **WumboCore Labs:** not appropriate — progression stopped at Phase 3; do not present as a completed model review.

## 19. Artifact index

| Artifact | Path |
|---|---|
| Protocol snapshot manifest | `protocol-snapshot/manifest.json` |
| Gate records | `results/admission/admission.json` · `results/performance/gate.json` · `results/practical/gate.json` |
| Performance evidence | `results/performance/performance.json` |
| Practical raw output + scores | `results/practical/raw.jsonl` · `results/practical/scored.json` |
| Execution counts | `summaries/execution_counts.json` |
| WELP conformance record | `summaries/wlep_conformance.json` · `WLEP-CONFORMANCE.md` |
| Protocol findings | `protocol-findings.md` |
| Producer claims | `results/producer_claims.json` |
| OMP evidence | `results/omp/connectivity_smoke.json` · `results/omp/smoke_transcript.txt` |
| LocalMaxxing evidence | `summaries/localmaxxing.json` · `publication/localmaxxing_report_draft.md` |
| Telemetry/safety | `telemetry/nvidia-smi-initial.csv` · `telemetry/nvidia-smi-final.csv` · `telemetry/telemetry.csv` · `telemetry/journal-baseline-errors.txt` |
| Model provenance | `sources/acquisition.json` · `sources/gguf_metadata.json` · `sources/README.md` |
| Contracts & scripts | `prompts/practical_contract.json` · `scripts/perf.py` · `scripts/run_practical.py` · `scripts/telemetry.sh` |
| Publication bundle | `publication/` (+ `publication/REPRODUCE.md`) |
