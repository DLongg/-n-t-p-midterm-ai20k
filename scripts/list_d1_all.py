import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d1 = [q for q in data["questions"] if q["day"] == 1]
for i, q in enumerate(d1, 1):
    print(f"{i:03d}: {q['question_id']} | {q['interaction_type']} | std: {q['is_standard']} | ca: {q.get('current_correct_answer')}")
