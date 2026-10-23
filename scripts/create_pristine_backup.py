#!/usr/bin/env python3
"""
scripts/create_pristine_backup.py

Milestone M1: Pristine Backup for VLearn Quiz Audit & Cross-File Synchronization.
Creates a dedicated pristine backup directory at `backup_original_files/` containing
exact, unmodified copies of all original JSON, TXT, XLSX, and ZIP files prior to edits.
Generates `backup_manifest.json` recording relative source path, backup path,
file size in bytes, and SHA256 hashes, then verifies 100% bit-for-bit integrity.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def compute_sha256(file_path: Path) -> str:
    """Computes SHA-256 hash of a file using chunked binary reading."""
    hasher = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def collect_target_files(workspace_root: Path) -> list[tuple[str, Path]]:
    """
    Collects all target files categorized as specified in Milestone M1 dispatch:
    1. JSON (5 files)
    2. TXT (45 in vlearn-app/public/quiz_txt/ + 15 in downloads/Khoa_4_Phase_1/*/QUIZ_CHI_TIET_DAP_AN.txt)
    3. XLSX (3 standalone files + TONG_HOP_QUIZ_15_NGAY_EXCEL tree + vlearn-app/public/quiz_excel tree)
    4. ZIP (2 standalone files)
    Returns list of (category, resolved_path).
    """
    targets: list[tuple[str, Path]] = []

    # 1. JSON
    json_rel_paths = [
        "vlearn-app/src/multiphase_course_data.json",
        "vlearn-app/src/course_data.json",
        "vlearn-app/src/quiz_data.json",
        "verified_all_quizzes_master.json",
        "downloads/Khoa_4_Phase_1/TAT_CA_QUIZ_KHOA_HOC.json",
    ]
    for rel in json_rel_paths:
        p = (workspace_root / rel).resolve()
        if not p.is_file():
            raise FileNotFoundError(f"Required JSON file not found: {rel}")
        targets.append(("json", p))

    # 2. TXT
    txt_dir = (workspace_root / "vlearn-app/public/quiz_txt").resolve()
    if not txt_dir.is_dir():
        raise FileNotFoundError(f"Missing directory: {txt_dir}")
    txt_app_files = sorted(txt_dir.glob("*.txt"))
    if len(txt_app_files) != 45:
        raise ValueError(f"Expected 45 txt files in {txt_dir}, found {len(txt_app_files)}")
    for p in txt_app_files:
        targets.append(("txt", p.resolve()))

    dl_dir = (workspace_root / "downloads/Khoa_4_Phase_1").resolve()
    if not dl_dir.is_dir():
        raise FileNotFoundError(f"Missing directory: {dl_dir}")
    txt_dl_files = sorted(dl_dir.glob("*/QUIZ_CHI_TIET_DAP_AN.txt"))
    if len(txt_dl_files) != 15:
        raise ValueError(f"Expected 15 txt files in downloads/Khoa_4_Phase_1, found {len(txt_dl_files)}")
    for p in txt_dl_files:
        targets.append(("txt", p.resolve()))

    # 3. XLSX
    xlsx_rel_paths = [
        "VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx",
        "VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES_VERIFIED.xlsx",
        "vlearn-app/public/VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx",
    ]
    for rel in xlsx_rel_paths:
        p = (workspace_root / rel).resolve()
        if not p.is_file():
            raise FileNotFoundError(f"Required XLSX file not found: {rel}")
        targets.append(("xlsx", p))

    # TONG_HOP_QUIZ_15_NGAY_EXCEL/ (entire tree)
    th_dir = (workspace_root / "TONG_HOP_QUIZ_15_NGAY_EXCEL").resolve()
    if not th_dir.is_dir():
        raise FileNotFoundError(f"Missing directory: {th_dir}")
    for p in sorted(th_dir.rglob("*")):
        if p.is_file():
            targets.append(("xlsx", p.resolve()))

    # vlearn-app/public/quiz_excel/ (entire tree)
    qe_dir = (workspace_root / "vlearn-app/public/quiz_excel").resolve()
    if not qe_dir.is_dir():
        raise FileNotFoundError(f"Missing directory: {qe_dir}")
    for p in sorted(qe_dir.rglob("*")):
        if p.is_file():
            targets.append(("xlsx", p.resolve()))

    # 4. ZIP
    zip_rel_paths = [
        "TONG_HOP_QUIZ_15_NGAY_EXCEL.zip",
        "vlearn-app/public/TONG_HOP_QUIZ_15_NGAY_EXCEL.zip",
    ]
    for rel in zip_rel_paths:
        p = (workspace_root / rel).resolve()
        if not p.is_file():
            raise FileNotFoundError(f"Required ZIP file not found: {rel}")
        targets.append(("zip", p))

    return targets


def run_backup(workspace_root: Path, backup_root: Path) -> dict:
    """Executes the file copy and computes hashes."""
    backup_root.mkdir(parents=True, exist_ok=True)
    raw_targets = collect_target_files(workspace_root)

    # Ensure uniqueness
    seen: set[Path] = set()
    unique_targets: list[tuple[str, Path]] = []
    for cat, p in raw_targets:
        if p not in seen:
            seen.add(p)
            unique_targets.append((cat, p))

    print(f"Total files to backup: {len(unique_targets)}")

    manifest_entries = []
    category_counts: dict[str, int] = {}
    category_bytes: dict[str, int] = {}
    total_bytes = 0

    for idx, (cat, src_file) in enumerate(unique_targets, start=1):
        rel_path = src_file.relative_to(workspace_root).as_posix()
        dest_file = backup_root / rel_path
        dest_file.parent.mkdir(parents=True, exist_ok=True)

        # 1. Source stats & hash
        src_size = src_file.stat().st_size
        src_sha256 = compute_sha256(src_file)

        # 2. Copy file (preserving metadata)
        shutil.copy2(src_file, dest_file)

        # 3. Destination stats & hash
        dest_size = dest_file.stat().st_size
        dest_sha256 = compute_sha256(dest_file)

        # 4. Verify match immediately
        if src_size != dest_size:
            raise ValueError(
                f"Size mismatch for {rel_path}: src={src_size} != dest={dest_size}"
            )
        if src_sha256 != dest_sha256:
            raise ValueError(
                f"Hash mismatch for {rel_path}: src={src_sha256} != dest={dest_sha256}"
            )

        manifest_entries.append({
            "category": cat,
            "source_relative_path": rel_path,
            "backup_relative_path": dest_file.relative_to(backup_root).as_posix(),
            "backup_path": str(dest_file.resolve()),
            "size_bytes": src_size,
            "sha256": src_sha256,
            "verified_bit_for_bit": True,
        })

        category_counts[cat] = category_counts.get(cat, 0) + 1
        category_bytes[cat] = category_bytes.get(cat, 0) + src_size
        total_bytes += src_size

        if idx % 50 == 0 or idx == len(unique_targets):
            print(f"  [{idx}/{len(unique_targets)}] Copied and verified: {rel_path}")

    manifest_data = {
        "metadata": {
            "title": "VLearn Pristine Backup Manifest",
            "created_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "workspace_root": str(workspace_root.resolve()),
            "backup_root": str(backup_root.resolve()),
            "total_files": len(manifest_entries),
            "total_bytes": total_bytes,
            "integrity_verified_100_percent": True,
        },
        "by_category": {
            cat: {
                "file_count": category_counts.get(cat, 0),
                "total_bytes": category_bytes.get(cat, 0),
            }
            for cat in ["json", "txt", "xlsx", "zip"]
        },
        "files": manifest_entries,
    }

    manifest_path = backup_root / "backup_manifest.json"
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)

    print(f"\nManifest successfully written to: {manifest_path}")
    print(f"Total files: {len(manifest_entries)}")
    print(f"Total size: {total_bytes} bytes ({total_bytes / (1024 * 1024):.2f} MB)")
    for cat in ["json", "txt", "xlsx", "zip"]:
        c = category_counts.get(cat, 0)
        b = category_bytes.get(cat, 0)
        print(f"  - {cat.upper()}: {c} files ({b / (1024*1024):.2f} MB)")

    # Establish .backup junction if feasible
    dot_backup = workspace_root / ".backup"
    if not dot_backup.exists():
        try:
            print(f"\nCreating directory junction from {dot_backup} -> {backup_root}...")
            subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(dot_backup), str(backup_root)],
                check=True,
                capture_output=True,
                text=True,
            )
            print("Successfully linked .backup -> backup_original_files")
        except (subprocess.CalledProcessError, OSError) as e:
            print(f"Note: Could not create junction {dot_backup}: {e}")

    return manifest_data


def main():
    root = Path(__file__).resolve().parent.parent
    backup_dir = root / "backup_original_files"
    print(f"Starting pristine backup from {root} to {backup_dir}...")
    run_backup(root, backup_dir)
    print("\nPristine backup complete and 100% verified!")


if __name__ == "__main__":
    main()
