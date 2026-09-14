# Qwen3.8-27B Inventory

Inspected: 2026-08-14

## Native model

- Repository: Qwen/Qwen3.8-27B
- Revision: 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0
- License: Apache-2.0
- Transformers architecture: Qwen3_5ForConditionalGeneration (`model_type=qwen3_5`)
- Task: image-text-to-text; text-only use is the controlled evaluation baseline
- Parameters: 27,781,427,952 BF16
- Repository storage: 55,575,816,096 bytes
- Native weights: 18 safetensors shards
- Tokenizer: repository tokenizer/config at the same revision; chat template exposes `enable_thinking`, `reasoning_effort` (`xhigh`, `medium`, `low`), and `preserve_thinking`
- Native context: 262,144 tokens; the hosted-service 1M extension claim is not treated as local-runtime evidence
- Language model: 64 layers; hidden size 5120; hybrid Gated DeltaNet/Gated Attention layout; MTP trained
- Official capabilities relevant here: coding, agent execution, flexible thinking control, vision-language support. Upstream benchmark claims are not host measurements.

## Official FP8 representation

- Repository: Qwen/Qwen3.8-27B-FP8
- Revision: 017b9c7af6b5689d5dd426a76e0bc077eb5ca20a
- Quantization: FP8 E4M3 for 24,699,207,680 parameters; 3,082,220,272 BF16 parameters remain unconverted
- Repository storage: 30,879,676,248 bytes
- vLLM viability is borderline and must be established by real construction with text-only mode and CPU offload; file size alone is not fit evidence.

## GGUF source

- Repository: unsloth/Qwen3.8-27B-GGUF
- Revision: fdd03b8bbd279c1694563650e79d85a2373d9934
- GGUF architecture: qwen35
- Context metadata: 262,144
- Quantization source advertises an importance matrix and a Qwen3.8 chat template.

## Selected practical matrix

| Quant | Bytes | Reason selected |
|---|---:|---|
| Q6_K | 22,884,408,288 | Highest conventional quant reasonably hybrid-runnable within host RAM/VRAM |
| Q5_K_M | 19,834,055,648 | High-quality conventional hybrid candidate |
| Q4_K_M | 17,106,775,008 | Common quality/size hybrid reference |
| IQ4_NL | 16,337,628,128 | Importance-matrix 4-bit candidate |
| IQ4_XS | 15,705,861,088 | Smaller importance-matrix 4-bit candidate |
| Q3_K_M | 13,818,690,528 | Reinspection addition; strongest plausible near-VRAM 3-bit conventional quant |
| Q3_K_S | 12,574,489,568 | Prior-audit candidate near physical VRAM size |
| UD-IQ3_XXS | 11,913,559,104 | Ultra-dynamic 3-bit full-offload candidate |
| UD-IQ2_M | 10,319,907,904 | Higher-quality ultra-low-bit full-offload candidate |
| UD-IQ2_XXS | 9,010,048,064 | Smallest practical full-offload candidate |

## Documented exclusions

- BF16/F16 GGUF: roughly 54.7 GB, beyond physical RAM plus usable VRAM once runtime allocations are included; native BF16 is inventoried for vLLM admission instead.
- Q8_0 (29,047,086,048 B) and UD-Q8_K_XL (31,457,991,680 B): insufficient practical host-memory margin; Q6_K is the bounded highest-quality hybrid test.
- Q4_0/Q4_1/Q4_K_S and Q5_K_S: lower-value duplicates beside K_M/IQ variants at similar sizes.
- UD-Q*_K_XL variants: redundant size/quality points beside the selected conventional and IQ matrix; several are larger than corresponding selected candidates.
- BF16/F16 mmproj: excluded because the controlled matrix is explicitly text-only; vision is a model capability, not part of this evaluation baseline.

Every selected file must still load and generate before receiving a viability classification.
