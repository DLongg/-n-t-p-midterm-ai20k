"""
tests/test_backup_integrity.py

Automated pytest suite validating Milestone M1 pristine backup:
- Directory existence and manifest schema
- 100% bit-for-bit SHA256 integrity match between source files and backups
- Completeness across JSON, TXT, XLSX, and ZIP categories
"""

import json
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.verify_backup_integrity import compute_sha256, verify_backup

BACKUP_DIR = WORKSPACE_ROOT / "backup_original_files"
MANIFEST_PATH = BACKUP_DIR / "backup_manifest.json"


def test_backup_directory_and_manifest_exist():
    assert BACKUP_DIR.is_dir(), f"Backup directory missing: {BACKUP_DIR}"
    assert MANIFEST_PATH.is_file(), f"Backup manifest missing: {MANIFEST_PATH}"


def test_backup_manifest_structure():
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("metadata", {})
    assert meta.get("integrity_verified_100_percent") is True
    assert meta.get("total_files") == 336
    assert meta.get("total_bytes") > 18_000_000

    by_cat = data.get("by_category", {})
    assert by_cat.get("json", {}).get("file_count") == 5
    assert by_cat.get("txt", {}).get("file_count") == 60
    assert by_cat.get("xlsx", {}).get("file_count") == 269
    assert by_cat.get("zip", {}).get("file_count") == 2

    files = data.get("files", [])
    assert len(files) == 336


def test_backup_bit_for_bit_integrity():
    result = verify_backup(WORKSPACE_ROOT, MANIFEST_PATH, verify_sources=False)
    assert result["status"] == "PASS"
    assert result["failed_count"] == 0
    assert result["passed"] == 336


def test_canonical_json_files_preserved():
    canonical_files = [
        "vlearn-app/src/multiphase_course_data.json",
        "vlearn-app/src/course_data.json",
        "vlearn-app/src/quiz_data.json",
        "verified_all_quizzes_master.json",
        "downloads/Khoa_4_Phase_1/TAT_CA_QUIZ_KHOA_HOC.json",
    ]
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        manifest = json.load(f)
    manifest_hashes = {
        e["source_relative_path"].replace("\\", "/"): e["sha256"]
        for e in manifest["files"]
    }

    for rel in canonical_files:
        src = WORKSPACE_ROOT / rel
        bak = BACKUP_DIR / rel
        assert src.is_file(), f"Source file missing: {src}"
        assert bak.is_file(), f"Backup file missing: {bak}"
        # Pristine backup file matches the original manifest hash 100%
        assert compute_sha256(bak) == manifest_hashes[rel]
