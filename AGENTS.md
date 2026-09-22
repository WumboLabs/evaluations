# Evaluations repository policy

This repository is the canonical public scientific evidence registry. The website is the human-facing discovery/sharing surface and a deterministic derivative. Local research retains working/raw/internal science; WumboServer preserves large model artifacts.

- Reuse/create model_id, profile_id, and event_id. A profile is a scientific identity, not a repository boundary.
- Publish accepted public-safe packages into WumboLabs/evaluations. Never automatically create new eval-* repositories.
- Edit registry.json, then generate metadata and Markdown indexes with scripts/validate.py --generate. Do not independently edit generated indexes or website registries.
- Preserve published events and scientific results. Supersession changes current-state attribution, not historical evidence. Corrections require an explicit erratum/new event.
- Canonical citations require repo + full commit SHA + path. Preserve event-introduction pins separately from registry snapshot pins.
- Store genuine multi-model reports once under shared-events/. Do not manufacture owner models or duplicate reports.
- Legacy eval-* repositories and provenance/legacy-repositories/ are historical provenance, not active publication configuration. Do not execute imported historical scripts as migration validation.
- Never publish weights, secrets, private prompts, raw LocalMaxxing payloads, large telemetry, caches, or Nsight Systems traces.
- Validate registry, public safety, provenance, and generated-index idempotence before publication. Human authorization remains required for commits, pushes, deployment, and external changes, except for the standing automatic-closeout authorization of a clean COMPLETE_PASS WELP campaign (workspace `AGENTS.md`, "Model campaign lifecycle"), bounded to the publication/closeout operations that campaign requires.

Detailed publication contract: WumboLabs/welp docs/publication.md. Scientific methodology is unchanged.
