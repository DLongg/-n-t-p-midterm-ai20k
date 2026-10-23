"""
Assembler and comprehensive verifier for Block 01-03 essay dataset.
Gathers authored questions from Day 01 (49), Day 02 (86), Day 03 (52) -> 187 items total.
Outputs to: data/essay_block_01_03.json.
"""
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.author_day01 import get_day01_data
from scripts.author_day02 import get_day02_data
from scripts.author_day03 import get_day03_data

def assemble_and_verify():
    print("=== Step 1: Loading authored questions from modules ===")
    d1 = get_day01_data()
    d2 = get_day02_data()
    d3 = get_day03_data()
    
    print(f"Loaded Day 01: {len(d1)} questions")
    print(f"Loaded Day 02: {len(d2)} questions")
    print(f"Loaded Day 03: {len(d3)} questions")
    
    total_authored = len(d1) + len(d2) + len(d3)
    print(f"Total authored questions: {total_authored}")
    assert total_authored == 187, f"Expected 187 questions, got {total_authored}"
    
    # Load ground truth questions
    with open(".audit_work/questions_block_01_03.json", "r", encoding="utf-8") as f:
        ground_truth_list = json.load(f)
    
    assert len(ground_truth_list) == 187, f"Expected 187 ground truth questions, got {len(ground_truth_list)}"
    gt_map = {q["question_id"]: q for q in ground_truth_list}
    
    # Assemble unified dictionary
    block_data = {}
    
    # Preserve order of questions as they appear in the course
    for q in ground_truth_list:
        qid = q["question_id"]
        day = q["day_num"]
        
        if day == 1:
            assert qid in d1, f"Missing {qid} in Day 01"
            block_data[qid] = d1[qid]
        elif day == 2:
            assert qid in d2, f"Missing {qid} in Day 02"
            block_data[qid] = d2[qid]
        elif day == 3:
            assert qid in d3, f"Missing {qid} in Day 03"
            block_data[qid] = d3[qid]
        else:
            raise ValueError(f"Unexpected day_num {day} for {qid}")
            
    print(f"Successfully assembled {len(block_data)} questions in chronological order.")
    
    # Step 2: Quality assertions
    print("\n=== Step 2: Running Deep Quality Audit ===")
    old_boilerplate = "Đúng bản chất vấn đề và yêu cầu kỹ thuật"
    issues = []
    
    for qid, item in block_data.items():
        gt = gt_map[qid]
        pts = gt.get("points", 3)
        
        # Field presence
        for f in ["sample_answer", "explanation", "rubric", "reference_source"]:
            if f not in item or not isinstance(item[f], str) or not item[f].strip():
                issues.append(f"Missing or empty field '{f}' in {qid}")
                
        ans = item.get("sample_answer", "").strip()
        exp = item.get("explanation", "").strip()
        rub = item.get("rubric", "").strip()
        ref = item.get("reference_source", "").strip()
        
        # Length constraints
        if len(ans) < 150:
            issues.append(f"sample_answer too short in {qid}: {len(ans)} chars (<150)")
        if len(exp) < 50:
            issues.append(f"explanation too short in {qid}: {len(exp)} chars (<50)")
        if len(rub) < 50:
            issues.append(f"rubric too short in {qid}: {len(rub)} chars (<50)")
        if len(ref) < 10:
            issues.append(f"reference_source too short in {qid}: {len(ref)} chars (<10)")
            
        # Boilerplate checks
        if old_boilerplate in ans:
            issues.append(f"Old boilerplate found in sample_answer of {qid}")
        if old_boilerplate in exp:
            issues.append(f"Old boilerplate found in explanation of {qid}")
        if old_boilerplate in rub:
            issues.append(f"Old boilerplate found in rubric of {qid}")
            
        # Rubric point alignment
        point_str_1 = f"{pts} điểm"
        point_str_2 = f"{pts} diem"
        point_str_3 = f"{pts} pts"
        point_str_4 = f"{pts}.0 điểm"
        if not (point_str_1 in rub or point_str_2 in rub.lower() or point_str_3 in rub.lower() or point_str_4 in rub):
            issues.append(f"Rubric does not specify {pts} points in {qid}")
            
        # Authoritative reference check
        if not ("http://" in ref or "https://" in ref):
            issues.append(f"reference_source missing valid HTTP/HTTPS URL in {qid}: '{ref}'")
            
    if issues:
        print(f"\nAUDIT FAILED WITH {len(issues)} ISSUES:")
        for iss in issues[:30]:
            print("  *", iss)
        if len(issues) > 30:
            print(f"  ... and {len(issues) - 30} more issues")
        raise AssertionError(f"Block 01-03 quality audit failed with {len(issues)} issues.")
        
    print("ALL 187 QUESTIONS PASSED DEEP QUALITY AUDIT 100%!")
    
    # Step 3: Write to target file
    out_dir = Path("data")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "essay_block_01_03.json"
    
    print(f"\n=== Step 3: Writing output to {out_file} ===")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(block_data, f, ensure_ascii=False, indent=2)
        
    file_size_kb = out_file.stat().st_size / 1024
    print(f"Successfully generated {out_file} ({file_size_kb:.1f} KB, {len(block_data)} questions)")
    
    # Step 4: Verification of the written file
    print("\n=== Step 4: Verifying written file on disk ===")
    with open(out_file, "r", encoding="utf-8") as f:
        reloaded = json.load(f)
        
    assert len(reloaded) == 187, f"File content mismatch: expected 187, got {len(reloaded)}"
    print(f"VERIFICATION SUCCESSFUL: {out_file} contains exactly 187 fully-authored essay questions!")

if __name__ == "__main__":
    assemble_and_verify()
