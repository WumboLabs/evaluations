# MODEL — Liquid LFM2.5 1.2B Instruct (`lfm2.5-1.2b-qad`)

**Identity / provenance:** Liquid AI official quants + Unsloth UD-Q4_K_XL @ pinned revisions; all local SHA-256 match upstream LFS OIDs

**Campaign verdict (from `report.md`):** QAD Q4_0 is the best deployment quant of the five-way matrix and best always-resident sidecar candidate measured in this family (31/52 practical; 585.6±2.79 t/s decode; +5.6% vs Q4_K_M). Hallucination lane 0/12 for every quant including BF16. Useful context <=8K.

**Artifacts:** physical binaries at `models/lfm2.5-1.2b/artifacts/` (symlinked from this campaign root; never publish the binaries).

| File | Bytes | SHA-256 | Role |
|---|---|---|---|
| `LFM2.5-1.2B-Instruct-BF16.gguf` | 2,343,326,528 | `3d80914b903cd6f3cc041208cf20ec46a3224f840c732e5fd7698832b4743d1b` | full-precision reference |
| `LFM2.5-1.2B-Instruct-Q4_0.gguf` | 695,751,488 | `2ea801949d760cdf1a2cc04a54262c22c3c0c54f0769d57760c9adeb0e59233f` | PTQ comparison arm |
| `LFM2.5-1.2B-Instruct-Q4_K_M.gguf` | 730,895,168 | `b1b3de114215d9507409a662a501a631095a479a419584e8a2ded6304b19b4f5` | K-quant control |
| `LFM2.5-1.2B-Instruct-Q5_K_M.gguf` | 843,354,944 | `fa03f3ac4da941a53a0cd4450aacf6a80804c6a1ff885d2fdcbe9406c03215c4` | K-quant reference |
| `LFM2.5-1.2B-Instruct-QAD-Q4_0.gguf` | 695,755,488 | `bb741ebb106d543e9de114b843a3d3d73d51c74b5801e69da2abde821a0cb3e1` | recommended deployment quant |
| `LFM2.5-1.2B-Instruct-UD-Q4_K_XL.gguf` | 730,895,584 | `856aeee6d85ac684b1db8dee48795b44fc06731ecda03aee36ece682413a9b9a` | Unsloth control (byte-identical LFS OID to Unsloth Q4_K_M) |

Integrity: SHA-256 recomputed after the 2026-08-26 reorganization migration. Where the pre-move report.md documented a hash, it matches (see `model-manifest.json`).
