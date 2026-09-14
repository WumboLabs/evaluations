# MODEL — Qwen3.5-4B

**Identity / provenance:** Alibaba (Qwen team); GGUF conversion by Unsloth; official model `Qwen/Qwen3.5-4B` @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`; upstream license Apache-2.0.

**Campaign verdict:** PASS — QWEN35_4B_RTX5070_BASELINE_CHARACTERIZED; classification **READY_WITH_GUARDRAILS** (Comfortable-fit high-precision BF16 text control).

**Tested artifact:** Qwen3.5-4B-BF16.gguf (text-only conversion; Unsloth revision e87f176479d0855a907a41277aca2f8ee7a09523); precision BF16 weights, F16 KV cache, F32 recurrent state; SHA-256 `9e6e2841a75f503ccb330831832fd7861266e187e0dbf149a954219ccb8c197a`; source unsloth/Qwen3.5-4B-GGUF, hash-matched to upstream LFS.
The binary is NOT stored in this repository; the hash records provenance only.

**Runtime:** llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) — All 33/33 runtime layers GPU-resident; CPU-mapped input embedding disclosed; non-thinking text-only greedy surface.

**Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12GB; Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44.
