# Qwen3.8-27B vLLM Representation Admission

Date: 2026-08-14
Runtime: vLLM 0.27.1, PyTorch 2.13.0+cu130, RTX 5070 SM120
Verdict: PASS for one bounded real construction attempt

## Architecture support

The installed vLLM registry directly implements `Qwen3_5ForConditionalGeneration` in `vllm/model_executor/models/qwen3_5.py` and registers it in `registry.py`. The installed configuration layer also contains a Qwen3.5 verifier. The official vLLM recipe states Qwen3.8-27B text serving is verified with vLLM 0.17.0 or newer. The admitted 0.27.1 runtime exceeds that minimum.

## Representation decision

Selected: `Inferact/Qwen3.8-27B-NVFP4` at revision `6128240ebaf4eaa7bad2b3d1c72c37d677c5f462`.

- Repository storage: 26,394,058,632 bytes (24.58 GiB).
- Safetensors parameter accounting: 7,480,996,592 BF16 plus 10,150,215,680 U8 storage elements; total represented parameters 17,631,212,272 in the repository metadata.
- Quantization config: ModelOpt/compressed-tensors style 4-bit weights with extensive unquantized hybrid linear-attention components.
- Official vLLM recipe identifies this checkpoint as the Blackwell low-latency TP1 representation and explicitly states 24.6 GiB model memory on a sufficiently large Blackwell GPU.
- WumboJetsII has only 12 GB VRAM, so the recipe's bare launch cannot fit. A real attempt is admitted only with text-only mode, one sequence, 4K context, eager execution, bounded CPU offload, and loopback binding.
- CPU offload is plausible but borderline: roughly 13–15 GiB of model storage must remain in host memory, plus runtime state, within 30.5 GiB physical RAM. This is not fit evidence until construction and generation succeed.

Alternate inspected representations:

- Native BF16 `Qwen/Qwen3.8-27B` revision `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`: 55,575,816,096 bytes; no plausible single-GPU/offload path on this host.
- Official FP8 `Qwen/Qwen3.8-27B-FP8` revision `017b9c7af6b5689d5dd426a76e0bc077eb5ca20a`: 30,879,676,248 bytes; official recipe targets TP4. Its download was stopped after the smaller Blackwell-native TP1 NVFP4 representation was found. FP8 metadata is preserved; no FP8 construction claim is made.
- GGUF is not selected for vLLM because the current official Qwen/vLLM recipe identifies Transformer NVFP4/FP8 representations and the llama.cpp matrix already evaluates GGUF directly.

## Planned launch boundary

- Host: 127.0.0.1 only
- Port: 8012
- Served model: qwen38-27b-nvfp4
- Max model length: 4096
- Tensor parallel: 1
- Max sequences: 1
- GPU memory utilization: bounded below full device allocation
- CPU offload: bounded and recorded
- Language-model-only mode
- Eager execution initially to reduce CUDA graph memory
- Reasoning parser: qwen3
- Tool parser for agent run: qwen3_coder or the exact Qwen3.8-compatible parser accepted by the server
- Required environment: `VLLM_NO_USAGE_STATS=1`, `HF_HUB_DISABLE_TELEMETRY=1`, `VLLM_USE_FLASHINFER_SAMPLER=0`

Unsupported construction, OOM, impractical offload speed, or incomplete generation is a model/runtime result, not a vLLM environment-admission failure.
