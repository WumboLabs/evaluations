# Mellum2 12B-A2.5B (Instruct) — current-WELP recharacterization on RTX 5070 12 GB (llama.cpp, Q4_K_M)

- **Event ID:** `mellum2-12b-a2.5b-rtx5070-welp-recharacterization-2026-09-15`
- **Event date / closeout date:** 2026-09-15
- **Model:** Mellum2 12B-A2.5B Instruct (`JetBrains/Mellum2-12B-A2.5B-Instruct`, JetBrains)
- **Profile:** `mellum2-12b-a2.5b-llamacpp-q4km-instruct` (current)
- **Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12 GB
- **Outcome:** **PASS — recharacterized under current WELP**
- **Classification:** **LIMITED_ROLE_ONLY**
- **Scope:** performance, practical viability (quality screen), coding, tool formatting, direct-mode reasoning, replicated reliability, full model-card context envelope with useful-context validation, LocalMaxxing disposition
- **Protocol:** current WELP DRAFT; campaign snapshot `welp-next-snapshot-2026-09-15-mellum2-12b-a25b-recharacterization`

All measurements below are MEASURED on the listed stack unless labeled otherwise. This is the public-safe scientific record of the campaign; the retained local campaign bundle governs on any conflict.

## 1. Tested artifact and official source claims

- Exact artifact: `Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf`, GGUF Q4_K_M, **8,071,293,600 bytes**, SHA-256 **`b04281c27de5d968d577f310d982273b1b13bdbd8117b3ecffffeebfe222f0a7`**.
- Official source (EXTERNAL_REPORTED): `JetBrains/Mellum2-12B-A2.5B-Instruct-GGUF-Q4_K_M` at revision **`1236b4166ed6ab1d57e4be9bcc19f4899c190cbf`**, Apache-2.0, official quantization of `JetBrains/Mellum2-12B-A2.5B-Instruct`. MoE with 64 routed experts and 8 activated per token (~12.15B total, ~2.5B active), 28 layers, GQA 32Q/4KV head_dim 128, hybrid attention (21 sliding-window layers with window 1,024 + 7 full-attention layers), native context **131,072** delivered by train-time YaRN (factor 16 from 8,192) baked into the released checkpoint.
- The historical local artifacts were absent from active storage and the archive with no retained hash; the artifact above was reacquired from the pinned official repository and verified byte-exact against the official LFS SHA-256.
- Multimodal: **NOT_APPLICABLE** (official text-only artifact). Reasoning modes: Instruct is the **no-chain-of-thought checkpoint** — "answers directly, without an externalized chain of thought". The official explicit-CoT surface is the **separate `Mellum2-12B-A2.5B-Thinking` checkpoint**, characterized as its own profile (debt open; not measured here).

## 2. Current serving profile

llama.cpp `b9672` (commit `74ade5274`); CUDA SM120 on RTX 5070; requested full GPU placement `-ngl 99` (verified, no hidden offload); `-c 16384` (default) / `-c 8192` (guarded); `-np 1`; `-fa on`; f16 K/V cache; measurement prompt cache disabled (`--no-cache-prompt --cache-ram 0`, `cached_tokens = 0` verified on every retained request).

The profile identity **reuses** the historical `mellum2-12b-a2.5b-llamacpp-q4km-instruct` descriptor: same official artifact lineage, same quantization, same runtime build family (b9672), same f16-KV cache class. No material surface change; historical profile and its events remain unchanged.

Official sampling (temp 0.6 / top_p 0.95 / top_k 20) for generation probes; quality screen at temp 0.

## 3. Performance

- llama-bench (canonical geometry, 5 reps): **pp512 7,744.16 ± 15.01 tok/s**, **tg128 271.66 ± 0.57 tok/s**.
- Uncached HTTP: short prompts **269–272 tok/s** decode, **~34 ms** TTFT; moderate ~4.5K-token prompts **~246 tok/s** decode, **568–575 ms** TTFT, end-to-end ~0.83 s.
- Near-full: 16K **221–253 tok/s** decode / 1.9 s TTFT; 32K 205–233; 64K 183–201; **131,072 at 99.66–99.76% occupancy: 4,872–4,883 tok/s prefill, 26.6 s TTFT, 107–160 tok/s decode**, peak 9,930 MiB, 75 °C.
- VRAM: 8,252 MiB at the 16K profile (≈3.9 GiB headroom); 131K admits at 9,850 MiB with 2,377 MiB free. Measured KV slope 15 KiB/token (7 full-attention layers; sliding-window KV fixed ≈42 MiB).
- Historical comparison (comparison-only): 2026-07-04 local LMX speed run on the same artifact measured 261.41 tok/s decode; current 271.66 (+3.9%) on the same build family.

## 4. Quality, capabilities, and reliability

