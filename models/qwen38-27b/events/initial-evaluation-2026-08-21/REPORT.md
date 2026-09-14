# Qwen3.8-27B cross-configuration comparison

Date: 2026-08-14
Host: WumboJetsII — Ryzen 7 9800X3D, 30 GiB usable RAM, RTX 5070 with 12,227 MiB VRAM

## Decision table

| Configuration | Placement / context | Generation speed | Manual evidence | Resource result | Decision |
|---|---|---:|---|---|---|
| llama.cpp Q6_K | 28 GPU layers, 8K practical suite | 4.1 tok/s | 3.54/5 across 6 prompts | 11,249 MiB peak VRAM; 978 MiB minimum headroom | Viable but slow; no measured quality gain over Q4_K_M on this suite |
| llama.cpp Q4_K_M | 38 GPU layers, 8K practical suite | 6.4–6.9 tok/s | 3.54/5 across 6 prompts | 11,734 MiB peak VRAM; 493 MiB minimum headroom | Best balanced coding/daily-driver candidate, but hybrid and tight on VRAM |
| llama.cpp Q4_K_M coding smoke | 38 GPU layers, 8K | 6.4–6.8 tok/s | 4.85–5.0/5 on 4 bounded coding/tool-output prompts | 11,760 MiB peak VRAM; 467 MiB minimum headroom | Strongest measured bounded coding result |
| llama.cpp UD-IQ2_M | Full GPU, 4K practical suite | 42.0–42.9 tok/s | 3.62/5 across 6 prompts | 11,626 MiB peak VRAM; 601 MiB minimum headroom | Fastest practical candidate; quality varies by task and 8K LLMGauge run OOMed |
| llama.cpp UD-IQ2_XXS + OMP | Full GPU, 12K server | Not comparable to suite throughput | Correct minimal edit; agent completion mixed | 9,356 MiB idle server VRAM; host RAM stayed near 5.1 GiB used | Only resource-safe agent configuration; context exhaustion prevented self-verification |
| vLLM NVFP4 | 0.84 GPU utilization, 16 GiB CPU offload, 4K | about 1.4 tok/s | One complete answer with technical errors | 29/30 GiB RAM used and 6.2 GiB swap after one request | Unsafe and not viable on this host |

Manual scores are bounded review metadata for the tested prompts, not universal rankings. The practical-suite averages do not prove UD-IQ2_M is higher fidelity than Q6_K or Q4_K_M; its unusually strong parser answer materially raised its six-prompt average.

## llama.cpp fit envelope

- All ten selected GGUFs loaded and generated at a bounded placement.
- Q6_K through UD-IQ3_XXS failed their first all-layer attempt with recorded CUDA OOM, then ran hybrid.
- UD-IQ2_M and UD-IQ2_XXS ran fully on GPU.
- Exact-placement synthetic context ceilings: Q6_K 28-layer and Q4_K_M 38-layer passed 16K but failed 32K; UD-IQ2_M full GPU passed 8K but failed 16K.
- The practical UD-IQ2_M LLMGauge run was stable at 4K. Its separate 8K run preserved six context-initialization OOM failures, showing the full-GPU 8K placement lacks robust ambient headroom.

## Reasoning mode

Q4_K_M reasoning-off produced a complete runnable answer at 3.72/5, 6.2 tok/s, and 503 MiB VRAM headroom. Reasoning-on consumed the full 1,024-token allowance in visible thinking, ended mid-code, scored 2.1/5, ran at 5.0 tok/s, and left 471 MiB headroom. Use reasoning off by default for bounded local work.

## Agent result

The isolated OMP session on UD-IQ2_XXS inspected the correct project and ultimately made the exact minimal retry-ledger fix. It initially hallucinated an unrelated implementation after compaction, recovered by re-reading, then exhausted the 12,288-token boundary before running the required post-fix tests or completing its report. Independent verification passed all 3 tests. LLMGauge rejected the compacted source as unsupported; the raw session was preserved without mutation.

## Recommendation

- Best measured bounded coding quality: Q4_K_M, 38 GPU layers, 8K, reasoning off.
- Best speed: UD-IQ2_M, full GPU, 4K, reasoning off; use only for short, reviewable tasks.
- Highest-precision retained reference: Q6_K, but its 4.1 tok/s speed and equal six-prompt average do not justify routine use on this host.
- vLLM: no safe configuration found. Do not repeat the 16 GiB CPU-offload configuration on a 32 GB system.
- OMP: usable only with the full-GPU UD-IQ2_XXS configuration and strict review; the observed agent did not meet completion requirements unaided.
