<!-- Generated from registry metadata — do not hand-edit. -->

# Spark-X2.5-4B

**Classification:** READY_WITH_GUARDRAILS

**Recommended profile:** `spark25-4b-q8-0-llamacpp`

**Context:** practical_default_tokens: 32768; guarded_tokens: 131072; native_maximum_tokens: 1048576 (FIT_LIMIT: f16 KV alone requires 38,654,705,664 bytes at the exact native maximum - 3.16x the 12,227 MiB card; no official extension mechanism documented); envelope_complete: true; useful context is PROFILE-SCOPED: USEFUL_CONTEXT_MAX_SEMANTIC = 131,072 on the predeclared thinking-off non-starving lane (VALIDATED 2/2 seeds, 512-token reserve, >=99% occupancy); canonical vendor-default thinking-on lane is BUDGET_LIMITED at every tested rung (reserve consumed by thinking); retrieval capability intact.

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/spark-x2-5-4b/)

## Profiles

- [spark25-4b-q8-0-llamacpp](profiles/spark25-4b-q8-0-llamacpp/) — current; llama.cpp (upstream); XHToken/Spark-X2.5-4B-GGUF@9826e0be :: Spark-X2.5-4B-Q8_0.gguf (sha256 5c2c3c190e4337e1016b8593ca8e26e8b18c972200b107385d4ec61a25d9dea2)

## Testing history

- 2026-09-20 — [Current-WELP characterization (official Q8_0, upstream llama.cpp b10999)](events/spark25-4b-rtx5070-welp-20260920/) — READY_WITH_GUARDRAILS; [spark25-4b-rtx5070-welp-20260920](events/spark25-4b-rtx5070-welp-20260920/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
