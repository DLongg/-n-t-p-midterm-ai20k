"""
scripts/evaluate_judge_samples.py

Deep evaluation of the 90 sampled questions across Days 01–15.
Evaluates:
1. Prompt Completeness
2. Technical Accuracy
3. Rubric Alignment
4. Reference Validity
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_PATH = PROJECT_ROOT / "data" / "sampled_judge_audit.json"

def evaluate_sample():
    with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
        samples = json.load(f)

    print(f"Loaded {len(samples)} sample questions.")

    results = []
    pass_count = 0

    for idx, q in enumerate(samples, 1):
        qid = q["question_id"]
        day_idx = q["day_idx"]
        day_id = q["day_id"]
        pts = q.get("points")
        prompt = q.get("interaction", {}).get("prompt", "")
        sample_ans = q.get("sample_answer", "")
        explanation = q.get("explanation", "")
        rubric = q.get("rubric", "")
        ref = q.get("reference_source", "")

        # Check Rubric Alignment
        header_m = re.search(r"(?:Rubric|Thang điểm|Điểm tối đa)\s*:?\s*(\d+(?:\.\d+)?)\s*(?:điểm|đ)", rubric, re.IGNORECASE)
        header_pts = float(header_m.group(1)) if header_m else None
        
        # Criteria sub-points
        sub_pts = []
        for line in rubric.splitlines():
            if header_m and line.strip() == header_m.group(0).strip():
                continue
            paren_m = re.search(r"[\(\[]\s*(\d+(?:\.\d+)?)\s*(?:điểm|đ)\s*[\)\]]", line, re.IGNORECASE)
            if paren_m:
                sub_pts.append(float(paren_m.group(1)))
                continue
            bullet_m = re.search(r"(?:^|\s)(?:[-*•]|\d+\.)\s*.*?(?:[\(\[]|\b:?\s*)(\d+(?:\.\d+)?)\s*(?:điểm|đ)\b", line, re.IGNORECASE)
            if bullet_m:
                sub_pts.append(float(bullet_m.group(1)))

        rubric_ok = True
        rubric_notes = []
        if header_pts is not None and abs(header_pts - pts) > 0.01:
            rubric_ok = False
            rubric_notes.append(f"Header pts {header_pts} != points {pts}")
        if sub_pts:
            sub_sum = sum(sub_pts)
            if abs(sub_sum - pts) > 0.05:
                rubric_ok = False
                rubric_notes.append(f"Criteria sum {sub_sum} != points {pts}")
        elif header_pts is None:
            rubric_ok = False
            rubric_notes.append("No numeric points parsed")

        # Check Reference Source
        ref_ok = len(ref.strip()) >= 10
        ref_notes = []
        if not ref_ok:
            ref_notes.append("Reference too short (<10 chars)")

        # Check Completeness (length and prompt coverage)
        ans_len = len(sample_ans.strip())
        comp_ok = ans_len >= 150
        comp_notes = []
        if not comp_ok:
            comp_notes.append(f"Answer too short ({ans_len} < 150 chars)")

        # Technical Accuracy (basic checks: non-empty, detailed explanation)
        acc_ok = len(explanation.strip()) >= 50
        acc_notes = []
        if not acc_ok:
            acc_notes.append(f"Explanation too short ({len(explanation.strip())} < 50 chars)")

        is_pass = rubric_ok and ref_ok and comp_ok and acc_ok
        if is_pass:
            pass_count += 1

        results.append({
            "index": idx,
            "qid": qid,
            "day": f"Day {day_idx:02d}",
            "day_id": day_id,
            "points": pts,
            "prompt_summary": prompt.replace("\n", " ")[:80] + ("..." if len(prompt) > 80 else ""),
            "full_prompt": prompt,
            "sample_answer": sample_ans,
            "rubric": rubric,
            "reference_source": ref,
            "explanation": explanation,
            "ans_len": ans_len,
            "rubric_ok": rubric_ok,
            "rubric_notes": rubric_notes,
            "ref_ok": ref_ok,
            "ref_notes": ref_notes,
            "comp_ok": comp_ok,
            "comp_notes": comp_notes,
            "acc_ok": acc_ok,
            "acc_notes": acc_notes,
            "is_pass": is_pass,
        })

    print(f"\nAutomated Evaluation Results:")
    print(f"Total evaluated: {len(results)}")
    print(f"Passed: {pass_count} / {len(results)} ({pass_count / len(results) * 100:.2f}%)")

    # Save detailed evaluation
    eval_file = PROJECT_ROOT / "data" / "judge_evaluation_raw.json"
    with open(eval_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved evaluation details to {eval_file}")

if __name__ == "__main__":
    evaluate_sample()
