<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp PTQ1_0 (thinking-off)

- **Profile ID:** `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off`
- **Model ID:** `bonsai-2-27b`
- **Status:** current
- **Artifact identity:** prism-ml/Ternary-Bonsai-2-27B-gguf@6ed5e12b :: Ternary-Bonsai-2-27B-PTQ1_0.gguf (sha256 53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3)
- **Runtime family:** llama.cpp (PrismML-Eng fork)
- **Runtime revision:** 9a9394a895b96003ca842a6041cb28ac49a108f7 (prism-b10709-9a9394a, build 10709), CUDA SM120
- **Quantization / precision:** PTQ1_0 ternary 1.75 bpw group 128 (Hadamard-rotated basis); f16 K/V cache (FA on)
- **Deployment topology:** Identical serving geometry to the reasoning-on profile (-ngl 99 full GPU, -fa on, f16 KV, -np 1, vendor instruct sampler) with the single declared delta: reasoning OFF via chat_template_kwargs enable_thinking=false - the only reasoning control proven effective on the pinned runtime. Recommended bounded deployment profile (READY_WITH_GUARDRAILS): pin enable_thinking=false and size generation ceilings to the profile's measured verbosity; verify strict one-shot outputs.
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-20 — [Methodology-revision supplement (thinking-off profile)](../../../../models/bonsai-2-27b/events/bonsai2-27b-rtx5070-welp-methodology-supplement-20260920/)

## Provenance


Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
