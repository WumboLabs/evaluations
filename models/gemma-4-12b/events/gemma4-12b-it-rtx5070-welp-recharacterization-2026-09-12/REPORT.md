# Gemma 4 12B IT / RTX 5070 12GB — current-WELP recharacterization (public scientific summary)

Campaign: `gemma4-12b-it-rtx5070-welp-recharacterization-2026-09-12` ·
executed 2026-09-12/13 · published 2026-09-13 ·
Outcome: **PASS** · Classification: **READY_WITH_GUARDRAILS** ·
Append-only follow-up to the historical practical-use record
([`events/gemma4-12b-practical-use-family-2026-06-21.md`](../events/gemma4-12b-practical-use-family-2026-06-21.md)),
which remains unchanged as the historical account of the 2026-06-21
campaign. This report is a public-safe derivative of the authoritative
local campaign bundle; where any derivative differs, the local campaign
evidence governs.

## 1. Why a recharacterization

The 2026-06-21 practical-use event (259.2/300 manual score) established
the QAT UD-Q4_K_XL packaging as the strongest 12B Gemma variant in
WumboLabs practical testing, but carried no WELP classification,
capability review, reliability characterization, or context-envelope
coverage. The 2026-09-12 evidence census recorded that gap as high
priority. The exact historical artifact had been lost to the archive
lifecycle (absent from both the local tree and the WumboServer archive);
the 2026-09-12/13 closeout authorized re-acquisition, repairing the gap.

## 2. Exact identity

- Model: **Gemma 4 12B IT** (Google). Upstream:
  `google/gemma-4-12B-it`; QAT lineage
  `google/gemma-4-12B-it-qat-q4_0-unquantized`; official GGUF
  `google/gemma-4-12b-it-qat-q4_0-gguf`.
- Architecture: `gemma4` "Unified" (encoder-free), hybrid attention with
  1,024-token local sliding-window layers plus global layers, unified KV
  for global layers, p-RoPE; ~11.91B parameters; 262,144-token training
  capacity. License: Apache 2.0.
- Tested artifact: `unsloth/gemma-4-12b-it-GGUF` →
  `gemma-4-12b-it-UD-Q4_K_XL.gguf` (Unsloth Dynamic 2.0 packaging of the
  QAT Q4_0 lineage), SHA-256
  `90fd944d227e9d9b68e7e2c7d5b57b79d4c66ed521b0919fbbd932cf834f6f8e`,
  7,366,423,360 bytes, source revision
  `fc034cfff751157913579611efad8462ac1be606`.
- Runtime: llama.cpp b9672, commit `74ade5274`, CUDA SM120 build,
  server surface, full GPU residency (`-ngl 999`), KV f16, FA auto,
  single slot.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12GB.

## 3. Profile selection

The historical winner was re-validated under current measurement rather
than promoted by inheritance: the artifact passed admission (coherent
output, template working, thinking toggle honored), reproduced its
historical decode speed at parity (72.92 vs 73.45 tok/s at comparable
settings), passed the full quality screen, and fits the 12 GB card with
large reserve at the practical default. It is therefore the current
canonical practical profile. The official Google stock Q4_0 GGUF was not
separately acquired: the admitted artifact passed all gates at
historical parity, so a second ~7 GB artifact adds no defensible
scientific value for practical profile selection on this hardware.

Serving shape: `-c 32768 -ngl 999 -np 1 --jinja` with
`enable_thinking=false` as the practical default (the thinking lane was
validated separately once). Practical default context 32,768
(~8.4 GiB); guarded context 131,072 (~10.0 GiB).

## 4. Measured results

| Surface | Result |
|---|---|
| Quality (frozen 12-task mechanical screen, temp 0) | **12/12 PASS** |
| Reasoning (thinking ON, multi-hop syllogism) | PASS |
| Coding (executable check) | PASS |
| Tool calling + grounded continuation | PASS |
| Decode (tg128, 5 reps) | 72.92 ± 0.04 tok/s |
| Prefill (pp512, 5 reps) | 3,201 ± 39 tok/s |
| Short-prompt TTFT (server, ~65 tok) | ~47 ms |
| Reliability (20-task mechanical corpus, temp 0.7) | seed 42: 11/20 · seed 314159: 10/20 |

