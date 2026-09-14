# vLLM feasibility result

Date: 2026-08-14
Host: WumboJetsII (30 GiB usable RAM, RTX 5070 12,227 MiB VRAM)
Runtime: vLLM 0.27.1
Model: `Inferact/Qwen3.8-27B-NVFP4` at pinned revision `6128240ebaf4eaa7bad2b3d1c72c37d677c5f462`

## Attempts

1. `gpu-memory-utilization=0.90`, `cpu-offload-gb=16`, 4K, one sequence, text-only, eager: rejected before weight loading. vLLM observed 9.88/11.53 GiB free but requested 10.38 GiB.
2. `gpu-memory-utilization=0.84` with the same remaining bounds: reached model loading, then the host lost power after freezing from system-RAM exhaustion. The interrupted log had reached the ModelOpt NVFP4 load path with UVA CPU offload.
3. After recovery, the same 0.84 configuration started successfully. vLLM reported:
   - 16.07 GiB-equivalent CPU-offloaded parameters;
   - 7.01 GiB GPU model-load allocation;
   - 1.99 GiB GPU KV cache, 18,659-token cache capacity;
   - loopback API startup complete.

One bounded, non-thinking direct chat request returned HTTP 200 with 173 completion tokens in 171.129 seconds. The answer was structurally complete but included an incorrect claim that runtime inference uses intermediate gradients and a confused hybridization criterion. Raw request/response: `direct-chat-response.json`.

Immediately after that single request, `free -h` showed 29 GiB of 30 GiB RAM used, only 693 MiB available, and 6.2 GiB swap used. This exceeded the post-recovery 80-85% safety ceiling and explains the prior freeze: the 16 GiB CPU-offload configuration plus vLLM/model/runtime allocations exhausted system RAM. The server was stopped immediately. Memory recovered to 3.6 GiB used and 26 GiB available; swap stopped growing and fell to 2.3 GiB. No compute process remained.

## Decision

**Not viable on WumboJetsII.** The NVFP4 checkpoint is technically loadable and can answer, but only by driving the 32 GB host into severe RAM and swap pressure while delivering roughly 1.4 generation tokens/s in the server log. No LLMGauge suite or OMP session will be run against vLLM: repeating the configuration would recreate the known freeze/power-cycle risk, and a larger/less-offloaded representation is even less feasible on 12 GB VRAM. The preserved direct request is the maximum safe evidence.

Safeguards applied after recovery: one expensive process at a time; no unattended high-memory operation; resource inspection before and after launch; stop at the first RAM/swap threshold breach; no further vLLM, CPU-only, or hybrid benchmark expansion.
