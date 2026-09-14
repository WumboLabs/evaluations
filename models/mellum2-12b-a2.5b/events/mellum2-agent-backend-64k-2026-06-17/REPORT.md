# Agent backend fit test (64k, Instruct + Thinking)

- Event ID: `mellum2-agent-backend-64k-2026-06-17`
- Date: 2026-06-17
- Evidence maturity: **SPECIALIZED_TEST**
- Evidence scope: specialized, agent-backend
- Hardware: WumboJetsII (RTX 5070 12GB)

Instruct + Thinking Q4_K_M through LLMGauge agent-backend-v1 at 64k on WumboJetsII. 64k fit confirmed (Instruct 5/5 complete, 251.0-257.2 tok/s out, 9203 MiB peak VRAM). Manual scores: Instruct preferred (overall trust 3.7/5) over Thinking; neither safe for unsupervised shell/systemd operations. Not a general model-quality verdict.

## Provenance

Derived from retained local WumboLabs evidence; see `provenance.json` for the exact
source artifact identities and SHA-256 hashes consumed for this repository. The
underlying run trees remain in the local LLMGauge/LocalMaxxing archives; no raw
internal bundles are published here.

Results are bounded by the tested artifact, runtime, hardware, suite, and settings,
and are not universal model rankings.
