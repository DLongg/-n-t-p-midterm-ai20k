#!/usr/bin/env python3
"""
scripts/validate_schemas.py

Pydantic schema validator for VLearn Quiz Audit & Cross-File Synchronization Project.
Validates all 15 Days of Phase 1 in `vlearn-app/src/multiphase_course_data.json`:
- Exactly 165 standard questions (`questions`)
- Exactly 904 expanded bank questions (`expanded_questions`)

Validates every interaction type:
1. `single_select`: `correct_answer` is string matching one `choice_id` in choices.
2. `multi_select`: `correct_answer` is non-empty list of valid `choice_id`s in choices.
3. `matching`: `correct_answer` is non-empty dict mapping every `left.id` to a valid `right.id`.
4. `ordering`: `correct_answer` is non-empty list representing complete valid permutation of `option_id`s.
5. `numeric_input`: `correct_answer` is int or float (strictly rejects "None" or "0" dummy string).
6. `explanation`: non-empty, stripped string length > 0.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Set, Tuple, Union

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator


# ----------------------------------------------------------------------
# Pydantic Interaction Submodels
# ----------------------------------------------------------------------

class ChoiceItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    choice_id: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


class MatchingLeftItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


class MatchingRightItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


class OrderingOptionItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    option_id: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)


# ----------------------------------------------------------------------
# Core Question Model
# ----------------------------------------------------------------------

class QuestionValidationModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    question_id: str = Field(..., min_length=1)
    explanation: str = Field(..., min_length=1)
    interaction: Dict[str, Any]
    correct_answer: Any

    @model_validator(mode="after")
    def validate_question_integrity(self) -> QuestionValidationModel:
        # 1. Explanation validation
        if not self.explanation or not isinstance(self.explanation, str) or not self.explanation.strip():
            raise ValueError(f"Question {self.question_id}: explanation must be a non-empty string.")

        # 2. Interaction dictionary check
        inter = self.interaction
        if not isinstance(inter, dict):
            raise ValueError(f"Question {self.question_id}: interaction must be a dictionary.")

        itype = inter.get("type")
        if not itype:
            raise ValueError(f"Question {self.question_id}: missing 'type' in interaction.")

        ca = self.correct_answer

        # 3. Type-specific validation
        if itype == "single_select":
            raw_choices = inter.get("choices")
            if not isinstance(raw_choices, list) or len(raw_choices) == 0:
                raise ValueError(f"Question {self.question_id}: single_select must have non-empty choices list.")
            valid_choice_ids = {c.get("choice_id") for c in raw_choices if isinstance(c, dict)}
            if not isinstance(ca, str):
                raise ValueError(
                    f"Question {self.question_id}: single_select correct_answer must be str, got {type(ca).__name__} ({ca!r})."
                )
            if ca not in valid_choice_ids:
                raise ValueError(
                    f"Question {self.question_id}: single_select correct_answer '{ca}' not found in choices {valid_choice_ids}."
                )

        elif itype == "multi_select":
            raw_choices = inter.get("choices")
            if not isinstance(raw_choices, list) or len(raw_choices) == 0:
                raise ValueError(f"Question {self.question_id}: multi_select must have non-empty choices list.")
            valid_choice_ids = {c.get("choice_id") for c in raw_choices if isinstance(c, dict)}
            if not isinstance(ca, list):
                raise ValueError(
                    f"Question {self.question_id}: multi_select correct_answer must be list, got {type(ca).__name__} ({ca!r})."
                )
            if len(ca) == 0:
                raise ValueError(f"Question {self.question_id}: multi_select correct_answer cannot be an empty list.")
            invalid_ids = [c for c in ca if c not in valid_choice_ids]
            if invalid_ids:
                raise ValueError(
                    f"Question {self.question_id}: multi_select correct_answer contains invalid choices {invalid_ids}; valid: {valid_choice_ids}."
                )

        elif itype == "matching":
            left_list = inter.get("left")
            right_list = inter.get("right")
            if not isinstance(left_list, list) or len(left_list) == 0:
                raise ValueError(f"Question {self.question_id}: matching must have non-empty 'left' list.")
            if not isinstance(right_list, list) or len(right_list) == 0:
                raise ValueError(f"Question {self.question_id}: matching must have non-empty 'right' list.")

            left_ids = {l.get("id") for l in left_list if isinstance(l, dict) and "id" in l}
            right_ids = {r.get("id") for r in right_list if isinstance(r, dict) and "id" in r}

            if not isinstance(ca, dict):
                raise ValueError(
                    f"Question {self.question_id}: matching correct_answer must be dict, got {type(ca).__name__} ({ca!r})."
                )
            if len(ca) == 0:
                raise ValueError(f"Question {self.question_id}: matching correct_answer is empty dictionary.")

            # Validate left keys match left items
            unmapped_left = left_ids - set(ca.keys())
            if unmapped_left:
                raise ValueError(f"Question {self.question_id}: matching answer missing mappings for left IDs: {unmapped_left}.")

            unknown_left = set(ca.keys()) - left_ids
            if unknown_left:
                raise ValueError(f"Question {self.question_id}: matching answer contains unknown left keys: {unknown_left}.")

            # Validate right values
            invalid_rights = {v for v in ca.values() if v not in right_ids}
            if invalid_rights:
                raise ValueError(f"Question {self.question_id}: matching answer maps to invalid right IDs: {invalid_rights}.")

        elif itype == "ordering":
            opts = inter.get("options")
            if not isinstance(opts, list) or len(opts) == 0:
                raise ValueError(f"Question {self.question_id}: ordering must have non-empty 'options' list.")

            option_ids = [o.get("option_id") for o in opts if isinstance(o, dict) and "option_id" in o]
            if not isinstance(ca, list):
                raise ValueError(
                    f"Question {self.question_id}: ordering correct_answer must be list, got {type(ca).__name__} ({ca!r})."
                )
            if len(ca) == 0:
                raise ValueError(f"Question {self.question_id}: ordering correct_answer cannot be empty list.")

            if sorted(ca) != sorted(option_ids):
                raise ValueError(
                    f"Question {self.question_id}: ordering correct_answer {ca} is not a valid permutation of options {option_ids}."
                )

        elif itype == "numeric_input":
            if ca is None:
                raise ValueError(f"Question {self.question_id}: numeric_input correct_answer cannot be None.")
            if isinstance(ca, str):
                raise ValueError(
                    f"Question {self.question_id}: numeric_input correct_answer cannot be string ({ca!r}), must be int or float."
                )
            if not isinstance(ca, (int, float)):
                raise ValueError(
                    f"Question {self.question_id}: numeric_input correct_answer must be int or float, got {type(ca).__name__} ({ca!r})."
                )

        else:
            raise ValueError(f"Question {self.question_id}: unsupported interaction type '{itype}'.")

        return self


# ----------------------------------------------------------------------
# Batch Validation Functions
# ----------------------------------------------------------------------

EXPECTED_DAY_COUNTS = {
    1: {"std": 10, "exp": 101},
    2: {"std": 5, "exp": 35},
    3: {"std": 15, "exp": 32},
    4: {"std": 15, "exp": 58},
    5: {"std": 10, "exp": 40},
    6: {"std": 15, "exp": 26},
    7: {"std": 10, "exp": 63},
    8: {"std": 10, "exp": 57},
    9: {"std": 10, "exp": 59},
    10: {"std": 10, "exp": 64},
    11: {"std": 10, "exp": 65},
    12: {"std": 10, "exp": 86},
    13: {"std": 10, "exp": 76},
    14: {"std": 10, "exp": 74},
    15: {"std": 15, "exp": 68},
}

TOTAL_EXPECTED_STD = 165
TOTAL_EXPECTED_EXP = 904


def validate_question(q_dict: Dict[str, Any]) -> Optional[str]:
    """Validates a single question dict. Returns None if valid, or error message string if invalid."""
    try:
        QuestionValidationModel.model_validate(q_dict)
        return None
    except ValidationError as err:
        return "; ".join([e["msg"] for e in err.errors()])
    except Exception as exc:
        return str(exc)


def validate_course_data(filepath: Union[str, Path]) -> Dict[str, Any]:
    """
    Validates `multiphase_course_data.json` across all 15 Days of Phase 1.
    Returns structured results dictionary.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    phases = data.get("phases", [])
    if not phases:
        raise ValueError("Invalid format: 'phases' key missing or empty.")

    phase1 = phases[0]
    days = phase1.get("days", [])
    if len(days) < 15:
        raise ValueError(f"Expected at least 15 days in Phase 1, found {len(days)}.")

    results: Dict[str, Any] = {
        "filepath": str(path),
        "days_checked": 15,
        "std_total": 0,
        "exp_total": 0,
        "std_valid": 0,
        "exp_valid": 0,
        "std_errors": [],
        "exp_errors": [],
        "day_counts": {},
        "structure_errors": [],
    }

    for day_idx in range(15):
        day_num = day_idx + 1
        day = days[day_idx]
        day_id = day.get("day_id", f"Day_{day_num}")

        std_qs = day.get("questions", [])
        exp_qs = day.get("expanded_questions", [])

        results["std_total"] += len(std_qs)
        results["exp_total"] += len(exp_qs)

        results["day_counts"][day_num] = {
            "day_id": day_id,
            "std_actual": len(std_qs),
            "std_expected": EXPECTED_DAY_COUNTS[day_num]["std"],
            "exp_actual": len(exp_qs),
            "exp_expected": EXPECTED_DAY_COUNTS[day_num]["exp"],
        }

        # Check expected counts
        if len(std_qs) != EXPECTED_DAY_COUNTS[day_num]["std"]:
            results["structure_errors"].append(
                f"Day {day_num} ({day_id}): expected {EXPECTED_DAY_COUNTS[day_num]['std']} standard questions, got {len(std_qs)}."
            )
        if len(exp_qs) != EXPECTED_DAY_COUNTS[day_num]["exp"]:
            results["structure_errors"].append(
                f"Day {day_num} ({day_id}): expected {EXPECTED_DAY_COUNTS[day_num]['exp']} expanded questions, got {len(exp_qs)}."
            )

        # Validate standard questions
        for q in std_qs:
            err = validate_question(q)
            if err:
                results["std_errors"].append({
                    "day": day_num,
                    "question_id": q.get("question_id", "UNKNOWN"),
                    "type": q.get("interaction", {}).get("type", "UNKNOWN"),
                    "error": err,
                })
            else:
                results["std_valid"] += 1

        # Validate expanded questions
        for q in exp_qs:
            err = validate_question(q)
            if err:
                results["exp_errors"].append({
                    "day": day_num,
                    "question_id": q.get("question_id", "UNKNOWN"),
                    "type": q.get("interaction", {}).get("type", "UNKNOWN"),
                    "error": err,
                })
            else:
                results["exp_valid"] += 1

    results["passed"] = (
        len(results["structure_errors"]) == 0
        and len(results["std_errors"]) == 0
        and len(results["exp_errors"]) == 0
        and results["std_total"] == TOTAL_EXPECTED_STD
        and results["exp_total"] == TOTAL_EXPECTED_EXP
    )

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Pydantic schema validator for VLearn quiz questions.")
    parser.add_argument(
        "--json-path",
        default="vlearn-app/src/multiphase_course_data.json",
        help="Path to multiphase_course_data.json (default: vlearn-app/src/multiphase_course_data.json)",
    )
    parser.add_argument(
        "--show-errors",
        action="store_true",
        default=True,
        help="Show detailed list of validation errors",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero code if any validation errors are detected",
    )
    args = parser.parse_args()

    print(f"=== VLearn Pydantic Quiz Schema Validator ===")
    print(f"Target: {args.json_path}\n")

    try:
        res = validate_course_data(args.json_path)
    except Exception as exc:
        print(f"FATAL ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Phase 1 Days checked: {res['days_checked']}")
    print(f"Standard Questions : {res['std_valid']}/{res['std_total']} valid (Expected: {TOTAL_EXPECTED_STD})")
    print(f"Expanded Questions : {res['exp_valid']}/{res['exp_total']} valid (Expected: {TOTAL_EXPECTED_EXP})")

    if res["structure_errors"]:
        print("\n[!] Structure / Count Discrepancies:")
        for err in res["structure_errors"]:
            print(f"    - {err}")

    if res["std_errors"]:
        print(f"\n[!] Standard Questions Errors ({len(res['std_errors'])}):")
        for err in res["std_errors"][:15]:
            print(f"    - Day {err['day']} [{err['question_id']}] ({err['type']}): {err['error']}")
        if len(res["std_errors"]) > 15:
            print(f"    ... and {len(res['std_errors']) - 15} more.")

    if res["exp_errors"]:
        print(f"\n[!] Expanded Questions Errors ({len(res['exp_errors'])}):")
        # Group by type and error reason
        from collections import Counter
        err_types = Counter(e["type"] for e in res["exp_errors"])
        for etype, cnt in err_types.items():
            print(f"    - Interaction type '{etype}': {cnt} invalid questions")
        print("\nSample expanded errors:")
        for err in res["exp_errors"][:10]:
            print(f"    - Day {err['day']} [{err['question_id']}] ({err['type']}): {err['error']}")
        if len(res["exp_errors"]) > 10:
            print(f"    ... and {len(res['exp_errors']) - 10} more.")

    print("\n------------------------------------------------------------")
    if res["passed"]:
        print("[SUCCESS] All 165 standard and 904 expanded questions pass strict Pydantic validation!")
        return 0
    else:
        print(f"[BASELINE REPORT] Validation complete. Found {len(res['std_errors']) + len(res['exp_errors'])} data issues.")
        if args.strict:
            return 1
        return 0


if __name__ == "__main__":
    sys.exit(main())
