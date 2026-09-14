# MODEL — NVIDIA Nemotron 3 Nano 4B (`nemotron-3-nano-4b`)

**Identity / provenance:** NVIDIA official Q4_K_M GGUF

**Campaign verdict (from `report.md`):** PROTOCOL_BLOCKED at Phase 3 gate decision (12/12 screen; WELP defines no advancement threshold — finding F-01). Phases 0–2 passed: clean load/serve, ~178 t/s decode, ~6.5k t/s prefill. No generalization to a model review.

**Artifacts:** physical binaries at `models/nemotron-3-nano-4b/artifacts/` (symlinked from this campaign root; never publish the binaries).

| File | Bytes | SHA-256 | Role |
|---|---|---|---|
| `NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf` | 2,837,072,864 | `be5d9a656a51922f24f1f09a759cebb694e1f5d9728bf0ef9f8c972c5a0b5ef2` | sole evaluated artifact |

Integrity: SHA-256 recomputed after the 2026-08-26 reorganization migration. Where the pre-move report.md documented a hash, it matches (see `model-manifest.json`).
