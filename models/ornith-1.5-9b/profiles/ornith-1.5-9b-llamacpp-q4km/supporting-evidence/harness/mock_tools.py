#!/usr/bin/env python3
"""Deterministic mock tool execution for wlep-native-tools. No network, no state leakage.

execute(name, arguments) -> dict result (may contain {"error": ...}).
"""
import json
from pathlib import Path

CONTRACT = json.load(open(Path(__file__).resolve().parents[1] / "contract" / "wlep-native-tools-0.1.0-draft.json"))
STOCK = {"VX-220": 42, "QX-9": 310, "RTR-B-CARD": 7}
PRICES = {("QX-9", "USD"): 19, ("QX-9", "EUR"): 17, ("VX-220", "USD"): 249, ("VX-220", "EUR"): 229}
LISTS = {
    "gpu": [{"part_id": "VX-220", "name": "Meridian accelerator"}, {"part_id": "GPU-LEGACY", "name": "Legacy adapter"}],
    "cooling": [{"part_id": "QX-9", "name": "Nordwind fan controller"}],
    "network": [{"part_id": "RTR-B-CARD", "name": "Site B line card"}],
}
_ORDER_SEQ = iter(["ORD-1001", "ORD-1002", "ORD-1003", "ORD-1004", "ORD-1005"])
CATALOG = {t["function"]["name"] for t in CONTRACT["tool_catalog"]}
SCHEMAS = {t["function"]["name"]: t["function"]["parameters"] for t in CONTRACT["tool_catalog"]}


def schema_error(name, args):
    req = SCHEMAS.get(name, {}).get("required", [])
    props = SCHEMAS.get(name, {}).get("properties", {})
    for k in req:
        if k not in args:
            return f"MISSING_REQUIRED: {k}"
    for k, v in args.items():
        spec = props.get(k)
        if spec is None:
            continue
        if "enum" in spec and v not in spec["enum"]:
            return f"INVALID_ENUM: {k}={v!r}"
        tmap = {"string": str, "integer": int, "boolean": bool, "array": list, "object": dict}
        want = tmap.get(spec.get("type"))
        if want is int and isinstance(v, bool):
            return f"INVALID_TYPE: {k}"
        if want is not None and not isinstance(v, want):
            return f"INVALID_TYPE: {k}"
        if k == "qty" and not (isinstance(v, int) and 1 <= v <= 10):
            return "INVALID_RANGE: qty must be integer 1..10"
        if k == "target" and isinstance(v, dict):
            if "part_id" not in v or not isinstance(v["part_id"], str):
                return "INVALID_NESTED: target.part_id"
    return None


def execute(name, args):
    if name not in CATALOG:
        return {"error": "UNKNOWN_TOOL"}
    err = schema_error(name, args)
    if err:
        return {"error": err}
    if name == "get_part_stock":
        pid = args["part_id"]
        return {"part_id": pid, "stock": STOCK.get(pid, 0)}
    if name == "get_price":
        cur = args.get("currency", "USD")
        key = (args["part_id"], cur)
        if cur not in ("USD", "EUR"):
            return {"error": f"INVALID_ENUM: currency={cur}"}
        if key not in PRICES:
            return {"error": "UNKNOWN_PART"}
        return {"part_id": args["part_id"], "currency": cur, "price": PRICES[key]}
    if name == "list_parts":
        rows = LISTS.get(args["category"], [])
        if args.get("in_stock_only"):
            rows = [r for r in rows if STOCK.get(r["part_id"], 0) > 0]
        return {"parts": rows}
    if name == "order_part":
        try:
            oid = next(_ORDER_SEQ)
        except StopIteration:
            oid = "ORD-EXHAUSTED"
        return {"order_id": oid, "part_id": args["part_id"], "qty": args["qty"], "status": "confirmed"}
    if name == "schedule_maintenance":
        return {"ticket": "MTN-" + args["date"].replace("-", ""), "lead_time_hours": 48 if args["priority"] == "routine" else 0}
    if name == "audit_log":
        return {"error": "PERMISSION_DENIED"}
    if name == "create_alert":
        return {"alert_id": f"ALRT-{args['target']['part_id']}-{args['threshold']}", "created": True}
    if name == "compare_parts":
        rows = [{"part_id": p, "stock": STOCK.get(p, 0),
                 "price_usd": PRICES.get((p, "USD"))} for p in args["part_ids"]]
        return {"comparison": rows}
    return {"error": "UNIMPLEMENTED"}


def selftest():
    cases = [
        (execute("get_part_stock", {"part_id": "VX-220"}), {"part_id": "VX-220", "stock": 42}),
        (execute("get_price", {"part_id": "QX-9"}), {"part_id": "QX-9", "currency": "USD", "price": 19}),
        (execute("get_price", {"part_id": "QX-9", "currency": "GBP"})["error"].startswith("INVALID_ENUM"), True),
        (execute("order_part", {"part_id": "QX-9", "qty": 50})["error"], "INVALID_RANGE: qty must be integer 1..10"),
        (execute("order_part", {"part_id": "VX-220", "qty": "three"})["error"], "INVALID_TYPE: qty"),
        (execute("audit_log", {}), {"error": "PERMISSION_DENIED"}),
        (execute("send_email", {})["error"], "UNKNOWN_TOOL"),
        (execute("create_alert", {"target": {"part_id": "QX-9"}, "threshold": 25})["created"], True),
        (execute("compare_parts", {"part_ids": ["VX-220", "QX-9"]})["comparison"][1]["stock"], 310),
        ("part_id" in execute("create_alert", {"target": {}, "threshold": 25})["error"], True),
    ]
    fails = []
    for i, (got, want) in enumerate(cases):
        if got != want:
            fails.append(f"case{i}: got {got!r} want {want!r}")
    return len(cases), fails


if __name__ == "__main__":
    n, fails = selftest()
    print(json.dumps({"fixtures_run": n, "failures": fails, "pass": not fails}, indent=2))
