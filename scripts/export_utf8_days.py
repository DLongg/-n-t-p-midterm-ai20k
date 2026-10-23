import json

def export_all():
    with open('scripts/extracted_day10_12_questions.json', 'r', encoding='utf-8') as f:
        qs = json.load(f)

    for day in (10, 11, 12):
        target_qs = [q for q in qs if q['day_num'] == day]
        out_path = f"scripts/day{day}_utf8.txt"
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(f"Total questions for Day {day}: {len(target_qs)}\n\n")
            for i, q in enumerate(target_qs):
                out.write(f"================================================================================\n")
                out.write(f"Question {i+1}/{len(target_qs)} | ID: {q['question_id']} | Points: {q['points']}\n")
                out.write(f"KC: {q['kc_title']}\n")
                out.write(f"PROMPT:\n{q['prompt']}\n")
                out.write(f"HINTS: {q['hints']}\n")
                out.write(f"CURRENT_RUBRIC:\n{q['current_rubric']}\n")
                out.write(f"CURRENT_EXPLANATION:\n{q['current_explanation']}\n\n")
        print(f"Wrote {len(target_qs)} questions to {out_path}")

if __name__ == '__main__':
    export_all()
