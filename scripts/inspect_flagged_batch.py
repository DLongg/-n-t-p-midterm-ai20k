import sys
import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
flagged_a = [q for q in data["questions"] if "single_select_choice_a_default" in q.get("review_reasons", [])]

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else len(flagged_a)

for i in range(start - 1, min(end, len(flagged_a))):
    q = flagged_a[i]
    print(f"\n================ Flagged #{i+1}: {q['question_id']} (Day {q['day']:02d}) ================")
    print(f"Prompt: {q['prompt']}")
    print("Choices:")
    for c in q.get("choices", []):
        print(f"  [{c['choice_id']}] {c['text']}")
    print(f"Current CA: {q.get('current_correct_answer')}")
    print(f"Explanation: {q.get('explanation')}")
