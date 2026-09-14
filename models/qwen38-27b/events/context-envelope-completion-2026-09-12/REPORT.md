# Qwen3.8-27B / RTX 5070 — model-card context-envelope completion (public summary)

Campaign: `qwen38-27b-rtx5070-context-completion-2026-09-12` · executed 2026-09-12 ·
Outcome: **PASS — QWEN38_27B_CONTEXT_ENVELOPE_COMPLETED** ·
Classification: **guarded/limited deployment suitability (inherited, unchanged)** ·
Append-only follow-up to the 2026-08-14 historical evaluation and the
2026-09-11 H1 canonical-profile update
([`reports/h1-canonical-profile-update.md`](h1-canonical-profile-update.md)),
published 2026-09-12.

## Why a follow-up

The historical deep evaluation validated useful context only to 8K on its
tested llama.cpp stack, and the H1 profile update promoted the current
canonical serving surface without a full model-card context campaign — its
export recorded `envelope_complete: false` explicitly. This bounded campaign
closes that context debt on the accepted H1 surface. Both earlier records are
preserved unchanged; this report adds context-envelope claims only and does
not rewrite, re-date, or reinterpret them.

## Tested stack (the accepted canonical H1 surface, hash re-verified)

- Model: Qwen/Qwen3.8-27B (post-trained instruct; text-only surface; thinking
  disabled via the chat template). Architecture `qwen3_5`: 64 layers =
  16 × (3× GatedDeltaNet → FFN → 1× Gated Attention → FFN) plus an
  in-checkpoint MTP head; vocabulary 248,320.
- Artifact: `Qwen3.8-27B-SC_2.20bpw_H3_V3` (EXL3, 2.20 bpw, head_bits 3,
  mtp_bits 2; q4 target KV, q4 draft KV). Constituent safetensors freshly
  SHA-256 verified at campaign start; no redownload.
- Runtime: ExLlamaV3 1.4.6+cu128.torch2.10.0 (torch 2.10.0+cu128, CUDA 12.8,
  Python 3.12.13). Canonical H1 profile: MTP width 1, batch 1, max_chunk 256,
  recurrent history H1, CPU embedding lookup, all 64 transformer blocks
  GPU-resident. Only the serving context varies per arm.
- Hardware: WumboJetsII — NVIDIA GeForce RTX 5070 12 GB (12,227 MiB),
  Ryzen 7 9800X3D, Fedora Linux 44.

## Official context claims (pinned and reconciled)

- **Native maximum: 262,144 tokens** — official model card, live official
  card, and the artifact's own `max_position_embeddings` all agree.
- **Official extension: YaRN, factor 4.0** (`original_max_position_embeddings`
  262,144), advertised exact maximum **1,000,000 tokens**. No second official
  extension mechanism is advertised; the Qwen3.5 family's 1,010,000 value is
  distinct and was not transferred.

## Method in brief

Current-WELP context-scaling: every admitted rung is executed at true
near-full occupancy (≥99.4% of the usable prompt budget, two seeds each)
with a strict useful-context fixture placing five authoritative values at
2/25/50/75/95% depths plus synthesis, a decoy, an absent field, and a
checksum. Rungs that cannot safely admit are disposed by a fit model frozen
from measured anchors **before** any high-context execution. Capacity
admission alone is never treated as context validation.

## Measured rungs — both VALIDATED

| Rung | Occupancy (seeds 42 / 314159) | Near-full perf (prefill / decode proxies) | Strict useful-context | Disposition |
|---|---|---|---|---|
| 65,536 (anchor; 64,703 / 64,699 rendered of 65,024 budget) | 99.506% / 99.500% | ~606 tok/s / 61–62 tok/s; TTFT ~107 s | **2/2 strict; all seven gates 4/4** | **VALIDATED** |
| 98,304 (highest admitted; 97,293 / 97,318 rendered of 97,792 budget) | 99.490% / 99.515% | ~537 tok/s / 56–57 tok/s; TTFT ~181 s | **2/2 strict; all seven gates 4/4** | **VALIDATED** |

