# Nemotron 3 Nano 4B / RTX 5070 — full current-WELP recharacterization (public summary)

Campaign: `nemotron3-nano-4b-rtx5070-welp-recharacterization-2026-09-11` ·
executed 2026-09-11 · published 2026-09-12 ·
Outcome: **PASS — NEMOTRON3_NANO_4B_RTX5070_RECHARACTERIZED** ·
Classification: **READY_WITH_GUARDRAILS** (reliability is the guardrail) ·
Append-only follow-up to the historical 2026-08-25 record
([`report.md`](../report.md)), which remains unchanged below.

## Why a recharacterization

The historical campaign was **PROTOCOL_BLOCKED at the Phase-3 gate decision**:
the model passed the 12/12 practical screen, but the protocol of that day
defined no deterministic advancement threshold (finding F-01), and no versioned
Phase-4 contract existed — so no deterministic PASS/FAIL could be produced.
This campaign re-ran the entire characterization under the current WELP
protocol, whose deterministic phase gates resolve that blockage without any
protocol modification. The historical report is preserved unchanged; this
report supersedes it **as the current characterization** while the historical
record remains the accurate account of what the 2026-08-25 campaign measured.

## Exact identity

- Model: **NVIDIA Nemotron 3 Nano 4B** — official repositories
  `nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF` (GGUF) and
  `nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16` (BF16 weights); pinned revision
  `ba223d14e45525f7fae81db77ea8cabeb2fc6c25`. Unified reasoning/non-reasoning
  instruction model (reasoning controlled at serving time via the
  `enable_thinking` template kwarg, default ON).
- Architecture: `nemotron_h` — **dense** hybrid Mamba-2/MLP with exactly 4
  attention layers (42 blocks total), 3.97B parameters, all active per token.
  **Not MoE**: the MoE sibling is Nemotron 3 Nano 30B-A3B; family-level
  assumptions do not apply to this 4B model.
- Tested artifact: `NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf` — the **only**
  official llama.cpp quant NVIDIA publishes (SHA-256
  `be5d9a656a51922f24f1f09a759cebb694e1f5d9728bf0ef9f8c972c5a0b5ef2`,
  2,837,072,864 bytes). BF16 is fit-limited on this 12 GB card at the tested
  context targets, so Q4_K_M is the canonical deployment surface; the Q4_K_M
  quality confound is disclosed, not resolved.
