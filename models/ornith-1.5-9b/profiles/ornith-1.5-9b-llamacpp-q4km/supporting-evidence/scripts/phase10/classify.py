#!/usr/bin/env python3
"""wlep-final-classification engine (DRAFT). Consumes campaign evidence JSON.
Usage: classify.py <evidence.json>
Evidence keys: phase4_gate_decision, modules{coding:{class},native_tools:{},extraction_rag:{},reasoning:{delta}},
context_useful_ceiling, producer_claims{}. Emits roles x readiness deterministically."""
import json,sys
ROLES={
 "coding_specialist":{"requires_module_pass":"coding"},
 "tool_agent":{"requires_module_pass":"native_tools"},
 "omp_agent":{"requires_module_pass":"omp_local_agent","also":"phase4 ADVANCE"},
 "extraction_helper":{"requires_module_pass":"extraction_rag"},
 "router_classifier":{"requires_module_pass":"structured_interfaces"},
 "primary_assistant":{"requires_all":["structured_interfaces","linux_systems"],"also":"phase4 ADVANCE"}}
def classify(ev):
    adv = ev.get("phase4_gate_decision")=="ADVANCE"
    mods={k.lower():v.get("class") for k,v in ev.get("modules",{}).items()}
    out={"roles":[],"readiness":None,"guardrails":ev.get("guardrails",[]),
         "not_reached":[k for k,v in ev.get("modules",{}).items() if v.get("class")=="NOT_REACHED"],
         "producer_claims_separate":ev.get("producer_claims",{})}
    for role,req in ROLES.items():
        ok=True
        if req.get("also")=="phase4 ADVANCE" and not adv: ok=False
        mp=req.get("requires_module_pass")
        if mp and mods.get(mp)!="PASS": ok=False
        for m in req.get("requires_all",[]):
            if mods.get(m)!="PASS": ok=False
        if ok: out["roles"].append(role)
    if not out["roles"]:
        out["readiness"]="NOT_READY" if not adv else "LIMITED_ROLE_ONLY"
    elif ev.get("guardrails"): out["readiness"]="READY_WITH_GUARDRAILS"
    else: out["readiness"]="READY"
    return out
if __name__=="__main__":
    print(json.dumps(classify(json.load(open(sys.argv[1]))),indent=1))
