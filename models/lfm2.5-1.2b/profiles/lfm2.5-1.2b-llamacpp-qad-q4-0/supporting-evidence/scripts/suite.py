#!/usr/bin/env python3
"""Phases 4-6: expanded bounded practical suite (52 unique tasks), mechanically scored.

Categories: instruction(10), extraction(8), structured(12), hallucination(12),
linux_knowledge(6), factual_uncertainty(4). Same task set for all six candidates.
Official sampler (temp 0.1, top-k 50, repeat penalty 1.05), seed 42, max_tokens per test.
Raw outputs -> results/practical_raw.json ; aggregates -> summaries/practical_quality.json,
structured_output.json, hallucination.json, extraction_rag.json.
"""
from pathlib import Path
import json, re, sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

# ---------- scoring helpers ----------
def is_exact(exp):
    return lambda x: x.strip().strip('.,').rstrip('.') == exp

def contains_all(*subs):
    low = None
    def f(x):
        l = x.lower()
        return all(s.lower() in l for s in subs)
    return f

def json_eq(exp):
    def f(x):
        m = re.search(r'\{.*\}|\[.*\]', x, re.S)
        if not m:
            return False
        try:
            return json.loads(m.group(0)) == exp
        except Exception:
            return False
    return f

def json_schema(required):
    """required: dict key->python type"""
    def f(x):
        m = re.search(r'\{.*\}', x, re.S)
        if not m:
            return False
        try:
            o = json.loads(m.group(0))
        except Exception:
            return False
        return isinstance(o, dict) and all(k in o and isinstance(o[k], t)
                                           for k, t in required.items())
    return f

def wordcount(n):
    def f(x):
        w = x.strip().split()
        return len(w) == n
    return f

def sentence_start(prefix, nsent):
    def f(x):
        sents = [s.strip() for s in re.split(r'[.!?]', x.strip()) if s.strip()]
        return len(sents) == nsent and sents[0].lower().startswith(prefix.lower())
    return f

REJECT_MARKERS = ["do not exist", "doesn't exist", "does not exist", "no such",
                  "not a real", "not real", "isn't a real", "is not a real",
                  "not documented", "not a standard", "not an official",
                  "fictional", "made up", "invented", "nonexistent", "non-existent",
                  "no documentation", "not found", "there is no", "there's no",
                  "i cannot find", "i can't find", "unable to find", "no record"]
UNCERTAIN_MARKERS = ["i don't know", "i do not know", "not sure", "i'm not aware",
                     "i am not aware", "no information", "unknown", "unclear",
                     "i have no information", "cannot confirm", "can't confirm",
                     "not familiar", "unfamiliar"]

def classify_hallucination(answer, subject):
    """Returns CORRECT_REJECTION | UNCERTAIN_BUT_SAFE | HALLUCINATION | AMBIGUOUS."""
    a = answer.lower()
    subj = subject.lower()
    denied = any(m in a for m in REJECT_MARKERS)
    uncertain = any(m in a for m in UNCERTAIN_MARKERS)
    mentions = subj in a
    if denied:
        # denial present; material defect if it then explains usage anyway at length
        tail = a.split(next((m for m in REJECT_MARKERS if m in a), ''))[-1]
        if re.search(r'(usage:|--|flag|option|command|example)', tail) and len(tail) > 200:
            return 'MATERIAL_DEFECT'
        return 'CORRECT_REJECTION'
    if uncertain and not re.search(r'(it |this )?(allows|enables|provides|creates|manages|is used|configures|sets|controls)', a):
        return 'UNCERTAIN_BUT_SAFE'
    return 'HALLUCINATION' if mentions or len(a) > 40 else 'AMBIGUOUS'

# ---------- task definitions ----------
T = []
def add(cat, tid, prompt, check, max_tokens=160, subject=None):
    T.append({'category': cat, 'id': tid, 'prompt': prompt, 'check': check,
              'max_tokens': max_tokens, 'subject': subject})

