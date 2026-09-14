# Protocol Findings — apodex-1.1-mini campaign

Snapshot: `wlep-next-snapshot-2026-08-25-end-to-end` · Campaign: 2026-08-25 · WLEP untouched during run.

Findings are incorporated into the draft WLEP only through a separate post-run protocol-update milestone.

## PF-01 — PV scorer rejection lexicon has recall gaps (scorer defect)
- **Observation:** `score_pv.py` (79f29b2c…) classifies correct false-premise rejections as HALLUCINATION when the phrasing is outside its fixed REJECT/UNCERTAIN lists, via the `len(out) > 40 → HALLUCINATION` fallback.
- **Evidence:** FP01 s42 ("I don't have information about a package named fastjsonify2…"), FP05 s43 ("there's no `ulimit --warp` command in bash"), FP04 s44, FP05 s42/s44 — all correct rejections scored HALLUCINATION. 8 of 27 Phase-3 fails reviewed as artifacts.
- **Affected note:** Scoring Policy / contract wlep-practical-viability.
- **Impact:** G2 (false-premise) rates understated. Gate verdict unchanged even correcting all artifacts in the model's favor (seed-42 aggregate still <0.75).
- **Proposed direction:** extend lexicon or add semantic rejection detection in a NEW scorer revision with fresh self-tests; recalibrate G2 on controls before reuse.
- **Status:** OPEN — post-campaign review.

## PF-02 — Gate-phase reasoning state is precedent-implied, not ruled (ambiguity AMB-01)
- **Observation:** The frozen PV runner does not pin thinking mode; the reliability runner hard-codes `enable_thinking:false`. Precedent lives only in an invalidated-run remark (qwen38 "--reasoning off omitted").
- **Evidence:** First Apodex PV pass produced 90/90 reasoning_content, 57/90 length-truncations, 55/90 empty content (retained: `INVALIDATED-phase3-pass3-think-budget-starvation.jsonl`) — exactly the documented starvation failure mode.
- **Impact:** campaigns can burn full passes and mis-score a model silently.
- **Proposed direction:** add "gate baseline reasoning state" as an explicit field of the Serving Profile Identity standard + enforce in runners.
- **Status:** OPEN.

## PF-03 — Frozen Phase-2 harness defects (HF-01/02/03)
- **Observation:** decode workload permits ~2-token compliant termination; contamination audit treats any nonzero cached_tokens as contamination; runner assumes pre-existing output dir.
- **Impact:** two invalidated perf passes this campaign; prior campaigns may have carried the same latent issues.
- **Proposed direction:** force minimum generation length in workload; audit via processed-token cross-check instead of cached_tokens; mkdir output dir.
- **Status:** OPEN (campaign-local revisions recorded in `scripts/phase2_perf_v3.py`, `scripts/phase2_prefill_nocache.py`).

## PF-04 — llama.cpp runtime reports constant `cached_tokens=74` artifact
- **Observation:** usage.prompt_tokens_details.cached_tokens reads a constant 74 for all requests regardless of content/length (verified with disjoint prompts), while real cache hits report true magnitudes (5643/5695 observed).
- **Impact:** any consumer using cached_tokens for contamination detection gets both false positives and a floor artifact.
- **Proposed direction:** note for Runtime Pinning; upstream llama.cpp investigation.
- **Status:** OPEN.

## PF-05 — Runtime currency check rule (operator directive, 2026-08-25)
- **Observation:** operator directive: going forward, diff existing runtime builds against newer requirements first; build only on affirmative evidence of incompatibility.
- **This campaign:** verified QWEN35MOE arch + draft-mtp existed in old tree but repo pinned ≥f280b269 (166 commits ahead); built separate pinned tree per boundary rules.
- **Proposed direction:** add a Runtime Pinning checklist step: "compatibility delta vs newest existing local build before any new build".
- **Status:** ADOPTED as standing practice.

## PF-06 — Background-job filesystem isolation lost a generation pass (operational)
- **Observation:** a harness-backgrounded generation job reported success writing 90 rows, but the output file was unrecoverable afterward (`find` across $HOME found nothing).
- **Impact:** 90 generations invalidated; rerun driven through persistent-kernel execution with absolute paths.
- **Proposed direction:** Evaluation Operations should mandate absolute output paths + immediate post-run hash verification for long model-generation jobs.
- **Status:** OPEN.

## Convergence statement
No structural blocker occurred. Every phase entered ran to its frozen definition; every gate decision came from frozen thresholds; all deviations are documented decisions D1–D5 plus recorded defects above. **WLEP did not change during the run: NO.** This is further evidence of protocol convergence toward v1.0 candidacy.
