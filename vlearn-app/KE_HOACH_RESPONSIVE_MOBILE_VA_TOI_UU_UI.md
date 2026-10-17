# Kế Hoạch Nâng Cấp Giao Diện Responsive Mobile & Sắp Xếp Nút Chức Năng Hợp Lý (VLearn App)

> **Mục tiêu:** Tối ưu hóa trải nghiệm học tập và ôn thi trắc nghiệm trên thiết bị di động (Smartphones & Tablets), biến VLearn thành một Web App mượt mà, trực quan, dễ thao tác bằng một tay (Thumb-Zone Friendly), loại bỏ hoàn toàn tình trạng vỡ khung, tràn ngang và quá tải nút bấm.

---

## I. Phân Tích Hiện Trạng & Điểm Nghẽn (Pain Points) Trên Mobile

Hiện tại, giao diện VLearn đang tối ưu chủ yếu cho Desktop (màn hình rộng $\ge 1200\text{px}$). Khi mở trên điện thoại (màn hình $360\text{px} - 430\text{px}$), ứng dụng gặp các hạn chế nghiêm trọng sau:

```
┌────────────────────────────────────────────────────────────────────────┐
│ TRÊN DESKTOP (Hiện tại): Rộng rãi, hiển thị ngang 2 cột                │
├───────────────────┬────────────────────────────────────────────────────┤
│ Sidebar (340px)   │ Main Content (Quiz / Slide)                        │
│ Danh sách 16 Day  │ Hàng loạt nút chọn kho + Nút tải + Lưới 150 ô số   │
└───────────────────┴────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│ TRÊN MOBILE (Vấn đề):                                                  │
│ ❌ Header (64px) nhồi nhét 6-7 nút to ➔ Vỡ giao diện, tràn viền         │
│ ❌ Sidebar 340px chiếm trọn màn hình ➔ Không thấy nội dung bài tập      │
│ ❌ Cụm nút kho đề (5 nút) + Công cụ (6 nút) chiếm 50% màn hình dọc     │
│ ❌ Lưới câu hỏi (10-150 ô) đẩy câu hỏi xuống quá sâu                   │
│ ❌ Dạng Ghép cặp (Matching) 2 cột bị co rúm, không đọc được nội dung   │
│ ❌ Nút "Kiểm tra" / "Câu tiếp theo" nằm ở đáy thẻ, phải cuộn liên tục  │
└────────────────────────────────────────────────────────────────────────┘
```

### Chi tiết các điểm nghẽn cụ thể:
1. **Thanh Header trên cùng (`.app-header`):**
   - Đang chứa đồng thời: Logo `VLearn`, Phase Switcher (2 nút), Tab Luyện tập / Slide, nút "Cấu trúc đề", nút "Tải Bảng Excel (.xlsx)", nút "Bộ Quizizz (.zip)".
   - *Hậu quả:* Trên màn hình $\le 768\text{px}$, các nút bị rớt dòng lộn xộn hoặc tràn màn hình ngang.
2. **Thanh Sidebar bên trái (`.sidebar`):**
   - Đang fix cứng `width: 340px` và layout ngang `flex-direction: row`.
   - *Hậu quả:* Chiếm toàn bộ không gian điện thoại, người dùng không thể làm bài hoặc phải cuộn ngang bất tiện.
3. **Cụm nút chọn kho & thao tác phụ (Quiz Header Card):**
   - Đang hiển thị cùng lúc hơn **10 nút bấm**:
     - Nhóm kho: `Đề chuẩn`, `Toàn bộ kho`, `Thẻ tự luận`, `Câu hay sai`, `Tổng câu sai`.
     - Nhóm thao tác: `Chế độ Ôn thi`, `Tải kho (.txt)`, `Excel Quizizz`, `Tải bài giải (.txt)`, `Hiện hết đáp án`, `Làm lại`.
   - *Hậu quả:* Người dùng phải cuộn qua 2-3 màn hình toàn nút bấm mới thấy đề câu hỏi.
4. **Lưới số câu hỏi (`.question-nav-grid`):**
   - Khi ở kho mở rộng (100 - 150 câu), lưới 150 nút chiếm chiều cao rất lớn.
5. **Dạng câu hỏi Ghép cặp (Matching) & Sắp xếp (Ordering):**
   - Ghép cặp chia lưới `grid-template-columns: 1fr 1fr;` khiến mỗi cột chỉ còn $\sim 150\text{px}$, text bị cắt xén, dropdown bị tràn.
   - Nút tăng giảm thứ tự sắp xếp ($\uparrow \downarrow$) quá nhỏ, ngón tay khó chạm chính xác.
