# Bonsai 2 27B — WELP methodology-revision supplement (thinking-off profile, RTX 5070 12 GB)

- **Event ID:** `bonsai2-27b-rtx5070-welp-methodology-supplement-20260920`
- **Event date:** 2026-09-20 (profile-pure correction pass same date)
- **Model:** Ternary Bonsai 2 27B (`prism-ml/Ternary-Bonsai-2-27B-gguf`, PrismML)
- **New profile:** `bonsai2-27b-ptq1-0-prism-llamacpp-thinking-off` (declared reasoning state: OFF via `chat_template_kwargs.enable_thinking=false`)
- **Prior profile (immutable):** `bonsai2-27b-ptq1-0-prism-llamacpp` (reasoning-on; historical NOT_READY, event `bonsai2-27b-rtx5070-welp-20260918`)
- **Hardware:** RTX 5070 12 GB
- **Outcome:** **PASS — campaign execution COMPLETE_PASS**
- **Classification (new profile):** **READY_WITH_GUARDRAILS** (WELP final-classification rule R-C5, derived by the canonical harness — not hand-selected)

All measurements below are MEASURED unless labeled otherwise; derived items are labeled.
Public-safe scientific record; the retained local campaign bundle
(`research/model-evaluations/bonsai-2-27b/bonsai-2-27b-welp-methodology-supplement-2026-09-20`,
including `HUMAN-GATE-CORRECTION.md`) governs on any conflict.

## 1. What this event is

A bounded supplement executing the 2026-09-19 WELP methodology revision (snapshot
`welp-next-snapshot-2026-09-19-methodology-revision`, **DRAFT — NOT v1.0**) on Bonsai 2:
71 generation requests, inside the frozen budget. It links to — and modifies nothing in —
the 2026-09-18 original event. Old and new aggregate scores are **NOT directly equivalent
across methodologies** (different outcome semantics, budgets, and profiles).

A same-day human-gate correction pass diagnosed two report defects: (A) a prose-only
aggregate transcription error (actual raw outcomes were always 36 PASS / 4 FAIL / 0
NOT_EVALUABLE, 40/40 COMPLETE), and (B) a campaign scoping error that fed the reasoning-on
operational lane into the thinking-off profile's BUDGET_DISCIPLINE (CASE 1: campaign/report
invocation misuse — no WELP protocol defect; 0 protocol rules mandate cross-profile
consumption). Classification was recomputed from profile-pure evidence with **0 additional
inference requests** (≤40/≤2 correction budgets; 0 used). Raw evidence, the prior event, and
the frozen WELP snapshot were byte-verified untouched.

## 2. Profile boundary

Reasoning mode is a declared material profile dimension under
`welp-generation-budget-0.1.0-draft`, so a new profile ID was required. Exact delta:
`enable_thinking=false` (the only reasoning control proven effective on the pinned runtime;
per-request budget/effort kwargs are ignored by this build). Unchanged: artifact
(PTQ1_0 SHA-256 `53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3`),
runtime (`PrismML-Eng/llama.cpp` `9a9394a895b96003ca842a6041cb28ac49a108f7`), full-GPU
topology, FP16 KV, flash attention, sampler. ENHANCED_SEMANTIC admission: known-answer
battery 4/4 PASS; reasoning-control effectiveness verified (requested == effective).

## 3. Reliability — thinking-off profile (frozen 20-task fixture v2, scorer v2)

| Metric | Seed 42 | Seed 314159 |
|---|---|---|
| Semantic PASS (evaluable denominator, ceiling 2048) | **18/20** | **18/20** |
| Completion at ceiling | 20/20 | 20/20 |
| Truncation / finish=length | 0 | 0 |

Semantic-clean 0.90 per seed (0.90 pooled), stability range 0 tasks; adaptive third seed NOT
triggered (all predeclared bands outside). Category floors: hallucination 4/4 + 4/4, uncertainty
3/3 + 3/3, strict interfaces 2/3 + 2/3 (load-bearing: a real exact-format defect,
`strict-extract-09`, fails both seeds), sycophancy 2/3 + 2/3, 0 UNSAFE. The 4 semantic FAILs
are genuine, not mechanical.

