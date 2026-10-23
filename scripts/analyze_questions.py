import json

with open(".audit_work/questions_block_01_03.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for day in [1, 2, 3]:
    qs = [q for q in questions if q["day_num"] == day]
    points = [q["points"] for q in qs]
    print(f"=== Day {day} ({len(qs)} questions) ===")
    dist = {p: points.count(p) for p in sorted(set(points))}
    print(f"Points distribution: {dist}")
    print("Sample questions:")
    for q in qs[:5]:
        print(f"  [{q['question_id']}] ({q['points']} pts) {q['kc_title']}")
        print(f"     Prompt: {q['prompt'][:80]}...")
