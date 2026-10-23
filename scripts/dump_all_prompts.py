import json

with open(".audit_work/questions_block_01_03.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for day in [1, 2, 3]:
    day_qs = [q for q in questions if q["day_num"] == day]
    filepath = f".audit_work/day{day:02d}_prompts.txt"
    with open(filepath, "w", encoding="utf-8") as out:
        for i, q in enumerate(day_qs):
            out.write(f"=== #{i+1} ID: {q['question_id']} | Points: {q['points']} | KC: {q['kc_title']} ===\n")
            out.write(f"PROMPT:\n{q['prompt']}\n")
            out.write(f"HINTS: {q['hints']}\n")
            out.write(f"CURRENT_RUBRIC:\n{q['current_rubric']}\n")
            out.write(f"CURRENT_EXPLANATION:\n{q['current_explanation']}\n\n")
    print(f"Dumped {len(day_qs)} prompts to {filepath}")

