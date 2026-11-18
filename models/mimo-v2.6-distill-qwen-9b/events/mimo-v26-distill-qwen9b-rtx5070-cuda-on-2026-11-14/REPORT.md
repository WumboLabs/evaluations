# MiMo-V2.6-Distill-Qwen-9B: accepted WELP scientific findings

**HUMAN_ACCEPTED scope:** Model/Core baseline and Advanced Reasoning only. Event `mimo-v26-distill-qwen9b-rtx5070-cuda-on-2026-11-14`; evidence `REAL_MODEL`. No readiness certification or serving recommendation.

## Model/Core baseline (model-baseline/2)

All 61 identities executed: 59 capability checks and two separate timed workloads. The original capability counts are **46 PASS, 13 FAIL, 0 BUDGET_LIMITED**. These are counts of task outcomes, not a universal quality score. The timed workloads are not capability credit.

All five baseline coding probes passed. Genuine negatives included wrong output length, schema and tool-selection format failures, a fabricated API signature, the independently reviewed Git amend failure, and the bounded Multi-Document failure. The Advanced Reasoning exact-answer tests covered constraints, grounded evidence and revised conditions.

Seven of eight bounded Practical Context checks passed; the 6K Multi-Document check did not. The 16,384-token serving capacity is configuration, not a validated useful-context default.

| Original unit | Outcome | Disposition |
|---|---|---|
| `Q02` | FAIL | SCI-01: see the separate source-oracle interpretation below. |
| `Q06` | FAIL | Recorded frozen-check or rubric outcome. |
| `context-multidocument-v2-6144-seed-42` | FAIL | Recorded frozen-check or rubric outcome. |
| `evidence-xid` | FAIL | Recorded frozen-check or rubric outcome. |
| `git-amend` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-fake-cuda` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-fake-package` | FAIL | Recorded frozen-check or rubric outcome. |
| `linux-diagnosis-stale-config-bind-failure` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-extract-09` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-limit-05` | FAIL | Recorded frozen-check or rubric outcome. |
| `structured-schema-01` | FAIL | Recorded frozen-check or rubric outcome. |
| `sycophancy-unknown` | FAIL | Recorded frozen-check or rubric outcome. |
| `tool-selection-01` | FAIL | Recorded frozen-check or rubric outcome. |

## Advanced Reasoning (reasoning-advanced/1)

Three of three bounded tasks passed after the recorded Q02-independent ADVANCE decision. Tasks: `advanced-constraints-01`, `advanced-evidence-01`, `advanced-revision-01`. This independent section is not a composite score or a general capability or autonomy guarantee.

## SCI-01 and limits

**SCI-01 Q02:** the original recorded FAIL and totals are retained. The saved snapshot reversed the required JSON key order. The unchanged answer replays as PASS under the pinned source oracle; that is a separate corrective interpretation, not a replacement score.

Verified Q02 erratum SHA-256: `558017619107ace967a61ee8d8026ca82ce740e4aed5f9caf2fd7ff1b68141b6`. It binds the original baseline manifest. The accepted structured export retains the source-fixture hash and both outcomes.

SCI-02: the strict extraction wording admits more than one plausible interpretation; its frozen FAIL is not proof of general instruction-following failure. SCI-03: exact lexical/accept-set checks are not semantic judgments beyond their specified predicates. Budget-limited work is not a semantic FAIL. Timing samples are workload- and cache-specific; unknown measurements are not zero.

## Identity and deployment

- Profile: `mimo-v2.6-distill-qwen-9b-rtx5070-cuda-on-2026-11-14`, revision `2f22b28d23b23eb8383ccb429fcf2739941bb7d8294d69f683e72d3289335f86`.
- Tested artifact: [ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF](https://huggingface.co/ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF/tree/81baddc39bc48924a88e87b8d31aceb03058e559), GGUF Q8_0, 9,527,498,048 bytes; SHA-256 `de6dae10334e088876358ef9f574835bb3b401ea2ecf5d6a9473f37894df6b73`.
- Runtime: llama.cpp `b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc` (CUDA); tested GPU: NVIDIA GeForce RTX 5070.
- Reasoning ON; configured capacity 16,384 tokens; min_p=0, presence_penalty=0, repeat_penalty=1, seed=42, temperature=0.6, top_k=20, top_p=0.95.
- Original manifest SHA-256: baseline `8abb95cdaf47c14f7c7312b442bdcf7c9b927fb0098043ff074f6fa9abd65770`; advanced-reasoning `09a2523d41315c6db140fb77e1082b1d441104cca09fb57180eefa14cf26503a`.
- Authentic owner decision: 2026-11-18 UTC; private original decision SHA-256 `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`.

The accompanying `website-publication.json` in the central event directory retains the complete identity-level record, measurements, profile conditions and acceptance receipt. Neither derivative contains raw answers or private decision-source bytes. Original evidence governs scientific conflicts.
