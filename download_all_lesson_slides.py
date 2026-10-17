import os
import json
import re
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads", "Khoa_4_Phase_1")
USER_DATA_DIR = os.path.abspath("vlearn_browser_profile")

def clean_filename(s):
    # Remove invalid characters
    s = re.sub(r'[\\/*?:"<>|]', '_', s)
    return s.strip()

def run():
    print("=" * 70)
    print(" BẮT ĐẦU TẢI TOÀN BỘ CÁC FILE SLIDE BÀI GIẢNG GỐC CỦA TẤT CẢ CÁC DAY")
    print("=" * 70)

    slides_data = json.load(open("all_lesson_slides_cdn.json", encoding="utf-8"))

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(USER_DATA_DIR, headless=True)

        total_downloaded = 0
        total_slides = sum(len(d["slide_parts"]) for d in slides_data)

        for day in slides_data:
            day_folder = day["folder_name"]
            day_dir = os.path.join(BASE_DIR, day_folder)
            os.makedirs(day_dir, exist_ok=True)

            print(f"\n📂 [{day['day_label']}] -> {day_folder} ({len(day['slide_parts'])} slides):")

            for idx, part in enumerate(day["slide_parts"], 1):
                raw_title = part["title"]
                safe_title = clean_filename(raw_title)
                filename = f"Slide_{idx:02d}_{safe_title}.pdf"
                filepath = os.path.join(day_dir, filename)

                if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
                    print(f"  [✓ Đã có] {filename} ({os.path.getsize(filepath) // 1024} KB)")
                    total_downloaded += 1
                    continue

                cdn_url = part["cdn_url"]
                print(f"  [↓ Tải về] {filename} ...", end="", flush=True)

                try:
                    r = ctx.request.get(cdn_url)
                    if r.status == 200:
                        content = r.body()
                        with open(filepath, "wb") as f:
                            f.write(content)
                        print(f" Xong! ({len(content) // 1024} KB)")
                        total_downloaded += 1
                    else:
                        print(f" Lỗi! Status {r.status}")
                except Exception as e:
                    print(f" Lỗi exception: {e}")

        print("\n" + "=" * 70)
        print(f" [✓] HOÀN TẤT TẢI: {total_downloaded}/{total_slides} SLIDES VỀ THƯ MỤC CỤ THỂ!")
        print("=" * 70)
        ctx.close()

if __name__ == "__main__":
    run()