Profile-pure operational-ceiling audit (DERIVED, 0 new requests; deterministic fixed-seed
stream-identity rule, per-instance table retained): at the legacy 20–140-token operational
caps, derived completion 0.55/0.65 with **EXHAUSTED_IN_ANSWER only** — verbosity-vs-cap-sizing,
never reasoning starvation (contrast: the reasoning-on profile at the same caps completes 1/20
with 17/20 EXHAUSTED_IN_REASONING).

## 4. Context — capacity vs semantic vs operational, per profile

| Profile | Capacity | Semantic useful context | Operational useful context |
|---|---|---|---|
| thinking-off (this event) | 65,536 serves at ~99.6% occupancy; 98,304+ FIT_LIMIT | **65,536 VALIDATED 2/2** (all six gates; stop at 40/512 reserve tokens) | **65,536 VALIDATED 2/2** (same requests; the 512-token reserve is the rung output budget) |
| reasoning-on (prior event, unchanged) | same geometry | 32,768 VALIDATED (prior snapshot); 65K semantic lane never measured | **32,768** (2/2 prior); 65K = 1/2 seeds, budget-starved seed retained with in-trace retrieval evidence (BUDGET_LIMITED-class; never marked retrieval-FAILED, never promoted to semantic PASS) |

The prior event's "64K FAILED 1/2" is thereby precisely attributed to the reasoning-on
profile: capacity and retrieval were intact; its reasoning consumed the answer.

## 5. Classification — READY_WITH_GUARDRAILS (thinking-off only)

Dimensions (profile-pure): SEMANTIC_CAPABILITY ACCEPTABLE · BUDGET_DISCIPLINE POOR (this
profile's own ceiling audit) · CONTEXT_USABILITY VALIDATED · INTEGRATION_QUALITY CLEAN ·
campaign_execution_outcome COMPLETE_PASS. R-C5: POOR budget discipline with acceptable
semantics, and the declared alternative lane (ceiling 2048, proven-effective reasoning-off
control) completes 40/40 at 0.90 semantics → READY_WITH_GUARDRAILS, not LIMITED_ROLE_ONLY.

Practical guardrails: pin `enable_thinking=false`; size generation ceilings to the profile's
measured verbosity (legacy 20–140-token caps truncate 35–45% of tasks on answer length alone);
never trust strict one-shot exact formats unverified; verify nonexistent-API/package/commit
claims. The default reasoning-on profile remains operationally budget-hostile and keeps its
historical NOT_READY; the thinking-off result does not retroactively improve it. **Neither
profile represents "Bonsai 2" universally — configuration is part of the result.**

## 6. LocalMaxxing disposition

**SUBMITTED** (origin NEW, 2026-09-21 terminal closeout): the canonical practical profile's
llama-bench arm — unchanged by the reasoning-state delta, which is not a LocalMaxxing
benchmark identity field and exercises no chat reasoning — is recorded on the service as
[`cmuajqjjd09y4lq01wrf8ht0j`](https://www.localmaxxing.com/api/speed-tests/cmuajqjjd09y4lq01wrf8ht0j)
(APPROVED; tokSOut 59.22 / tokSPrefill 586.54, PTQ1_0, PrismML fork `9a9394a8`, RTX 5070;
duplicate audit NO_EXACT_MATCH). `verifiedRun: false` recorded honestly. Owning record: the
2026-09-18 event's campaign bundle; this supplement carried the disposition to terminal state
without any new benchmark.

## 7. Testing debt state (after this event)

- **Resolved pending human acceptance (now human-accepted):** `bonsai2-reliability-budget-parity`
  (thinking-off lane complete, new profile classified) and `bonsai2-useful-64k-reserve`
  (re-validated under the frozen 512-token reserve) — both survived the profile-pure correction.
- **Open, specialized/optional:** PQ2_0 packing comparison; OMP agent module; vision module;
  `bonsai2-reasoningon-operational-profile-repair` (reasoning-on profile only — the pinned
  runtime ignores per-request reasoning budgets); `bonsai2-thinkingoff-ceiling-guardrail`
  (verbosity vs legacy cap sizing).

## 8. Publication chronology

Executed and corrected 2026-09-20; human-accepted at the closeout gate; published to
`WumboLabs/evaluations` at the human publication gate (see the registry event record for the
exact evidence commit). No eval-* repository exists or was created; the prior event is
byte-unchanged.
