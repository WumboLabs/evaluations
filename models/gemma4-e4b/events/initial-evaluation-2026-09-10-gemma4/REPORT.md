# Gemma 4 E4B / RTX 5070 — full WELP characterization (public summary)

Campaign: `gemma4-e4b-rtx5070-welp-characterization-2026-09-10` (+ 2026-09-11
bounded evidence-completion pass) · Final decision: **PASS —
GEMMA4_E4B_EVIDENCE_COMPLETION_COMPLETE** ·
Classification: **READY_WITH_GUARDRAILS** · 80 valid scientific requests
across 9 supervised arms; zero OOM/CUDA/Xid.

## Tested stack

- Model: google/gemma-4-E4B-it @ `ee0ef602…` (dense decoder + Per-Layer
  Embeddings; 35 sliding-window + 7 global attention layers with unified
  shared KV; vision and audio encoders).
- Artifact: **official Google QAT Q4_0 GGUF** `gemma-4-E4B_q4_0-it.gguf`
  (`676c3507…`, LFS-matched) + **official mmproj** (`7498a37c…`) from
  google/gemma-4-E4B-it-qat-q4_0-gguf @ `4b4a2c1d…`. Community Q4_K_M pairs
  were rejected (provenance unknown) and retained untouched.
- Runtime: llama.cpp b10449 (`0d9ceae1e…`), campaign-local CUDA 13.3 SM120
  build; all 42 layers + PLE tables + encoders GPU-resident; official
  mmproj for multimodal arms; greedy temperature-0 primary surface.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB, Ryzen 7 9800X3D.

## Headline results (MEASURED)

- Short (66-token prompt): TTFT 22.5 ms median; decode 150.4 tok/s.
- Moderate (2,785-token prompt): TTFT 0.504 s; prefill 7,217 tok/s; decode
  145.7 tok/s.
- **MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES.** Native 131,072 (no
  official E4B extensions exist — source-backed absence). Ladder 8K/16K/32K/
  64K/131,072 at 99.5% occupancy, both seeds per rung; exact maximum:
  TTFT ~38 s, decode ~79 tok/s, ≥6.5 GiB spare (PLE + 5:1 SWA/global +
  unified KV make 131K KV small). Practical default 32,768; exact maximum
  guarded (latency tolerance required).
- **Exact native 131,072 disposition: measured FAILED on the strict
  aggregate useful-context gate** — while five-needle target retrieval was
  **perfect (10/10) across ALL rungs including the exact maximum**, decoy
  resistance 10/10, and near-full performance itself was valid. The
  failure surface is strict output/instruction compliance: `absent`
  (absent-information) filled with a present value at 10/10, and JSON
  tail truncation from 16K upward.
- Multimodal: vision TESTED_PASS; multi-image TESTED_PASS; audio ASR
  TESTED_PASS; audio AST TESTED_PASS; bounded three-frame video
  TESTED_PASS; **OCR/document TESTED_LIMITED** (units/section exact; one
  document-ID digit dropped at temperature 0).
- Constrained quality 3/7 strict (markdown-fenced JSON + the absent-field
  defect); content-level supplement 3/3 needle facts exact.
- Reliability: 20/20 runtime completion, zero errors; behavioral exactness
  14/20 — all six failures are the known dossier strict-format/absent
  defect, bit-stable across arms.
- LocalMaxxing (canonical practical stack, 32K): tokSOut 152.7, TTFT
  59.74 ms, tokSPrefill 1,322.5, 77 actual prompt tokens (endpoint usage),
  submission `cmtwgcs7c097sps01sdq9ihbu` (SUBMITTED once, NEW, APPROVED;
  verifiedRun null — service returned no verification state; recorded
  honestly).

## Negative findings and limitations (retained, not sanitized)

- Do not simplify 131K into "passed": capacity/performance work, retrieval
  is perfect, but the strict aggregate gate FAILED at every rung.
- Strict-format fragility: fenced JSON unless explicitly forbidden;
  absent-information (negative-space) questions unreliable at temperature 0.
- OCR exactness limited at temperature 0; broader OCR/document types,
  variable visual token budgets, broader audio conditions, and the full
  <=60 s @1 fps video envelope remain untested. MTP/speculative deferred
  (distinct serving surface, not authorized in this campaign).
- lmx verifiedRun returned null (client verification-transmission limits).

Canonical scientific authority: the local WELP campaign evidence. This
summary is a public derivative; the campaign's `REPORT.md` governs on any
conflict.
