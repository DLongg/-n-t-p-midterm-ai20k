import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d2 = [q for q in data["questions"] if q["day"] == 2 and q["interaction_type"] == "multi_select"]

for q in d2:
    print(f"\n=== {q['question_id']} (is_std: {q['is_standard']}) ===")
    print("Prompt:", q["prompt"])
    print("Choices:")
    for c in q["choices"]:
        print(f"  [{c['choice_id']}] {c['text']}")
    print("Current CA:", q.get("current_correct_answer"))
    print("Explanation:", q.get("explanation"))
