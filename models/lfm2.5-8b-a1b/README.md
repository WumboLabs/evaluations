<!-- Generated from registry metadata — do not hand-edit. -->

# LFM2.5-8B-A1B

**Classification:** NOT_READY

**Recommended profile:** `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment`

**Context:** Native 128,000-token context; measured capacity matches at every configured rung (f16 KV, full-GPU). Controlled Context fixture 1.3 (canonical answer oracle, hardened snapshots): coverage COMPLETE (20/20 valid near-full cells, max placement error 0.23 pp), capability PARTIAL with USEFUL_CONTEXT_MAX 8,192 tokens on both lanes; seed 314159 validates 16K and 32K via oracle-reviewed cells; seed 42 and the 64K/128K rungs fail on synthesis and retrieval errors. The 2026-09-24 adjudication event supersedes current-state attribution only: raw evidence reused byte-identically from the hardening-validation campaign, whose 1-1 blinded document-synthesis disagreement resolved FAIL (2-of-3 with one blinded tie-break). Classification NOT_READY (R-C3, semantic WEAK) is terminal on this profile.

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/lfm2-5-8b-a1b/)

## Profiles

- [lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment](profiles/lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment/) — current; llama.cpp (upstream); LiquidAI/LFM2.5-8B-A1B-GGUF@49c14831 :: LFM2.5-8B-A1B-Q6_K.gguf (sha256 7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6)

## Testing history

- 2026-09-24 — [Blinded tie-break adjudication and calibration sanity completion of the hardening-validation event (official Q6_K, upstream llama.cpp b10999)](events/lfm25-8b-a1b-rtx5070-welp-adjudication-20260924/) — NOT_READY; [lfm25-8b-a1b-rtx5070-welp-adjudication-20260924](events/lfm25-8b-a1b-rtx5070-welp-adjudication-20260924/REPORT.md)
- 2026-09-23 — [Prospective retest with reliability-class calibration and proven uncached timing (official Q6_K, upstream llama.cpp b10999)](events/lfm25-8b-a1b-rtx5070-welp-20260923/) — NOT_READY; [lfm25-8b-a1b-rtx5070-welp-20260923](events/lfm25-8b-a1b-rtx5070-welp-20260923/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
