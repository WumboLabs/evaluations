# WumboServer RTX 2060S admission/boundary + LocalMaxxing (Q4/Q5/Q6)

- Event ID: `qwen38-empero-9b-distill-wumboserver-2026-09-01`
- Date: 2026-09-01
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboServer (RTX 2060 SUPER 8GB)

empero-ai/Qwen3.8-9B-Distill-GGUF Q4_K_M/Q5_K_M/Q6_K on WumboServer RTX 2060S: admission benchmark, Q6 fit boundary, Q5 WELP-style serving campaign, and LocalMaxxing reconciliation (9b-q4 60.4 tok/s out, 5.37 GB peak VRAM). Hardware-lane evidence; Ornith-9B admission on the same GPU is recorded under its own model.

## Provenance

Derived from retained local WumboLabs evidence; see `provenance.json` for the exact
source artifact identities and SHA-256 hashes consumed for this repository. The
underlying run trees remain in the local LLMGauge/LocalMaxxing archives; no raw
internal bundles are published here.

Results are bounded by the tested artifact, runtime, hardware, suite, and settings,
and are not universal model rankings.
