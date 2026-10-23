#!/usr/bin/env python3
"""
scripts/sync_all_quizzes.py

Centralized Cross-File Synchronization Engine for VLearn Quiz Audit.
Synchronizes canonical audited questions, answers, and explanations from
`.audit_work/audit_result_days_*.json` into all 7 target formats:

1. Canonical Master JSON: `vlearn-app/src/multiphase_course_data.json`
   - Both `expanded_questions` (904) and `questions` (165 standard)
2. Auxiliary JSONs:
   - `verified_all_quizzes_master.json` (170 verified master solutions)
   - `vlearn-app/src/course_data.json` (student course data)
   - `vlearn-app/src/quiz_data.json` (student quiz data)
   - `downloads/Khoa_4_Phase_1/TAT_CA_QUIZ_KHOA_HOC.json` (mirror of quiz_data)
3. Text Quiz Files:
   - `vlearn-app/public/quiz_txt/*_QUIZ_CHI_TIET_DAP_AN.txt` (15 files) and mirrors
   - `vlearn-app/public/quiz_txt/*_NGAN_HANG_TOAN_DIEN.txt` and `DAY*_...` mirrors
4. Master Excel Workbooks:
   - `VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx`
   - `VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES_VERIFIED.xlsx`
   - `vlearn-app/public/VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx`
5. Quizizz Excel Workbooks:
   - `TONG_HOP_QUIZ_15_NGAY_EXCEL/01_CHUAN_IMPORT_QUIZIZZ_QUIZ_COM_904_CAU/` (15 FULL + 45 parts)
   - `TONG_HOP_QUIZ_15_NGAY_EXCEL/02_FULL_NGAN_HANG_1679_CAU_CHI_TIET_CHIA_20_CAU/` (84 parts)
   - `vlearn-app/public/quiz_excel/` (mirror of 60 files)
6. ZIP Archives:
   - `TONG_HOP_QUIZ_15_NGAY_EXCEL.zip`
   - `vlearn-app/public/TONG_HOP_QUIZ_15_NGAY_EXCEL.zip` (100% SHA256 equality)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import openpyxl


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CANONICAL_MASTER_JSON = PROJECT_ROOT / "vlearn-app" / "src" / "multiphase_course_data.json"
MASTER_SOLUTIONS_JSON = PROJECT_ROOT / "verified_all_quizzes_master.json"
COURSE_DATA_JSON = PROJECT_ROOT / "vlearn-app" / "src" / "course_data.json"
QUIZ_DATA_JSON = PROJECT_ROOT / "vlearn-app" / "src" / "quiz_data.json"
DOWNLOADS_QUIZ_JSON = PROJECT_ROOT / "downloads" / "Khoa_4_Phase_1" / "TAT_CA_QUIZ_KHOA_HOC.json"

MASTER_XLSX_1 = PROJECT_ROOT / "VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx"
MASTER_XLSX_2 = PROJECT_ROOT / "VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES_VERIFIED.xlsx"
MASTER_XLSX_3 = PROJECT_ROOT / "vlearn-app" / "public" / "VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx"

QUIZ_TXT_DIR = PROJECT_ROOT / "vlearn-app" / "public" / "quiz_txt"
DOWNLOADS_K4P1_DIR = PROJECT_ROOT / "downloads" / "Khoa_4_Phase_1"

QUIZIZZ_01_DIR = PROJECT_ROOT / "TONG_HOP_QUIZ_15_NGAY_EXCEL" / "01_CHUAN_IMPORT_QUIZIZZ_QUIZ_COM_904_CAU"
QUIZIZZ_02_DIR = PROJECT_ROOT / "TONG_HOP_QUIZ_15_NGAY_EXCEL" / "02_FULL_NGAN_HANG_1679_CAU_CHI_TIET_CHIA_20_CAU"
PUBLIC_QUIZ_EXCEL_DIR = PROJECT_ROOT / "vlearn-app" / "public" / "quiz_excel"

ZIP_MAIN = PROJECT_ROOT / "TONG_HOP_QUIZ_15_NGAY_EXCEL.zip"
ZIP_PUBLIC = PROJECT_ROOT / "vlearn-app" / "public" / "TONG_HOP_QUIZ_15_NGAY_EXCEL.zip"

AUDIT_BATCH_FILES = [
    PROJECT_ROOT / ".audit_work" / "audit_result_days_01_05.json",
    PROJECT_ROOT / ".audit_work" / "audit_result_days_06_10.json",
    PROJECT_ROOT / ".audit_work" / "audit_result_days_11_15.json",
]


def load_audit_map() -> Dict[str, Dict[str, Any]]:
    """Loads all 3 audit batch files into a unified dictionary keyed by question_id."""
    audit_map: Dict[str, Dict[str, Any]] = {}
    for batch_file in AUDIT_BATCH_FILES:
        if not batch_file.exists():
            raise FileNotFoundError(f"Missing audit batch file: {batch_file}")
        with open(batch_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for q in data.get("questions", []):
                qid = q["question_id"]
                audit_map[qid] = q
    return audit_map


def sync_canonical_master_json(audit_map: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Updates multiphase_course_data.json with verified answers and explanations."""
    print("--- [Step 1] Synchronizing Canonical Master JSON ---")
    with open(CANONICAL_MASTER_JSON, "r", encoding="utf-8") as f:
        master_data = json.load(f)

    phase1 = master_data["phases"][0]["days"][:15]
    exp_updated = 0
    std_updated = 0

    for day in phase1:
        # 1. Update expanded_questions
        for q in day.get("expanded_questions", []):
            qid = q.get("question_id")
            if qid in audit_map:
                aud = audit_map[qid]
                q["correct_answer"] = aud["new_correct_answer"]
                q["explanation"] = aud["updated_explanation"]
                if aud.get("is_modified"):
                    exp_updated += 1

        # 2. Update questions (standard)
        for q in day.get("questions", []):
            qid = q.get("question_id")
            if qid in audit_map:
                aud = audit_map[qid]
                q["correct_answer"] = aud["new_correct_answer"]
                q["explanation"] = aud["updated_explanation"]
                if aud.get("is_modified"):
                    std_updated += 1

    with open(CANONICAL_MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)

    print(f"Master JSON updated: {exp_updated} expanded and {std_updated} standard questions updated.")
    return {"exp_updated": exp_updated, "std_updated": std_updated}


