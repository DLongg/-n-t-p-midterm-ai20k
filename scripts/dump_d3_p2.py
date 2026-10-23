import json

data = json.load(open('.audit_work/questions_block_01_03.json', encoding='utf-8'))
d3 = [x for x in data if x['day_num'] == 3]

with open('.audit_work/d3_part2_prompts.txt', 'w', encoding='utf-8') as f:
    for i, q in enumerate(d3[26:]):
        f.write(f"=== {i+27}. {q['question_id']} ({q['points']} pts) [{q['kc_title']}] ===\n")
        f.write(f"PROMPT:\n{q['prompt']}\n\n")
        f.write(f"CURRENT_RUBRIC:\n{q['current_rubric']}\n\n")
        f.write(f"CURRENT_EXPLANATION:\n{q['current_explanation']}\n\n")
        f.write(f"HINTS:\n{q['hints']}\n\n")
        f.write("-" * 60 + "\n\n")

print("Dumped d3_part2_prompts.txt successfully")
