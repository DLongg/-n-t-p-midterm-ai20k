import json

qs = json.load(open('scripts/extracted_day10_12_questions.json', encoding='utf-8'))
for q in qs:
    if q['points'] != 4:
        print(f"{q['question_id']} | Day {q['day_num']} | Points: {q['points']} | KC: {q['kc_title']}")
