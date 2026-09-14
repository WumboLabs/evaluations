#!/usr/bin/env python3
"""Validate the public registry and regenerate its small Markdown/JSON indexes."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
REPO = "WumboLabs/evaluations"
ID = re.compile(r"[a-z0-9][a-z0-9.-]*")
SHA = re.compile(r"[0-9a-f]{40}")
HASH = re.compile(r"[0-9a-f]{64}")
GENERATED = "<!-- Generated from registry metadata — do not hand-edit. -->\n\n"
PINNED = {}


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def relative(value):
    require(isinstance(value, str) and bool(value), "missing evidence path")
    path = PurePosixPath(value)
    require(not path.is_absolute() and all(x not in (".", "..", "") for x in value.split("/"))
            and "\\" not in value and not re.search(r"[%?#\x00-\x20]", value),
            f"unsafe evidence path: {value!r}")
    require(not (ROOT / value).is_symlink(), f"symlink evidence path: {value}")
    require((ROOT / value).resolve().is_relative_to(ROOT), f"escaping evidence path: {value}")
    return value

def verify_pin(commit, path):
    key = (commit, path)
    if key not in PINNED:
        result = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=ROOT, capture_output=True)
        require(result.returncode == 0, f"missing pinned Git object: {commit}:{path}")
        PINNED[key] = hashlib.sha256(result.stdout).hexdigest()
    require(PINNED[key] == digest(ROOT / path), f"working evidence differs from pinned commit: {path}")



def citation(evidence):
    require(evidence.get("repo") == REPO, "canonical evidence must use WumboLabs/evaluations")
    require(isinstance(evidence.get("commit"), str) and SHA.fullmatch(evidence["commit"]),
            "canonical evidence requires a full commit SHA")
    path = relative(evidence.get("path"))
    require((ROOT / path).is_file(), f"missing evidence file: {path}")
    verify_pin(evidence["commit"], path)
    return f"https://github.com/{REPO}/blob/{evidence['commit']}/{path}"


def unique(items, key):
    ids = [x.get(key) for x in items]
    require(all(isinstance(x, str) and ID.fullmatch(x) for x in ids), f"invalid {key}")
    require(len(ids) == len(set(ids)), f"duplicate {key}")
    return dict(zip(ids, items))


def event_models(event):
    return event["related_model_ids"] if event.get("shared_event_id") else [event["model_id"]]


def event_profiles(event):
    if event.get("shared_event_id"):
        return event.get("related_profile_ids", [])
    return [event["profile_id"], *event.get("related_profile_ids", [])]


def scan_public_tree():
    reviews = load("provenance/public-safety-review.json")["reviewed_files"]
    reviewed = {(r["path"], r["sha256"], r["category"]): r for r in reviews}
    patterns = {
        "private_home": re.compile(r"/" + r"(?:home|Users)/[^\s\"\)]+"),
        "username": re.compile(r"\b" + "che" + "ez" + r"\b", re.I),
        "credential": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]{20,}|Bearer\s+[A-Za-z0-9._-]{12,}|-----BEGIN [A-Z ]*PRIVATE KEY-----", re.I),
        "sensitive_assignment": re.compile(r"(?:api[_-]?key|access[_-]?token|password|secret)\s*[=:]\s*[\"'][^\"']{8,}", re.I),
    }
    files = 0
    findings = []
    for path in sorted(ROOT.rglob("*")):
        if any(part in {".git", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        require(not path.is_symlink(), f"public tree contains symlink: {path.relative_to(ROOT)}")
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        require(path.suffix.lower() not in {".gguf", ".safetensors", ".bin", ".pt", ".pth", ".nsys", ".nsys-rep", ".sqlite", ".db"}, f"prohibited public artifact: {rel}")
        require(path.stat().st_size < 5_000_000, f"large artifact requires separate archive: {rel}")
        text = path.read_text(encoding="utf-8")
        files += 1
        for category, pattern in patterns.items():
            if pattern.search(text):
                key = (rel, digest(path), category)
                require(category != "credential" and key in reviewed,
                        f"unreviewed public-safety finding: {rel} ({category})")
                findings.append({"path": rel, "category": category, "disposition": reviewed[key]["reason"]})
    return {"status": "PASS", "files": files, "reviewed_nonsecret_findings": findings}


def validate(registry):
    require(registry.get("schema") == "wumbolabs-evaluations/1", "unsupported registry schema")
    models = unique(registry["models"], "model_id")
    profiles = unique(registry["profiles"], "profile_id")
    events = unique(registry["records"] + registry["shared_events"], "event_id")
    unique(registry["shared_events"], "shared_event_id")
    order = registry["website_event_order"]
    require(len(order) == len(set(order)) and set(order) == events.keys(), "website event order must cover each event exactly once")
    used_paths = set()
    for mid, model in models.items():
        require(model.get("website_url") == f"https://wumbolabs.dev/evaluations/{model['website_slug']}/", f"invalid website URL: {mid}")
        state = model["current_state"]
        require(state["recommended_profile_id"] in profiles, f"unknown recommended profile: {mid}")
        require(profiles[state["recommended_profile_id"]]["model_id"] == mid, f"cross-model recommendation: {mid}")
        require(set(state["event_ids"]) <= events.keys(), f"unknown current-state event: {mid}")
        require(all(mid in event_models(events[eid]) for eid in state["event_ids"]), f"cross-model current-state event: {mid}")
    for pid, profile in profiles.items():
        require(profile["model_id"] in models, f"unknown profile model: {pid}")
        require(set(profile["event_ids"]) <= events.keys(), f"unknown profile event: {pid}")
        require(profile.get("profile_path") == f"models/{profile['model_id']}/profiles/{pid}", f"profile path identity mismatch: {pid}")
        require(profile.get("repository") == REPO, f"invalid current profile repository: {pid}")
        expected_events = {eid for eid, event in events.items() if pid in event_profiles(event)}
        require(len(profile["event_ids"]) == len(set(profile["event_ids"])) and set(profile["event_ids"]) == expected_events, f"incomplete profile event relationships: {pid}")
        require(bool(profile.get("legacy_sources")) or bool(profile.get("publication_provenance")), f"missing profile provenance: {pid}")
    for eid, event in events.items():
        mids, pids = event_models(event), event_profiles(event)
        require(bool(mids) and len(mids) == len(set(mids)) and set(mids) <= models.keys(), f"invalid event models: {eid}")
        require(bool(pids) and len(pids) == len(set(pids)) and set(pids) <= profiles.keys(), f"invalid event profiles: {eid}")
        require(all(profiles[pid]["model_id"] in mids for pid in pids), f"cross-model event profile: {eid}")
        require(re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", event["event_date"]), f"invalid event date: {eid}")
        path = relative(event["event_path"])
        require(path not in used_paths, f"duplicate canonical event directory: {path}")
        used_paths.add(path)
        if event.get("shared_event_id"):
            require(len(mids) >= 2 and path == f"shared-events/{event['shared_event_id']}", f"invalid shared event: {eid}")
            require("model_id" not in event and "profile_id" not in event, f"shared event has fake owner: {eid}")
            attr = event["website_attribution"]
            require(attr["model_id"] in mids and attr["profile_id"] in pids, f"invalid shared attribution: {eid}")
        else:
            require(path == f"models/{event['model_id']}/events/{eid}", f"event path identity mismatch: {eid}")
        require(event["canonical_evidence"]["path"] == path + "/REPORT.md", f"report outside canonical event: {eid}")
        citation(event["canonical_evidence"])
        require(bool(event.get("legacy_sources")) or bool(event.get("publication_provenance")), f"event lacks provenance: {eid}")
        for field in ("source", "body_source"):
            source = event.get(field)
            if source:
                file = ROOT / relative(source["path"])
                require(file.is_file() and HASH.fullmatch(source["sha256"]) and digest(file) == source["sha256"], f"invalid {field} bytes: {eid}")
                require(SHA.fullmatch(source["commit"]), f"unpinned {field}: {eid}")
                verify_pin(source["commit"], source["path"])
    imports = load("provenance/legacy-imports.json")["imports"]
    seen = set()
    for record in imports:
        key = (record["legacy_repo"], record["legacy_commit"], record["legacy_path"])
        require(key not in seen, f"duplicate legacy source: {key}")
        seen.add(key)
        require(SHA.fullmatch(record["legacy_commit"]) and HASH.fullmatch(record["source_sha256"]), "invalid legacy source identity")
        path = record["canonical_path"]
        if path is None:
            require(record["import_result"] == "EXCLUDED_RAW_LOCALMAXXING_PAYLOAD", "unexplained legacy omission")
            continue
        require(record["canonical_repo"] == REPO, "invalid import destination")
        require(SHA.fullmatch(record["canonical_commit"]), "missing import commit")
        file = ROOT / relative(path)
        require(file.is_file(), f"missing imported file: {path}")
        verify_pin(record["canonical_commit"], path)
        if record["byte_identical"] == "YES":
            require(digest(file) == record["source_sha256"], f"changed scientific source bytes: {path}")
        else:
            require(bool(record["transformation"]) and digest(file) == record["canonical_sha256"], f"undocumented transformation: {path}")
    for source in registry["legacy_sources"]:
        expected = {(source["repo"], source["commit"], p) for p in source["paths"]}
        require(expected <= seen, f"incomplete legacy source coverage: {source['repo']}")
    for event in events.values():
        require(any(r["canonical_path"] == event["canonical_evidence"]["path"] for r in imports)
                or bool(event.get("publication_provenance")), f"report lacks artifact provenance: {event['event_id']}")
    return models, profiles, events


def generated(registry, models, profiles, events):
    outputs = {}

    def put(path, body):
        outputs[path] = GENERATED + body.rstrip() + "\n" if path.endswith(".md") else json.dumps(body, indent=2, ensure_ascii=False) + "\n"

    def link(path, label):
        return f"[{label}]({path})"

    model_rows = ["# Models", "", "| Model | Classification | Profiles | Events | Website |", "|---|---|---:|---:|---|"]
    profile_rows = ["# Profiles", "", "| Profile ID | Model | Status | Runtime / artifact |", "|---|---|---|---|"]
    event_rows = ["# Events", "", "One row per immutable event; shared reports are stored once. Newest first.", "", "| Date | Model(s) | Event type | Profile(s) | Report | Website |", "|---|---|---|---|---|---|"]
    for mid, model in models.items():
        mp = f"models/{mid}"
        state = model["current_state"]
        ps = [p for p in profiles.values() if p["model_id"] == mid]
        es = [e for e in events.values() if mid in event_models(e)]
        classification = state["classification"] or "No model-level classification published"
        model_rows.append(f"| {link(mp+'/', model['display_name'])} | {classification} | {len(ps)} | {len(es)} | {link(model['website_url'], 'Evaluation')} |")
        context_event = events.get(state.get("context"))
        context = load(context_event["source"]["path"]).get("context", {}) if context_event and context_event.get("source") else {}
        summary_parts = [
            f"{label}: {context[key]:,} tokens"
            for key, label in (("practical_default_tokens", "Practical default"),
                               ("guarded_tokens", "Guarded boundary"),
                               ("native_maximum_tokens", "Model-card native maximum"))
            if isinstance(context.get(key), int)
        ]
        context_summary = "; ".join(summary_parts) or model["context_summary"]
        lines = [f"# {model['display_name']}", "", f"**Classification:** {classification}", "", f"**Recommended profile:** `{state['recommended_profile_id']}`", "", f"**Context:** {context_summary}", ""]
        if summary_parts:
            lines += ["Advertised capacity is not useful-context validation; the report retains exact admission, validation, and extension dispositions.", "", "<details>", "<summary>Published context findings and limitations</summary>", "", model["context_summary"], "", "</details>", ""]
        lines += [f"[Human-facing Evaluation]({model['website_url']})", "", "## Profiles", ""]
        for p in ps:
            lines.append(f"- [{p['profile_id']}](profiles/{p['profile_id']}/) — {p['current_status']}; {p['runtime_family']}; {p['artifact']}")
        lines += ["", "## Testing history", ""]
        for e in sorted(es, key=lambda x: (x["event_date"], x["event_id"]), reverse=True):
            ep = "../../" + e["event_path"] if e.get("shared_event_id") else "events/" + e["event_id"]
            lines.append(f"- {e['event_date']} — [{e['event_title']}]({ep}/) — {e['welp_status']}; [{e['event_id']}]({ep}/REPORT.md)")
        lines += ["", "Current-state attribution is recorded in [model.json](model.json). Related shared events do not silently replace this model's classifications or context findings."]
        put(mp + "/README.md", "\n".join(lines))
        put(mp + "/model.json", model)
    for pid, p in profiles.items():
        pp = f"models/{p['model_id']}/profiles/{pid}"
        profile_rows.append(f"| {link(pp+'/', pid)} | {p['model_display_name']} | {p['current_status']} | {p['runtime_family']} / {p['artifact'].replace('|', '/')} |")
        lines = [f"# {p['profile_display_name']}", "", f"- **Profile ID:** `{pid}`", f"- **Model ID:** `{p['model_id']}`", f"- **Status:** {p['current_status']}", f"- **Artifact identity:** {p['artifact']}", f"- **Runtime family:** {p['runtime_family']}", f"- **Runtime revision:** {p.get('runtime_version', 'Not recorded in legacy descriptor')}", f"- **Quantization / precision:** {p.get('artifact_precision', 'See artifact identity; no separate legacy precision field')}", f"- **Deployment topology:** {p.get('deployment_topology', 'Not separately recorded in legacy descriptor')}", f"- **Hardware:** {p.get('hardware_scope', 'See reports')}", "", "[Model index](../../) · [Profile metadata](profile.json)", "", "## Events", ""]
        for eid in p["event_ids"]:
            e = events[eid]
            lines.append(f"- {e['event_date']} — [{e['event_title']}](../../../../{e['event_path']}/)")
        if (ROOT / pp / "supporting-evidence").is_dir():
            lines += ["", "[Supporting public evidence](supporting-evidence/) retains unindexed historical reports and reproduction artifacts without inventing new event identities."]
        lines += ["", "## Provenance", ""]
        for s in p.get("legacy_sources", []):
            lines.append(f"- [{s['repo']} @ `{s['commit']}`](https://github.com/{s['repo']}/blob/{s['commit']}/{s['path']})")
        lines += ["", "Repository boundaries are publication infrastructure, not scientific identity. Legacy descriptor fields are preserved with their original meaning in the provenance archive."]
        put(pp + "/README.md", "\n".join(lines))
        put(pp + "/profile.json", p)
    for e in sorted(events.values(), key=lambda x: (x["event_date"], x["event_id"]), reverse=True):
        names = ", ".join(models[mid]["display_name"] for mid in event_models(e))
        sites = " · ".join(link(models[mid]["website_url"], models[mid]["display_name"]) for mid in event_models(e))
        pids = ", ".join(f"`{pid}`" for pid in event_profiles(e))
        event_rows.append(f"| {e['event_date']} | {names} | {e['event_type']} | {pids} | {link(e['event_path']+'/REPORT.md', e['event_id'])} | {sites} |")
        lines = [f"# {e['event_title']}", "", f"- **Event ID:** `{e['event_id']}`", f"- **Date:** {e['event_date']}", f"- **Models:** {names}", f"- **Profiles:** {pids}", f"- **Type:** {e['event_type']}", f"- **Status:** {e['welp_status']}", f"- **Evidence maturity:** {e['evidence_maturity']}", "", "[Public scientific report](REPORT.md) · [Event metadata](event.json)", "", f"**Exact citation:** {citation(e['canonical_evidence'])}", "", f"**Browse results:** {sites}", "", "The report retains its originally published scope; a public summary is not represented as a full internal campaign report. Imported scientific bytes are unchanged. No public Lab Record companion was present unless explicitly linked here."]
        if e.get("shared_event_id"):
            lines += ["", f"**Shared event ID:** `{e['shared_event_id']}`. One report, no owner model. The website attribution only preserves pre-migration display and current-state precedence."]
        lines += ["", "## Provenance", ""]
        for s in e.get("legacy_sources", []):
            lines.append(f"- [{s['repo']} @ `{s['commit']}` — `{s['path']}`](https://github.com/{s['repo']}/blob/{s['commit']}/{s['path']})")
        for field, label in (("source", "Original public structured export"), ("body_source", "Original public narrative")):
            if e.get(field):
                lines.append(f"- [{label}](https://github.com/{REPO}/blob/{e[field]['commit']}/{e[field]['path']})")
        put(e["event_path"] + "/README.md", "\n".join(lines))
        put(e["event_path"] + "/event.json", e)
    put("MODELS.md", "\n".join(model_rows))
    put("PROFILES.md", "\n".join(profile_rows))
    put("EVENTS.md", "\n".join(event_rows))
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--scan-only", action="store_true")
    args = parser.parse_args()
    try:
        if args.scan_only:
            print(json.dumps(scan_public_tree(), indent=2))
            return 0
        registry = load("registry.json")
        models, profiles, events = validate(registry)
        changes = []
        for rel, content in generated(registry, models, profiles, events).items():
            path = ROOT / rel
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                changes.append(rel)
                if args.generate:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(content, encoding="utf-8")
        require(args.generate or not changes, f"generated indexes stale: {changes}")
        result = {"status": "PASS", "models": len(models), "profiles": len(profiles), "events": len(events), "shared_events": len(registry["shared_events"]), "generated_changes": len(changes), "public_safety": scan_public_tree()}
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