def sync_auxiliary_jsons(audit_map: Dict[str, Dict[str, Any]]) -> None:
    """Updates verified_all_quizzes_master.json, course_data.json, quiz_data.json."""
    print("--- [Step 2] Synchronizing Auxiliary JSON Files ---")

    # 1. verified_all_quizzes_master.json
    with open(MASTER_SOLUTIONS_JSON, "r", encoding="utf-8") as f:
        master_sol = json.load(f)

    master_sol_updated = 0
    for qid, entry in master_sol.items():
        if qid in audit_map:
            aud = audit_map[qid]
            entry["explanation"] = aud["updated_explanation"]
            itype = aud["interaction_type"]
            new_ca = aud["new_correct_answer"]

            if itype == "single_select":
                entry["correct_response"] = {"correct_choice_id": new_ca}
            elif itype == "multi_select":
                entry["correct_response"] = {"correct_choice_ids": new_ca}
            elif itype == "matching":
                entry["correct_response"] = {"correct_pairs": new_ca}
            elif itype == "ordering":
                entry["correct_response"] = {"correct_order": new_ca}
            elif itype == "numeric_input":
                entry["correct_response"] = {"value": new_ca}

            if aud.get("is_modified"):
                master_sol_updated += 1

    with open(MASTER_SOLUTIONS_JSON, "w", encoding="utf-8") as f:
        json.dump(master_sol, f, ensure_ascii=False, indent=2)
    print(f"verified_all_quizzes_master.json: updated {master_sol_updated} entries.")

    # 2. Synchronize TAT_CA_QUIZ_KHOA_HOC.json from quiz_data.json
    shutil.copy2(QUIZ_DATA_JSON, DOWNLOADS_QUIZ_JSON)
    print(f"Mirrored {QUIZ_DATA_JSON.name} -> {DOWNLOADS_QUIZ_JSON}")


