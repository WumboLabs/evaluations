# Protocol Findings — ornith-1.5-9b campaign

Snapshot: `welp-next-snapshot-2026-08-26-post-rename` · Campaign 2026-08-27 · Protocol untouched during run; findings queued for post-run protocol update.

## PF-01 — Scorer lexicons systematically understate capability (reliability + linux + reasoning)
- **Observation:** exact-string/substring gates misclassify correct answers: `can't` rejected where `cannot` required; `forbid:["enable"]` substring-matches "enabling" in a substantively correct systemd answer; `rpm -qf --whatprovides` judged wrong vs pinned `dnf provides`; extra explanatory prose after a correct command fails rag tasks.
- **Evidence:** Phase 4 G6 fail analysis (summaries/reliability.json manual_review); Phase 5 linux_systems 32/66 fails dominated by vocabulary variants; reasoning r-arith-2 `FINAL: 875 Wh` vs exact `875`.
- **Impact:** cross-module pass rates understated; a whole-model gate (Phase 4) can flip on scorer artifacts, not model behavior.
- **Proposed direction:** word-boundary matching for forbid-lists; synonym classes or semantic adjudication layer with fresh selftest fixtures; report raw + adjudicated rates.
- **Status:** OPEN.

## PF-02 — run_context.py overshoots at exact n_ctx boundary; /tokenize failure silently degrades ladder
- **Observation:** at rung == configured ctx (32768), generator produced a 42042-token prompt (delta +28 % > ±10 % band) because live `/tokenize` returned an error and the two-pass refinement was skipped without aborting. Seeds 42/43 got HTTP 400 (never entered model); seed 44's refinement converged and passed.
- **Impact:** ladder rungs at/near allocation are untestable; INCONCLUSIVE verdicts; useful_context ceiling under-reports.
- **Proposed direction:** treat /tokenize unavailability as FATAL for targeting (or fall back to local tokenizer with safety margin); cap rung targeting at n_ctx − max_tokens − margin.
- **Status:** OPEN.

## PF-03 — soak.py sentinel s2 KeyError inflates error count 50 %
- **Observation:** `SENTINELS[1]` has no `"expect"` key; `s["expect"]` raises AFTER a successful HTTP response; generic `except` counts it as an error. Any campaign using the frozen harness reports ~50 % false errors.
- **Evidence:** screening.json errors 5724 ≈ requests/2; post-hoc probes: both sentinels answer correctly; server log clean.
- **Proposed direction:** `s.get("expect")`; add selftest fixture exercising both sentinel branches.
- **Status:** OPEN.

## PF-04 — welp-reasoning contract ground-truth defect
- **Observation:** r-arith-1 expects `59`; prompt arithmetic 42−17+24 = 49. Model was scored wrong for being right.
- **Impact:** 3/60 reasoning rows mis-scored (all seeds, both modes).
- **Proposed direction:** contract erratum + regeneration of the pinned hash; scorer selftests should include arithmetic-consistency checks of expected values.
- **Status:** OPEN.

## PF-05 — MTP self-draft speculation is not output-lossless (llama.cpp b10449)
- **Observation:** `--spec-type draft-mtp` against the model's own nextn tensors: +9.9 % decode, but 1/6 identical-seed probe outputs diverged; decode stdev rose 0.06 → 3.71 t/s.
- **Impact:** breaks the identical-decision-across-seeds property gate phases rely on.
- **Proposed direction:** optimization contract should define an explicit losslessness probe (N fixed prompts, byte-compare) as an acceptance test before any speed profile is adoptable.
- **Status:** OPEN.

## PF-06 — /props lacks n_slots in b10449 server build
- **Observation:** effective-profile verification via `/props` raised KeyError on `n_slots`; startup log remains authoritative.
- **Proposed direction:** admission harness should read n_slots from log, not /props, for this build lineage.
- **Status:** OPEN (workaround applied).

## PF-07 — Mid-run protocol-tree consolidation broke frozen paths
- **Observation:** `wlep-development/final-hardening/` was reorganized into `welp/` during Phase 9; running processes survived (source already loaded) but new launches would have failed.
- **Impact:** campaign reproducibility risk if harness files are referenced by mutable path.
- **Proposed direction:** campaigns must copy harness files into campaign-local `scripts/` with hashes at freeze time (apodex protocol-snapshot pattern validated this campaign — snapshot copy of soak.py/classify.py kept Phase 9/10 running).
- **Status:** MITIGATED in-campaign; protocol proposal OPEN.

## PF-08 — Phase-4 stop-scope ambiguity in frozen protocol text
- **Observation:** `protocol/WELP.md` summary prose says failing models "stop there instead of consuming unnecessary compute", while the pinned Early-Stop Philosophy note (sha256 `b76daedb…`) gate-flow specifies `Reliability FAIL → classify limitations / potentially STOP` — permissive, and asymmetric vs the mandatory `STOP` after Practical Viability FAIL. Two defensible readings: (A) halt all phases; (B) halt advancement-dependent work, continue characterization.
- **Impact:** conformance adjudication for this campaign required a manual ruling (see WELP-CONFORMANCE.md "conformance ruling", answer B). A future campaign could choose A and call B-campaigns nonconformant.
- **Proposed direction:** WELP v1.0 must state, normatively, which artifacts survive a Phase-4 (and Phase-3) failure: characterization-only modules, context/variance/optimization/soak measurement, and role classification are retained under B; only gate-bearing advancement stops. Codify the Phase-3 vs Phase-4 STOP asymmetry explicitly.
- **Status:** OPEN (protocol-text defect; campaign ruling documented, results unchanged).
