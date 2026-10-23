import json

with open(".audit_work/questions_block_01_03.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

d2_qs = [q for q in questions if q["day_num"] == 2]
print(f"Total Day 2 questions: {len(d2_qs)}")

# Group by kc_title
kc_groups = {}
for q in d2_qs:
    kc = q["kc_title"]
    kc_groups.setdefault(kc, []).append(q["question_id"])

print(f"Unique KCs: {len(kc_groups)}")
for kc, qids in sorted(kc_groups.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {kc} ({len(qids)}): {', '.join(qids)}")
