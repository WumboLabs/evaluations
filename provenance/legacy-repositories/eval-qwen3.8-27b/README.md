# Qwen3.8-27B Evaluation Workspace

> **⚠️ HISTORICAL ARCHIVE — superseded by profile-specific canonical repositories.**
> This repository preserves historical publication history and remains fully
> accessible; its Git history is frozen and was not rewritten. Canonical
> profile-specific evidence now lives at:
> - **Historical llama.cpp profile** (`qwen38-27b-llamacpp-ud-q2-k-xl`): [WumboLabs/eval-qwen3.8-27b-llamacpp](https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp)
> - **Current ExLlamaV3 H1 profile** (`qwen38-27b-exl3-h1`, includes the H1 promotion and the 2026-09-12 context-envelope completion): [WumboLabs/eval-qwen3.8-27b-exl3-h1](https://github.com/WumboLabs/eval-qwen3.8-27b-exl3-h1)
> Migration notice added 2026-09-12 (WumboLabs model/profile/event publication-identity milestone). All evidence below is unchanged.
> **Status:** **COMPLETED_DEEP_EVALUATION** · Protocol: WELP end-to-end (frozen snapshot `wlep-next-snapshot-2026-08-25-end-to-end`) · Hardware: WumboJetsII (RTX 5070 12 GB SM120)

## At-a-glance
- **Model:** Qwen 3.8 27B — AD IQ2_XS + DFlash2 Q4_K_M (also tested Q4_K_M, UD-IQ2_M/XXS, Q6_K)
- **Evaluation date:** 2026-08-14 · **Host:** WumboJetsII
- **Verdict:** **Guarded/limited deployment suitability.** Strong reviewed local coding/technical-assistant evidence under the tested configuration; not recommended as an unguarded daily driver or unattended autonomous agent.
- **Best bounded coding config:** Q4_K_M, 38 GPU layers, 8K, reasoning off — 4.85–5.0/5 at 6.4–6.8 tok/s, 467 MiB min VRAM headroom.
- **Fast short work:** UD-IQ2_M, full GPU, 4K — ~42 tok/s (362/5 manual avg); task-dependent quality.
- **Performance (quality/balance):** 6.4–6.8 generation tok/s · ~880 tok/s prefill.
- **LocalMaxxing:** APPROVED speed-test submissions (`cmt3jngze0njfmv0133xpneeu` BALANCED 16K; `cmt3jp2cn0njpmv01t5u8m6wd` FAST 8K MTP) + benchmark suite **APPROVED/PUBLIC**; ref-quant `cmsv68xl3085ims01w8aeacig`. (See `evaluations/localmaxxing/report.md`.)
- **Important limitations:** no LLMGauge Agent Harness result; OMP evidence is a bounded one-file pass (not broad autonomy); useful context not established beyond 8K for the fast quants; vLLM unsafe above.
- **Evidence:** public reports under [`reports/`](reports/), model/revision identities in [`model-manifest.json`](model-manifest.json), checksums and inventories under [`manifests/`](manifests/), and first-release boundaries in [`PUBLICATION-POLICY.md`](PUBLICATION-POLICY.md).

> Manual scores are bounded review metadata, not universal quality rankings. Structural validation does not establish answer quality.

---

## Host hardware
- AMD Ryzen 7 9800X3D, 8 cores / 16 threads.
- 32,695,726,080 bytes physical RAM; about 30 GiB usable during evaluation.
- 8 GiB zram swap.
- NVIDIA GeForce RTX 5070 with 12,227 MiB VRAM, compute capability 12.0 (SM120), driver 610.57.04.
- Fedora Linux 44, kernel 7.1.8-200.fc44.x86_64.

## Best measured configurations
| Use | Configuration | Measured result | Boundary |
|---|---|---|---|
| Quality/balance | **Q4_K_M**, 38 GPU layers, 8K context, reasoning off | Four focused coding/tool-output prompts scored 4.85–5.0/5 at 6.4–6.8 generation tok/s | Hybrid and VRAM-tight; minimum measured headroom was 467 MiB |
| Speed | **UD-IQ2_M**, full GPU, 4K context, reasoning off | 42.0–42.9 generation tok/s; 362/5 manual average over six practical prompts | Task-dependent quality; the separate 8K LLMGauge run failed all six prompts during context initialization |
| Agent-safe tested placement | **UD-IQ2_XXS**, full GPU, 12,288-token server context, reasoning off | Resource-safe in two OMP runs; the smaller follow-up completed inspect, edit, test, and report autonomously | The first larger task compacted at the context boundary; the complete follow-up was deliberately limited to one file and three tests |

## Known limitations
- **Runtime safety boundary:** the evaluated vLLM configuration exhausted host memory during an earlier admission attempt. The complete evaluation treats this as an operational deployment boundary, not a model-quality result.
- **Autonomy evidence is bounded:** the OMP follow-up completed a deliberately limited one-file inspect/edit/test/report loop. It does not establish broad autonomous-agent suitability.
- **No LLMGauge Agent Harness result exists.** This is a coverage limit, not a replacement classification.
- Earlier admission-state drafts remain historical evidence. The current classification is **COMPLETED_DEEP_EVALUATION** with the guarded conclusion above.
- Restricted working material, including raw logs, runtime trees, local model references, OMP internals, and source acquisitions, is excluded from the initial public release.

## First-release evidence surface
- [`reports/`](reports/) — reviewed reports and cross-configuration summaries.
- [`evidence/inventory/`](evidence/inventory/) — reproducibility inventories, hashes, and text comparisons only.
- [`manifests/`](manifests/) — inventory and checksum records.
- [`notes/continuation-notes.md`](notes/continuation-notes.md) — bounded completed-work and follow-up notes.
- LocalMaxxing public submission/result identifiers are listed in the at-a-glance section.

> The release contains reproducibility metadata, not model artifacts, raw telemetry, runtime trees, credential material, or acquisition sources.

---

## Current canonical profile (H1) — 2026-09 follow-up update

The historical evaluation above remains valid for its tested stack
(Unsloth UD-Q2_K_XL GGUF on llama.cpp b10449, campaign 2026-08-14..21) and is
**not** rewritten or reinterpreted by this section. The canonical serving
stack has since evolved substantially; it is documented as a dated,
append-only follow-up:

- **Follow-up report:** [`reports/h1-canonical-profile-update.md`](reports/h1-canonical-profile-update.md)
- **Machine-readable record:** [`website-publication.json`](website-publication.json)
  (schema `wumbolabs-labs-publication/1`; disposition `WEBSITE_READY`,
  canonical evidence `PUBLISHED` at this repository)
- **Current profile (summary):** ExLlamaV3 1.4.6+cu128.torch2.10.0;
  `Qwen3.8-27B-SC_2.20bpw_H3_V3` (EXL3, 2.20 bpw; q4 target/draft KV);
  context 65,536; MTP width 1; batch 1; recurrent history **H1** (explicit H4
  fallback retained); CPU embedding lookup (not transformer-layer offload);
  all 64 transformer blocks GPU-resident.
- **Promotion evidence:** E18H candidate validation (PASS) then E18I canonical
  promotion (PASS — `E18I_H1_CANONICAL_PROMOTION_COMPLETE`); E18E corrected
  oracle 3/3 requests / 15/15 target fields; seven-check quality 7/7; 20/20
  exactly-flat stability sequence.
- **Scope boundary:** H1 is canonical only for this exact artifact/runtime and
  text-only width1/batch1 surface; no width>1, batch>1, multimodal,
  tensor-parallel, other artifact/runtime release, or recurrent-geometry
  validation is implied. Historical model-role findings above belong to the
  historical tested stack and are not superseded.

---

## Model-card context-envelope completion — 2026-09-12 follow-up update (append-only)

The historical evaluation and the H1 profile update above remain valid for
their tested stacks and are **not** rewritten or reinterpreted by this
section. The full model-card context envelope has since been completed on the
accepted H1 surface; it is documented as a dated, append-only follow-up:

- **Follow-up report:**
  [`reports/qwen38-27b-context-envelope-completion-2026-09-12.md`](reports/qwen38-27b-context-envelope-completion-2026-09-12.md)
- **Machine-readable record:** [`website-publication.json`](website-publication.json)
  (schema `wumbolabs-labs-publication/1`; disposition `WEBSITE_READY`,
  canonical evidence `PUBLISHED` at this repository; this file now represents
  the context-envelope completion generation)
- **Campaign:** `qwen38-27b-rtx5070-context-completion-2026-09-12` —
  **PASS — QWEN38_27B_CONTEXT_ENVELOPE_COMPLETED**;
  **MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES**.
- **Measured rungs (2 seeds each, ≥99.49% near-full occupancy, strict
  useful-context 2/2 per rung, all seven gates passing):** 65,536 anchor
  VALIDATED; **98,304 VALIDATED** — the highest measured/admitted context and
  the guarded boundary on this surface.
- **Native maximum 262,144 = FIT_LIMIT on the accepted H1 / RTX 5070
  surface** (12,530 MiB required at ready vs 12,227 MiB total card VRAM;
  nearest measured boundary 98,304). This is a property of the accepted
  artifact/cache/MTP profile on this 12 GB GPU — not a claim that the model
  cannot run 262K elsewhere.
- **Official extension YaRN 4.0 → 1,000,000 = INTEGRATION_BLOCKED on the
  accepted surface** (the pinned runtime exposes no supported activation for
  the required `rope_parameters` on this artifact), and **independently
  FIT_LIMIT** on this card (cache alone ≈16.6 GiB). Two distinct dispositions;
  neither is a general "YaRN unsupported" claim.
- **Practical default unchanged: 65,536.** Inherited classification,
  reliability evidence, and the LocalMaxxing record
  (`cmtwcncwr07f4ps01ef75q6ne`, VERIFIED_EXISTING — no new submission) carry
  unchanged.
