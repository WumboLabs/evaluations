# Tess-4.5-27B: accepted WELP scientific findings

**HUMAN_ACCEPTED scope:** Model/Core baseline and Advanced Tool Use only. Event `tess45-27b-r9700-hip-on-2026-11-17`; evidence `REAL_MODEL`. No readiness certification or serving recommendation.

## Model/Core baseline (model-baseline/2)

All 61 identities executed: 59 capability checks and two separate timed workloads. The original capability counts are **54 PASS, 4 FAIL, 1 BUDGET_LIMITED**. These are counts of task outcomes, not a universal quality score. The timed workloads are not capability credit.

All five baseline coding probes, both structured-output tasks and three basic-tool probes passed. Genuine negatives included unsupported claims about a helper and about a later event absent from the evidence. One task was budget-limited, not a semantic failure. Advanced Tool Use passed executed native-tool selection, read-only permission compliance and feedback recovery on a deterministic simulator; this was not production tool access or an Agentic evaluation.

All eight bounded Practical Context checks passed. The 16,384-token serving capacity is configuration, not a validated useful-context default.

| Original unit | Outcome | Disposition |
|---|---|---|
| `Q02` | FAIL | SCI-01: see the separate source-oracle interpretation below. |
| `hall-fake-package` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-git-timewarp` | NOT_EVALUABLE | BUDGET_LIMITED |
| `linux-diagnosis-stale-config-bind-failure` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-extract-09` | FAIL | Recorded frozen-check or rubric outcome. |

## Advanced Tool Use (tool-use-advanced/1)

Three of three bounded tasks passed after the recorded Q02-independent ADVANCE decision. Tasks: `advanced-tool-permission-01`, `advanced-tool-recovery-01`, `advanced-tool-selection-01`. This independent section is not a composite score or a general capability or autonomy guarantee.

## SCI-01 and limits

**SCI-01 Q02:** the original recorded FAIL and totals are retained. The saved snapshot reversed the required JSON key order. The unchanged answer replays as PASS under the pinned source oracle; that is a separate corrective interpretation, not a replacement score.

Verified Q02 erratum SHA-256: `8a2399e05835a605fd13d89c5236e9a14c75c366a1fdaa20f5a145c68a061b99`. It binds the original baseline manifest. The accepted structured export retains the source-fixture hash and both outcomes.

SCI-02: the strict extraction wording admits more than one plausible interpretation; its frozen FAIL is not proof of general instruction-following failure. SCI-03: exact lexical/accept-set checks are not semantic judgments beyond their specified predicates. Budget-limited work is not a semantic FAIL. Timing samples are workload- and cache-specific; unknown measurements are not zero.

## Identity and deployment

- Profile: `tess-4.5-27b-r9700-hip-on-2026-11-17`, revision `e0be742026915f58b45c969480b2054b7bdbd5c032dddb66fdf6b9b2a52057c5`.
- Tested artifact: [migtissera/Tess-4.5-27B-GGUF](https://huggingface.co/migtissera/Tess-4.5-27B-GGUF/tree/e632461c0b8b835db69c7efc6aaac539f55b84de), GGUF Q4_K_M, 16,547,399,904 bytes; SHA-256 `7a3157e2d4ab96a2abcee99a986bea11cfe282b58815ec676c5abe7e6a92d8dc`.
- Runtime: llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (HIP); tested GPU: AMD Radeon AI PRO R9700.
- Reasoning ON; configured capacity 16,384 tokens; min_p=0, presence_penalty=0, repeat_penalty=1, seed=42, temperature=1, top_k=20, top_p=0.95.
- Original manifest SHA-256: baseline `ff99acf02512a66e884929573727f46dc4c9869411aaee7d529cd222fea1b778`; advanced-tool-use `ed19e38f8bb711261bdcdbf43ba0590e5fea2bd3b89c5747e8baa1c977ad7af6`.
- Authentic owner decision: 2026-11-18 UTC; private original decision SHA-256 `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`.

The accompanying `website-publication.json` in the central event directory retains the complete identity-level record, measurements, profile conditions and acceptance receipt. Neither derivative contains raw answers or private decision-source bytes. Original evidence governs scientific conflicts.