- Runtime: llama.cpp b10449, commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`,
  CUDA SM120. Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB,
  Ryzen 7 9800X3D. Full GPU residency, f16 KV, reasoning-off baseline.

## Performance

Short prompts: TTFT ~46 ms, decode ~186.6 tok/s. Moderate ~3,900-token
prompts: TTFT ~507 ms, prefill ~7,498 tok/s, decode ~182.9 tok/s. Peak
247–249 W, 75 °C, zero OOM/CUDA errors/Xid.

## Quality and capabilities

Frozen 12-task model-neutral screen (mechanical scorer, frozen before
outputs): **12/12** — factual instruction, structured JSON, retrieval,
conflict resistance, absent-information grounding, instruction retention,
repeat consistency, extraction, false premise, uncertainty behavior.
Bounded capability dispositions: reasoning TESTED_PASS (official thinking
mode), coding TESTED_PASS (executable, frozen cases), tool calling
TESTED_PASS (structural validity + grounded continuation; not
autonomous-agent qualification), agent use TESTED_LIMITED, structured output
TESTED_PASS, multilingual/multimodal NOT_APPLICABLE (no advertised claim).

## The historical 0.93 vs 0.38 numbers

These were two different instruments and are **not comparable**:

- **0.93** = the Phase-3 12-task practical-viability *screen* score
  (0.9333/0.90/0.9333 across three seeds) — a triage surface.
- **0.38** = the Phase-4 54-task reliability-corpus clean-pass rate
  (0.377 clean, 0.259 hallucination) — a much harder adversarial surface,
  measured later by a corrective milestone.

Classification: methodology surface difference; neither result was
invalidated. The genuine behavioral signal — strong bounded/structured
behavior alongside weak adversarial reliability — was freshly retested in
this campaign.

## Reliability (the guardrail)

Current-WELP bounded reliability at the practical profile, deterministic
20-request stratified sample of the proven mechanical corpus, two frozen
seeds:

| Seed | Clean pass | Hallucination | Structural failure | Transport success |
|---|---|---|---|---|
| 42 | 6/20 (0.30) | 4/20 (0.20) | 2/20 | 20/20 |
| 314159 | 5/20 (0.25) | 3/20 (0.15) | 2/20 | 20/20 |

**Both readings must be preserved together.** Transport/runtime reliability
is strong, and bounded quality/structured behavior is clean. But behavioral
reliability has **measurable hallucination and evidence-discipline defects**
under the adversarial corpus: the model confidently fabricated a nonexistent
CUDA API, capitulated to a false user assertion, and missed
evidence-discipline labels. Practical guardrail: independently verify
technical/factual claims in adversarial or evidence-discipline-sensitive
contexts. The 12/12 quality screen is **not** evidence of universal
reliability.

## Context architecture insight

First hybrid Mamba-2 model characterized under current WELP on this host:
the 4 attention layers carry context-linear KV (~16 KiB/token f16), while
the 38 Mamba-2 layers carry a fixed, context-independent recurrent state
(~100–300 MiB). Measured allocation confirms this hybrid memory model —
the full 262,144-token slot fits in 7,268 MiB with 4,546 MiB free.

## Context envelope — COMPLETE

All five useful-context fields (exact retrieval, synthesis, decoy
resistance, absent-information grounding, instruction/output compliance)
passed the **strict aggregate at every tested rung**, at ≥99.48% near-full
occupancy of the usable budget, with depth-placement errors ≤0.21 pp:

| Rung | Occupancy | Prefill | Decode | Strict aggregate |
|---|---|---|---|---|
| 8,192 | 99.51% | 7,735 tok/s | — | PASS |
| 32,768 | 99.48% | 6,758 tok/s | 152.8 tok/s | PASS |
| 131,072 | 99.49% | 4,348 tok/s | 112.4 tok/s | PASS |
| 262,144 (seed 42) | 99.49% | 2,877 tok/s | 79.0 tok/s | PASS |
| 262,144 (seed 314159) | 99.49% | 2,877 tok/s | 81.4 tok/s | PASS |

- **Native maximum 262,144 = VALIDATED**: capacity admitted, near-full
  performance measured (uncached prefill, cached tokens 0), and strict
  useful-context **PASS at both required seeds**.
- **Official context extensions: NONE** — a source-backed absence on both
  official model cards. The family "1M" claim belongs to the 30B-A3B MoE
  sibling; the GGUF header's 1,048,576 is converter metadata, not a card
  claim.
- **MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES** — every authoritative
  maximum carries a completed evidence-backed disposition.

Bounded interpretation: the tested frozen near-full context fixture passes
strictly across all tested rungs, including both native-maximum seeds. This
is **not** proof of universal long-document reasoning on arbitrary material.

## Practical profile

**32,768 default** (near-full decode ~153 tok/s, ~3.4 GiB VRAM) /
**131,072 guarded** (near-full decode ~112 tok/s, ~5.1 GiB VRAM) for
long-document work with latency tolerance. The native 262,144 surface is
functional but boundary-class (~90 s TTFT, ~79 tok/s decode) — not a daily
profile.

## LocalMaxxing

**SUBMITTED, origin VERIFIED_EXISTING** — submission
`cmt86gy1j000eli01ca3cwwn0` (185.8 tok/s out, approved 2026-08-25). The
exact canonical practical profile (Q4_K_M, llama.cpp b10449, 32,768 context,
f16 KV, full GPU, RTX 5070) was already on the service, so per the
never-duplicate rule **zero new submissions** were created. A fresh local
benchmark (tg128 191.0 tok/s, pp512 8,275 tok/s, 5 reps) reproduces the
submitted result.

## Limitations

- Q4_K_M quantization confound disclosed, not measured against BF16 (BF16
  does not fit the tested context targets on 12 GB).
- Reliability used the deterministic 20-request stratified sample of the
  proven 54-task corpus (current standard request count); rates are
  sample-weighted, not corpus-exact.
- Quality screen is 12 tasks at temp 0, seed 42 — bounded, not exhaustive.
- Card claims are external reported material; artifact identity is anchored
  on the verified SHA-256 of the local artifact.
- Results are bounded by the tested artifact, runtime, hardware,
  configuration, and protocol snapshot; they are not universal model
  rankings.

## Relationship to the historical record

This repository now holds **two evidence generations**: the 2026-08-25
PROTOCOL_BLOCKED campaign ([`report.md`](../report.md), unchanged) and this
2026-09-11 current-WELP recharacterization. The new campaign resolves the old
protocol blockage, reproduces the historical reliability weakness on the
current instrument, and completes the context record through the validated
native maximum. Neither generation rewrites the other.

Canonical scientific authority: the local WELP campaign `REPORT.md` for
`nemotron3-nano-4b-rtx5070-welp-recharacterization-2026-09-11`. This summary
is a public derivative; the campaign report governs on any conflict.
