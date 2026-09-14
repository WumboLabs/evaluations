# Qwen3.8-27B — current RTX 5070 H1 canonical profile (public summary)

Follow-up to the historical eval-qwen3.8-27b evaluation. The historical
evaluation remains valid for its tested stack (Unsloth UD-Q2_K_XL GGUF,
llama.cpp b10449, campaign 2026-08-14..21). The canonical serving stack has
since evolved substantially; this document describes the CURRENT canonical
profile only and supersedes nothing.

Campaigns: `e18h-h1-candidate-validation-2026-09-08` (PASS; H1 validated as
candidate, not promoted) and `e18i-h1-canonical-promotion-2026-09-09`
(PASS — E18I_H1_CANONICAL_PROMOTION_COMPLETE).

## Current canonical profile

- Artifact: `Qwen3.8-27B-SC_2.20bpw_H3_V3` (EXL3, 2.20 bpw; q4 target KV;
  q4 draft KV).
- Runtime: ExLlamaV3 1.4.6+cu128.torch2.10.0; context 65,536; MTP width 1;
  batch 1; max_chunk 256.
- Recurrent history: **H1** (max_history 1) — promoted from H4 by E18I after
  E18H validated the candidate. Explicit H4 fallback remains available in
  the same launcher (`--max-history 4`).
- Placement: CPU embedding lookup (not transformer-layer offload); all 64
  transformer blocks GPU-resident. Recovered memory (434.8125 MiB) is
  retained as unspent reserve, not spent on context or batch growth.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB, Ryzen 7 9800X3D.

## Measured H1 evidence

- Recurrent/GDN storage: **292.6875 MiB (H1)** vs 727.5 MiB (H4) — measured
  reduction 434.8125 MiB.
- E18E corrected combined oracle (exact frozen inputs): **3/3 requests,
  15/15 target fields exact** on H1 (actual prompt tokens 58,849 / 58,902 /
  58,883).
- Seven-check quality fixture (retained E3 source, all three E18H arms):
  7/7 PASS.
- 20-request bounded stability sequence: 20/20 exact, HTTP 200 throughout,
  allocator blocks exactly flat (zero growth, zero slope).
- Performance (E18H arm-B H1 medians; frozen 3,514-token prompt, MTP width 1
  active): TTFT 4.4487 s; prefill 789.89 tok/s; decode 75.79 tok/s; all
  frozen regression gates PASS (B within the favorable direction of the H4
  spread for every metric). H1 oracle-minimum free 1,888 MiB vs 1,470 MiB
  (H4). Zero CUDA/OOM/Xid in both campaigns.
- LocalMaxxing (current H1 profile, 65,536): tokSOut 75.4, TTFT 71.35 ms,
  submission `cmtwcncwr07f4ps01ef75q6ne` (APPROVED, NEW; verifiedRun false;
  disclosed: MTP acceptance counters not exposed by the canonical wrapper —
  none fabricated).

## Boundaries

- H1 is canonical only for this exact artifact/runtime and text-only
  width1/batch1 surface. No width>1, batch>1, multimodal, tensor-parallel,
  other architecture/artifact/runtime release, or recurrent-geometry
  validation is implied.
- No full model-card context campaign exists for this profile; the inherited
  oracle evidence is at ~58.8K actual inputs, and no context growth or
  recovered-memory spending is authorized.
- Historical model-role findings (reliability/hallucination statistics,
  strict interfaces, native tools) belong to the historical tested stack and
  are not superseded by this profile work.

Canonical scientific authority: the local E18H/E18I evidence bundles. This
summary is a public derivative; the campaigns' `REPORT.md` files govern on
any conflict.
