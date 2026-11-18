# Qwen3-Coder-30B-A3B-Instruct: accepted WELP Model/Core findings

**HUMAN_ACCEPTED scope: Model/Core baseline only.** Advanced Coding is **DEFERRED_BY_OWNER**, not an accepted result. This event describes one tested configuration, not production readiness or unattended repository autonomy.

## Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **49 PASS, 10 FAIL, 0 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. These counts are task outcomes, not a composite score. All six controlled Family A context checks passed. Both Multi-Document checks failed: several requested values were correct, but both replies attributed the conflicting replica count to the wrong document. The configured 16,384-token serving capacity is not a validated useful-context default.

The short coding-correction probe returned the wrong clamped value. Document synthesis promoted two timestamps into an unsupported measured startup interval. In one Linux diagnosis, the model identified the wrong port for a failed bind. The frozen record also retains failures for the forbidden-letter check, invented Git extension behavior, an unavailable-tool instruction, strict extraction, and systemd diagnosis. All three baseline tool probes passed; a separate technical qualification obtained a grounded tool result but made an unnecessary extra call rather than ending cleanly.

**SCI-01:** Q02 originally passed under the corrected frozen key order. No historical erratum or replacement score applies. **SCI-02:** the strict-extraction wording permits more than one plausible reading; the recorded exact-check FAIL does not establish broad instruction-following failure. **SCI-03:** the systemd reply rejected the premise that active means serving, but missed the frozen lexical check and overstated what `active` establishes about listening. Keep the original FAIL without interpreting it as agreement with the premise.

## Advanced Coding: DEFERRED_BY_OWNER

The frozen multi-file repair task supplied an already-correct target, so the Advanced Coding section is excluded from this scientific acceptance pending a separately governed methodological correction. The original record remains intact; no specialist scores are published here.

- Deferred section: `coding` (`coding-advanced/1`), original manifest SHA-256 `1205222e2e70cce736294026e48892bbc17cb1d8715d71f215cf06b7b8a0659e`.
- Original specialist report SHA-256 `efe469271ffcb193ba147c6a5a9dfac6221aded95561f2ba8281920fe6e7b471`.

## Identity and deployment

- Event: `qwen3-coder-30b-a3b-instruct-r9700-hip-native-2026-11-17`. Profile: `qwen3-coder-30b-a3b-instruct-r9700-hip-not-configurable-2026-11-17`, revision `cf92da45dbe0ca725b58a0f46457906b3df5ca32702308237afdffd1403ed71e`.
- Tested [GGUF artifact](https://huggingface.co/ggml-org/Qwen3-Coder-30B-A3B-Instruct-GGUF/tree/ef85c7f175f00be8af4e1de0c14e59ce7e5d0db3): Q4_K_M, 17,988,419,552 bytes, SHA-256 `f6050b4da22869aa3fb9d94bb3314e9fc5a027d4741c1f97761c387d6b2b2335`.
- AMD Radeon AI PRO R9700, HIP, llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (flash attention off), native non-thinking profile. Context and performance findings apply only to the bounded workloads tested.
- Accepted baseline manifest SHA-256 `6a50a7e8311ada876046ec97e3122f3740a63add953b4b83ee449c5435c688aa`, owner acceptance 2026-11-18 UTC.

The accompanying structured export, `website-publication.json`, retains all identity-level baseline outcomes, workload measurements, exact deployment conditions, acceptance bindings, and deferred-section provenance. Original local evidence governs scientific conflicts.
