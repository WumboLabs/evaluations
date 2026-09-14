# Practical-use verdict + v025 pool comparison

- Event ID: `grug-practical-verdict-2026-07-04`
- Date: 2026-07-04
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Grug-12B Q4_K_M scored 243.6/300 (4.06 avg; 4 pass, 2 mixed) on wumbolabs-practical-use-v1; structurally viable but not a replacement for Gemma 4 12B QAT as the 12GB practical default. 66.65 tok/s avg generation, 8485 MiB peak VRAM.

## Provenance

Derived from retained local WumboLabs evidence; see `provenance.json` for the exact
source artifact identities and SHA-256 hashes consumed for this repository. The
underlying run trees remain in the local LLMGauge/LocalMaxxing archives; no raw
internal bundles are published here.

Results are bounded by the tested artifact, runtime, hardware, suite, and settings,
and are not universal model rankings.
