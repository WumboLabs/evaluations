# LFM2.5-2.6B QAD Q4_0 on WumboJetsII

## Verdict

**QAD Q4_0 is the rational ultra-fast deployment quant when 1.59 GB is the hard model-size target, but this campaign did not reproduce a material practical-quality win over ordinary PTQ Q4_0.** It exactly retained PTQ Q4_0's 4K GPU footprint and throughput, and it improved the fixed-corpus perplexity diagnostic. The small practical, tool, and coding lanes do not establish the producer's 96.6% aggregate-retention or Q4_K_M-equivalence claims.

## Identity and method

- Source: `LiquidAI/LFM2.5-2.6B-GGUF` revision `f4a289c8a200a5ca71005ba7abc2dad33058a450`.
- QAD: a high-precision teacher is distilled into a quantized Q4_0 student. It is not a differently decoded tensor format; QAD and PTQ use Q4_0 layout/runtime paths.
- Model card verified: 2.69B parameters; 30 layers (22 double-gated short-convolution plus 8 GQA); 131,072 context; 34T training tokens; agentic post-training. Official sampling: temperature 0.1, top-k 50, repeat penalty 1.1.
- Runtime: llama.cpp build 10449, commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`, CUDA architecture 120, CUDA 13.3, Flash Attention on, GPU layers all, GPU KV, `--fit off`, one sequence.
- Hardware: RTX 5070 12 GB, driver 610.57.04; Ryzen 7 9800X3D.

## Candidate files

| Quant | Bytes | SHA-256 |
|---|---:|---|
| BF16 | 5,403,158,528 | `590b1534d5ec57dbddb750d25468d7ba4df0d1976531a731590418efa360edb5` |
| PTQ Q4_0 | 1,593,894,912 | `e1a61bf937bc60726e18626e97f7ee9bfd2574d95744c2ed909de98b78006fbe` |
| QAD Q4_0 | 1,593,894,944 | `a247afd6414918eac8e520a9e6137dc271235461ecbe1180462221d5b8d40b03` |
| Q4_K_M | 1,674,455,040 | `02a8b7e17487d326e46d68ce0ba24211e1b80a14c4cd0597fa73c1cd697f52ed` |
| Q5_K_M | 1,939,744,768 | `17ce54cc676e15e572adebfeeed8da6abd12b0f68d595be19b59e662476c21b3` |

Q6_K and Q8_0 were also acquired for speed references.

## Admission, memory, and speed

Matched 4K context, 128 generated tokens, one warmup excluded, five measured repetitions:

| Quant | Peak GPU MiB | Prompt tok/s mean | Decode tok/s mean ± sd | Mean TTFT ms |
|---|---:|---:|---:|---:|
| BF16 | 6100 | 1498.0 | 105.1 ± 0.2 | 20.7 |
| PTQ Q4_0 | 2404 | 3235.4 | 282.7 ± 1.0 | 9.6 |
| QAD Q4_0 | 2404 | 3221.8 | 282.5 ± 0.4 | 9.6 |
| Q4_K_M | 2480 | 2777.0 | 263.1 ± 0.3 | 11.2 |
| Q5_K_M | 2734 | 2649.9 | 240.5 ± 0.2 | 11.7 |

QAD is 0.07% slower than PTQ decode, within run variance, and has the identical observed peak allocation. This reproduces the native-Q4_0 speed/memory claim.

## Fidelity

`llama-perplexity` on fixed local repeated natural-language and code corpora found QAD lower than PTQ (natural 1.0408 vs 1.0882; code 1.1248 vs 1.1412). QAD also scored below BF16 on those corpora. This is evidence of a QAD-vs-PTQ log-probability improvement, not a BF16-quality percentage: the repeated local corpus gives QAD a lower perplexity than BF16, so it cannot calibrate aggregate intelligence or retention.

## Producer benchmark reproduction

**INCONCLUSIVE.** Liquid's 19 Aug 2026 QAD release reports 96.6% 2.6B BF16-average retention and 48.4% PTQ-gap recovery over GPQA Diamond, MMLU-Pro, IFEval, IFBench, Multi-IF, BFCLv4, and AIME25, averaged over five repeats. The accepted read-only LLMGauge commit explicitly lacks faithful public contracts for MMLU-Pro, GPQA, and IFEval and forbids native-prompt substitutes. No proxy was called a reproduction; LLMGauge was not modified.

## Practical behavior

A compact mechanically scored exact-match set tested instruction following, JSON, absent-evidence responses, and document extraction. Results were noisy and small: QAD was stronger than PTQ on the three instruction/extraction exact checks but weaker on the two hallucination and two structured-output checks. BF16 was not consistently best in this tiny suite, so BF16 retention and PTQ-to-BF16 gap-recovery percentages are mathematically undefined here.

- **Structured output:** no demonstrated QAD improvement over PTQ; QAD 1/2 vs PTQ 2/2.
- **Hallucination resistance:** no demonstrated QAD improvement; QAD 1/2 vs PTQ 2/2 on explicit invented-command/field refusals.
- **Extraction/RAG:** QAD 1/2 vs PTQ 0/2, but this is too small for a deployment claim.
- Human review: all mechanical failures were retained in `results/practical_raw.json`; no bulk successful output was used as agent evidence.

## Coding

Twenty isolated sandbox executions were attempted per primary quant. Each produced 4/20 execution successes; the suite exposed brittle single-code-block compliance and supports Liquid's warning that 2.6B is not for agentic coding. The bubblewrap sandbox used no network and no host writable bind. Coding is a poor fit regardless of the observed QAD quantization change.

## Native tools

All four compared quants passed the five deterministic local schema cases (tool selection, no-tool, enum, and integer-array arguments): 5/5. QAD did not improve this already-saturated simple suite. Nested-object, tool-result continuation, and recovery after an error remain unverified; do not generalize 5/5 to real agent reliability.

## Context

All three finalists allocated and prefixed prompts through 127,777 actual tokens. QAD and PTQ retrieved the beginning needle at approximately 3.9K and 8.0K tokens, but neither produced a final answer above 16K within a 256-token generation budget. Q4_K_M retrieved at 3.9K and 32.5K but failed other rungs. Allocation is not useful context. **Useful long-context behavior is not established beyond 8K for QAD/PTQ from this run.** No claim of QAD long-context improvement is supported.

## Sampling and variance

Official settings were primary. A bounded QAD comparison used official (0.1), deterministic (0.0), and expressive (0.25) temperatures; see `summaries/sampling.json`. Three fixed seeds were run on instruction, structured, hallucination, tool-like, and coding contracts; see `summaries/variance.json`. Use the official 0.1 / top-k 50 / repeat penalty 1.1 profile; no bounded evidence justified changing it.

## Stability and power

The loopback QAD server completed 1,808.7 seconds (30m 8.7s), 175 varied requests, and zero request errors; observed response latency was 0.159–0.508 s. It shut down cleanly and GPU allocation returned to 535 MiB desktop baseline. GPU telemetry was sampled every two seconds; final kernel-log query found no Xid/reset/GSP/channel-failure entries. Power-limit experiments were not run: QAD's matched run peaked at 163.29 W, already below 175 W, and no established non-privileged power-limit workflow was available.

## Deployment recommendation

**Recommended profile:** QAD Q4_0; llama-server loopback-only; `-ngl all -fit off -c 4096 -b 2048 -ub 512 -fa on -np 1`; GPU KV; official sampler (0.1, top-k 50, repeat penalty 1.1).

- Best fastest/lowest-memory quant: PTQ Q4_0 and QAD Q4_0 tie operationally; QAD is preferred because its fixed-corpus fidelity diagnostic is better.
- Closest to BF16: unestablished by practical tests; BF16 is the full-precision reference, Q5_K_M is the sensible higher-quality small quant.
- Best tool use: all four tie on the limited deterministic suite.
- Best sidecar candidate: QAD Q4_0, as an always-loaded router/extraction/tool helper with schema validation and evidence checks.
- Not a primary assistant, long-context retriever, or coding agent.

## Claim classifications

| Claim | Classification |
|---|---|
| QAD preserves Q4_0 memory | REPRODUCED |
| QAD preserves Q4_0 decode throughput | REPRODUCED |
| QAD materially beats ordinary PTQ Q4_0 | PARTIALLY_REPRODUCED: lower local PPL; no material practical win shown |
| QAD retains 96.6% BF16 aggregate | INCONCLUSIVE |
| QAD recovers 48.4% of PTQ gap | INCONCLUSIVE |
| QAD matches Q4_K_M quality | INCONCLUSIVE |
| QAD improves native tools | INCONCLUSIVE: all simple cases saturated |
| QAD improves structured output | NOT_REPRODUCED |
| QAD improves hallucination resistance | NOT_REPRODUCED |
| QAD improves long context | NOT_REPRODUCED |

## Retention

Keep QAD primary, BF16 control, PTQ control, Q4_K_M/Q5_K_M references. Q6_K and Q8_0 are optional. Potential space recoverable after human review: 5,096,394,752 bytes. Nothing was deleted.
