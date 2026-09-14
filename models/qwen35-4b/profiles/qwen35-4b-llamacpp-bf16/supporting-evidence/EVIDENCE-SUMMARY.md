# Qwen3.5-4B / RTX 5070 — first-pass baseline characterization (public summary)

Campaign: `qwen35-4b-rtx5070-baseline-2026-09-09` · executed 2026-09-09 ·
Outcome: **PASS — QWEN35_4B_RTX5070_BASELINE_CHARACTERIZED** ·
Classification: **READY_WITH_GUARDRAILS** · 43 valid inference requests.

## Tested stack

- Model: Qwen/Qwen3.5-4B @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` (dense
  hybrid: 24 Gated DeltaNet + 8 full-attention blocks; text-only surface).
- Artifact: `Qwen3.5-4B-BF16.gguf` (Unsloth rev `e87f1764…`, SHA-256
  `9e6e2841…`, upstream-LFS-matched), BF16 weights / F16 KV / F32 recurrent
  state.
- Runtime: llama.cpp b10449 (`0d9ceae1e…`), CUDA 13.3, SM120; all 33/33
  runtime layers GPU-resident (CPU-mapped input embedding disclosed).
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB, Ryzen 7 9800X3D.
- Surface: single-user, text-only, non-thinking, greedy; no optimization.

## Headline results (MEASURED)

- Short (68-token prompt): TTFT 0.040569 s median; decode 67.91 tok/s median.
- Moderate (3,642-token prompt): TTFT 0.691319 s; prefill 5,268.19 tok/s;
  decode 67.29 tok/s.
- Constrained quality 7/7 (factual, structured, beginning/middle/end
  retrieval, conflict resistance, absent-field grounding, instruction
  retention, repeat consistency).
- Context: 32,768 practical default (2,346 MiB lifetime-minimum free);
  65,536 guarded (1,292 MiB). Exact synthetic retrieval 30/30 target-field
  observations through 58,638 actual input tokens at 65,536 (seeds 42/43 at
  32K/64K).
- Reliability 20/20 exact on a continuous 32K server; no CUDA/OOM/Xid events.
- LocalMaxxing (canonical practical stack, 32K): tokSOut 68.0, TTFT 76.92 ms,
  submission `cmtwcmm3207eqps01w7fubuuw` (APPROVED, NEW; verifiedRun false —
  client capture limitation, recorded honestly).

## Negative findings and limitations (retained, not sanitized)

- **Model-card context completion is NOT complete under the later
  corrected-WELP standard.** Native claim 262,144 tokens (card describes YaRN
  to 1,010,000); nothing above 65,536 was tested; the full envelope debt
  remains deferred. Do not cite this campaign as full-context coverage.
- Concrete free-form errors were observed: the short output conflated
  corrupted-weights/load failures with capability degradation; the moderate
  summary asserted uninterrupted operation and implied checksum verification
  its input never established. Constrained-check success does not establish
  robust free-form grounding.
- Coding, tool use, multi-turn autonomous-agent behavior, and vision were
  not tested. Context coverage is bounded (30 target-depth observations; two
  seeds at 32K/64K). Reliability is bounded, not endurance certification.
- WELP classification READY_WITH_GUARDRAILS; optimization needed: NO.

Canonical scientific authority: the local WELP campaign evidence. This
summary is a public derivative; the campaign's `REPORT.md` governs on any
conflict.
