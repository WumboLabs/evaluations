# Gemma 4 12B IT — current-WELP recharacterization (RTX 5070 12GB)

- Event ID: `gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12`
- Event type: CURRENT_WELP_RECHARACTERIZATION
- Date: 2026-09-12 (executed 2026-09-12/13; published 2026-09-13)
- Evidence maturity: **CURRENT_WELP**
- Evidence scope: performance, quality, capabilities, reasoning, coding, tools, reliability, context envelope, text-profile LocalMaxxing measurement
- Hardware: WumboJetsII (RTX 5070 12GB)
- Outcome: **PASS** — Classification: **READY_WITH_GUARDRAILS**

## Summary

Gemma 4 12B IT recharacterized under the current WumboLabs Evaluation
Lifecycle Protocol on the canonical practical profile: Unsloth
UD-Q4_K_XL packaging of the Google QAT Q4_0 lineage (SHA-256
`90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e`,
7,366,423,360 bytes, source revision `fc034cfff751157913579611efad8462ac1be606`),
served by llama.cpp b9672 (74ade5274, CUDA SM120) with full GPU residency.

- Quality: 12/12 frozen mechanical screen (frozen scorer, temp 0).
- Capabilities: reasoning (thinking mode), executable coding, and
  tool-calling with grounded continuation all PASS.
- Performance: pp512 3,201 tok/s; tg128 72.92 tok/s (5-rep bench);
  near-full prefill degrades 2,855 → 1,397 tok/s across the ladder.
- Reliability (20-task mechanical corpus, 2 seeds): 11/20 and 10/20.
  Guardrails: verbosity/token-cap truncation, git-safety advisory
  weakness, uncertainty and sycophancy weakness.
- Context envelope COMPLETE (text profile): native rungs 8K/16K/32K/
  64K/128K VALIDATED with near-full performance; useful-context at
  131,072 passes all five gates at both seeds at 99.5% near-full
  occupancy. The exact native maximum 262,144 is **FIT_LIMIT** on a
  12 GB card (measured admission failure + KV-slope accounting; nearest
  measured boundary 131,072). No official extension mechanisms are
  documented by the upstream model cards.
- Practical default 32,768 (~8.4 GiB VRAM); guarded 131,072.
- Multimodal (image/audio/video via mmproj) is officially supported but
  **SUPPORTED_NOT_CHARACTERIZED**: this campaign characterized the
  canonical TEXT profile only; no model-wide multimodal claim is made.
- LocalMaxxing: MEASURED_NOT_SUBMITTED (canonical-profile local
  benchmark pp512 3,201 / tg128 72.92 tok/s; live submission is
  human-gated and did not occur).

## Relation to historical events

The 2026-06-21 practical-use event (259.2/300 manual score), the 2026-06-16
scored runs, the honesty-ladder smoke, and the 2026-07-04 LMX speed records
remain valid HISTORICAL evidence, unchanged. This event supersedes them as
the current characterization only; no protocol score equivalence between the
practical-use suite and current-WELP surfaces is claimed.

## Provenance

Derived from retained local WumboLabs campaign evidence; see
`provenance.json` for the exact source identities and SHA-256 hashes
consumed for this repository. The full local campaign bundle
(`REPORT.md`, `WELP-LAB-RECORD.md`, raw runs, fixtures, and telemetry)
remains in the local research workspace; only public-safe derivatives
are published here.

Results are bounded by the tested artifact, runtime, hardware, suite,
context rungs, and settings, and are not universal model rankings.
