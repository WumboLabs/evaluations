# Qwen3.8-27B llama.cpp matrix on WumboJetsII

Date: 2026-08-14
Runtime: llama.cpp b9672 (`74ade5274`), CUDA SM120 build
Host GPU: RTX 5070, 12,227 MiB total VRAM
Baseline: 4096 context, 96 output tokens, batch 512, ubatch 256, flash attention on, temperature 0, top-p 1, reasoning off, one fixed functional prompt.

Raw commands, stdout, stderr, 0.5-second telemetry, and per-attempt JSON are under `llamacpp/baseline/`. Display throughput is derived from llama.cpp's final `[ Prompt: … | Generation: … ]` line; raw files remain authoritative.

| GGUF | Bytes | Working placement | Result | Prompt t/s | Generation t/s | Peak VRAM MiB | Headroom MiB |
|---|---:|---|---|---:|---:|---:|---:|
| Q6_K | 22,884,408,288 | 28 GPU layers, hybrid | PASS | 72.7 | 4.1 | 10,825 | 1,402 |
| Q5_K_M | 19,834,055,648 | 32 GPU layers, hybrid | PASS | 92.4 | 5.2 | 10,777 | 1,450 |
| Q4_K_M | 17,106,775,008 | 38 GPU layers, hybrid | PASS | 121.8 | 7.0 | 10,969 | 1,258 |
| IQ4_NL | 16,337,628,128 | 40 GPU layers, hybrid | PASS | 130.4 | 7.8 | 10,971 | 1,256 |
| IQ4_XS | 15,705,861,088 | 42 GPU layers, hybrid | PASS | 138.9 | 8.7 | 11,031 | 1,196 |
| Q3_K_M | 13,818,690,528 | 48 GPU layers, hybrid | PASS | 172.9 | 11.6 | 11,061 | 1,166 |
| Q3_K_S | 12,574,489,568 | 52 GPU layers, hybrid | PASS | 202.5 | 14.8 | 10,893 | 1,334 |
| UD-IQ3_XXS | 11,913,559,104 | 55 GPU layers, hybrid | PASS | 192.9 | 16.0 | 10,957 | 1,270 |
| UD-IQ2_M | 10,319,907,904 | all layers, full GPU | PASS | 401.6 | 42.9 | 11,155 | 1,072 |
| UD-IQ2_XXS | 9,010,048,064 | all layers, full GPU | PASS | 446.2 | 46.3 | 9,905 | 2,322 |

Every quant first received an all-layer attempt. Q6_K through UD-IQ3_XXS failed that attempt with a recorded CUDA allocation OOM, then completed at the bounded hybrid placement above. UD-IQ2_M and UD-IQ2_XXS completed full-GPU inference. These are observed 4K fit results, not quality rankings.

## Long-context retention and fit

Synthetic prompts placed `WUMBO-38-BLACKWELL` amid low-salience filler and asked the model to return it. Context values below are configured limits; generated prompt estimates were 3,586, 7,702, 15,346, and 30,662 tokens. Raw evidence is under `llamacpp/context/`.

| Configuration | 4K | 8K | 16K | 32K | Last successful generation t/s | Limitation |
|---|---|---|---|---|---:|---|
| Q6_K, 28 GPU layers | PASS, needle found | PASS, needle found | PASS, needle found | FAIL, CUDA OOM during decode | 3.9 at 16K | 32K peak reached 11,753 MiB before OOM |
| Q4_K_M, 38 GPU layers | PASS, needle found | PASS, needle found | PASS, needle found | FAIL, CUDA context allocation OOM | 6.5 at 16K | Only 754 MiB measured headroom at 16K |
| UD-IQ2_M, full GPU | PASS, needle found | PASS, needle found | FAIL, CUDA recurrent-state allocation OOM | Not attempted after 16K failure | 41.5 at 8K | Full-GPU weight placement leaves insufficient 16K cache headroom |

Practical ceiling under these exact placements: 16K for the Q6_K and Q4_K_M hybrid configurations, 8K for UD-IQ2_M full GPU. Lower GPU-layer placement or smaller caches may extend context, but was not silently substituted because it changes the tested performance configuration.
