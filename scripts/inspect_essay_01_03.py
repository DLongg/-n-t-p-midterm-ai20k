import json

with open("vlearn-app/src/multiphase_course_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

phases = data.get("phases", [])
print(f"Total phases: {len(phases)}")
for i, p in enumerate(phases):
    print(f"Phase {i} keys:", list(p.keys()))
    days = p.get("days", [])
    print(f"Phase {i} has {len(days)} days")
    if days:
        print(f"  Day 0 keys:", list(days[0].keys()))
        print(f"  Day 0 id field:", {k: days[0][k] for k in ['id', 'day', 'day_id', 'title'] if k in days[0]})
p1 = phases[0]
for d in p1.get("days", [])[:3]:
    day_id = d.get("day_id")
    eqs = d.get("essay_questions", [])
    print(f"=== {day_id}: {len(eqs)} questions ===")
    if eqs:
        q = eqs[0]
        print("Keys:", list(q.keys()))
        print("ID:", q.get("question_id"))
        print("Points:", q.get("points"))
        print("KC Title:", q.get("kc_title"))
        print("Prompt:", q.get("interaction", {}).get("prompt"))
        print("Rubric:", q.get("rubric"))
        print("Explanation:", q.get("explanation"))
        print("Hints:", q.get("hints"))


