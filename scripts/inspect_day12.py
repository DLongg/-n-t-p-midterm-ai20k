import json

with open('scripts/extracted_day10_12_questions.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

d12 = [it for it in items if it['day_num'] == 12]
print(f"Total Day 12 questions: {len(d12)}")
for i, q in enumerate(d12):
    print(f"{i+1:2d}. id={q['question_id']} | pts={q['points']} | prompt={q['prompt'][:70]}...")
