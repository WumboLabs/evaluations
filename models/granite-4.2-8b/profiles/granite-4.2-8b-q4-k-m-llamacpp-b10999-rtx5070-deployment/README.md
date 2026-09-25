<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp official Q4_K_M (reasoning-on, deployment sampler, 32K)

- **Profile ID:** `granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment`
- **Model ID:** `granite-4.2-8b`
- **Status:** current
- **Artifact identity:** ibm-granite/granite-4.2-8b-GGUF@93f3f6a8 :: granite-4.2-8b-Q4_K_M.gguf (sha256 16a9369d0805f80b7377d25d87f937a90c05dc04ad79173a52001e42c9aab311)
- **Runtime family:** llama.cpp (upstream)
- **Runtime revision:** b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120
- **Quantization / precision:** Q4_K_M official publisher GGUF; f16 K/V cache (FA on)
- **Deployment topology:** Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (40/40 layers), -fa on, f16 KV, -np 1, embedded GGUF Jinja template, DEPLOYMENT sampler (temp 0.2 / top_k 80 / top_p 1.0 / repeat_penalty 1.05); effective reasoning ON (built-in thinking; OFF control proven effective but not the campaign profile). Default context 32,768 / native exact 131,072; uncached scientific arms via --cache-ram 0 --no-cache-prompt --slot-prompt-similarity 0 with cache_prompt:false (proven by repeated-prompt probe). Publisher sampler (temp 1.0 / top_p 0.95) measured as a matched comparison, never pooled.
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-24 — [First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999)](../../../../models/granite-4.2-8b/events/granite-42-8b-rtx5070-welp-context-completion-20260924/)

## Provenance


Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
