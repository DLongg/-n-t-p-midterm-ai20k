import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
matching_qs = [q for q in data["questions"] if q["interaction_type"] == "matching" and q["day"] >= 2]

print(f"Total matching in Days 02-05: {len(matching_qs)}")

with open(".audit_work/matching_days_02_05_dump.txt", "w", encoding="utf-8") as out:
    for i, q in enumerate(matching_qs, 1):
        out.write(f"\n=== Matching #{i}: {q['question_id']} (Day {q['day']:02d}, is_std: {q['is_standard']}) ===\n")
        out.write(f"Prompt: {q['prompt']}\n")
        out.write("Left:\n")
        for l in q["left"]:
            out.write(f"  {l['id']}: {l['text']}\n")
        out.write("Right:\n")
        for r in q["right"]:
            out.write(f"  {r['id']}: {r['text']}\n")
        out.write(f"Current CA: {q.get('current_correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")
