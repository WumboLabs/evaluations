# WumboLabs Model Evaluation Report — Ornith 1.5 9B

Campaign: `ornith-1.5-9b-welp-2026-08-27` · Protocol: WELP `welp-next-snapshot-2026-08-26-post-rename` (DRAFT)
Declared objective: TEXT + REASONING + CODING + TOOLS + AGENTIC USE · Host: WumboJetsII (RTX 5070 12 GB)

---

## 1. Final classification

| Field | Value |
|---|---|
| **Outcome** | **NOT_READY** (Phase 10, deterministic engine) — 0 deployment roles earned |
| Blocking gate | Phase 4 Reliability **DO_NOT_ADVANCE** (G6 hallucination rate 1/21 = 0.0476 > threshold) |
| Earned evidence | Phase 3 ADVANCE (0.922, all gates); strong coding 0.867 / structured-interfaces 0.875 / tools 0.80; clean soak; useful context 24576 |
| NOT_REACHED | omp_local_agent module (auto-blocked by Phase 4), LOCKIN soak, vision module |
| NOT_APPLICABLE ≠ FAIL | Phase 5 gates (characterization-only per frozen decision D4); 32768 context rung (harness overshoot, INCONCLUSIVE) |

Per protocol semantics, NOT_READY is a role verdict, not a capability verdict: the model passed practical viability and most capability characterization; one reliability gate failure (with documented scorer-lexicon contamination, PF-01) closes all deployment roles.

## 2. Model identity

- Upstream `ornith-ai/Ornith-1.5-9B` @ `489cb97981b8654bcfcf30ce1f94ed1b62e07b53`; hybrid attention (full_attention_interval 4), trained ctx 262144 (producer claim, reported separately).
- Canonical artifact: `Ornith-1.5-9B-Q4_K_M.gguf`, sha256 `70c112196e0b7023803c9762752e46d29e612a92c83f995bc3ba1ceb07e8fab6`.
- Native MTP head present (`blk.32.nextn.*`) — used only in Phase 8 experiment.
- mmproj BF16 available; vision **NOT_EVALUATED** (frozen applicability).

## 3. Runtime & environment

llama.cpp b10449 @ `0d9ceae1e38291035605613ab41a8f5e693d6fcd`, CUDA 13.3, driver 610.57.04, sm_120 build `build-cuda-sm120-new`. Runtime LEAVE_IN_PLACE policy; hashes in `summaries/toolchain_inventory.json`.

## 4. Serving profile (frozen canonical baseline)

`-c 32768 -ngl 99 --parallel 1 --fit off -fa on --jinja --reasoning off`, b 2048/ub 512, speculation none. Gate baseline reasoning state REASONING_OFF (requested + effective recorded in manifest; 0 leaks across 624 rows). Single-runtime rule enforced by sequential instance swaps (canonical 8931 / no-cache 8932 / MTP swap).

## 5. Performance (Phase 2)

| Metric | Result |
|---|---|
| Decode | **102.04 ± 0.06 t/s** (5 reps, 200→1024) |
| Prefill 4k (no-cache) | **4046.67 ± 15.68 t/s** |
| TTFT (est.) | 46.72 ms |
| Warm reload | 0.76 s |

## 6. Practical viability (Phase 3) — ADVANCE

83/90 = **0.922**. G1 0.922 ≥ 0.75 · G2 0.6/0.8/0.8 ≥ 0.6 · G3 1.0 ≥ 0.5 · G4 1.0 ≥ 0.7 · G5 identical ADVANCE decision on seeds 42/43/44. Per-seed: 0.900/0.933/0.933.

## 7. Reliability (Phase 4) — DO_NOT_ADVANCE

162/162 rows. G1 aggregate 0.4877 PASS · G2 hallucination-on-false-premise 0.1296 PASS · G3 refusal-drift 0.0185 PASS · G4 UNSAFE = 0 · G5 seed range 0.0926 PASS · **G6 1/21 = 0.0476 FAIL**. Manual review: dominant failure mode is scorer-lexicon false-negatives (PF-01); mechanical gate stands authoritative.

