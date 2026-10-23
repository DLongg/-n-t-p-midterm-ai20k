import json

data = json.load(open('.audit_work/questions_block_01_03.json', encoding='utf-8'))
d3 = [x for x in data if x['day_num'] == 3]
print(f"Total Day 03 questions: {len(d3)}")
for i, q in enumerate(d3):
    print(f"{i+1}. {q['question_id']} ({q['points']} pts) [{q['kc_title']}]")
