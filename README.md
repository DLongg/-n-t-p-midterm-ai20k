# VLearn - Nền Tảng Ôn Tập & Luyện Thi Thích Ứng (AI 20K Midterm)

Ứng dụng web luyện thi thích ứng, quản lý ngân hàng câu hỏi và ôn tập toàn diện cho khoá đào tạo **AI 20K - Khóa 4 Phase 1 & Phase 2 (Day 01 - Day 29)**.

---

## 🌟 Tính Năng Nổi Bật

1. **Ngân Hàng 1.679 Câu Hỏi Khảo Thí Toàn Diện:**
   - **165 Câu Đề Chuẩn (VLearn Official):** Đúng 100% đề thi kiểm tra cuối ngày chính thức của 15 Day.
   - **904 Câu Trắc Nghiệm Khách Quan Tương Tác Trực Tuyến:**
     - 🔵 Trắc nghiệm đơn (Single Select)
     - 🟦 Trắc nghiệm nhiều đáp án đúng (Multi Select)
     - 🟣 Ghép cặp tương ứng (Matching)
     - 🟠 Sắp xếp quy trình (Ordering / Ranking)
     - 🟡 Tính toán điền số (Numeric Input)
   - **775 Câu Tự Luận & Phân Tích Tình Huống (Flashcard):**
     - Đề bài thực tế, case study, viết code thực hành.
     - Cơ chế lật thẻ xem Tiêu chí chấm điểm (Rubric), Phân tích nguyên lý thiết kế từ VLearn và Gợi ý cốt lõi.

2. **Chức Năng Gom & Luyện Tập "Câu Hay Sai":**
   - Tự động ghi nhận các câu làm sai vào bộ nhớ cục bộ (LocalStorage).
   - Nút **🔥 Câu hay sai (X)** tích hợp trực tiếp trên từng Day, cho phép luyện lại các câu chưa ổn như một đề thi chuẩn.
   - Cơ chế 1-click: **`[✅ Đã ổn · Bỏ khỏi câu hay sai]`** để gỡ câu hỏi khỏi danh sách câu sai khi đã nắm vững.

3. **Slide Bài Giảng Gốc Tích Hợp:**
   - Trình đọc Slide PDF nhúng trực tiếp trên từng bài học (kèm hỗ trợ chuyển slide nhanh).

4. **Tải Về Đầy Đủ Tài Liệu Học Tập:**
   - Bảng tổng hợp Master Excel (`.xlsx`).
   - Bộ đề chia nhỏ chuẩn Quiz.com / Quizizz (`.zip`).
   - File văn bản tổng hợp chi tiết đề và lời giải (`.txt`).

---

## 📊 Thống Kê Ngân Hàng Câu Hỏi Theo Từng Day (Phase 1)

| Day | Chủ Đề Bài Học | Đề Chuẩn | Kho Trắc Nghiệm | Thẻ Tự Luận | Tổng Ngân Hàng |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **Day 01** | Giới thiệu & Foundation LLM | 10 | 101 | 49 | **150** |
| **Day 02** | AI Product Lab & Business Framing | 5 | 35 | 86 | **121** |
| **Day 03** | Chatbot vs ReAct Agent | 15 | 32 | 52 | **84** |
| **Day 04** | System Prompt Engineering & Tool Calling Engine | 15 | 58 | 30 | **88** |
| **Day 05** | AI Product Thinking & Requirements | 10 | 40 | 38 | **78** |
| **Day 06** | AI Product Project Management | 15 | 26 | 27 | **53** |
| **Day 07** | Data Foundations, Embedding & Vector Store | 10 | 63 | 45 | **108** |
| **Day 08** | RAG Pipeline & Retrieval Evaluation | 10 | 57 | 55 | **112** |
| **Day 09** | Multi-Agent & A2A Systems | 10 | 59 | 48 | **107** |
| **Day 10** | Data Pipeline & Observability | 10 | 64 | 48 | **112** |
| **Day 11** | Guardrails & AI Safety | 10 | 65 | 57 | **122** |
| **Day 12** | Cloud Services & Deployment | 10 | 86 | 73 | **159** |
| **Day 13** | Monitoring, Logging & Observability | 10 | 76 | 61 | **137** |
| **Day 14** | AI Evaluation & Benchmarking | 10 | 74 | 52 | **126** |
| **Day 15** | Triển khai thực tế & Định hướng Enterprise | 15 | 68 | 54 | **122** |
| **Day 16** | Mini Hackathon Phase 1 | 0 | 0 | 0 | *Thi nhóm* |
| **TỔNG** | **Khóa 4 Phase 1** | **165** | **904** | **775** | **1.679** |

*Phase 2 (Track 3: Day 16 – Day 29) tập trung vào nghiên cứu Advanced Agents, Lab thực hành và Hackathon tốt nghiệp, sử dụng tài liệu slide lý thuyết.*

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Cục Bộ

### 1. Yêu cầu hệ thống:
- [Node.js](https://nodejs.org/) (phiên bản 18+ hoặc mới nhất).

### 2. Cài đặt và khởi chạy ứng dụng:
```bash
# 1. Chuyển vào thư mục ứng dụng web
cd vlearn-app

# 2. Cài đặt các gói phụ thuộc
npm install

# 3. Khởi chạy máy chủ phát triển
npm run dev
```

Mở trình duyệt truy cập: `http://localhost:5173/`

### 3. Đóng gói bản Production:
```bash
npm run build
```
Bản dựng tối ưu hóa sẽ được xuất ra thư mục `vlearn-app/dist/`.

---

## 📁 Cấu Trúc Thư Mục Dự Án

```
├── vlearn-app/                           # Ứng dụng React + Vite Frontend
│   ├── src/
│   │   ├── App.jsx                       # Thành phần giao diện chính & logic tương tác
│   │   ├── multiphase_course_data.json   # Dữ liệu 1.679 câu hỏi khảo thí toàn diện
│   │   ├── index.css                     # Hệ thống thiết kế & Style sheets
│   │   └── main.jsx
│   ├── public/
│   │   ├── quiz_txt/                     # Toàn bộ 15 file text đề thi mở rộng (.txt)
│   │   ├── quiz_excel/                   # File Excel chia nhỏ chuẩn Quizizz
│   │   ├── slides/                       # Tài liệu slide bài giảng các ngày
│   │   └── TONG_HOP_QUIZ_15_NGAY_EXCEL.zip
│   └── package.json
├── downloads/                            # Thư mục lưu trữ tài nguyên đã thu thập
├── TONG_HOP_QUIZ_15_NGAY_EXCEL/          # Thư mục bộ file Excel 15 ngày
├── VLEARN_K4P1_TOAN_BO_QUIZ_VA_SLIDES.xlsx # File bảng tính tổng hợp Master
├── update_all_day_quiz_files.py          # Script xử lý và đồng bộ đề thi
└── README.md
```

---

## 📜 Bản Quyền & Tác Quyền
Được phát triển phục vụ công tác ôn tập và luyện thi năng lực AI cho học viên khóa **AI 20K**.
