<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp Q4_K_M (Thinking)

- **Profile ID:** `mellum2-12b-a2.5b-llamacpp-q4km-thinking`
- **Model ID:** `mellum2-12b-a2.5b`
- **Status:** current-alternate
- **Artifact identity:** JetBrains/Mellum2-12B-A2.5B-Thinking-GGUF-Q4_K_M
- **Runtime family:** llama.cpp
- **Runtime revision:** b9672 (74ade5274), CUDA SM120
- **Quantization / precision:** Q4_K_M weights; f16 K/V cache (FA on)
- **Deployment topology:** Full-GPU llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (28/28 layers GPU-resident, no offload), -np 1, --no-cache-prompt --cache-ram 0 for uncached measurement; reasoning ON (Thinking is the official explicit-CoT checkpoint; reasoning_content emitted by the native template)
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-06-17 — [Agent backend fit test (64k, Instruct + Thinking)](../../../../models/mellum2-12b-a2.5b/events/mellum2-agent-backend-64k-2026-06-17/)
- 2026-07-04 — [12B practical pool comparison v025 + Grug](../../../../shared-events/practical-use-comparison-2026-07-04/)
- 2026-09-16 — [Current-WELP recharacterization](../../../../models/mellum2-12b-a2.5b/events/mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16/)

[Supporting public evidence](supporting-evidence/) retains unindexed historical reports and reproduction artifacts without inventing new event identities.

## Provenance

- [WumboLabs/eval-mellum2-12b-a2.5b-thinking @ `294840163db9f3f6ecc19c8767b975aa003314f1`](https://github.com/WumboLabs/eval-mellum2-12b-a2.5b-thinking/blob/294840163db9f3f6ecc19c8767b975aa003314f1/profile.json)

Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
