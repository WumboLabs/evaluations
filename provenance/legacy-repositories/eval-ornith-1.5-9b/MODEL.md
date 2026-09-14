# Model: Ornith-1.5-9B

- Upstream: `ornith-ai/Ornith-1.5-9B` @ revision `489cb97981b8654bcfcf30ce1f94ed1b62e07b53` (MIT)
- Architecture: `qwen3_5` — 9B dense (hidden 4096, 32 layers + 1 nextn/MTP layer,
  GQA 16q/4kv, head_dim 256, ffn 12288), hybrid attention (linear/SSM ×3 then
  full_attention, interval 4), max_position_embeddings 262144, vocab 248320
- Reasoning mechanism: `<|think|>…<|im_end|>` span in assistant turn; controlled by
  chat-template kwarg `enable_thinking` (template default true). Campaign served with
  reasoning OFF (`--reasoning off` + per-request `enable_thinking=false`).
- Tool calling: XML function tags emitted inside content; no native server-side
  tool_calls parsing.

## Evaluated artifact

| Field | Value |
|---|---|
| File | `Ornith-1.5-9B-Q4_K_M.gguf` |
| Bytes | 5,780,090,816 |
| sha256 | `70c112196e0b7023803c9762752e46d29e612a92c83f995bc3ba1ceb07e8fab6` |
| Quant | Q4_K_M (file_type 15, quantization_version 2) |
| Chat template | embedded == `chat_template.jinja` (sha256-identical), `9dd2fbd270feaa1fbef2d4f634d7887c9c506e3bde140f8e7351c8944e8fd235` |
| Vision | `mmproj-Ornith-1.5-9B-BF16.gguf` downloaded but NOT evaluated (text+agentic scope) |

GGUF metadata: `general.architecture=qwen35`, `context_length=262144`,
`block_count=33`, `nextn_predict_layers=1`, `eos_token_id=248046`.

## Serving profile (frozen)

llama.cpp b10449 @ commit `0d9ceae1`, binary sha256 `b3a740b8…`;
ctx 32768, parallel 1, `-ngl 99`, flash-attn on, batch 2048 / ubatch 512,
fit off, no speculation, `--reasoning off`, single instance.

## Producer-claim status (reviewed @ 489cb979)

- 9B identity / open weights: REPRODUCED_IDENTITY
- 256K context: PARTIALLY_REPRODUCED — measured useful context 24576 under this
  hardware/serving profile
- coding / native tools / reasoning-first: PARTIALLY_REPRODUCED (see
  `summaries/producer_claims.json`)
- vendor benchmark tables: PHYSICALLY_UNTESTABLE on this rig
