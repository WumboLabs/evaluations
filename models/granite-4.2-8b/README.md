<!-- Generated from registry metadata — do not hand-edit. -->

# Granite 4.2 8B

**Classification:** NOT_READY

**Recommended profile:** `granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment`

**Context:** Native 128,000-token context; 524,288 advertised extension (IBM). Measured on the 12 GB card: 32,768 configured practical context with full-GPU placement (f16 KV, FA on); 65,536, 131,072 and 524,288 FIT_LIMIT (measured load failure and derived arithmetic); 8,192 RESERVE_LIMITED on the semantic lane (the frozen 8,192-token reserve leaves no constructible cell). Controlled Context under the repaired welp-context 0.3.0 methodology: coverage COMPLETE 8/8 (7 VALIDATED + 1 measured BUDGET_LIMITED answerless cell at 16K/semantic that covers coverage and never validates capability), capability VALIDATED at the practical rung, USEFUL_CONTEXT_MAX 32,768 tokens on both lanes, max placement error 0.349 pp. Multi-Document Context practical cell (24,576 usable tokens) PASS. Classification NOT_READY (R-C3) is terminal on this profile: replicated semantic-lane fabrication guardrail (R7 FAIL, DO_NOT_ADVANCE) with dimensions ACCEPTABLE/GOOD/VALIDATED/CLEAN.

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/granite-4-2-8b/)

## Profiles

- [granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment](profiles/granite-4.2-8b-q4-k-m-llamacpp-b10999-rtx5070-deployment/) — current; llama.cpp (upstream); ibm-granite/granite-4.2-8b-GGUF@93f3f6a8 :: granite-4.2-8b-Q4_K_M.gguf (sha256 16a9369d0805f80b7377d25d87f937a90c05dc04ad79173a52001e42c9aab311)

## Testing history

- 2026-09-24 — [First published evaluation via linked completion of the methodology-repair predecessor (official Q4_K_M, upstream llama.cpp b10999)](events/granite-42-8b-rtx5070-welp-context-completion-20260924/) — NOT_READY; [granite-42-8b-rtx5070-welp-context-completion-20260924](events/granite-42-8b-rtx5070-welp-context-completion-20260924/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
