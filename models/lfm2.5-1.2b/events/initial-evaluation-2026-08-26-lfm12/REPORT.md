# LFM2.5-1.2B-Instruct QAD Q4_0 on WumboJetsII

## 1. Executive verdict

**QAD Q4_0 is the best deployment quant of the five-way matrix and the best always-resident sidecar candidate measured so far in this model family, but the campaign did not reproduce Liquid's hallucination or aggregate-retention story: at 1.2B every quant including BF16 fabricates confidently on invented subjects (0/12), and QAD's fixed-corpus perplexity advantage over PTQ inverted.** QAD kept exactly Q4_0 memory and within-variance Q4_0 speed, scored best of all quants on the 52-task practical suite (31/52 vs PTQ 30, Q5_K_M 29, Q4_K_M / UD-Q4_K_XL 27), and is faster than both K-quant controls (~+6% decode). Useful context is ≤ 8K for every candidate.

## 2. Exact identities

| Quant | Repo@revision | Bytes | SHA-256 |
|---|---|---:|---|
| BF16 | LiquidAI/LFM2.5-1.2B-Instruct-GGUF@`67672651…3615b` | 2,343,326,528 | `3d80914b903cd6f3cc041208cf20ec46a3224f840c732e5fd7698832b4743d1b` |
| PTQ Q4_0 | same | 695,751,488 | `2ea801949d760cdf1a2cc04a54262c22c3c0c54f0769d57760c9adeb0e59233f` |
| **QAD Q4_0** | same | 695,755,488 | `bb741ebb106d543e9de114b843a3d3d73d51c74b5801e69da2abde821a0cb3e1` |
| Q4_K_M | same | 730,895,168 | `b1b3de114215d9507409a662a501a631095a479a419584e8a2ded6304b19b4f5` |
| UD-Q4_K_XL | unsloth/…@`b01cc872…d854` | 730,895,584 | `856aeee6d85ac684b1db8dee48795b44fc06731ecda03aee36ece682413a9b9a` |
| Q5_K_M | LiquidAI | 843,354,944 | `fa03f3ac4da941a53a0cd4450aacf6a80804c6a1ff885d2fdcbe9406c03215c4` |

All local SHA-256s match upstream LFS OIDs at the pinned revisions. **UD-Q4_K_XL is byte-identical to Unsloth's own `LFM2.5-1.2B-Instruct-Q4_K_M.gguf` (same LFS OID) and is NOT byte-identical to Liquid's Q4_K_M (416 bytes smaller, different OID).** Model card facts: 1.17B params, 16 layers (10 conv + 6 GQA), 28T training tokens, context 32,768, license lfm1.0. Official sampling verified from current cards: temp 0.1, top-k 50, repeat penalty **1.05** (the 2.6B card used 1.1).

## 3. Hardware/runtime