6. **Thanh điều hướng câu hỏi đáy bài (`.quiz-action-bar`):**
   - Đặt cố định cuối câu hỏi. Với câu dài hoặc nhiều phương án, người dùng phải cuộn kịch sàn mới thấy nút "Kiểm tra" hoặc "Câu tiếp theo".

---

## II. Nguyên Tắc Thiết Kế Trải Nghiệm Mới (Design Principles)

1. **Mobile First & Thumb Zone Focus:** Mọi nút bấm cốt lõi (Kiểm tra, Tiếp theo, Chọn đáp án) phải nằm trong vùng thao tác tự nhiên của ngón tay cái (nửa dưới màn hình).
2. **Phân cấp chức năng (Visual Hierarchy & Progressive Disclosure):**
   - **Tần suất cao (Core Loop):** Đọc đề $\rightarrow$ Chọn đáp án $\rightarrow$ Kiểm tra $\rightarrow$ Sang câu tiếp. Luôn luôn nổi bật 100%.
   - **Tần suất trung bình:** Đổi kho câu hỏi, Lọc trạng thái (Đúng/Sai/Chưa làm), Xem gợi ý, Ghim câu sai. Hiển thị dạng thanh cuộn ngang hoặc Tab gọn gàng.
   - **Tần suất thấp:** Tải file (.xlsx, .zip, .txt), xem cấu trúc đề thi, làm lại từ đầu. Gom vào menu mở rộng `[ ⋯ Thao tác ]`.
3. **Off-canvas Navigation:** Chuyển Sidebar danh sách Day thành ngăn kéo trượt (Slide-out Drawer) hoặc Bottom Sheet, mở ra khi bấm vào tiêu đề Day ở đỉnh trang.
4. **Sticky Bottom Action Bar:** Thanh nút điều hướng câu hỏi luôn cố định ở mép dưới cùng màn hình điện thoại (có hỗ trợ Safe-area cho iPhone notch).

---

## III. Bảng Ma Trận & Tái Bố Trí Toàn Bộ Nút Chức Năng

| Tên Nút / Chức Năng | Tần Suất Dùng | Vị Trí Cũ (Desktop) | Vị Trí Mới Đề Xuất Trên Mobile | Kiểu Trình Bày (UI Pattern) |
| :--- | :---: | :--- | :--- | :--- |
| **Nút mở danh sách Day** | Cao | Nằm lộ ở Sidebar bên trái | Nút Dropdown trên Topbar: `[Day 01 ▾]` | Header Bar Button (chạm để mở Drawer) |
| **Chuyển Phase (Phase 1 / Phase 2)** | Thấp | Cạnh logo trên Header | Đặt bên trong đầu Drawer chọn Day | Segmented Switcher gọn gàng |
| **Chuyển Tab (Quiz / Slide)** | Vừa | Nằm trên Header | Segmented Control 2 nút ngay dưới Header | 2 Tab chia đều 50% - 50% |
| **Cấu trúc đề (165 câu)** | Thấp | Nằm trên Header | Chuyển vào Menu mở rộng (More menu `⋯`) | Item trong Dropdown Sheet |
| **Tải Excel Master (.xlsx)** | Thấp | Nút xanh lá trên Header | Chuyển vào Menu mở rộng (More menu `⋯`) | Item trong Dropdown Sheet |
| **Tải ZIP 45 file Quizizz** | Thấp | Nút tím trên Header | Chuyển vào Menu mở rộng (More menu `⋯`) | Item trong Dropdown Sheet |
| **Bộ chọn Kho câu hỏi (5 chế độ)** | Cao | Cụm nút dài ngoằng trên card | Thanh Tabs cuộn ngang (Horizontal Scroll Pill) | Swipeable Pills mượt mà |
| **Toggle Chế độ Ôn thi** | Vừa | Checkbox dài trong card | Nút icon bóng đèn / Switch nhỏ trên toolbar | Quick Switch `[💡 Ôn thi: Bật/Tắt]` |
| **Bộ nút tải Txt / Excel theo Day** | Thấp | 3 nút dài chiếm diện tích | Gom vào nút `[ 📥 Tải tài liệu ▾ ]` | Dropdown Action Sheet |
| **Hiện hết đáp án / Làm lại** | Thấp | 2 nút nằm cạnh bộ lọc | Nằm trong menu `[ ⋯ ]` của Quiz | Tránh bấm nhầm làm lộ/mất kết quả |
| **Lưới số câu hỏi (Nav Grid)** | Cao | Lưới 40x40px chiếm 1 khối lớn | Thanh tóm tắt `[◄] Câu 3/10 [►] [☷ Lưới]` | Bấm `[☷]` bung Modal Bottom Sheet |
| **Bộ lọc câu hỏi (Tất cả/Đúng/Sai)**| Vừa | 5 nút nhỏ xếp hàng | Hàng chip lọc nhỏ có thể lướt ngang | Horizontal Chip Filter List |
| **Ghim câu sai / Đã ổn bỏ ra** | Cao | Nằm cạnh tiêu đề câu | Nằm góc phải của thẻ câu hỏi | Badge Button trực quan `[🔥 Ghim]` |
| **Nút "Xem đáp án câu này"** | Vừa | Nằm góc dưới bên phải card | Nút phụ bên cạnh nút Kiểm tra | Secondary Button |
| **Nút "Kiểm tra đáp án"** | Cực cao| Nằm góc dưới bên phải card | **Thanh cố định đáy màn hình (Sticky Bottom)** | Primary CTA Button to, dễ bấm |
| **Nút "Câu tiếp theo / Câu trước"** | Cực cao| Nằm góc dưới card | **Thanh cố định đáy màn hình (Sticky Bottom)** | Cố định 2 bên ngón cái |

