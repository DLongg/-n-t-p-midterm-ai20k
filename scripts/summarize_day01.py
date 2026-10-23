import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
d1_questions = [q for q in data["questions"] if q["day"] == 1]

print(f"Total Day 1: {len(d1_questions)}")

# Check each interaction type
for itype in ["numeric_input", "ordering", "matching", "single_select", "multi_select"]:
    subset = [q for q in d1_questions if q["interaction_type"] == itype]
    print(f"\n--- Day 1 {itype}: {len(subset)} questions ---")
    for q in subset:
        qid = q["question_id"]
        ca = q.get("current_correct_answer")
        print(f"[{qid}] CA: {ca} | Prompt: {q['prompt'][:80]}...")
