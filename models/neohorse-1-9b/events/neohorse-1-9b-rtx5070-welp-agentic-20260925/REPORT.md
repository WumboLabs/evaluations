# REPORT — NeoHorse-1-9B, WELP Agentic event (fresh-model campaign group)

Artifact role: PRIMARY SCIENTIFIC REPORT
Campaign: neohorse-1-9b-rtx5070-welp-agentic-2026-09-25
Status: CURRENT
Protocol: WELP snapshot `welp-next-snapshot-2026-09-25-model-agentic`
(DRAFT / NOT v1.0; snapshot introduction commit `5f611de36e44a2d06fa41acd75aa62dcf66c0edb`;
campaign group started from WELP working tree `228dfe6`)
Event class: **FRESH_MODEL** Agentic event of the NeoHorse-1-9B campaign
group.

Run fingerprint: campaign slug `welp-agentic` · date 2026-09-25/26 ·
harness selftest PASS 37/37 · 2 adapter qualification probes (both PASS) ·
3 required task classes: 2 scored (1 PASS / 1 FAIL) + 1 INTEGRATION_BLOCKED
(deterministic frozen-harness defect) · parent profile predeclared
(publisher-default Reasoning On).

---

## 1. Purpose and scope

WELP Agentic for NeoHorse-1-9B: can the tested model, through the specified
agent harness, independently complete bounded tasks using tools and
environment feedback? The Model section is NOT re-measured: its evidence is
reused byte-identical from the linked sibling events (the full evidence tree
is copied hash-bound into this bundle); the classification is re-derived
here from that same evidence (READY_WITH_GUARDRAILS, R-C6/R-C7).

## 2. Tested configuration (MODEL + HARNESS + ENVIRONMENT)

- Parent profile: `neohorse-1-9b-q8-0-llamacpp-b10999-rtx5070-deployment-reasoning-on`
  — PREDECLARED in `summaries/profile-selection.json` BEFORE any scored
  Agentic output (publisher-default preference rule of
  `welp-agentic-0.1.0-draft`; the model is explicitly marketed for agent
  harnesses, which the publisher default targets). Reasoning Off remains
  explicitly untested for Agentic behavior.
- Artifact/runtime/hardware: identical to the parent profile event
  (profile-invariant reuse, hash-bound).
- Harness: `welp-agentic-harness/0.1.0-draft` (welp commit `5f611de...`,
  executed bytes hash-bound in the manifest); selftest PASS 37/37.
- Adapter: BOTH declared adapters qualified on the real endpoint before any
  scored task (retained probes): text_json PASS (8 turns / 863 tokens) and
  native_tools PASS (9 turns / 800 tokens). Frozen choice: **native_tools**
  — the model's chat template carries native tool calls and `--jinja`
  serving parses them into OpenAI-style tool calls; the frozen contract
  requires the model's actual deployment path.
