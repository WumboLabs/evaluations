# WumboLabs Model Evaluation Report — Apodex 1.1 mini

Campaign: `apodex-1.1-mini` · Date: 2026-08-25 · Protocol: WELP `wlep-next-snapshot-2026-08-25-end-to-end` (DRAFT)
Declared objective: TEXT + REASONING + CODING + TOOLS + AGENTIC USE · Host: WumboJetsII (RTX 5070 12 GB)

---

## 1. Final classification

| Field | Value |
|---|---|
| **Outcome** | **DO_NOT_ADVANCE at Phase 3** (early stop, frozen gate) |
| Roles supported by evidence | none beyond "runs coherently on 12 GB at extreme quantization" |
| NOT_REACHED | Phases 4–10, OMP Stage 2, all capability modules, context/variance/optimization/soak/classification engine |
| NOT_APPLICABLE | Vision module (declared objective is text+agentic; source supports vision — SUPPORTED_BY_SOURCE / NOT_EVALUATED) |

Per protocol, an early Phase-3 stop limits all conclusions. Nothing here measures reliability, coding, tools, agentic ability, useful context, or stability.

## 2. Model identity

- **Upstream:** `apodex/Apodex-1.1-mini` @ `62583b464707ad58848bc2ab066747d8d5b02533` (verified live 2026-08-25). Qwen3_5MoeForConditionalGeneration; base `Qwen/Qwen3.5-35B-A3B`; ~36B total / A3B active MoE; hybrid attention (full every 4th of 40 layers); native MTP head; Apache-2.0; vision-capable source.
- **Official quant siblings verified:** FP8 `4a1ff0e7…`, NVFP4 `499ed0ee…`, GPTQ-Int4 `e5a684bb…` (~24.7 GB → PRODUCER_REFERENCE only; cannot fully reside on this GPU).
- **Canonical evaluated artifact:** community conversion `abenzerps/Apodex-1.1-mini-GGUF` @ `59afa57852525f79a9634d5f80dd639cceee572c` (**not official**), file `Apodex-1.1-mini-IQ1_M.gguf`, 8,821,221,376 bytes, SHA-256 `1e84d8adf7837e96fb18712882a8a114becc7e53554372e2f612c5e0c6276cd4` (matches repo SHA256SUMS).
- **External chat template:** `chat_template.jinja` sha256 `d139c773…`, byte-identical to upstream revision.
- **Rejected admission candidate:** IQ2_M (`450afff9…`, 12,241,706,816 B) — full-GPU placement deterministically impossible (11.43 GB weights buffer vs 10.87 GB free VRAM).

## 3. Runtime & environment

- llama.cpp pinned at `f280b26983ad0fdb705a0d9ebf0503e76f2899b0` (2026-08-24), campaign-local tree `runtime/llama.cpp` (existing trees untouched). Existing newest build `0d9ceae1` was 166 commits behind the repo's stated minimum. Build: Release, GGML_CUDA=ON, sm_120, CUDA 13.3, host g++-15 + `-allow-unsupported-compiler`. Driver 610.57.04.
- **Experimental identity difference:** runtime differs from prior campaigns' builds (recorded per Runtime Pinning).

## 4. Serving profile (canonical baseline)

REQUESTED/EFFECTIVE both captured (`summaries/serving_profile_requested.json`, admission evidence in `summaries/admission.json`): `-ngl 999 -np 1 -c 32768 -fa on -kvu -fit off -b 2048 -ub 512 -rea off --jinja --chat-template-file …`; speculation OFF (native MTP present but disabled); alias `apodex-1.1-mini-iq1m`; endpoint `127.0.0.1:18450`.
EFFECTIVE verified: startup log `n_slots = 1, n_ctx_slot = 32768, kv_unified = true`; VRAM 9.7 GB vs RSS 74 MB ⇒ full-GPU, no hidden CPU offload; reasoning behavioral probe clean.

## 5. Performance (Phase 2 — COMPLETE)

| Metric | Result | Method |
|---|---|---|
| Decode throughput | **169.36 t/s** (median 169.46, σ 1.70) | 5 reps after warmups, long-form task, unique prompts |
| Prefill (~5.6K tok) | **1798.76 t/s** (σ 11.19) | dedicated `--no-cache-prompt` instance, cross-checked |
| TTFT (short prompt) | ~125 ms | temp-0.2 probes |
| Load → serving | ~2.6 s from log | no-cache instance |
| VRAM idle / power / temp | 9.7 GB / 29.9 W / 42 °C | nvidia-smi |

Invalidated measurement passes retained with reasons (see §10): two harness-defect passes and one genuinely contaminated prefill pass.

## 6. Phase 3 Practical Viability — DO_NOT_ADVANCE

Contract `wlep-practical-viability 0.1.2-draft` (`a7b2af11…`), scorer `score_pv.py` (`79f29b2c…`, self-test 35/35 immediately before use), 30 tasks × seeds {42,43,44}, thinking OFF baseline.

