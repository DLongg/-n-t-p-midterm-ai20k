import sys, os
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tests.test_essay_answers import validate_essay_entry, load_master_metadata
import scripts.day12_part1 as d12p1

master_meta = load_master_metadata(Path("."))

issues = []
for qid, qdata in d12p1.DAY12_PART1.items():
    meta = master_meta.get(qid, {})
    exp_pts = meta.get("points")
    hints = meta.get("hints", [])
    errs = validate_essay_entry(qid, qdata, expected_points=exp_pts, hints=hints)
    if errs:
        for err in errs:
            issues.append(f"[{qid}] {err}")

if issues:
    print(f"FAILED with {len(issues)} issues:")
    for iss in issues:
        print(" -", iss)
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(d12p1.DAY12_PART1)} questions in Day 12 Part 1 are 100% VALID!")
