<!-- Generated from registry metadata — do not hand-edit. -->

# LFM2.5-8B-A1B

**Classification:** NOT_READY

**Recommended profile:** `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 128,000 tokens; Model-card native maximum: 128,000 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

Native 128,000-token context; measured capacity matches at every configured rung (f16 KV, full-GPU). Controlled Context fixture 1.3 (canonical answer oracle, hardened snapshots): coverage COMPLETE (20/20 valid near-full cells, max placement error 0.23 pp), capability PARTIAL with USEFUL_CONTEXT_MAX 8,192 tokens on both lanes; seed 314159 validates 16K and 32K via oracle-reviewed cells; seed 42 and the 64K/128K rungs fail on synthesis and retrieval errors. The 2026-09-24 adjudication event supersedes current-state attribution only: raw evidence reused byte-identically from the hardening-validation campaign, whose 1-1 blinded document-synthesis disagreement resolved FAIL (2-of-3 with one blinded tie-break). Classification NOT_READY (R-C3, semantic WEAK) is terminal on this profile.

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/lfm2-5-8b-a1b/)

## Profiles

- [lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment](profiles/lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment/) — current; llama.cpp (upstream); LiquidAI/LFM2.5-8B-A1B-GGUF@49c14831 :: LFM2.5-8B-A1B-Q6_K.gguf (sha256 7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6)
- [lfm2.5-8b-a1b-rtx5070-cuda-not-configurable-2026-11-10](profiles/lfm2.5-8b-a1b-rtx5070-cuda-not-configurable-2026-11-10/) — current; llama.cpp (CUDA); Q5_K_M (official LiquidAI GGUF) :: revision LiquidAI-Q5_K_M-49c14831707011e64d70b2ebd8462ba08d608434 :: sha256 eb8bd10148ea21e195502d6d6a205983ba40815302068ce72eb160684df92b3e
- [lfm2.5-8b-a1b-rtx5070-cuda-heli-not-configurable-2026-11-11](profiles/lfm2.5-8b-a1b-rtx5070-cuda-heli-not-configurable-2026-11-11/) — current; llama.cpp (CUDA); Q5_K_M (official LiquidAI GGUF) :: revision LiquidAI-Q5_K_M-49c14831707011e64d70b2ebd8462ba08d608434 :: sha256 eb8bd10148ea21e195502d6d6a205983ba40815302068ce72eb160684df92b3e

## Testing history

- 2026-11-11 — [LFM2.5-8B-A1B HelicopterBench /2 one-shot objective result](events/lfm25-8b-a1b-rtx5070-cuda-helicopterbench-v2-2026-11-11/) — NOT_ASSIGNED; [lfm25-8b-a1b-rtx5070-cuda-helicopterbench-v2-2026-11-11](events/lfm25-8b-a1b-rtx5070-cuda-helicopterbench-v2-2026-11-11/REPORT.md)
- 2026-11-10 — [LFM2.5-8B-A1B Model/Core baseline + advanced reasoning (RTX 5070 CUDA)](events/lfm25-8b-a1b-rtx5070-cuda-m2-2026-11-10/) — NOT_ASSIGNED; [lfm25-8b-a1b-rtx5070-cuda-m2-2026-11-10](events/lfm25-8b-a1b-rtx5070-cuda-m2-2026-11-10/REPORT.md)
- 2026-09-24 — [Blinded tie-break adjudication and calibration sanity completion of the hardening-validation event (official Q6_K, upstream llama.cpp b10999)](events/lfm25-8b-a1b-rtx5070-welp-adjudication-20260924/) — NOT_READY; [lfm25-8b-a1b-rtx5070-welp-adjudication-20260924](events/lfm25-8b-a1b-rtx5070-welp-adjudication-20260924/REPORT.md)
- 2026-09-23 — [Prospective retest with reliability-class calibration and proven uncached timing (official Q6_K, upstream llama.cpp b10999)](events/lfm25-8b-a1b-rtx5070-welp-20260923/) — NOT_READY; [lfm25-8b-a1b-rtx5070-welp-20260923](events/lfm25-8b-a1b-rtx5070-welp-20260923/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
