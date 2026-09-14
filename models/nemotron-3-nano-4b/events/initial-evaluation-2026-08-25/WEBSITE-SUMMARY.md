### Identity

| Field | Value |
|---|---|
| Model | Nemotron 3 Nano 4B |
| Producer | NVIDIA |
| Evaluated artifact | NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf |
| Source revision | `ba223d14e45525f7fae81db77ea8cabeb2fc6c25` |
| SHA-256 | `be5d9a656a51922f24f1f09a759cebb694e1f5d9728bf0ef9f8c972c5a0b5ef2` |
| Evaluation date | 2026-08-25 |
| Protocol | WELP, first deliberate WELP validation campaign |
| Highest phase reached | Phase 3 (gate decision) |
| Campaign classification | PARTIAL_PROTOCOL_DEVELOPMENT |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| CPU | AMD Ryzen 7 9800X3D |
| OS | Fedora Linux 44, kernel 7.1.9 |
| Driver / CUDA | NVIDIA 610.57.04 |
| Runtime | llama.cpp b10449 (commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`) |

### Headline Verdict

**PROTOCOL_BLOCKED at Phase 3 gate decision.**

The model showed no failing behavior. WELP's documented material contains no Phase 3 advancement threshold, so no deterministic PASS/FAIL could be produced without inventing a rule, which the campaign forbids.

This campaign contributed to protocol development. It is **not a complete WELP capability review**. Do not present it as equivalent in evaluation depth to Qwen3.8-27B.

### Performance

| Metric | Result |
|---|---|
| Decode | ~178 tok/s mean (512-token generations) |
| Prefill | ~6,500 tok/s at ~2,600-token prompts |
| TTFT (short prompt) | ~30 ms |
| llama-bench (p512/n128) | ~180 tok/s out, 65 ms TTFT |

### Phases Reached

| Phase | Gate | Outcome |
|---|---|---|
| 0 Provenance | — | PASS |
| 1 Admission (hard) | PASS | Loads; full GPU residency verified; clean inference/termination |
| 2 Performance | PASS* | Criterion interpreted (F-02) |
| 3 Practical Viability | **PROTOCOL_BLOCKED** | 12/12 screen but protocol defines no advancement threshold (F-01) |
| 4–10, OMP-21B | NOT RUN | Stopped per campaign rule |

### Practical Viability Evidence

12 tasks across instruction following, strict output, extraction, structured JSON, technical knowledge, false-premise rejection, uncertainty behavior, simple reasoning: **12/12**, mechanical scoring. This is screening evidence, not a gate pass.

### Reasoning Findings

Bounded observations only (dedicated module not reached): default mode emits `<think>` traces then answers; `enable_thinking=false` yields direct correct answers. Producer's reasoning-off benchmark framing is operationally reproducible on this runtime.

### Role Classification

**No deployment recommendation is supported by this evidence.**

What the reached phases establish:
- The model loaded cleanly and served stably across the tested phases
- Performance was measured
- The Phase-3 screening result was measured: 12/12
- OMP connectivity was demonstrated
- The reasoning-control mechanism was boundedly observed

**Explicitly NOT TESTED:** reliability, capability modules, context quality, variance, soak, and agent capability.

### Important Limitations

- **Single-seed practical screen.** Reliability, context quality, coding, tools, agent behavior, and soak were NOT TESTED.
- **Context wording:** the server was configured with a 32K context window and inference ran within it. Useful 32K context behavior was **not evaluated**.
- **No LLMGauge Agent Harness result.** LLMGauge was never invoked.
- **Protocol findings:** this campaign identified 9 protocol ambiguities (F-01 through F-09) and 4 undocumented decisions required. These are documented in the canonical repo.
- Results must not be generalized to a model review.

### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/eval-nemotron-3-nano-4b
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/labs
- **LocalMaxxing:** Speed run measured locally (~180 tok/s); submission blocked on missing credentials. No benchmark suite submissions.

### Reproduction

Direct link to canonical reproduction material: [eval-nemotron-3-nano-4b/](https://github.com/WumboLabs/eval-nemotron-3-nano-4b)

This Lab Record is a summary; the canonical repo is the source of truth.
