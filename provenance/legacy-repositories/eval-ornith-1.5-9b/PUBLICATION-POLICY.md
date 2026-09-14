# Publication Policy — eval-ornith-1.5-9b

**Policy: ALLOWLIST_FIRST. Default: DO_NOT_PUBLISH.**

A file is publishable only if it matches `publication-allowlist.json`
`allowed` and no `excluded` pattern. Everything else — including anything
added later — stays private until explicitly allowlisted.

## Classes

- **PUBLIC** — report/conformance/findings docs, root metadata, `summaries/`,
  pinned `contracts/`, `corpus/`, `scorers/`, `scripts/`, `harness/`,
  `results/` (evidence JSON/JSONL), `calibration/`, `publication/` records.
- **LOCAL_ONLY** — model weights and symlinks, `logs/`, runtime binaries,
  raw soak sampler CSVs (host pids), `sources/` acquisition provenance,
  `protocol-snapshot/` (frozen upstream tree copy), unsanitized originals of
  files whose public form is the `<USER_HOME>`-rewritten copy.
- **EXCLUDED_INITIAL_RELEASE** — `sources/**` wholesale.

## Privacy rules

1. No absolute user paths (`/home/…`, `/Users/…`) in any published file.
   Where campaign evidence contains them, the published copy substitutes
   `<USER_HOME>` / `<USER>`; originals remain LOCAL_ONLY.
2. `WumboJetsII` is an established public hardware alias (already used in the
   apodex INITIAL_PUBLIC_RELEASE report) — retained, not a private identifier.
3. Secret scanning (token patterns, private keys, credential assignments,
   private IPs, credential-bearing URLs) must be clean at packaging time and
   is re-run by `welp/validators/validate_public_tree.py`.
4. Frozen artifact filenames (`wlep-*` contract ids, `wlep-rag-corpus-0.1.0`)
   are hash-pinned functional identifiers — kept verbatim.

## Gate

Publication requires a human git gate: no `git init`, staging, committing,
pushing, or repo creation happens without explicit user authorization.
External posts (LocalMaxxing, X, WumboCore) are governed separately in
`publication-policy.json` → `external_posts`.