---

## IV. Bản Vẽ Giao Diện Mobile Chi Tiết (Wireframes)

### 1. Header & Navigation Trên Điện Thoại
```
┌────────────────────────────────────────────────────────┐
│  [☰] VLearn       [ Day 01: Giới thiệu AI ▾ ]      [⋯] │  <-- Topbar tinh gọn (54px)
├───────────────────────────┬────────────────────────────┤
│   📝 Luyện tập Quiz (10)  │   📑 Slide Bài giảng (2)   │  <-- Segmented Tab Switcher
└───────────────────────────┴────────────────────────────┘
```
- **Nút [☰]:** Mở Drawer danh sách toàn bộ các Day (có Phase 1, Phase 2, số câu sai, trạng thái hoàn thành).
- **Nút [ Day 01 ▾ ]:** Hiển thị tên bài hiện tại, bấm vào cũng có thể đổi nhanh Day kế tiếp/trước đó.
- **Nút [⋯]:** Mở Action Sheet gồm:
  - ℹ️ Hướng dẫn cấu trúc đề thi (165 câu)
  - 📊 Tải Bảng Excel Master (.xlsx)
  - 📦 Tải Trọn bộ 45 file Quizizz (.zip)
  - 📥 Tải bài giải chi tiết Day này (.txt)
  - 🔄 Làm lại bài thi của Day này

---

### 2. Khu Vực Luyện Quiz & Bộ Nút Kho Đề
```
┌────────────────────────────────────────────────────────┐
│ ── CHỌN KHO ĐỀ (Vuốt ngang) ────────────────────────── │
│ [🎯 Đề chuẩn (10)] [📚 Mở rộng (101)] [🔥 Câu sai (2)] │  <-- Horizontal Scroll Pills
├────────────────────────────────────────────────────────┤
│ Tiến độ: 4/10 câu · 3 đúng, 1 sai    [💡 Ôn thi: TẮT]  │  <-- Tóm tắt tiến độ & Toggle
├────────────────────────────────────────────────────────┤
│ [Tất cả 10] [Chưa làm 6] [Đúng 3] [Sai 1]              │  <-- Chips lọc trạng thái
├────────────────────────────────────────────────────────┤
│  ◄ Câu trước       Câu 4 / 10       [☷ Xem lưới câu]  ►│  <-- Điều hướng nhanh câu hỏi
└────────────────────────────────────────────────────────┘
```
- Người dùng chỉ mất $\sim 130\text{px}$ chiều dọc cho phần điều khiển, dành $80\%$ diện tích còn lại để đọc đề bài!
- Bấm vào `[☷ Xem lưới câu]` sẽ đẩy lên một **Bottom Sheet** chứa toàn bộ các ô tròn $1, 2, 3... 100$ để nhảy nhanh tới câu mong muốn, không lo chiếm chỗ giao diện chính.

---

### 3. Thẻ Câu Hỏi & Tương Tác Thích Ứng (Responsive Question Card)

