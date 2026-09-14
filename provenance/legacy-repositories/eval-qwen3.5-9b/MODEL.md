# MODEL — Qwen3.5-9B

**Identity / provenance:** Alibaba (Qwen team); GGUF conversion by Unsloth; official model `Qwen/Qwen3.5-9B` @ `c202236235762e1c871ad0ccb60c8ee5ba337b9a`; upstream license Apache-2.0.

**Campaign verdict:** PASS — QWEN35_9B_RTX5070_BASELINE_CHARACTERIZED; classification **READY_WITH_GUARDRAILS** (HIGH_QUALITY_QUANTIZED_CONTROL — medium-fit Q8_0 control; this is NOT a high-precision BF16 result (BF16 cannot fit this GPU)).

**Tested artifact:** Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5); precision Q8_0 weights (acquired), F16 KV cache, F32 recurrent state; SHA-256 `809626574d0cb43d4becfa56169980da2bb448f2299270f7be443cb89d0a6ae4`; source unsloth/Qwen3.5-9B-GGUF, hash-matched to upstream LFS.
The binary is NOT stored in this repository; the hash records provenance only.

**Runtime:** llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120) — All 33/33 runtime layers GPU-resident; CPU-mapped input embedding disclosed; pinned official chat template; non-thinking text-only greedy surface.

**Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12GB; Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44.