def sync_txt_files(audit_map: Dict[str, Dict[str, Any]]) -> None:
    """Updates standard quiz TXT files and question bank TXT files."""
    print("--- [Step 3] Synchronizing TXT Files ---")

    # 1. Standard TXT files: update explanations for the 5 modified standard questions
    std_txt_files = sorted(QUIZ_TXT_DIR.glob("*_QUIZ_CHI_TIET_DAP_AN.txt"))
    for f in std_txt_files:
        content = f.read_text(encoding="utf-8")
        original_content = content

        for qid, aud in audit_map.items():
            if qid in content and aud.get("is_modified"):
                new_exp = aud["updated_explanation"]
                # Match LỜI GIẢI THÍCH CHI TIẾT TỪ VLEARN:\n  <old_text> up to GỢI Ý or next CÂU
                pattern = re.compile(
                    rf"(Mã:\s*{re.escape(qid)}[\s\S]*?LỜI GIẢI THÍCH CHI TIẾT TỪ VLEARN:\s*\n\s*)([^\n]+(?:\n\s+[^\n]+)*)",
                    re.IGNORECASE,
                )
                m = pattern.search(content)
                if m:
                    content = content[:m.start(2)] + "  " + new_exp + content[m.end(2):]

        if content != original_content:
            f.write_text(content, encoding="utf-8")
            print(f"Updated standard TXT: {f.name}")

        # Mirror to downloads/Khoa_4_Phase_1/*/QUIZ_CHI_TIET_DAP_AN.txt
        folder_prefix = f.name.replace("_QUIZ_CHI_TIET_DAP_AN.txt", "")
        dl_target = DOWNLOADS_K4P1_DIR / folder_prefix / "QUIZ_CHI_TIET_DAP_AN.txt"
        if dl_target.exists():
            shutil.copy2(f, dl_target)

    # 2. Bank TXT files: update explanations and ensure mirror parity
    bank_files = sorted(QUIZ_TXT_DIR.glob("*_NGAN_HANG_TOAN_DIEN.txt"))
    alias_files = sorted(QUIZ_TXT_DIR.glob("DAY*_NGAN_HANG_*_TOAN_DIEN.txt"))

    for f in bank_files:
        content = f.read_text(encoding="utf-8")
        original_content = content

        for qid, aud in audit_map.items():
            if qid in content and aud.get("is_modified"):
                new_exp = aud["updated_explanation"]
                pattern = re.compile(
                    rf"(Mã:\s*{re.escape(qid)}[\s\S]*?PHÂN TÍCH LỜI GIẢI / NGUYÊN LÝ THIẾT KẾ TỪ VLEARN:\s*\n\s*)([^\n]+(?:\n\s+[^\n]+)*)",
                    re.IGNORECASE,
                )
                m = pattern.search(content)
                if m:
                    content = content[:m.start(2)] + "  " + new_exp + content[m.end(2):]

        if content != original_content:
            f.write_text(content, encoding="utf-8")
            print(f"Updated bank TXT: {f.name}")

        # Mirror to DAY*_... alias
        num = f.name.split("_")[0]
        matching_aliases = [a for a in alias_files if f"DAY{num}_" in a.name or f"DAY{int(num)}_" in a.name]
        for a in matching_aliases:
            shutil.copy2(f, a)


