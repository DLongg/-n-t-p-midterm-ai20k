import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
questions = data["questions"]
flagged_a = [q for q in questions if "single_select_choice_a_default" in q.get("review_reasons", [])]

print(f"Total flagged 'a': {len(flagged_a)}")
for i, q in enumerate(flagged_a, 1):
    print(f"#{i:02d} | {q['question_id']} | Day {q['day']:02d}")
