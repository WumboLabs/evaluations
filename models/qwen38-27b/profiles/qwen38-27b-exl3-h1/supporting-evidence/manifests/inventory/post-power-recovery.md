# Post-power-loss recovery check

Date: 2026-08-14

- LLMGauge repository: clean `main...origin/main`.
- llama.cpp repository: clean `master...origin/master`.
- GPU: RTX 5070, driver 610.57.04, 12,227 MiB total, 752 MiB used, 11,059 MiB free; no surviving evaluation server.
- RAM: 30 GiB total, 26 GiB available; swap unused.
- All ten GGUF files were re-read and their SHA-256 values exactly matched `inventory/gguf-download-manifest.md` and the upstream LFS object identifiers.
- All seven NVFP4 safetensor files were re-read and their SHA-256 values exactly matched `vllm/nvfp4-sha256.txt`.
- Every pre-existing LLMGauge result revalidated successfully after reboot:
  - `llamacpp-q4km-coding-smoke`
  - `llamacpp-q4km-practical`
  - `llamacpp-q6k-practical`
  - `llamacpp-udiq2m-practical` (preserved failed run)
  - `llamacpp-udiq2m-practical-4k`
  - `reasoning-q4km-off`
  - `reasoning-q4km-on`

Verdict: prior evidence is structurally and cryptographically intact. Continue from the interrupted vLLM startup retry; do not rerun successful earlier evaluation work.