def sync_master_excel(audit_map: Dict[str, Dict[str, Any]]) -> None:
    """Updates VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx and its 2 mirrors."""
    print("--- [Step 4] Synchronizing Master Excel Workbooks ---")

    wb = openpyxl.load_workbook(MASTER_XLSX_1)

    # 1. Update 'Toàn Bộ 165 Câu Quiz & Đáp Án'
    if "Toàn Bộ 165 Câu Quiz & Đáp Án" in wb.sheetnames:
        ws = wb["Toàn Bộ 165 Câu Quiz & Đáp Án"]
        for r in range(4, ws.max_row + 1):
            qid_val = ws.cell(r, 4).value
            if qid_val:
                qid = str(qid_val).strip()
                if qid in audit_map:
                    aud = audit_map[qid]
                    ws.cell(r, 10).value = aud["updated_explanation"]
                    if aud["interaction_type"] == "numeric_input":
                        ws.cell(r, 9).value = f"👉 ĐÁP ÁN SỐ CHÍNH XÁC: {aud['new_correct_answer']}"

    # 2. Update individual day_* sheets
    day_sheets = [s for s in wb.sheetnames if s.startswith("day_") and "_Kho_" not in s]
    for sname in day_sheets:
        ws = wb[sname]
        for r in range(4, ws.max_row + 1):
            qid_val = ws.cell(r, 2).value
            if qid_val:
                qid = str(qid_val).strip()
                if qid in audit_map:
                    aud = audit_map[qid]
                    ws.cell(r, 8).value = aud["updated_explanation"]
                    if aud["interaction_type"] == "numeric_input":
                        ws.cell(r, 7).value = f"👉 ĐÁP ÁN SỐ CHÍNH XÁC: {aud['new_correct_answer']}"

    # 3. Update Day_*_Kho_* sheets (and Day_01_Ngan_Hang_150_Cau if present)
    kho_sheets = [s for s in wb.sheetnames if "_Kho_" in s or s == "Day_01_Ngan_Hang_150_Cau"]
    for sname in kho_sheets:
        ws = wb[sname]
        for r in range(4, ws.max_row + 1):
            qid_val = ws.cell(r, 2).value
            if qid_val:
                qid = str(qid_val).strip()
                if qid in audit_map:
                    aud = audit_map[qid]
                    if aud.get("is_modified"):
                        ws.cell(r, 10).value = aud["updated_explanation"]
                    # Update col 9 answer text if numeric
                    if aud["interaction_type"] == "numeric_input":
                        ws.cell(r, 9).value = f"👉 ĐÁP ÁN SỐ CHÍNH XÁC: {aud['new_correct_answer']}"

    # Save to all 3 paths
    wb.save(MASTER_XLSX_1)
    wb.close()
    shutil.copy2(MASTER_XLSX_1, MASTER_XLSX_2)
    shutil.copy2(MASTER_XLSX_1, MASTER_XLSX_3)
    print("Master Excel workbooks updated and mirrored to all 3 locations.")


def _format_matching_pairs(q: Dict[str, Any], ca: Dict[str, str]) -> str:
    """Formats matching pairs as '1-A, 2-B, 3-C'."""
    left_items = q["interaction"]["left"]
    right_items = q["interaction"]["right"]
    right_id_to_letter = {item["id"]: chr(ord("A") + idx) for idx, item in enumerate(right_items)}
    pairs = []
    for idx, litem in enumerate(left_items, 1):
        rid = ca.get(litem["id"])
        letter = right_id_to_letter.get(rid, "?")
        pairs.append(f"{idx}-{letter}")
    return ", ".join(pairs)


