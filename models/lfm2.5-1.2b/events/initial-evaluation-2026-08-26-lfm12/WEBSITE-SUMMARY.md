### Identity

| Field | Value |
|---|---|
| Model | LFM2.5 1.2B-Instruct |
| Producer | Liquid AI |
| Evaluated artifact | QAD Q4_0 from `LiquidAI/LFM2.5-1.2B-Instruct-GGUF` @ `67672651…3615b` |
| SHA-256 | `bb741ebb106d543e9de114b843a3d3d73d51c74b5801e69da2abde821a0cb3e1` |
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
| OS | Fedora Linux 44, kernel 7.1.9-200.fc44 |
| Driver / CUDA | NVIDIA 610.57.04 |
| Runtime | llama.cpp b10449 (commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`) |

### Headline Verdict

**QAD Q4_0 is the best deployment quant of the five-way matrix and the best always-resident sidecar candidate measured so far in this model family, but the campaign did not reproduce Liquid's hallucination or aggregate-retention story: at 1.2B every quant including BF16 fabricates confidently on invented subjects (0/12), and QAD's fixed-corpus perplexity advantage over PTQ inverted.**

QAD kept exactly Q4_0 memory and within-variance Q4_0 speed, scored best of all quants on the 52-task practical suite (31/52), and is faster than both K-quant controls (~+6% decode). Useful context is <=8K for every candidate.

### Performance

| Quant | Prompt tok/s | Decode tok/s | TTFT ms |
|---|---|---|---|
| BF16 | 3383 | 232.6 | 9.7 |
| PTQ Q4_0 | 6944 | 592.3 | 4.8 |
| QAD Q4_0 | 6600 | 585.6 | 4.9 |
| Q4_K_M | 6054 | 554.4 | 5.5 |
| UD-Q4_K_XL | 5947 | 551.0 | 5.3 |
| Q5_K_M | 5777 | 510.7 | 6.0 |

Deltas: QAD -1.14% vs PTQ decode (within variance), +5.63% vs Liquid Q4_K_M, +6.28% vs UD-Q4_K_XL.

### Fidelity

`llama-perplexity` on fixed local repeated corpora:

| Quant | Natural PPL | Code PPL |
|---|---|---|
| BF16 | 1.5235 | 1.0514 |
| PTQ Q4_0 | 1.2454 | 1.0378 |
| QAD Q4_0 | 1.3941 | 1.0472 |
| Q4_K_M | 1.3176 | 1.0457 |

**The 2.6B finding inverted: at 1.2B PTQ beats QAD on natural text.** The repeated-corpus pathology persists and worsens — BF16 is worse than most quants on natural text, so no BF16-relative percentage from this corpus is valid.

### Practical Capability

52 unique mechanically-scored tasks, same set for all six models, seed 42:

| Model | Instr | Extr | Struct | Halluc | Linux | Uncert | Total |
|---|---|---|---|---|---|---|---|
| BF16 | 8/10 | 4/8 | 12/12 | 0/12 | 4/6 | 4/4 | 32/52 |
| QAD Q4_0 | 8/10 | 4/8 | 11/12 | 0/12 | 4/6 | 4/4 | 31/52 |
| PTQ Q4_0 | 8/10 | 4/8 | 10/12 | 0/12 | 4/6 | 4/4 | 30/52 |
| Q5_K_M | 8/10 | 4/8 | 10/12 | 0/12 | 3/6 | 4/4 | 29/52 |
| Q4_K_M | 8/10 | 3/8 | 10/12 | 0/12 | 3/6 | 3/4 | 27/52 |
| UD-Q4_K_XL | 8/10 | 3/8 | 10/12 | 0/12 | 3/6 | 3/4 | 27/52 |

### Hallucination Resistance

Twelve invented-subject probes (packages, flags, APIs, files, systemd units, sysctls, Kconfig options): **every model, including BF16, fabricated confident detailed explanations — 0/12 across the entire matrix.** This is a model-family property at 1.2B scale, not a quantization effect. QAD shows no improvement.

### Structured Output

Mechanical JSON/schema scoring: QAD 11/12, PTQ/Q4_K_M/Q5_K_M/UD 10/12, BF16 12/12. A small QAD-over-PTQ edge appeared (+1).

### Native Tools

v1 (exact five-case contract): saturated — 5/5 for BF16, PTQ, QAD, Q4_K_M, Q5_K_M; UD-Q4_K_XL 4/5.

v2 (ten harder cases): complete multi-turn tool sequences succeed only half the time even for BF16. QAD ties its controls.

### Context

Three-needle retrieval at 4K/8K/16K/32K: at >=16K every model degenerates into repeating filler text. **Useful context ceiling: 8K for all finalists.**

### Stability

The loopback-only QAD soak completed 1,805.9s (30m 6s), 180 varied requests, zero request errors. Peak power 33.6 W, max temperature 52 C. Zero Xid/reset/GSP/channel events.

### Role Classification

**GOOD FIT:** always-loaded router, classifier, simple tool selector.

**USABLE WITH GUARDRAILS:** extraction helper, RAG helper (<=8K), structured formatter, conversational sidecar.

**POOR FIT:** coding helper, primary assistant, autonomous agent.

### 1.2B vs 2.6B Comparison

| Dimension | 2.6B QAD | 1.2B QAD | Delta |
|---|---|---|---|
| GGUF bytes | 1,593,894,944 | 695,755,488 | -898 MB |
| Peak VRAM | 2404 MiB | 1534 MiB | -870 MiB |
| Decode tok/s | 282.5 | 585.6 | x2.07 |
| Useful context | <=8K | <=8K | equal |
| Hallucination resistance | no QAD effect shown | absent at model level | worse |

The 1.2B creates a genuinely better always-resident micro-sidecar niche (twice as fast, two-thirds the VRAM) but is a strictly weaker knowledge/extraction assistant.

### Claim Classifications

| Claim | Classification |
|---|---|
| QAD keeps Q4_0 memory | REPRODUCED |
| QAD keeps Q4_0 speed | REPRODUCED |
| 97.4% BF16 aggregate retention | INCONCLUSIVE |
| Matches Liquid Q4_K_M | PARTIALLY_REPRODUCED |
| Matches Unsloth UD-Q4_K_XL | PARTIALLY_REPRODUCED |
| Meaningful recovery of PTQ loss | PARTIALLY_REPRODUCED |
| Improves hallucination resistance | NOT_REPRODUCED |

### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/eval-lfm2.5-1.2b
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/labs

### Reproduction

Direct link to canonical reproduction material: [eval-lfm2.5-1.2b/](https://github.com/WumboLabs/eval-lfm2.5-1.2b)

This Lab Record is a summary; the canonical repo is the source of truth.
