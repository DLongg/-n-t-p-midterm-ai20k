import json
import sys

def main(target_day):
    with open('scripts/extracted_day10_12_questions.json', 'r', encoding='utf-8') as f:
        qs = json.load(f)

    target_qs = [q for q in qs if q['day_num'] == target_day]
    print(f"Total questions for Day {target_day}: {len(target_qs)}")
    for i, q in enumerate(target_qs):
        print(f"--- Question {i+1}/{len(target_qs)}: {q['question_id']} ({q['points']} pts) ---")
        print(f"KC: {q['kc_title']}")
        print(f"Prompt:\n{q['prompt']}")
        print(f"Hints: {q['hints']}")
        print()

if __name__ == '__main__':
    day = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    main(day)
