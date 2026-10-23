"""
tests/test_quiz_schema.py

Pytest test suite integrating Pydantic schema validation for:
- Phase 1 structure (15 days)
- 165 standard questions (`questions`)
- 904 expanded questions (`expanded_questions`)
- 5 interaction types: single_select, multi_select, matching, ordering, numeric_input
- Non-empty explanations

Designed to establish the M0 baseline and verify data integrity throughout project milestones.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List

import pytest

# Ensure scripts directory is importable
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.validate_schemas import (
    EXPECTED_DAY_COUNTS,
    TOTAL_EXPECTED_EXP,
    TOTAL_EXPECTED_STD,
    QuestionValidationModel,
    validate_course_data,
    validate_question,
)


class TestQuizStructure:
    """Verifies the high-level JSON structure and day-by-day question counts."""

    def test_multiphase_json_exists_and_parses(self, multiphase_data: Dict[str, Any]):
        assert "phases" in multiphase_data, "Missing 'phases' key in JSON"
        assert len(multiphase_data["phases"]) >= 1, "No phases found in JSON"

    def test_phase1_days_and_total_counts(self, phase1_days: List[Dict[str, Any]]):
        assert len(phase1_days) == 15, f"Phase 1 must contain exactly 15 active days, found {len(phase1_days)}"
        total_std = sum(len(d.get("questions", [])) for d in phase1_days)
        total_exp = sum(len(d.get("expanded_questions", [])) for d in phase1_days)

        assert total_std == TOTAL_EXPECTED_STD, f"Expected {TOTAL_EXPECTED_STD} standard questions, found {total_std}"
        assert total_exp == TOTAL_EXPECTED_EXP, f"Expected {TOTAL_EXPECTED_EXP} expanded questions, found {total_exp}"

    @pytest.mark.parametrize("day_num", list(range(1, 16)))
    def test_day_question_counts(self, phase1_days: List[Dict[str, Any]], day_num: int):
        day = phase1_days[day_num - 1]
        std_count = len(day.get("questions", []))
        exp_count = len(day.get("expanded_questions", []))

        expected_std = EXPECTED_DAY_COUNTS[day_num]["std"]
        expected_exp = EXPECTED_DAY_COUNTS[day_num]["exp"]

        assert std_count == expected_std, (
            f"Day {day_num} ({day.get('day_id')}) standard question count mismatch: got {std_count}, expected {expected_std}"
        )
        assert exp_count == expected_exp, (
            f"Day {day_num} ({day.get('day_id')}) expanded question count mismatch: got {exp_count}, expected {expected_exp}"
        )


class TestStandardQuestionsSchema:
    """Validates all 165 standard questions across all 5 interaction types."""

    def test_all_165_standard_questions_valid(self, standard_questions: List[Dict[str, Any]]):
        assert len(standard_questions) == TOTAL_EXPECTED_STD
        failures = []
        for q in standard_questions:
            err = validate_question(q)
            if err:
                failures.append(f"Day {q['_day_num']} [{q.get('question_id')}]: {err}")

        assert len(failures) == 0, f"{len(failures)} standard questions failed validation:\n" + "\n".join(failures)

    def test_standard_single_select(self, standard_questions: List[Dict[str, Any]]):
        ss_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "single_select"]
        assert len(ss_questions) == 70, f"Expected 70 single_select standard questions, found {len(ss_questions)}"
        for q in ss_questions:
            err = validate_question(q)
            assert err is None, f"Question {q.get('question_id')} error: {err}"

    def test_standard_multi_select(self, standard_questions: List[Dict[str, Any]]):
        ms_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "multi_select"]
        assert len(ms_questions) == 28, f"Expected 28 multi_select standard questions, found {len(ms_questions)}"
        for q in ms_questions:
            err = validate_question(q)
            assert err is None, f"Question {q.get('question_id')} error: {err}"

    def test_standard_matching(self, standard_questions: List[Dict[str, Any]]):
        mat_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "matching"]
        assert len(mat_questions) == 46, f"Expected 46 matching standard questions, found {len(mat_questions)}"
        for q in mat_questions:
            err = validate_question(q)
            assert err is None, f"Question {q.get('question_id')} error: {err}"

    def test_standard_ordering(self, standard_questions: List[Dict[str, Any]]):
        ord_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "ordering"]
        assert len(ord_questions) == 15, f"Expected 15 ordering standard questions, found {len(ord_questions)}"
        for q in ord_questions:
            err = validate_question(q)
            assert err is None, f"Question {q.get('question_id')} error: {err}"

    def test_standard_numeric_input(self, standard_questions: List[Dict[str, Any]]):
        num_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "numeric_input"]
        assert len(num_questions) == 6, f"Expected 6 numeric_input standard questions, found {len(num_questions)}"
        for q in num_questions:
            err = validate_question(q)
            assert err is None, f"Question {q.get('question_id')} error: {err}"


class TestExpandedQuestionsSchema:
    """Validates the 904 expanded questions across all 5 interaction types."""

    def test_expanded_questions_count(self, expanded_questions: List[Dict[str, Any]]):
        assert len(expanded_questions) == TOTAL_EXPECTED_EXP

    def test_expanded_single_select(self, expanded_questions: List[Dict[str, Any]]):
        ss_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "single_select"]
        assert len(ss_questions) == 471, f"Expected 471 single_select expanded questions, found {len(ss_questions)}"
        failures = []
        for q in ss_questions:
            err = validate_question(q)
            if err:
                failures.append(f"Day {q['_day_num']} [{q.get('question_id')}]: {err}")
        assert len(failures) == 0, f"{len(failures)} single_select questions failed:\n" + "\n".join(failures)

    def test_expanded_multi_select(self, expanded_questions: List[Dict[str, Any]]):
        ms_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "multi_select"]
        assert len(ms_questions) == 136, f"Expected 136 multi_select expanded questions, found {len(ms_questions)}"
        failures = []
        for q in ms_questions:
            err = validate_question(q)
            if err:
                failures.append(f"Day {q['_day_num']} [{q.get('question_id')}]: {err}")
        assert len(failures) == 0, f"{len(failures)} multi_select questions failed:\n" + "\n".join(failures)

    def test_expanded_ordering(self, expanded_questions: List[Dict[str, Any]]):
        ord_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "ordering"]
        assert len(ord_questions) == 72, f"Expected 72 ordering expanded questions, found {len(ord_questions)}"
        failures = []
        for q in ord_questions:
            err = validate_question(q)
            if err:
                failures.append(f"Day {q['_day_num']} [{q.get('question_id')}]: {err}")
        assert len(failures) == 0, f"{len(failures)} ordering questions failed:\n" + "\n".join(failures)

    def test_expanded_matching(self, expanded_questions: List[Dict[str, Any]]):
        """
        Validates 156 matching questions.
        In M0 baseline, catches 48 questions with empty correct_answer {}.
        After M2.1/M2 audit repair, 100% must pass.
        """
        mat_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "matching"]
        assert len(mat_questions) == 156, f"Expected 156 matching expanded questions, found {len(mat_questions)}"
        failures = []
        for q in mat_questions:
            err = validate_question(q)
            if err:
                failures.append(f"Day {q['_day_num']} [{q.get('question_id')}]: {err}")

        # In baseline, exactly 48 are empty dicts
        assert len(failures) == 0, (
            f"Matching schema validation caught {len(failures)} invalid questions (Baseline known: 48 empty matching):\n"
            + "\n".join(failures[:10])
        )

    def test_expanded_numeric_input(self, expanded_questions: List[Dict[str, Any]]):
        """
        Validates 69 numeric_input questions.
        In M0 baseline, catches 69 non-numeric answers (6 'None' + 63 dummy string '0').
        After M2 audit calculation & repair, 100% must pass.
        """
        num_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "numeric_input"]
        assert len(num_questions) == 69, f"Expected 69 numeric_input expanded questions, found {len(num_questions)}"
        failures = []
        for q in num_questions:
            err = validate_question(q)
            if err:
                failures.append(f"Day {q['_day_num']} [{q.get('question_id')}]: {err}")

        # In baseline, exactly 69 are non-numeric strings ('None' or '0')
        assert len(failures) == 0, (
            f"Numeric schema validation caught {len(failures)} invalid questions (Baseline known: 69 invalid numeric):\n"
            + "\n".join(failures[:10])
        )


class TestExplanationsSchema:
    """Verifies that all questions across standard and expanded sets have non-empty explanations."""

    def test_all_standard_explanations_non_empty(self, standard_questions: List[Dict[str, Any]]):
        for q in standard_questions:
            exp = q.get("explanation")
            assert isinstance(exp, str) and len(exp.strip()) > 0, (
                f"Question {q.get('question_id')} has missing or empty explanation"
            )

    def test_all_expanded_explanations_non_empty(self, expanded_questions: List[Dict[str, Any]]):
        for q in expanded_questions:
            exp = q.get("explanation")
            assert isinstance(exp, str) and len(exp.strip()) > 0, (
                f"Question {q.get('question_id')} has missing or empty explanation"
            )
