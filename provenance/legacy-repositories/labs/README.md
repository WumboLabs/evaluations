# labs/

Future candidate for **WumboLabs/labs** — the cross-model CATALOG / INDEX.

This directory is the index, NOT the evidence monorepo. Public campaign evidence is published separately in the corresponding `WumboLabs/eval-<slug>` repository.

## Contents

- `catalog.json` — machine-readable per-model index (one entry per eval root)
- `models/` — per-model index stubs / links
- `hardware/` — hardware index
- `comparisons/` — cross-model aggregate comparison indexes

## Convention

Future public repo name for a model: `WumboLabs/eval-<slug>`.

Current-facing catalog presentation uses WELP. Do not expose internal frozen campaign identifiers in `catalog.json`. Frozen provenance stays in the eval evidence repos.

Do not duplicate full campaign evidence here.
