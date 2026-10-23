import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d1 = [q for q in data["questions"] if q["day"] == 1]

q_ids = ['d01-q090', 'd01-q092', 'd01-q104', 'd01-q108', 'd01-q140', 'd01-q144', 'd01-q145', 'd01-q150']
for q in d1:
    if q["question_id"] in q_ids:
        print(f"\n=== {q['question_id']} ===")
        print("Prompt:", q["prompt"])
        print("Choices:")
        for c in q["choices"]:
            print(f"  [{c['choice_id']}] {c['text']}")
        print("Current CA:", q.get("current_correct_answer"))
        print("Explanation:", q.get("explanation"))
