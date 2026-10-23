"""
tests/conftest.py

Shared pytest fixtures for the VLearn Quiz Audit verification test suite.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def project_root() -> Path:
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def multiphase_data_path(project_root: Path) -> Path:
    return project_root / "vlearn-app" / "src" / "multiphase_course_data.json"


@pytest.fixture(scope="session")
def multiphase_data(multiphase_data_path: Path) -> Dict[str, Any]:
    assert multiphase_data_path.exists(), f"Missing file: {multiphase_data_path}"
    with open(multiphase_data_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def phase1_days(multiphase_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    phases = multiphase_data.get("phases", [])
    assert len(phases) > 0, "No phases found in multiphase_course_data.json"
    phase1 = phases[0]
    days = phase1.get("days", [])
    assert len(days) >= 15, f"Phase 1 has only {len(days)} days, expected at least 15"
    return days[:15]


@pytest.fixture(scope="session")
def standard_questions(phase1_days: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    qs = []
    for day_idx, day in enumerate(phase1_days):
        day_num = day_idx + 1
        day_id = day.get("day_id")
        for q in day.get("questions", []):
            item = dict(q)
            item["_day_num"] = day_num
            item["_day_id"] = day_id
            qs.append(item)
    return qs


@pytest.fixture(scope="session")
def expanded_questions(phase1_days: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    qs = []
    for day_idx, day in enumerate(phase1_days):
        day_num = day_idx + 1
        day_id = day.get("day_id")
        for q in day.get("expanded_questions", []):
            item = dict(q)
            item["_day_num"] = day_num
            item["_day_id"] = day_id
            qs.append(item)
    return qs


@pytest.fixture(scope="session")
def master_json_data(project_root: Path) -> Dict[str, Any]:
    p = project_root / "verified_all_quizzes_master.json"
    assert p.exists(), f"Missing master file: {p}"
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def course_data_json(project_root: Path) -> List[Dict[str, Any]]:
    p = project_root / "vlearn-app" / "src" / "course_data.json"
    assert p.exists(), f"Missing file: {p}"
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def quiz_data_json(project_root: Path) -> Dict[str, Any]:
    p = project_root / "vlearn-app" / "src" / "quiz_data.json"
    assert p.exists(), f"Missing file: {p}"
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)
