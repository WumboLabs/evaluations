# Occamy-1.0: accepted WELP scientific findings

**HUMAN_ACCEPTED scope:** Model/Core baseline and Advanced Reasoning only. Event `occamy10-r9700-hip-on-2026-11-17`; evidence `REAL_MODEL`. No readiness certification or serving recommendation.

## Model/Core baseline (model-baseline/2)

All 61 identities executed: 59 capability checks and two separate timed workloads. The original capability counts are **47 PASS, 12 FAIL, 0 BUDGET_LIMITED**. These are counts of task outcomes, not a universal quality score. The timed workloads are not capability credit.

All five baseline coding probes and both structured-output tasks passed. Genuine negatives included a fabricated Git command, unsupported present-health inference, two Multi-Document failures and strict format failure after executed tool feedback. The original retained request strings were already NFC; this does not establish general Unicode tokenizer equivalence.

Six of eight bounded Practical Context checks passed; both Multi-Document checks failed. The 16,384-token serving capacity is configuration, not a validated useful-context default.

| Original unit | Outcome | Disposition |
|---|---|---|
| `Q02` | FAIL | SCI-01: see the separate source-oracle interpretation below. |
| `context-multidocument-v2-6144-seed-42` | FAIL | Recorded frozen-check or rubric outcome. |
| `context-multidocument-v2-8192-seed-42` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-fake-cuda` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-fake-package` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-git-timewarp` | FAIL | Recorded frozen-check or rubric outcome. |
| `linux-diagnosis-stale-config-bind-failure` | FAIL | Recorded frozen-check or rubric outcome. |
| `linux-diagnosis-startup-invalid-config` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-extract-09` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-limit-05` | FAIL | Recorded frozen-check or rubric outcome. |
| `tool-recovery-01` | FAIL | Recorded frozen-check or rubric outcome. |
| `uncertainty-file` | FAIL | Recorded frozen-check or rubric outcome. |

## Advanced Reasoning (reasoning-advanced/1)

Three of three bounded tasks passed after the recorded Q02-independent ADVANCE decision. Tasks: `advanced-constraints-01`, `advanced-evidence-01`, `advanced-revision-01`. This independent section is not a composite score or a general capability or autonomy guarantee.

## SCI-01 and limits

**SCI-01 Q02:** the original recorded FAIL and totals are retained. The saved snapshot reversed the required JSON key order. The unchanged answer replays as PASS under the pinned source oracle; that is a separate corrective interpretation, not a replacement score.

Verified Q02 erratum SHA-256: `5fcef1deb62a1f7d3c1b74aec6bdc3884a23312673cbe0f8e14302cba09a12ed`. It binds the original baseline manifest. The accepted structured export retains the source-fixture hash and both outcomes.

SCI-02: the strict extraction wording admits more than one plausible interpretation; its frozen FAIL is not proof of general instruction-following failure. SCI-03: exact lexical/accept-set checks are not semantic judgments beyond their specified predicates. Budget-limited work is not a semantic FAIL. Timing samples are workload- and cache-specific; unknown measurements are not zero.

## Identity and deployment

- Profile: `occamy-1.0-r9700-hip-on-2026-11-17`, revision `8fe42148c60216898b68983dbd77167e0e2e907572a7d3d54eafbecf9d521198`.
- Tested artifact: [Accio-Lab/occamy-1.0-GGUF](https://huggingface.co/Accio-Lab/occamy-1.0-GGUF/tree/15027de49a5f8bbb5a131ed3fcfc1b54a543089d), GGUF Q4_K_M, 21,166,757,696 bytes; SHA-256 `ffb25f763ff9c27f5f4e2adcdef399c5654f9f840fdac33dffe7035ba8266a87`.
- Runtime: llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (HIP); tested GPU: AMD Radeon AI PRO R9700.
- Reasoning ON; configured capacity 16,384 tokens; min_p=0, presence_penalty=0, repeat_penalty=1, seed=42, temperature=1, top_k=20, top_p=0.95.
- Original manifest SHA-256: baseline `05ef081eed62e764b5934b64b7b0fc9df11916e32e2bbdd9dfab66341c0ce3f0`; advanced-reasoning `d78b52f56c64a97aa123a5891110b56230e5799fa75a2410f3f2389d2a6b4c48`.
- Authentic owner decision: 2026-11-18 UTC; private original decision SHA-256 `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`.

The accompanying `website-publication.json` in the central event directory retains the complete identity-level record, measurements, profile conditions and acceptance receipt. Neither derivative contains raw answers or private decision-source bytes. Original evidence governs scientific conflicts.
