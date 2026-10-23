import json
from pathlib import Path

batch_path = Path(".audit_work/batch_days_01_05.json")
data = json.load(open(batch_path, encoding="utf-8"))
questions = data["questions"]

print(f"Total questions in batch: {len(questions)}")
numeric_qs = [q for q in questions if q["interaction_type"] == "numeric_input"]
print(f"Total numeric questions: {len(numeric_qs)}")

for i, q in enumerate(numeric_qs, 1):
    print(f"\n================ Question #{i}: {q['question_id']} (Day {q['day']:02d}) ================")
    print(f"Prompt:\n{q['prompt']}")
    print(f"Required unit: {q.get('required_unit')}")
    print(f"Current correct_answer: {q.get('current_correct_answer')} (type: {type(q.get('current_correct_answer')).__name__})")
    print(f"Explanation:\n{q.get('explanation')}")
