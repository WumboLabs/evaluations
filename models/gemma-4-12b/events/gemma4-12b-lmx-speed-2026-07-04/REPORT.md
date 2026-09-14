# LMX speed runs across four Gemma 4 12B quants

- Event ID: `gemma4-12b-lmx-speed-2026-07-04`
- Date: 2026-07-04
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboJetsII (RTX 5070 12GB)

LMX local speed evidence: Q4_K_M 72.11, UD-Q5_K_XL 62.76, UD-Q6_K_XL 51.26 tok/s out (llama.cpp). Archaeology additionally cites Q8_0 test and NVFP4 conversion-attempt records (weights since removed).

## Provenance

Derived from retained local WumboLabs evidence; see `provenance.json` for the exact
source artifact identities and SHA-256 hashes consumed for this repository. The
underlying run trees remain in the local LLMGauge/LocalMaxxing archives; no raw
internal bundles are published here.

Results are bounded by the tested artifact, runtime, hardware, suite, and settings,
and are not universal model rankings.
