import os
import json

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads", "Khoa_4_Phase_1")

# Load raw quiz questions (165 questions)
quizzes_raw = json.load(open("all_days_quizzes_raw.json", encoding="utf-8"))

DAY_FOLDERS = [
    "01_Day01",
    "02_DAY02",
    "03_DAY03",
    "04_DAY04",
    "05_Day05",
    "06_Day06",
    "07_Day07",
    "08_Day08",
    "09_Day09",
    "10_Day10-data-pipeline-observability",
    "11_Day11-guardrails-ai-safety",
    "12_Day12-cloud-services-and-deployment",
    "13_Day13-monitoring-logging-observability",
    "14_Day14-ai-evaluation-benchmarking",
    "15_Day15-trien-khai-thuc-te-dinh-huong"
]

def format_quiz_detail(q_idx, q):
    q_id = q.get("question_id", "")
    inter = q.get("interaction", {})
    q_type = inter.get("type", "single_select")
    prompt = inter.get("prompt", "").strip()
    diff = q.get("estimated_difficulty", "medium")
    hints = [h.get("text") for h in q.get("hints", []) if h.get("text")]

    type_titles = {
        "single_select": "TRẮC NGHIỆM ĐƠN (CHỌN 1 ĐÁP ÁN)",
        "multi_select": "TRẮC NGHIỆM NHIỀU ĐÁP ÁN (CHỌN TẤT CẢ ĐÁP ÁN ĐÚNG)",
        "matching": "GHÉP CẶP TƯƠNG ỨNG",
        "ordering": "SẮP XẾP THỨ TỰ QUY TRÌNH",
        "numeric_input": "TÍNH TOÁN / ĐIỀN SỐ CHÍNH XÁC"
    }

    lines = []
    lines.append(f"{'='*70}")
    lines.append(f"CÂU {q_idx:02d} [{type_titles.get(q_type, q_type.upper())}] - Mã: {q_id} (Độ khó: {diff})")
    lines.append(f"{'='*70}")
    lines.append(f"ĐỀ BÀI:\n{prompt}\n")

    if q_type in ["single_select", "multi_select"]:
        lines.append("CÁC PHƯƠNG ÁN LỰA CHỌN:")
        for idx, c in enumerate(inter.get("choices", []), 1):
            letter = chr(64 + idx)
            lines.append(f"  [{letter}] {c.get('text')}")
    elif q_type == "matching":
        lines.append("NỘI DUNG GHÉP CẶP:")
        lines.append("  * Danh sách mệnh đề / tác vụ [Cột trái]:")
        for idx, l in enumerate(inter.get("left", []), 1):
            lines.append(f"     {idx}. {l.get('text')}")
        lines.append("  * Danh sách ý nghĩa / định nghĩa [Cột phải]:")
        for idx, r in enumerate(inter.get("right", []), 1):
            letter = chr(64 + idx)
            lines.append(f"     ({letter}) {r.get('text')}")
    elif q_type == "ordering":
        lines.append("CÁC BƯỚC CẦN SẮP XẾP:")
        for idx, it in enumerate(inter.get("items", []), 1):
            lines.append(f"  - Bước: {it.get('text')}")
    elif q_type == "numeric_input":
        req = inter.get("required_unit", "")
        lines.append(f"YÊU CẦU ĐẦU RA: Điền giá trị số cụ thể (Đơn vị: {req if req else 'Không có'})")

    if hints:
        lines.append("\nGỢI Ý / NGUYÊN LÝ TỪ VLEARN:")
        for h in hints:
            lines.append(f"  💡 {h}")

    lines.append("\n")
    return "\n".join(lines)

for idx, day_obj in enumerate(quizzes_raw):
    folder_name = DAY_FOLDERS[idx]
    day_label = day_obj["dayLabel"]
    qs = day_obj["questions"]
    day_dir = os.path.join(BASE_DIR, folder_name)
    os.makedirs(day_dir, exist_ok=True)

    txt_path = os.path.join(day_dir, "QUIZ_CHI_TIET_DAP_AN.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"######################################################################\n")
        f.write(f"# BẢNG ĐỀ BÀI VÀ HƯỚNG DẪN GIẢI QUIZ CHI TIẾT: {day_label} ({folder_name})\n")
        f.write(f"# Tổng số câu hỏi: {len(qs)} câu hỏi gốc (100% văn bản chuẩn cấu trúc VLearn)\n")
        f.write(f"######################################################################\n\n")

        for q_idx, q in enumerate(qs, 1):
            f.write(format_quiz_detail(q_idx, q))

    print(f"[✓] Đã cập nhật file QUIZ_CHI_TIET_DAP_AN.txt cho {folder_name} ({len(qs)} câu đầy đủ)")

print("\nHoàn tất cập nhật tất cả file text quiz cho 15 Day!")
