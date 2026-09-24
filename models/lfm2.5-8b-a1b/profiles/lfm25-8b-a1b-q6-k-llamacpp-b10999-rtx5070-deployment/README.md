<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp upstream official Q6_K (reasoning-on, publisher sampler)

- **Profile ID:** `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment`
- **Model ID:** `lfm2.5-8b-a1b`
- **Status:** current
- **Artifact identity:** LiquidAI/LFM2.5-8B-A1B-GGUF@49c14831 :: LFM2.5-8B-A1B-Q6_K.gguf (sha256 7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6)
- **Runtime family:** llama.cpp (upstream)
- **Runtime revision:** b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120
- **Quantization / precision:** Q6_K official publisher GGUF; f16 K/V cache (FA on)
- **Deployment topology:** Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (25/25 layers), -fa on, f16 KV, -np 1, --fit off, embedded Jinja template, publisher sampler (temp 0.2 / top_k 80 / top_p 1.0 / repeat_penalty 1.05); effective reasoning ON (template flags do not disable generation). Default context 32,768 / native exact 128,000; uncached scientific arms via --cache-ram 0 --no-cache-prompt --slot-prompt-similarity 0 with cache_prompt:false (proven by repeated-prompt probe).
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-23 — [Prospective retest with reliability-class calibration and proven uncached timing (official Q6_K, upstream llama.cpp b10999)](../../../../models/lfm2.5-8b-a1b/events/lfm25-8b-a1b-rtx5070-welp-20260923/)

## Provenance


Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
