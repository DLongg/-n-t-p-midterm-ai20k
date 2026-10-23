import json

def summarize():
    with open('scripts/extracted_day10_12_questions.json', 'r', encoding='utf-8') as f:
        qs = json.load(f)

    for day in (10, 11, 12):
        day_qs = [q for q in qs if q['day_num'] == day]
        print(f"\n==========================================")
        print(f"=== DAY {day}: {len(day_qs)} QUESTIONS ===")
        print(f"==========================================")
        for i, q in enumerate(day_qs):
            print(f"[{i+1}/{len(day_qs)}] {q['question_id']} ({q['points']} pts) - {q['kc_title']}")
            print(f"  Prompt: {q['prompt']}")
            print(f"  Hint: {q['hints']}")

if __name__ == '__main__':
    summarize()
