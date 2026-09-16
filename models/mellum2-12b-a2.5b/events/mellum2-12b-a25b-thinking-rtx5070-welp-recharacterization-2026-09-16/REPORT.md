# Mellum2 12B-A2.5B (Thinking) — current-WELP recharacterization on RTX 5070 12 GB (llama.cpp, Q4_K_M)

- **Event ID:** `mellum2-12b-a25b-thinking-rtx5070-welp-recharacterization-2026-09-16`
- **Event date / closeout date:** 2026-09-16
- **Model:** Mellum2 12B-A2.5B Thinking (`JetBrains/Mellum2-12B-A2.5B-Thinking`, JetBrains)
- **Profile:** `mellum2-12b-a2.5b-llamacpp-q4km-thinking` (current-alternate)
- **Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12 GB
- **Outcome:** **PASS — recharacterized under current WELP** (a restricted model verdict is a valid scientific result; outcome semantics follow the accepted Mellum2 Instruct recharacterization convention)
- **Classification:** **NOT_READY** for a current-WELP agent role
- **Scope:** performance, practical viability (quality screen), explicit-CoT reasoning, coding, native tools, replicated reliability, full native context capacity ladder with useful-context gates, LocalMaxxing disposition
- **Protocol:** current WELP DRAFT; campaign snapshot `welp-next-snapshot-2026-09-16-mellum2-12b-a25b-thinking-recharacterization`

All measurements below are MEASURED on the listed stack unless labeled otherwise. This is the public-safe scientific record of the campaign; the retained local campaign bundle governs on any conflict.

## 1. Tested artifact and official source claims

- Exact artifact: `Mellum2-12B-A2.5B-Thinking-Q4_K_M.gguf`, GGUF Q4_K_M, **8,071,295,040 bytes**, SHA-256 **`489cf0d7ca86ef4683e34e2efe8a46a9b52573bfe994a6ad9c86bf57c7173ccb`** — verified byte-exact against the official LFS object.
- Official source (EXTERNAL_REPORTED): `JetBrains/Mellum2-12B-A2.5B-Thinking-GGUF-Q4_K_M` at revision **`71a489e7b95efacf89feaaa6fe3b2995f3542409`**, Apache-2.0, official quantization of `JetBrains/Mellum2-12B-A2.5B-Thinking`. MoE with 64 routed experts and 8 activated per token (~12.15B total, ~2.5B active), 28 layers, GQA 32Q/4KV head_dim 128, hybrid attention (21 sliding-window layers with window 1,024 + 7 full-attention layers), native context **131,072** delivered by train-time YaRN (factor 16 from 8,192) baked into the released checkpoint.
- The Thinking artifact is the **official explicit-CoT checkpoint** — it emits its reasoning inside `<think>...</think>` blocks. It is a separate post-trained artifact from Instruct, **not** a runtime toggle on the Instruct profile. Both profiles are valid distinct official surfaces; this event does not alter the separately published Instruct result (LIMITED_ROLE_ONLY, USEFUL_CONTEXT_MAX 16,384).
- Historical Thinking artifacts were absent from active storage and the archive with no retained hash; the artifact above was independently reacquired from the pinned official repository revision and verified byte-exact before any measurement.

## 2. Current serving profile

llama.cpp `b9672` (commit `74ade5274`); CUDA SM120 on RTX 5070; full GPU placement `-ngl 99` (28/28 transformer layers GPU-resident, no hidden offload); `-np 1`; `-fa on`; f16 K/V cache; measurement prompt cache disabled (`--no-cache-prompt --cache-ram 0`, `cached_tokens = 0` verified on every retained request).

Native Jinja template with thinking enabled; server-extracted `reasoning_content` recorded separately from final content. Official sampling (temp 0.6 / top_p 0.95 / top_k 20) for admission and generation probes; quality screen at temp 0. No sampling, scoring, output budget, or fixture was changed after outputs were observed.

The profile identity **reuses** the existing `mellum2-12b-a2.5b-llamacpp-q4km-thinking` descriptor: same official Thinking artifact lineage, same quantization, same llama.cpp runtime family, same f16-KV cache class. Historical Thinking events (agent-backend fit, practical pool, LMX speed) are preserved unchanged.

## 3. Performance

- llama-bench (canonical geometry): **pp512 7,710.53 ± 18.61 tok/s**, **tg128 270.75 ± 0.66 tok/s**.
- Uncached HTTP: short-prompt decode **267.8–268.3 tok/s** (~43 ms TTFT); moderate ~4.5K-token prompts **245.4–246.9 tok/s** decode; near-full 16K TTFT ~1.91 s. All retained performance measurements are cache-free; a first performance attempt invalidated by implicit prompt caching was discarded and re-run cache-free.

