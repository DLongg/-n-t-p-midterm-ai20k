import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
questions = data["questions"]
other_ss = [q for q in questions if q["interaction_type"] == "single_select" and "single_select_choice_a_default" not in q.get("review_reasons", [])]

print(f"Total other single_select: {len(other_ss)}")

with open(".audit_work/other_ss_view.txt", "w", encoding="utf-8") as f:
    for i, q in enumerate(other_ss, 1):
        f.write(f"\n================ Other SS #{i}: {q['question_id']} (Day {q['day']:02d}, is_std: {q['is_standard']}) ================\n")
        f.write(f"Prompt: {q['prompt']}\n")
        f.write("Choices:\n")
        for c in q.get("choices", []):
            f.write(f"  [{c['choice_id']}] {c['text']}\n")
        f.write(f"Current CA: {q.get('current_correct_answer')}\n")
        f.write(f"Explanation: {q.get('explanation')}\n")
