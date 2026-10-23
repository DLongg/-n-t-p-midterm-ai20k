import json

with open('data/raw_questions_04_06.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/output_d4_d6_utf8.txt', 'w', encoding='utf-8') as out_f:
    for day in [4, 5, 6]:
        d_qs = [q for q in qs if q['day'] == day]
        out_f.write(f"\n=======================================================\n")
        out_f.write(f"DAY {day}: Total {len(d_qs)} questions\n")
        out_f.write(f"=======================================================\n")
        for i, q in enumerate(d_qs, 1):
            out_f.write(f"--- [{i}/{len(d_qs)}] ID: {q['question_id']} | Points: {q['points']} | KC: {q['kc_title']} ---\n")
            out_f.write(f"PROMPT: {q['prompt']}\n")
            out_f.write(f"HINT: {q['hint']}\n\n")
