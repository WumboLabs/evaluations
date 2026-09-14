# MODEL — MiniCPM5-2B

**Identity / provenance:** OpenBMB; official model `openbmb/MiniCPM5-2B` @ `cd199ce3ee67549c42ef7372f809f2c63599a3e9`; upstream license Apache-2.0.

**Campaign verdict:** PASS — MINICPM5_2B_RTX5070_CHARACTERIZED; MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES; classification **READY_WITH_GUARDRAILS** (Official BF16 full-precision candidate (characterized; not deployed); architecture-diversity control value HIGH).

**Tested artifact:** model-00000-of-00001.safetensors (official BF16; no quantization or conversion); precision BF16 weights and BF16 KV (primary surface); fp8(e4m3) KV only on the single authorized 131,072 alternate surface; SHA-256 `14fb8e7f0a18d53d1f239773758bf581cee7e456a4523a54622c3a245b64402c`; source openbmb/MiniCPM5-2B at the pinned revision.
The binary is NOT stored in this repository; the hash records provenance only.

**Runtime:** vLLM 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3 — Qualified contained CUDA 13.0 toolchain (compute_120f/sm_120f); full transformer GPU residency; fresh-cache containment proven; greedy temperature-0 primary surface.

**Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12GB; Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44.
