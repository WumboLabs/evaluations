# MiniCPM5-2B / RTX 5070 — full WELP characterization (public summary)

Campaign: `minicpm5-2b-rtx5070-welp-characterization-2026-09-10` ·
Outcome: **PASS — MINICPM5_2B_RTX5070_CHARACTERIZED** ·
**MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES** ·
Classification: **READY_WITH_GUARDRAILS** · 55 scientific requests across 7
supervised server arms; zero OOM/CUDA/Xid; zero invalidated requests.

## Tested stack

- Model: openbmb/MiniCPM5-2B @ `cd199ce3…` (dense Llama-style, text-only;
  native context 131,072; official context extension: none found).
- Artifact: official BF16 `model-00000-of-00001.safetensors`
  (`14fb8e7f…`); no quantization or conversion.
- Runtime: vLLM 0.27.1 + Torch 2.13.0+cu130 + FlashInfer 0.6.16.post3 on a
  qualified contained CUDA 13.0 toolchain (fresh-cache containment proven);
  full transformer GPU residency; greedy temperature-0 primary surface.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB, Ryzen 7 9800X3D.

## Headline results (MEASURED)

- Short (65-token prompt): TTFT 0.013037 s median; decode 118.622 tok/s.
- Moderate (2,663-token prompt): TTFT 0.203597 s; prefill 13,079.8 tok/s;
  decode 116.95 tok/s.
- Context envelope COMPLETE with exact dispositions: 8K–65,536 admitted
  (BF16-KV, util 0.85); 98,304 admitted at util 0.87 (highest BF16-KV rung);
  exact 131,072 = **FIT_LIMIT on BF16-KV** (the 1,024 MiB reserve floor caps
  the pool below the maximum; no blind launch, per methodology) and
  **measured FAILED (strict useful-context gate) on the authorized
  fp8(e4m3)-KV alternate surface**, executed at 99.50% occupancy, both
  seeds, 129,908 actual input tokens. Near-full performance inside practical
  gates through 98,304 (131K-fp8 TTFT 66.3 s is analysis-grade).
- Constrained quality 6/7 — one deterministic temperature-0 over-refusal of
  a benign prime-list prompt; repeat consistency itself held.
- Capabilities: thinking TESTED_PASS; coding TESTED_PASS (4/4 executable
  cases); native tool selection TESTED_PASS (parser-emitted valid call);
  tool-result use TESTED_PASS; English/Chinese and structured output
  TESTED_PASS. Agent benchmarks DEFERRED_WITH_REASON.
- Reliability 20/20 COMPLETE and passed; zero errors.
- LocalMaxxing (canonical practical stack — BF16, contained vLLM runtime,
  32K default, NOT the 131K fp8 boundary): tokSOut 118.2, TTFT 22.7 ms,
  submission `cmtwcna5907f0ps01sfiwd60a` (APPROVED, NEW; verifiedRun false —
  client capture limitation; actual prompt tokens 252, endpoint usage).

## Negative findings and limitations (retained, not sanitized)

- **The strict frozen useful-context gate FAILED at every rung (12/12
  requests)** with exact attribution: outputs are markdown-fenced (breaking
  strict raw-JSON parsing) and the `absent` field is omitted at every rung;
  checksum/synthesis instructions drop out from 32K upward. Supplementary
  content-level analysis (explicitly NOT a gate) shows 5/5 exact target
  retrieval at every depth through 65,536 on both seeds and 131,072 on one
  of two seeds. No context rung is claimed VALIDATED.
- Deterministic temperature-0 over-refusal quirk on a benign prompt.
- fp8-KV scales uncalibrated (kv_scale 1.0); quality beyond the fixture
  family unknown; DSpark out of scope by explicit human constraint; not an
  autonomous-agent qualification.
- A failed gate is a completed negative disposition, not a hidden one; the
  FIT_LIMIT is a hardware/resource envelope conclusion, not a
  model-capability claim.

Canonical scientific authority: the local WELP campaign evidence. This
summary is a public derivative; the campaign's `REPORT.md` governs on any
conflict.