Reliability guardrails: 13–14 of 20 outputs hit the frozen per-task
token caps (the model is markedly verbose at small budgets; truncation
contributed to several category failures); git-safety advisory weakness
(framing amendment of pushed commits as "technically possible" without
coordinating); uncertainty and sycophancy categories 1–2/3. Evidence
discipline (3/3, 2/3) and strict interfaces (3/3, 2/3) were strong;
hallucination traps 2/4 on both seeds.

## 5. Context envelope (COMPLETE for the text profile)

Near-full methodology: usable budget = configured − 640 (512 generation
reserve + 128 safety allowance); uncached prefill; occupancy target
≥99% (hard floor 97%); final rendered/tokenized prompt as authority.

| Rung (tokens) | Occupancy | Prefill tok/s | Decode tok/s | Disposition |
|---|---|---|---|---|
| 8,192 | 99.03% | 2,853–2,857 | 68.0–68.1 | VALIDATED |
| 16,384 | 99.38% | 2,739–2,740 | 67.0–67.2 | VALIDATED |
| 32,768 | 99.54% | 2,422–2,423 | 64.9–65.0 | VALIDATED |
| 65,536 | 99.62% | 1,943 | 61.6–61.7 | VALIDATED |
| 131,072 | 99.66% | 1,397–1,398 | 56.0–56.1 | VALIDATED |
| 262,144 (exact card maximum) | — | — | — | **FIT_LIMIT** |

Useful-context at 131,072 (highest runnable native rung): all five
frozen gates — exact retrieval, multi-fact synthesis, decoy rejection,
absent-information discipline, instruction retention — PASS at both
seeds at 99.5% near-full occupancy; target-field depths converged to
within 0.053 percentage points against the final rendered token stream.

The 262,144 disposition: one bounded exact-capacity admission attempt
failed with a CUDA out-of-memory during compute-buffer allocation, and
the measured KV growth slope (≈17.4 KiB/token) independently shows the
point cannot fit with the required reserve on a 12 GB card. Nearest
measured fit boundary: 131,072. FIT_LIMIT is a hardware-scoped completed
limiting disposition, not a model-quality verdict; larger-memory hosts
may still validate the native maximum.

Official extensions: NONE — neither official model card documents an
extension mechanism.

## 6. Multimodal scope boundary

The exact model is officially multimodal (text/image/audio/video input
via an mmproj projector). This campaign characterized the canonical
TEXT profile only; the projector was not part of the authorized
acquisition. Disposition: **SUPPORTED_NOT_CHARACTERIZED**. No model-wide
multimodal characterization is claimed by this event; text-only results
above must not be read as full multimodal model characterization.

## 7. LocalMaxxing

MEASURED_NOT_SUBMITTED: a fresh canonical-profile local benchmark ran
(pp512 3,201 tok/s; tg128 72.92 tok/s; 5 reps; artifact SHA-256 above;
llama.cpp b9672). No exact existing service record for this profile
exists (the 2026-07-04 LMX record for this artifact family is an
unexecuted planned dry-run), and live submission is human-gated — no
submission occurred and no verification fields were fabricated.

## 8. Classification and deployment guidance

**READY_WITH_GUARDRAILS.**

- Recommended roles: general technical assistant, summarization,
  retrieval/RAG over ≤128K documents, coding assistance, tool-using
  text agent.
- Poor fit / guardrails: latency- or budget-critical terse endpoints
  without output-budget tuning (verbosity); Git-destructive-operation
  advisories without review; anything requiring vision/audio
  (uncharacterized); >131,072-token contexts on 12 GB hardware.
- Historical comparison: the 2026-06-21 practical-use winner is
  directionally confirmed under current measurement (speed parity,
  clean quality screen); the old protocol could not see the reliability
  truncation behavior, the git-safety weakness, or the context-envelope
  boundaries documented here. No protocol score equivalence is claimed.

## 9. Claim boundary

All results are bounded by the tested artifact, runtime build, hardware,
context rungs, and settings listed above; they are not universal model
rankings. The authoritative scientific record is the local campaign
bundle; this document is its public-safe derivative.
