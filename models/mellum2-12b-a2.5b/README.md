<!-- Generated from registry metadata — do not hand-edit. -->

# Mellum2 12B-A2.5B

**Classification:** LIMITED_ROLE_ONLY

**Recommended profile:** `mellum2-12b-a2.5b-llamacpp-q4km-instruct`

**Context:** Practical default: 16,384 tokens; Guarded boundary: 8,192 tokens; Model-card native maximum: 131,072 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

practical_default_tokens: 16384; guarded_tokens: 8192; native_maximum_tokens: 131072; envelope_complete: true; native_maximum_disposition: "FAILED on useful context with capacity+performance validated: exact 131,072 admits at f16 KV (9,850 MiB, 2,377 MiB free) and passes near-full performance; frozen two-seed useful-context gate failed 0/2 (replicated recency-bias). Not FIT_LIMIT, not validated."; exact_max_dispositions: {"native_131072": "FAILED useful-context (capacity + near-full performance validated)", "official_extension": "none advertised (documented absence; native 131,072 is train-time YaRN x16 baked in checkpoint)"}; highest_measured_admitted: {"tokens": 131072, "note": "99.66-99.76% occupancy; 4,872-4,883 tok/s prefill; peak 9,930 MiB; 2,297 MiB free floor"}; useful_context_finding: "USEFUL_CONTEXT_MAX 16,384: two seeds pass depths 2/25/50/75/95% at 8K and 16K (max placement error 0.024 pp); 32,768 fails 1/2 seeds; 64,536 and 131,072 fail 0/2 with identical decoy-capture/early-window-loss signature."

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/mellum2-12b-a2-5b/)

## Profiles

- [mellum2-12b-a2.5b-llamacpp-q4km-thinking](profiles/mellum2-12b-a2.5b-llamacpp-q4km-thinking/) — specialized-test; llama.cpp; JetBrains/Mellum2-12B-A2.5B-Thinking-GGUF-Q4_K_M
- [mellum2-12b-a2.5b-llamacpp-q4km-instruct](profiles/mellum2-12b-a2.5b-llamacpp-q4km-instruct/) — current; llama.cpp; Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf (8,071,293,600-byte Q4_K_M; sha256 b04281c27de5d968d577f310d982273b1b13bdbd8117b3ecffffeebfe222f0a7; official JetBrains/Mellum2-12B-A2.5B-Instruct-GGUF-Q4_K_M @ 1236b4166ed6ab1d57e4be9bcc19f4899c190cbf, reacquired 2026-09-15 after local+archive absence, byte-verified against official LFS SHA-256)

## Testing history

- 2026-09-15 — [Current-WELP recharacterization](events/mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15/) — LIMITED_ROLE_ONLY; [mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15](events/mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15/REPORT.md)
- 2026-07-04 — [LocalMaxxing LMX speed runs (Instruct + Thinking)](events/mellum2-lmx-speed-2026-07-04/) — BENCHMARK_ONLY (LMX local speed); [mellum2-lmx-speed-2026-07-04](events/mellum2-lmx-speed-2026-07-04/REPORT.md)
- 2026-07-04 — [12B practical pool comparison v025 + Grug](../../shared-events/practical-use-comparison-2026-07-04/) — PRACTICAL_USE / SHARED_MULTI_MODEL_COMPARISON (canonical); [gemma4-12b-practical-pool-v025-2026-07-04](../../shared-events/practical-use-comparison-2026-07-04/REPORT.md)
- 2026-06-17 — [Fake-tool honesty runs (64k)](events/mellum2-fake-tool-2026-06-17/) — SPECIALIZED_TEST / UNSCORED_PROBES; [mellum2-fake-tool-2026-06-17](events/mellum2-fake-tool-2026-06-17/REPORT.md)
- 2026-06-17 — [Agent backend fit test (64k, Instruct + Thinking)](events/mellum2-agent-backend-64k-2026-06-17/) — SPECIALIZED_TEST / AGENT_BACKEND_FIT_TEST (not a general quality verdict); [mellum2-agent-backend-64k-2026-06-17](events/mellum2-agent-backend-64k-2026-06-17/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
