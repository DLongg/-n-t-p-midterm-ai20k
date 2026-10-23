#!/usr/bin/env python3
"""
scripts/partition_audit_batches.py

Partitions the questions across Days 01–15 into 3 clean, structured audit batch work files
under `.audit_work/`:
- `batch_days_01_05.json`: Days 01–05 (Day 01 to Day 05)
- `batch_days_06_10.json`: Days 06–10 (Day 06 to Day 10)
- `batch_days_11_15.json`: Days 11–15 (Day 11 to Day 15)

Each question entry contains:
- `day`: integer (1-15)
- `day_id`: string (e.g. 'p1_day_01')
- `question_id`: string (e.g. 'd01-q001')
- `is_standard`: boolean (whether this question is in the 165 standard set)
- `interaction_type`: string ('single_select', 'multi_select', 'matching', 'ordering', 'numeric_input')
- `prompt`: string (question text)
- `choices`: list or None (for single_select / multi_select)
- `options`: list or None (for ordering)
- `left`: list or None (for matching)
- `right`: list or None (for matching)
- `required_unit`: string or None (for numeric_input)
- `current_correct_answer`: any (current answer value)
- `explanation`: string
- `status`: string ('NEEDS_REVIEW' or 'READY_FOR_AUDIT')
- `needs_review`: boolean
- `review_reasons`: list of string reason tags
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CANONICAL_JSON = Path("vlearn-app/src/multiphase_course_data.json")
AUDIT_WORK_DIR = Path(".audit_work")

BATCH_CONFIGS = [
    {
        "filename": "batch_days_01_05.json",
        "title": "Batch Days 01–05",
        "start_day": 1,
        "end_day": 5,
    },
    {
        "filename": "batch_days_06_10.json",
        "title": "Batch Days 06–10",
        "start_day": 6,
        "end_day": 10,
    },
    {
        "filename": "batch_days_11_15.json",
        "title": "Batch Days 11–15",
        "start_day": 11,
        "end_day": 15,
    },
]


def extract_question_record(
    q: dict[str, Any],
    day_num: int,
    day_id: str,
    standard_ids: set[str],
) -> dict[str, Any]:
    qid = q.get("question_id", "")
    inter = q.get("interaction", {})
    itype = inter.get("type", "")
    ca = q.get("correct_answer")
    explanation = q.get("explanation", "")
    prompt = q.get("prompt") or inter.get("prompt", "")

    # Extract interaction items
    choices = inter.get("choices")
    options = inter.get("options")
    left = inter.get("left")
    right = inter.get("right")
    required_unit = inter.get("required_unit")

    # Review heuristics
    review_reasons: list[str] = []
    if itype == "numeric_input" and (ca == "0" or ca == 0 or ca == "None" or ca is None):
        review_reasons.append("numeric_dummy_zero")

    if itype == "single_select" and ca == "a":
        review_reasons.append("single_select_choice_a_default")

    needs_review = len(review_reasons) > 0
    status = "NEEDS_REVIEW" if needs_review else "READY_FOR_AUDIT"

    return {
        "day": day_num,
        "day_id": day_id,
        "question_id": qid,
        "is_standard": qid in standard_ids,
        "interaction_type": itype,
        "prompt": prompt,
        "choices": choices,
        "options": options,
        "left": left,
        "right": right,
        "required_unit": required_unit,
        "current_correct_answer": ca,
        "explanation": explanation,
        "status": status,
        "needs_review": needs_review,
        "review_reasons": review_reasons,
    }


def partition_batches(
    canonical_path: Path = CANONICAL_JSON,
    output_dir: Path = AUDIT_WORK_DIR,
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(canonical_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    phase1 = next((p for p in data.get("phases", []) if p.get("id") == "phase1"), None)
    if not phase1:
        raise ValueError("Could not find 'phase1' in course data.")

    phase1_days = phase1.get("days", [])[:15]

    # Collect all standard IDs
    standard_ids = {
        q.get("question_id")
        for day in phase1_days
        for q in day.get("questions", [])
        if q.get("question_id")
    }

    summary: dict[str, Any] = {}

    for cfg in BATCH_CONFIGS:
        start_day = cfg["start_day"]
        end_day = cfg["end_day"]
        filename = cfg["filename"]
        out_file = output_dir / filename

        batch_days = phase1_days[start_day - 1 : end_day]
        questions_list: list[dict[str, Any]] = []

        needs_review_count = 0
        numeric_zero_count = 0
        choice_a_count = 0
        standard_count = 0

        for day_offset, day in enumerate(batch_days):
            day_num = start_day + day_offset
            day_id = day.get("day_id", f"p1_day_{day_num:02d}")

            for q in day.get("expanded_questions", []):
                rec = extract_question_record(q, day_num, day_id, standard_ids)
                questions_list.append(rec)

                if rec["is_standard"]:
                    standard_count += 1
                if rec["needs_review"]:
                    needs_review_count += 1
                if "numeric_dummy_zero" in rec["review_reasons"]:
                    numeric_zero_count += 1
                if "single_select_choice_a_default" in rec["review_reasons"]:
                    choice_a_count += 1

        batch_data = {
            "batch_name": cfg["title"],
            "filename": filename,
            "start_day": start_day,
            "end_day": end_day,
            "day_count": len(batch_days),
            "total_questions": len(questions_list),
            "standard_questions_count": standard_count,
            "needs_review_count": needs_review_count,
            "flags_breakdown": {
                "numeric_dummy_zero": numeric_zero_count,
                "single_select_choice_a_default": choice_a_count,
            },
            "questions": questions_list,
        }

        with open(out_file, "w", encoding="utf-8", newline="\n") as f:
            json.dump(batch_data, f, ensure_ascii=False, indent=2)

        summary[filename] = {
            "path": str(out_file),
            "total_questions": len(questions_list),
            "standard_count": standard_count,
            "needs_review_count": needs_review_count,
            "numeric_zero_count": numeric_zero_count,
            "choice_a_count": choice_a_count,
        }

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Partition Days 01-15 into audit batches")
    parser.parse_args()

    print("=== Partitioning Days 01–15 into Audit Work Batches ===")
    summary = partition_batches()

    total_q = sum(s["total_questions"] for s in summary.values())
    total_std = sum(s["standard_count"] for s in summary.values())
    total_rev = sum(s["needs_review_count"] for s in summary.values())
    total_num0 = sum(s["numeric_zero_count"] for s in summary.values())
    total_cha = sum(s["choice_a_count"] for s in summary.values())

    print(f"\n[+] Created {len(summary)} batch files under '{AUDIT_WORK_DIR}':")
    for fname, info in summary.items():
        print(
            f"    - {fname}: {info['total_questions']} questions "
            f"({info['standard_count']} std, {info['needs_review_count']} needs review: "
            f"{info['numeric_zero_count']} num-0, {info['choice_a_count']} choice-a)"
        )

    print(f"\nTotal questions partitioned: {total_q} (Expected: 904)")
    print(f"Total standard questions: {total_std} (Expected: 165)")
    print(f"Total needs-review flagged: {total_rev}")
    print(f"  - Numeric dummy zero: {total_num0} (Expected: 63)")
    print(f"  - Single select choice 'a': {total_cha}")

    assert total_q == 904, f"Expected 904 questions, got {total_q}"
    assert total_std == 165, f"Expected 165 standard questions, got {total_std}"
    assert total_num0 == 63, f"Expected 63 numeric dummy zero, got {total_num0}"

    print("\n[SUCCESS] Batch partitioning verified and complete!")


if __name__ == "__main__":
    main()
