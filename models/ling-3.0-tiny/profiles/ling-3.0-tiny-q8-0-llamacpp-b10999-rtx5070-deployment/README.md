<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp official Q8_0 (Reasoning On, deployment sampler, 32K)

- **Profile ID:** `ling-3.0-tiny-q8-0-llamacpp-b10999-rtx5070-deployment`
- **Model ID:** `ling-3.0-tiny`
- **Status:** current
- **Artifact identity:** inclusionAI/Ling-3.0-tiny-GGUF@01b850e2 :: Ling-3.0-tiny-Q8_0.gguf (sha256 9299a9e5cbc540597619e252a41fd671faa4e84e619e3cea816542c84e19f0d6)
- **Runtime family:** llama.cpp (upstream)
- **Runtime revision:** b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120
- **Quantization / precision:** Q8_0 official publisher GGUF; f16 K/V cache (FA on)
- **Deployment topology:** Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (24/24 layers), -fa on, f16 KV, -np 1, embedded GGUF Bailing-V3 Jinja template, DEPLOYMENT sampler (temp 0.2 / top_k 80 / top_p 1.0 / repeat_penalty 1.05); effective reasoning ON (bailing v3 thinking default; enable_thinking=false OFF control proven effective but not the campaign profile). Default context 32,768 / native exact 131,072 / advertised 262,144 (YaRN x2.0, mechanism-qualified on this runtime); uncached scientific arms via --cache-ram 0 --no-cache-prompt --slot-prompt-similarity 0 with cache_prompt:false (proven by repeated-prompt probe). Publisher sampler (temp 1.0 / top_k 20 / top_p 0.95) measured as a matched comparison, never pooled.
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-24 — [Second WELP stabilization-cohort campaign: hybrid-attention MoE characterized end-to-end on the pinned runtime (official Q8_0)](../../../../models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-characterization-20260924/)
- 2026-09-25 — [Reasoning On classification re-derived under the 2026-09-25 reasoning-profiles snapshot from retained hash-bound evidence (no new inference)](../../../../models/ling-3.0-tiny/events/ling-3-0-tiny-rtx5070-welp-reasoning-on-20260925/)

## Provenance


Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
