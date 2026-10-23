import json

with open('vlearn-app/src/multiphase_course_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

p1 = data['phases'][0]

def dump_day_text(day_num, filename):
    d = [x for x in p1['days'] if x.get('day_num') == day_num][0]
    with open(filename, 'w', encoding='utf-8') as out:
        for i, q in enumerate(d.get('essay_questions', []), 1):
            out.write(f"=== [{i:02d}] {q['question_id']} | Points: {q['points']} | KC: {q.get('kc_title')} ===\n")
            out.write(f"PROMPT:\n{q['interaction']['prompt']}\n")
            out.write(f"HINTS: {[h.get('text') for h in q.get('hints', [])]}\n\n")
    print(f"Wrote {filename}")

dump_day_text(7, 'data/day07_prompts.txt')
dump_day_text(8, 'data/day08_prompts.txt')
dump_day_text(9, 'data/day09_prompts.txt')
