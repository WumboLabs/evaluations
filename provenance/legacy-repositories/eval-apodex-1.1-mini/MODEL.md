# MODEL — Apodex 1.1 mini (`apodex-1.1-mini`)

**Identity / provenance:** Community GGUF conversion abenzerps/Apodex-1.1-mini-GGUF @ 59afa578 (NOT official upstream)

**Campaign verdict (from `report.md`):** WELP DO_NOT_ADVANCE at Phase 3 (early stop, frozen gate). Phase 2 decode 169.36 t/s. LocalMaxxing speed SUBMITTED/APPROVED (cmt9ijytg00xali017f46xk25, 182.31 tok/s p512/n128).

**Artifacts:** physical binaries at `models/apodex-1.1-mini/artifacts/` (symlinked from this campaign root; never publish the binaries).

| File | Bytes | SHA-256 | Role |
|---|---|---|---|
| `Apodex-1.1-mini-IQ1_M.gguf` | 8,821,679,936 | `1e84d8adf7837e96fb18712882a8a114becc7e53554372e2f612c5e0c6276cd4` | canonical evaluated artifact (1.75 bpw; only quant admitting full-GPU placement) |
| `Apodex-1.1-mini-IQ2_M.gguf` | 12,241,706,816 | `450afff9cd60e19ad485b4be4c22adf561df35072e4b4879bcc981e6fad88a8f` | rejected admission candidate (12.24 GB weights vs 10.87 GB free VRAM) |

Integrity: SHA-256 recomputed after the 2026-08-26 reorganization migration. Where the pre-move report.md documented a hash, it matches (see `model-manifest.json`).