#### A. Trắc nghiệm 1 đáp án (Single) & Nhiều đáp án (Multi):
```
┌────────────────────────────────────────────────────────┐
│ [🔵 TRẮC NGHIỆM ĐƠN]        [+ Ghim câu hay sai ⭐]   │
│ Câu 4 / 10 · Mã: D01_Q04 · Độ khó: Vừa                │
├────────────────────────────────────────────────────────┤
│ ĐỀ BÀI:                                                │
│ Khái niệm "Hallucination" trong mô hình ngôn ngữ lớn   │
│ ám chỉ hiện tượng nào sau đây?                         │
│                                                        │
│ ┌────────────────────────────────────────────────────┐ │
│ │ (A) Mô hình phản hồi thông tin bịa đặt/không thực  │ │ <-- Touch target >= 48px
│ └────────────────────────────────────────────────────┘ │
│ ┌────────────────────────────────────────────────────┐ │
│ │ (B) Mô hình bị tràn bộ nhớ context window          │ │
│ └────────────────────────────────────────────────────┘ │
│ ┌────────────────────────────────────────────────────┐ │
│ │ (C) Mô hình sinh câu trả lời quá chậm              │ │
│ └────────────────────────────────────────────────────┘ │
│                                                        │
│ [💡 Xem gợi ý từ VLearn]                               │
└────────────────────────────────────────────────────────┘
```

#### B. Dạng Ghép Cặp (Matching) trên Mobile (Chuyển từ 2 cột sang dạng Thẻ Khối):
```
┌────────────────────────────────────────────────────────┐
│ [🟣 GHÉP CẶP TƯƠNG ỨNG]                                │
│ Chọn ý nghĩa phù hợp cho từng mệnh đề bên dưới:        │
├────────────────────────────────────────────────────────┤
│ 1. Zero-shot Prompting                                 │
│ ┌────────────────────────────────────────────────────┐ │
│ │ ▾ Chọn: [B] Đưa ra yêu cầu mà không kèm ví dụ mẫu  │ │ <-- Dropdown rộng 100%
│ └────────────────────────────────────────────────────┘ │
│                                                        │
│ 2. Few-shot Prompting                                  │
│ ┌────────────────────────────────────────────────────┐ │
│ │ ▾ Chọn: [A] Kèm 2-3 ví dụ mẫu để LLM bắt chước     │ │
│ └────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────┘
```
*(Khắc phục hoàn toàn lỗi co kéo 2 cột trước đây, 100% người dùng chạm chọn dễ dàng trên smartphone).*

#### C. Dạng Sắp Xếp Quy Trình (Ordering) trên Mobile:
- Tăng kích thước nút $\uparrow$ và $\downarrow$ lên $42\text{px} \times 42\text{px}$ để tránh ấn trượt.
- Hỗ trợ đổi thứ tự mượt mà, viền màu xanh lá khi đúng vị trí.

---

### 4. Thanh Điều Hướng Đáy Màn Hình Cố Định (Sticky Bottom Action Bar)
```
==========================================================
│   [ ◄ Câu trước ]   [  KIỂM TRA ĐÁP ÁN  ]   [ Tiếp ► ]  │  <-- Luôn ghim ở đáy
==========================================================
```
- **Vị trí:** Luôn nổi ở đáy màn hình điện thoại (`position: fixed; bottom: 0; z-index: 100;`).
- **Nút trung tâm (CTA Chính):**
  - Trạng thái chưa làm: `[ KIỂM TRA ĐÁP ÁN ]` (Nút to màu xanh dương đậm hoặc xanh lá).
  - Trạng thái đã kiểm tra / Chế độ ôn thi: Nút chuyển thành `[ CÂU TIẾP THEO ► ]`.
  - Trạng thái câu tự luận: `[ 💡 LẬT XEM LỜI GIẢI & RUBRIC ]`.
- **Hỗ trợ Safe Area:** Thêm `padding-bottom: max(12px, env(safe-area-inset-bottom))` để không bị cấn thanh vuốt Home của iPhone.

---

## V. Kế Hoạch Triển Khai Kỹ Thuật Chi Tiết (5 Bước)

### Bước 1: Khai Báo Media Queries & Hệ Thống Biến Giao Diện Trong `index.css`
- **Breakpoints chuẩn:**
  - Mobile nhỏ: `@media (max-width: 480px)` (iPhone SE, Galaxy A series).
  - Mobile tiêu chuẩn & Phablet: `@media (max-width: 768px)` (iPhone 13/14/15/16, Pixel, Xiaomi).
  - Tablet: `@media (min-width: 769px) and (max-width: 1024px)`.
  - Desktop: `@media (min-width: 1025px)`.
- **Thiết lập Safe Area & Touch Action:**
  - Chống phóng to vô tình khi double-tap: `touch-action: manipulation;`.
  - Font size input $\ge 16\text{px}$ để ngăn iOS tự động zoom màn hình khi gõ số.

