# WumboLabs Evaluations

Canonical public scientific evidence from WumboLabs model evaluations.

**Start with the [website model catalog](https://wumbolabs.dev/evaluations/) to discover, understand, compare, and share results. Use this repository to verify, cite, audit, and reproduce public claims.** Results are hardware-, artifact-, runtime-, and event-scoped, not universal model rankings.

## Browse the evidence

- [Models](MODELS.md) — model names, classifications, profiles, and testing history.
- [Profiles](PROFILES.md) — every materially distinct tested scientific surface.
- [Events](EVENTS.md) — reverse-chronological public reports, including shared comparisons.
- [Registry](registry.json) — the single editable public model/profile/event registry.
- [Legacy provenance](provenance/legacy-imports.json) — exact source repositories, commits, paths, hashes, and transformations.

Every model and profile directory has a readable index. Reports are linked, not copied into indexes.

## Four layers

| Layer | Responsibility |
|---|---|
| [wumbolabs.dev/evaluations](https://wumbolabs.dev/evaluations/) | DISCOVER + UNDERSTAND + COMPARE + SHARE |
| [WumboLabs/evaluations](https://github.com/WumboLabs/evaluations) | VERIFY + CITE + AUDIT public scientific evidence |
| Local `research/model-evaluations/` workspace | WORK + ANALYZE; retain raw and internal scientific material |
| WumboServer `ai/models-archive/` | PRESERVE large tested model artifacts; never GitHub model weights |

## Identity and layout

- **Model ID** identifies the model, independently of storage or repository names.
- **Profile ID** identifies a materially distinct artifact/runtime/deployment surface. One profile means one profile ID, **not one GitHub repository**.
- **Event ID** identifies an immutable evidence event. Later events may update current-state attribution; they never rewrite earlier observations.

`models/<model-id>/profiles/<profile-id>/` holds profile metadata and links. `models/<model-id>/events/<event-id>/` holds each ordinary event's public report and record. Genuine multi-model comparisons live once in `shared-events/<shared-event-id>/`; every related model links to the same report. Legacy shared-event and event IDs are both preserved. Website attribution preserves existing display/precedence, not a fictional owner model.

Small supporting artifacts that predate the event registry remain under profile `supporting-evidence/` directories. Their original filenames and provenance are retained; the migration does not invent missing scientific identities. `provenance/legacy-repositories/` is frozen historical material, **not current publication policy**.

The registry owns model facts, profile metadata, event relationships, and per-surface current-state attribution. Model/profile/event JSON files and Markdown indexes are generated derivatives. The website pins an exact registry commit and generates static pages; it is not a second independently maintained registry.

## Cite and share

Normally share `https://wumbolabs.dev/evaluations/<website-slug>/`.

For a scientific citation, use the exact repository, **full commit SHA**, and path:

```text
https://github.com/WumboLabs/evaluations/blob/<full-commit-sha>/models/<model-id>/events/<event-id>/REPORT.md
```

Each event README provides a real immutable citation. Event-introduction commits may differ from the website's registry snapshot commit. Do not replace event pins with `main`, `HEAD`, or `latest`. Legacy `eval-*` repositories were deleted on 2026-09-14 after verified consolidation into this repository; their identifiers remain historical provenance only and their URLs no longer resolve (`provenance/legacy-repository-retirement.json`).

## Publish and validate

The detailed future workflow is [WELP's publication contract](https://github.com/WumboLabs/welp/blob/main/docs/publication.md). Scientific methodology remains WELP's responsibility.

1. Run the campaign locally; obtain human scientific review.
2. Prepare a public-safe event package. Never publish weights, credentials, private prompts, large telemetry, caches, or raw submission payloads.
3. Reuse/create model/profile/event IDs here. **Do not create new `eval-<model>` or `eval-<profile>` repositories** without a later explicit architecture decision.
4. Commit event evidence, then record its exact commit/path in registry metadata. New native events use `publication_provenance`; historical imports use `legacy_sources` and the import manifest.
5. Generate and validate indexes, inspect scoped changes, and commit/push with human authorization.
6. Pin the website to the exact registry commit; sync, build, deploy with authorization, and verify production.
7. Archive large model artifacts separately when the campaign closes, under the artifact lifecycle policy.

```sh
python3 scripts/validate.py --generate
python3 scripts/validate.py --generate  # generated_changes must be 0
python3 scripts/validate.py
git diff --check
```

Validation checks IDs and references, paths, full commits, provenance coverage, file hashes, public safety, and deterministic indexes. Public-safety exceptions are restricted to reviewed exact file hashes containing nonsecret placeholders; credentials are never exempted.
