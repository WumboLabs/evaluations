<!-- Generated from registry metadata — do not hand-edit. -->

# Qwen3.8-9B (Empero)

**Classification:** No model-level classification published

**Recommended profile:** `qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver`

**Context:** No separate current context characterization is published; consult the bounded event reports.

[Human-facing Evaluation](https://wumbolabs.dev/evaluations/qwen3-8-9b-empero/)

## Profiles

- [qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver](profiles/qwen3.8-9b-empero-distill-llamacpp-q4q5q6-wumboserver/) — benchmark-only; llama.cpp; empero-ai/Qwen3.8-9B-Distill-GGUF Q4_K_M / Q5_K_M / Q6_K
- [qwen3.8-9b-empero-vendor-battery](profiles/qwen3.8-9b-empero-vendor-battery/) — specialized-test; llama.cpp/vLLM; empero-ai/Qwen3.8-9B-GGUF@760121cd70bb4c36b2b5ec58eb765e0df5987efe (Q8_0) + base Q4 lane

## Testing history

- 2026-09-01 — [WumboServer RTX 2060S admission/boundary + LocalMaxxing (Q4/Q5/Q6)](events/qwen38-empero-9b-distill-wumboserver-2026-09-01/) — BENCHMARK_ONLY / HARDWARE_LANE (not a WumboJetsII result); [qwen38-empero-9b-distill-wumboserver-2026-09-01](events/qwen38-empero-9b-distill-wumboserver-2026-09-01/REPORT.md)
- 2026-08-18 — [LLMGauge vendor-alignment battery (9B Q8_0)](events/qwen38-empero-9b-vendor-battery-2026-08-18/) — SPECIALIZED_TEST / VENDOR_ALIGNMENT_BATTERY; [qwen38-empero-9b-vendor-battery-2026-08-18](events/qwen38-empero-9b-vendor-battery-2026-08-18/REPORT.md)

Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings.
