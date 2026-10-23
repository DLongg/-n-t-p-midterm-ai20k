import json
import os

with open("vlearn-app/src/multiphase_course_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

phases = data.get("phases", [])
p1 = phases[0]

questions_01_03 = []

for d in p1.get("days", []):
    day_num = d.get("day_num")
    day_id = d.get("day_id")
    if day_num in [1, 2, 3]:
        eqs = d.get("essay_questions", [])
        for q in eqs:
            questions_01_03.append({
                "day_num": day_num,
                "day_id": day_id,
                "question_id": q.get("question_id"),
                "q_num": q.get("q_num"),
                "points": q.get("points"),
                "estimated_difficulty": q.get("estimated_difficulty"),
                "kc_title": q.get("kc_title"),
                "prompt": q.get("interaction", {}).get("prompt"),
                "current_rubric": q.get("rubric"),
                "current_explanation": q.get("explanation"),
                "hints": [h.get("text") for h in q.get("hints", [])]
            })

print(f"Total extracted: {len(questions_01_03)}")
by_day = {}
for q in questions_01_03:
    by_day[q['day_num']] = by_day.get(q['day_num'], 0) + 1
print(f"By day: {by_day}")

os.makedirs(".audit_work", exist_ok=True)
with open(".audit_work/questions_block_01_03.json", "w", encoding="utf-8") as f:
    json.dump(questions_01_03, f, ensure_ascii=False, indent=2)

print("Saved to .audit_work/questions_block_01_03.json")
