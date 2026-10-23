import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d1 = [q for q in data["questions"] if q["day"] == 1]

print(f"Total Day 1: {len(d1)}")
for i, q in enumerate(d1):
    qid = q["question_id"]
    itype = q["interaction_type"]
    ca = q["current_correct_answer"]
    is_std = q["is_standard"]
    # Check if needs modification
