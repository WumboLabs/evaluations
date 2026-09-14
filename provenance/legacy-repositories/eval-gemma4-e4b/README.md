# WumboLabs evaluation records — Gemma 4 E4B

Canonical public evidence record for the WumboLabs WELP characterization of
**Gemma 4 E4B** on the WumboJetsII workstation (NVIDIA GeForce RTX 5070 12GB).

- **Campaign:** `gemma4-e4b-rtx5070-welp-characterization-2026-09-10` (campaign 2026-09-10 (+ 2026-09-11 bounded evidence-completion pass))
- **Outcome:** PASS — GEMMA4_E4B_EVIDENCE_COMPLETION_COMPLETE
- **Classification:** READY_WITH_GUARDRAILS
- **Tested artifact:** gemma-4-E4B_q4_0-it.gguf + official gemma-4-E4B-it-mmproj.gguf (Google official QAT release) — QAT Q4_0 weights, F16 KV cache (SHA-256 `676c3507 (weights; matches pinned upstream LFS) / 7498a37c (mmproj; matches pinned upstream LFS)`)
- **Runtime:** llama.cpp — 0.1.0-dev build b10449, commit 0d9ceae1e38291035605613ab41a8f5e693d6fcd (campaign-local CUDA 13.3 build, SM120)
- **LocalMaxxing:** SUBMITTED `cmtwgcs7c097sps01sdq9ihbu` — 152.7 tok/s out

## Contents

| File | Content |
|---|---|
| [`EVIDENCE-SUMMARY.md`](EVIDENCE-SUMMARY.md) | bounded public scientific summary (positive and negative findings) |
| [`website-publication.json`](website-publication.json) | machine-readable derivative consumed by the WumboLabs website publication registry (schema `wumbolabs-labs-publication/1`) |
| [`MODEL.md`](MODEL.md) / [`model-manifest.json`](model-manifest.json) | model/artifact identity and provenance (no model binaries are stored here) |
| [`PUBLICATION-POLICY.md`](PUBLICATION-POLICY.md) + publication metadata | first-release boundaries: allowlist-first, default DO_NOT_PUBLISH |

## Evidence identity

- Authoritative local report: `research/engine-kernel/experiments/gemma4-e4b-rtx5070-welp-characterization-2026-09-10/REPORT.md` (sha256 `8d8bd9c7975711f35406e19c8403625230e276eafe9b035b153f12056e352991`) (reconciled final package incl. §54–59 completion/reconciliation)
- LocalMaxxing: SUBMITTED `cmtwgcs7c097sps01sdq9ihbu` — 152.7 tok/s out; evidence retained in the local campaign bundle.

## Canonical evidence

This repository is the canonical public evidence for the campaign above. The
WumboLabs website hosts a derived Lab Record for it at
<https://wumbolabs.dev/labs/gemma4-e4b/>; the website is a
derivative, never a second source of model facts. On any conflict, the local
WELP campaign `REPORT.md` governs.

## Claim boundary

Official Google QAT Q4_0 + mmproj on llama.cpp, READY_WITH_GUARDRAILS: 32K default / 131K guarded with the full card envelope complete; perfect five-needle retrieval through the exact 131,072 maximum while the strict aggregate gate FAILED at every rung. Vision, multi-image, ASR, AST and bounded video PASS; OCR TESTED_LIMITED; reliability 20/20 completion, 14/20 exactness.

Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings.

## License / attribution

The evaluated model weights remain under their upstream license
(Apache-2.0 (Gemma license terms apply)); no weights are redistributed
here. The evaluation evidence in this repository is WumboLabs work product.
