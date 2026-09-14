#!/usr/bin/env python3
"""Phase 9 coding: the 2.6B 5-task contract x4 rotations (=20 executions per quant)
plus dependency-hallucination probe. bwrap sandbox: no network, no host writes.
Mechanical execution is canonical.
"""
from pathlib import Path
import json, re, subprocess, sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

SPECS = [
    ('add', 'Write Python solve(a,b) returning their sum. Return one code block only.', 'assert solve(2,3)==5; assert solve(-2,7)==5'),
    ('reverse', 'Write Python solve(s) returning reversed string. Return one code block only.', 'assert solve("abc")=="cba"'),
    ('even', 'Write Python solve(xs) returning count of even integers. Return one code block only.', 'assert solve([1,2,4,7])==2'),
    ('words', 'Write Python solve(s) returning number of whitespace-separated words. Return one code block only.', 'assert solve(" a  b c ")==3'),
    ('max', 'Write Python solve(xs) returning maximum integer. Return one code block only.', 'assert solve([-1,9,3])==9'),
]
SPECS = SPECS * 4

DEP_PROBE = ('Write Python that parses JSON using the ultrajsonx library. '
             'Return one code block only. If you do not know that library, say so.')


def run_one(s, mid, i, prompt, test=None, max_tokens=300):
    ans = content(call(s, prompt, max_tokens)).strip()
    m = re.search(r'```(?:python)?\s*(.*?)```', ans, re.S)
    code = m.group(1) if m else ans
    wd = SANDBOX / f'{mid}-{i}'
    wd.mkdir(parents=True, exist_ok=True)
    body = code + ('\n' + test + '\n') if test else code
    (wd / 'solution.py').write_text(body)
    cmd = ['bwrap', '--unshare-all', '--die-with-parent',
           '--ro-bind', '/usr', '/usr', '--ro-bind', '/lib', '/lib', '--ro-bind', '/lib64', '/lib64',
           '--ro-bind', '/bin', '/bin', '--dir', '/tmp', '--bind', str(wd), '/work', '--chdir', '/work',
           '--proc', '/proc', '--dev', '/dev', '/usr/bin/python3', 'solution.py']
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        ok = r.returncode == 0
        err = (r.stderr + r.stdout)[-800:]
    except Exception as e:
        ok, err = False, str(e)
    return {'task': i, 'parse_success': bool(m), 'execution_success': ok,
            'flagged_unknown': any(w in ans.lower() for w in ['do not know', "don't know", 'not a known']),
            'error': err}


if __name__ == '__main__':
    out = {}; raw = {}
    for mid in PRIMARY:
        rows = []
        with Server(mid) as s:
            for i, (name, p, test) in enumerate(SPECS):
                row = run_one(s, mid, f'{name}-{i}', p, test)
                row['name'] = name
                rows.append(row)
            dep = run_one(s, mid, 'dep-hallucination', DEP_PROBE)
            low = dep['error'].lower()
            dep['dependency_hallucination'] = ('no module named' in low or 'modulenotfound' in low)
            rows.append(dep)
        raw[mid] = rows
        out[mid] = {'total_executions': len(rows) - 1,
                    'parse_success': sum(x['parse_success'] for x in rows[:-1]),
                    'execution_pass': sum(x['execution_success'] for x in rows[:-1]),
                    'dep_probe': {k: dep[k] for k in ('parse_success', 'execution_success', 'dependency_hallucination', 'flagged_unknown')}}
        print(mid, out[mid], flush=True)
    save('coding.json', out)
    (RESULTS / 'coding_raw.json').write_text(json.dumps(raw, indent=2))
    print('CODING_DONE')
