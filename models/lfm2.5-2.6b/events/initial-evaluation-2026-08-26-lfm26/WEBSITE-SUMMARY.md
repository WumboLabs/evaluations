### Identity

| Field | Value |
|---|---|
| Model | LFM2.5 2.6B |
| Producer | Liquid AI |
| Evaluated artifact | QAD Q4_0 from `LiquidAI/LFM2.5-2.6B-GGUF` @ `f4a289c8a200a5ca71005ba7abc2dad33058a450` |
| SHA-256 | `a247afd6414918eac8e520a9e6137dc271235461ecbe1180462221d5b8d40b03` |
| Evaluation date | 2026-08-26 |
| Protocol | WELP |
| Campaign classification | COMPLETE_SMALL_MODEL_EVALUATION |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| CPU | AMD Ryzen 7 9800X3D |
| OS | Fedora Linux 44 |
| Driver / CUDA | NVIDIA 610.57.04 |
| Runtime | llama.cpp b10449 (commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`) |

### Headline Verdict

**QAD Q4_0 is the rational ultra-fast deployment quant when 1.59 GB is the hard model-size target, but this campaign did not reproduce a material practical-quality win over ordinary PTQ Q4_0.**

QAD exactly retained PTQ Q4_0's 4K GPU footprint and throughput, and it improved the fixed-corpus perplexity diagnostic. The small practical, tool, and coding lanes do not establish the producer's 96.6% aggregate-retention or Q4_K_M-equivalence claims.

### Performance

| Quant | Peak GPU MiB | Prompt tok/s | Decode tok/s | TTFT ms |
|---|---|---|---|---|
| BF16 | 6100 | 1498.0 | 105.1 | 20.7 |
| PTQ Q4_0 | 2404 | 3235.4 | 282.7 | 9.6 |
| QAD Q4_0 | 2404 | 3221.8 | 282.5 | 9.6 |
| Q4_K_M | 2480 | 2777.0 | 263.1 | 11.2 |
| Q5_K_M | 2734 | 2649.9 | 240.5 | 11.7 |

QAD is 0.07% slower than PTQ decode (within run variance) and has identical observed peak allocation. This reproduces the native-Q4_0 speed/memory claim.

### Fidelity

`llama-perplexity` on fixed local repeated corpora found QAD lower than PTQ (natural 1.0408 vs 1.0882; code 1.1248 vs 1.1412). QAD also scored below BF16 on those corpora. This is evidence of a QAD-vs-PTQ log-probability improvement, not a BF16-quality percentage.

### Practical Behavior

A compact mechanically scored exact-match set tested instruction following, JSON, absent-evidence responses, and document extraction. Results were noisy and small:

- **Structured output:** no demonstrated QAD improvement over PTQ; QAD 1/2 vs PTQ 2/2.
- **Hallucination resistance:** no demonstrated QAD improvement; QAD 1/2 vs PTQ 2/2.
- **Extraction/RAG:** QAD 1/2 vs PTQ 0/2, but too small for a deployment claim.

### Coding

Twenty isolated sandbox executions per primary quant. Each produced 4/20 execution successes. The suite exposed brittle single-code-block compliance and supports Liquid's warning that 2.6B is not for agentic coding. Coding is a poor fit regardless of the observed QAD quantization change.

### Native Tools

All four compared quants passed the five deterministic local schema cases: 5/5. QAD did not improve this already-saturated simple suite. Nested-object, tool-result continuation, and recovery after an error remain unverified.

### Context

All three finalists allocated and prefixed prompts through 127,777 actual tokens. QAD and PTQ retrieved the beginning needle at approximately 3.9K and 8.0K tokens, but neither produced a final answer above 16K within a 256-token generation budget. **Useful long-context behavior is not established beyond 8K for QAD/PTQ.**

### Stability

The loopback QAD server completed 1,808.7 seconds (30m 8.7s), 175 varied requests, zero request errors. It shut down cleanly and GPU allocation returned to desktop baseline. No Xid/reset/GSP/channel-failure entries.

### Role Classification

**Supported roles:**
- Always-loaded router/extraction/tool helper with schema validation and evidence checks
- Ultra-fast sidecar (when 1.59 GB is the hard size target)

**Not supported:**
- Primary assistant
- Long-context retriever
- Coding agent

### Claim Classifications

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

### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/eval-lfm2.5-2.6b
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/labs

### Reproduction

Direct link to canonical reproduction material: [eval-lfm2.5-2.6b/](https://github.com/WumboLabs/eval-lfm2.5-2.6b)

This Lab Record is a summary; the canonical repo is the source of truth.