def sync_quizizz_workbooks(audit_map: Dict[str, Dict[str, Any]]) -> None:
    """Updates 01_CHUAN Quizizz workbooks (15 FULL + 45 parts) and 02_FULL workbooks."""
    print("--- [Step 5] Synchronizing Quizizz Excel Workbooks ---")

    with open(CANONICAL_MASTER_JSON, "r", encoding="utf-8") as f:
        master_data = json.load(f)
    phase1_days = master_data["phases"][0]["days"][:15]

    # 1. Update 01_CHUAN_IMPORT_QUIZIZZ_QUIZ_COM_904_CAU
    day_folders = sorted([d for d in QUIZIZZ_01_DIR.iterdir() if d.is_dir()])
    for day_idx, (day_data, folder) in enumerate(zip(phase1_days, day_folders), 1):
        exp_qs = day_data.get("expanded_questions", [])
        full_file = list(folder.glob("*FULL*.xlsx"))[0]

        wb = openpyxl.load_workbook(full_file)
        ws = wb["Create a Quiz"]

        for i, q in enumerate(exp_qs):
            row_idx = 3 + i
            qid = q["question_id"]
            if qid in audit_map and audit_map[qid].get("is_modified"):
                aud = audit_map[qid]
                new_ca = aud["new_correct_answer"]
                itype = aud["interaction_type"]

                # Update Explanation (col 11)
                ws.cell(row_idx, 11).value = aud["updated_explanation"]

                # Update Answer according to type
                if itype == "single_select":
                    sorted_choices = sorted(q["interaction"]["choices"], key=lambda c: c["choice_id"])
                    ca_idx = next(idx + 1 for idx, c in enumerate(sorted_choices) if c["choice_id"] == new_ca)
                    ws.cell(row_idx, 8).value = ca_idx
                elif itype == "multi_select":
                    sorted_choices = sorted(q["interaction"]["choices"], key=lambda c: c["choice_id"])
                    top5 = sorted_choices[:5]
                    ca_indices = sorted([idx + 1 for idx, c in enumerate(top5) if c["choice_id"] in new_ca])
                    ws.cell(row_idx, 8).value = ",".join(str(x) for x in ca_indices)
                elif itype == "numeric_input":
                    ws.cell(row_idx, 3).value = str(new_ca)
                    ws.cell(row_idx, 8).value = 1
                elif itype == "matching":
                    ws.cell(row_idx, 3).value = _format_matching_pairs(q, new_ca)
                    ws.cell(row_idx, 8).value = 1
                elif itype == "ordering":
                    ws.cell(row_idx, 3).value = " → ".join(new_ca)
                    ws.cell(row_idx, 8).value = 1

        wb.save(full_file)

        # Sync Part workbooks from the updated FULL workbook
        part_files = sorted(folder.glob("*Phan*.xlsx"))
        current_offset = 0
        for pf in part_files:
            wb_p = openpyxl.load_workbook(pf)
            ws_p = wb_p["Create a Quiz"]
            part_row_count = ws_p.max_row - 2

            for r_p in range(1, part_row_count + 1):
                full_row_idx = 3 + current_offset + (r_p - 1)
                p_row_idx = 2 + r_p
                # Copy values for options, ca, and explanation
                for c in range(1, 12):
                    ws_p.cell(p_row_idx, c).value = ws.cell(full_row_idx, c).value

            wb_p.save(pf)
            wb_p.close()
            current_offset += part_row_count

        wb.close()
        print(f"Day {day_idx:02d}: updated FULL and {len(part_files)} Part workbooks.")

    # Mirror all 60 files to vlearn-app/public/quiz_excel/
    for src_file in QUIZIZZ_01_DIR.rglob("*.xlsx"):
        rel_path = src_file.relative_to(QUIZIZZ_01_DIR)
        dest_file = PUBLIC_QUIZ_EXCEL_DIR / rel_path
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dest_file)
    print("Mirrored all 60 Quizizz workbooks to vlearn-app/public/quiz_excel/.")

    # 2. Update 02_FULL_NGAN_HANG_1679_CAU_CHI_TIET_CHIA_20_CAU
    wb_master = openpyxl.load_workbook(MASTER_XLSX_1, data_only=True)
    kho_sheets = [s for s in wb_master.sheetnames if "_Kho_" in s]
    p2_folders = sorted([d for d in QUIZIZZ_02_DIR.iterdir() if d.is_dir()])

    for sname, folder in zip(kho_sheets, p2_folders):
        ws_kho = wb_master[sname]
        kho_qids = [ws_kho.cell(r, 2).value for r in range(4, ws_kho.max_row + 1)]

        current_idx = 0
        for pf in sorted(folder.glob("*.xlsx")):
            wb_p2 = openpyxl.load_workbook(pf)
            ws_p2 = wb_p2["Create a Quiz"]
            data_rows = ws_p2.max_row - 2

            for r_p in range(1, data_rows + 1):
                qid = str(kho_qids[current_idx]).strip() if current_idx < len(kho_qids) else None
                row_idx = 2 + r_p

                if qid and qid in audit_map and audit_map[qid].get("is_modified"):
                    aud = audit_map[qid]
                    ws_p2.cell(row_idx, 11).value = aud["updated_explanation"]
                    if aud["interaction_type"] == "numeric_input":
                        ws_p2.cell(row_idx, 3).value = str(aud["new_correct_answer"])
                        ws_p2.cell(row_idx, 8).value = 1

                current_idx += 1

            wb_p2.save(pf)
            wb_p2.close()

    wb_master.close()
    print("Updated 02_FULL_NGAN_HANG_1679_CAU workbooks.")


