# WELP Conformance — ornith-1.5-9b (2026-08-27)

Protocol: `welp-next-snapshot-2026-08-26-post-rename` (DRAFT — NOT v1.0). Snapshot manifest sha256 `32c38e2a…` (verified against live `welp/snapshot-freeze/manifest.json`), tree sha256 `8b68e316…` — **stale**: computed mid-migration (PF-07); the campaign-local `protocol-snapshot/` copy is byte-identical to the current `welp/` HEAD tree `5ece8f9` (find|sort|xargs cat | sha256 = `83e2a3ec…` both sides; diff clean). Every hash in `sources/dataset_inventory.json` resolves to a file inside the campaign copy (verified 2026-08-27), so campaign binding is intact.
Campaign: `ornith-1.5-9b-welp-2026-08-27` · Host WumboJetsII (RTX 5070 12 GB) · Model `Ornith-1.5-9B-Q4_K_M.gguf` sha256 `70c11219…` (upstream revision `489cb979`).

## Phase ledger

| Phase | Status | Detail |
|---|---|---|
| 0 Provenance | COMPLETE | upstream @489cb979 verified; GGUF hash-pinned; llama.cpp b10449 @0d9ceae1 pinned |
| 1 Admission | PASS | full-GPU placement proven (6.77 GB VRAM, RSS ~1.1 GB); warm load 0.76 s |
| 2 Performance | COMPLETE | decode 102.04 ± 0.06 t/s · prefill 4046.67 ± 15.68 t/s · TTFT est 46.72 ms |
| 3 Practical Viability | **ADVANCE** | 83/90 = 0.922; G1–G5 all PASS (G2 boundary 0.600 seed 42) |
| 4 Reliability | **DO_NOT_ADVANCE** | G1 0.4877 · G2 0.1296 · G3 0.0185 · G4 UNSAFE=0 · G5 range 0.0926 · **G6 1/21 = 0.0476 FAIL** |
| 5 Capability Modules | FINAL_CHARACTERIZATION | si 0.875 · rag 0.722 · linux 0.515 · coding 0.867 · tools 0.80 · reasoning 0.567 (off=on, Δ0); omp_local_agent NOT_REACHED (Phase-4 gate); vision NOT_EVALUATED |
| 6 Context | FINAL_USEFUL_24576 | 4096/16384/24576 PASS 3/3; 32768 INCONCLUSIVE (harness tokenization overshoot → HTTP 400; never entered model) |
| 7 Variance | FINAL_CHARACTERIZED | 7/9 STABLE; ESCALATE_TO_5: linux_systems (0.1819), reasoning-off (0.20) |
| 8 Optimization | OPTIMIZED_PROFILE_FOUND | MTP draft: +9.9 % decode (112.16 ± 3.71) but 1/6 probe outputs diverge → baseline RETAINED for gate work |
| 9 Soak | SCREENING_PASS | 11449 req / 0 real errors / tps drift −0.02 % / RSS flat / 0 Xid; LOCKIN NOT_REACHED (precluded by Phase 4) |
| 10 Classification | **NOT_READY** | classify.py deterministic: 0 roles earned (Phase 4 DO_NOT_ADVANCE + D4 characterization-only) |

## Gate decisions (frozen before use)
1. Canonical serving profile frozen pre-campaign: ctx 32768, parallel 1, fit off, fa on, b 2048/ub 512, REASONING_OFF, speculation none.
2. Gate baseline reasoning state = REASONING_OFF (server `--reasoning off` + per-request `enable_thinking=false`); 0 reasoning leaks across 624 gate/characterization rows.
3. Phase 5 applicability frozen before execution (b51bb36e…), grounded in pinned card @489cb979.
4. Phase 5 = characterization only (decision-log D4: no honest gate thresholds at 4-control calibration).
5. Mechanical gates authoritative; manual review annotates scorer-lexicon artifacts only; MINOR_DEFECT reclassification cannot alter CLEAN_PASS counts → Phase-4 DO_NOT_ADVANCE stands.
6. finish=length with non-empty output = valid truncation (empty-length finish invalidates a pass — frozen precedent applied throughout).

## Protocol changes during run
**NO.** Contracts, scorers, schemas, thresholds untouched. All scorer/contract artifacts hash-pinned in `sources/dataset_inventory.json` before use. One campaign-local harness revision: Phase-2 script repair (documented, retained).

## Invalidated / documented runs
- Phase 2 prefill on cache-enabled instance → invalidated, re-run on dedicated no-cache port 8932.
- Phase 6 rung 32768 seeds 42/43 → HTTP 400 transport rejection (harness overshoot), recorded INCONCLUSIVE, not counted as behavioral failure.
- Phase 9 harness `errors: 5724` → proven false (soak.py s2 sentinel KeyError after successful response); effective 0 errors.

## Phase-4 post-block characterization — conformance ruling
**RULING: CONFORMANT (B), with protocol ambiguity filed as PF-08.** After Phase 4 DO_NOT_ADVANCE, the campaign continued Phases 5–9 as characterization and stopped role advancement. Authority, all frozen pre/post-campaign and hash-pinned:
1. Early-Stop Philosophy note (pinned sha256 `b76daedb…`, snapshot-freeze manifest `note_hashes`): gate flow reads `Reliability ├─ FAIL → classify limitations / potentially STOP` — STOP is permissive ("potentially"), classification-after-failure is the named behavior. Contrast Phase 3: `FAIL → bounded report + STOP` (mandatory). The asymmetry is deliberate in the frozen text.
2. `protocol/WELP.md` summary prose ("stop there instead of consuming unnecessary compute") is compute-saving rationale, not a normative all-work termination rule; it does not override the gate-flow note.
3. All Phase 5 module contracts are CHARACTERIZATION_ONLY in the frozen index; decision-log D4 issues no gates. Characterization cannot "advance" anything, so it cannot violate an advance-block.
4. Campaign-side freeze: `summaries/phase5_applicability.json` gates omp_local_agent on Phase 4 CLEAN_PASS → NOT_RUN. Role eligibility was closed at the gate; classify.py deterministically returned roles=[] (Phase 10), consistent with the block.
5. No later-phase result was used to soften the Phase-4 decision anywhere: DO_NOT_ADVANCE stands in manifest, report, conformance, and classification.
Later runs were retained (never deleted) and labeled characterization. The residual ambiguity — whether "stop there" mandates halting all phases — is a protocol-text defect, filed as PF-08.

## Findings
PF-01…PF-08 in `protocol-findings.md`; machine-readable classification (defect classes vs genuine model failures) in `summaries/protocol_findings.json`.
