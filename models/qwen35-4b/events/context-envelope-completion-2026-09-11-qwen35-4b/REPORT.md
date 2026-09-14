# Qwen3.5-4B / RTX 5070 — full model-card context envelope completion (public summary)

Campaign: `qwen35-4b-rtx5070-context-completion-2026-09-11` · executed 2026-09-11 ·
Outcome: **PASS — QWEN35_4B_CONTEXT_ENVELOPE_COMPLETED** ·
Classification: **READY_WITH_GUARDRAILS** (unchanged) ·
Append-only follow-up to the 2026-09-09 baseline record
([`EVIDENCE-SUMMARY.md`](../EVIDENCE-SUMMARY.md)), published 2026-09-11.

## Why a follow-up

The 2026-09-09 baseline record disclosed the full model-card context envelope
as NOT complete under the corrected WELP near-full occupancy standard:
nothing above 65,536 had been tested and the exact maxima carried no
dispositions. This bounded completion campaign closes that debt. The baseline
summary is preserved unchanged; this report supersedes it **for context claims
only** (performance, quality, and reliability surfaces remain inherited from
the baseline).

## Tested stack (identical to the baseline, hash re-verified)

- Model: Qwen/Qwen3.5-4B @ `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`
  (instruct, text-only, non-thinking surface).
- Artifact: `Qwen3.5-4B-BF16.gguf` (Unsloth rev `e87f1764…`, SHA-256
  `9e6e2841a75f503ccb330831832fd7861266e187e0dbf149a954219ccb8c197a`) —
  BF16 weights / F16 KV (primary surface) / F32 recurrent state.
- Runtime: llama.cpp b10449 (`0d9ceae1e…`), CUDA 13.3, SM120.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB, Ryzen 7 9800X3D.

## Context envelope — every exact maximum dispositioned

| Surface | Exact maximum | Disposition | Basis |
|---|---|---|---|
| Native primary (BF16 + f16 KV) | 262,144 | **FIT_LIMIT** | rigorous arithmetic lower bound: weights 8,023.7 MiB + f16 KV 8,192.0 MiB = 16,215.7 MiB > 12,227 MiB total VRAM, before any compute/recurrent/reserve cost |
| Native alternate (BF16 + q4_0 KV; one pre-authorized attempt) | 262,144 | **FIT_LIMIT** | measured admission failure: weights + 2,304.0 MiB q4_0 KV allocated, then the 1,330.28 MiB compute-buffer reservation failed with `cudaMalloc` out-of-memory; no inference in flight |
| Official extension (YaRN factor 4.0, orig 262,144) | 1,010,000 | **FIT_LIMIT** | exceeds total VRAM at every KV precision representable in the pinned runtime (f16 / q8_0 / q4_0); the YaRN mechanism itself is represented by the runtime (measured `freq_scale = 0.25` probe) |

Completed negative dispositions count per WELP. These are dispositions for
this 12 GB card and pinned stack — not claims about the model on other
hardware. The card's advertised extension maximum is 1,010,000 (the pinned
official card text), not the arithmetic product 262,144 × 4.0.

## Boundary between the practical rungs and the maxima

- **Highest measured/admitted near-full primary context: 65,536 tokens**
  (99.5% occupancy, minimum sampled free 1,292 MiB). This is the highest rung
  actually admitted and measured — it is NOT claimed as the absolute runtime
  maximum.
- **98,304 was intentionally not launched**: the measured-calibrated fit
  projection placed free VRAM below the frozen 1,024 MiB operational safety
  floor (a designed fit-stop, no OOM). The exact physical safe ceiling
  between 65,536 and 98,304 was not bracketed; the campaign did not attempt
  to locate it.

## Near-full useful-context rechecks (32K and 64K)

- **4 near-full useful-context requests** (2 rungs {32,768; 65,536} ×
  2 seeds {42; 314159}); **20 target-field-depth observations** at
  2/25/50/75/95% depths; occupancy 99.44–99.51% of the usable budget;
  placement error ≤ 0.092 pp.
- Planted-target retrieval is **perfect: 20/20 values exact**, decoy
  resisted 4/4.
- The **strict useful-context gate is FAILED, 0/4**: the auxiliary
  synthesis / absent-information / checksum output requirements were dropped
  in all four requests (12 of 12 auxiliary-field observations),
  deterministically. Retrieval and instruction compliance diverge at extreme
  occupancy — an instruction-retention defect, not a retrieval failure.
  Practical guardrail: do not place binding output instructions at extreme
  prompt occupancy.

## Attempt accounting

5 server launches · 6 completed inference requests (4 near-full + 2 smokes) ·
1 admission-only attempt (no inference) · 1 allocation-phase OOM (the
pre-authorized native-maximum attempt) · 0 CUDA errors during inference ·
0 Xid events · 0 invalidated requests · 0 silent retries.

## Practical profile (revalidated, unchanged)

**32,768 default** (near-full TTFT 6.6–6.7 s, decode ~60.3 tok/s) /
**65,536 guarded** (near-full TTFT 15.2 s, decode ~54.1–54.4 tok/s).
Reliability inherited from the baseline (profile unchanged, no rerun).
**MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES** (completed negative
dispositions count).

## LocalMaxxing

The existing submission `cmtwcmm3207eqps01w7fubuuw` (68.0 tok/s out, 32K
canonical practical stack) is **VERIFIED_EXISTING** for this campaign: the
canonical practical profile is unchanged, so the existing record matches
exactly. No new benchmark was run and no duplicate submission was made.

## Claim boundary

- Do not summarize this record as "Qwen3.5-4B supports 64K": 65,536 is the
  highest measured/admitted near-full rung on this 12 GB card under the
  frozen safety floor, and the strict useful-context gate failed at that
  occupancy (retrieval remained perfect).
- Do not summarize this record as "262K failed" without attribution: the
  native maximum 262,144 is a completed **FIT_LIMIT** — an arithmetic
  impossibility on the f16 primary surface and a measured compute-buffer
  admission failure on the pre-authorized q4_0-KV alternate surface — not a
  capability judgment on other hardware.
- The official YaRN 1,010,000 extension maximum is **FIT_LIMIT** on this
  card at every representable KV precision; the mechanism is representable
  in the pinned runtime.
- Results are bounded by the tested artifact, runtime, hardware,
  configuration, and protocol snapshot; they are not universal model
  rankings.

Canonical scientific authority: the local WELP campaign `REPORT.md` for
`qwen35-4b-rtx5070-context-completion-2026-09-11`
(`research/engine-kernel/experiments/qwen35-4b-rtx5070-context-completion-2026-09-11/REPORT.md`).
This summary is a public derivative; the campaign report governs on any
conflict.