### Bước 2: Tái Cấu Trúc Header & Bổ Sung Drawer Menu Cho Sidebar
- **Header:**
  - Desktop: Giữ nguyên bố cục thanh ngang đầy đủ.
  - Mobile ($\le 768\text{px}$): Thu gọn chỉ còn `Logo` + `Day Indicator Badge` + `Nút Drawer [☰]` + `Nút Thao tác [⋯]`.
- **Sidebar Drawer (`.sidebar-drawer`):**
  - Trạng thái mở/đóng quản lý bằng state React: `const [isSidebarOpen, setIsSidebarOpen] = useState(false)`.
  - Hiệu ứng trượt mượt mà với CSS `transform: translateX(-100%)` $\rightarrow$ `translateX(0)`.
  - Backdrop tối mờ (`background: rgba(0,0,0,0.5)`) có thể chạm ra ngoài để đóng.

### Bước 3: Quy Hoạch Lại Các Nút Chức Năng Của Quiz
- Tạo component `QuizMobileToolbar`:
  - Dòng 1: Tabs cuộn ngang chọn kho đề (`standard`, `expanded`, `essay`, `wrong`, `all_wrong`).
  - Dòng 2: Mini bar hiển thị tóm tắt tiến độ + Toggle Chế độ ôn thi dạng công tắc nhỏ.
  - Dòng 3: Chip lọc câu hỏi vuốt ngang.
- Tạo Modal/Bottom Sheet cho Lưới số câu hỏi:
  - Khi người dùng cần nhảy câu, bấm nút `[☷]` sẽ mở Bottom Sheet với lưới nút câu hỏi to rõ ràng ($44\text{px} \times 44\text{px}$), dễ nhìn và dễ ấn.
- Menu thao tác phụ (`MoreActionsModal`):
  - Chuyển các nút ít dùng (Tải Excel, Tải Zip, Tải txt, Hiện hết đáp án, Reset) vào đây.

### Bước 4: Tối Ưu Từng Dạng Tương Tác Câu Hỏi (Question Interactions)
- **Matching:**
  - CSS `@media (max-width: 768px)` chuyển `.matching-pair-row` thành `display: flex; flex-direction: column; align-items: stretch;`.
  - Select box có `width: 100%`, font size $15\text{px}$, padding $12\text{px}$.
- **Ordering:**
  - Đảm bảo khoảng cách nút di chuyển không bị dính vào text câu trả lời.
- **Choices (Single & Multi):**
  - Căn lề padding hợp lý, icon chữ cái A, B, C to rõ, nhãn `[✓ Đáp án đúng]` đưa xuống góc dưới hoặc đầu thẻ để không đè vào chữ của phương án trên màn hình hẹp.

### Bước 5: Cài Đặt Sticky Bottom Action Bar
- Thêm container `.mobile-sticky-action-bar` hiển thị ở màn hình $\le 768\text{px}$.
- Thêm padding phụ cho `.quiz-screen` (`padding-bottom: 90px`) để nội dung câu hỏi cuối trang không bị thanh bar che khuất khi cuộn kịch sàn.
- Kiểm thử thực tế trên DevTools với các thiết bị:
  - iPhone 14 / 15 / 16 (390 x 844 px)
  - Samsung Galaxy S20 / S22 / S24 (360 x 800 px)
  - iPad Mini / Air (768 x 1024 px)

---

## VI. Tiêu Chí Nghiệm Thu (Acceptance Criteria)

- [ ] **Không tràn ngang (No Horizontal Scroll):** Màn hình từ $320\text{px}$ trở lên không xuất hiện thanh cuộn ngang ngoài ý muốn.
- [ ] **Touch Target $\ge 44\text{px}$:** Tất cả các nút bấm, ô chọn đáp án, item chuyển Day đều có chiều cao chạm tối thiểu $44\text{px}$.
- [ ] **Tốc độ làm bài tăng:** Người dùng có thể chuyển câu, kiểm tra đáp án liên tục chỉ bằng ngón tay cái mà không cần cuộn trang lên xuống.
- [ ] **Không gian nội dung tối đa:** $75\% - 85\%$ màn hình dành cho câu hỏi và đáp án, các nút điều khiển phụ được giấu gọn gàng.
- [ ] **Hoạt động trơn tru trên cả iOS Safari và Chrome Android.**

---
*Kế hoạch được lập ngày 18/10/2026 bởi Antigravity AI Coding Assistant dành cho VLearn App.*
