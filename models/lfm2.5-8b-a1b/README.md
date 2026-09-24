<!-- Generated from registry metadata — do not hand-edit. -->

# LFM2.5-8B-A1B

**Classification:** NOT_READY

**Recommended profile:** `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 128,000 tokens; Model-card native maximum: 128,000 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

Native 128,000-token context; measured capacity matches at every configured rung (f16 KV, full-GPU). Family A 1.2 placement preflight passed at all executed rungs (max depth error 0.464 pp, >=99% occupancy) but every completed answer failed at least one useful-context gate - synthesis fails at all rungs and retrieval degrades with depth. Disposition FAILED (valid near-full measurements failing frozen useful-context gates); no useful-context maximum; envelope_complete: false.

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/lfm2-5-8b-a1b/)

## Profiles

- [lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment](profiles/lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment/) — current; llama.cpp (upstream); LiquidAI/LFM2.5-8B-A1B-GGUF@49c14831 :: LFM2.5-8B-A1B-Q6_K.gguf (sha256 7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6)

## Testing history

- 2026-09-23 — [Prospective retest with reliability-class calibration and proven uncached timing (official Q6_K, upstream llama.cpp b10999)](events/lfm25-8b-a1b-rtx5070-welp-20260923/) — NOT_READY; [lfm25-8b-a1b-rtx5070-welp-20260923](events/lfm25-8b-a1b-rtx5070-welp-20260923/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
