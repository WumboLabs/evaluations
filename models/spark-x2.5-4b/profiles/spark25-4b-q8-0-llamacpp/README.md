<!-- Generated from registry metadata — do not hand-edit. -->

# llama.cpp upstream official Q8_0 (reasoning-on, vendor default)

- **Profile ID:** `spark25-4b-q8-0-llamacpp`
- **Model ID:** `spark-x2.5-4b`
- **Status:** current
- **Artifact identity:** XHToken/Spark-X2.5-4B-GGUF@9826e0be :: Spark-X2.5-4B-Q8_0.gguf (sha256 5c2c3c190e4337e1016b8593ca8e26e8b18c972200b107385d4ec61a25d9dea2)
- **Runtime family:** llama.cpp (upstream)
- **Runtime revision:** b04d4e567cd2fb8d2ded6e17d38dbbcfafe29063 (tag b10999, 0.4.1-dev build 1), CUDA SM120
- **Quantization / precision:** Q8_0 official publisher GGUF (8.50 BPW); f16 K/V cache (FA on)
- **Deployment topology:** Full-GPU upstream llama.cpp CUDA serving on RTX 5070 12GB: -ngl 99 (36/36 layers), -fa on, f16 KV, -np 1 (verified via /slots), embedded Jinja template, vendor sampler (temp 1.0 / top_p 0.95 / top_k -1); REASONING_ON vendor default with enable_thinking=false as the only effective control (no effort-level control exists). Default context 32,768 / guarded fit ceiling 131,072; standardized 512-token output reserve.
- **Hardware:** WumboJetsII (RTX 5070 12GB)

[Model index](../../) · [Profile metadata](profile.json)

## Events

- 2026-09-20 — [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999)](../../../../models/spark-x2.5-4b/events/spark25-4b-rtx5070-welp-20260920/)

## Provenance


Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive.
