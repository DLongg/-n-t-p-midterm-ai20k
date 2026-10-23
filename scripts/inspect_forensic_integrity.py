#!/usr/bin/env python3
"""
scripts/inspect_forensic_integrity.py

Forensic inspection script to verify:
1. Exact diff of modified questions in multiphase_course_data.json vs backup.
2. Authenticity of the 63 numeric calculations.
3. Authenticity of the 48 matching repairs.
4. Absence of dummy/mock/facade strings in answers and explanations.
5. Exact consistency with audit_changelog.json.
"""

import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent

def main():
    bak_path = ROOT / "backup_original_files" / "vlearn-app" / "src" / "multiphase_course_data.json"
    cur_path = ROOT / "vlearn-app" / "src" / "multiphase_course_data.json"
    changelog_path = ROOT / "audit_changelog.json"

    with open(bak_path, "r", encoding="utf-8") as f:
        bak_data = json.load(f)
    with open(cur_path, "r", encoding="utf-8") as f:
        cur_data = json.load(f)
    with open(changelog_path, "r", encoding="utf-8") as f:
        changelog = json.load(f)

    bak_std = {q["question_id"]: q for d in bak_data["phases"][0]["days"][:15] for q in d.get("questions", [])}
    bak_exp = {q["question_id"]: q for d in bak_data["phases"][0]["days"][:15] for q in d.get("expanded_questions", [])}
    cur_std = {q["question_id"]: q for d in cur_data["phases"][0]["days"][:15] for q in d.get("questions", [])}
    cur_exp = {q["question_id"]: q for d in cur_data["phases"][0]["days"][:15] for q in d.get("expanded_questions", [])}

    print(f"Loaded: {len(bak_std)} standard, {len(bak_exp)} expanded from backup.")
    print(f"Loaded: {len(cur_std)} standard, {len(cur_exp)} expanded from current.")

    # 1. Modifications in standard
    mod_std = []
    for qid, bq in bak_std.items():
        cq = cur_std[qid]
        a_diff = (bq.get("correct_answer") != cq.get("correct_answer"))
        e_diff = (bq.get("explanation") != cq.get("explanation"))
        if a_diff or e_diff:
            mod_std.append((qid, a_diff, e_diff, bq.get("correct_answer"), cq.get("correct_answer"), cq.get("explanation")))

    print(f"\n--- STANDARD MODIFICATIONS: {len(mod_std)} ---")
    for qid, ad, ed, old_a, new_a, exp in mod_std:
        print(f"  [{qid}] ans_diff={ad}, exp_diff={ed}: old={old_a!r} -> new={new_a!r}")

    # 2. Modifications in expanded
    mod_exp = []
    for qid, bq in bak_exp.items():
        cq = cur_exp[qid]
        a_diff = (bq.get("correct_answer") != cq.get("correct_answer"))
        e_diff = (bq.get("explanation") != cq.get("explanation"))
        if a_diff or e_diff:
            itype = bq.get("interaction", {}).get("type")
            mod_exp.append((qid, itype, a_diff, e_diff, bq.get("correct_answer"), cq.get("correct_answer"), cq.get("explanation")))

    print(f"\n--- EXPANDED MODIFICATIONS: {len(mod_exp)} ---")
    type_counts = Counter(item[1] for item in mod_exp)
    for itype, count in sorted(type_counts.items()):
        print(f"  Interaction '{itype}': {count} modified")

    # 3. Numeric Calculations Authenticity Check
    print(f"\n--- 63 NUMERIC CALCULATIONS AUTHENTICITY ---")
    numeric_mods = [item for item in mod_exp if item[1] == "numeric_input"]
    print(f"Total numeric modifications: {len(numeric_mods)}")
    dummy_numerics = []
    real_numerics = []
    for qid, itype, ad, ed, old_a, new_a, exp in numeric_mods:
        # Check if new answer is numeric int or float
        if not isinstance(new_a, (int, float)):
            dummy_numerics.append((qid, "Not int or float", new_a))
        elif new_a == 0:
            dummy_numerics.append((qid, "Zero numeric", new_a))
        else:
            real_numerics.append((qid, old_a, new_a, exp[:60] + "..."))

    print(f"Real computed numbers: {len(real_numerics)}")
    print(f"Suspicious/dummy numerics: {len(dummy_numerics)}")
    print("Sample 5 numeric calculations:")
    for qid, old_a, new_a, exp_snippet in real_numerics[:5]:
        print(f"  [{qid}] old={old_a!r} -> new={new_a!r} | Expl: {exp_snippet}")

    # 4. Matching Repairs Authenticity Check
    print(f"\n--- 48 MATCHING REPAIRS AUTHENTICITY ---")
    matching_mods = [item for item in mod_exp if item[1] == "matching"]
    print(f"Total matching modifications: {len(matching_mods)}")
    empty_matchings = [item for item in matching_mods if not item[5] or len(item[5]) == 0]
    print(f"Empty/unrepaired matchings: {len(empty_matchings)}")
    print("Sample 3 matching repairs:")
    for qid, itype, ad, ed, old_a, new_a, exp in matching_mods[:3]:
        print(f"  [{qid}] old={old_a!r} -> new={new_a!r}")

    # 5. Facade / Mock Strings Scan
    print(f"\n--- FACADE & MOCK STRINGS SCAN ---")
    suspicious_keywords = ["TODO", "FIXME", "DUMMY", "MOCK", "PLACEHOLDER", "HARDBALL", "FACADE", "TEST_REPLACE"]
    flagged_strings = []
    for qid, cq in cur_exp.items():
        exp = cq.get("explanation", "")
        ca = str(cq.get("correct_answer", ""))
        for kw in suspicious_keywords:
            if kw in exp.upper():
                flagged_strings.append((qid, "explanation", kw, exp))
            if kw in ca.upper():
                flagged_strings.append((qid, "correct_answer", kw, ca))

    for qid, cq in cur_std.items():
        exp = cq.get("explanation", "")
        ca = str(cq.get("correct_answer", ""))
        for kw in suspicious_keywords:
            if kw in exp.upper():
                flagged_strings.append((qid, "std explanation", kw, exp))
            if kw in ca.upper():
                flagged_strings.append((qid, "std correct_answer", kw, ca))

    print(f"Suspicious placeholder/mock keywords found: {len(flagged_strings)}")
    for item in flagged_strings:
        print(f"  FLAGGED: {item}")

    # 6. Cross-reference with audit_changelog.json
    print(f"\n--- AUDIT CHANGELOG PARITY ---")
    cl_mods = changelog.get("modified_questions", [])
    print(f"audit_changelog.json modified count: {len(cl_mods)}")
    cl_qids = {item["question_id"] for item in cl_mods}
    exp_mod_qids = {item[0] for item in mod_exp}
    std_mod_qids = {item[0] for item in mod_std}

    print(f"Expanded modifications set == changelog modified set: {exp_mod_qids == cl_qids}")
    diff1 = exp_mod_qids - cl_qids
    diff2 = cl_qids - exp_mod_qids
    if diff1:
        print(f"In expanded mods but not in changelog: {diff1}")
    if diff2:
        print(f"In changelog but not in expanded mods: {diff2}")

if __name__ == "__main__":
    main()
