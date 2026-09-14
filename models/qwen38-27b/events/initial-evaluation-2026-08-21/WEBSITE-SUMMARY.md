### Identity

| Field | Value |
|---|---|
| Model | Qwen 3.8 27B |
| Producer | Alibaba (Qwen team); quantized by Unsloth |
| Evaluated artifact | Unsloth Qwen3.8-27B UD-Q2_K_XL |
| Source revision | `27af057ecb382ddfea5d12837360a8980560e3ed` |
| SHA-256 | `fd4730dd8aad070517978752b63d530aeb1740d2283cab9fa24f1e404032ddb0` |
| Evaluation date | 2026-08-14 through 2026-08-21 |
| Protocol | WELP end-to-end (frozen snapshot `welp-next-snapshot-2026-08-25-end-to-end`) |
| Highest phase reached | Full campaign (Phase 10+) |
| Campaign classification | COMPLETED_DEEP_EVALUATION |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| VRAM | 12,227 MiB physical |
| GPU power | 250 W stock reference limit |
| CPU | AMD Ryzen 7 9800X3D, 8 cores / 16 threads |
| RAM | ~32 GiB DDR5 (~30 GiB usable) |
| OS | Fedora Linux 44, kernel 7.1.8-200.fc44.x86_64 |
| Driver / CUDA | NVIDIA 610.57.04 / CUDA 13.3 |
| Runtime | llama.cpp b10449 (commit `0d9ceae1e38291035605613ab41a8f5e693d6fcd`) |

The RTX 5070 also drove the Fedora/Hyprland desktop during testing. Practical free VRAM was therefore lower than raw physical capacity; this is representative workstation evidence, not benchmark isolation.

### Headline Verdict

**NOT READY AS DAILY DRIVER**

Qwen3.8-27B UD-Q2_K_XL is stable in the tested runtime, practically fast, unusually strong at coding, capable of useful bounded 64K context, and substantially improved by bounded reasoning on hard tasks.

But the frozen primary reliability corpus classified 19.0% of executions as hallucinations; the frozen strict campaign had 21.2% failures; false-premise resistance was weak; and only 5/50 full native-tool sequences met the strict contract.

**Recommended classification: Strong reviewed local coding/technical assistant.**

The evidence does not support use as an unattended agent, source of unverified technical facts, autonomous system administrator, autonomous Git operator, unsupervised native-tool agent, or fail-closed structured-output engine.

### Performance

| Configuration | Decode tok/s | Prefill tok/s | Context | Notes |
|---|---|---|---|---|
| Quality/balance (Q4_K_M, 38 GPU layers, 8K) | 6.4–6.8 | ~880 | 8K | 4.85–5.0/5 coding score; 467 MiB min headroom |
| Speed (UD-IQ2_M, full GPU, 4K) | 42.0–42.9 | — | 4K | 362/5 manual avg; task-dependent quality |
| Agent-safe (UD-IQ2_XXS, full GPU, 12K) | — | — | 12K | Bounded one-file OMP pass |
| Large context (Q2_K_XL, 64K Q4/Q4) | ~30 | ~704 | 64K | Low-headroom reviewed work |

Native MTP at 8K: ~66 tok/s (1.47x speedup over baseline ~45 tok/s, ~75% acceptance).

### Capabilities

#### Coding
**Strongest supported domain.** Fresh executable coding passed 28/30 in disposable sandboxes with no network, minimal devices, resource limits, and no host modification. Coding recovery passed 36/40 changed-constraint revisions. This supports Qwen3.8-27B as a strong **reviewed** local coding assistant, not a hallucination-free coding system.

#### Reasoning
Tested, not enabled by default. On the fresh hard subset, reasoning on passed 9/10 versus 4/10 for the matched reasoning-off control. Use the reasoning profile for difficult math, logic, code diagnosis, evidence synthesis, and constrained planning. Leave it off for ordinary factual questions, strict interfaces, native tools, and routine work.

#### Strict Interfaces
The frozen strict campaign passed 197/250 (78.8%) and failed 53/250 (21.2%) across exact strings, JSON, extraction, enums, CSV, and word limits. Do not rely on one-shot strict responses; parse and mechanically validate structured output.

