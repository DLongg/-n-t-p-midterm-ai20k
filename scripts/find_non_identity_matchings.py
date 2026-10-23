import json

data = json.load(open(".audit_work/batch_days_01_05.json", encoding="utf-8"))
matching_qs = [q for q in data["questions"] if q["interaction_type"] == "matching"]

print(f"Total matching questions: {len(matching_qs)}")

for q in matching_qs:
    ca = q.get("current_correct_answer", {})
    left = q.get("left", [])
    right = q.get("right", [])
    
    # Check if number of left items equals number of right items
    # and whether mapping is xi -> ri
    diffs = []
    for l in left:
        lid = l["id"]
        rid = ca.get(lid)
        l_num = "".join(filter(str.isdigit, lid))
        r_num = "".join(filter(str.isdigit, rid)) if rid else ""
        if l_num != r_num:
            diffs.append((lid, rid))
            
    if diffs:
        print(f"\n[{q['question_id']}] (Day {q['day']:02d}, is_std: {q['is_standard']}) CA: {ca}")
        print("  Prompt:", q["prompt"][:80])
        print("  Left:", [(l['id'], l['text']) for l in left])
        print("  Right:", [(r['id'], r['text']) for r in right])
        print("  Diffs (where l_i != r_i):", diffs)
