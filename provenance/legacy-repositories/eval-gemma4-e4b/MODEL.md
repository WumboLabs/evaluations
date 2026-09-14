# MODEL — Gemma 4 E4B

**Identity / provenance:** Google; official model `google/gemma-4-E4B-it` @ `ee0ef6023621cff504d758262d4e04895a5af4a2`; upstream license Apache-2.0 (Gemma license terms apply).

**Campaign verdict:** PASS — GEMMA4_E4B_EVIDENCE_COMPLETION_COMPLETE; classification **READY_WITH_GUARDRAILS** (Official Google QAT Q4_0 + official mmproj — the only official precision that hosts the full card range with reserve on this GPU; community Q4_K_M pair retained as evidence only (provenance unknown)).

**Tested artifact:** gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release); precision QAT Q4_0 weights, F16 KV cache; SHA-256 `676c3507 (weights; matches pinned upstream LFS) / 7498a37c (mmproj; matches pinned upstream LFS)`; source google/gemma-4-E4B-it-qat-q4_0-gguf @ 4b4a2c1d584be7264f87aac328a1bc739ce81b6c.
The binary is NOT stored in this repository; the hash records provenance only.

**Runtime:** llama.cpp 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (campaign-local CUDA 13.3 build, SM120) — All 42 layers + PLE tables + vision/audio encoders GPU-resident; official mmproj loaded for multimodal arms; greedy temperature-0 primary surface.

**Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12GB; Single-user workstation; AMD Ryzen 7 9800X3D; Fedora Linux 44.
