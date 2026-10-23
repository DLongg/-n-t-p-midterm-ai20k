import sys, json

start = int(sys.argv[1]) if len(sys.argv) > 1 else 10
end = int(sys.argv[2]) if len(sys.argv) > 2 else 20

with open('scripts/extracted_day10_12_questions.json', encoding='utf-8') as f:
    items = [it for it in json.load(f) if it['day_num'] == 12]

for i in range(start, min(end, len(items))):
    q = items[i]
    print(f"=== [{i+1}] {q['question_id']} ({q['points']} pts) ===")
    print("PROMPT:\n" + q['prompt'])
    print("\nHINTS:\n" + str(q['hints']))
    print("\n" + "="*50 + "\n")
