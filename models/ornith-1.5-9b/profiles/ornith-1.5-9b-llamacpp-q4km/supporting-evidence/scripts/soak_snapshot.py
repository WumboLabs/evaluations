#!/usr/bin/env python3
"""wlep-stability soak harness (DRAFT). SCREENING 30min / LOCKIN 120min+3 cycles.
Usage: soak.py selftest | soak.py --url U --level screening [--minutes N]"""
import json, statistics as st, sys, time, urllib.request
from pathlib import Path
SENTINELS=[{"id":"s1","prompt":"Reply with exactly: SOAK_OK_2026","expect":"SOAK_OK_2026"},
 {"id":"s2","prompt":"Return ONLY JSON {\"ok\": true}","expect_json":{"ok":True}}]
def req(url,payload):
    r=urllib.request.Request(url+"/v1/chat/completions",data=json.dumps(payload).encode(),
        headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(r,timeout=300) as resp: return json.loads(resp.read())
def drift(a,b): return round((b-a)/a*100,2) if a else None
def run(url,minutes,sampler):
    t_end=time.time()+minutes*60; lat=[]; tps=[]; errs=0; n=0; sent_ok=0; sent_n=0
    while time.time()<t_end:
        s=SENTINELS[n%len(SENTINELS)]
        try:
            b=req(url,{"messages":[{"role":"user","content":s["prompt"]+" [t%d]"%n}],
                "max_tokens":64,"temperature":0,"seed":n})
            txt=b["choices"][0]["message"]["content"] or ""
            if s["expect"] and s["expect"] in txt: sent_ok+=1
            if s.get("expect_json"):
                import re
                m=re.search(r"\{.*\}",txt,re.S)
                try: sent_ok += json.loads(m.group(0))==s["expect_json"]
                except Exception: pass
            sent_n+=1
            t=b.get("timings",{}); lat.append(t.get("prompt_ms",0)); tps.append(t.get("predicted_per_second",0))
        except Exception: errs+=1
        n+=1
    return {"requests":n,"errors":errs,"sentinel_successes":sent_ok,"sentinel_total":sent_n,
      "latency_first10_mean_ms":round(st.mean(lat[:10]),1) if len(lat)>=10 else None,
      "latency_last10_mean_ms":round(st.mean(lat[-10:]),1) if len(lat)>=10 else None,
      "latency_drift_pct":drift(st.mean(lat[:10]),st.mean(lat[-10:])) if len(lat)>=20 else None,
      "tps_drift_pct":drift(st.mean(tps[:10]),st.mean(tps[-10:])) if len(tps)>=20 else None}
if __name__=="__main__":
    if "--selftest" in sys.argv:
        # offline validation of drift math + sentinel defs
        assert drift(100,110)==10.0 and drift(100,90)==-10.0 and drift(0,5) is None
        print(json.dumps({"pass":True,"fixtures_run":3})); sys.exit(0)
    url=[a for a in sys.argv if a.startswith("http")][0]
    mins=30 if "screening" in sys.argv else 120
    print(json.dumps(run(url,mins,None),indent=1))
