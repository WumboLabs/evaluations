# LFM2.5-8B-A1B HelicopterBench /2 one-shot objective result — public scientific summary

Event `lfm25-8b-a1b-rtx5070-cuda-helicopterbench-v2-2026-11-11` · type welp-recharacterization · executed 2026-11-11 · recorded 2026-11-11 ·
Model: **LFM2.5-8B-A1B** (Liquid AI) · Evidence: REAL_MODEL · classification: NOT_ASSIGNED (no model classification is assigned by these events).

This is a public-safe derivative of the authoritative local campaign bundle. Where this summary and the campaign evidence differ, the campaign evidence governs. Configuration-specific outcomes only; no composite model score; original negatives, budget limits and failed units are retained verbatim. This event package declares no product release, operational activation or website deployment.

## Tested identity

- Profile: `lfm2.5-8b-a1b-rtx5070-cuda-heli-not-configurable-2026-11-11` — Single-GPU llama.cpp CUDA serving on NVIDIA GeForce RTX 5070; reasoning arm NOT_CONFIGURABLE; publisher sampler (temperature 0.2, top_k 80, top_p 1.0, min_p 0.0, repeat_penalty 1.05, seed 42); configured capacity 16,384 tokens; one-shot HelicopterBench /2 generation surface.
- Artifact: GGUF Q5_K_M (official LiquidAI GGUF); revision `LiquidAI-Q5_K_M-49c14831707011e64d70b2ebd8462ba08d608434`; sha256 `eb8bd10148ea21e195502d6d6a205983ba40815302068ce72eb160684df92b3e`.
- Runtime: llama.cpp b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc (CUDA).
- Hardware: NVIDIA GeForce RTX 5070.
- Context: configured capacity 16384 tokens; native/extension maximum disposition NOT_CLAIMED; envelope_complete false.
- Reasoning arm: {"arm": "NOT_CONFIGURABLE", "controls": {}}.
- Sampling: `{"min_p": 0.0, "presence_penalty": 0.0, "repeat_penalty": 1.05, "seed": 42, "temperature": 0.2, "top_k": 80, "top_p": 1.0}`.
- Chat template sha256 `6d65c8804847ad74eea912dd7eca3dc1cf7a457b53a77f47d841a14121910963`.


## Sections and outcomes

### HelicopterBench one-shot artifact benchmark — `helicopterbench/2`

Recorded advancement gate decision: **ADVANCE** (original decision, unchanged).

| Unit | Outcome | Reason |
|---|---|---|
| `helicopterbench-01` | PASS | — |

Negatives and budget limits retained:

Generation completed, but the generated game is broken: objective gameplay verification is PARTIAL, not PASS. Failed launch/animation, controls, course, collision and restart checks remain visible below.

Objective benchmark result (`helicopterbench/2`):

| Category | Points | Max |
|---|---:|---:|
| controls_and_physics | 6 | 20 |
| course_and_difficulty | 0 | 15 |
| launch_and_rendering | 6 | 20 |
| obstacles_and_collision | 7 | 20 |
| score_failure_restart | 0 | 15 |
| **Total (mechanical)** | **19** | **90** |

Generation outcome: PASS; verification class: **PARTIAL**; normalized final score: **21.1 / 100**. The first completed submission is the submission; the rubric scores observed behavior of the executed artifact, never source code; resource exhaustion is never a completed incorrect game.

## Findings

One-shot artifact benchmark under methodology helicopterbench/2: the first completed submission is the submission; behavior was verified by executing the generated artifact in an isolated browser namespace, and the mechanical rubric scored observed behavior, never source code. The single unit helicopterbench-01 is recorded with generation PASS and verification class PARTIAL. Objective category points: controls_and_physics 6/20 (numeric control state present; gravity-descent and input-ascent checks failed), launch_and_rendering 6/20 (canvas present; animation liveliness and runtime-exception checks failed), obstacles_and_collision 7/20 (obstacles present; advance and game-over-on-collision checks failed), course_and_difficulty 0/15, score_failure_restart 0/15 (game-over/restart checks unevaluable in the broken gameplay). Total 19/90, normalized 21.1/100, PARTIAL. This is a broken game playthrough documented as the honest result; nothing was regenerated, repaired or rescored. The historical /1 record (mechanical 34/90 under the /1 methodology) keeps its separate original interpretation and was never scored under /2.

## Supplementary gameplay media

Actual independently executed footage from the evaluated generated artifact is bound to the event, profile, model artifact and methodology in `website-publication.json`. H.264 MP4, 800×364, 10 fps, 26.0 seconds, 8,993 bytes; SHA-256 `72a16a92c3fb259322ef01969e401ac8a7e2ab56cd2fddafc678f7175d4f3fc4`. Browser playback of the original captured bytes was verified locally. The observed clip shows the Loading screen, not functioning gameplay. It is supplementary to the objective PARTIAL score and is not a repaired game or reference demonstration. Intended website asset: `/media/evaluations/lfm25-8b-a1b-rtx5070-cuda-helicopterbench-v2-2026-11-11/gameplay.mp4`; this is not a claim that it is live.

## Limits and interpretation

- Bounded diagnostics over finite frozen inventories; not exhaustive capability certification and not a cross-model ranking.
- One result per fixed task identity; no duplicated credit; separate configurations, reasoning arms and seeds are never averaged.
- Budgets, non-evaluables, excluded interfaces and unresolved reviews remain visible; NOT_EVALUABLE / BUDGET_LIMITED is a budget limit, not a model failure or a score.
- Model/Agentic findings are independent; performance is deployment-attributed, never quality credit; missing metrics remain unknown (UNKNOWN is unmeasured, never zero).
- This result package does not itself activate inference services, perform infrastructure cutover or prove website deployment; public promotion is verified separately.

## Scientific acceptance and provenance

- Acceptance receipt: `welp-scientific-acceptance/1`, decision **HUMAN_ACCEPTED**, reviewed 2026-11-11. Basis: Owner explicitly recorded HUMAN_ACCEPTED for the authentic objective HelicopterBench /2 result on 2026-11-11: one LFM generation, 19/90 raw, 21.1/100 normalized, PARTIAL, no visual score. The historical /1 record (34/90) stays distinct and unchanged; nothing was regenerated, repaired or rescored, and no favorable reclassification is implied.
- The exact private decision source is retained outside this public package and is bound by SHA-256 `ad697f53f0c4ddfbb89e9c04eb0caa4da1eecc88019c708ee8a1b2461e5e8cc4`; receipts live at `receipts/acceptance-receipts.json`.
- Section manifest bindings (exact finalized sections covered by the review):

  - `helicopterbench`: `661685b0921cac90addd7b2a3adf82f1d3cf833fbc1bb879988d36d1da8c05b6`

- Export provenance: composed by the existing in-memory `export_campaign` + `accepted_export` contract; staged export sha256 `010533924d0c9a7af4c44499cc1ebe231fb3512b1791e884b30d465060823e54`; canonical evidence is PENDING_HUMAN_GATE at `WumboLabs/evaluations` until the standing-authorized registry commit pins repo/commit/path — none is fabricated here.
- Disposition history: sealed source disposition NOT_FOR_PUBLICATION (default development hold, no custom reason); superseded only by the evidence-bound HUMAN_ACCEPTED receipt above; staged disposition **WEBSITE_READY**. No explicit privacy or scope hold was overridden.

