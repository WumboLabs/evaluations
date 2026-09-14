#!/usr/bin/env python3
"""wlep-module-coding scorer (DRAFT). Sandbox-executes promoted coding tasks.

Usage:
  score_coding.py selftest
  score_coding.py score <raw.jsonl> <contract.json> <out.json>
Classes: CLEAN_PASS STRUCTURAL_FAILURE HALLUCINATION MATERIAL_DEFECT NONTERMINATING
"""
import json, subprocess, sys, tempfile, shutil, re
from pathlib import Path

def extract_code(text):
    m = re.findall(r"```(?:python)?\s*(.*?)```", text or "", re.S)
    return (m[0] if m else (text or "")).strip()

def sandbox_run(source, test_program, tag):
    work = Path(tempfile.mkdtemp(prefix=tag+"-"))
    runner = work/"runner.py"
    code = ("import resource\n"
            "resource.setrlimit(resource.RLIMIT_CPU,(3,3))\n"
            "resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))\n"
            + source + "\n\n" + test_program + "\n")
    runner.write_text(code)
    cmd=["bwrap","--unshare-all","--new-session","--die-with-parent","--tmpfs","/",
         "--dir","/usr","--ro-bind","/usr","/usr","--dir","/lib","--ro-bind","/lib","/lib",
         "--dir","/lib64","--ro-bind","/lib64","/lib64","--dir","/work","--bind",str(work),"/work",
         "--dir","/tmp","--proc","/proc","--dev","/dev","--chdir","/work",
         "/usr/bin/python3","/work/runner.py"]
    try:
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=8)
        out={"executed":True,"returncode":r.returncode,"stdout":r.stdout[-2000:],"stderr":r.stderr[-2000:],"passed":r.returncode==0}
    except subprocess.TimeoutExpired:
        out={"executed":True,"timeout":True,"passed":False}
    except Exception as e:
        out={"executed":False,"error":repr(e),"passed":False}
    finally:
        shutil.rmtree(work,ignore_errors=True)
    return out

def classify(detail):
    if not detail.get("executed"):
        return "NONTERMINATING" if detail.get("timeout") else "MATERIAL_DEFECT"
    err=(detail.get("stderr") or "")
    if detail.get("timeout"): return "NONTERMINATING"
    if detail.get("passed"): return "CLEAN_PASS"
    if "ModuleNotFoundError" in err or "ImportError" in err: return "HALLUCINATION"
    if "SyntaxError" in err: return "STRUCTURAL_FAILURE"
    return "MATERIAL_DEFECT"

FIX=[ # (name, source, test, want)
 ("pass_simple","def add(a,b):\n    return a+b\n","assert add(2,3)==5",  "CLEAN_PASS"),
 ("fail_test","def add(a,b):\n    return a-b\n","assert add(2,3)==5",   "MATERIAL_DEFECT"),
 ("syntax","def add(:\n    return 1\n","assert True",                  "STRUCTURAL_FAILURE"),
 ("halluc_dep","import nonexistent_lib_xyz\n","assert True",            "HALLUCINATION"),
]

def selftest():
    fails=[]
    for name,src,test,want in FIX:
        got=classify(sandbox_run(src,test,"selftest-"+name))
        if got!=want: fails.append(f"{name}: {got} != {want}")
    return len(FIX),fails

if __name__=="__main__":
    a=sys.argv
    if len(a)>=2 and a[1]=="selftest":
        n,f=selftest(); print(json.dumps({"fixtures_run":n,"failures":f,"pass":not f},indent=2)); sys.exit(0 if not f else 1)
    if len(a)>=5 and a[1]=="score":
        contract=json.load(open(a[3])); tests={t["id"]:t["expected"].get("test_program","") for t in contract["tasks"]}
        rows=[json.loads(l) for l in open(a[2])]
        out=[]
        for r in rows:
            if r["id"] not in tests: continue
            d=sandbox_run(extract_code(r.get("output")),tests[r["id"]],r["id"]+"-s"+str(r.get("seed")))
            out.append({"id":r["id"],"seed":r.get("seed"),"class":classify(d),"detail":{k:v for k,v in d.items() if k!="source"}})
        json.dump(out,open(a[4],"w"),indent=1); print(f"scored={len(out)}"); sys.exit(0)
    print(__doc__); sys.exit(2)
