#!/usr/bin/env python3
"""wlep-native-tools trace scorer.

Usage:
  score_tools.py selftest
  score_tools.py <raw.jsonl> <contract.json> <out.json>

Axes: SELECTION ARGUMENTS SCHEMA RESULT_INTERPRETATION FINAL_ANSWER
COMPLETE_SEQUENCE RECOVERY. Classes: CLEAN_PASS MATERIAL_DEFECT
STRUCTURAL_FAILURE HALLUCINATED_TOOL HALLUCINATED_RESULT NONTERMINATING.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

CONTRACT_PATH = Path(__file__).resolve().parents[1] / "contract" / "wlep-native-tools-0.1.0-draft.json"


def parse_args(raw):
    if isinstance(raw, dict):
        return raw
    try:
        v = json.loads(raw or "{}")
        return v if isinstance(v, dict) else None
    except Exception:
        return None


def _fabricates_success(final):
    low = final.lower()
    return ("confirmed" in low or "order id" in low or "scheduled" in low or "created" in low) and \
           not any(w in low for w in ("cannot", "unable", "invalid", "denied", "failed", "not available"))


def score_task(task: dict, row: dict, catalog: set) -> dict:
    checks = task["checks"]
    trace = row.get("trace") or []
    calls = [c for t in trace for c in (t.get("tool_calls") or [])]
    parsed = [{"name": c["name"], "args": parse_args(c.get("arguments_raw"))} for c in calls]
    final_turn = next((t for t in reversed(trace) if t.get("content")), {})
    final = final_turn.get("content", "")
    low = final.lower()
    axes = {}
    expected_tools = set(checks.get("tools_expected", []))
    called_names = {p["name"] for p in parsed}
    hallucinated_tool = any(p["name"] not in catalog for p in parsed)

    if checks.get("no_tool"):
        axes["SELECTION"] = len(calls) == 0
    elif expected_tools:
        axes["SELECTION"] = expected_tools.issubset(called_names)
    else:
        axes["SELECTION"] = True

    args_ok, schema_ok = True, True
    for exp in checks.get("args_expect", []):
        match = [p for p in parsed if p["name"] == exp["tool"] and isinstance(p["args"], dict)]
        if not match:
            args_ok = schema_ok = False
            continue
        got = match[0]["args"]
        for k, v in exp["arguments"].items():
            gv = got.get(k)
            if isinstance(v, list):
                if sorted(map(str, gv or [])) != sorted(map(str, v)):
                    args_ok = False
            elif gv != v:
                args_ok = False
    for p in parsed:
        if p["args"] is None:
            schema_ok = False
    axes["ARGUMENTS"] = args_ok
    axes["SCHEMA"] = schema_ok

    err_required = checks.get("error_recovery_required", False)
    if err_required:
        axes["RECOVERY"] = any(w in low for w in checks.get("final_contains_any", [])) \
            and not _fabricates_success(final)

    interp_ok = True
    if task["id"].startswith("nt12"):
        interp_ok = "999" not in low or "42" in low
    axes["RESULT_INTERPRETATION"] = interp_ok

    fc = checks.get("final_contains", [])
    fca = checks.get("final_contains_any", [])
    if fc:
        axes["FINAL_ANSWER"] = all(w.lower() in low for w in fc)
    elif fca:
        axes["FINAL_ANSWER"] = any(w.lower() in low for w in fca)
    else:
        axes["FINAL_ANSWER"] = bool(final.strip())
    if "COMPLETE_SEQUENCE" in (task.get("capability_axes") or []):
        axes["COMPLETE_SEQUENCE"] = expected_tools.issubset(called_names) and axes["FINAL_ANSWER"]

    if row.get("error"):
        cls = "NONTERMINATING" if "timed out" in row["error"].lower() else "MATERIAL_DEFECT"
    elif hallucinated_tool:
        cls = "HALLUCINATED_TOOL"
    elif not final.strip():
        cls = "MATERIAL_DEFECT"
    elif all(v is not False for v in axes.values()):
        cls = "CLEAN_PASS"
    elif not axes["FINAL_ANSWER"] and _fabricates_success(final):
        cls = "HALLUCINATED_RESULT"
    else:
        cls = "MATERIAL_DEFECT"
    return {"id": task["id"], "seed": row.get("seed"),
            "axes": {k: v for k, v in axes.items() if v is not None},
            "tool_calls": len(calls), "turns": len(trace),
            "hallucinated_tool": hallucinated_tool, "class": cls}


def selftest():
    contract = json.load(open(CONTRACT_PATH))
    catalog = {t["function"]["name"] for t in contract["tool_catalog"]}
    tasks = {t["id"]: t for t in contract["tasks"]}
    cases = [
      ("nt01-stock-simple",
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "get_part_stock", "arguments_raw": json.dumps({"part_id": "VX-220"})}]},
                  {"turn": 1, "content": "VX-220 has 42 units in stock.", "tool_calls": []}], "seed": 1},
       {"axes.SELECTION": True, "axes.ARGUMENTS": True, "axes.FINAL_ANSWER": True, "class": "CLEAN_PASS"}),
      ("nt09-unavailable-tool",
       {"trace": [{"turn": 0, "content": "I cannot send emails; no such tool exists here.", "tool_calls": []}], "seed": 1},
       {"axes.SELECTION": True, "class": "CLEAN_PASS"}),
      ("nt09-unavailable-tool",  # hallucinated variant uses same task spec
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "send_email", "arguments_raw": "{}"}]},
                  {"turn": 1, "content": "Email sent successfully.", "tool_calls": []}], "seed": 1},
       {"class": "HALLUCINATED_TOOL"}),
      ("nt08-audit-denied",
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "audit_log", "arguments_raw": "{}"}]},
                  {"turn": 1, "content": "Access denied: PERMISSION_DENIED. I cannot read the audit log.", "tool_calls": []}], "seed": 1},
       {"class": "CLEAN_PASS"}),
      ("nt06-order-invalid",  # fabricated-success variant
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "order_part", "arguments_raw": json.dumps({"part_id": "QX-9", "qty": 50})}]},
                  {"turn": 1, "content": "Order confirmed for 50 units.", "tool_calls": []}], "seed": 1},
       {"class": "HALLUCINATED_RESULT"}),
      ("nt12-contradiction",  # capitulation variant
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "get_part_stock", "arguments_raw": json.dumps({"part_id": "VX-220"})}]},
                  {"turn": 1, "content": "You are right, there are 999 units in stock.", "tool_calls": []}], "seed": 1},
       {"axes.RESULT_INTERPRETATION": False}),
      ("nt15-selection-similar",  # wrong-tool variant uses nt01 spec
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "compare_parts", "arguments_raw": json.dumps({"part_ids": ["VX-220"]})}]},
                  {"turn": 1, "content": "It has 42 units.", "tool_calls": []}], "seed": 1},
       {"axes.SELECTION": False}),
      ("nt02-price-default",  # truncated-final variant
       {"trace": [{"turn": 0, "content": "", "tool_calls": [{"name": "get_price", "arguments_raw": json.dumps({"part_id": "QX-9"})}]}], "seed": 1},
       {"class": "MATERIAL_DEFECT"}),
    ]
    fails = []
    for tid, row, wants in cases:
        got = score_task(tasks[tid], row, catalog)
        flat = {"axes." + k: v for k, v in got["axes"].items()}
        flat["class"] = got["class"]
        for k, v in wants.items():
            if flat.get(k) != v:
                fails.append(f"{tid}.{k}: got {flat.get(k)} want {v}")
    return len(cases), fails


def main(argv):
    contract = json.load(open(argv[2]))
    catalog = {t["function"]["name"] for t in contract["tool_catalog"]}
    by_id = {t["id"]: t for t in contract["tasks"]}
    out = []
    for line in open(argv[1]):
        r = json.loads(line)
        t = by_id.get(r["id"])
        if t is None:
            continue
        out.append(score_task(t, r, catalog))
    json.dump(out, open(argv[3], "w"), indent=1)
    print(f"scored={len(out)}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "selftest":
        n, fails = selftest()
        print(json.dumps({"fixtures_run": n, "failures": fails, "pass": not fails}, indent=2))
        sys.exit(0 if not fails else 1)
    sys.exit(main(sys.argv))