| Gate | Threshold | s42 | s43 | s44 | Verdict |
|---|---|---|---|---|---|
| G1 aggregate | ≥0.75 | 0.667 | 0.700 | 0.733 | **FAIL (all)** |
| G2 false-premise | ≥0.60 | 0.400 | 0.200 | 0.600 | **FAIL (42,43)** |
| G3 factual-uncertainty | ≥0.50 | 0.500 | 0.750 | 0.500 | PASS (boundary) |
| G4 structured-output | ≥0.70 | 0.714 | 0.714 | 0.714 | PASS |

Decision identical across seeds ⇒ stable FAIL. Bounded failure review (27 rows): ~19 genuine failures — fabricated package description, explained nonexistent git flag, asserted 25 prime, invented phone number for absent field, echoed un-reversed word; ~8 scorer lexicon artifacts (PF-01/SC-01). Verdict robust: correcting every artifact still leaves seed-42 aggregate <0.75.

## 7. Agentic results

- **Native Tools / Coding / Reasoning modules:** NOT_REACHED (gated).
- **OMP local agent:** Stage 1 connectivity smoke PASS (`omp/18.0.5`, implicit llama.cpp discovery, isolated profile `wlep-apodex`, zero config mutation) — an INTEGRATION result only. Stage 2 NOT_REACHED.
- **Reasoning mechanism observation (non-gate):** thinking mode functional and separated correctly at runtime; a thinking-off probe answered arithmetic wrongly that thinking-on answered correctly — but IQ1_M budgets are consumed aggressively by reasoning (one full PV pass invalidated for starvation). Producer "reasoning-first" positioning is directionally consistent; quantized practical quality did not clear viability gates.

## 8. Producer claims

Agent Team benchmark scores (APEX-Agent 27.7, FrontierFinance 50.2, FrontierScience 51.7 for mini) are **FrontierAgent system-level results** — PHYSICALLY_UNTESTABLE here and not comparable to raw-model WLEP numbers. Full classification table: `summaries/producer_claims.json`.

## 9. Reliability / Context / Variance / Optimization / Stability

NOT_REACHED — explicitly not tested. No soak ran; no Xid/reset/GSP/channel/display events occurred during any server operation.

## 10. Execution accounting

Valid measured: 106 generations/reps (90 PV + 10 perf + 3 cache probes + 2 admission probes + 1 OMP smoke). Invalidated/discarded (retained on disk, excluded from statistics): 230 across 6 recorded events — see `summaries/execution_counts.json`.

## 11. Publication routing

- LocalMaxxing speed result: **SUBMITTED / APPROVED** — canonical ID `cmt9ijytg00xali017f46xk25` (2026-08-26T03:07:38Z; llama-bench p512/n128 → 182.31 tok/s out). A byte-identical duplicate `cmt9imzoz00xfli01g5tzz3kx` was accidentally created by a non-idempotent `--json` re-invocation of the submit command; LocalMaxxing has no speed-test delete mechanism; canonical = earlier ID. Full disclosure: `summaries/localmaxxing.json`.
- WELP outcome is unchanged by this submission: **DO_NOT_ADVANCE at Phase 3**. No reliability/coding/tools/context/soak claims are made.
- LocalMaxxing benchmark suites: NOT_SUBMITTED / NOT_APPLICABLE due to early WELP stop.
- LocalMaxxing Report: NOT_CREATED due to early WELP stop.
- GitHub Lab Record bundle: prepared at `publication/repo-candidate/` (no git operations performed).
- WumboCore: machine-readable summary ready (`summaries/wumbocore_summary.json`); website untouched.

## 12. Limitations

Single 12 GB consumer GPU forced extreme quantization (IQ1_M, 1.75-bpw); producer positioning rests on BF16-class deployments plus an agent harness we were not authorized to run. Phase-3 failure at IQ1_M does NOT establish that BF16/FP8/GPTQ or Agent Team deployments would fail — it establishes that the strongest representation satisfying the frozen WumboJetsII full-GPU baseline does not clear the frozen viability gate. Scorer lexicon defect understates false-premise performance modestly; verdict unaffected.

## 13. Reproduction

1. Acquire GGUF + template at pinned revisions (`sources/acquisition_iq2_m.json`, `sources/provenance.json`).
2. Build runtime at pinned commit (flags in `summaries/environment.json`).
3. Launch server with canonical flags (§4).
4. Run `scripts/run_calibration.py` semantics for 30 tasks × seeds 42–43–44 (driver recorded in conformance JSON); score with `scorers/score_pv.py score`.
5. All artifact hashes in `summaries/artifact_index.json`.

## 14. Artifact index

Machine-readable index: `summaries/artifact_index.json`. Key paths: `summaries/{admission,performance,practical_quality,producer_claims,execution_counts,wlep_conformance,localmaxxing,wumbocore_summary,serving_profile_requested}.json`, `results/*` (raw + INVALIDATED-*), `protocol-snapshot/campaign-snapshot-manifest.json`, `WLEP-CONFORMANCE.md`, `protocol-findings.md`.
