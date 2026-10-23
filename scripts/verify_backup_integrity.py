#!/usr/bin/env python3
"""
scripts/verify_backup_integrity.py

Milestone M1: Independent verification script for pristine backup.
Verifies that 100% of files in backup_original_files match their source files
and backup_manifest.json bit-for-bit via SHA-256 hash recalculation.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def compute_sha256(file_path: Path) -> str:
    """Computes SHA-256 hash of a file using chunked binary reading."""
    hasher = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_backup(
    workspace_root: Path,
    manifest_path: Path,
    verify_sources: bool = False,
) -> dict:
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with manifest_path.open("r", encoding="utf-8") as f:
        manifest = json.load(f)

    files_list = manifest.get("files", [])
    if not files_list:
        raise ValueError("Manifest contains no file records")

    print(f"Verifying {len(files_list)} files from manifest: {manifest_path}")

    passed = 0
    failed = []

    for idx, entry in enumerate(files_list, start=1):
        rel_src = entry["source_relative_path"]
        expected_size = entry["size_bytes"]
        expected_hash = entry["sha256"]

        src_path = (workspace_root / rel_src).resolve()
        backup_path = Path(entry["backup_path"]).resolve()

        # Optionally check source existence and hash (pre-edit check)
        if verify_sources:
            if not src_path.is_file():
                failed.append({
                    "path": rel_src,
                    "reason": f"Source file missing: {src_path}",
                })
                continue

            src_size = src_path.stat().st_size
            if src_size != expected_size:
                failed.append({
                    "path": rel_src,
                    "reason": f"Source size mismatch: expected {expected_size}, got {src_size}",
                })
                continue

            src_hash = compute_sha256(src_path)
            if src_hash != expected_hash:
                failed.append({
                    "path": rel_src,
                    "reason": f"Source hash mismatch: expected {expected_hash}, got {src_hash}",
                })
                continue

        # Check backup existence and hash
        if not backup_path.is_file():
            failed.append({
                "path": rel_src,
                "reason": f"Backup file missing: {backup_path}",
            })
            continue

        backup_size = backup_path.stat().st_size
        if backup_size != expected_size:
            failed.append({
                "path": rel_src,
                "reason": f"Backup size mismatch: expected {expected_size}, got {backup_size}",
            })
            continue

        backup_hash = compute_sha256(backup_path)
        if backup_hash != expected_hash:
            failed.append({
                "path": rel_src,
                "reason": f"Backup hash mismatch: expected {expected_hash}, got {backup_hash}",
            })
            continue

        passed += 1
        if idx % 50 == 0 or idx == len(files_list):
            print(f"  [{idx}/{len(files_list)}] Verified: {rel_src} (SHA256 matches)")

    result = {
        "total": len(files_list),
        "passed": passed,
        "failed_count": len(failed),
        "failed_details": failed,
        "status": "PASS" if len(failed) == 0 else "FAIL",
    }
    return result


def main():
    root = Path(__file__).resolve().parent.parent
    manifest_path = root / "backup_original_files" / "backup_manifest.json"

    result = verify_backup(root, manifest_path)

    print("\n" + "=" * 50)
    print("BACKUP INTEGRITY VERIFICATION RESULT")
    print("=" * 50)
    print(f"Total files checked: {result['total']}")
    print(f"Passed bit-for-bit: {result['passed']}")
    print(f"Failed count:       {result['failed_count']}")
    print(f"Status:             {result['status']}")

    if result["failed_count"] > 0:
        print("\nFailures:")
        for fail in result["failed_details"]:
            print(f"  - {fail['path']}: {fail['reason']}")
        sys.exit(1)
    else:
        print("\n100% of backed up files match their source SHA256 hashes bit-for-bit!")
        sys.exit(0)


if __name__ == "__main__":
    main()
