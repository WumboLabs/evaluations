# Recommended deployment profile — LFM2.5-1.2B-Instruct QAD Q4_0

## Runtime

- Binary: `<workspace>/llama.cpp-current/bin/llama-server`
  (build 10449, commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`)
- Model: `models/LFM2.5-1.2B-Instruct-QAD-Q4_0.gguf`
  SHA-256 `bb741ebb106d543e9de114b843a3d3d73d51c74b5801e69da2abde821a0cb3e1`

```
llama-server -m LFM2.5-1.2B-Instruct-QAD-Q4_0.gguf \
  -ngl all -fit off -c 4096 -b 2048 -ub 512 -fa on -np 1 \
  --host 127.0.0.1 --port 8093 --no-webui --metrics
```

## Sampler (official, verified from current Liquid cards)

temperature 0.1 · top_k 50 · repeat_penalty **1.05** (1.2B card differs from the 2.6B card's 1.1)

## Envelope

- Resident GPU: ~958 MiB process VRAM; ~1534 MiB observed peak at 4K ctx
- Decode ≈ 586 tok/s; prompt ≈ 6600 tok/s (RTX 5070, matched runs)
- Useful context ceiling established: ≤ 8K (retrieval collapses ≥ 16K)

## Guardrails (mandatory)

1. Schema-validate every structured output; retry once on invalid JSON.
2. Never trust factual/tool-free answers about specific APIs, packages, flags:
   the model fabricates confidently on invented subjects (0/12 across all quants incl. BF16).
3. Constrain context to ≤ 8K documents.
4. Do not use as a coding helper without an external test harness (4/20 executable;
   ignores required symbol names).
