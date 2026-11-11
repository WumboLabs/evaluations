# Qwen3.5-9B advanced reasoning specialist (RTX 5070 CUDA, thinking-on) — public scientific summary

Event `qwen35-9b-rtx5070-cuda-advanced-reasoning-2026-11-06` · type welp-recharacterization · executed 2026-11-06 · recorded 2026-11-11 ·
Model: **Qwen3.5-9B** (Alibaba (Qwen team)) · Evidence: REAL_MODEL · classification: NOT_ASSIGNED (no model classification is assigned by these events).

This is a public-safe derivative of the authoritative local campaign bundle. Where this summary and the campaign evidence differ, the campaign evidence governs. Configuration-specific outcomes only; no composite model score; original negatives, budget limits and failed units are retained verbatim. This event package declares no product release, operational activation or website deployment.

## Tested identity

- Profile: `qwen35-9b-rtx5070-cuda-on-2026-11-06` — Single-GPU llama.cpp CUDA serving on NVIDIA GeForce RTX 5070; thinking-on (enable_thinking=true); wide16k-original-C0 sampler (temperature 1.0, top_k 20, top_p 0.95, min_p 0.0, presence_penalty 1.5, repeat_penalty 1.0, seed 42); configured capacity 16,384 tokens; specialist sections and scored Agentic M3.
- Artifact: GGUF Q4_K_M (Unsloth publisher GGUF); revision `unsloth-Q4_K_M-sha256-03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`; sha256 `03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`.
- Runtime: llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc (CUDA).
- Hardware: NVIDIA GeForce RTX 5070.
- Context: configured capacity 16384 tokens; native/extension maximum disposition NOT_CLAIMED; envelope_complete false.
- Reasoning arm: {"arm": "ON", "controls": {"chat_template_kwargs": {"enable_thinking": true}}}.
- Sampling: `{"min_p": 0.0, "presence_penalty": 1.5, "repeat_penalty": 1.0, "seed": 42, "temperature": 1.0, "top_k": 20, "top_p": 0.95}`.
- Chat template sha256 `7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67`.


## Sections and outcomes

### Advanced reasoning — `reasoning-advanced/1`

Recorded advancement gate decision: **ADVANCE** (original decision, unchanged).

| Unit | Outcome | Reason |
|---|---|---|
| `advanced-constraints-01` | PASS | — |
| `advanced-evidence-01` | NOT_EVALUABLE | BUDGET_LIMITED |
| `advanced-revision-01` | PASS | — |

Negatives and budget limits retained:

- `advanced-evidence-01`: NOT_EVALUABLE / BUDGET_LIMITED (budget limit, preserved as a limit — never a failure or a credit).

## Findings

Deterministic exact-answer oracles decided the scored exchange only; internal reasoning style, length and exposed chain-of-thought were never scored. advanced-constraints-01 and advanced-revision-01 PASS. advanced-evidence-01 hit the transport deadline and is retained NOT_EVALUABLE / BUDGET_LIMITED. Across the three diverse families this same methodology is reported independently per configuration (Qwen two PASS / one budget-limited; fresh Gemma three PASS; LFM two PASS / one valid FAIL); configurations are never averaged.

## Limits and interpretation

- Bounded diagnostics over finite frozen inventories; not exhaustive capability certification and not a cross-model ranking.
- One result per fixed task identity; no duplicated credit; separate configurations, reasoning arms and seeds are never averaged.
- Budgets, non-evaluables, excluded interfaces and unresolved reviews remain visible; NOT_EVALUABLE / BUDGET_LIMITED is a budget limit, not a model failure or a score.
- Model/Agentic findings are independent; performance is deployment-attributed, never quality credit; missing metrics remain unknown (UNKNOWN is unmeasured, never zero).
- This result package does not itself activate inference services, perform infrastructure cutover or prove website deployment; public promotion is verified separately.

## Scientific acceptance and provenance

- Acceptance receipt: `welp-scientific-acceptance/1`, decision **HUMAN_ACCEPTED**, reviewed 2026-11-11. Basis: Owner explicitly recorded HUMAN_ACCEPTED for WELP v1.0 Advanced Reasoning (reasoning-advanced/1) on 2026-11-11 with bounded diagnostic claims over the finite deterministic inventory and accepted ceilings; separate configurations are never averaged. Original outcomes retained: two PASS and one NOT_EVALUABLE (BUDGET_LIMITED); no reclassification.
- The exact private decision source is retained outside this public package and is bound by SHA-256 `ad697f53f0c4ddfbb89e9c04eb0caa4da1eecc88019c708ee8a1b2461e5e8cc4`; receipts live at `receipts/acceptance-receipts.json`.
- Section manifest bindings (exact finalized sections covered by the review):

  - `advanced-reasoning`: `a6e50b0ff0b3a026807464d17ae7259235332662ba39b55ae2e93ec5d3f913c2`

- Export provenance: composed by the existing in-memory `export_campaign` + `accepted_export` contract; staged export sha256 `a4c78d20f05cde7da380cdbd7d9394bd238a0892dc6fedb804261fe07ced4721`; canonical evidence is PENDING_HUMAN_GATE at `WumboLabs/evaluations` until the standing-authorized registry commit pins repo/commit/path — none is fabricated here.
- Publication overlay: this campaign predates the summaries visibility convention; an externally documented overlay (see the stage receipt) supplied only the default development hold so the existing export could run. The scientific source is unchanged.
- Disposition history: sealed source disposition NOT_FOR_PUBLICATION (default development hold, no custom reason); superseded only by the evidence-bound HUMAN_ACCEPTED receipt above; staged disposition **WEBSITE_READY**. No explicit privacy or scope hold was overridden.

