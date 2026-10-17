import os
import json
import time
import re
from playwright.sync_api import sync_playwright

BASE_DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)
USER_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vlearn_browser_profile")

def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[\\/*?:"<>|\n\r\t]', "_", name).strip()
    return cleaned[:100] if cleaned else "untitled"

def solve_and_extract_interactive_quiz(page, lesson_dir):
    """
    TỰ ĐỘNG THAO TÁC QUIZ ĐỂ KÍCH HOẠT VÀ BẮT TRỌN VẸN ĐÁP ÁN:
    - Nhận diện đa dạng các loại câu hỏi: Trắc nghiệm (Radio/Checkbox), Sắp xếp thứ tự (Drag/Drop/Rank), Nối cặp (Matching), Điền từ (Input)
    - Tự động click thử đáp án / nút kiểm tra / submit để giao diện hiển thị:
      + Đáp án đúng (Correct answer - màu xanh lá / class success/correct)
      + Giải thích chi tiết (Explanation / Feedback)
    """
    print("       [*] Đang kiểm tra câu hỏi tương tác / Quiz trên trang...")

    # BƯỚC 1: Tìm tất cả các container câu hỏi
    # Các selector phổ biến trên hệ thống LMS / Next.js
    quiz_containers = page.query_selector_all("""
        [data-question-id],
        [class*="question-card"],
        [class*="quiz-item"],
        [class*="exam-item"],
        [class*="quiz-container"],
        fieldset,
        [role="radiogroup"],
        .space-y-4 > div:has(label),
        [class*="card"]:has(label)
    """)

    if not quiz_containers:
        # Thử tìm theo cấu trúc danh sách hoặc câu hỏi
        quiz_containers = page.query_selector_all(".quiz, [class*='quiz'], [class*='question']")

    print(f"       [+] Tìm thấy {len(quiz_containers)} khối nghi vấn câu hỏi/bài tập.")

    extracted_quizzes = []

    # BƯỚC 2: Thao tác tương tác với từng câu hỏi
    for q_idx, container in enumerate(quiz_containers, 1):
        try:
            # 1. Trích xuất nội dung đề bài
            q_title = container.evaluate("""(node) => {
                const header = node.querySelector('h3, h4, h5, [class*="title"], [class*="text"], legend, strong, p');
                return header ? header.innerText.trim() : node.innerText.split('\\n')[0].trim();
            }""")

            # 2. Nhận diện hình thức câu hỏi:
            # a) Trắc nghiệm Radio / Checkbox
            choices_els = container.query_selector_all("label, [role='radio'], [role='checkbox'], button:has([class*='choice'])")
            
            # b) Sắp xếp thứ tự / Ranking / Drag & Drop
            drag_items = container.query_selector_all("[draggable='true'], [class*='sortable'], [class*='rank'], [class*='order']")

            # c) Ô nhập liệu / Điền từ
            text_inputs = container.query_selector_all("input[type='text'], textarea")

            q_type = "unknown"
            raw_options = []

            if drag_items:
                q_type = "ordering_ranking (sắp xếp thứ tự / ưu tiên)"
                raw_options = [d.inner_text().strip() for d in drag_items]
            elif choices_els:
                q_type = "multiple_choice (lựa chọn trắc nghiệm)"
                raw_options = [c.inner_text().strip() for c in choices_els]
            elif text_inputs:
                q_type = "fill_in_blank (điền từ / trả lời ngắn)"

            # THAO TÁC: Thử click lựa chọn đầu tiên để kích hoạt trạng thái "Submit" hoặc "Kiểm tra"
            if choices_els:
                try:
                    # Click thử vào một đáp án
                    first_choice = choices_els[0]
                    first_choice.scroll_into_view_if_needed()
                    first_choice.click(timeout=1500)
                    time.sleep(0.5)
                except Exception:
                    pass

            # BƯỚC 3: Tìm nút "Kiểm tra đáp án" / "Submit" / "Xem giải thích" / "Check"
            action_buttons = container.query_selector_all("button, [role='button']")
            for btn in action_buttons:
                btn_text = btn.inner_text().lower()
                if any(w in btn_text for w in ["kiểm tra", "check", "xem đáp án", "nộp bài", "submit", "giải thích", "xem kết quả"]):
                    try:
                        btn.click(timeout=2000)
                        time.sleep(1.2) # Chờ kết quả trả về từ server
                        break
                    except Exception:
                        pass

            # BƯỚC 4: Sau khi thao tác, trích xuất đáp án đúng hiển thị trên UI
            feedback = container.evaluate("""(node) => {
                const res = {
                    correctAnswers: [],
                    explanations: [],
                    isCorrect: false
                };

                // Tìm các phần tử được highlight màu xanh lá (thành công / đúng)
                const correctNodes = node.querySelectorAll(
                    '[class*="success"], [class*="correct"], [class*="bg-emerald"], [class*="bg-green"], [aria-label*="correct"], [data-correct="true"]'
                );
                correctNodes.forEach(c => {
                    if (c.innerText) res.correctAnswers.push(c.innerText.trim());
                });

                // Tìm khối giải thích / gợi ý
                const expNodes = node.querySelectorAll('[class*="explain"], [class*="explanation"], [class*="feedback"], [class*="hint"]');
                expNodes.forEach(e => {
                    if (e.innerText) res.explanations.push(e.innerText.trim());
                });

                return res;
            }""")

            quiz_item = {
                "cau_so": q_idx,
                "loai_cau_hoi": q_type,
                "de_bai": q_title,
                "danh_sach_lua_chon": raw_options,
                "dap_an_dung_sau_thao_tac": feedback.get("correctAnswers", []),
                "giai_thich_chi_tiet": feedback.get("explanations", [])
            }

            extracted_quizzes.append(quiz_item)
            print(f"         + Câu {q_idx} [{q_type}]: {q_title[:60]}...")
            if feedback.get("correctAnswers"):
                print(f"           -> Đáp án đúng nhận được: {feedback.get('correctAnswers')}")

        except Exception as e:
            print(f"         [!] Lỗi khi xử lý câu {q_idx}: {e}")

    # BƯỚC 5: Lưu dữ liệu Quiz vào file
    if extracted_quizzes:
        json_out = os.path.join(lesson_dir, "quiz_chi_tiet_kem_dap_an.json")
        txt_out = os.path.join(lesson_dir, "quiz_chi_tiet_kem_dap_an.txt")

        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(extracted_quizzes, f, ensure_ascii=False, indent=2)

        with open(txt_out, "w", encoding="utf-8") as f:
            for q in extracted_quizzes:
                f.write(f"CÂU {q['cau_so']}: {q['de_bai']}\n")
                f.write(f"Hình thức: {q['loai_cau_hoi']}\n")
                f.write("Các lựa chọn / thành phần ban đầu:\n")
                for opt in q['danh_sach_lua_chon']:
                    f.write(f"   - {opt}\n")
                if q['dap_an_dung_sau_thao_tac']:
                    f.write(f"\n=> ĐÁP ÁN ĐÚNG TRẢ VỀ: {', '.join(q['dap_an_dung_sau_thao_tac'])}\n")
                if q['giai_thich_chi_tiet']:
                    f.write(f"=> GIẢI THÍCH: {', '.join(q['giai_thich_chi_tiet'])}\n")
                f.write("\n" + "="*50 + "\n\n")

        print(f"       [✓] Đã xuất {len(extracted_quizzes)} câu hỏi Quiz kèm đáp án vào: quiz_chi_tiet_kem_dap_an.txt")

def inspect_and_download_slides(page, context, lesson_dir):
    """
    TÌM TOÀN BỘ SLIDE TRONG CẤU TRÚC:
    - File slide trực tiếp (.pdf, .pptx)
    - Slide nhúng (Google Slides, Canva, Loom, Iframe viewer)
    - Tải file về thư mục nếu có link tải
    """
    time.sleep(2)
    slide_info = page.evaluate("""() => {
        const result = {
            iframes: [],
            downloadFiles: []
        };

        // 1. Quét iframe
        document.querySelectorAll('iframe').forEach(f => {
            if (f.src) {
                result.iframes.push({
                    src: f.src,
                    title: f.title || f.getAttribute('aria-label') || 'Slide Embed'
                });
            }
        });

        // 2. Quét file tài liệu
        document.querySelectorAll('a').forEach(a => {
            const href = a.href || '';
            const text = (a.innerText || '').trim();
            if (/\\.(pdf|pptx?|docx?|zip|rar)(\\?|$)/i.test(href) || /slide|tài liệu|bài giảng|tải về/i.test(text)) {
                if (href.startsWith('http')) {
                    result.downloadFiles.push({ text: text || 'Slide_Tai_Lieu', url: href });
                }
            }
        });

        return result;
    }""")

    # Lưu thông tin slide nhúng
    if slide_info["iframes"]:
        print(f"       [+] Tìm thấy {len(slide_info['iframes'])} Slide nhúng (Canva / Slides / Viewer):")
        with open(os.path.join(lesson_dir, "slide_nhung.txt"), "w", encoding="utf-8") as f:
            for s in slide_info["iframes"]:
                print(f"           - {s['title']}: {s['src']}")
                f.write(f"Tiêu đề: {s['title']}\nLink: {s['src']}\n\n")

    # Tải file slide trực tiếp
    if slide_info["downloadFiles"]:
        for idx, dl in enumerate(slide_info["downloadFiles"], 1):
            url = dl["url"]
            ext = url.split("?")[0].split(".")[-1] if "." in url else "pdf"
            fname = sanitize_filename(dl["text"] or f"Slide_{idx}") + f".{ext}"
            fpath = os.path.join(lesson_dir, fname)
            try:
                res = context.request.get(url)
                if res.status == 200:
                    with open(fpath, "wb") as f:
                        f.write(res.body())
                    print(f"       [✓] Đã tải slide/tài liệu: {fname}")
            except Exception as e:
                print(f"       [!] Không thể tải slide từ {url}: {e}")

def process_single_lesson(page, context, lesson_dir, lesson_title):
    os.makedirs(lesson_dir, exist_ok=True)
    print(f"\n[*] Đang xử lý nội dung bài: {lesson_title}")
    
    # 1. Quét và tải Slide
    inspect_and_download_slides(page, context, lesson_dir)

    # 2. Tự động tương tác giải Quiz và trích xuất đáp án đúng
    solve_and_extract_interactive_quiz(page, lesson_dir)

    # 3. Chụp ảnh toàn bài & lưu nội dung HTML
    try:
        page.screenshot(path=os.path.join(lesson_dir, "man_hinh_bai_hoc.png"), full_page=True)
        with open(os.path.join(lesson_dir, "noi_dung_bai.html"), "w", encoding="utf-8") as f:
            f.write(page.content())
    except Exception:
        pass

def scrape_entire_course(page, context):
    print("\n[*] Đang phân tích cấu trúc cây bài học của khóa học...")
    time.sleep(3)

    structure = page.evaluate("""() => {
        const data = {
            courseName: '',
            items: []
        };

        const h1 = document.querySelector('h1, [class*="course_title"], .course-learning__identity h1');
        data.courseName = h1 ? h1.innerText.trim() : (document.title || 'Khoa_Hoc_Vlearn');

        const anchors = Array.from(document.querySelectorAll('a'));
        const lessonLinks = [];

        anchors.forEach(a => {
            const href = a.href || '';
            const text = (a.innerText || '').trim();
            if (href.includes('reader?day=') || href.includes('/lesson/') || href.includes('/quiz/')) {
                if (!lessonLinks.some(x => x.href === href)) {
                    const lines = text.split('\\n').map(s => s.trim()).filter(Boolean);
                    const cleanTitle = lines.length > 0 ? lines.join(' - ') : href.split('/').pop();
                    lessonLinks.push({
                        title: cleanTitle,
                        href: href
                    });
                }
            }
        });

        data.items = lessonLinks;
        return data;
    }""")

    items = structure.get("items", [])
    course_name = structure.get("courseName") or "Khoa_Hoc_Vlearn"
    course_dir = os.path.join(BASE_DOWNLOAD_DIR, sanitize_filename(course_name))
    os.makedirs(course_dir, exist_ok=True)

    print("=" * 70)
    print(f" [✓] KHÓA HỌC:          {course_name}")
    print(f" [✓] SỐ BÀI HỌC TÌM THẤY: {len(items)} bài")
    print(f" [✓] THƯ MỤC LƯU TRỮ:    {course_dir}")
    print("=" * 70)

    # Lưu file sơ đồ cấu trúc
    with open(os.path.join(course_dir, "CAU_TRUC_KHOA_HOC.md"), "w", encoding="utf-8") as f:
        f.write(f"# CẤU TRÚC KHÓA HỌC: {course_name}\n\n")
        f.write(f"URL: {page.url}\n\n")
        f.write("## Danh mục bài học chi tiết:\n\n")
        for idx, it in enumerate(items, 1):
            f.write(f"{idx:02d}. [{it['title']}]({it['href']})\n")

    # Bắt đầu tự động duyệt từng bài, tải slide và thao tác quiz
    for idx, item in enumerate(items, 1):
        folder_name = f"{idx:02d}_{sanitize_filename(item['title'])}"
        lesson_dir = os.path.join(course_dir, folder_name)

        print(f"\n=======================================================")
        print(f"[{idx}/{len(items)}] ĐANG DUYỆT BÀI: {item['title']}")
        print(f"URL: {item['href']}")
        print(f"Thư mục lưu: {folder_name}")
        print("=======================================================")

        try:
            page.goto(item["href"], wait_until="domcontentloaded", timeout=45000)
            process_single_lesson(page, context, lesson_dir, item["title"])
        except Exception as e:
            print(f"      [!] Lỗi khi duyệt bài: {e}")

    print("\n" + "=" * 70)
    print(" [✓] HOÀN TẤT QUÉT CẤU TRÚC, TẢI SLIDE VÀ THAO TÁC LẤY ĐÁP ÁN QUIZ!")
    print(f" [✓] Kiểm tra kết quả tại: {course_dir}")
    print("=" * 70)

def main():
    print("=" * 70)
    print(" VLEARN SCRAPER: TỰ ĐỘNG THAO TÁC QUIZ & TẢI SLIDE THEO CẤU TRÚC")
    print("=" * 70)

    # Lắng nghe các API calls (đặc biệt là API submit/check quiz ngầm)
    captured_apis = []

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            viewport={"width": 1400, "height": 900},
            args=["--start-maximized"]
        )
        page = context.pages[0] if context.pages else context.new_page()

        def on_response(response):
            try:
                url = response.url.lower()
                if any(k in url for k in ["quiz", "answer", "submit", "check", "question", "grade"]):
                    if "json" in response.headers.get("content-type", ""):
                        data = response.json()
                        captured_apis.append({"url": response.url, "data": data})
            except Exception:
                pass

        page.on("response", on_response)

        print("[*] Đang mở VLearn...")
        page.goto("https://vlearn.dev/dashboard", wait_until="domcontentloaded")

        print("\n[>>>] BẠN VUI LÒNG ĐĂNG NHẬP TÀI KHOẢN TRÊN TRÌNH DUYỆT...")
        print("      (Script sẽ tự động phát hiện khi bạn đăng nhập thành công)")

        # Tự động chờ bạn đăng nhập
        while True:
            time.sleep(2)
            url = page.url.lower()
            if "login" not in url and ("dashboard" in url or "course" in url or "my-courses" in url):
                print(f"\n[✓] Đã phát hiện đăng nhập thành công! (URL: {page.url})")
                break

        # Nếu chưa vào trang khóa học cụ thể, tự tìm hoặc điều hướng
        if "course/" not in page.url.lower():
            print("[*] Đang tự động tìm khóa học của bạn...")
            time.sleep(2)
            course_link = page.evaluate("""() => {
                const a = document.querySelector('a[href*="/course/"]');
                return a ? a.href : null;
            }""")
            if course_link:
                page.goto(course_link, wait_until="domcontentloaded")
            else:
                page.goto("https://vlearn.dev/my-courses", wait_until="domcontentloaded")
                time.sleep(2.5)
                course_link = page.evaluate("""() => {
                    const a = document.querySelector('a[href*="/course/"]');
                    return a ? a.href : null;
                }""")
                if course_link:
                    page.goto(course_link, wait_until="domcontentloaded")
                else:
                    print("[!] Hãy click vào khóa học bạn muốn tải trên trình duyệt...")
                    while "course/" not in page.url.lower():
                        time.sleep(1.5)

        # Đã ở trong trang khóa học -> Bắt đầu quét & thao tác quiz
        scrape_entire_course(page, context)

        # Lưu lại toàn bộ API calls bắt được trong lúc thao tác Quiz
        if captured_apis:
            api_save_path = os.path.join(BASE_DOWNLOAD_DIR, "tat_ca_api_quiz_goi_ve.json")
            with open(api_save_path, "w", encoding="utf-8") as f:
                json.dump(captured_apis, f, ensure_ascii=False, indent=2)
            print(f"[✓] Đã lưu file bắt gói tin API Quiz: {api_save_path}")

        print("\nHoàn tất! Giữ cửa sổ 15 giây trước khi đóng...")
        time.sleep(15)
        context.close()

if __name__ == "__main__":
    main()
