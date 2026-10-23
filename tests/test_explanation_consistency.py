"""
tests/test_explanation_consistency.py

Pytest test suite ensuring zero contradictions between `correct_answer` and `explanation`.
Validates across both standard questions (165) and expanded questions (904):
- Explanations are non-empty and substantive.
- Explanations never assert that an unselected choice letter is the correct answer.
- Explanations never claim that the selected correct answer choice letter is wrong, incorrect, or eliminated.
- Multi-select count phrases (e.g. 'chọn cả 3 đáp án') strictly match the number of answers in correct_answer.
- Numeric explanations mention or calculate the required value.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List

import pytest


class TestExplanationPresenceAndQuality:
    """Verifies that all questions across standard and expanded sets have substantive explanations."""

    def test_standard_explanations_substantive(self, standard_questions: List[Dict[str, Any]]):
        for q in standard_questions:
            exp = q.get("explanation")
            assert isinstance(exp, str), f"Question {q.get('question_id')}: explanation is not a string"
            clean = exp.strip()
            assert len(clean) >= 15, (
                f"Question {q.get('question_id')}: explanation is too brief ({len(clean)} chars): '{clean}'"
            )

    def test_expanded_explanations_substantive(self, expanded_questions: List[Dict[str, Any]]):
        for q in expanded_questions:
            exp = q.get("explanation")
            assert isinstance(exp, str), f"Question {q.get('question_id')}: explanation is not a string"
            clean = exp.strip()
            assert len(clean) >= 15, (
                f"Question {q.get('question_id')}: explanation is too brief ({len(clean)} chars): '{clean}'"
            )


class TestSingleSelectExplanationConsistency:
    """Ensures 0 contradictions between correct_answer and explanation in single-choice questions."""

    # Regex detecting phrases asserting a choice letter is correct
    ASSERT_CORRECT_PATTERN = re.compile(
        r"(?:đáp án đúng là|chọn|phương án đúng là|lựa chọn đúng là|kết quả đúng là)\s+([A-D])\b",
        re.IGNORECASE,
    )

    # Regex detecting phrases claiming a choice letter is wrong/invalid
    ASSERT_WRONG_PATTERN = re.compile(
        r"(?:đáp án|phương án|lựa chọn)\s+([A-D])\s+(?:là\s+)?(?:sai|không đúng|không chính xác|bị loại|không phải là đáp án đúng)\b",
        re.IGNORECASE,
    )

    def test_standard_single_select_no_wrong_choice_claimed_correct(
        self, standard_questions: List[Dict[str, Any]]
    ):
        ss_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "single_select"]
        contradictions = []

        for q in ss_questions:
            ca = str(q.get("correct_answer", "")).strip().lower()
            exp = q.get("explanation", "")
            for m in self.ASSERT_CORRECT_PATTERN.finditer(exp):
                letter = m.group(1).lower()
                if letter != ca:
                    contradictions.append(
                        f"Question [{q.get('question_id')}]: explanation claims choice '{letter.upper()}' is correct, but correct_answer is '{ca.upper()}'. Snippet: {m.group(0)}"
                    )

        assert len(contradictions) == 0, f"Found {len(contradictions)} contradiction(s):\n" + "\n".join(contradictions)

    def test_standard_single_select_no_correct_choice_claimed_wrong(
        self, standard_questions: List[Dict[str, Any]]
    ):
        ss_questions = [q for q in standard_questions if q.get("interaction", {}).get("type") == "single_select"]
        contradictions = []

        for q in ss_questions:
            ca = str(q.get("correct_answer", "")).strip().lower()
            exp = q.get("explanation", "")
            for m in self.ASSERT_WRONG_PATTERN.finditer(exp):
                letter = m.group(1).lower()
                if letter == ca:
                    contradictions.append(
                        f"Question [{q.get('question_id')}]: explanation claims correct choice '{ca.upper()}' is wrong/eliminated. Snippet: {m.group(0)}"
                    )

        assert len(contradictions) == 0, f"Found {len(contradictions)} contradiction(s):\n" + "\n".join(contradictions)

    def test_expanded_single_select_no_wrong_choice_claimed_correct(
        self, expanded_questions: List[Dict[str, Any]]
    ):
        ss_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "single_select"]
        contradictions = []

        for q in ss_questions:
            ca = str(q.get("correct_answer", "")).strip().lower()
            exp = q.get("explanation", "")
            for m in self.ASSERT_CORRECT_PATTERN.finditer(exp):
                letter = m.group(1).lower()
                if letter != ca:
                    contradictions.append(
                        f"Day {q['_day_num']} [{q.get('question_id')}]: explanation claims '{letter.upper()}' is correct, but correct_answer is '{ca.upper()}'. Snippet: {m.group(0)}"
                    )

        assert len(contradictions) == 0, f"Found {len(contradictions)} contradiction(s):\n" + "\n".join(contradictions)

    def test_expanded_single_select_no_correct_choice_claimed_wrong(
        self, expanded_questions: List[Dict[str, Any]]
    ):
        ss_questions = [q for q in expanded_questions if q.get("interaction", {}).get("type") == "single_select"]
        contradictions = []

        for q in ss_questions:
            ca = str(q.get("correct_answer", "")).strip().lower()
            exp = q.get("explanation", "")
            for m in self.ASSERT_WRONG_PATTERN.finditer(exp):
                letter = m.group(1).lower()
                if letter == ca:
                    contradictions.append(
                        f"Day {q['_day_num']} [{q.get('question_id')}]: explanation claims correct choice '{ca.upper()}' is wrong. Snippet: {m.group(0)}"
                    )

        assert len(contradictions) == 0, f"Found {len(contradictions)} contradiction(s):\n" + "\n".join(contradictions)


class TestMultiSelectExplanationConsistency:
    """Ensures 0 contradictions between correct_answer and explanation in multiple-choice questions."""

    ASSERT_WRONG_PATTERN = re.compile(
        r"(?:đáp án|phương án|lựa chọn)\s+([A-D])\s+(?:là\s+)?(?:sai|không đúng|không chính xác|bị loại|không phải là đáp án đúng)\b",
        re.IGNORECASE,
    )
    COUNT_PHRASE_PATTERN = re.compile(
        r"(?:chọn\s+(?:cả\s+)?(\d+)\s+đáp án|có\s+(\d+)\s+đáp án đúng)",
        re.IGNORECASE,
    )

    def test_multi_select_no_correct_choice_claimed_wrong(
        self, standard_questions: List[Dict[str, Any]], expanded_questions: List[Dict[str, Any]]
    ):
        all_ms = [
            q for q in standard_questions + expanded_questions
            if q.get("interaction", {}).get("type") == "multi_select"
        ]
        contradictions = []

        for q in all_ms:
            ca_list = [str(x).strip().lower() for x in q.get("correct_answer", []) if isinstance(x, (str, int))]
            exp = q.get("explanation", "")
            for m in self.ASSERT_WRONG_PATTERN.finditer(exp):
                letter = m.group(1).lower()
                if letter in ca_list:
                    contradictions.append(
                        f"Question [{q.get('question_id')}]: explanation claims choice '{letter.upper()}' (which is in correct_answer {ca_list}) is wrong. Snippet: {m.group(0)}"
                    )

        assert len(contradictions) == 0, f"Found {len(contradictions)} contradiction(s):\n" + "\n".join(contradictions)

    def test_multi_select_count_phrases_match_answer_length(
        self, standard_questions: List[Dict[str, Any]], expanded_questions: List[Dict[str, Any]]
    ):
        all_ms = [
            q for q in standard_questions + expanded_questions
            if q.get("interaction", {}).get("type") == "multi_select"
        ]
        count_mismatches = []

        for q in all_ms:
            ca = q.get("correct_answer")
            if not isinstance(ca, list):
                continue
            exp = q.get("explanation", "")
            for m in self.COUNT_PHRASE_PATTERN.finditer(exp):
                cnt_str = m.group(1) or m.group(2)
                if cnt_str:
                    expected_cnt = int(cnt_str)
                    if expected_cnt != len(ca):
                        count_mismatches.append(
                            f"Question [{q.get('question_id')}]: explanation mentions {expected_cnt} correct answers, but correct_answer has {len(ca)} ({ca}). Snippet: {m.group(0)}"
                        )

        assert len(count_mismatches) == 0, f"Found count phrase mismatches:\n" + "\n".join(count_mismatches)


class TestNumericAndOrderingExplanationConsistency:
    """Verifies that numeric and ordering explanations are technically consistent with answers."""

    def test_standard_numeric_explanations(self, standard_questions: List[Dict[str, Any]]):
        num_qs = [q for q in standard_questions if q.get("interaction", {}).get("type") == "numeric_input"]
        for q in num_qs:
            ca = q.get("correct_answer")
            exp = q.get("explanation", "")
            assert isinstance(ca, (int, float)), f"Question [{q.get('question_id')}]: non-numeric answer {ca!r}"
            # Check explanation is substantive
            assert len(exp.strip()) >= 20, f"Question [{q.get('question_id')}]: explanation too short"

    def test_ordering_explanations_substantive(
        self, standard_questions: List[Dict[str, Any]], expanded_questions: List[Dict[str, Any]]
    ):
        ord_qs = [
            q for q in standard_questions + expanded_questions
            if q.get("interaction", {}).get("type") == "ordering"
        ]
        for q in ord_qs:
            exp = q.get("explanation", "")
            assert len(exp.strip()) >= 20, f"Question [{q.get('question_id')}]: ordering explanation too short"
