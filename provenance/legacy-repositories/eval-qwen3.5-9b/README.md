# WumboLabs evaluation records — Qwen3.5-9B

Canonical public evidence record for the WumboLabs WELP characterization of
**Qwen3.5-9B** on the WumboJetsII workstation (NVIDIA GeForce RTX 5070 12GB).

- **Campaign:** `qwen35-9b-rtx5070-baseline-2026-09-09` (executed 2026-09-09/10)
- **Outcome:** PASS — QWEN35_9B_RTX5070_BASELINE_CHARACTERIZED
- **Classification:** READY_WITH_GUARDRAILS
- **Tested artifact:** Qwen3.5-9B-Q8_0.gguf (text-only conversion; Unsloth revision 3885219b6810b007914f3a7950a8d1b469d598a5) — Q8_0 weights (acquired), F16 KV cache, F32 recurrent state (SHA-256 `809626574d0cb43d4becfa56169980da2bb448f2299270f7be443cb89d0a6ae4`)
- **Runtime:** llama.cpp — 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (CUDA 13.3, SM120)
- **LocalMaxxing:** SUBMITTED `cmtwcn79807eups01faxxmyr1` — 67.3 tok/s out

## Contents

| File | Content |
|---|---|
| [`EVIDENCE-SUMMARY.md`](EVIDENCE-SUMMARY.md) | bounded public scientific summary (positive and negative findings) |
| [`reports/qwen35-9b-context-envelope-completion-2026-09-11.md`](reports/qwen35-9b-context-envelope-completion-2026-09-11.md) | dated append-only follow-up: full model-card context envelope completion (2026-09-11) |
| [`website-publication.json`](website-publication.json) | machine-readable derivative consumed by the WumboLabs website publication registry (schema `wumbolabs-labs-publication/1`) |
| [`MODEL.md`](MODEL.md) / [`model-manifest.json`](model-manifest.json) | model/artifact identity and provenance (no model binaries are stored here) |
| [`PUBLICATION-POLICY.md`](PUBLICATION-POLICY.md) + publication metadata | first-release boundaries: allowlist-first, default DO_NOT_PUBLISH |

## Evidence identity

- Authoritative local report: `research/engine-kernel/experiments/qwen35-9b-rtx5070-baseline-2026-09-09/REPORT.md` (sha256 `62761e8ad82bd8092caaee43e3122fba163d19d7b01137c8f28df284b8a4221b`)
- LocalMaxxing: SUBMITTED `cmtwcn79807eups01faxxmyr1` — 67.3 tok/s out; evidence retained in the local campaign bundle.

## Canonical evidence

This repository is the canonical public evidence for the campaign above. The
WumboLabs website hosts a derived Lab Record for it at
<https://wumbolabs.dev/labs/qwen35-9b/>; the website is a
derivative, never a second source of model facts. On any conflict, the local
WELP campaign `REPORT.md` governs.

## Claim boundary

Medium-fit Q8_0 quantized control (BF16 cannot fit), READY_WITH_GUARDRAILS: 32K default / 64K guarded, 66.7 tok/s short decode, 7/7 constrained quality and 20/20 reliability. The full revised context envelope remains deferred and quality superiority over 4B is unproven; this is not a high-precision BF16 result.

## Follow-up (2026-09-11): context envelope completion — append-only

Campaign `qwen35-9b-rtx5070-context-completion-2026-09-11` (executed and
published 2026-09-11) completed the full model-card context envelope:
**PASS — QWEN35_9B_CONTEXT_ENVELOPE_COMPLETED**; MODEL-CARD CONTEXT ENVELOPE
COMPLETE = YES. Full report:
[`reports/qwen35-9b-context-envelope-completion-2026-09-11.md`](reports/qwen35-9b-context-envelope-completion-2026-09-11.md).

This follow-up supersedes the baseline context claims above (including the
"envelope deferred" statement in the baseline claim boundary) **for context
claims only**; all other baseline results remain inherited unchanged.

- Native maximum **262,144 = FIT_LIMIT** (Q8_0/f16 primary: arithmetic lower
  bound; pre-authorized q4_0-KV alternate: measured compute-buffer admission
  failure).
- Official extension **YaRN 1,010,000 = FIT_LIMIT** at every representable KV
  precision; mechanism representation confirmed in the pinned runtime.
- **Highest measured/admitted near-full primary context: 65,536** — not
  claimed as the absolute runtime maximum. 98,304 was intentionally not
  launched (measured-calibrated projection below the frozen 1,024 MiB
  operational safety floor); the exact physical ceiling between the two
  values was not bracketed.
- 32K/64K near-full rechecks: planted-target retrieval perfect (20/20 values,
  4 requests, 20 observations), synthesis and checksum instructions retained
  4/4; strict useful-context gate **FAILED 0/4** — the absent-information
  value (correct) is returned under the wrong key name (`zeta` instead of
  `absent`), deterministically at both rungs and both seeds — a completed
  measured negative and a new occupancy guardrail.

Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings.

## License / attribution

The evaluated model weights remain under their upstream license
(Apache-2.0); no weights are redistributed
here. The evaluation evidence in this repository is WumboLabs work product.