All 20 target-field observations across both rungs landed within ±0.036
percentage points of their planned depths. The model did not substitute the
decoy, did not hallucinate the absent field, and returned complete JSON
objects with natural stop at both rungs. The frozen fit model proved
conservative at both measured points (predicted minimum free VRAM 1,848 vs
measured 1,924–1,928 MiB at 65,536; 1,304 vs 1,332–1,336 MiB at 98,304) and
no prediction was rewritten. Zero OOM, zero CUDA errors, zero Xid events;
peak sampled power 232.7 W, peak temperature 71 °C.

## Exact maxima — completed dispositions

- **Native 262,144 = FIT_LIMIT on this surface.** The accepted H1
  artifact/cache/MTP profile requires 12,530 MiB at ready for a 262,144-token
  cache (8,178 MiB context-independent + 262,144 × 17,408 B/token KV),
  exceeding both idle-available (11,814 MiB) and total card (12,227 MiB)
  VRAM. This is a hard lower-bound accounting under the frozen profile — it
  does **not** mean Qwen3.8-27B cannot run 262K; it means the accepted H1
  profile cannot fit 262K on this 12 GB GPU while retaining its required
  topology. **Nearest measured boundary: 98,304 VALIDATED.** Intermediate
  rungs 131,072 and 196,608: FIT_LIMIT by the same frozen accounting (no
  launch was attempted solely to induce an OOM).
- **Official YaRN 1,000,000 = INTEGRATION_BLOCKED on the accepted surface.**
  ExLlamaV3 1.4.6 contains a complete HF-semantics YaRN implementation and
  its config path reads the model's `rope_parameters`, but activation
  requires `rope_type: "yarn"` inside the artifact's own `config.json` (the
  card-documented method), and the runtime exposes no supported override for
  that path on this pinned artifact. Editing protected model state or
  mutating configuration in memory would be an unofficial, unverifiable
  alternate surface, so no probe was executed. This limitation is specific to
  the accepted artifact + H1 profile + runtime 1.4.6 configuration surface —
  it is not a claim that "YaRN is unsupported" by the runtime or the model
  family, and a future authorized runtime/artifact change could re-open it.
- **Independently, YaRN 1,000,000 is also FIT_LIMIT on this card:** the KV
  cache alone would need ~16.6 GiB (≈1.36× total card VRAM), and the full
  ready-state requirement ≈24,783 MiB ≈ 3.03× the card. Established by
  arithmetic from the same frozen model; the GPU was never crashed to show it.

Both maxima therefore carry completed, evidence-backed dispositions.

## Practical profile — unchanged

- **Default stays 65,536.** 98,304 is real and validated but guarded:
  near-full TTFT roughly doubles (107 s → 181 s), full-occupancy decode drops
  ~8%, and the minimum free-VRAM margin shrinks to ~300 MiB on sampled
  evidence.
- **Guarded boundary: 98,304** — the highest measured/admitted context on
  this surface.
- Inherited classification (guarded/limited deployment suitability) and all
  inherited reliability evidence carry unchanged because the practical
  default did not change.

## LocalMaxxing

**SUBMITTED / VERIFIED_EXISTING** — submission `cmtwcncwr07f4ps01ef75q6ne`
(75.4 tok/s out, 71.35 ms TTFT, 266 actual prompt tokens) on the identical
canonical H1 profile. The practical profile did not change, so no new
benchmark or submission was made and the service was not contacted in this
campaign; the retained record was audited for duplication only.

## Limitations

- Prefill/decode figures are client streaming proxies, not kernel timings.
- Minimum-free figures are 0.5 s samples; true instantaneous extrema are not
  established (the 98,304 floor margin of ~300 MiB rests on sampled
  evidence).
- Useful-context evidence covers the tested fixture style and depths at the
  two measured rungs; it is not a claim about every long-context task or
  untested rungs.
- The YaRN disposition is specific to the pinned artifact/runtime/profile
  combination described above.
- MTP acceptance behavior at near-full occupancy was not measured.

## Envelope status

**MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES.** Every exact official maximum
(native 262,144; extension YaRN 1,000,000) and every proportional native
rung now carries a completed disposition (VALIDATED, FIT_LIMIT, or
INTEGRATION_BLOCKED). No PARTIAL or NOT_TESTED row remains on the accepted
surface.

Results are bounded by the tested artifact, runtime, hardware, configuration,
and protocol snapshot; they are not universal model rankings.