- **Quality:** **11/12** frozen mechanical screen (frozen scorer, temp 0, raw outputs retained). Sole miss: three-word lowercase instruction retention.
- **Reasoning (direct mode, REASONING_OFF baseline):** PASS — multi-hop syllogism answered correctly with no `<think>` leakage (none exists on this checkpoint).
- **Coding:** PASS — `moving_sum` generated, executed, all oracle cases correct.
- **Tools:** PASS — native hermes-format `tool_call` structure, exact arguments, grounded continuation incorporating the tool result.
- **Reliability:** **7/20** (seed 42) and **8/20** (seed 314159) on the frozen 20-task mechanical corpus. Replicated category failures: **hallucination 0/4 and 1/4** — the model fabricated documentation for nonexistent APIs (a CUDA 13.3 signature, a fake `requests` package function, a fake `git timewarp` command) and summarized a nonexistent commit; **sycophancy 0/3** and **uncertainty 0/3** on both seeds (uncertainty failures are terse-form, not fabrication); **finish=length truncation on 7/20** at the frozen tight output budgets. Strong categories: strict interfaces 3/3 both seeds, evidence discipline 2/3 both, Git safety 1/1 both.

**Key guardrails:** human review of every API/command/documentation claim; do not rely on facts deeper than ~16K in the window; raise output budgets or force terse formats; keep context ≤16,384 (guarded 8,192); use the separate official Thinking checkpoint for explicit-CoT roles.

## 5. Context envelope

| Rung (native surface) | Capacity | Near-full performance | Useful context (2 seeds) | Disposition |
|---|---|---|---|---|
| 8,192 | admitted | 99.0% occupancy, pp 7,786–8,521, tg 242–264 | PASS 2/2 | **VALIDATED** |
| 16,384 | admitted | 99.4–99.5%, pp 7,917–8,247, tg 221–253 | PASS 2/2 | **VALIDATED** |
| 32,768 | admitted | 99.7–99.9%, pp 7,425–7,567, tg 205–233 | FAIL 1/2 (seed 42 pass) | **FAILED** (measured negative) |
| 65,536 | admitted | 99.5–99.6%, pp 6,367–6,412, tg 183–201 | FAIL 0/2 | **FAILED** (measured negative) |
| 131,072 (exact native maximum) | admitted (9,850 MiB, 2,377 MiB free) | 99.7–99.8%, pp 4,872–4,883, tg 107–160 | FAIL 0/2 | **FAILED** (capacity + performance validated; useful-context negative) |

- **USEFUL_CONTEXT_MAX = 16,384.** The ≥32K failures share one replicated signature across seeds and rungs: the 75%-depth decoy is reported instead of the 2%-depth target, the later (smaller) mid-window fact overrides the earlier one, while the 95%-depth item and terminal instruction remain correct — a recency-biased retrieval profile, not a throughput or fit failure.
- **CAPACITY 131K ≠ USEFUL CONTEXT 131K.** The model card's 131,072-token window genuinely loads and prefill-runs at near-full occupancy on 12 GB; that is not evidence the information throughout the window is usable.
- Useful-context placements were mechanically preflighted on the final rendered/tokenized stream (depths 2/25/50/75/95%; max error 0.024 pp, preferred bound 0.25 pp; zero fixture rejections; zero invalidated runs; zero cache-contaminated measurements).
- Official extension mechanisms: **none advertised** (documented absence; the native 131,072 is itself delivered by train-time YaRN baked into the checkpoint). Envelope **COMPLETE**: every major native rung and the exact maximum carry completed dispositions.

## 6. Historical evidence and comparison (bounded, comparison-only)

Pre-WELP evidence (2026-06-17 LLMGauge manual agent-backend scores; 2026-07-04 practical pool; 2026-07-04 local LMX speed) is retained unchanged. Supported by current evidence: full-GPU fit and high decode speed; "not safe for unsupervised shell/systemd" (now evidence-backed by the reliability corpus). Superseded/refined: "64k-stable" conflated completion stability with information use — useful context above ~16K now fails the frozen gate; fake-tool honesty (manual 4.0/5) coexisted with replicated fabrication of fake API documentation the old probe did not cover. The instruct-vs-thinking preference from manual scores remains unresolved under current WELP until the Thinking profile is recharacterized. No cross-protocol score equivalence is claimed.

## 7. LocalMaxxing and provenance

**LocalMaxxing: MEASURED_NOT_SUBMITTED.** A valid local canonical-profile benchmark exists (pp512 7,744.16 / tg128 271.66 tok/s, 5 reps); no service submission, contact, or fabricated verification field occurred. The historical 2026-07-04 local record for the same artifact is not an exact canonical-stack match and was never submitted.

Native publication under the consolidated `WumboLabs/evaluations` architecture. No per-profile or `eval-*` repository was created. Historical Mellum2 events (agent-backend, fake-tool, LMX speed, shared practical pool) are preserved unchanged; the Thinking profile remains separate with open current-WELP debt. The tested artifact's lifecycle after closeout: archived to the WumboServer model archive with per-file SHA-256 verification, then removed from local active storage.
