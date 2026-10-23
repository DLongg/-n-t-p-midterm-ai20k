import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.author_day03 import get_day03_data

def verify_day03():
    with open(".audit_work/questions_block_01_03.json", "r", encoding="utf-8") as f:
        all_q = json.load(f)
    
    expected_d3 = {q["question_id"]: q for q in all_q if q["day_num"] == 3}
    print(f"Total expected Day 03 questions: {len(expected_d3)}")
    
    d3_authored = get_day03_data()
    print(f"Total authored Day 03 questions: {len(d3_authored)}")
    
    assert len(d3_authored) == len(expected_d3), f"Mismatch count: expected {len(expected_d3)}, got {len(d3_authored)}"
    
    issues = []
    for qid, q in expected_d3.items():
        if qid not in d3_authored:
            issues.append(f"Missing authored question {qid}")
            continue
        item = d3_authored[qid]
        
        ans = item.get("sample_answer", "")
        exp = item.get("explanation", "")
        rub = item.get("rubric", "")
        ref = item.get("reference_source", "")
        
        if len(ans.strip()) < 150:
            issues.append(f"Answer too short in {qid}: {len(ans)} chars")
        if len(exp.strip()) < 50:
            issues.append(f"Explanation too short in {qid}: {len(exp)} chars")
        if len(rub.strip()) < 50:
            issues.append(f"Rubric too short in {qid}: {len(rub)} chars")
        if len(ref.strip()) < 10:
            issues.append(f"Reference too short in {qid}: {len(ref)} chars")
        
        pts = q.get("points", 3)
        if not (f"{pts} điểm" in rub or f"{pts} diem" in rub.lower() or f"{pts} pts" in rub.lower() or f"{pts}.0 điểm" in rub):
            issues.append(f"Rubric doesn't state {pts} points in {qid}")
            
        if not ("http" in ref):
            issues.append(f"Reference missing http URL in {qid}: {ref}")
            
    if issues:
        print(f"FOUND {len(issues)} ISSUES IN DAY 03:")
        for iss in issues:
            print("  -", iss)
        raise AssertionError(f"Day 03 verification failed with {len(issues)} issues")
        
    print(f"ALL {len(d3_authored)} DAY 03 QUESTIONS VERIFIED SUCCESSFULLY!")

if __name__ == "__main__":
    verify_day03()
