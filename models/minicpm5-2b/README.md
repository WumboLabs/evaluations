<!-- Generated from registry metadata — do not hand-edit. -->

# MiniCPM5-2B

**Classification:** READY_WITH_GUARDRAILS

**Recommended profile:** `minicpm5-2b-vllm-bf16`

**Context:** Practical default: 32,768 tokens; Guarded boundary: 65,536 tokens; Model-card native maximum: 131,072 tokens

Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.

<details>
<summary>Published context findings and limitations</summary>

practical_default_tokens: 32768; guarded_tokens: 65536; native_maximum_tokens: 131072; envelope_complete: true; native_maximum_disposition: "Exact 131,072 carries two completed dispositions: FIT_LIMIT on the BF16-KV surface (1,024 MiB reserve floor caps the pool below the maximum) and measured FAILED (strict useful-context gate) on the authorized fp8-KV alternate surface executed at 99.50% occupancy; the highest admitted BF16-KV rung was 98,304"; notes: "The strict frozen useful-context gate FAILED at every rung (12/12 requests) with exact attribution: markdown-fenced JSON and an omitted absent field cascade the per-field gates. Supplementary content-level analysis (explicitly not a gate) shows 5/5 exact target retrieval at every depth through 65,536 on both seeds and at 131,072 on one of two seeds. A FAILED gate is a completed negative disposition, not VALIDATED; no rung is claimed VALIDATED."

</details>

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/minicpm5-2b/)

## Profiles

- [minicpm5-2b-vllm-bf16](profiles/minicpm5-2b-vllm-bf16/) — current; vLLM; model-00000-of-00001.safetensors (official BF16; no quantization or conversion)

## Testing history

- 2026-09-10 — [Initial evaluation (full characterization)](events/initial-evaluation-2026-09-10-minicpm5/) — READY_WITH_GUARDRAILS; [initial-evaluation-2026-09-10-minicpm5](events/initial-evaluation-2026-09-10-minicpm5/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
