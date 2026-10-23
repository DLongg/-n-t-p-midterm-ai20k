import json

with open("vlearn-app/src/multiphase_course_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

p1 = data["phases"][0]
days = [d for d in p1.get("days", []) if d.get("day_num") in [4, 5, 6]]

print(f"Target days found: {len(days)}")
total_eqs = 0
for d in days:
    num = d.get("day_num")
    eqs = d.get("essay_questions", [])
    total_eqs += len(eqs)
    print(f"\n==================================================")
    print(f"DAY {num}: {d.get('title')} ({len(eqs)} essay questions)")
    print(f"==================================================")
    for idx, q in enumerate(eqs, 1):
        qid = q.get("question_id")
        pts = q.get("points")
        kc = q.get("kc_title")
        prompt = q.get("interaction", {}).get("prompt", "")
        hint = q.get("hints", [{}])[0].get("text", "")
        print(f"\n[{idx}/{len(eqs)}] {qid} ({pts} pts) - {kc}")
        print(f"PROMPT:\n{prompt}")
        print(f"HINT:\n{hint}")

print(f"\nTotal essay questions across Days 4-6: {total_eqs}")
