#!/usr/bin/env python3
"""Phase 7 native tools: v1 = exact 2.6B five-case contract (historical comparability);
v2 = ten harder cases with deterministic mock scoring.

Scored separately: tool selection, argument/schema validity, result interpretation
(v2 follow-ups), correct final answer, complete sequence.
"""
from pathlib import Path
import json, re, sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

TOOLS_V1 = [
    {'type': 'function', 'function': {'name': 'lookup_weather', 'description': 'Get weather by city and unit',
     'parameters': {'type': 'object', 'properties': {'city': {'type': 'string'}, 'unit': {'type': 'string', 'enum': ['C', 'F']}},
      'required': ['city', 'unit']}}},
    {'type': 'function', 'function': {'name': 'sum_numbers', 'description': 'Return sum of integer values',
     'parameters': {'type': 'object', 'properties': {'values': {'type': 'array', 'items': {'type': 'integer'}}},
      'required': ['values']}}}]
CASES_V1 = [
    ('What is weather in Oslo in C?', 'lookup_weather', {'city': 'Oslo', 'unit': 'C'}),
    ('Sum 2, 5, and 9.', 'sum_numbers', {'values': [2, 5, 9]}),
    ('Just greet me; do not call a tool.', None, None),
    ('What is weather in Lima in F?', 'lookup_weather', {'city': 'Lima', 'unit': 'F'}),
    ('Sum -3 and 8.', 'sum_numbers', {'values': [-3, 8]})]

# v2 harder tools
TOOLS_V2 = TOOLS_V1 + [
    {'type': 'function', 'function': {'name': 'create_ticket', 'description': 'Create a ticket',
     'parameters': {'type': 'object',
                    'properties': {'title': {'type': 'string'}, 'priority': {'type': 'string', 'enum': ['low', 'medium', 'high']},
                                   'retries': {'type': 'integer'}, 'tags': {'type': 'array', 'items': {'type': 'string'}},
                                   'assignee': {'type': 'object', 'properties': {'team': {'type': 'string'}, 'level': {'type': 'integer'}},
                                                'required': ['team']}},
                    'required': ['title', 'priority']}}},
    {'type': 'function', 'function': {'name': 'get_stock_price', 'description': 'Get current stock price by ticker',
     'parameters': {'type': 'object', 'properties': {'ticker': {'type': 'string'}}, 'required': ['ticker']}}}]
MOCK = {
    ('lookup_weather',): lambda a: f"Weather in {a.get('city')}: 12 degrees{'' if a.get('unit') != 'F' else ' (converted)'}",
    ('sum_numbers',): lambda a: f"Sum is {sum(a.get('values', []))}",
    ('create_ticket',): lambda a: f"Ticket TCK-101 created for '{a.get('title')}'",
    ('get_stock_price',): lambda a: "ERROR: unknown ticker" if a.get('ticker', '').upper() == 'ZZZZZ' else f"{a['ticker']} trades at 142.50 USD",
}


def first_call(resp):
    m = resp['choices'][0]['message']
    calls = m.get('tool_calls') or []
    if not calls:
        return None, None, content(resp)
    try:
        args = json.loads(calls[0]['function']['arguments'])
    except Exception:
        args = None
    return calls[0]['function']['name'], args, content(resp)


def run_v1():
    out = {}; raw = {}
    for mid in PRIMARY:
        rows = []
        with Server(mid) as s:
            for q, want, wargs in CASES_V1:
                r = call(s, q, 256, tools=TOOLS_V1)
                got, gargs, _ = first_call(r)
                ok = got == want and gargs == wargs
                rows.append({'query': q, 'expected_tool': want, 'expected_arguments': wargs,
                             'got_tool': got, 'got_arguments': gargs, 'pass': bool(ok)})
        raw[mid] = rows
        out[mid] = {'total': len(rows),
                    'correct_tool_selection': sum(x['got_tool'] == x['expected_tool'] for x in rows),
                    'correct_arguments': sum(x['got_arguments'] == x['expected_arguments'] for x in rows),
                    'end_to_end_pass': sum(x['pass'] for x in rows)}
    return out, raw


