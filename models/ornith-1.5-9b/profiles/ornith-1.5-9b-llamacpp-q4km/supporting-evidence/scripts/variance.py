#!/usr/bin/env python3
"""wlep-variance analyzer (DRAFT): consumes per-seed gate-relevant rates.
Usage: variance.py <summary.json with per_seed {seed: rate}> [threshold=0.5]
Verdicts: STABLE UNSTABLE ESCALATE_TO_5 HUMAN_REVIEW"""
import json,sys
def analyze(per_seed,threshold=None):
    v=list(per_seed.values())
    rng=max(v)-min(v)
    if threshold and all(abs(x-threshold)<=0.05 for x in v): return "ESCALATE_TO_5"
    if len(set(round(x,4) for x in v))==1 or rng<=0.10: return "STABLE"
    if rng>0.25: return "HUMAN_REVIEW"
    return "ESCALATE_TO_5"
if __name__=="__main__":
    d=json.load(open(sys.argv[1])); th=sys.argv[2] if len(sys.argv)>2 else None
    print(json.dumps(analyze(d,float(th) if th else None)))