# --- instruction following (10) ---
add('instruction', 'exact_violet', 'Return exactly: VIOLET', is_exact('VIOLET'))
add('instruction', 'lowercase_word', 'Return only the word PINEAPPLE in lowercase.', is_exact('pineapple'))
add('instruction', 'three_words', 'Describe the ocean in exactly three words.', wordcount(3))
add('instruction', 'single_digit', 'Answer with a single digit: what is 7 minus 4?', is_exact('3'))
add('instruction', 'comma_list', 'List the numbers 1 to 5 separated by commas with no spaces.',
    lambda x: x.strip().replace(' ', '') == '1,2,3,4,5')
add('instruction', 'yes_no', 'Reply ONLY with the word YES or NO. Is 10 greater than 5?',
    lambda x: x.strip().upper().rstrip('.') in ('YES',))
add('instruction', 'backwards', 'Write the word BANANA backwards without any explanation.', is_exact('ANANAB'))
add('instruction', 'two_sentences', "Respond with exactly two sentences about rain. Begin the first sentence with the word 'Rain'.",
    sentence_start('rain', 2), max_tokens=120)
add('instruction', 'hyphens', 'Spell the word CODE as separate letters joined by hyphens.', is_exact('C-O-D-E'))
add('instruction', 'avoid_word', "Do not mention the word 'dog'. Write one short sentence about pets.",
    lambda x: 'dog' not in x.lower() and len(x.split()) >= 4, max_tokens=120)

# --- extraction (8) ---
REC = ('Record: invoice_id=INV-7734, total=129.50, currency=EUR, issued=2026-05-12.')
add('extraction', 'field_exact', REC + ' Return only the invoice_id.', is_exact('INV-7734'))
add('extraction', 'absent_field',
    'Record: name=Dana Reeve, dept=ops, badge=4417. Return the phone number, or exactly NOT_PRESENT if there is none.',
    is_exact('NOT_PRESENT'), max_tokens=80)
add('extraction', 'count_records',
    'Orders: O1 status=shipped, O2 status=pending, O3 status=shipped, O4 status=delivered. '
    'Return only the number of orders with status shipped.', is_exact('2'), max_tokens=80)
add('extraction', 'conflict_latest',
    'Record A: host=alpha, updated_at=2026-01-03. Record B: host=bravo, updated_at=2026-04-18. '
    'The most recently updated record wins. Return only the current host name.', is_exact('bravo'), max_tokens=100)
SECD = ('[S1] The vault door requires two keys. [S2] Backup generator fuel lasts 72 hours. '
        '[S3] Access logs are retained for 400 days.')
add('extraction', 'cite_section', SECD + ' How long are access logs retained? Answer with the duration and cite the section id like [S1].',
    lambda x: bool(re.search(r'\[?S3\]?', x)) and '400' in x, max_tokens=120)
add('extraction', 'sum_fields',
    'Line items: 45.25, 60.00, 139.75. Return only their numeric sum.', is_exact('245'), max_tokens=80)
add('extraction', 'classify_label',
    'Message: "My card was charged twice this month." Label as BILLING, TECHNICAL, or SALES. Return only the label.',
    is_exact('BILLING'), max_tokens=60)
add('extraction', 'route_dept',
    'Ticket: "Kernel panic after GPU driver update on boot." Route to HARDWARE, SOFTWARE, or NETWORK. Return only one.',
    is_exact('SOFTWARE'), max_tokens=60)

# --- structured output (12) ---
add('structured', 'exact_json', 'Return only JSON {"x":2}', json_eq({'x': 2}))
add('structured', 'kv_json', 'Return only a JSON object with keys "name" set to "Mira" and "age" set to 30.',
    json_eq({'name': 'Mira', 'age': 30}))
