# Qwen3.6-35B-A3B — current-WELP recharacterization on RTX 5070 12 GB (llama.cpp, UD-IQ2_M, q8_0 KV)

- **Event ID:** `qwen36-35b-a3b-rtx5070-welp-recharacterization-2026-09-15`
- **Event date / closeout date:** 2026-09-15
- **Model:** Qwen3.6-35B-A3B (`Qwen/Qwen3.6-35B-A3B`, Alibaba Qwen team)
- **Profile:** `qwen3.6-35b-a3b-llamacpp-ud-iq2-m-q8kv` (current)
- **Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12 GB
- **Outcome:** **PASS — recharacterized under current WELP**
- **Classification:** **LIMITED_ROLE_ONLY**
- **Scope:** performance, practical viability (quality screen), coding, tool formatting, bounded reasoning probes, replicated reliability, text-context envelope with useful-context validation, and LocalMaxxing disposition
- **Protocol:** current WELP DRAFT; campaign snapshot `welp-next-snapshot-2026-09-15-qwen36-35b-a3b-recharacterization`

All measurements below are MEASURED on the listed stack unless labeled otherwise. This is the public-safe scientific record of the campaign; the retained local campaign bundle governs on any conflict.

## 1. Tested artifact and official source claims

- Exact artifact: `Qwen3.6-35B-A3B-UD-IQ2_M.gguf`, GGUF UD-IQ2_M, **11,522,702,304 bytes**, SHA-256 **`2be7ef1ed7e1af8b10d3829102cf9a6c2bd5ddb64d675b4ece23a60799403d43`**.
- Official source (EXTERNAL_REPORTED): `Qwen/Qwen3.6-35B-A3B` at revision **`995ad96eacd98c81ed38be0c5b274b04031597b0`**, Apache-2.0; multimodal Qwen3.5 MoE with 40 layers, 35B total / 3B active parameters, 256 routed experts (top-8 plus shared), native 262,144 context, and advertised static-YaRN extension to 1,010,000.
- The official model is multimodal. The tested profile is deliberately **text-generation only** (`--no-mmproj`): vision is **SUPPORTED_NOT_CHARACTERIZED**, not vision-tested.

## 2. Current serving profile

llama.cpp `0.1.0-dev`, build `10449`, commit `0d9ceae1e`; CUDA on RTX 5070; requested full GPU placement `-ngl 99`; `-c 32768 -ctk q8_0 -ctv q8_0 -b 256 -ub 64 -np 1 -fa auto --no-cache-prompt --reasoning off --no-mmproj --jinja`.

The q8_0 K/V cache, uncached prompt control, and 32K geometry are material to this profile identity. The older `qwen3.6-35b-a3b-llamacpp-ud-iq2-m` profile remains historical and retains its events.

## 3. Performance

- Uncached HTTP at 32K: short prompts **152.0–153.5 tok/s** decode and **70.6–86.9 ms** TTFT; moderate 3.58–3.66K prompts **146.8–148.1 tok/s** decode and **1.883–1.953 s** TTFT.
- Independent local llama-bench: **pp512 3571.96 ± 151.06 tok/s** and **tg128 157.62 ± 0.43 tok/s**.
- These are local measurements, not an external LocalMaxxing result.

## 4. Quality, capabilities, and reliability

- **Quality:** **11/12** frozen contract cases. The sole miss was the lexical no-`e` constraint.
- **Coding:** PASS. **Tools:** PASS.
- **Reasoning:** the frozen 1,500-token probe did not produce a final answer before its cap. A separate 4,096-token operational probe correctly completed `17 × 23 = 391` with coherent reasoning. Reasoning is operational with sufficient output budget; this is not an unconditional frozen-cap PASS.
- **Reliability:** **9/20** at seed 42 and **9/20** at seed 314159. Strict interfaces were 3/3 at both seeds, but Git safety was **0/1 at both seeds**. Substantive factual errors, hallucination-related failures, sycophancy and uncertainty weaknesses, plus repeated output-budget truncation determine the LIMITED_ROLE_ONLY classification.

Appropriate roles are bounded supervised text-generation work, structured interfaces, coding assistance with human review, and supervised tool formatting. Do not use this profile as an autonomous Git operator, high-assurance operational advisor, unsupervised open-ended factual assistant, high-assurance reasoning system, or autonomous destructive agent.

## 5. Context envelope

| Context | Disposition | Near-full occupancy | VRAM |
|---|---|---:|---:|
| 8,192 | VALIDATED | 99.007%, 98.848% | 11,126 MiB |
| 16,384 | VALIDATED | 99.378%, 99.206% | 11,228 MiB |
| 32,768 | VALIDATED | 99.549%, 99.209% | 11,434 MiB |

The canonical measured maximum is **32,768**. It is a tight-fit-only condition: roughly 433 MiB remains after a near-full request, so no concurrent GPU workload. The guarded practical limit is **16,384**. Do not flatten the validated maximum into the guarded operating point.

At 32K, two required seeds passed all useful-context gates with exact placement depths 2/25/50/75/95%; usable context was 31,961–31,964 tokens (99.48–99.49%). The measured q8 K/V slope was approximately 12.9 KiB/token.

The native **262,144** and advertised static-YaRN **1,010,000** maxima are both **FIT_LIMIT on this RTX 5070 12 GB/profile** under measured KV growth and the frozen 512 MiB headroom reserve. They are not universal model limitations and no unsafe OOM probe was run.

## 6. LocalMaxxing and provenance

**LocalMaxxing: MEASURED_NOT_SUBMITTED.** A valid local canonical-profile benchmark exists; no service submission, contact, or fabricated verification field occurred.

Native publication under the consolidated `WumboLabs/evaluations` architecture. No per-profile or `eval-*` repository was created. The public event preserves the accepted campaign outcome and limitations; retained raw evidence remains outside the public package.