V2_CASES = [
    # id, system/user prompt, expected tool, validator(args)->(ok,detail), follow-up or None, final-answer check
    ('v2_nested_object', 'Create a high priority ticket titled "GPU fan alarm" assigned to team infra at level 3.',
     'create_ticket',
     lambda a: isinstance(a, dict) and a.get('priority') == 'high' and isinstance(a.get('assignee'), dict) and a.get('assignee', {}).get('team') == 'infra',
     'Now what is the weather in Oslo in C?', lambda t: 'Oslo' in t),
    ('v2_multiple_possible', 'I need the sum of 4 and 17, and also the price of MSFT.',
     None,  # expects two calls; special handling below
     None, None, None),
    ('v2_irrelevant_tool', 'My favorite color is teal. Remember that. Do not call any tools unless needed.',
     None, None, None, None),  # expect NO call
    ('v2_int_constraint', 'Create a medium priority ticket titled "disk almost full" with retries set to the number of legs a spider has.',
     'create_ticket',
     lambda a: a.get('retries') == 8,
     None, None),
    ('v2_enum_invalid_then_fix', 'Create a low priority ticket titled "typo in docs" with urgency URGENT.',
     'create_ticket',  # model must coerce to valid enum or ask; accept low/medium/high valid call OR refusal question
     lambda a: a.get('priority') in ('low', 'medium', 'high'),
     None, None),
    ('v2_error_retry', 'What is the stock price of ZZZZZ? If the lookup fails, tell me it failed.',
     'get_stock_price', lambda a: a.get('ticker') == 'ZZZZZ',
     'RESULT: ERROR: unknown ticker\n\nGiven this tool result, did the lookup succeed? Answer YES or NO.',
     lambda t: 'NO' in t.upper()),
    ('v2_contradiction', 'What is the stock price of AAPL?',
     'get_stock_price', lambda a: a.get('ticker') == 'AAPL',
     'RESULT: AAPL trades at 142.50 USD\n\nEarlier I assumed the price was over 500 dollars. Given the tool result, is my assumption right? Answer YES or NO with the actual price.',
     lambda t: 'NO' in t.upper() and '142.5' in t),
    ('v2_no_tool_case', 'What is 12 times 11 in your head? No tools.',
     None, None, None, lambda t: '132' in content(t) if isinstance(t, dict) else False),
    ('v2_multiturn_seq', 'First get the weather in Lima in F. Then, using the temperature number from the result as an integer, sum it with 8 using the second tool. Report both numbers.',
     'lookup_weather', lambda a: a.get('city') == 'Lima' and a.get('unit') == 'F',
     'RESULT: Weather in Lima: 12 degrees (converted)\n\nNow sum exactly that integer temperature with 8 using the sum tool.',
     lambda a2: a2 and a2.get('values') == [12, 8]),
    ('v2_array_of_strings', 'Create a high priority ticket titled "audit" with tags ["security", "q3"].',
     'create_ticket',
     lambda a: a.get('tags') == ['security', 'q3'], None, None),
]


def run_v2():
    out = {}; raw = {}
    for mid in PRIMARY:
        rows = []
        with Server(mid) as s:
            for cid, q, want, validator, followup, fincheck in V2_CASES:
                row = {'id': cid}
                try:
                    r = call(s, q, 300, tools=TOOLS_V2)
                    name, args, txt = first_call(r)
                    row.update(got_tool=name, got_args=args)
                    if cid == 'v2_multiple_possible':
                        # success = made >=2 distinct correct calls across turns; simplified: first call correct + follow-up handled
                        r2 = s.chat([{'role': 'user', 'content': q}, {'role': 'assistant', 'content': txt or '(tool call)'},
                                     {'role': 'user', 'content': 'Do the other one too.'}], 300, tools=TOOLS_V2)
                        n2, a2, _ = first_call(r2)
                        row['second_tool'] = n2; row['second_args'] = a2
                        row['selection_ok'] = {name, n2} == {'sum_numbers', 'get_stock_price'}
                        row['schema_ok'] = isinstance(args, dict) and isinstance(a2, dict)
                    elif cid == 'v2_irrelevant_tool':
                        row['selection_ok'] = name is None
                        row['schema_ok'] = True
                    elif cid == 'v2_no_tool_case':
                        row['selection_ok'] = name is None
                        row['final_ok'] = '132' in (txt or '')
                        row['schema_ok'] = True
                    else:
                        row['selection_ok'] = name == want
                        try:
                            row['schema_ok'] = bool(name and validator(args))
                        except Exception:
                            row['schema_ok'] = False
                    if followup:
                        msgs = [{'role': 'user', 'content': q}]
                        if name:
                            msgs.append({'role': 'assistant', 'tool_calls': None, 'content': f'[called {name}]'})
                        msgs.append({'role': 'user', 'content': followup})
                        r2 = call(s, followup, 300, tools=TOOLS_V2)
                        n2, a2, t2 = first_call(r2)
                        row['followup_tool'] = n2; row['followup_args'] = a2; row['followup_text'] = t2[:300]
                        if fincheck:
                            try:
                                row['final_ok'] = bool(fincheck(t2))
                            except Exception:
                                row['final_ok'] = False
                    row['interpretation_ok'] = row.get('final_ok', True)
                    row['complete_sequence_ok'] = bool(row['selection_ok'] and row['schema_ok']
                                                       and row.get('interpretation_ok', True)
                                                       and (row.get('final_ok', True)))
                except Exception as ex:
                    row.update(error=str(ex), selection_ok=False, schema_ok=False, complete_sequence_ok=False)
                rows.append(row)
                print(f"{mid} {cid}: sel={row.get('selection_ok')} sch={row.get('schema_ok')} done={row.get('complete_sequence_ok')}", flush=True)
        raw[mid] = rows
        out[mid] = {
            'cases': len(rows),
            'tool_selection': sum(x['selection_ok'] for x in rows),
            'argument_schema_validity': sum(x['schema_ok'] for x in rows),
            'result_interpretation': sum(x.get('interpretation_ok', False) for x in rows if 'interpretation_ok' in x),
            'correct_final_answer': sum(x.get('final_ok', False) for x in rows if 'final_ok' in x),
            'complete_sequences': sum(x['complete_sequence_ok'] for x in rows)}
    return out, raw


if __name__ == '__main__':
    o1, r1 = run_v1()
    o2, r2 = run_v2()
    save('tool_calling.json', {'v1_historical_5cases': o1,
                               'v2_harder_10cases': o2,
                               'scoring_note': 'v1: exact tool+args match (2.6B contract). v2 scored separately on selection/args/interpretation/final/sequence.'})
    (RESULTS / 'tool_raw.json').write_text(json.dumps({'v1': r1, 'v2': r2}, indent=2))
    print('TOOLS_DONE')
