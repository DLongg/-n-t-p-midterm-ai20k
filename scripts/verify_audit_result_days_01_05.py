import json
from pathlib import Path

audit_file = Path(".audit_work/audit_result_days_01_05.json")
assert audit_file.exists(), "Output file does not exist!"

with open(audit_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. Top-level schema check
assert data.get("batch") == "days_01_05", f"Wrong batch: {data.get('batch')}"
assert data.get("total_questions_audited") == 266, f"Wrong total: {data.get('total_questions_audited')}"
assert isinstance(data.get("modified_count"), int) and data.get("modified_count") > 0, "Invalid modified count"

questions = data.get("questions", [])
assert len(questions) == 266, f"Questions list length mismatch: {len(questions)}"

# 2. Check each question record
required_keys = {
    "question_id",
    "day",
    "interaction_type",
    "prompt_summary",
    "previous_correct_answer",
    "new_correct_answer",
    "updated_explanation",
    "web_search_evidence",
    "is_modified",
}

days_found = set()
types_found = set()
numeric_qs = []

for idx, q in enumerate(questions):
    assert set(q.keys()) == required_keys, f"Question {q.get('question_id')} has incorrect keys: {set(q.keys()) ^ required_keys}"
    assert q["day"] in ["Day 01", "Day 02", "Day 03", "Day 04", "Day 05"], f"Invalid day format: {q['day']}"
    days_found.add(q["day"])
    types_found.add(q["interaction_type"])
    
    assert len(q["prompt_summary"]) > 0, f"Empty prompt summary at {q['question_id']}"
    assert len(q["updated_explanation"].strip()) > 10, f"Empty or too short explanation at {q['question_id']}"
    assert len(q["web_search_evidence"].strip()) > 5, f"Empty evidence at {q['question_id']}"
    assert isinstance(q["is_modified"], bool), f"is_modified must be bool at {q['question_id']}"

    if q["interaction_type"] == "numeric_input":
        numeric_qs.append(q)
        assert isinstance(q["new_correct_answer"], (int, float)), f"Numeric answer must be int/float at {q['question_id']}"
        assert not isinstance(q["new_correct_answer"], bool), f"Numeric answer cannot be bool at {q['question_id']}"
        assert str(q["new_correct_answer"]) != "None" and str(q["new_correct_answer"]) != "0", f"Numeric dummy 0 at {q['question_id']}"

print(f"Days verified: {sorted(days_found)}")
print(f"Types verified: {sorted(types_found)}")
print(f"Total numeric questions verified: {len(numeric_qs)}/14")
for n in numeric_qs:
    print(f"  {n['question_id']} ({n['day']}): {n['new_correct_answer']} (was {n['previous_correct_answer']})")

print(f"\nALL 266 QUESTIONS STRICTLY VALIDATED!")
