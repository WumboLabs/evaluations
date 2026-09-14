### Identity and scope

- Profile: `qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver` — llama.cpp Distill Q4_K_M/Q5_K_M/Q6_K (WumboServer RTX 2060S lane)
- Evidence maturity: **BENCHMARK_ONLY**
- Evidence scope: performance
- Hardware: WumboServer (RTX 2060 SUPER 8GB)

empero-ai/Qwen3.8-9B-Distill-GGUF Q4_K_M/Q5_K_M/Q6_K on WumboServer RTX 2060S: admission benchmark, Q6 fit boundary, Q5 WELP-style serving campaign, and LocalMaxxing reconciliation (9b-q4 60.4 tok/s out, 5.37 GB peak VRAM). Hardware-lane evidence; Ornith-9B admission on the same GPU is recorded under its own model.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.
