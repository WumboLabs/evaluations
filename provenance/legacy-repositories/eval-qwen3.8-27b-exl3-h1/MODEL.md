# MODEL — Qwen 3.8 27B (`qwen3.8-27b`)

**Identity / provenance:** Community AD (atomic decomposition) IQ2_XS and DFlash2 Q4_K_M conversions; see campaign manifests/

**Campaign verdict (from `report.md`):** PARTIAL. Best bounded coding config Q4_K_M 38 GPU layers / 8K / reasoning off (4.85–5.0/5 at 6.4–6.8 t/s, 467 MiB min headroom). Fastest UD-IQ2_M full-GPU 4K (~42 t/s). vLLM NOT viable on this host (29/30 GiB RAM + 6.2 GiB swap after one request; preceding host freeze/power-loss). No LLMGauge Agent Harness result exists.

**Artifacts:** physical binaries at `models/qwen3.8-27b/artifacts/` (symlinked from this campaign root; never publish the binaries).

| File | Bytes | SHA-256 | Role |
|---|---|---|---|
| `Qwen3.8-27B-AD-IQ2_XS.gguf` | 9,889,846,752 | `a437190b719a4f1498cb54120d73a97b595fcfa0c263bc0753cc9c19942e82c5` | atomic-decomposition IQ2_XS evidence artifact |
| `Qwen3.8-27B-DFlash2-Q4_K_M.gguf` | 1,143,006,752 | `18a380efc9b7ed8d88677fc895f5c11ae170653434ee378f7348f715c14d0594` | DFlash2 Q4_K_M sharp-dflash evaluation artifact |

Integrity: SHA-256 recomputed after the 2026-08-26 reorganization migration. Where the pre-move report.md documented a hash, it matches (see `model-manifest.json`).
