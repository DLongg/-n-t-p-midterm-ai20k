import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d1_match = [q for q in data["questions"] if q["day"] == 1 and q["interaction_type"] == "matching"]

for i, q in enumerate(d1_match, 1):
    print(f"\n=== Matching #{i}: {q['question_id']} (is_std: {q['is_standard']}) ===")
    print("Prompt:", q["prompt"])
    print("Left:")
    for l in q["left"]:
        print(f"  {l['id']}: {l['text']}")
    print("Right:")
    for r in q["right"]:
        print(f"  {r['id']}: {r['text']}")
    print("Current CA:", q.get("current_correct_answer"))
    print("Explanation:", q.get("explanation"))
