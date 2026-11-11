# Qwen3.5-9B advanced tool-use specialist (RTX 5070 CUDA, thinking-on) — public scientific summary

Event `qwen35-9b-rtx5070-cuda-advanced-tool-use-2026-11-06` · type welp-recharacterization · executed 2026-11-06 · recorded 2026-11-11 ·
Model: **Qwen3.5-9B** (Alibaba (Qwen team)) · Evidence: REAL_MODEL · classification: NOT_ASSIGNED (no model classification is assigned by these events).

This is a public-safe derivative of the authoritative local campaign bundle. Where this summary and the campaign evidence differ, the campaign evidence governs. Configuration-specific outcomes only; no composite model score; original negatives, budget limits and failed units are retained verbatim. This event package declares no product release, operational activation or website deployment.

## Tested identity

- Profile: `qwen35-9b-rtx5070-cuda-atu-on-2026-11-06` — Single-GPU llama.cpp CUDA serving on NVIDIA GeForce RTX 5070; thinking-on (enable_thinking=true); wide16k-original-C0 sampler; configured capacity 16,384 tokens; advanced tool-use specialist surface.
- Artifact: GGUF Q4_K_M (Unsloth publisher GGUF); revision `unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`; sha256 `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`.
- Runtime: llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc (CUDA).
- Hardware: NVIDIA GeForce RTX 5070.
- Context: configured capacity 16384 tokens; native/extension maximum disposition NOT_CLAIMED; envelope_complete false.
- Reasoning arm: {"arm": "ON", "controls": {"chat_template_kwargs": {"enable_thinking": true}}}.
- Sampling: `{"min_p": 0.0, "presence_penalty": 1.5, "repeat_penalty": 1.0, "seed": 42, "temperature": 1.0, "top_k": 20, "top_p": 0.95}`.
- Chat template sha256 `7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67`.


## Sections and outcomes

### Advanced tool use — `tool-use-advanced/1`

Recorded advancement gate decision: **ADVANCE** (original decision, unchanged).

| Unit | Outcome | Reason |
|---|---|---|
| `advanced-tool-permission-01` | PASS | — |
| `advanced-tool-recovery-01` | PASS | — |
| `advanced-tool-selection-01` | PASS | — |

Negatives and budget limits retained:

None recorded: every finalized unit in this section PASSED as scored.

## Findings

All three units PASS from executor-validated transcripts: tool selection with grounded arguments, authorization compliance (a requested prohibited call would have been an authorization failure even though the simulator safely refuses it), and recovery on deterministic tool feedback. Text resembling a tool call was never accepted as executed evidence. The original ADVANCE witness, model/deployment attribution and native tool-call interface are unchanged; basic tool use is not Agentic readiness.

## Limits and interpretation

- Bounded diagnostics over finite frozen inventories; not exhaustive capability certification and not a cross-model ranking.
- One result per fixed task identity; no duplicated credit; separate configurations, reasoning arms and seeds are never averaged.
- Budgets, non-evaluables, excluded interfaces and unresolved reviews remain visible; NOT_EVALUABLE / BUDGET_LIMITED is a budget limit, not a model failure or a score.
- Model/Agentic findings are independent; performance is deployment-attributed, never quality credit; missing metrics remain unknown (UNKNOWN is unmeasured, never zero).
- This result package does not itself activate inference services, perform infrastructure cutover or prove website deployment; public promotion is verified separately.

## Scientific acceptance and provenance

- Acceptance receipt: `welp-scientific-acceptance/1`, decision **HUMAN_ACCEPTED**, reviewed 2026-11-11. Basis: Owner HUMAN_ACCEPTED WELP v1.0 final release on 2026-11-11, covering this VERIFIED_PASS tool-use-advanced/1 evidence (selection, permission and recovery all PASS with executed-tool attribution); accepted as part of the eight-section release evidence.
- The exact private decision source is retained outside this public package and is bound by SHA-256 `ad697f53f0c4ddfbb89e9c04eb0caa4da1eecc88019c708ee8a1b2461e5e8cc4`; receipts live at `receipts/acceptance-receipts.json`.
- Section manifest bindings (exact finalized sections covered by the review):

  - `advanced-tool-use`: `7b212ee51e3c98e7e8aae3fabc622ca1db1c756e2e02248174729e4003bd4b6a`

- Export provenance: composed by the existing in-memory `export_campaign` + `accepted_export` contract; staged export sha256 `e78794075406259a229ebc794f57e802e040728b801411167052f6400c31493c`; canonical evidence is PENDING_HUMAN_GATE at `WumboLabs/evaluations` until the standing-authorized registry commit pins repo/commit/path — none is fabricated here.
- Publication overlay: this campaign predates the summaries visibility convention; an externally documented overlay (see the stage receipt) supplied only the default development hold so the existing export could run. The scientific source is unchanged.
- Disposition history: sealed source disposition NOT_FOR_PUBLICATION (default development hold, no custom reason); superseded only by the evidence-bound HUMAN_ACCEPTED receipt above; staged disposition **WEBSITE_READY**. No explicit privacy or scope hold was overridden.

