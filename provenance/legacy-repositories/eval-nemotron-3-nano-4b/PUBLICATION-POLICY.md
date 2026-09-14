# Publication policy — `nemotron-3-nano-4b` (-> WumboLabs/eval-nemotron-3-nano-4b)

## Artifact classification

### PUBLIC (safe to publish as text)
- README.md
- report.md
- reports/
- website-publication.json
- MODEL.md
- model-manifest.json
- PUBLICATION-POLICY.md
- publication-policy.json
- WLEP-CONFORMANCE.md
- protocol-findings.md
- protocol-snapshot/
- publication/
- profiles/
- prompts/
- results/
- summaries/
- scripts/
### EXCLUDED_INITIAL_RELEASE / DO_NOT_PUBLISH
- sources/ (EXCLUDED_INITIAL_RELEASE; excluded wholesale; no per-file source review performed)
- omp-evidence/ (OMP internals - review)
- wlep-validation-2/localmaxxing/speed-test.json (host telemetry incl. GPU model/OS) - review
### LOCAL_ONLY (never published - local tooling/binaries/caches)
- models/ (symlink -> ../../models/nemotron-3-nano-4b/artifacts, never tracked)
- telemetry/

## Model binaries
No model GGUF weights are stored under this campaign root; `models/` is a relative symlink into `models/<slug>/artifacts/` (qwen holds only `inventory.md` plus evidence symlinks). Symlink targets MUST be excluded from any public repo tree. See `model-manifest.json` for SHA-256 provenance only.

## Secret scan
2026-08-26 pattern scan — CLEAN, zero matches. `sources/` is excluded wholesale from the initial public release; no per-file source review was performed.
2026-09-12 re-scan including the recharacterization follow-up files (`reports/`, `website-publication.json`) — CLEAN, zero matches.

## LocalMaxxing
SUBMITTED, origin VERIFIED_EXISTING — canonical submission `cmt86gy1j000eli01ca3cwwn0` (185.8 t/s out, approved 2026-08-25). The exact canonical practical profile was already on the service; zero new submissions were created for the recharacterization. (Historical release note preserved: `cmt84q6zw0028xl0168x31zkg` at 182.2 t/s is one of the two documented CLI-defect duplicate submissions from 2026-08-25, superseded in bookkeeping by the canonical corrective submission.)

## WumboCore
Classification for this model's Lab Record: PARTIAL.
Current-WELP recharacterization classification (2026-09-11): READY_WITH_GUARDRAILS (reliability is the guardrail).

## 2026-09-12 current-WELP recharacterization follow-up (append-only)
The 2026-08-25 campaign remains **PROTOCOL_BLOCKED** (12/12 screen; WELP then defined no deterministic Phase-3 advancement threshold — finding F-01); `report.md` and all historical files are preserved unchanged. The follow-up campaign
`nemotron3-nano-4b-rtx5070-welp-recharacterization-2026-09-11` (executed 2026-09-11) is appended under `reports/` with a machine-readable export at `website-publication.json`. Claim boundary: MODEL-CARD CONTEXT ENVELOPE COMPLETE = YES (native 262,144 VALIDATED at both required seeds, strict useful-context aggregate PASS at every rung, official extensions source-backed absent); practical default 32,768 / guarded 131,072; quality screen 12/12; reliability is the guardrail (clean-pass 0.30/0.25, hallucination 0.20/0.15 across seeds 42/314159 on the stratified mechanical corpus — transport/runtime reliability strong, behavioral adversarial reliability materially weaker). The tested frozen near-full fixture passing strictly is not proof of universal long-document reasoning, and the bounded quality screen is not evidence of universal reliability.

Results are bounded by the tested artifact, runtime, hardware, configuration, and protocol snapshot; they are not universal model rankings. Canonical scientific authority is the local WELP campaign evidence for the historical campaign and for `nemotron3-nano-4b-rtx5070-welp-recharacterization-2026-09-11` (authoritative for current claims).
