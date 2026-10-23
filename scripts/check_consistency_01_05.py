import json
import re

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
questions = data["questions"]

print(f"Total questions: {len(questions)}")

# Let's see how many have explanations mentioning choices, or if explanations are generic
contradictions = []
for q in questions:
    qid = q["question_id"]
    itype = q["interaction_type"]
    ca = q.get("current_correct_answer")
    exp = q.get("explanation", "")
    choices = q.get("choices")
    
    # Check if explanation explicitly mentions another choice or contradicts
    # Also check if choice 'a' default is actually choice 'a' or if explanation says otherwise
    if itype == "single_select":
        # Let's see what the choices are
        choice_map = {c["choice_id"]: c["text"] for c in choices} if choices else {}
        # Print if explanation mentions another choice or if it explains something else
        pass

print("Done scanning.")
