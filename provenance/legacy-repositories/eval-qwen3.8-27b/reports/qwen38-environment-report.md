# Qwen3.8-27B Environment Report

Date: 2026-08-14
Host: WumboJetsII
Outcome: **FAIL — complete evaluation not admitted**

## Admission

The environment audit completed without modifying either repository. The requested complete workflow is blocked before model acquisition because no usable vLLM installation, executable, container image, cached tool, or local environment exists. LLMGauge treats vLLM as an externally managed runtime. Installing or constructing that runtime would change the host and is not authorized by this testing-only handoff or the repository policy.

Per the fail-closed policy and the instruction to stop on a blocking issue, no model was downloaded and no partial llama.cpp, LLMGauge, or OMP evaluation was launched.

## Repository State

| Repository | Branch | HEAD | State |
|---|---|---|---|
| LLMGauge | `main` | `d5d8df5fde409c0cc61c22dfb1f704be1bdbe1b5` | Clean |
| llama.cpp | `master` | `74ade52741203e5c8f81eaf06a96cb1cfe15f2a3` | Clean |

No branches, commits, staging, pushes, or repository changes were made.

## System

| Field | Observed value |
|---|---|
| Distribution | Fedora 44 |
| Kernel | `7.1.8-200.fc44.x86_64` |
| CPU | AMD Ryzen 7 9800X3D, 8 cores / 16 threads |
| RAM | 32,695,726,080 bytes |
| Swap | 8,589,930,496 bytes |
| Free storage | Approximately 1.2 TiB at audit |

## GPU

| Field | Observed value |
|---|---|
| GPU | NVIDIA GeForce RTX 5070 |
| Driver | `610.57.04` |
| CUDA reported by driver/toolkit | `13.3` |
| VRAM total (`nvidia-smi`) | 12,227 MiB |
| VRAM free at audit (`nvidia-smi`) | 10,781 MiB |
| VRAM visible to llama.cpp | 11,810 MiB total / 10,610 MiB free |

## llama.cpp

| Field | Observed value |
|---|---|
| Revision | `74ade52741203e5c8f81eaf06a96cb1cfe15f2a3` |
| Build/version | `v9672`, Release |
| Compiler | GNU 15.3.1 |
| CUDA architecture | SM120 |
| Relevant build flags | `GGML_CUDA=ON`, `GGML_NATIVE=ON` |
| `llama-cli` | Present; reports the v9672 CUDA build |
| `llama-server` | Present; reports the v9672 CUDA build |

## LLMGauge

| Field | Observed value |
|---|---|
| Version | `0.72.0` |
| Repository state | Clean |
| Doctor | Passed |
| Doctor checks | Package, runner, six suites, configuration, `llama-cli`, eight profiles, and `nvidia-smi` recognized |

## OMP

| Field | Observed value |
|---|---|
| Version | `17.3.3` |
| Configuration | Existing global configuration inspected without retaining secret values |
| Provider/runtime state | Cloud-default `openai-codex` roles; no local Qwen3.8 model provider configured |

## Model Availability Audit

No Qwen3.8 model files were present locally. The following upstream artifacts were identified but not downloaded:

- Original weights: `Qwen/Qwen3.8-27B`
- GGUF ladder: `unsloth/Qwen3.8-27B-GGUF`

Candidate GGUF inventory from upstream metadata:

| Quantization | Upstream size (bytes) | Acquired | Tested |
|---|---:|---|---|
| Q6_K | 22,884,408,288 | No | No |
| Q5_K_M | 19,834,055,648 | No | No |
| Q4_K_M | 17,106,775,008 | No | No |
| IQ4_NL | 16,337,628,128 | No | No |
| IQ4_XS | 15,705,861,088 | No | No |
| Q3_K_S | 12,574,489,568 | No | No |
| UD-IQ3_XXS | 11,913,559,104 | No | No |
| UD-IQ2_M | 10,319,907,904 | No | No |
| UD-IQ2_XXS | 9,010,048,064 | No | No |

These sizes are inventory evidence only. They do not establish load success, fit, context viability, or inference quality.

## Blocking vLLM Capability

Audit results were negative for all locally plausible runtime locations:

- no `vllm` executable on `PATH`;
- no importable vLLM Python package;
- no local vLLM container image;
- no vLLM uv tool or usable cached environment;
- no repository-local vLLM virtual environment.

Historical local logs referenced vLLM 0.25.1, but that environment no longer exists. Historical evidence is not a usable runtime and was not treated as one.

LLMGauge's accepted contract keeps vLLM externally operator-managed. Creating a new runtime would require an installation/host-change milestone and compatibility validation for CUDA 13.3, SM120, and Qwen3.8. That work is outside this testing-only authorization.

## Smallest Unblock

A human/operator must provide an existing isolated vLLM environment compatible with CUDA 13.3, NVIDIA SM120, and Qwen3.8-27B, or explicitly authorize a separate environment-admission/install milestone. After that capability exists, issue a fresh full-evaluation handoff. The complete evaluation must restart from model acquisition; no quant has yet been claimed to fit or work.
