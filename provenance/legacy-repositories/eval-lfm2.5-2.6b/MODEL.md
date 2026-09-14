# MODEL — Liquid LFM2.5 2.6B (`lfm2.5-2.6b-qad`)

**Identity / provenance:** Liquid AI official quants incl. 19 Aug 2026 QAD release; hashes documented in report.md

**Campaign verdict (from `report.md`):** QAD Q4_0 is the rational ultra-fast deployment quant when 1.59 GB is the hard size target; it retained PTQ Q4_0 footprint and throughput (282.5±0.4 t/s) and improved fixed-corpus perplexity, but the campaign did NOT reproduce a material practical-quality win over PTQ Q4_0 nor the 96.6% retention claim.

**Artifacts:** physical binaries at `models/lfm2.5-2.6b/artifacts/` (symlinked from this campaign root; never publish the binaries).

| File | Bytes | SHA-256 | Role |
|---|---|---|---|
| `LFM2.5-2.6B-BF16.gguf` | 5,403,158,528 | `590b1534d5ec57dbddb750d25468d7ba4df0d1976531a731590418efa360edb5` | full-precision reference |
| `LFM2.5-2.6B-Q4_0.gguf` | 1,593,894,912 | `e1a61bf937bc60726e18626e97f7ee9bfd2574d95744c2ed909de98b78006fbe` | PTQ comparison arm (32 bytes smaller; INTENTIONAL distinct artifact, not a duplicate) |
| `LFM2.5-2.6B-Q4_K_M.gguf` | 1,674,455,040 | `02a8b7e17487d326e46d68ce0ba24211e1b80a14c4cd0597fa73c1cd697f52ed` | K-quant control |
| `LFM2.5-2.6B-Q5_K_M.gguf` | 1,939,744,768 | `17ce54cc676e15e572adebfeeed8da6abd12b0f68d595be19b59e662476c21b3` | K-quant reference |
| `LFM2.5-2.6B-Q6_K.gguf` | 2,221,615,104 | `2e74b1a0979a4a1936a408445147d103b8f15b2e2ec31c65fa0166f9069c250d` | high-precision reference |
| `LFM2.5-2.6B-Q8_0.gguf` | 2,874,779,648 | `1e22128dfa128bdfb684da167e74e072d0a056baa7d06d9f280291e2839b0fc9` | high-precision reference |
| `LFM2.5-2.6B-QAD-Q4_0.gguf` | 1,593,894,944 | `a247afd6414918eac8e520a9e6137dc271235461ecbe1180462221d5b8d40b03` | QAD student (distilled) — recommended ultra-fast quant |

Integrity: SHA-256 recomputed after the 2026-08-26 reorganization migration. Where the pre-move report.md documented a hash, it matches (see `model-manifest.json`).
