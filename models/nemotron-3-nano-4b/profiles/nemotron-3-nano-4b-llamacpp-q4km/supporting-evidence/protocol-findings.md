# Protocol Findings — Nemotron 3 Nano 4B WLEP Validation Campaign

Campaign: `nemotron-3-nano-4b-wlep-validation`
Protocol snapshot: HiveMindVault HEAD `5db5a637c6bd64dc38f22ac6a00b2a046ee7e333` (clean), see `protocol-snapshot/manifest.json`.
Scope: findings **about WLEP**, not about the model. Nothing in HivemindVault was edited.

---

## F-01 · Phase 3 has no advancement threshold (BLOCKING)

- **Observation:** The Phase 3 gate cannot be evaluated. `WLEP Phase Structure.md` says "Advancement gate intended but threshold NOT finalized"; `Protocol Open Questions.md` item 1 asks what the criteria should be. No note defines a score, margin, or rule.
- **Why it matters:** This is the campaign's first non-deterministic gate after the Phase 1 hard gate. Any agent executing WLEP must either invent a threshold (forbidden) or halt progression. Our campaign stopped here with a 12/12 screen result that could not be converted into a gate decision.
- **Evidence:** `results/practical/gate.json`; `WLEP Phase Structure.md` line 23; `Protocol Open Questions.md` line 9.
- **Affected note:** `WLEP Phase Structure.md`, `Early-Stop Philosophy.md`.
- **Proposed direction:** Define a deterministic Phase 3 advancement rule (e.g., per-category minimums plus an overall fraction) before the next campaign; until then, campaigns will either stall or silently improvise.

## F-02 · Phase 2 has no defined pass/fail criterion

- **Observation:** Phase Structure describes characterization outputs but no gate condition. We recorded PASS as "completed per Repetition Policy," which is an interpretation, not a documented rule.
- **Why it matters:** Minor, but the conformance record requires stating whether any rule had to be interpreted — this is one.
- **Evidence:** `results/performance/gate.json`.
- **Affected note:** `WLEP Phase Structure.md`.
- **Proposed direction:** Either declare Phase 2 informational (no gate) explicitly, or define resource/throughput sanity criteria.

## F-03 · No canonical test contracts exist yet

- **Observation:** `Standard Campaign Artifacts.md` lists candidate contracts but states canonical prompts still live in local campaign evidence (migration TODO). Every contract in this campaign (`prompts/practical_contract.json`) is campaign-local v0.
- **Why it matters:** Cross-model comparability — a WLEP invariant — cannot hold while each campaign authors its own prompts.
- **Evidence:** `prompts/practical_contract.json`; `Standard Campaign Artifacts.md` lines 30-34.
- **Affected note:** `Standard Campaign Artifacts.md`, `Protocol Open Questions.md` (item on prompt migration).
- **Proposed direction:** Promote at least the Practical Quality contract to a versioned fixture before v1.0.

## F-04 · Context rungs referenced but never defined

- **Observation:** Phase 6 says "advance through predefined context rungs," but no vault note defines any rung ladder. Handoff §20 anticipated this ("If the current protocol does not specify exact rungs, record that").
- **Why it matters:** An agent reaching Phase 6 must invent rungs — exactly the silent-invention WLEP forbids.
- **Evidence:** `WLEP Phase Structure.md` line 33 (no definition anywhere else in `03 - Reference/WumboLabs/`).
- **Affected note:** `WLEP Phase Structure.md`.
- **Proposed direction:** Publish a default ladder (e.g., 4k/8k/16k/… with filled-context checks) or make rung selection an explicit pre-campaign decision.

## F-05 · OMP integration requirement absent from the vault

- **Observation:** Handoff §§21–22 add a two-stage OMP integration test (21A connectivity smoke, 21B full agent module). No WumboLabs note mentions OMP integration testing. Handoff itself flags this as a post-cleanup provisional addition.
- **Why it matters:** The protocol under test did not contain a requirement the operator was instructed to execute; we ran it as a handoff-level override and recorded it separately from WLEP phases.
- **Evidence:** grep of `03 - Reference/WumboLabs/*.md` shows no OMP references; `results/omp/connectivity_smoke.json`.
- **Affected note:** none (missing).
- **Proposed direction:** Add an OMP Integration module note: trigger conditions, INTEGRATION_BLOCKED vs MODEL_FAIL semantics, isolation requirements, scoring dimensions for 21B.