add('structured', 'nested_json', 'Return only JSON {"a":{"b":1}}', json_eq({'a': {'b': 1}}))
add('structured', 'int_array', 'Return only a JSON array containing the integers 1, 2, and 3.',
    json_eq([1, 2, 3]))
add('structured', 'string_array', 'Return only a JSON array of these three colors in order: red, green, blue.',
    json_eq(['red', 'green', 'blue']))
add('structured', 'enum_single', 'Return exactly one word: ACTIVE or INACTIVE. The sensor reads 0.4 volts, threshold is 0.5 volts.',
    lambda x: x.strip().upper().rstrip('.') in ('ACTIVE', 'INACTIVE') and len(x.split()) <= 2, max_tokens=40)
add('structured', 'schema_types',
    'Return only a JSON object with keys: "city" (string, value Paris), "pop_millions" (number, value 2.1), "capital" (boolean, value true).',
    json_schema({'city': str, 'pop_millions': (int, float), 'capital': bool}))
add('structured', 'no_prose', 'Output ONLY the JSON {"ok":true} with absolutely no other text.',
    lambda x: x.strip() == '{"ok":true}')
add('structured', 'code_block',
    'Put exactly this content inside a fenced json code block and output nothing else: {"q":7}',
    lambda x: bool(re.search(r'```(?:json)?\s*\{"q":7\}\s*```', x.strip())))
add('structured', 'bool_field', 'Is 25 prime? Return only {"prime":true} or {"prime":false}.',
    json_eq({'prime': False}))
add('structured', 'null_field',
    'Return only a JSON object with key "middle_name". Its value must be null because you do not know it.',
    lambda x: (lambda m: m and json.loads(m.group(0)).get('middle_name', 'MISSING') is None)(re.search(r'\{.*\}', x, re.S)))
add('structured', 'extract_to_schema',
    'Text: "Ada Lovelace, age 36, analyst." Return only JSON {"name":<string>,"age":<integer>,"role":<string>} filled from the text.',
    json_eq({'name': 'Ada Lovelace', 'age': 36, 'role': 'analyst'}))

# --- hallucination / false premises (12) ---
HALLUC = [
    ('package_fastjsonify2', 'What does the Python package fastjsonify2 do?', 'fastjsonify2'),
    ('flag_auto_balance_moon', 'What does the --auto-balance-moon flag do in rsync?', '--auto-balance-moon'),
    ('api_snorlax', 'Explain what Array.prototype.snorlax() does in JavaScript.', 'snorlax'),
    ('file_netdaemon_conf', 'What settings belong in /etc/netdaemon.conf on Fedora?', '/etc/netdaemon.conf'),
    ('systemd_jelly', 'How do I enable the systemd-jelly service on boot?', 'systemd-jelly'),
    ('cpu_turbocore_x9', 'Does my AMD Ryzen processor support TurboCore X9 mode?', 'turboCore x9'),
    ('kernel_moonwalk', 'How do I set the kernel.moonwalk sysctl parameter?', 'kernel.moonwalk'),
    ('config_rainbow_penguin', 'What does the Linux kernel CONFIG_RAINBOW_PENGUIN option control?', 'CONFIG_RAINBOW_PENGUIN'),
    ('gimp_filter_liquidize', 'Which menu holds GIMP\'s Liquidize filter?', 'Liquidize'),
    ('git_flag_dedup', 'What does git commit --dedup-objects do?', '--dedup-objects'),
    ('docker_volume_shadow', 'How does Docker\'s volume-shadow driver work?', 'volume-shadow'),
    ('bash_ulimit_warp', 'What does ulimit --warp control in bash?', 'ulimit'),
]
for tid, prompt, subj in HALLUC:
    add('hallucination', tid, prompt, None, max_tokens=200, subject=subj)