#### Native Tools
Only 5/50 full native-tool sequences satisfied the complete frozen end-to-end contract. Tool selection and argument structure performed better than the strict execution/recovery sequence. Native tools require deterministic execution, schema validation, result validation, and external supervision.

#### Long Context
Fresh baseline Q4 work passed bounded retrieval, synthesis, and instruction/code-retention probes at 16K, 32K, and 64K. The first filled 64K prompt contained approximately 64,275 tokens; first prefill took 91.24 s at 704.5 prompt tok/s. This demonstrates bounded 64K retrieval on this configuration. It does not establish that arbitrary 64K workloads are reliable.

#### Reliability
Primary reliability statistics covered 685 evaluated task executions:

| Classification | Count | Rate |
|---|---|---|
| CLEAN_PASS | 414 | 60.4% |
| MATERIAL_DEFECT | 43 | 6.3% |
| HALLUCINATION | 130 | 19.0% |
| STRUCTURAL_FAILURE | 98 | 14.3% |

False-premise resistance was the decisive readiness failure: hallucination-category runs were 67/150 CLEAN_PASS and 83/150 HALLUCINATION; sycophancy/false-premise runs were 28/75 CLEAN_PASS and 47/75 HALLUCINATION.

#### Stability
A two-hour balanced-profile soak completed 225/225 HTTP successes and 46/46 exact sentinels. Mean generation was 44.81 tok/s. VRAM started/ended/peaked at 10,340/10,248/10,342 MiB; peak soak temperature was 65 C. No new Xid, reset-required state, GSP failure, or display-engine collapse appeared during the controlled final campaign.

### Role Classification

**Supported roles:**
- Reviewed local coding assistant
- Technical assistant (with verification)
- Bounded reasoning assistant (reasoning on, difficult tasks only)

**Guarded roles:**
- Drafting and editing (review required)
- 64K context retrieval (low headroom, reviewed only)

**Unsupported / not ready:**
- Unguarded daily driver
- Unattended autonomous agent
- Source of unverified technical facts
- Autonomous system administrator
- Autonomous Git operator
- Unsupervised native-tool agent
- Fail-closed structured-output engine

### Important Limitations

- **No LLMGauge Agent Harness result exists.** This is a coverage limit, not a replacement classification.
- **Autonomy evidence is bounded:** the OMP follow-up completed a deliberately limited one-file inspect/edit/test/report loop. It does not establish broad autonomous-agent suitability.
- **Runtime safety boundary:** the evaluated vLLM configuration exhausted host memory during an earlier admission attempt. This is an operational deployment boundary, not a model-quality result.
- **Useful context not established beyond 8K for the fast quants.**
- Results apply to the pinned artifacts, llama.cpp b10449 runtime, Fedora 44 workstation condition, RTX 5070 12GB configuration, stated contexts, and frozen WumboLabs probes. They do not establish producer accuracy claims, cloud behavior, broad hardware representativeness, or universal model quality.

### Evidence Links

- **Canonical evaluation repo (historical llama.cpp profile):** https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/labs
- **LocalMaxxing:** APPROVED speed-test submissions (`cmt3jngze0njfmv0133xpneeu` BALANCED 16K; `cmt3jp2cn0njpmv01t5u8m6wd` FAST 8K MTP) + benchmark suite APPROVED/PUBLIC; ref-quant `cmsv68xl3085ims01w8aeacig`

### Reproduction

Direct link to canonical reproduction material: [eval-qwen3.8-27b-llamacpp/reports/](https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp/tree/main/reports)

Full reproduction instructions, manifests, and checksums are published in the canonical repository. This Lab Record is a summary; the canonical repo is the source of truth.

> **Provenance note (2026-09-12):** this evidence was originally published at
> [WumboLabs/eval-qwen3.8-27b](https://github.com/WumboLabs/eval-qwen3.8-27b)
> (evidence commit `54b14b30e3779f15486c3785222647324459dcf5`). It moved
> byte-identical to the canonical historical-profile repository
> ([eval-qwen3.8-27b-llamacpp](https://github.com/WumboLabs/eval-qwen3.8-27b-llamacpp))
> by the model/profile/event publication-identity milestone; the original
> repository is preserved unchanged as a historical archive.