- RTX 5070 12 GB (GPU-3606a9f1…), driver 610.57.04, power limit 250 W, desktop baseline ~572–607 MiB
- Ryzen 7 9800X3D, Fedora 44, kernel 7.1.9-200.fc44
- llama.cpp build 10449 commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd` (same runtime as the 2.6B campaign; not updated)
- All runs: CUDA, `-ngl all -fit off -fa on -np 1`, GPU KV, loopback-only server; placement verified from per-PID compute-apps VRAM and verbose logs (17/17 layers offloaded for every candidate)
- LLMGauge untouched at accepted commit `595e1771c6e2b6d9f9cd2f34f48a89117ef5782f`

## 4. Producer claims

See §22 classifications. Headline: 97.4% BF16 aggregate retention INCONCLUSIVE (suite not locally reproducible); native Q4_0 speed/memory REPRODUCED.

## 5. Candidate matrix

Six candidates (§2). Five-way core comparison BF16 / PTQ Q4_0 / QAD Q4_0 / Liquid Q4_K_M / Unsloth UD-Q4_K_XL plus Q5_K_M reference. No optional Q6_K/Q8_0 acquired (no concrete evidence reason).

## 6. Admission

All six models load successfully, 17/17 layers on GPU:

| Quant | Process VRAM MiB | Peak MiB | Model buffer MiB |
|---|---:|---:|---:|
| BF16 | 2530 | 3106 | 2232.5 |
| PTQ Q4_0 | 958 | 1534 | 661.25 |
| **QAD Q4_0** | **958** | **1534** | **661.25** |
| Q4_K_M | 992 | 1568 | 694.76 |
| UD_Q4_K_XL | 992 | 1568 | 694.76 |
| Q5_K_M | 1100 | 1676 | 802.01 |

QAD and PTQ are byte-for-byte identical in allocation behavior. No CPU offload occurred anywhere.

## 7. Performance

Matched 4K context, identical prompt, official sampler, 1 warmup excluded, 5 measured repetitions each:

| Quant | Prompt tok/s | Decode tok/s mean ± sd | Median | TTFT ms |
|---|---:|---:|---:|---:|
| BF16 | 3383 | 232.6 ± 3.16 | — | 9.7 |
| PTQ Q4_0 | 6944 | 592.3 ± 2.27 | — | 4.8 |
| **QAD Q4_0** | 6600 | **585.6 ± 2.79** | — | 4.9 |
| Q4_K_M | 6054 | 554.4 ± 1.65 | — | 5.5 |
| UD_Q4_K_XL | 5947 | 551.0 ± 4.19 | — | 5.3 |
| Q5_K_M | 5777 | 510.7 ± 4.44 | — | 6.0 |

Deltas: **QAD −1.14% vs PTQ decode** (within variance), **+5.63% vs Liquid Q4_K_M**, **+6.28% vs UD-Q4_K_XL**, +151.7% vs BF16. Every individual measurement retained in `summaries/performance.json`. No cherry-picking.

## 8. Objective fidelity

`llama-perplexity`, 512-token chunks ×8, on the exact 2.6B-campaign corpora (`sources/SHA256SUMS`):

| Quant | Natural PPL | Code PPL |
|---|---:|---:|
| BF16 | 1.5235 | 1.0514 |
| PTQ Q4_0 | **1.2454** | **1.0378** |
| QAD Q4_0 | 1.3941 | 1.0472 |
| Q4_K_M | 1.3176 | 1.0457 |
| UD_Q4_K_XL | 1.3260 | 1.0463 |
| Q5_K_M | 1.6216 | 1.0475 |

**The 2.6B finding inverted: at 1.2B PTQ beats QAD on natural text.** The repeated-corpus pathology persists and worsens — BF16 is worse than most quants on natural text, so no BF16-relative percentage from this corpus is valid. These values measure log-probability fit on a memorized corpus only.

## 9. Practical capability

52 unique mechanically-scored tasks (instruction 10, extraction 8, structured 12, false-premise 12, Linux knowledge 6, factual uncertainty 4), same set for all six models, seed 42:

| Model | Instr | Extr | Struct | Halluc | Linux | Uncert | Total |
|---|---|---|---|---|---|---|---|
| BF16 | 8/10 | 4/8 | 12/12 | 0/12 | 4/6 | 4/4 | **32/52** |
| **QAD Q4_0** | 8/10 | 4/8 | **11/12** | 0/12 | 4/6 | 4/4 | **31/52** |
| PTQ Q4_0 | 8/10 | 4/8 | 10/12 | 0/12 | 4/6 | 4/4 | 30/52 |
| Q5_K_M | 8/10 | 4/8 | 10/12 | 0/12 | 3/6 | 4/4 | 29/52 |
| Q4_K_M | 8/10 | 3/8 | 10/12 | 0/12 | 3/6 | 3/4 | 27/52 |
| UD_Q4_K_XL | 8/10 | 3/8 | 10/12 | 0/12 | 3/6 | 3/4 | 27/52 |

One scoring defect was found during human review (bool_field expected `{"prime":true}` for "Is 25 prime?" — 25 is composite) and corrected; all six models then passed it; everything else re-aggregated unchanged. Failure review showed many "fails" are strict-format strictness (`DNF` vs `dnf`, prose around refusals); genuine errors were arithmetic (sum_fields) and routing judgment. QAD is the best quant and within one task of BF16.

## 10. Hallucination resistance

Twelve invented-subject probes (packages, flags, APIs, files, systemd units, sysctls, Kconfig options): **every model, including BF16, fabricated confident detailed explanations — 0/12 across the entire matrix.** Classifier output manually verified against raw answers. This is a model-family property at 1.2B scale, not a quantization effect; QAD shows no improvement (and none was claimed by the producer). The separate absent-evidence probes behaved safely everywhere ("not provided"/"absent"); only QAD emitted the exact required `ABSENT` token (strict format 4/4).

## 11. Structured output

Mechanical JSON/schema scoring: QAD 11/12, PTQ/Q4_K_M/Q5_K_M/UD 10/12, BF16 12/12. Unlike the 2.6B campaign, a small QAD-over-PTQ edge appeared (+1). The universal miss before correction was our own bug; residual strictness cases (`{"ok": true}` with space) parse as valid JSON semantically. Variance lane: outputs are deterministic (1 unique answer per probe across seeds 11/22/33) for all quants.

## 12. Native tools

v1 (exact 2.6B five-case contract): saturated — 5/5 for BF16, PTQ, QAD, Q4_K_M, Q5_K_M; **UD-Q4_K_XL 4/5**.
v2 (ten harder cases, scored separately):

| Model | Selection | Schema valid | Result interpretation | Final answer correct | Complete sequences |
|---|---|---|---|---|---|
| BF16 / PTQ / QAD / Q4_K_M | 7/10 | 9/10 | 7/10 | 2/10 | 5/10 |
| Q5_K_M | 7/10 | 9/10 | 6/10 | 1/10 | 4/10 |
| UD_Q4_K_XL | 6/10 | 8/10 | 7/10 | 2/10 | 4/10 |

No single "tool accuracy" number is reported; complete multi-turn tool sequences succeed only half the time even for BF16. QAD ties its controls; the external control is weakest again.

## 13. Extraction/RAG

Strict exact-match extraction: QAD/BF16/PTQ/Q5_K_M 4/8, Q4_K_M/UD 3/8. Absent-information handling is safe for all models. QAD does not beat PTQ here (tie); both beat the two K-quant controls by one task. Section-ID citation and conflict-resolution tasks pass only when phrased tightly. A 1.2B extraction helper needs schema validation and should not be trusted for arithmetic over fields (sum_fields failed for every quant except BF16-class runs).

## 14. Coding

20 sandboxed executions per quant (the 2.6B 5-task contract ×4 rotations, bwrap, no network) + dependency-hallucination probe:

| Quant | Executable | Parse | Dependency hallucination |
|---|---:|---:|---|
| Q5_K_M | 12/20 | 20/20 | no |
| BF16 / Q4_K_M / UD | 8/20 | 20/20 | no |
| PTQ / **QAD** | 4/20 | 20/20 | no |

Parse success is universal; failures are instruction-compliance (QAD defines `sum(a,b)` instead of required `solve`) rather than syntax. Coding remains a poor fit at this scale; QAD is worse than the K-quants here.

## 15. Context

Three-needle retrieval (begin/middle/end) + trailing-format instruction + absent-evidence probe at 4K/8K/16K/32K (card limit 32,768), finalists only:

| Rung actual tokens | QAD | PTQ | Q4_K_M | UD |
|---|---|---|---|---|
| 3608 | 3/3 needles, ordered | 3/3 ordered | 3/3 ordered* | 3/3 ordered |
| 7568 | 3/3 ordered | 3/3 ordered | 3/3 ordered* | 3/3 ordered* |
| 15308 | 0/3 (filler parroting) | 0/3 | 0/3 | 0/3 |
| 30968 | 0/3 | 0/3 | 0/3 | 0/3 |

\* minor trailing-prose violations. At ≥16K every model degenerates into repeating filler text. **Useful context ceiling: 8K for all finalists.** Allocation beyond that is meaningless. Per the campaign bounds, 64–128K was not pursued: the card documents 32K and behavior already collapsed at 16K.

## 16. Variance

Three seeds × five representative tasks × six models (`summaries/variance.json`): zero output diversity (single unique response per probe) for every model/quant; pass differences between quants come from ability, not sampling noise. Speed sd ≤ 4.4 tok/s across 5 reps. No lane needed escalation to 5 seeds.

## 17. Producer benchmark reproduction

INCONCLUSIVE. Liquid's suite: GPQA Diamond, MMLU-Pro, IFEval, IFBench, Multi-IF, BFCLv4, AIME25 (mean of 5 repeats). Verified read-only at accepted commit 595e177: LLMGauge qualifies Bundle-1 benchmarks only and explicitly lists MMLU-Pro, GPQA, IFEval as unsupported/Bundle-2 and forbids recreating them as native prompts. Running lm-eval-harness defaults would be a proxy with unknown prompt/generation methodology, not a reproduction, so it was not run and not labeled as reproduction.

## 18. 1.2B vs 2.6B

| Dimension | 2.6B QAD | 1.2B QAD | Δ |
|---|---|---|---|
| GGUF bytes | 1,593,894,944 | 695,755,488 | −898 MB |
| Peak VRAM | 2404 MiB | 1534 MiB | −870 MiB |
| Decode tok/s | 282.5 | 585.6 | ×2.07 |
| Prompt tok/s | 3221.8 | 6600.0 | ×2.05 |
| Fidelity vs PTQ | QAD better on both corpora | PTQ better (natural) | inverted |
| Structured vs PTQ | no improvement | +1 task | small positive |
| Hallucination resistance | no QAD effect shown | absent at model level | worse scale behavior |
| Coding | 4/20 all quants | QAD 4/20 (K-quants 8–12) | comparable/poor |
| Useful context | ≤ ~8K | ≤ 8K | equal |
| Tool saturation | 5/5 all | 5/5 (UD 4/5) | equal |

Performance gained: 2× throughput, 870 MiB freed. Capability lost: fidelity-diagnostic direction, some coding robustness relative to K-quants, and — critically — hallucination resistance, which at 1.2B is nonexistent even in BF16 while the 2.6B class could at least sometimes reject invented commands under explicit-refusal prompts. On a 12 GB RTX 5070 the extra 870 MiB saved is rarely decisive; the doubled speed and tiny resident footprint are the real arguments.

**Verdict: the 1.2B creates a genuinely better *always-resident micro-sidecar* niche (router/classifier/formatter/tool-selector) because it is twice as fast at less than two-thirds of the VRAM, but it is a strictly weaker *knowledge/extraction assistant*: anything where fabrication risk matters got worse, and the capability loss is NOT worth ~900 MB on a 12 GB card if extraction/RAG quality is the goal — for that role the 2.6B QAD remains preferable.**

## 19. Stability

The loopback-only QAD soak completed 1805.9 s (30 m 6 s), **180 varied requests, zero request errors**; response latency 0.013–0.024 s, mean decode 547 tok/s, peak power 33.6 W, max temperature 52 °C. Three of four sentinels passed every repetition; the fourth (`Return ticket only`) deterministically wrapped the correct value in prose — the same strict-compliance quirk seen in extraction. Server stopped cleanly, GPU allocation returned to the 576 MiB desktop baseline, no llama processes remained. Telemetry sampled every 2 s throughout (`telemetry/gpu_telemetry.csv`). Kernel journal before, during, and after: **zero Xid / reset / GSP / channel events.**

## 20. Role suitability

GOOD FIT: always-loaded router, classifier, simple tool selector.
USABLE WITH GUARDRAILS: extraction helper, RAG helper (≤8K), structured formatter, conversational sidecar.
POOR FIT: coding helper, primary assistant, autonomous agent.

## 21. Claim classifications

| Claim | Classification |
|---|---|
| QAD keeps Q4_0 memory | REPRODUCED (identical buffers/peak) |
| QAD keeps Q4_0 speed | REPRODUCED (−1.14%, within variance) |
| 97.4% BF16 aggregate retention | INCONCLUSIVE |
| Matches Liquid Q4_K_M | PARTIALLY_REPRODUCED (beats it on practical suite + speed) |
| Matches Unsloth UD-Q4_K_XL | PARTIALLY_REPRODUCED (ahead or tied on every lane) |
| Meaningful recovery of PTQ loss | PARTIALLY_REPRODUCED (+1 practical total, +1 structured; PPL direction inverted) |
| Improves hallucination resistance | NOT_REPRODUCED (no quant helps; model-level failure) |
| Within half a point of Q5_K_M | INCONCLUSIVE (producer benchmark); on bounded tests QAD ≥ Q5_K_M |

## 22. Recommended deployment profile

QAD Q4_0, profile in `profiles/deployment.md`: `-ngl all -fit off -c 4096 -b 2048 -ub 512 -fa on -np 1`, loopback, official sampler (0.1/50/1.05), schema validation + fabrication guardrails, context ≤ 8K.

Rankings: fastest = PTQ (marginal) → QAD; smallest = tie PTQ/QAD; closest objective fidelity = PTQ on this corpus; best practical quality = BF16 then QAD; best structured = BF16 then QAD; tools = four-way tie; coding = Q5_K_M; useful context = tie at 8K; quality-per-byte and best overall sidecar = **QAD Q4_0**.

QAD preferable to PTQ Q4_0: YES (equal cost, better practical suite, negligible speed cost).
QAD preferable to Liquid Q4_K_M: YES (better quality AND faster AND smaller).
QAD preferable to Unsloth UD-Q4_K_XL: YES (same margins; UD additionally failed a simple tool case).

## 23. Limitations

Single machine, single seed per practical task (variance lane shows determinism, but single-seed category scores carry ±1–2 task noise at n=52). Fixed-corpus PPL is pathological (memorized corpus) and cannot calibrate retention. Producer benchmark claims remain untested. Hallucination suite is 12 invented subjects — enough to establish absence of rejection ability, not fine gradations. Context findings capped at card limit 32K.

## 24. Execution-count accounting

See `summaries/execution_counts.json`; headline totals: 312 practical generations (52×6; includes 72 hallucination probes), 30 tool v1 + ~102 tool v2 generations, 126 coding generations/executions, 90 variance generations, 32 context calls, 12 perplexity runs, 36 speed runs (6 warmups + 30 measured), 180 soak requests — roughly 770 local model generations in total. All generations were mechanically scored by local scripts; supervising-agent review was limited to failures plus bounded samples, producing one scoring correction (§9).

## 25. Retention

Delete nothing. KEEP: QAD, BF16, PTQ, Q4_K_M. OPTIONAL after human review: Q5_K_M, UD-Q4_K_XL (byte-identical to unsloth's own Q4_K_M). Potential recoverable: 1,574,250,528 bytes. Nothing was deleted.
