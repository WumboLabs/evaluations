<!-- Generated from registry metadata — do not hand-edit. -->

# ExLlamaV3 H1 (SC_2.20bpw_H3_V3)

- **Profile ID:** `qwen38-27b-exl3-h1`
- **Model ID:** `qwen38-27b`
- **Status:** current
- **Artifact identity:** Qwen3.8-27B-SC_2.20bpw_H3_V3 (EXL3)
- **Runtime family:** ExLlamaV3
- **Runtime revision:** 1.4.6+cu128.torch2.10.0
- **Quantization / precision:** 2.20 bpw EXL3; q4 target KV; q4 draft KV; MTP width 1
- **Deployment topology:** MTP width 1, batch 1, max_chunk 256, recurrent history H1 (max_history 1) with explicit H4 fallback via --max-history 4; CPU embedding lookup (not transformer-layer offload); all 64 transformer blocks GPU-resident
- **Hardware:** WumboJetsII (NVIDIA GeForce RTX 5070 12GB, SM120)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-09 — [H1 deployment / canonical promotion](../../../../models/qwen38-27b/events/h1-canonical-promotion-2026-09-09/)
- 2026-09-12 — [Context envelope completion](../../../../models/qwen38-27b/events/context-envelope-completion-2026-09-12/)

[Supporting public evidence](supporting-evidence/) retains unindexed historical reports and reproduction artifacts without inventing new event identities.

## Provenance

- [WumboLabs/eval-qwen3.8-27b-exl3-h1 @ `484c9184ae459c79754b77b7dc95da09e64d37a5`](https://github.com/WumboLabs/eval-qwen3.8-27b-exl3-h1/blob/484c9184ae459c79754b77b7dc95da09e64d37a5/profile.json)

Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
