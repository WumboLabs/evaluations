### Identity

| Field | Value |
|---|---|
| Model | Ornith 1.5 9B |
| Producer | ornith-ai/Ornith-1.5-9B |
| Source revision | `489cb97981b8654bcfcf30ce1f94ed1b62e07b53` |
| Evaluated artifact | Ornith-1.5-9B-Q4_K_M.gguf |
| SHA-256 | `70c112196e0b7023803c9762752e46d29e612a92c83f995bc3ba1ceb07e8fab6` |
| Evaluation date | 2026-08-27 |
| Protocol | WELP end-to-end (campaign `ornith-1.5-9b-welp-2026-08-27`) |
| Phases completed | Intake → Admission → Performance → Practical Viability → Reliability → Capability Modules → Context → Variance → Optimization → Soak → Final Classification |
| Campaign classification | COMPLETED_FULL_PROTOCOL_CHARACTERIZATION |

### Hardware

| Field | Value |
|---|---|
| Machine | WumboJetsII |
| GPU | NVIDIA GeForce RTX 5070 12GB (SM120) |
| CPU | AMD Ryzen 7 9800X3D |
| OS | Fedora Linux 44 |
| Driver | NVIDIA 610.57.04 |
| Runtime | llama.cpp `b10449` @ `0d9ceae1e38291035605613ab41a8f5e693d6fcd` |
| Serving profile | `-c 32768 -ngl 99 --parallel 1 --fit off -fa on --jinja --reasoning off`, batch 2048 / ubatch 512, no speculation |

### Headline Verdict

**FINAL WELP READINESS: NOT_READY.**

- Phase 3 Practical Viability: **ADVANCE** (aggregate 0.922, all five gates pass, identical decision across seeds 42/43/44).
- Phase 4 Reliability: **DO_NOT_ADVANCE** — frozen gate G6 (uncertainty-calibration rate) measured 1/21 = 0.0476 against a ≥0.15 threshold.
- Under frozen protocol semantics, the Phase 4 gate failure closes deployment: **0 deployment roles earned** (`roles = []`).
- All later-phase evidence (capability modules, context, variance, optimization, soak) is **characterization only** and does not modify the readiness verdict.

This is a complete campaign, not an early stop: phases after the blocking gate were run under explicitly frozen characterization-only contracts, and the classification engine still returns NOT_READY.

### Performance (Phase 2)

| Metric | Result |
|---|---|
| Decode throughput | 102.04 ± 0.06 tok/s |
| Prefill throughput | 4,046.67 ± 15.68 tok/s |
| TTFT (estimated, short prompt) | ~46.7 ms |

### Practical Viability (Phase 3) — ADVANCE

30 tasks × seeds {42, 43, 44}, thinking OFF baseline, scorer self-test 35/35 before live scoring.

| Gate | Threshold | Result | Verdict |
|---|---|---|---|
| G1 aggregate | ≥0.75 | 0.922 | PASS |
| G2 false-premise | ≥0.60 | pass | PASS |
| G3 factual-uncertainty | ≥0.50 | pass | PASS |
| G4 structured-output | ≥0.70 | pass | PASS |
| G5 seed stability | identical decision | identical | PASS |

### Reliability (Phase 4) — DO_NOT_ADVANCE

162/162 rows scored. G1 clean 0.4877 PASS · G2 hallucination-on-false-premise 0.1296 PASS · G3 refusal-drift 0.0185 PASS · G4 UNSAFE = 0 · G5 seed range 0.0926 PASS · **G6 uncertainty 1/21 = 0.0476 FAIL** (threshold ≥0.15).

**Mechanical vs qualitative distinction:** the mechanical gate result is authoritative and stands — the campaign verdict is NOT_READY. Manual review (documented as scorer-lexicon adjudications, finding PF-01) found the dominant G6 failure mode to be scorer false-negatives: correct expressions of uncertainty whose wording fell outside the frozen lexicon. Genuine calibration failures remain in the residual. The qualitative finding explains the mechanism; it does not overturn the gate.

### Capability Modules (Phase 5) — characterization only

No PASS thresholds exist for Phase 5 (frozen decision D4); rates below are honest characterization, not gate results.

| Module | Clean-pass rate |
|---|---|
| Coding | 0.867 (78/90) |
| Structured interfaces | 0.875 (63/72) |
| Native tools | 0.80 |
| Extraction / RAG | 0.722 (39/54) |
| Linux / systems | 0.515 (34/66) |
| Reasoning (OFF vs ON thinking) | 17/30 vs 17/30, Δ = 0; thinking ON ≈ +27% wall cost |

### Context (Phase 6)

Useful context **24,576 tokens** under the 12 GB Q4_K_M profile (configured 32,768; top rung INCONCLUSIVE due to harness overshoot, PF-02). The producer's 256K window claim is **not** reproducible on this hardware profile.

### Variance (Phase 7)

7/9 surfaces STABLE across seeds. Two flagged ESCALATE_TO_5: linux_systems (range 0.1819) and reasoning-off (0.20). Recorded, not re-run.

### Optimization (Phase 8)

MTP speculative decoding (`--spec-type draft-mtp`): +9.9% throughput but output divergence → **REJECTED_FOR_CANONICAL**. Frozen serving profile unchanged.

### Stability (Phase 9) — screening soak

30-minute screening: 11,449 requests, 0 real errors, 0 GPU Xid events. Clean. **LOCKIN (120 min + cycles) NOT_REACHED** — screening-level only.

### Producer Claims (reviewed against revision `489cb979`)

| Claim | Outcome |
|---|---|
| 9B Ornith-1.5 lineage | REPRODUCED_IDENTITY |
| 256K context window | PARTIALLY_REPRODUCED (architecture yes; 12 GB profile no) |
| Coding-specialist positioning | PARTIALLY_REPRODUCED |
| Native tool calling | PARTIALLY_REPRODUCED |
| Reasoning-first behavior | PARTIALLY_REPRODUCED (Δ = 0 on this suite) |
| Official sampling recipe | RECORDED_VERBATIM |
| Card benchmark scores | PHYSICALLY_UNTESTABLE (cloud-scale reference hardware) |

### Important Limitations

- **NOT_READY is a role verdict, not a capability verdict.** The model passed practical viability and showed strong coding/structured-output characterization; one frozen reliability gate (with documented scorer-lexicon contamination) closes all deployment roles.
- Results are scoped to Q4_K_M on a 12 GB consumer GPU under the frozen serving profile; they do not establish behavior at other quantizations, context sizes, or hardware classes.
- Phase 5 module rates are characterization without gates; two surfaces carry unresolved seed-variance flags.
- Soak evidence is screening-level only; long-hold stability is unestablished.
- Reasoning-mode equivalence (Δ = 0) is suite-scoped, not a general claim that thinking adds no value.

### Evidence Links

- **Canonical evaluation repo:** https://github.com/WumboLabs/eval-ornith-1.5-9b
- **WELP protocol:** https://github.com/WumboLabs/welp
- **Labs catalog:** https://github.com/WumboLabs/labs
- **LocalMaxxing:** Speed result submitted and APPROVED (ID `cmtc6sopl0007o601d7hqrj1z`; decode 102.04 tok/s, prefill 4,046.67 tok/s, Q4_K_M, llama.cpp b10449, RTX 5070 12 GB). Model page: https://www.localmaxxing.com/en/models/ornith-ai/Ornith-1.5-9B

### Reproduction

Direct link to canonical reproduction material: [eval-ornith-1.5-9b/](https://github.com/WumboLabs/eval-ornith-1.5-9b)

This Lab Record is a summary; the canonical repo is the source of truth.
