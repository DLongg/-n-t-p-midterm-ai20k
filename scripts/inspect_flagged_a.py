import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
questions = data["questions"]

flagged_a = [q for q in questions if "single_select_choice_a_default" in q.get("review_reasons", [])]
print(f"Total single_select with default 'a': {len(flagged_a)}")

with open(".audit_work/flagged_a_dump.txt", "w", encoding="utf-8") as out:
    for i, q in enumerate(flagged_a, 1):
        out.write(f"\n--- Flagged #{i}: {q['question_id']} (Day {q['day']:02d}) ---\n")
        out.write(f"Prompt: {q['prompt']}\n")
        out.write("Choices:\n")
        for c in q.get("choices", []):
            out.write(f"  [{c['choice_id']}] {c['text']}\n")
        out.write(f"Current CA: {q.get('current_correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")
