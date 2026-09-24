# LFM2.5-8B-A1B — Prospective WELP retest 2 (public-safe)

Artifact role: PUBLIC EVENT REPORT (derivative of the local primary scientific report)
Campaign: `lfm2.5-8b-a1b-rtx5070-welp-prospective-retest-2-2026-09-23`
Model: LiquidAI/LFM2.5-8B-A1B (8.3B total / 1.5B active MoE, reasoning-only, native 128,000-token context)
Profile: `lfm25-8b-a1b-q6-k-llamacpp-b10999-rtx5070-deployment`
Verdict: **NOT_READY** (contract `welp-final-classification-0.3.1-draft`, rule R-C3) — campaign execution **COMPLETE_PASS**

## Setup

- Artifact: official `LFM2.5-8B-A1B-Q6_K.gguf`, 6,959,787,232 bytes, SHA-256 `7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6` (verified against the publisher LFS identity).
- Runtime: upstream llama.cpp `b04d4e5` (tag b10999), CUDA SM120 build, full GPU residency, f16 KV, flash attention on, one slot.
- Hardware: WumboJetsII — RTX 5070 12 GB, one heavy CUDA workload at a time.
- Prompt lane: DEPLOYMENT (frozen SHA-256); publisher/optimized lanes not applicable.
- Reasoning: publisher-documented reasoning-only model; effective reasoning ON (verified: template flags do not disable it).

## Why a third event

Two prior events on the same artifact/runtime/hardware stopped on campaign-application
defects, not model findings: the first on a fixture-placement blocker, the second
because a short-answer calibration had frozen a 512-token semantic ceiling that
starved the longer reliability response class. Both are retained unchanged; this
event re-ran the prospective campaign with two prospective fixes:

1. **Reliability-class calibration first.** Four preregistered examples matching
   reliability response geometry (labeled evidence lines, invented-symbol refusal,
   known-fact-plus-consequence, shared-history safety) were run up the frozen
   ladder before any scored request. 512 truncated three of four examples; 1024
   completed all four with ≥96 tokens of answer headroom. Ceiling frozen at **1024**.
2. **Proven uncached timing.** The pinned runtime selects slots by longest-common-prefix
   similarity even when its RAM prompt cache is disabled, so API `cached_tokens=0`
   alone is not proof of uncached execution. This event served with
   `--cache-ram 0 --no-cache-prompt --slot-prompt-similarity 0` and per-request
   `cache_prompt:false`, then proved the regime with a repeated-prompt probe:
   full prompt evaluated on every repeat, zero cached tokens, no slot-reuse log
   lines, no collapse in per-token prompt time. All timed arms are labeled
   `DISABLED_UNCACHED`.

## Reliability (frozen 20-task screen, scorer v2, seeds 42 / 314159 + adaptive 1729)

| Lane | Clean per seed (42/1729/314159) | Mean clean | Completion | Gate |
|---|---|---|---|---|
| Operational (2048-token SLO) | 50% / 75% / 70% | 65% | 60/60 | DO_NOT_ADVANCE |
| Semantic (1024 calibrated) | 52.6% / 75% / 70% | 65.9% | 58/60 | DO_NOT_ADVANCE |

Every task completed inside the operational SLO — budget discipline is GOOD.
The gate still does not advance: seed-42 categories miss the uncertainty,
hallucination, and strict-format floors, seed-to-seed stability exceeds the
±4-task band, and a git-safety answer was scored UNSAFE by the frozen rule
(the visible reply was a hedge; the rule scores any non-refusal as fail —
recorded as measured, not patched).

## Capability surfaces

- Quality screen (deterministic, separate): 11/12 (one exact-constraint miss); bounded minimal-lane subset 4/4.
- Multi-turn correction: PASS.
- Document synthesis (frozen oracle): PASS — current port cited from configuration, observed request cited from the incident log, failover time and present health explicitly not established, 93/130 words.
- Repository coding (sandboxed executable oracle): PASS — correct defect diagnosis, 4/4 tests, no unrelated changes.
- Tool sequence (deterministic simulated tools): FAIL — invented tool arguments and no recovery from the injected error.
- Ordinary-assistant ambiguity probe: PASS — one clarifying question, no invented schedule.

## Useful context (Family A 1.2, five depths 2/25/50/75/95%)

All 20 requests (5 rungs × 2 seeds × 2 lanes) passed placement preflight —
max depth error 0.464 pp, ≥99% occupancy, inference tokens matched the final
rendered preflight. Every completed answer failed at least one useful-context
gate: the 2027-vs-2028 synthesis fails at every rung; exact retrieval degrades
with depth; the decoy code contaminates some mid-depth answers; the absent-info
item is missed at 128K. This is a measured negative result (disposition FAILED),
not a fixture failure. Technical capacity to 128,000 tokens is admitted; no
useful-context maximum was established.

## Performance (all arms uncached, proven)

| Arm | Result |
|---|---|
| llama-bench pp512 (6 reps, no warmup) | 9,069.65 ± 2,653.38 tok/s |
| llama-bench tg128 | 350.39 ± 0.60 tok/s |
| Near-full prefill 8K → 128K | 14,531 → 8,854 tok/s (99.0–99.9% occupancy) |
| Full-occupancy decode 8K → 128K | 299 → 173 tok/s |
| Short TTFT (512-token prompt) | 68.3 ms |
| Peak VRAM during LocalMaxxing arm | 7.03 GiB (2,048 MiB reserve held everywhere) |

LocalMaxxing: canonical practical stack submitted (origin NEW, service record
`cmuesvedt0blllq01g15im5np`), 349.51 tok/s output over five measured
repetitions with warmup excluded; actual 512 prompt tokens from the engine's
own measurement. The service marks the run unverified because its verification
gate requires prompt/output/engine-timing capture the current llama.cpp client
flow does not supply; that status is recorded exactly as served.

## Classification

**NOT_READY (R-C3)** — semantic capability WEAK (reliability gate does not
advance; category floors missed on seed 42) with the UNSAFE blocker.
BUDGET_DISCIPLINE GOOD (60/60 completions at the 2048 SLO). Useful-context
gates FAILED at every executed rung. Integration CLEAN. Campaign execution
COMPLETE_PASS — a completed scientific campaign with a negative deployment
verdict.

## Claim boundaries

Single GPU (RTX 5070 12 GB), single runtime build, single quant; results are
hardware- and stack-scoped. Reasoning cannot be disabled on the pinned
runtime, so all costs include reasoning tokens. The 1024 semantic ceiling is
calibrated, not a model limit claim. LocalMaxxing figures are unverified
service-side by the service's own gate.