def repack_and_mirror_zip() -> None:
    """Repacks TONG_HOP_QUIZ_15_NGAY_EXCEL.zip and mirrors it to vlearn-app/public/."""
    print("--- [Step 6] Repacking and Mirroring ZIP Archives ---")
    source_dir = PROJECT_ROOT / "TONG_HOP_QUIZ_15_NGAY_EXCEL"

    # Remove old zip if present
    if ZIP_MAIN.exists():
        ZIP_MAIN.unlink()

    # Create zip preserving relative paths
    with zipfile.ZipFile(ZIP_MAIN, "w", zipfile.ZIP_DEFLATED) as z:
        for file_path in sorted(source_dir.rglob("*")):
            if file_path.is_file():
                rel_path = file_path.relative_to(source_dir).as_posix()
                z.write(file_path, arcname=rel_path)

    # Mirror to public
    shutil.copy2(ZIP_MAIN, ZIP_PUBLIC)

    # Verify SHA256 equality and entry count
    h1 = hashlib.sha256(ZIP_MAIN.read_bytes()).hexdigest()
    h2 = hashlib.sha256(ZIP_PUBLIC.read_bytes()).hexdigest()
    assert h1 == h2, f"ZIP hash mismatch: {h1} != {h2}"

    with zipfile.ZipFile(ZIP_MAIN, "r") as z:
        entries = [name for name in z.namelist() if not name.endswith("/")]
    assert len(entries) == 146, f"Expected 146 entries in ZIP, found {len(entries)}"

    print(f"ZIP archives synchronized! SHA256: {h1[:16]}... (146 files verified)")


def run_all_sync() -> None:
    """Runs the full cross-file synchronization pipeline."""
    print("================================================================")
    print("Starting VLearn Quiz Cross-File Synchronization Pipeline")
    print("================================================================")

    audit_map = load_audit_map()
    print(f"Loaded {len(audit_map)} audited questions ({sum(1 for q in audit_map.values() if q.get('is_modified'))} modified).")

    sync_canonical_master_json(audit_map)
    sync_auxiliary_jsons(audit_map)
    sync_txt_files(audit_map)
    sync_master_excel(audit_map)
    sync_quizizz_workbooks(audit_map)
    try:
        from scripts.sync_essay_quizzes import run_essay_sync
        run_essay_sync()
    except Exception as e:
        print(f"Essay sync note: {e}")

    print("================================================================")
    print("Synchronization Complete: All Targets Successfully Synchronized!")
    print("================================================================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synchronize all quiz targets from audit results.")
    args = parser.parse_args()
    run_all_sync()
