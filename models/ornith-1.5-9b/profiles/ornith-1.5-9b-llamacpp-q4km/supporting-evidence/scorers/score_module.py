#!/usr/bin/env python3
"""Generic mechanical scorer for raw-model Phase-5 module contracts.

Usage: score_module.py <raw.jsonl> <contract.json> <out.json>

Expectation kinds:
  exact            stripped output equals value
  contains_all     case-insensitive substrings; forbid list vetoes
  json_equal       parsed JSON deep-equals value
  schema_check     JSON object with required keys/types (+ optional no-extra)
  code_block_exact single fenced block containing all `need` strings
  final_line_exact last non-empty line starts with "FINAL: " and matches

Classification mirrors the wlep-reliability taxonomy.
"""
from __future__ import annotations
import json, re, sys


def score_text(text: str, expected: dict) -> tuple[bool, dict]:
    kind = expected["kind"]
    stripped = (text or "").strip()
    if kind == "exact":
        return stripped.strip(". \t") == expected["value"] or stripped == expected["value"], {"actual": stripped[:200]}
    if kind == "contains_all":
        low = (text or "").lower()
        missing = [v for v in expected.get("need", []) if v.lower() not in low]
        forbidden = [v for v in expected.get("forbid", []) if v.lower() in low]
        return (not missing and not forbidden), {"missing": missing, "forbidden_present": forbidden}
    if kind == "json_equal":
        try:
            m = re.search(r"[\[{].*[\]}]", stripped, re.S)
            value = json.loads(m.group(0) if m else stripped)
        except Exception as exc:
            return False, {"json_error": str(exc), "actual": stripped[:200]}
        return sorted_json(value) == sorted_json(expected["value"]), {"actual": value}
    if kind == "schema_check":
        try:
            m = re.search(r"[\[{].*[\]}]", stripped, re.S)
            value = json.loads(m.group(0) if m else stripped)
        except Exception as exc:
            return False, {"json_error": str(exc), "actual": stripped[:200]}
        d = validate_schema(value, expected["schema"], expected.get("allow_extra", True))
        return not d, {"violations": d}
    if kind == "code_block_exact":
        blocks = re.findall(r"```(?:\w+)?\s*(.*?)```", text or "", re.S)
        low = text.lower()
        missing = [v for v in expected.get("need", []) if v.lower() not in low]
        prose = bool(re.sub(r"```.+?```", "", (text or ""), flags=re.S).strip())
        ok = len(blocks) == 1 and not missing and not prose
        return ok, {"blocks_found": len(blocks), "missing": missing,
                    "prose_around": bool(re.sub(r"```.+?```", "", (text or ""), flags=re.S).strip())}
    if kind == "final_line_exact":
        lines = [l.strip() for l in (text or "").splitlines() if l.strip()]
        want = f"FINAL: {expected['value']}"
        got = next((l for l in reversed(lines) if l.upper().startswith("FINAL:")), None)
        return got is not None and got.strip().lower() == want.lower(), {"got": got}
    raise ValueError(f"unsupported kind {kind}")


def sorted_json(v):
    return json.dumps(v, sort_keys=True)


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)

def validate_schema(value, schema, allow_extra) -> list:
    errs = []
    spec = schema.get("required", {})
    tmap = {"str": str, "int": int, "bool": bool, "float": float}
    if not isinstance(value, dict):
        return ["NOT_AN_OBJECT"]
    for k, rule in spec.items():
        if k not in value:
            errs.append(f"MISSING:{k}")
            continue
        v = value[k]
        if rule == "null_or_str" and (v is None or isinstance(v, str)):
            continue
        if rule.startswith("enum:"):
            if v not in rule[5:].split("|"):
                errs.append(f"ENUM:{k}")
            continue
        if rule.startswith("array_of_obj:"):
            if not isinstance(v, list) or not v:
                errs.append(f"ARRAY:{k}")
                continue
            keys = [kv.split(":")[0] for kv in rule[13:].split(",")]
            types = {kv.split(":")[0]: kv.split(":")[1] for kv in rule[13:].split(",")}
            for item in v:
                if not isinstance(item, dict):
                    errs.append(f"ARRAY_ITEM:{k}")
                    break
                for kk, tt in types.items():
                    want = tmap[tt]
                    if kk not in item or (want is int and not _is_int(item[kk])) or (want is not int and not isinstance(item[kk], want)):
                        errs.append(f"ARRAY_FIELD:{k}.{kk}")
                        break
            continue
        if ":" in rule and rule.split(":")[0] == "int":
            lo, hi = map(int, rule.split(":")[1].split(".."))
            if not (_is_int(v) and lo <= v <= hi):
                errs.append(f"RANGE:{k}")
            continue
        want = tmap.get(rule)
        if want is None:
            errs.append(f"RULE:{k}")
        elif want is int and not _is_int(v):
            errs.append(f"TYPE:{k}")
        elif want is not int and not isinstance(v, want):
            errs.append(f"TYPE:{k}")
    if not allow_extra:
        extra = set(value) - set(spec)
        if extra:
            errs.append("EXTRA:" + ",".join(sorted(extra)))
    return errs


def classify(category: str, passed: bool, detail: dict, error, finish_reason) -> str:
    if error:
        return "NONTERMINATING" if "timed out" in error.lower() else "MATERIAL_DEFECT"
    if passed:
        return "CLEAN_PASS"
    if detail.get("json_error") or category == "strict_interfaces" or detail.get("violations"):
        return "STRUCTURAL_FAILURE"
    if finish_reason == "length":
        return "MATERIAL_DEFECT"
    return "MATERIAL_DEFECT"


def main(argv):
    contract = json.load(open(argv[2]))
    exp = {t["id"]: t["expected"] for t in contract["tasks"]}
    cat = {t["id"]: t["category"] for t in contract["tasks"]}
    out = []
    for line in open(argv[1]):
        r = json.loads(line)
        e = exp.get(r["id"])
        if e is None or r.get("reasoning_mode", "off") != "off":
            if e is None:
                continue
        passed, detail = score_text(r.get("output") or "", e)
        cls = classify(cat[r["id"]], passed, detail, r.get("error"), r.get("finish_reason"))
        out.append({"id": r["id"], "seed": r.get("seed"), "passed": passed, "class": cls,
                    "detail": detail})
    json.dump(out, open(argv[3], "w"), indent=1)
    print(f"scored={len(out)}")


if __name__ == "__main__":
    main(sys.argv)