## F-06 · LocalMaxxing publication routing absent from the vault

- **Observation:** Publication Routing defines OBSIDIAN / GITHUB / WUMBOCORE LABS only. The LocalMaxxing.com community-publication layer (handoff §30) appears nowhere in the frozen snapshot.
- **Why it matters:** Publication routing is load-bearing; an unrecorded fourth destination risks either missed publications or ad-hoc policy. Treated here as PROVISIONAL workflow addition.
- **Evidence:** `Publication Routing.md` (no LocalMaxxing); handoff §30.
- **Affected note:** `Publication Routing.md`.
- **Proposed direction:** Add LocalMaxxing to Publication Routing with submission rules (dry-run first, fresh measurements only, no cherry-picked reps) once its workflow stabilizes.

## F-07 · Producer reasoning-control wording contradicts its own mechanism

- **Observation:** Model-card prose says reasoning "can be controlled via a system prompt," but the documented mechanism (BF16 card + GGUF template) is the chat-template kwarg `enable_thinking` (default true). No exact system-prompt string exists in pinned sources.
- **Why it matters:** WLEP Phase 0 requires template identity and reasoning-control instructions; an agent following card prose would look for a system prompt that is never specified.
- **Evidence:** `sources/acquisition.json` (template_identity.discrepancy_note); GGUF `tokenizer.chat_template`; BF16 README line ~206.
- **Affected note:** none directly; relevant to `Model Acquisition & Identity.md` recording requirements.
- **Proposed direction:** Producer-side wording fix; WLEP could require capturing the *effective* control mechanism from the artifact/template rather than card prose.

## F-08 · Scorer-defect policy lacks a mechanical scorer-validation step

- **Observation:** Scoring Bug & Correction Policy reacts to discovered scorer defects but prescribes no proactive validation. We spot-checked two tricky tasks by hand; nothing in the protocol required it.
- **Why it matters:** Lesson 10 ("scorers can be wrong") implies validation should be systematic, not incidental.
- **Evidence:** `scripts/run_practical.py` (spot-check step), `Scoring Bug & Correction Policy.md`.
- **Affected note:** `Scoring Policy.md`.
- **Proposed direction:** Add a bounded manual-review sample requirement for new contracts (e.g., all failures + N boundary passes).

## F-09 · Execution-accounting machine standard is "developing" without schema

- **Observation:** `Execution Accounting.md` says `summaries/execution_counts.json` "should eventually exist" but defines no field schema. Field names here are invented per campaign.
- **Why it matters:** Aggregation/comparison across campaigns needs stable keys.
- **Evidence:** `summaries/execution_counts.json`.
- **Affected note:** `Execution Accounting.md`.
- **Proposed direction:** Freeze a minimal JSON schema (keys for each count category listed in the note).

---

## Summary

| # | Severity | Type |
|---|----------|------|
| F-01 | Blocking | Missing threshold → PROTOCOL_BLOCKED |
| F-02 | Low | Undefined phase criterion |
| F-03 | High | Missing canonical contracts |
| F-04 | High | Undefined context rungs |
| F-05 | High | OMP module missing |
| F-06 | Medium | LocalMaxxing routing missing |
| F-07 | Low (producer-side) | Card/template discrepancy |
| F-08 | Medium | Missing scorer-validation requirement |
| F-09 | Medium | Unspecified accounting schema |

**Silently invented rules: NONE.** Every gap above produced a recorded finding, not an improvised permanent rule.


## Addendum (post-inspection): LocalMaxxing tooling state

- The `lmx` CLI has **no `report` subcommand**; Reports exist only as API endpoints (`GET /api/report-format`, `POST /api/models/<org>/<name>/reports`) surfaced through `lmx context`.
- No newer CLI build was locatable (site root serves an SPA page at the old tarball path; `/docs/agent-skill` 404s; no public source repo found in binary strings).
- Operator authorized updating the CLI mid-campaign; without source or a newer artifact, extension is limited to campaign-local scripts against the documented API.
- Speed-benchmark submission workflow **is** present and methodologically compatible; dry-run + fresh measurement completed (`runs/nvidia-NVIDIA-Nemotron-3-Nano-4B-GGUF/20260825T015538Z.json`, validate-local: valid), submission blocked only on missing API key.