import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
questions = data["questions"]
ms_qs = [q for q in questions if q["interaction_type"] == "multi_select"]

print(f"Total multi_select: {len(ms_qs)}")
std_ms = [q for q in ms_qs if q["is_standard"]]
exp_ms = [q for q in ms_qs if not q["is_standard"]]
print(f"Standard MS: {len(std_ms)}, Expanded MS: {len(exp_ms)}")

with open(".audit_work/ms_inspect_view.txt", "w", encoding="utf-8") as f:
    for i, q in enumerate(ms_qs, 1):
        f.write(f"\n================ MS #{i}: {q['question_id']} (Day {q['day']:02d}, is_std: {q['is_standard']}) ================\n")
        f.write(f"Prompt: {q['prompt']}\n")
        f.write("Choices:\n")
        for c in q.get("choices", []):
            f.write(f"  [{c['choice_id']}] {c['text']}\n")
        f.write(f"Current CA: {q.get('current_correct_answer')}\n")
        f.write(f"Explanation: {q.get('explanation')}\n")