## 8. Capability modules (Phase 5) — characterization only

| Module | Rate | Failure character |
|---|---|---|
| structured_interfaces | 63/72 = 0.875 | genuine contract violations (enum/extract/limit) |
| extraction_rag | 39/54 = 0.722 | extra prose after correct answer; one conflict-task flip |
| linux_systems | 34/66 = 0.515 | vocabulary variants (PF-01) dominate |
| coding | 78/90 = 0.867 | 3 tasks fail all seeds (executed, returncode 1) |
| native_tools | 48/60 = 0.80 | 5 HALLUCINATED_RESULT, 7 MATERIAL_DEFECT |
| reasoning | off 17/30, on 17/30 (Δ 0) | incl. contract ground-truth defect PF-04; thinking ON costs +27 % wall for zero accuracy gain |

## 9. Context (Phase 6)

useful_context = **24576** (3/3 PASS incl. absent-evidence screening). 4096, 16384 PASS. 32768 INCONCLUSIVE: harness overshoot → HTTP 400 (PF-02); not a behavioral failure.

## 10. Variance (Phase 7)

7/9 STABLE. ESCALATE_TO_5: linux_systems (range 0.1819), reasoning-off (0.20). All gate decisions individually seed-stable.

## 11. Optimization (Phase 8)

MTP self-draft: 112.16 ± 3.71 t/s (**+9.9 %**) but not output-lossless (1/6 probe divergence, PF-05) → **BASELINE RETAINED**; MTP profile = conditional speed-role only.

## 12. Stability (Phase 9)

SCREENING 30 min: 11449 requests, **0 real errors** (reported 5724 = harness artifact, PF-03), tps drift −0.02 %, RSS flat 1950244 kB × 62 samples, 0 Xid/GPU events. LOCKIN NOT_REACHED (precluded by Phase 4).

## 13. Reproduction

`scripts/` + `scorers/` + `contracts/` + `corpus/` hash-pinned in `sources/dataset_inventory.json`; server relaunch command in manifest `reproduction`; artifact index with sha256 per artifact (final count in `summaries/campaign_manifest.json`; growth/reconciliation documented in `summaries/artifact_reconciliation.json`).

## 14. Invalidated runs
- Phase 2 prefill on cache-enabled instance (invalidated; re-run no-cache 8932).
- Phase 6 rung-32768 seeds 42/43 (transport rejection; INCONCLUSIVE).
- Phase 9 error counter (harness KeyError; effective 0).

## 15. Publication & closeout
- Conformance ruling (Phase-4 block vs later characterization): **B — conformant**. Frozen gate-flow + CHARACTERIZATION_ONLY module contracts + applicability freeze + roles=[] semantics permit post-block characterization; WELP.md "stop there" prose ambiguity filed as **PF-08**. Full analysis in `WELP-CONFORMANCE.md`.
- Artifact index grew 43 → 54 → 62 entries (freeze → publication v1 → closeout); per-entry sha256 re-verification, 4 stale-hash refreshes, and the phase2_raw/phase2_summary missing-file defect (INVALIDATED_RETAINED, null hash; per-rep values in `summaries/performance.json` remain authoritative) are documented in `summaries/artifact_reconciliation.json`.
- Publication package: `publication/repo-candidate/` (86 files) passes `welp/validators/validate_public_tree.py` with 0 errors / 0 findings; 8 leaking evidence files published as sanitized copies (`/home/<user>` → `<USER_HOME>`); root files README/MODEL/model-manifest/PUBLICATION-POLICY/publication-policy/allowlist/manifest/.gitignore authored.
- Package records (no submissions): LocalMaxxing `localmaxxing/package-record.json` NOT_SUBMITTED (payload ready, awaiting explicit authorization); labs catalog + WumboCore routing entries added (ornith NOT_READY).
- Verdict: **READY_FOR_PUBLICATION** at the human git gate; GitHub/LMX/X/WumboCore actions remain NOT_AUTHORIZED.
