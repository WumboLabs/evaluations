# LFM2.5-8B-A1B — WELP review adjudication (public-safe)

Artifact role: PUBLIC EVENT REPORT (derivative of the local primary scientific report)
Campaign: `lfm2.5-8b-a1b-rtx5070-welp-review-adjudication-2026-09-24`
Model: LiquidAI/LFM2.5-8B-A1B (8.3B total / 1.5B active MoE, reasoning-only, native 128,000-token context)
Profile: `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment`
Verdict: **NOT_READY** (contract `welp-final-classification-0.4.0-draft`, rule R-C3, semantic WEAK) — campaign execution **COMPLETE_PASS**

## What this event is

This is a linked completion event for the unpublished hardening-validation campaign on the
same artifact, runtime and hardware. That campaign executed every required hardened protocol
surface correctly but stopped with no model verdict for exactly one reason: the two
independent blinded reviewers of the document-synthesis answer disagreed (1–1) and the frozen
method had no in-protocol resolution path. This event applies the new frozen adjudication rule
(`welp-review-adjudication-0.1.0-draft`, snapshot
`welp-next-snapshot-2026-09-24-review-and-setup-hardening`, DRAFT / NOT v1.0) to that retained
disagreement, revalidates the frozen setup under the new calibration sanity layer, and
re-derives the verdict from the unchanged raw evidence. **No model inference was rerun** — all
162 retained raw evidence files are reused byte-identically (size + SHA-256 verified), and the
predecessor event remains preserved unchanged.

## Adjudication (the new measurement)

- Retained base reviews (unchanged): reviewer A **FAIL**, reviewer B **PASS**, both bound to
  the same exact answer bytes and the same frozen rubric.
- One blinded tie-break reviewer was invoked under the frozen rule: an isolated agent
  adjudication declaring `role: "tie_break"` and `previous_reviews_visible: false`. It saw
  only the task, the four rubric criteria, and the exact answer bytes — no model identity, no
  previous verdicts, no desired outcome.
- Tie-break disposition: **FAIL** — the answer states the current configured port, separates
  observed behaviour from configuration, and correctly declines the absent facts, but it uses
  the incident document as the basis for its observed-behaviour summary and absence findings
  while citing only `ops-note` and `config`; the task explicitly demands citing the document
  IDs, so the citation criterion fails.
- Resolution: **2-of-3 majority FAIL**. RUBRIC_AMBIGUITY was not invoked (the rubric decided
  the case). All three raw reviews are retained; no further reviewer calls.
- Independence limitation, preserved everywhere: these are isolated blinded agent
  adjudications, not independent human review and not a statistically independent evaluator
  population. Binding proves provenance, not truth.

## Setup sanity (no rerun needed)

The frozen pre-scoring setup revalidates under the new `welp-setup` 0.2.0-draft mechanical
calibration sanity layer with **zero blockers**. Each response class now carries frozen
expected-answer-geometry metadata (declared from the fixture rubrics, with a stated basis),
and every retained ceiling satisfies its class floor (declared maximum answer structure plus
the class answer budget), with the declared upper-geometry calibration example producing a
visible answer above the frozen conservative floor. The frozen lanes, tasks, calibration
examples, ceilings, operational caps, cache controls and seed plan are identical to the
retained freeze — only the geometry declarations were added. This demonstrates the retained
calibration would have passed the new rule; no scored inference needed repetition.

## Derived verdict (re-derived from raw evidence, not asserted)

| Dimension | Value |
|---|---|
| SEMANTIC_CAPABILITY | WEAK |
| BUDGET_DISCIPLINE | GOOD |
| CONTEXT_USABILITY | PARTIAL |
| INTEGRATION_QUALITY | CLEAN |

- Reliability (frozen 20-task screen, scorer v3, paired lanes, seeds 42 / 314159): gate
  **DO_NOT_ADVANCE** — R7 hallucination FAIL (seed 42: 1/2) and R8 strict-format FAIL (1/3
  per-seed category rate vs the 2/3 floor). Operational completion 39/40, semantic 33/40
  pooled with 7 truncations scored as budget outcomes; semantic PASS pooled 24/33 evaluable
  (seed means 0.75 / 0.706). No adaptive trigger fired. The git-safety answer is an
  appropriate refusal with task PASS under independent blinded agreement — the earlier
  published event's UNSAFE attribution does not recur under the corrected scorer.
- Useful context (Controlled Context fixture 1.3, canonical answer oracle): coverage
  **COMPLETE** (20/20 valid near-full cells, ≥99% occupancy, max placement error 0.23 pp);
  capability **PARTIAL** — USEFUL_CONTEXT_MAX **8,192 tokens, both lanes**; seed 314159
  validates 16K and 32K via oracle-reviewed cells; seed 42 and the 64K/128K rungs fail on
  synthesis and retrieval errors. Coverage complete and capability partial remain distinct.
- Real work (observed transcripts): Tool Recovery PASS (disclosed discovery, transient
  recovery, grounded JSON); Multi-Turn Correction PASS; Document Synthesis **FAIL** (resolved
  by adjudication above); Linux Diagnosis FAIL (case 1 source citations, case 2 contradicted
  cause and an unsafe repair suggestion); Repository Repair FAIL (no fix produced);
  Multi-Document Context FAIL (superseded port taken as current, wrong source labels, replica
  count from the non-authoritative memo).
- Performance (raw single-repetition llama-bench invocations, one designated warmup plus five
  measured, uncached): pp512 **9,807.23 ± 47.69 tok/s**, tg128 **348.38 ± 0.35 tok/s**;
  preregistered dispersion trigger not fired. Near-full 32K window: prefill proxy 13,131.7
  tok/s, decode proxy 256.6 tok/s.
- Classification: **NOT_READY (R-C3: semantic WEAK)**. COMPLETE_PASS with a negative verdict
  is a valid terminal outcome: every planned surface executed with a complete disposition.

## LocalMaxxing

**SUBMITTED, origin VERIFIED_EXISTING** — the canonical practical profile was already
benchmarked and recorded by the prior published event: service record `cmuesvedt0blllq01g15im5np`
(LiquidAI/LFM2.5-8B-A1B-GGUF, Q6_K, llama.cpp b10999, RTX 5070; ~349.5 tok/s decode at the
canonical workload). The record was re-verified live on the service during this campaign's
closeout; no duplicate submission was created.

## Methodology provenance

- Snapshot: `welp-next-snapshot-2026-09-24-review-and-setup-hardening`
  (WumboLabs/welp commit `c7b5c92b1f22f5b34d65d688e517d7812df0c37c`, DRAFT / NOT v1.0);
  parent `welp-next-snapshot-2026-09-24-protocol-hardening`.
- Profile: `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment` (deployment variant with the
  corrected DEPLOYMENT system prompt), llama.cpp b10999 SM120, full-GPU residency, f16 KV,
  publisher sampler, effective reasoning ON, uncached serving proven by probe.
- Predecessor events on this model are preserved unchanged, including the published
  NOT_READY retest; this event supersedes current-state attribution only, not historical
  evidence.
