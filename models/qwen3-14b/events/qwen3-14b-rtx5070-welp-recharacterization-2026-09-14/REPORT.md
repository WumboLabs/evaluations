# Qwen3-14B — current-WELP recharacterization on RTX 5070 12 GB (llama.cpp, Q4_K_M, q8_0 KV)

- **Event ID:** `qwen3-14b-rtx5070-welp-recharacterization-2026-09-14`
- **Event date:** 2026-09-14 (execution); recorded 2026-09-15 (closeout publication)
- **Model:** Qwen3-14B (`Qwen/Qwen3-14B`, Alibaba Qwen team)
- **Profile:** `qwen3-14b-llamacpp-q4km-q8kv` (current)
- **Hardware:** WumboJetsII — NVIDIA GeForce RTX 5070 12 GB (12,227 MiB total / 11,813 MiB addressable)
- **Outcome:** **PASS — recharacterized under current WELP**
- **Classification:** **READY_WITH_GUARDRAILS**
- **Scope:** performance, practical viability (quality screen), capabilities (reasoning / coding / tools), reliability, context envelope with useful-context validation, LocalMaxxing disposition
- **Protocol:** current WELP DRAFT (`WumboLabs/welp`), current context-scaling DRAFT methodology; campaign snapshot `welp-next-snapshot-2026-09-14-qwen3-14b-recharacterization`

All measurements below are MEASURED on the listed stack unless labeled otherwise.
This report is the public-safe scientific record of the campaign; the retained
local campaign bundle (under the WumboLabs research tree,
`research/model-evaluations/qwen3-14b/qwen3-14b-rtx5070-welp-recharacterization-2026-09-14/`)
governs on any conflict.

## 1. Tested artifact and provenance

- Artifact: `Qwen3-14B-Q4_K_M.gguf` (unsloth/Qwen3-14B-GGUF lineage), **9,001,753,376 bytes**
- SHA-256: `712c0791d5124d3dd6d1e4968de1201207afeae49c6e10fbeb9c58fe00c58555`
  (recomputed 2026-09-14 at campaign start and re-verified 2026-09-15 before the
  useful-context completion)
- Downloaded 2026-05-08T22:13:02Z with in-place Hugging Face download provenance;
  the recorded download digest equals the recomputed SHA-256 and the byte
  fingerprint in the historical registry record.
- Uniqueness: current public Q4_K_M artifacts (unsloth, Qwen, bartowski HEADs,
  checked 2026-09-14) all carry different bytes — the tested file is the unique
  surviving exact historical artifact; a bit-exact re-download is impossible.

## 2. Official source claims (EXTERNAL_REPORTED, revision-pinned)

- Repository `Qwen/Qwen3-14B`, card `README.md` + `config.json`, exact revision
  **`40c069824f4251a91eefaf281ebe4c544efd3e18`** (repo last commit 2025-07-26,
  predating the 2026-09-14 observation, so card/config content observed 2026-09-14
  at HEAD equals this revision; retrieved 2026-09-15).