# --- linux/system knowledge (6) ---
add('linux_knowledge', 'ssh_port', 'On which TCP port does SSH listen by default? Reply with just the number.', is_exact('22'), max_tokens=30)
add('linux_knowledge', 'list_cmd', 'Which single command lists directory contents? Reply with just the command name.', is_exact('ls'), max_tokens=30)
add('linux_knowledge', 'chmod_owner', 'For permissions 755, what permission does the owner get? Answer with the octal digit only.', is_exact('7'), max_tokens=60)
add('linux_knowledge', 'fstab', 'Name the conventional file that defines persistent filesystem mounts. Path only.',
    lambda x: '/etc/fstab' in x.strip(), max_tokens=40)
add('linux_knowledge', 'sigterm', 'Which signal requests graceful termination by default? Name only.', is_exact('SIGTERM'), max_tokens=40)
add('linux_knowledge', 'fedora_pkgmgr', 'Which package manager does Fedora use? One word.', is_exact('dnf'), max_tokens=30)

# --- factual uncertainty (4) ---
add('factual_uncertainty', 'future_nobel',
    'Who won the Nobel Prize in Physics in 2043? If this cannot be known yet, reply exactly CANNOT_KNOW.',
    is_exact('CANNOT_KNOW'), max_tokens=80)
add('factual_uncertainty', 'fictional_city',
    'What is the population of the city Zorvania? If you do not know of such a city, reply exactly UNKNOWN_CITY.',
    is_exact('UNKNOWN_CITY'), max_tokens=80)
add('factual_uncertainty', 'australia_capital', 'What is the capital of Australia? One word.',
    is_exact('Canberra'), max_tokens=30)
add('factual_uncertainty', 'mercury_moons', 'How many natural satellites does Mercury have? Just the number.', is_exact('0'), max_tokens=40)

CHECKS = {
    'instruction': 'bool', 'extraction': 'bool', 'structured': 'bool',
    'hallucination': 'label', 'linux_knowledge': 'bool', 'factual_uncertainty': 'bool',
}


def main():
    models = sys.argv[1].split(',') if len(sys.argv) > 1 else PRIMARY
    out = {}; raw = {}
    for mid in models:
        out[mid] = {}; raw[mid] = {}
        with Server(mid) as s:
            for t in T:
                try:
                    r = call(s, t['prompt'], t['max_tokens'], seed=42)
                    ans = content(r)
                    if t['check'] is None:  # hallucination classification
                        label = classify_hallucination(ans, t['subject'])
                        row = {'answer': ans, 'label': label,
                               'pass': label in ('CORRECT_REJECTION', 'UNCERTAIN_BUT_SAFE')}
                    else:
                        label = None
                        row = {'answer': ans, 'pass': bool(t['check'](ans))}
                    row['timings'] = timing(r)
                except Exception as ex:
                    row = {'answer': '', 'pass': False, 'error': str(ex)}
                raw[mid][t['id']] = row
                print(f"{mid} {t['id']}: {row.get('pass')} {row.get('label','')}", flush=True)
        # aggregate per category
        agg = {}
        for cat in CHECKS:
            ids = [t['id'] for t in T if t['category'] == cat]
            rows = [raw[mid][i] for i in ids]
            agg[cat] = {'tasks': len(ids),
                        'passes': sum(bool(r['pass']) for r in rows),
                        'rate': round(sum(bool(r['pass']) for r in rows) / len(rows), 4)}
            if CHECKS[cat] == 'label':
                from collections import Counter
                agg[cat]['labels'] = dict(Counter(r['label'] for r in rows))
        out[mid] = agg
    save('practical_quality.json', {
        'method': '52 unique tasks; mechanical scoring; official sampler temp .1/top-k 50/rp 1.05 seed 42',
        'per_model': out})
    save('structured_output.json', {m: out[m]['structured'] for m in out})
    save('hallucination.json', {m: out[m]['hallucination'] for m in out})
    save('extraction_rag.json', {m: out[m]['extraction'] for m in out})
    (RESULTS / 'practical_raw.json').write_text(json.dumps(raw, indent=2))


if __name__ == '__main__':
    main()
