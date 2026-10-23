import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d5_exp_ms = [q for q in data["questions"] if q["day"] == 5 and q["interaction_type"] == "multi_select" and not q["is_standard"]]

print(f"Total Day 5 expanded MS: {len(d5_exp_ms)}")
for q in d5_exp_ms:
    print(f"\n=== {q['question_id']} ===")
    print("Prompt:", q["prompt"])
    print("Choices:")
    for c in q["choices"]:
        print(f"  [{c['choice_id']}] {c['text']}")
    print("Current CA:", q.get("current_correct_answer"))
    print("Explanation:", q.get("explanation"))
