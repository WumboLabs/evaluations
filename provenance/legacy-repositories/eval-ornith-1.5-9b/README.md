# WELP Campaign: Ornith-1.5-9B (Q4_K_M) on RTX 5070 12 GB

Full WELP (WumboLabs Evaluation Lifecycle Protocol) campaign record for
`ornith-ai/Ornith-1.5-9B`, GGUF Q4_K_M, served locally by llama.cpp b10449
(commit 0d9ceae1) on a single RTX 5070 12 GB host (alias WumboJetsII).

Campaign id: `ornith-1.5-9b-welp-2026-08-27`. Protocol snapshot:
`welp-next-snapshot-2026-08-26-post-rename` (DRAFT, naming-only migration).

## Headline results

| Phase | Result |
|---|---|
| Admission | PASS (identity, artifact sha256, template, runtime all verified) |
| Performance | decode 102.04 ± 0.06 t/s, prefill 4046.67 ± 15.68 t/s, TTFT(first-token est) 46.72 ms |
| Practical viability | 83/90 = 0.922, all gates G1–G5 PASS → ADVANCE |
| Reliability | G6 = 1/21 = 0.0476 FAIL → DO_NOT_ADVANCE (dominated by scorer-lexicon false negatives; see PF-04/PF-06) |
| Capability modules | characterization only (no gates exist; decision D4) |
| Context | useful context 24576; 32768 rung INCONCLUSIVE (PF-02) |
| Variance | 7/9 tasks STABLE; ESCALATE_TO_5: linux_systems (0.1819), reasoning-off (0.20) |
| Optimization | MTP draft +9.9% decode but output-divergent → REJECTED_FOR_CANONICAL |
| Soak | screening (30 min) clean: 0 effective errors, tps drift −0.02%, RSS flat, 0 Xid |
| Classification | roles = [] → NOT_READY |

## External records

- LocalMaxxing speed result: submitted and APPROVED, id
  `cmtc6sopl0007o601d7hqrj1z` (decode 102.04 t/s, prefill 4046.67 t/s,
  Q4_K_M, llama.cpp b10449, RTX 5070 12 GB; model page
  <https://www.localmaxxing.com/en/models/ornith-ai/Ornith-1.5-9B>).

## Layout

- `report.md` — narrative campaign report
- `WELP-CONFORMANCE.md` — phase-by-phase conformance determination
- `protocol-findings.md` — PF-01…PF-08 protocol/process findings
- `MODEL.md` / `model-manifest.json` — evaluated-model identity + provenance
- `summaries/` — one machine-readable JSON per phase + campaign manifest
- `contracts/`, `corpus/`, `scorers/`, `scripts/`, `harness/` — hash-pinned evaluation artifacts
- `results/`, `calibration/` — raw and scored run evidence
- `publication/` — publication status records
- `publication-allowlist.json`, `PUBLICATION-MANIFEST.json`,
  `publication-policy.json`, `PUBLICATION-POLICY.md` — allowlist-first publication controls

## Reproducing

Every JSON in `summaries/campaign_manifest.json` is sha256-pinned. Start the
server exactly as in `summaries/launch_command.txt` (paths are host-relative
placeholders `<USER_HOME>`), then run the corresponding `scripts/` entry with
the pinned contract and sampling files. Single-runtime rule: one
`llama-server` instance at a time.

## Caveats

- Phase-2 raw per-repetition files (`results/phase2_raw.jsonl`,
  `results/phase2_summary.json`) are MISSING from the evidence tree
  (INVALIDATED_RETAINED in the manifest); per-rep values survive in
  `summaries/performance.json`.
- Reliability G6 failure is characterized as scorer-lexicon artifact, not a
  clean model-capability signal; adjudication notes in `protocol-findings.md`.
- Producer claims reviewed against model card revision 489cb979 in
  `summaries/producer_claims.json`.
