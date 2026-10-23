import json

with open(".audit_work/questions_block_01_03.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for day in [1, 2, 3]:
    day_qs = [q for q in questions if q["day_num"] == day]
    print(f"\n--- Day {day} IDs ({len(day_qs)}) ---")
    ids = [q["question_id"] for q in day_qs]
    print(", ".join(ids))
