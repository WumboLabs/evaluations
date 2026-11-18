# Nanbeige4.3-33B: accepted WELP scientific findings

**HUMAN_ACCEPTED scope:** Model/Core baseline and Advanced Reasoning only. Event `nanbeige43-33b-r9700-hip-on-recovery-2026-11-16`; evidence `REAL_MODEL`. No readiness certification or serving recommendation.

## Model/Core baseline (model-baseline/2)

All 61 identities executed: 59 capability checks and two separate timed workloads. The original capability counts are **53 PASS, 5 FAIL, 1 BUDGET_LIMITED**. These are counts of task outcomes, not a universal quality score. The timed workloads are not capability credit.

All five coding and three basic-tool probes passed. Genuine negatives included unsupported current-health inference, an independently reviewed Git amend failure, and a contradictory bounded-context answer. One task was budget-limited, not a semantic failure. This is the November 16 recovery campaign only; no earlier partial result, response or review earned credit.

Seven of eight bounded Practical Context checks passed; the 4K seed-42 family-A check did not. The 16,384-token serving capacity is configuration, not a validated useful-context default.

| Original unit | Outcome | Disposition |
|---|---|---|
| `Q02` | FAIL | SCI-01: see the separate source-oracle interpretation below. |
| `context-family-a-v2-4096-seed-42` | FAIL | Recorded frozen-check or rubric outcome. |
| `git-amend` | FAIL | Recorded frozen-check or rubric outcome. |
| `hall-git-timewarp` | NOT_EVALUABLE | BUDGET_LIMITED |
| `linux-diagnosis-startup-invalid-config` | FAIL | Recorded frozen-check or rubric outcome. |
| `strict-extract-09` | FAIL | Recorded frozen-check or rubric outcome. |

## Advanced Reasoning (reasoning-advanced/1)

Three of three bounded tasks passed after the recorded Q02-independent ADVANCE decision. Tasks: `advanced-constraints-01`, `advanced-evidence-01`, `advanced-revision-01`. This independent section is not a composite score or a general capability or autonomy guarantee.

## SCI-01 and limits

**SCI-01 Q02:** the original recorded FAIL and totals are retained. The saved snapshot reversed the required JSON key order. The unchanged answer replays as PASS under the pinned source oracle; that is a separate corrective interpretation, not a replacement score.

Verified Q02 erratum SHA-256: `78baeb29ad4fe14dc99e30881c582e83c1f6aea0a57045291fc5669d829cc970`. It binds the original baseline manifest. The accepted structured export retains the source-fixture hash and both outcomes.

SCI-02: the strict extraction wording admits more than one plausible interpretation; its frozen FAIL is not proof of general instruction-following failure. SCI-03: exact lexical/accept-set checks are not semantic judgments beyond their specified predicates. Budget-limited work is not a semantic FAIL. Timing samples are workload- and cache-specific; unknown measurements are not zero.

## Identity and deployment

- Profile: `nanbeige4.3-33b-r9700-hip-recovery-on-2026-11-16`, revision `ef3f2903becc1a643b6334aead6f4ef1b686f29f77b7e6f5190e5cd71b87cd70`.
- Tested artifact: [bartowski/Nanbeige_Nanbeige4.3-33B-GGUF](https://huggingface.co/bartowski/Nanbeige_Nanbeige4.3-33B-GGUF/tree/9beb68421fdf7be095093a6888325fa2c83ddd38), GGUF Q4_K_M, 20,788,825,216 bytes; SHA-256 `2cef79855ca47ee6571e166db32a07089e34f3cf78e0397b262d124ddb814c37`.
- Runtime: llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (HIP); tested GPU: AMD Radeon AI PRO R9700.
- Reasoning ON; configured capacity 16,384 tokens; min_p=0, presence_penalty=0, repeat_penalty=1, seed=42, temperature=0.6, top_k=0, top_p=0.95.
- Original manifest SHA-256: baseline `c1130de723898258b53489ccf9e9c24aa23082acf498002a3c2b68dfe2bc49c8`; advanced-reasoning `fe376293602ebc6cfad102617b2896235d0f9313db23cbb1b43fa32dc6f0031d`.
- Authentic owner decision: 2026-11-18 UTC; private original decision SHA-256 `bbd66fe6a7314746f8bb77e386c5e68cf78b6121c374c35d5a0a22a2b54b10e4`.

The accompanying `website-publication.json` in the central event directory retains the complete identity-level record, measurements, profile conditions and acceptance receipt. Neither derivative contains raw answers or private decision-source bytes. Original evidence governs scientific conflicts.
