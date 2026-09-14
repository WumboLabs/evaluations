# 12B Gemma practical-use test (QAT vs UD-Q5 vs Gemmable)

- Event ID: `gemma4-12b-practical-use-family-2026-06-21`
- Date: 2026-06-21
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Gemma 4 12B IT QAT UD-Q4_K_XL scored 259.2/300 (4.32 avg, 73.45 tok/s) vs UD-Q5_K_XL 254.0/300 (4.23); QAT Q4 selected as best overall practical variant. Shared report also tested Gemmable 4 12B MTP Q4_K_M (119.8/300) on the same suite — that model carries its own Evaluation page.

## Provenance

Derived from retained local WumboLabs evidence; see `provenance.json` for the exact
source artifact identities and SHA-256 hashes consumed for this repository. The
underlying run trees remain in the local LLMGauge/LocalMaxxing archives; no raw
internal bundles are published here.

Results are bounded by the tested artifact, runtime, hardware, suite, and settings,
and are not universal model rankings.
