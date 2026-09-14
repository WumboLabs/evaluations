# WumboLabs evaluation records — MiniCPM5-2B

Canonical public evidence record for the WumboLabs WELP characterization of
**MiniCPM5-2B** on the WumboJetsII workstation (NVIDIA GeForce RTX 5070 12GB).

- **Campaign:** `minicpm5-2b-rtx5070-welp-characterization-2026-09-10` (campaign 2026-09-10)
- **Outcome:** PASS — MINICPM5_2B_RTX5070_CHARACTERIZED; MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES
- **Classification:** READY_WITH_GUARDRAILS
- **Tested artifact:** model-00000-of-00001.safetensors (official BF16; no quantization or conversion) — BF16 weights and BF16 KV (primary surface); fp8(e4m3) KV only on the single authorized 131,072 alternate surface (SHA-256 `14fb8e7f0a18d53d1f239773758bf581cee7e456a4523a54622c3a245b64402c`)
- **Runtime:** vLLM — 0.27.1 (g6e448d0ea), Torch 2.13.0+cu130, Transformers 5.15.0, FlashInfer 0.6.16.post3
- **LocalMaxxing:** SUBMITTED `cmtwcna5907f0ps01sfiwd60a` — 118.2 tok/s out

## Contents

| File | Content |
|---|---|
| [`EVIDENCE-SUMMARY.md`](EVIDENCE-SUMMARY.md) | bounded public scientific summary (positive and negative findings) |
| [`website-publication.json`](website-publication.json) | machine-readable derivative consumed by the WumboLabs website publication registry (schema `wumbolabs-labs-publication/1`) |
| [`MODEL.md`](MODEL.md) / [`model-manifest.json`](model-manifest.json) | model/artifact identity and provenance (no model binaries are stored here) |
| [`PUBLICATION-POLICY.md`](PUBLICATION-POLICY.md) + publication metadata | first-release boundaries: allowlist-first, default DO_NOT_PUBLISH |

## Evidence identity

- Authoritative local report: `research/engine-kernel/experiments/minicpm5-2b-rtx5070-welp-characterization-2026-09-10/REPORT.md` (sha256 `ad93c194e6b6d5a01605a921883f4b6f125db36138d8b5696a6c051b6440b799`) (current primary; quarantined prior attempt not used)
- LocalMaxxing: SUBMITTED `cmtwcna5907f0ps01sfiwd60a` — 118.2 tok/s out; evidence retained in the local campaign bundle.

## Canonical evidence

This repository is the canonical public evidence for the campaign above. The
WumboLabs website hosts a derived Lab Record for it at
<https://wumbolabs.dev/labs/minicpm5-2b/>; the website is a
derivative, never a second source of model facts. On any conflict, the local
WELP campaign `REPORT.md` governs.

## Claim boundary

Official BF16 full-precision characterization on a contained vLLM runtime, READY_WITH_GUARDRAILS: 32K default / 64K guarded, complete 131K model-card envelope (98K highest BF16-KV rung; exact 131K FIT_LIMIT on BF16-KV and strict-gate FAILED on the authorized fp8-KV surface), 118.6 tok/s decode, thinking/coding/tools PASS, 20/20 reliability.

Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings.

## License / attribution

The evaluated model weights remain under their upstream license
(Apache-2.0); no weights are redistributed
here. The evaluation evidence in this repository is WumboLabs work product.
