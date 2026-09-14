# Qwen3.5-9B / RTX 5070 — admission and baseline characterization (public summary)

Campaign: `qwen35-9b-rtx5070-baseline-2026-09-09` · executed 2026-09-09/10 ·
Outcome: **PASS — QWEN35_9B_RTX5070_BASELINE_CHARACTERIZED** ·
Classification: **READY_WITH_GUARDRAILS** · 43 valid inference requests.

## Tested stack

- Model: Qwen/Qwen3.5-9B @ `c202236235762e1c871ad0ccb60c8ee5ba337b9a` (dense
  hybrid: 24 Gated DeltaNet + 8 full-attention blocks; text-only surface).
- Artifact: `Qwen3.5-9B-Q8_0.gguf` (Unsloth rev `3885219b…`, SHA-256
  `80962657…`, upstream-LFS-matched), Q8_0 weights / F16 KV / F32 recurrent
  state. This is a **HIGH_QUALITY_QUANTIZED_CONTROL** result, NOT a
  high-precision BF16 result: BF16 could not fit this GPU (15,140 MiB GPU
  weights alone), and a larger mixed-Q8 candidate failed reserve screening.
- Runtime: llama.cpp b10449 (`0d9ceae1e…`), CUDA 13.3, SM120; all 33/33
  runtime layers GPU-resident (CPU-mapped input embedding disclosed); pinned
  official chat template; non-thinking.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB, Ryzen 7 9800X3D.

## Headline results (MEASURED)

- Short (68-token prompt): TTFT 0.043883 s median; decode 66.66 tok/s median.
- Moderate (3,642-token prompt): TTFT 0.831738 s; prefill 4,378.79 tok/s;
  decode 64.84 tok/s.
- Constrained quality 7/7 on the same compact fixture as the 4B control (the
  fixture is saturated by both; no stronger-capability claim is supported).
- Context: 32,768 practical default (2,362 MiB minimum across default arms);
  65,536 guarded (1,306 MiB). Exact synthetic retrieval 30/30 target-field
  observations through 58,638 actual input tokens at 65,536.
- Reliability 20/20 exact on a fresh 32K server; no CUDA/OOM/Xid events.
- LocalMaxxing (canonical practical stack, 32K): tokSOut 67.3, TTFT 88.65 ms,
  submission `cmtwcn79807eups01faxxmyr1` (APPROVED, NEW; verifiedRun false —
  client capture limitation).

## Negative findings and limitations (retained, not sanitized)

- **The full revised model-card context envelope is still deferred.** Native
  claim 262,144 tokens (YaRN to 1,010,000 described); nothing above 65,536
  was exercised under this first-pass standard.
- Free-form outputs showed unsupported provenance claims (synthetic checksum
  fields described as "cryptographic" with an invented verification
  protocol). Quality superiority over the 4B BF16 control is unproven; the
  9B adds a medium-size quantized control, not a demonstrated better
  assistant.
- Coding, tool use, multi-turn autonomous-agent behavior, and vision were
  not tested. Six combined retrieval requests / 30 target observations is
  bounded coverage; reliability is bounded, not endurance certification.
- WELP classification READY_WITH_GUARDRAILS; optimization needed: NO.

Canonical scientific authority: the local WELP campaign evidence. This
summary is a public derivative; the campaign's `REPORT.md` governs on any
conflict.
