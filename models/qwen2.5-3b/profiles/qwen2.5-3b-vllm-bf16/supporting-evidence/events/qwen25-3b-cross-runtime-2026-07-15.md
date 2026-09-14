# Cross-runtime comparison: llama.cpp F16 vs vLLM BF16

- Event ID: `qwen25-3b-cross-runtime-2026-07-15`
- Date: 2026-07-15
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

LLMGauge cross-runtime methodology study with model-specific results: Qwen2.5-3B Instruct as F16 llama.cpp vs BF16 vLLM agent-backend comparison incl. failed-command-recovery probes. Primary subject is cross-runtime methodology; the Qwen2.5-3B results are retained as its benchmark-only evidence. Archaeology separately cites a full Qwen2.5-3B quant-lab record set (F16/Q8_0/Q6_K/Q5_K_M/Q4_K_M/IQ4_XS) from the Arch era.

## Provenance

Derived from retained local WumboLabs evidence; see `provenance.json` for the exact
source artifact identities and SHA-256 hashes consumed for this repository. The
underlying run trees remain in the local LLMGauge/LocalMaxxing archives; no raw
internal bundles are published here.

Results are bounded by the tested artifact, runtime, hardware, suite, and settings,
and are not universal model rankings.