- Native context **32,768** (`n_ctx_train 32768` corroborated by runtime GGUF
  metadata, MEASURED); `max_position_embeddings=40,960` (32,768 output + 8,192
  prompt allocation; the card's authoritative native-context claim is 32,768).
- Official extension: YaRN factor 4.0 → **131,072** (card-validated by Qwen;
  llama.cpp flags `--rope-scaling yarn --rope-scale 4 --yarn-orig-ctx 32768`;
  static-YaRN short-text caveat noted on card).
- Architecture (config at pinned revision): dense `Qwen3ForCausalLM`, 14.8B
  parameters (13.2B non-embedding), 40 layers, GQA 40 Q / 8 KV heads, head_dim
  128, hidden 5,120, vocab 151,936, rope_theta 1e6, bf16. Multimodal: none
  (text-only). Tool calling: documented. Thinking/non-thinking hybrid with
  `enable_thinking` template switch.
- Recommended sampling: thinking 0.6/0.95/20 (greedy discouraged); non-thinking
  0.7/0.8/20. License Apache-2.0.

## 3. Runtime and serving profile

- llama.cpp **b9672** (commit `74ade5274`, tag `wumbo-known-good-b9672-2026-06-16`),
  CUDA SM120 build, ggml 0.15.1, server surface, `-np 1`. Driver 610.57.04.
- Canonical profile (`qwen3-14b-llamacpp-q4km-q8kv`): full GPU residency
  (`-ngl 999`, all 40 transformer layers GPU-resident, no hidden offload; CPU
  embedding lookup only), context **32,768** (native maximum; default = guarded),
  KV cache **q8_0 K and V** with flash attention, batch 2048/512,
  reasoning baseline **OFF** (server-side `enable_thinking=false`, verified by
  rendered empty `<think>` block and absence of `reasoning_content`).
- KV rationale: f16 KV (160 KiB/token) cannot reach the native 32,768 maximum on
  12 GB (2026-07-15 measured OOM at 5,120 MiB KV plus arithmetic); q8_0
  (80 KiB/token) fits with ~0.92 GiB reserve. All quality/reliability/capability
  evidence below was measured ON this exact configuration.
- GPU idle-verified between phases; one heavy CUDA workload at a time; no
  CUDA/Xid errors in any completed run; no Nsight Systems traces.

## 4. Performance (MEASURED)

- `llama-bench` (5 reps, canonical KV/FA flags): **pp512 2,719.17 ± 29.51 tok/s;
  tg128 65.95 ± 0.03 tok/s**.
- Server, canonical config: short-prompt TTFT ≈ 34–51 ms; ~4.1K-token prefill
  ≈ 2,470 tok/s; decode ≈ 66–67 tok/s.
- Near-full uncached ladder (final rendered prompts): prefill 2,335 (8K) →
  2,006 (16K) → 1,555 tok/s (32K near-full); decode 63.5 → 54.8 → 43.5 tok/s;
  TTFT 3.2 s → 7.8 s → 20.6 s. VRAM 9,196 → 9,884 → 11,296 MiB.
- Historical parity check: 2026-07-05 lane measured 66.57 tok/s out / 2,749 tok/s
  prefill on an older llama.cpp build — parity (−0.9% / −1.1%); no material
  runtime regression or gain.

## 5. Quality and capabilities

- **Quality:** frozen 12-task mechanical screen (scorer frozen before outputs,
  temp 0, seed 42): **11/12 PASS**. Sole FAIL: lexical constraint (sentence with
  no letter "e"). Clean on factual instruction, structured output, retrieval,
  conflict resistance, absent-information grounding, instruction retention
  (incl. nested), repeat consistency, extraction, strict JSON, false premise,
  uncertainty.
- **Reasoning (thinking ON, card sampler):** three-premise syllogism with
  disjoint-set step — correct answer with visible, on-point chain (~1.2K
  reasoning chars). PASS.
- **Coding:** executable-oracle task (`moving_sum` window sums) — generated code
  executes correctly on all oracle cases. PASS.
- **Tools:** valid tool call with correct JSON arguments and grounded
  continuation incorporating the tool result. PASS. Thinking channel works
  through the llama.cpp server (`reasoning_content` separated).

## 6. Reliability (proven mechanical 20-task corpus, 2 seeds)

Sampler: card-recommended non-thinking (temp 0.7 / top_p 0.8 / top_k 20 / min_p 0).

- Mechanical pass: **seed 42: 7/20; seed 314159: 8/20**.
- Attribution (DERIVED from verbatim outputs): **19 of 25 failing instances are
  substantively correct/acceptable answers failing mechanically** — question-phrase
  echo tripping `forbid` markers, keyword morphology, valid alternate wording, or
  frozen 140-token-cap truncation (`finish=length` 7/20 and 6/20). Consistent
  strengths: strict interfaces 3/3 both seeds; evidence discipline 2/3 both.
- Substantive failures (real guardrails, not scorer artifacts): fabricated a
  description of a nonexistent commit (both seeds) — one true hallucination
  pattern; asserted a root cause without logs (both seeds); never addressed a
  false premise framing (both seeds).
- Guardrails: deploy with generous output budgets; prefer strict-interface
  phrasings that do not invite question echo; treat ungrounded
  "explain this artifact/commit" requests as fabrication risk; thinking mode
  only with the card sampler.

## 7. Context envelope — MODEL-CARD CONTEXT ENVELOPE COMPLETE

| Surface | Rung (exact) | Disposition |
|---|---|---|
| Native | 8,192 | VALIDATED (98.99/98.84% occupancy; pp 2,335; tg 63.5) |
| Native | 16,384 | VALIDATED (99.37/99.20%; pp 2,006; tg 54.3–55.4) |
| Native | **32,768 (exact native max)** | **VALIDATED** (99.2–99.6% occupancy perf; useful-context PASS; VRAM 11,296 MiB) |
| YaRN (official) | 65,536 | FIT_LIMIT (measured cudaMalloc OOM, 5,440 MiB KV request) |
| YaRN (official) | **131,072 (exact advertised extension max)** | **FIT_LIMIT** (measured OOM at q8_0 KV 10,880 MiB AND lowest dtype q4_0 5,760 MiB; fixed memory ~8.6–8.9 GiB leaves no supported configuration) |

Attribution: RTX 5070 12 GB, not the model. Nearest measured fit boundary:
32,768. TECHNICAL = PRACTICAL = USEFUL CONTEXT MAX = **32,768** on the canonical
q8_0 surface. Three bounded allocation-failure attempts total; no repeated OOM
cycles, no Xid. FIT_LIMIT is 12 GB-specific; larger hosts may validate YaRN.

## 8. Useful context at 32,768 (two seeds + 95%-depth completion)

Measurement convention: reserve 640 tokens (512 generation + 128 safety);
occupancy measured on the FINAL rendered/tokenized prompt; placement depths
measured on the final rendered token stream against the contract depths
2/25/50/75/95%; preferred placement error ≤0.25 pp (hard ≤0.50 pp); two seeds
at the highest runnable rung; one combined inference request per seed.

- Execution-day runs (2026-09-14, seeds 42 and 314159): 99.47% occupancy
  (31,958 / 31,959 of 32,128 usable), all five behavioral gates PASS — exact
  retrieval, multi-fact synthesis, decoy rejection, absent-information
  ("NOT STATED"), instruction compliance. Fact targets placed at
  2.0/24.9/49.8/74.8% (max error 0.198 pp); terminal instruction block at ~99%.
- **Closeout completion (2026-09-15):** the frozen contract also requires a
  ~95% TARGET placement, which the execution-day fixture had not exercised
  (four fact targets plus the ~99% instruction block). An append-only
  completion under the SAME frozen fixture design, reserve, scoring rules,
  context, profile, and both required seeds added the 95% target. Results:
  99.49% occupancy both seeds; **all five contract depth placements within the
  preferred bound** — seed 42 max error 0.160 pp (95% target measured at
  94.944%), seed 314159 max error 0.087 pp (95% target at 94.913%); all gates
  PASS both seeds, including exact retrieval of the 95%-depth fact. Useful-context
  depth coverage: **COMPLETE**.

## 9. LocalMaxxing disposition

**MEASURED_NOT_SUBMITTED.** Eligible stack (GGUF + llama.cpp + RTX 5070). A
fresh local benchmark of the canonical practical profile was executed:
pp512 2,719.17 ± 29.51 / tg128 65.95 ± 0.03 tok/s, 5 reps, actual 512-token
prompts. The historical 2026-07-05 local record was never submitted (no
submission record exists) and is not an exact stack match. No submission was
performed; no verification fields were fabricated. Submission remains a
separate human decision.

## 10. Final classification

**READY_WITH_GUARDRAILS.** Recommended roles: general technical assistant,
retrieval/RAG over ≤32K windows, coding assistance, tool-using agent (text),
thinking-mode reasoning on demand. Poor fit: terse fixed-budget endpoints
without output-budget tuning; unsupervised explain-unknown-artifact duty;
>32K document work on this hardware. Recommended serving command surface:
llama.cpp b9672 SM120 server, `-ngl 999 -c 32768 -np 1 -ctk q8_0 -ctv q8_0
-fa auto --jinja` with server-side non-thinking baseline — 11,296 MiB VRAM
(~0.92 GiB reserve), decode ~66 tok/s practical / 43.5 tok/s at a full 32K window.

## 11. Limitations

- Reliability scores are mechanical-corpus scores; read §6's attribution, not
  the 7–8/20 headline alone.
- q8_0 KV is part of the canonical profile; the q8_0-vs-f16 KV quality delta is
  not separately characterized (all gates measured on the canonical config).
- Thinking mode validated by one dedicated probe; no thinking-mode reliability
  sweep. Tool behavior: single-tool probe + grounded continuation.
- FIT_LIMIT dispositions are 12 GB-hardware-specific.
- Upstream artifact drift means reproducibility rests on the pinned SHA-256;
  any future re-acquisition is a materially different artifact.

## 12. Provenance

Native publication (consolidated architecture): public-safe derivative of the
accepted local WELP campaign
`qwen3-14b-rtx5070-welp-recharacterization-2026-09-14` (executed 2026-09-14 on
WumboJetsII; closeout completion 2026-09-15). The retained local bundle holds
the primary report, structured lab record, conformance record, campaign
manifest with per-file SHA-256 evidence index, raw run outputs, and the
completion harness. No per-model repository was created; legacy `eval-*`
repositories remain retired historical provenance.