- Reasoning control: `enable_thinking=true` on every request (the parent
  profile's proven control). Sampling: temperature 0.2, top_p 0.95.
- Sandbox: disposable unprivileged bwrap (offline net/ipc/pid/uts, no /home,
  no evaluator files, minimal /etc, RLIMITs, 60 s command timeout); the
  harness positive-control probe passed before every attempt.
- Frozen limits: 40 turns, 3600 s wall, 262144 total completion tokens,
  2048 per-request, 60 s command timeout, 3 consecutive parse errors —
  derived from the non-scored disjoint qualification probes and never
  enlarged after scored outputs.

## 3. Scored results (2 of 3 tested tasks + 1 blocked class)

| Task | Class | Outcome | Stop reason | Turns | Tokens | Wall |
|---|---|---|---|---|---|---|
| agentic-repository-1-notes-cli | repository | **FAIL** | FINISHED | 13 | 5694 | 98.2 s |
| agentic-system-1-quoteservice | system | **NOT_EVALUABLE** (harness-side) | HARNESS_FAILURE x2 | 5+5 | 470+320 | n/a |
| agentic-research-1-atlas9-batching | research | **PASS** | FINISHED | 20 | 8690 | 141.4 s |

**Result: 1/2 completed scored tasks; the third required class is
INTEGRATION_BLOCKED** — reported as X of 3 tested tasks, never as an agent
success rate.

**Repository — FAIL (false verification claim).** Mechanical oracles: the
agent's final state passes the visible suite (4/4, exit 0) but fails the
hidden acceptance checks. The decisive recorded failure: the agent
terminated with a final report asserting completion while its actual final
environment state contradicts the claim — the model+harness outcome is FAIL
exactly as the frozen scoring requires (a plausible report never rescues
failed oracles).

**System — INTEGRATION_BLOCKED (deterministic frozen-harness defect; not a
model outcome).** Both attempts crashed identically inside the FROZEN
canonical harness: `_execute_tool` raises an unhandled PermissionError when
`read_file` touches the task-planted mode-000 data file, and this model's
diagnostic ordering reads that file within its first five turns (per-request
prompt-token sequences from the pinned server log confirm the identical tool
sequence across attempts: 851/941/1331/2085/2208 vs 851/942/1336/1989/2114).
The crash is a harness implementation defect (a missing OSError guard that
should return a denial observation), NOT model behavior: the same fixture
ran to completion for the methodology-validation model, whose agent happened
to chmod before reading. WELP was NOT modified by this campaign (the
handoff prohibits it), so the defect cannot be repaired in-campaign; it is
recorded as MINOR_WELP_IMPROVEMENT for the next WELP revision. Both crashed
attempts are preserved as honest HARNESS_FAILURE/NOT_EVALUABLE records with
server-log-recovered token accounting; per R23 they stay separate from any
model verdict.

**Research — PASS.** Correct current value (96), correct governing source
(ops-bulletin-7), correct superseded set, all citations resolved, artifact
completed — 20 turns, 8690 completion tokens, no assistance.

## 4. What this validates, and what it does not

- The Agentic methodology executed end to end on a fresh model: predeclared
  parent-profile selection; dual-adapter qualification; frozen limits held;
  sandbox isolation green on every attempt; mechanical oracles scored final
  state, not narration; the runner never rescued the model.
- The model's Agentic capability is NOT certified: 2 of 3 classes measured
  (bounded sample), the third blocked by frozen infrastructure. No general
  autonomous-reliability claim is made.

## 5. Evidence reuse and migration

Model-section evidence (reliability 120 scored instances, context cells,
capabilities, quality screens, reviews, performance arms) reused
byte-identical from `neohorse-1-9b-rtx5070-welp-reasoning-on-2026-09-25`;
only the reuse document's campaign_id and note changed (hash re-bound in
the manifest). The derived classification equals the parent verdict:
**READY_WITH_GUARDRAILS (R-C6/R-C7)**. Full mapping: `REUSE-MIGRATION.md`.

## 6. Costs and overhead

Agentic-specific overhead (this event only): ~15 min wall for qualification
+ scored tasks, ~15k completion tokens, no downloads, no fit ladder, no
context sweep, no speed benchmarks. LocalMaxxing disposition:
`SUBMITTED` / `VERIFIED_EXISTING` — the existing service record
(`cmuhu00r40dtjlq01ptbrfbx2`) already covers this canonical profile; Agentic
task metrics are not LocalMaxxing speed metrics and no duplicate was
submitted.

## 7. Completion status

Campaign execution: **COMPLETE_PASS** — the frozen methodology executed
fully; validators green; the INTEGRATION_BLOCKED task class is a recorded,
caused, terminal disposition with preserved evidence, never a silently
missing section. Agentic verdict: 1/2 scored tasks (1 PASS / 1 FAIL) with
the system class INTEGRATION_BLOCKED — reported independently, never
combined with the Model verdict (READY_WITH_GUARDRAILS / R-C6-R-C7).

Next gate: none on the success branch; group terminal closeout proceeds
(central publication -> website -> archive -> stabilization record).
