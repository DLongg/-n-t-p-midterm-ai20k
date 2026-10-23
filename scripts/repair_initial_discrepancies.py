#!/usr/bin/env python3
"""
scripts/repair_initial_discrepancies.py

Milestone M2.1: Repair initial shared question discrepancies in `vlearn-app/src/multiphase_course_data.json`.
1. Restores 46 matching questions in `expanded_questions` that have empty `{}` by copying
   the valid mapping from the corresponding standard question with the same `question_id`.
2. Restores `d01-q008` and `d01-q069` matching answers from `verified_all_quizzes_master.json`.
3. Restores 6 numeric_input questions in `expanded_questions` that have `"None"` by copying
   the valid numeric answer from the corresponding standard question.
4. Verifies that all 48 empty matching questions now have valid `{left_id: right_id}` dictionaries.
5. Saves the repaired `vlearn-app/src/multiphase_course_data.json` preserving formatting (indent 2, utf-8).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CANONICAL_JSON = Path("vlearn-app/src/multiphase_course_data.json")
MASTER_JSON = Path("verified_all_quizzes_master.json")


def repair_initial_discrepancies(
    canonical_path: Path = CANONICAL_JSON,
    master_path: Path = MASTER_JSON,
    dry_run: bool = False,
) -> dict[str, Any]:
    """
    Executes the initial repair on canonical course data JSON.
    Returns a summary dictionary of repaired items.
    """
    if not canonical_path.exists():
        raise FileNotFoundError(f"Canonical course data file not found at: {canonical_path}")
    if not master_path.exists():
        raise FileNotFoundError(f"Master solutions file not found at: {master_path}")

    with open(canonical_path, "r", encoding="utf-8") as f:
        course_data = json.load(f)

    with open(master_path, "r", encoding="utf-8") as f:
        master_solutions = json.load(f)

    # Locate Phase 1 days
    phase1 = next((p for p in course_data.get("phases", []) if p.get("id") == "phase1"), None)
    if not phase1:
        raise ValueError("Could not find 'phase1' in canonical course data.")

    phase1_days = phase1.get("days", [])[:15]

    # Build map of standard questions
    std_map: dict[str, dict[str, Any]] = {}
    for day in phase1_days:
        for q in day.get("questions", []):
            qid = q.get("question_id")
            if qid:
                std_map[qid] = q

    repaired_matching_std: list[dict[str, Any]] = []
    repaired_matching_master: list[dict[str, Any]] = []
    repaired_numeric_std: list[dict[str, Any]] = []

    # Iterate over expanded questions across Phase 1
    for day_idx, day in enumerate(phase1_days, start=1):
        day_id = day.get("day_id", f"p1_day_{day_idx:02d}")
        exp_questions = day.get("expanded_questions", [])

        for q in exp_questions:
            qid = q.get("question_id")
            itype = q.get("interaction", {}).get("type")
            ca = q.get("correct_answer")

            # 1. Matching repair
            if itype == "matching":
                if ca == {} or not ca:
                    if qid in ("d01-q008", "d01-q069"):
                        # Restore from verified_all_quizzes_master.json
                        master_entry = master_solutions.get(qid)
                        if not master_entry:
                            raise ValueError(f"Question {qid} not found in master solutions.")
                        correct_pairs = (
                            master_entry.get("correct_response", {}).get("correct_pairs")
                        )
                        if not isinstance(correct_pairs, dict) or not correct_pairs:
                            raise ValueError(f"Invalid or empty correct_pairs for {qid} in master solutions.")

                        q["correct_answer"] = dict(correct_pairs)
                        repaired_matching_master.append({
                            "day": day_idx,
                            "day_id": day_id,
                            "question_id": qid,
                            "source": "verified_all_quizzes_master.json",
                            "new_correct_answer": dict(correct_pairs),
                        })

                    elif qid in std_map:
                        std_q = std_map[qid]
                        std_ca = std_q.get("correct_answer")
                        if not isinstance(std_ca, dict) or not std_ca:
                            raise ValueError(f"Standard question {qid} does not have valid matching answer: {std_ca!r}")

                        q["correct_answer"] = dict(std_ca)
                        repaired_matching_std.append({
                            "day": day_idx,
                            "day_id": day_id,
                            "question_id": qid,
                            "source": f"standard_questions ({std_q.get('question_id')})",
                            "new_correct_answer": dict(std_ca),
                        })
                    else:
                        raise ValueError(f"Empty matching question {qid} not found in standard or master.")

            # 2. Numeric repair
            elif itype == "numeric_input" and (ca == "None" or ca is None):
                if qid in std_map:
                    std_q = std_map[qid]
                    std_ca = std_q.get("correct_answer")
                    if not isinstance(std_ca, (int, float)):
                        raise ValueError(f"Standard question {qid} does not have valid numeric answer: {std_ca!r}")

                    q["correct_answer"] = std_ca
                    repaired_numeric_std.append({
                        "day": day_idx,
                        "day_id": day_id,
                        "question_id": qid,
                        "source": f"standard_questions ({std_q.get('question_id')})",
                        "old_correct_answer": ca,
                        "new_correct_answer": std_ca,
                    })
                else:
                    raise ValueError(f"None numeric question {qid} not found in standard questions.")

    # Integrity assertions & idempotency check
    already_repaired = (
        len(repaired_matching_std) == 0
        and len(repaired_matching_master) == 0
        and len(repaired_numeric_std) == 0
    )

    if not already_repaired:
        assert len(repaired_matching_std) == 46, (
            f"Expected exactly 46 matching questions repaired from standard, got {len(repaired_matching_std)}"
        )
        assert len(repaired_matching_master) == 2, (
            f"Expected exactly 2 matching questions repaired from master, got {len(repaired_matching_master)}"
        )
        assert len(repaired_numeric_std) == 6, (
            f"Expected exactly 6 numeric questions repaired from standard, got {len(repaired_numeric_std)}"
        )

    # Verify that all 156 matching expanded questions now have non-empty dicts
    all_exp_matching = [
        q for d in phase1_days for q in d.get("expanded_questions", [])
        if q.get("interaction", {}).get("type") == "matching"
    ]
    assert len(all_exp_matching) == 156, f"Expected 156 matching questions, found {len(all_exp_matching)}"
    for q in all_exp_matching:
        ans = q.get("correct_answer")
        assert isinstance(ans, dict) and len(ans) > 0, (
            f"Question {q.get('question_id')} still has invalid matching answer: {ans!r}"
        )

    # Save changes
    if not dry_run:
        with open(canonical_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(course_data, f, ensure_ascii=False, indent=2)

    return {
        "already_repaired": already_repaired,
        "repaired_matching_std_count": len(repaired_matching_std),
        "repaired_matching_master_count": len(repaired_matching_master),
        "total_matching_repaired": len(repaired_matching_std) + len(repaired_matching_master),
        "repaired_numeric_std_count": len(repaired_numeric_std),
        "repaired_matching_std": repaired_matching_std,
        "repaired_matching_master": repaired_matching_master,
        "repaired_numeric_std": repaired_numeric_std,
        "dry_run": dry_run,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair initial shared discrepancies in multiphase_course_data.json")
    parser.add_argument("--dry-run", action="store_true", help="Inspect repairs without writing to disk")
    args = parser.parse_args()

    print("=== Running Initial Discrepancies Repair (Milestone M2.1) ===")
    results = repair_initial_discrepancies(dry_run=args.dry_run)

    if results["already_repaired"]:
        print("\n[OK] Canonical course data is ALREADY fully repaired:")
        print("     - All 48 previously empty matching questions have valid mappings.")
        print("     - All 6 previously 'None' numeric questions have valid numbers matching standard questions.")
        print("     - Zero initial discrepancies remain.")
        return

    print(f"\n[+] Repaired matching questions from standard questions: {results['repaired_matching_std_count']}")
    for r in results["repaired_matching_std"][:5]:
        print(f"    - Day {r['day']:02d} [{r['question_id']}]: -> {r['new_correct_answer']}")
    if len(results["repaired_matching_std"]) > 5:
        print(f"    ... and {len(results['repaired_matching_std']) - 5} more.")

    print(f"\n[+] Repaired matching questions from master solutions: {results['repaired_matching_master_count']}")
    for r in results["repaired_matching_master"]:
        print(f"    - Day {r['day']:02d} [{r['question_id']}]: -> {r['new_correct_answer']}")

    print(f"\n[+] Repaired numeric questions from standard questions: {results['repaired_numeric_std_count']}")
    for r in results["repaired_numeric_std"]:
        print(f"    - Day {r['day']:02d} [{r['question_id']}]: '{r['old_correct_answer']}' -> {r['new_correct_answer']}")

    print(f"\nTotal questions repaired: {results['total_matching_repaired'] + results['repaired_numeric_std_count']}")
    if args.dry_run:
        print("\n[DRY RUN] No files were modified.")
    else:
        print(f"\n[SUCCESS] Successfully updated '{CANONICAL_JSON}'!")


if __name__ == "__main__":
    main()
