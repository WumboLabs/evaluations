# WLEP Conformance — apodex-1.1-mini (2026-08-25)

Protocol: `wlep-next-snapshot-2026-08-25-end-to-end` (DRAFT — NOT v1.0).
Verification at campaign start: 27/27 vault note hashes matched; 29/29 executable artifact SHA-256 verified; immutable snapshot copy hashed into `protocol-snapshot/campaign-snapshot-manifest.json` (303 files).

## Phase ledger

| Phase | Status | Detail |
|---|---|---|
| 0 Provenance | COMPLETE | upstream @62583b46 verified live; community GGUF @59afa578 traced to it |
| 1 Admission IQ2_M full-GPU | FAIL (deterministic) | weights 11.43 GB > 10.87 GB free VRAM |
| 1 Admission IQ1_M full-GPU | PASS | full GPU placement proven (RSS 74 MB vs 9.7 GB VRAM) |
| 2 Performance | COMPLETE | decode 169.4 t/s ±1.7 · prefill 1798.8 t/s ±11.2 · TTFT ~125 ms short-prompt |
| 3 Practical Viability | **DO_NOT_ADVANCE** | G1 FAIL all seeds · G2 FAIL seeds 42/43 · decision seed-stable |
| 4–10 | NOT_REACHED | early stop mandated by Early-Stop Philosophy |
| OMP Stage 1 smoke | PASS (integration) | implicit llama.cpp discovery, isolated profile `wlep-apodex` |
| OMP Stage 2 | NOT_REACHED | gated on Phase 4 ADVANCE |

Stop phase: **3**. Stop reason: frozen Phase-3 gate failure ⇒ bounded report + STOP.

## Gate decisions
1. Canonical quant = IQ1_M (`1e84d8ad…`); IQ2_M rejected on deterministic allocation arithmetic (D2). Frozen before canonical testing.
2. Runtime pinned at f280b269 in a campaign-local tree; existing trees untouched (D3).
3. Gate baseline reasoning state = OFF, enforced server-side `-rea off` after a think-budget-starved pass was invalidated (D1, PF-02).
4. Phase 3 verdict DO_NOT_ADVANCE — robust to the recorded scorer lexicon defect (PF-05).

## Protocol changes during run
**NO.** Contracts, scorers, schemas, thresholds untouched. Campaign-local harness revisions for Phase 2 measurement are documented deltas with retained originals (`results/INVALIDATED-phase2-run*.jsonl`).

## Defects & findings
- SC-01 scorer lexicon recall gaps (8 artifact fails; gate outcome unaffected)
- HF-01/02/03 frozen Phase-2 harness defects; HF-04 latent argv bug in reliability runner
- AMB-01/02 ambiguities resolved as documented decisions D1/D4
- Full register: `protocol-findings.md` (PF-01 … PF-06)

## Undocumented decisions required (D1–D5)
See `summaries/wlep_conformance.json` — each is evidence-backed and none altered a threshold or contract.

## Verdict
**The end-to-end frozen WLEP ran this completely fresh, highly agentic MoE model through every phase it reached without structural change.** All stopping behavior matched the protocol exactly. This campaign counts as additional convergence evidence toward v1.0 candidacy.
