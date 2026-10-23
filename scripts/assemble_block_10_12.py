# scripts/assemble_block_10_12.py
# -*- coding: utf-8 -*-
"""
Assembler script for data/essay_block_10_12.json
Combines Day 10 (48 questions), Day 11 (57 questions), and Day 12 (73 questions)
Total: 178 essay questions
"""

import json
import sys
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tests.test_essay_answers import (
    load_master_metadata,
    validate_essay_entry,
    validate_chunk_file,
    BLOCK_METADATA,
)

from scripts.author_day10 import DAY10_DATA
from scripts.author_day11 import DAY11_DATA
from scripts.author_day12 import DAY12_DATA

def main():
    print("=== Assembling Essay Block 10-12 ===")
    print(f"Day 10 questions count: {len(DAY10_DATA)}")
    print(f"Day 11 questions count: {len(DAY11_DATA)}")
    print(f"Day 12 questions count: {len(DAY12_DATA)}")

    combined_data = {}
    combined_data.update(DAY10_DATA)
    combined_data.update(DAY11_DATA)
    combined_data.update(DAY12_DATA)

    total_count = len(combined_data)
    print(f"Total combined questions: {total_count}")
    if total_count != 178:
        print(f"ERROR: Expected 178 questions, got {total_count}")
        sys.exit(1)

    master_metadata = load_master_metadata(PROJECT_ROOT)
    expected_qids = [
        qid for qid, info in master_metadata.items() if info["day_num"] in [10, 11, 12]
    ]
    print(f"Expected QIDs from master metadata (Days 10-12): {len(expected_qids)}")

    missing_qids = [qid for qid in expected_qids if qid not in combined_data]
    if missing_qids:
        print(f"ERROR: Missing QIDs ({len(missing_qids)}): {missing_qids}")
        sys.exit(1)

    extra_qids = [qid for qid in combined_data if qid not in expected_qids]
    if extra_qids:
        print(f"ERROR: Extra QIDs ({len(extra_qids)}): {extra_qids}")
        sys.exit(1)

    # Validate each entry
    validation_errors = {}
    for qid in expected_qids:
        qdata = combined_data[qid]
        qmeta = master_metadata.get(qid, {})
        pts = qmeta.get("points")
        hints = qmeta.get("hints", [])
        errs = validate_essay_entry(qid, qdata, expected_points=pts, hints=hints)
        if errs:
            validation_errors[qid] = errs

    if validation_errors:
        print(f"ERROR: Found validation errors in {len(validation_errors)} questions:")
        for qid, errs in validation_errors.items():
            print(f"  [{qid}]:")
            for err in errs:
                print(f"    - {err}")
        sys.exit(1)

    print("Pre-validation passed with 0 errors!")

    # Format dictionary in order of expected_qids
    ordered_block = {}
    for qid in expected_qids:
        raw_entry = combined_data[qid]
        ordered_block[qid] = {
            "sample_answer": raw_entry["sample_answer"].strip(),
            "explanation": raw_entry["explanation"].strip(),
            "rubric": raw_entry["rubric"].strip(),
            "reference_source": raw_entry["reference_source"].strip(),
        }

    output_path = PROJECT_ROOT / "data" / "essay_block_10_12.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ordered_block, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {len(ordered_block)} questions to: {output_path}")

    # Run formal chunk validation
    report = validate_chunk_file(output_path, master_metadata)
    print("\n--- Diagnostic Report from validate_chunk_file ---")
    print(f"Chunk: {report['chunk']}")
    print(f"Status: {report['status']}")
    print(f"Total items: {report['total_items']} (Expected: {report['expected_items']})")
    print(f"Valid items: {report['valid_items']}")
    print(f"Missing items: {len(report['missing_items'])}")
    print(f"Item errors: {len(report['item_errors'])}")

    if report["status"] != "CLEAN":
        print("ERROR: Chunk validation status is NOT CLEAN!")
        sys.exit(1)

    print("\nALL 178 QUESTIONS ARE CLEAN, VALID, AND COMPLETE!")

if __name__ == "__main__":
    main()