## 4. Quality, capabilities, and reliability

- **Quality:** **11/12** frozen mechanical screen (frozen scorer, temp 0, raw outputs retained). Q12 returned empty at the fixed output cap.
- **Reasoning (explicit CoT):** PASS — narrow multi-hop syllogism probe answered correctly with explicit reasoning and a correct final answer.
- **Coding:** PASS — `moving_sum` generated, executed, all oracle cases correct.
- **Tools:** PASS — native tool call with exact name and arguments, plus a grounded continuation incorporating the tool result.
- **Reliability:** **3/20** (seed 42) and **3/20** (seed 314159) on the frozen 20-task mechanical corpus. **All 20/20 requests per seed ended `finish=length`**: the frozen 512-token completion reserve is systematically exhausted by explicit reasoning before any final answer. Strict interfaces 3/3 both seeds. The failure mode is systematic explicit-reasoning token consumption under the frozen output limits — not a transient GPU, cache, or artifact problem.

**Key guardrails:** do not deploy this profile as a current-WELP agent backend; every reliability output truncates in reasoning under the frozen budgets; narrow capability successes (reasoning probe, coding, tools) do not qualify the profile for an agent role; performance and capacity are not usefulness.

## 5. Context envelope

| Rung (native surface) | Capacity | Near-full performance | Useful context (2 seeds) | Disposition |
|---|---|---|---|---|
| 8,192 | admitted | 98.97–98.98% occupancy, pp 7,742–8,496 | FAIL 0/2 | **FAILED** (measured negative) |
| 16,384 | admitted | 99.36–99.50%, pp 7,926–8,242 | capacity-only rung | capacity + performance validated |
| 32,768 | admitted | 99.66–99.89%, pp 7,423–7,562 | capacity-only rung | capacity + performance validated |
| 65,536 | admitted | 99.47–99.63%, pp 6,352–6,407 | capacity-only rung | capacity + performance validated |
| 131,072 (exact native maximum) | **VALIDATED** (admits at f16 KV) | 99.66–99.76%, pp 4,875–4,886 | FAIL 0/2 | **CAPACITY VALIDATED; useful-context FAILED** |

- **CAPACITY_MAX = 131,072, VALIDATED** — the exact native window loads, prefill-runs, and generates at near-full occupancy (99.66–99.76%) with two cache-free reps at every rung from 8,192 through the exact maximum.
- **USEFUL_CONTEXT_MAX = NONE_VALIDATED.** The lowest native rung (8,192) and the exact maximum (131,072) both fail the frozen two-seed useful-context gate because the model spends the entire 512-token completion reserve on explicit reasoning before emitting any final answer (`answer` empty, `completion_tokens` 512/512 on failed runs). This is a completion-budget interaction with the Thinking format under the frozen contract, not a retrieval-quality or fit failure.
- **CAPACITY 131K ≠ USEFUL CONTEXT 131K.** The 131,072-token window genuinely admits and performs; that is not evidence that information throughout the window is usable under the frozen contract.
- Useful-context placements were mechanically preflighted on the final rendered/tokenized stream (99.50–99.76% occupancy on gate runs; `cached_tokens = 0` throughout). Official extension mechanisms: **none advertised** (documented absence). Envelope **COMPLETE**: every native rung and the exact maximum carry completed dispositions.

## 6. Relationship to the Instruct profile and historical evidence

Instruct and Thinking are distinct official RL-post-trained artifacts. The separately published Instruct current-WELP result (LIMITED_ROLE_ONLY, USEFUL_CONTEXT_MAX 16,384, reliability 7/20 and 8/20) is unchanged by this event. Pre-WELP Thinking evidence (2026-06-17 agent-backend fit at 64k; 2026-07-04 practical pool 232.8/300; 2026-07-04 LMX speed 265.47 tok/s) is retained unchanged as historical, non-comparable context; no cross-protocol score equivalence is claimed.

## 7. LocalMaxxing and provenance

**LocalMaxxing: MEASURED_NOT_SUBMITTED.** A valid local canonical-profile benchmark exists (pp512 7,710.53 / tg128 270.75 tok/s); no service submission, contact, or fabricated verification field occurred.

Native publication under the consolidated `WumboLabs/evaluations` architecture. No per-profile or `eval-*` repository was created. Historical Mellum2 events (agent-backend, fake-tool, LMX speed, shared practical pool) and the current Instruct event are preserved unchanged. After publication the tested artifact follows the model-artifact lifecycle: archival to the WumboServer model archive with per-file size + SHA-256 verification, with local removal only after the archive copy independently verifies byte-exact.
