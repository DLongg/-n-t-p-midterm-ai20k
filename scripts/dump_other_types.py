import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
questions = data["questions"]

# 1. single_select not flagged
ss_other = [q for q in questions if q["interaction_type"] == "single_select" and "single_select_choice_a_default" not in q.get("review_reasons", [])]
print(f"Single select (not 'a' flagged): {len(ss_other)}")

with open(".audit_work/ss_other_dump.txt", "w", encoding="utf-8") as out:
    for i, q in enumerate(ss_other, 1):
        out.write(f"\n--- SS #{i}: {q['question_id']} (Day {q['day']:02d}) ---\n")
        out.write(f"Prompt: {q['prompt']}\n")
        out.write("Choices:\n")
        for c in q.get("choices", []):
            out.write(f"  [{c['choice_id']}] {c['text']}\n")
        out.write(f"Current CA: {q.get('current_correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")

# 2. ordering
ordering_qs = [q for q in questions if q["interaction_type"] == "ordering"]
print(f"Ordering questions: {len(ordering_qs)}")
with open(".audit_work/ordering_dump.txt", "w", encoding="utf-8") as out:
    for i, q in enumerate(ordering_qs, 1):
        out.write(f"\n--- Ordering #{i}: {q['question_id']} (Day {q['day']:02d}) ---\n")
        out.write(f"Prompt: {q['prompt']}\n")
        out.write("Options:\n")
        for o in q.get("options", []):
            out.write(f"  [{o['option_id']}] {o['text']}\n")
        out.write(f"Current CA: {q.get('current_correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")

# 3. matching
matching_qs = [q for q in questions if q["interaction_type"] == "matching"]
print(f"Matching questions: {len(matching_qs)}")
with open(".audit_work/matching_dump.txt", "w", encoding="utf-8") as out:
    for i, q in enumerate(matching_qs, 1):
        out.write(f"\n--- Matching #{i}: {q['question_id']} (Day {q['day']:02d}) ---\n")
        out.write(f"Prompt: {q['prompt']}\n")
        out.write("Left:\n")
        for l in q.get("left", []):
            out.write(f"  [{l['id']}] {l['text']}\n")
        out.write("Right:\n")
        for r in q.get("right", []):
            out.write(f"  [{r['id']}] {r['text']}\n")
        out.write(f"Current CA: {q.get('current_correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")

# 4. multi_select
ms_qs = [q for q in questions if q["interaction_type"] == "multi_select"]
print(f"Multi select questions: {len(ms_qs)}")
with open(".audit_work/multi_select_dump.txt", "w", encoding="utf-8") as out:
    for i, q in enumerate(ms_qs, 1):
        out.write(f"\n--- Multi-select #{i}: {q['question_id']} (Day {q['day']:02d}) ---\n")
        out.write(f"Prompt: {q['prompt']}\n")
        out.write("Choices:\n")
        for c in q.get("choices", []):
            out.write(f"  [{c['choice_id']}] {c['text']}\n")
        out.write(f"Current CA: {q.get('current_correct_answer')}\n")
        out.write(f"Explanation: {q.get('explanation')}\n")
