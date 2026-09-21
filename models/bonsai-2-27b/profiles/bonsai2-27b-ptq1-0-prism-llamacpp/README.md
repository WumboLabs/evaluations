<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp PTQ1_0 (reasoning-on, vendor default)

- **Profile ID:** `bonsai2-27b-ptq1-0-prism-llamacpp`
- **Model ID:** `bonsai-2-27b`
- **Status:** historical
- **Artifact identity:** prism-ml/Ternary-Bonsai-2-27B-gguf@6ed5e12b :: Ternary-Bonsai-2-27B-PTQ1_0.gguf (sha256 53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3)
- **Runtime family:** llama.cpp (PrismML-Eng fork)
- **Runtime revision:** 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120
- **Quantization / precision:** PTQ1_0 ternary 1.75 bpw group 128 (Hadamard-rotated basis); f16 K/V cache (FA on)
- **Deployment topology:** Full-GPU PrismML-Eng/llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99, -fa on, f16 KV, -np 1, vendor instruct sampler; REASONING_ON vendor xhigh default (the pinned runtime ignores per-request reasoning budget/effort kwargs; template enable_thinking=false is the only effective control). Second hardware observation: same artifact/source on RTX 2060 SUPER 8GB (SM75 build), practical at 8K.
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-18 — [Current-WELP characterization + compression-retention + RTX 2060 SUPER portability](../../../../models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-20260918/)

## Provenance


Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
