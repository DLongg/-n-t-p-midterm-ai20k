import json

qs = json.load(open('scripts/extracted_day10_12_questions.json', encoding='utf-8'))
for day in (10, 11, 12):
    day_qs = [q for q in qs if q['day_num'] == day]
    print(f"\n=== Day {day} ({len(day_qs)} questions) ===")
    for i, q in enumerate(day_qs):
        print(f"{i+1:2d}. {q['question_id']} [{q['points']}p] {q['kc_title']}")
