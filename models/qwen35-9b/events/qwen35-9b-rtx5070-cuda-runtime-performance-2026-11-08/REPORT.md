# Qwen3.5-9B runtime performance (RTX 5070 CUDA, deployment-attributed) — public scientific summary

Event `qwen35-9b-rtx5070-cuda-runtime-performance-2026-11-08` · type welp-recharacterization · executed 2026-11-08 · recorded 2026-11-11 ·
Model: **Qwen3.5-9B** (Alibaba (Qwen team)) · Evidence: REAL_MODEL · classification: NOT_ASSIGNED (no model classification is assigned by these events).

This is a public-safe derivative of the authoritative local campaign bundle. Where this summary and the campaign evidence differ, the campaign evidence governs. Configuration-specific outcomes only; no composite model score; original negatives, budget limits and failed units are retained verbatim. This event package declares no product release, operational activation or website deployment.

## Tested identity

- Profile: `qwen35-9b-rtx5070-cuda-rtperf-on-2026-11-08` — Single-GPU llama.cpp CUDA serving on NVIDIA GeForce RTX 5070; thinking-on (enable_thinking=true); wide16k-original-C0 sampler; configured capacity 16,384 tokens; deployment-attributed runtime-performance measurement surface; single-device single-request condition.
- Artifact: GGUF Q4_K_M (Unsloth publisher GGUF); revision `unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`; sha256 `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`.
- Runtime: llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc (CUDA).
- Hardware: NVIDIA GeForce RTX 5070.
- Context: configured capacity 16384 tokens; native/extension maximum disposition NOT_CLAIMED; envelope_complete false.
- Reasoning arm: {"arm": "ON", "controls": {"chat_template_kwargs": {"enable_thinking": true}}}.
- Sampling: `{"min_p": 0.0, "presence_penalty": 1.5, "repeat_penalty": 1.0, "seed": 42, "temperature": 1.0, "top_k": 20, "top_p": 0.95}`.
- Chat template sha256 `7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67`.


## Sections and outcomes

### Runtime performance (deployment-attributed) — `runtime-performance/1`

Recorded advancement gate decision: **ADVANCE** (original decision, unchanged).

| Unit | Outcome | Reason |
|---|---|---|
| `perf-short` | PASS | — |
| `perf-substantial` | PASS | — |

Negatives and budget limits retained:

None recorded: every finalized unit in this section PASSED as scored.

Workload measurements (deployment-attributed, never quality scores):

- `perf-short` (3 samples): generation 83.28 tok/s (min 82.73 / median 83.09 / max, native metering), prompt 466.8 tok/s (median), TTFT 0.056-0.626 s.
- `perf-substantial` (3 samples): generation 81.16 tok/s (min 80.49 / median 80.87 / max, native metering), prompt 3668.9 tok/s (median), TTFT 1.012-1.094 s.
Wall-clock estimates are derived and distinct from native metering; per-sample values remain in the export (`performance_observations`). No cross-workload average is computed and no performance value is model-quality credit.

## Findings

One qualified deployment measured with the accepted M2 workload identities reused verbatim: perf-short generation ~83.1 tok/s (median, native metering; repeats 82.7/83.3/83.1) with TTFT 0.056-0.626 s; perf-substantial generation ~80.9 tok/s (median; repeats 80.5-81.2) with TTFT ~1.01 s and prompt processing ~3,670 tok/s. Wall-clock estimates are derived and reported as a distinct measurement, never merged with engine metering. Device memory telemetry was unavailable from the deployment observer and is reported unavailable, never zero. These are deployment-attributed numbers: they are never model-quality credit and never inputs to capability scoring.

## Limits and interpretation

- Bounded diagnostics over finite frozen inventories; not exhaustive capability certification and not a cross-model ranking.
- One result per fixed task identity; no duplicated credit; separate configurations, reasoning arms and seeds are never averaged.
- Budgets, non-evaluables, excluded interfaces and unresolved reviews remain visible; NOT_EVALUABLE / BUDGET_LIMITED is a budget limit, not a model failure or a score.
- Model/Agentic findings are independent; performance is deployment-attributed, never quality credit; missing metrics remain unknown (UNKNOWN is unmeasured, never zero).
- This result package does not itself activate inference services, perform infrastructure cutover or prove website deployment; public promotion is verified separately.

## Scientific acceptance and provenance

- Acceptance receipt: `welp-scientific-acceptance/1`, decision **HUMAN_ACCEPTED**, reviewed 2026-11-11. Basis: Release-relevant deployment-attributed runtime measurements (runtime-performance section, six measurement observations) were retained VERIFIED_PASS in the accepted 2026-11-11 reconciliation and are covered by the owner HUMAN_ACCEPTED final release of 2026-11-11. Performance is deployment-attributed and is never model-quality credit; unavailable memory telemetry stays reported unavailable, never zero.
- The exact private decision source is retained outside this public package and is bound by SHA-256 `ad697f53f0c4ddfbb89e9c04eb0caa4da1eecc88019c708ee8a1b2461e5e8cc4`; receipts live at `receipts/acceptance-receipts.json`.
- Section manifest bindings (exact finalized sections covered by the review):

  - `runtime-performance`: `d893aadc53116ac1b7b9936a7c15844a669b627497f724275b1226c1e44088fc`

- Export provenance: composed by the existing in-memory `export_campaign` + `accepted_export` contract; staged export sha256 `28db53d0d546f411001081fc8d6a2e24098692c9f89585d78fd63d170caa7d76`; canonical evidence is PENDING_HUMAN_GATE at `WumboLabs/evaluations` until the standing-authorized registry commit pins repo/commit/path — none is fabricated here.
- Publication overlay: this campaign predates the summaries visibility convention; an externally documented overlay (see the stage receipt) supplied only the default development hold so the existing export could run. The scientific source is unchanged.
- Disposition history: sealed source disposition NOT_FOR_PUBLICATION (default development hold, no custom reason); superseded only by the evidence-bound HUMAN_ACCEPTED receipt above; staged disposition **WEBSITE_READY**. No explicit privacy or scope hold was overridden.

