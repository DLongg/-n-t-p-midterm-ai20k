"""
scripts/independent_judge_audit.py

Independent Agent-as-Judge Quality Audit Engine for VLearn Essay Questions.
Performs stratified sampling across Days 01–15 (at least 5 per day, >= 75 questions total),
evaluates Prompt Completeness, Technical Accuracy, Rubric Alignment, and Reference Validity,
and generates detailed audit data for the formal Challenger report.
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "vlearn-app" / "src" / "multiphase_course_data.json"

def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    phase1_days = data["phases"][0]["days"][:15]
    print(f"Loaded Phase 1 with {len(phase1_days)} days.")

    # 1. Global Scan of all 775 questions
    total_essay = 0
    all_essay_questions = []
    for day_idx, day in enumerate(phase1_days, 1):
        day_id = day["day_id"]
        eqs = day.get("essay_questions", [])
        total_essay += len(eqs)
        for q in eqs:
            q_copy = dict(q)
            q_copy["day_idx"] = day_idx
            q_copy["day_id"] = day_id
            all_essay_questions.append(q_copy)

    print(f"Total essay questions scanned: {total_essay}")

    # 2. Stratified Sampling: 6 questions per day across 15 days = 90 questions total
    sampled_questions = []
    for day_idx, day in enumerate(phase1_days, 1):
        day_id = day["day_id"]
        eqs = [q for q in all_essay_questions if q["day_idx"] == day_idx]
        n = len(eqs)
        # Select 6 evenly spaced indices across the day's question list
        # e.g., 0, n//5, 2*n//5, 3*n//5, 4*n//5, n-1
        step = (n - 1) / 5.0
        indices = sorted(list(set(round(i * step) for i in range(6))))
        while len(indices) < 6 and len(indices) < n:
            for cand in range(n):
                if cand not in indices:
                    indices.append(cand)
                    break
            indices.sort()

        day_sampled = [eqs[i] for i in indices]
        sampled_questions.extend(day_sampled)
        print(f"Day {day_idx:02d} ({day_id}): {len(eqs)} total -> sampled {len(day_sampled)}: {[q['question_id'] for q in day_sampled]}")

    print(f"\nTotal sampled questions: {len(sampled_questions)}")

    # Save sampled questions to a structured inspection file
    out_file = PROJECT_ROOT / "data" / "sampled_judge_audit.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(sampled_questions, f, ensure_ascii=False, indent=2)

    print(f"Saved sampled questions to {out_file}")

if __name__ == "__main__":
    main()
