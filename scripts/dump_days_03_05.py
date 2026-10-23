import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))

for day in [3, 4, 5]:
    qs = [q for q in data["questions"] if q["day"] == day]
    print(f"Total Day {day}: {len(qs)}")
    with open(f".audit_work/day{day:02d}_audit_view.txt", "w", encoding="utf-8") as f:
        for i, q in enumerate(qs, 1):
            f.write(f"\n================ Day {day:02d} #{i}: {q['question_id']} ({q['interaction_type']}, is_std: {q['is_standard']}) ================\n")
            f.write(f"Prompt: {q['prompt']}\n")
            if q["choices"]:
                f.write("Choices:\n")
                for c in q["choices"]:
                    f.write(f"  [{c['choice_id']}] {c['text']}\n")
            if q["options"]:
                f.write("Options:\n")
                for o in q["options"]:
                    f.write(f"  [{o['option_id']}] {o['text']}\n")
            if q["left"]:
                f.write("Left:\n")
                for l in q["left"]:
                    f.write(f"  [{l['id']}] {l['text']}\n")
                f.write("Right:\n")
                for r in q["right"]:
                    f.write(f"  [{r['id']}] {r['text']}\n")
            if q["required_unit"]:
                f.write(f"Required unit: {q['required_unit']}\n")
            f.write(f"Current CA: {q.get('current_correct_answer')}\n")
            f.write(f"Explanation: {q.get('explanation')}\n")
print("Dumped Days 03, 04, 05.")
