# -*- coding: utf-8 -*-
"""
Day 07 Part 2: Questions 24 to 45 (d07-q063 to d07-q087)
"""

DAY_07_PART2 = {
    "d07-q063": {
        "sample_answer": (
            "1. Đánh giá tính hữu dụng của bộ lọc (Metadata Filter Utility Assessment):\n"
            "- Hiệu quả tăng độ chính xác (Precision Gain): Bộ lọc `audience=student` đã nâng số lượng bản ghi liên quan trong top-3 từ 2 lên 3 bản ghi (tăng Precision@3 từ 66.7% lên 100% đối với các tài liệu có gắn thẻ). Bộ lọc hoạt động hoàn hảo về mặt logic phân loại.\n"
            "- Tổn hại về độ bao phủ (Recall Trade-off / False Negative): Bộ lọc vô tình loại bỏ một chính sách đúng và có giá trị cao chỉ vì bản ghi đó bị khuyết thiếu trường metadata `audience` (Missing Metadata Defect).\n"
            "2. Phân định ranh giới lỗi:\n"
            "Cần tách bạch rõ ràng: Logic lọc của truy vấn là hoàn toàn đúng đắn; lỗi cốt lõi nằm ở **tầng chất lượng dữ liệu và độ bao phủ metadata (Data Ingestion Coverage Defect)** chứ không phải lỗi của thuật toán lọc.\n"
            "3. Quyết định bước xử lý tiếp theo:\n"
            "- Bước 1 (Sửa dữ liệu nguồn): Chạy pipeline kiểm tra và điền bù metadata (Metadata Backfill & Imputation) cho toàn bộ các bản ghi bị thiếu trường `audience` trong kho dữ liệu.\n"
            "- Bước 2 (Chính sách lọc an toàn tạm thời): Trong khi chờ dữ liệu được làm sạch hoàn toàn, triển khai logic lọc nới lỏng: `WHERE audience = 'student' OR audience IS NULL` hoặc gán nhãn mặc định `audience='all'` cho các tài liệu công khai."
        ),
        "explanation": (
            "Một bộ lọc metadata chỉ có thể phát huy tối đa giá trị khi tỷ lệ bao phủ của metadata đạt 100%. Lỗi thiếu metadata (Missing Tagging) "
            "trong quá trình nạp dữ liệu sẽ biến một bộ lọc đúng thành nguyên nhân gây đứt gãy thông tin (False Negatives). Cần phân biệt rõ lỗi logic của bộ lọc "
            "với lỗi chất lượng của dữ liệu đầu vào."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đánh giá Utility của bộ lọc] (1.5 điểm): Chỉ ra bộ lọc tăng Precision@3 lên 3/3 nhưng làm giảm Recall do loại bỏ chính sách thiếu thẻ.\n"
            "- [Tách biệt tầng lỗi] (1.0 điểm): Phân định dứt khoát lỗi thuộc về tầng chất lượng dữ liệu (metadata coverage) chứ không phải lỗi logic của bộ lọc.\n"
            "- [Kế hoạch hành động cụ thể] (1.5 điểm): Đưa ra 2 bước xử lý chuẩn xác: Backfill/chuẩn hóa dữ liệu nguồn và áp dụng điều kiện lọc an toàn tạm thời (OR audience IS NULL)."
        ),
        "reference_source": "Pinecone Documentation: 'Metadata Filtering Best Practices & Null Value Handling' (https://docs.pinecone.io/guides/data/filter-by-metadata)"
    },
    "d07-q065": {
        "sample_answer": (
            "1. Xác định lỗi sớm nhất trong chuỗi xử lý (Earliest Defect Localization):\n"
            "- Lỗi sớm nhất nằm ở **Tầng Trích xuất Dữ liệu (Document Extraction Layer)**.\n"
            "- Cụ thể: Bộ trích xuất văn bản (Text Parser / PDF Extractor) đã làm mất hoàn toàn bảng dữ liệu chứa câu trả lời chuẩn (Gold Answer). Các tầng phía sau (Chunking, Embedding, Vector Search, Generator) hoạt động hoàn toàn bình thường dựa trên dữ liệu đã nhận, nhưng vì dữ liệu đầu vào đã bị rỗng phần bảng nên việc Generator trả 'không có thông tin' là phản ứng hoàn toàn chính xác.\n"
            "2. Phương án thay thế kỹ thuật (Alternative Extraction Strategy):\n"
            "- Thay thế bộ parser văn bản thô bằng Bộ trích xuất nhận biết bố cục và bảng biểu chuyên dụng (Layout-Aware / Table-Aware Parser, ví dụ: Unstructured.io với mô hình `hi_res`, Azure Document Intelligence Layout API, Camelot, hoặc pdfplumber).\n"
            "- Trích xuất bảng thành định dạng có cấu trúc giữ nguyên mối liên hệ hàng - cột (Markdown Table, HTML Table hoặc cấu trúc JSON key-value) kèm tiêu đề ngữ cảnh của bảng.\n"
            "3. Quy trình chạy lại và xác minh (Rerun & Verification Workflow):\n"
            "- Chạy lại trích xuất văn bản cho tài liệu nguồn với parser mới -> Kiểm tra trực quan xem bảng dữ liệu đã có trong văn bản sau trích xuất chưa.\n"
            "- Re-chunk và Re-embed tài liệu vào Vector Store -> Thực hiện lại truy vấn tìm kiếm và kiểm tra xem đoạn ngữ cảnh chứa bảng có lọt vào Top-K và LLM có trả lời chính xác dữ kiện chuẩn hay không."
        ),
        "explanation": (
            "Nguyên tắc 'Garbage In, Garbage Out' trong RAG: nếu thông tin bị thất thoát ngay từ bước trích xuất ban đầu, không có bất kỳ kỹ thuật "
            "prompt engineering hay mô hình LLM tiên tiến nào có thể phục hồi được thông tin đó. Việc chẩn đoán lỗi phải lần ngược từ nguồn qua từng "
            "artifact trung gian để định vị chính xác mắt xích đứt gãy sớm nhất."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Xác định đúng lỗi sớm nhất] (1.5 điểm): Xác định chính xác lỗi nằm ở Tầng Trích xuất Tài liệu (Document Parser làm mất bảng), không đổ lỗi cho Generator.\n"
            "- [Phương án kỹ thuật thay thế] (1.5 điểm): Đề xuất sử dụng Layout-aware parser / Table extractor xuất ra bảng Markdown/HTML bảo toàn cấu trúc.\n"
            "- [Quy trình Rerun & Kiểm tra] (1.0 điểm): Mô tả rõ quy trình chạy lại từ trích xuất, re-index đến kiểm tra xác minh câu trả lời của mô hình."
        ),
        "reference_source": "Unstructured Documentation: 'Extracting Tables from PDF Documents' & LlamaIndex 'PDF Table Extraction Guides'"
    },
    "d07-q066": {
        "sample_answer": (
            "1. Chẩn đoán nguyên nhân lỗi (Root Cause Diagnosis):\n"
            "- Kết quả chạy không lọc đưa bản ghi đáp án chuẩn lên hạng 1 chứng minh rằng: Mô hình embedding, chiến lược chunking và thuật toán tìm kiếm vector hoạt động hoàn toàn chính xác về mặt ngữ nghĩa.\n"
            "- Lỗi xảy ra hoàn toàn do **Cấu hình sai điều kiện lọc thẩm quyền (Eligibility Filter Misconfiguration)**: Người truy vấn muốn tìm chính sách cho học viên kỳ `semester=2026`, nhưng tham số gửi vào bộ lọc metadata lại bị gán cứng là `semester=2025` (`department=engineering, semester=2025`). Vì bản ghi đúng có `semester=2026`, bộ lọc tiền truy vấn (pre-filter) đã loại bỏ bản ghi này ngay từ bước sàng lọc, dẫn đến kết quả trả về bị rỗng.\n"
            "2. Phép kiểm tra hoặc cách sửa tối thiểu (Minimal Fix & Verification Test):\n"
            "- Cách sửa tối thiểu trong mã nguồn/API: Cập nhật tham số truy vấn của bộ lọc để lấy động từ ngữ cảnh phiên của người dùng hoặc cho phép giá trị khớp với kỳ yêu cầu: `filter = {\"department\": \"engineering\", \"semester\": \"2026\"}`.\n"
            "- Phép kiểm tra hồi quy (Regression Test): Thiết lập bài kiểm thử tự động (Unit Test / Integration Test) xác nhận rằng tham số lọc `semester` trong query payload luôn được ánh xạ tự động từ thuộc tính học kỳ hiện tại của sinh viên (`user_session.target_semester`), không bị hardcode giá trị quá khứ."
        ),
        "explanation": (
            "Khi việc tìm kiếm không lọc (unfiltered retrieval) cho kết quả hoàn hảo nhưng tìm kiếm có lọc lại trả về rỗng, lỗi 100% thuộc về tầng "
            "điều phối bộ lọc (Eligibility / Metadata Filter Layer). Cần kiểm tra mapping giữa biến môi trường/người dùng và tham số query payload."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán chính xác nguyên nhân] (1.5 điểm): Chỉ ra việc gán cứng sai tham số lọc semester=2025 đã triệt tiêu bản ghi đúng có semester=2026.\n"
            "- [Chứng minh tầng retrieval hoạt động tốt] (1.0 điểm): Khẳng định tầng embedding và vector search đúng vì unfiltered đạt hạng 1.\n"
            "- [Cách sửa tối thiểu & Phép kiểm tra] (1.5 điểm): Đưa ra cách sửa đúng tham số semester=2026 và viết test kiểm tra mapping tham số từ session."
        ),
        "reference_source": "Qdrant Documentation: 'Payload Based Filtering & Debugging Empty Search Results' (https://qdrant.tech/documentation/)"
    },
    "d07-q068": {
        "sample_answer": (
            "1. Thiết kế Bảng Thí nghiệm Có kiểm soát (Controlled Experiment Table):\n"
            "Thực nghiệm được chạy trên cùng một tài liệu Handbook đóng băng với tập 50 câu hỏi thử nghiệm chuẩn hóa được phân loại thành 2 nhóm query:\n"
            "| Chiến lược Chunking | Kích thước & Tham số | Recall@5 Toàn cục | Recall@5 Nhóm Ngoại lệ (25 queries) | Recall@5 Nhóm Định nghĩa chung (25 queries) | Độ trễ p95 (ms) | Dung lượng Vector Store |\n"
            "|---|---|---|---|---|---|---|\n"
            "| Baseline: Fixed Window | `chunk_size=300`, `overlap=50` | 0.81 | 0.68 | 0.94 | 42 ms | 1.200 vectors |\n"
            "| Candidate: Heading Section | Chia theo `#`, `##`, `###` (dynamic) | 0.84 | 0.92 | 0.76 | 48 ms | 850 vectors |\n"
            "2. Quy tắc Quyết định Không thổi phồng (Objective Decision Rule):\n"
            "- Không tuyên bố 'Chiến lược Heading vượt trội toàn diện': Bảng số liệu cho thấy rõ tính chất đánh đổi (Trade-off). Chiến lược Heading thắng áp đảo ở nhóm câu hỏi về ngoại lệ và quy định lồng nhau (0.92 vs 0.68), nhưng lại kém hơn Fixed-300 ở các câu hỏi định nghĩa ngắn (0.76 vs 0.94) do các mục định nghĩa nhỏ bị gộp thành chunk lớn chứa nhiều từ ngữ thừa.\n"
            "- Quy tắc nghiệm thu triển khai:\n"
            "  + Nếu ứng dụng ưu tiên cao nhất về tính chính xác của các điều khoản ngoại lệ học vụ: Chọn Chiến lược Heading Section Chunking.\n"
            "  + Hướng đi tiếp theo: Triển khai chiến lược kết hợp (Hybrid Chunking: Heading splitting cho phần chính sách, Fixed splitting cho phần bảng thuật ngữ/FAQ) để tối ưu hóa cả hai nhóm truy vấn."
        ),
        "explanation": (
            "Trong nghiên cứu thực nghiệm AI, việc kết luận một chiến lược 'tốt hơn toàn diện' dựa trên chỉ số trung bình tổng thể là một lỗi thiên vị nguy hiểm "
            "(Aggregation Bias). Cần phân rã hiệu năng theo từng nhóm truy vấn chuyên biệt (Query Classes) để thấy rõ ưu - nhược điểm và ra quyết định kiến trúc "
            "dựa trên trọng số nghiệp vụ thực tế."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế bảng thực nghiệm đa chiều] (1.5 điểm): Xây dựng bảng so sánh đầy đủ các tham số, tách biệt chỉ số tổng thể với từng nhóm query (ngoại lệ vs định nghĩa).\n"
            "- [Phân tích đánh đổi khách quan] (1.5 điểm): Không overclaim; chỉ rõ Heading chunking thắng ở câu hỏi ngoại lệ nhưng thua ở câu hỏi ngắn/định nghĩa.\n"
            "- [Quy tắc quyết định kỹ thuật] (1.0 điểm): Đưa ra decision rule dựa trên ưu tiên nghiệp vụ và đề xuất giải pháp kết hợp."
        ),
        "reference_source": "LangChain Documentation: 'Evaluating Different Chunking Strategies' & Ragas Benchmarking Guidelines"
    },
    "d07-q069": {
        "sample_answer": (
            "1. Hoàn thiện danh mục quyết định cho bốn nguồn dữ liệu (Data Inventory Decisions):\n"
            "- Nguồn 1 (Tài liệu kỹ thuật công khai có giấy phép rõ ràng):\n"
            "  + Quyết định: **Được duyệt lập chỉ mục (APPROVED TO INDEX)**.\n"
            "  + Căn cứ: Bản quyền công khai rõ ràng, phục vụ trực tiếp kiến thức kỹ thuật, không chứa thông tin riêng tư.\n"
            "- Nguồn 2 (Xuất dữ liệu CRM chứa số điện thoại nhưng chưa duyệt):\n"
            "  + Quyết định: **TỪ CHỐI / CHẶN TUYỆT ĐỐI (REJECTED / BLOCKED)**.\n"
            "  + Căn cứ: Vi phạm bảo mật thông tin cá nhân (PII - Phone numbers) và chưa được Data Owner phê duyệt. Việc nạp dữ liệu này vào Vector Store vi phạm nghiêm trọng quy định bảo vệ dữ liệu (GDPR/Nghị định 13) và đối mặt nguy cơ rò rỉ dữ liệu.\n"
            "- Nguồn 3 (Nhật ký thay đổi do Engineering sở hữu, cập nhật mỗi phát hành):\n"
            "  + Quyết định: **ĐƯỢC DUYỆT CÓ ĐIỀU KIỆN (APPROVED WITH AUTOMATION)**.\n"
            "  + Căn cứ: Có chủ quản rõ ràng (Engineering), dữ liệu chính thống. Cần thiết lập webhook tự động cập nhật và thu hồi phiên bản cũ trong index.\n"
            "- Nguồn 4 (Thư mục cá nhân không rõ nguồn gốc):\n"
            "  + Quyết định: **TỪ CHỐI HOÀN TOÀN (REJECTED / QUARANTINED)**.\n"
            "  + Căn cứ: Thiếu tính minh chứng xuất xứ (Untracked Provenance), không xác minh được bản quyền và độ tin cậy.\n"
            "2. Điểm chặn kiểm soát trước khi lập chỉ mục (Pre-indexing Ingestion Gate):\n"
            "Thiết lập cổng kiểm soát tự động tại Ingestion Pipeline bắt buộc kiểm tra 3 điều kiện: (1) Nguồn có trong Danh mục Nguồn được phê duyệt (Whitelisted Sources); (2) Đã quét tự động không phát hiện PII (PII Scanning Check); (3) Có metadata xác định rõ Data Owner và Ngày có hiệu lực."
        ),
        "explanation": (
            "Quản trị dữ liệu (Data Governance) cho hệ thống RAG đòi hỏi nguyên tắc 'Chỉ vì đọc được không có nghĩa là được phép lập chỉ mục'. "
            "Dữ liệu đưa vào vector store phải có nguồn gốc hợp pháp, không vi phạm PII và có chủ quản rõ ràng để đảm bảo an toàn pháp lý và chất lượng tri thức."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định chuẩn xác cho 4 nguồn] (2.0 điểm): Đưa ra quyết định đúng cho từng nguồn: duyệt nguồn 1 và 3; từ chối dứt khoát nguồn 2 (chứa PII, chưa duyệt) và nguồn 4 (không rõ nguồn gốc).\n"
            "- [Căn cứ pháp lý & an toàn thông tin] (1.0 điểm): Nêu rõ lý do về bảo vệ dữ liệu cá nhân (PII) và trách nhiệm của Data Owner.\n"
            "- [Thiết kế cổng chặn Pre-indexing Gate] (1.0 điểm): Định nghĩa cổng kiểm soát tự động với whitelist, quét PII và kiểm tra metadata trước khi index."
        ),
        "reference_source": "NIST AI Risk Management Framework (AI RMF 1.0): 'Data Governance and Information Integrity' & OWASP Top 10 for LLM: LLM06"
    },
    "d07-q070": {
        "sample_answer": (
            "1. Thiết kế ranh giới thu thập dữ liệu (Collection Boundaries):\n"
            "- Ranh giới được phép (In-scope / Authorized Boundary):\n"
            "  + 6 trang hướng dẫn công khai: Được phép thu thập và lập chỉ mục.\n"
            "  + 2 tệp PDF công khai có gắn version: Được phép tải về, ghi nhận hash và số phiên bản phát hành.\n"
            "- Ranh giới cấm vượt quyền (Out-of-scope / Forbidden Boundary):\n"
            "  + Trang yêu cầu đăng nhập: **Cấm tuyệt đối** việc sử dụng tài khoản cá nhân hoặc bypass màn hình đăng nhập để cào dữ liệu khi chưa có thỏa thuận cấp phép bằng văn bản từ chủ quản hệ thống.\n"
            "2. Sổ theo dõi nguồn gốc tài liệu (Source Provenance Registry):\n"
            "Tạo tệp theo dõi `provenance_manifest.json` ghi lại thông tin xác thực để bất kỳ kiểm toán viên nào cũng có thể tái tạo tập ngữ liệu một cách hợp pháp:\n"
            "```json\n"
            "[\n"
            "  {\n"
            "    \"source_id\": \"guide-01\",\n"
            "    \"source_url\": \"https://portal.edu.vn/guide-1\",\n"
            "    \"access_tier\": \"public\",\n"
            "    \"license\": \"CC-BY-4.0\",\n"
            "    \"retrieved_at\": \"2026-10-23T10:00:00Z\",\n"
            "    \"content_sha256\": \"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\",\n"
            "    \"version\": \"v2.1\"\n"
            "  }\n"
            "]\n"
            "```\n"
            "3. Cơ chế tái tạo độc lập (Independent Reproducibility):\n"
            "Kiểm toán viên chỉ cần chạy script tải tự động dựa trên manifest; script sẽ so khớp mã băm SHA256 và xác nhận không có bất kỳ lệnh gọi truy cập nào vượt qua hàng rào đăng nhập trái phép."
        ),
        "explanation": (
            "Tính minh chứng nguồn gốc (Source Provenance) là yêu cầu cốt lõi trong nghiên cứu và triển khai AI tuân thủ chuẩn mực đạo đức và pháp lý. "
            "Một kho ngữ liệu có giá trị kiểm định phải chứng minh được mọi tài liệu đều có xuất xứ rõ ràng, có bản quyền sử dụng hợp pháp và có thể "
            "tái tạo nguyên bản thông qua mã băm mật mã học (cryptographic hash)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Xác định đúng ranh giới thu thập] (1.5 điểm): Xác định thu thập 6 trang web và 2 PDF công khai; loại bỏ hoàn toàn trang yêu cầu đăng nhập vì chưa có quyền sử dụng.\n"
            "- [Đặc tả Sổ theo dõi Provenance] (1.5 điểm): Thiết kế schema manifest đầy đủ: URL, access_tier, license, timestamp, mã băm SHA256, version.\n"
            "- [Khả năng tái lập và kiểm toán độc lập] (1.0 điểm): Nêu rõ cơ chế kiểm chứng độc lập bằng hash và kiểm toán quyền truy cập."
        ),
        "reference_source": "W3C PROV-O: The PROV Ontology & IEEE Standard for Machine Learning Data Provenance"
    },
    "d07-q071": {
        "sample_answer": (
            "1. Các sửa đổi ĐƯỢC PHÉP dựa trên bằng chứng xác thực (Permitted Repairs):\n"
            "- Sửa ký tự nhận diện lỗi: Sửa `Top-k = S` thành `Top-k = 5`. Căn cứ: Ảnh nguồn gốc xác nhận rõ ràng ký tự đó là số `5` (có minh chứng thị giác không thể chối cãi).\n"
            "- Loại bỏ thành phần lặp phi ngữ nghĩa (Boilerplate Stripping): Xóa bỏ dòng footer 'Internal draft' lặp lại ở mọi trang vì đây là artifact của văn bản in ấn, không mang nội dung tri thức và gây loãng vector.\n"
            "2. Phần PHẢI GIỮ nguyên trạng thái bất định (Mandatory Uncertainty Retention):\n"
            "- Tiêu đề cột thứ hai của bảng: Vì tiêu đề bị che mất hoàn toàn trong ảnh nguồn, **tuyệt đối không được tự ý bịa đặt hoặc suy đoán** tên cột. Hệ thống bắt buộc phải giữ nhãn bất định, ví dụ: `[Cột 2: Không xác định / Bị che]` (Unlabeled Column).\n"
            "- Cấu trúc bảng xen kẽ: Tách các dòng xen kẽ thành 2 cột dữ liệu độc lập theo cấu trúc ô tương ứng, nhưng phần tiêu đề cột 2 phải được đánh dấu rõ là thiếu thông tin.\n"
            "3. Bằng chứng kiểm tra lại (Verification Evidence & Audit Trail):\n"
            "- Lưu trữ ảnh cắt vùng gốc (Image Crop ROI) của số `5` và vùng bị che của bảng vào thư mục kiểm toán kèm ghi chú tọa độ.\n"
            "- Trong metadata của chunk, lưu cờ: `{\"data_quality\": \"repaired\", \"repaired_fields\": [\"top_k_value\"], \"uncertain_fields\": [\"table_col2_header\"], \"source_roi\": \"page1_box2.png\"}`."
        ),
        "explanation": (
            "Trong xử lý dữ liệu phục vụ AI, nguyên tắc toàn vẹn dữ liệu nghiêm cấm việc suy diễn vô căn cứ khi trích xuất OCR lỗi. "
            "Chỉ được phép sửa đổi khi có bằng chứng đối chiếu trực tiếp từ ảnh gốc. Các vùng dữ liệu bị mất hoặc không thể đọc được bắt buộc phải được "
            "đánh dấu là 'không xác định' (explicit uncertainty) để tránh tạo ra ảo giác dây chuyền sang mô hình ngôn ngữ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Sửa đổi được phép có căn cứ] (1.5 điểm): Cho phép sửa 'Top-k = S' thành 5 vì có ảnh nguồn xác thực; cho phép xóa footer lặp 'Internal draft'.\n"
            "- [Giữ nguyên bất định cho vùng mất dữ liệu] (1.5 điểm): Cấm bịa tên tiêu đề cột 2 bị che; bắt buộc đánh dấu rõ trạng thái không xác định.\n"
            "- [Bằng chứng kiểm tra và vết kiểm toán] (1.0 điểm): Yêu cầu lưu giữ vùng ảnh cắt ROI và cờ metadata kiểm toán chất lượng."
        ),
        "reference_source": "Google SRE / Data Quality Principles: 'Handling Incomplete Data and OCR Error Correction' & ISO 8000 Data Quality Standards"
    },
    "d07-q072": {
        "sample_answer": (
            "1. Dựng biểu diễn chuẩn hóa để bảo toàn cấu trúc ngữ nghĩa (Normalized Representation):\n"
            "Chuyển đổi trang tài liệu sang cấu trúc tài liệu phân cấp dựa trên JSON-LD hoặc Markdown mở rộng có neo giữ phạm vi (Scoped Markdown):\n"
            "```markdown\n"
            "# Quy chế Hỗ trợ Tài chính Học tập\n"
            "\n"
            "## 1. Học bổng\n"
            "- **Điều kiện tiên quyết**: Chỉ áp dụng khi GPA >= 3.2.\n"
            "- **Danh mục các loại học bổng và mức hỗ trợ**:\n"
            "  | Loại học bổng | Mức hỗ trợ | Đối tượng |\n"
            "  |---|---|---|\n"
            "  | Xuất sắc | 100% học phí | Sinh viên GPA >= 3.6 |\n"
            "  | Giỏi | 50% học phí | Sinh viên GPA từ 3.2 đến 3.59 |\n"
            "\n"
            "## 2. Gia hạn thời gian nộp học phí\n"
            "- **Quy định**: Sinh viên có thể nộp đơn xin gia hạn tối đa 30 ngày kể từ hạn chót nộp học phí thông thường.\n"
            "```\n"
            "2. Giải pháp kỹ thuật ngăn chặn gán nhầm sang mục Gia hạn:\n"
            "- Ràng buộc thứ bậc phân cấp (Hierarchical Scope Binding): Đưa điều kiện 'GPA >= 3.2' và Bảng học bổng vào cùng một Node/Chunk con của Section `## 1. Học bổng`.\n"
            "- Metadata Scope Injection: Mỗi chunk sinh ra từ mục Học bổng đều được gắn thuộc tính `metadata = {\"section_title\": \"Học bổng\", \"section_id\": \"sec_scholarship\", \"applies_to\": \"scholarship_only\"}`.\n"
            "- Ngăn chặn đứt gãy do Layout trôi: Bộ parser phải tôn trọng ranh giới dòng của Section 1 trước khi bắt đầu đọc Section 2, tuyệt đối không dùng bộ trích xuất thuần túy theo tọa độ từ trên xuống dưới mà không nhận diện khối phân cấp."
        ),
        "explanation": (
            "Lỗi trôi nổi điều kiện (Floating Condition Defect) xảy ra khi bộ trích xuất văn bản phẳng (flat text extraction) làm đứt gãy mối liên kết giữa "
            "điều kiện áp dụng và chủ đề của nó, dẫn đến việc điều kiện của mục này bị gán sang mục khác nằm kế cận. Việc áp dụng biểu diễn phân cấp có "
            "cấu trúc (Scoped Hierarchy) là giải pháp dứt điểm để bảo tồn ngữ nghĩa nguyên bản."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Biểu diễn chuẩn hóa có phân cấp] (1.5 điểm): Xây dựng biểu diễn Markdown/JSON phân cấp rõ ràng 2 mục Học bổng và Gia hạn, gắn điều kiện GPA vào đúng mục Học bổng.\n"
            "- [Bảo toàn bảng biểu trong phạm vi mục] (1.0 điểm): Giữ nguyên bảng học bổng trong phạm vi của mục Học bổng.\n"
            "- [Cơ chế kỹ thuật chống nhầm lẫn] (1.5 điểm): Sử dụng scoped chunking và metadata injection để neo giữ phạm vi áp dụng, ngăn chặn việc gán nhầm sang mục Gia hạn."
        ),
        "reference_source": "LlamaIndex Documentation: 'Structured Document Parsers and Node Hierarchy' (https://docs.llamaindex.ai)"
    },
    "d07-q073": {
        "sample_answer": (
            "1. Phân loại và xử lý từng bản ghi theo quy ước metadata (Metadata Compliance Decision):\n"
            "- Bản ghi thứ ba (Có tiêu đề nhưng thiếu trường bắt buộc `source_url`):\n"
            "  + Quyết định: **TỪ CHỐI NHẬP KHO HOÀN TOÀN (REJECTED)**.\n"
            "  + Lý do: Vi phạm hợp đồng dữ liệu cơ bản (Missing Mandatory Field). `source_url` là trường định danh nguồn gốc bắt buộc để phục vụ trích dẫn và kiểm toán pháp lý. Thiếu nguồn gốc sẽ biến tài liệu thành 'unverified data'.\n"
            "- Hai bản ghi đầu (Cùng `doc_id=policy-9`, cùng `source_url`, cùng `document_version=v3`; một bản ghi dùng `department=CS`, bản ghi kia dùng `department=computer-science`):\n"
            "  + Quyết định: **ĐƯA VÀO VÙNG CHỜ CHUẨN HÓA (QUARANTINED FOR NORMALIZATION)**.\n"
            "  + Lý do: Xung đột tính duy nhất của khóa danh tính (Duplicate Primary Key Conflict) và không nhất quán về giá trị thuộc tính phân loại (Taxonomy Inconsistency).\n"
            "2. Yêu cầu chuẩn hóa và lý giải nguyên nhân kỹ thuật:\n"
            "- Chuẩn hóa Taxonomy mã phòng ban: Quy ước một tập giá trị đóng duy nhất (Controlled Vocabulary), chuẩn hóa `\"computer-science\"` thành `\"CS\"` (hoặc ngược lại tùy chuẩn hệ thống).\n"
            "- Xử lý trùng lặp khóa chính: Nếu đây là hai chunk khác nhau của cùng một tài liệu, phải bổ sung `chunk_index` vào khóa chính: `\"policy-9::chunk_0\"` và `\"policy-9::chunk_1\"`. Nếu là hai phiên bản gửi trùng, chỉ giữ bản ghi mới nhất sau khi đã chuẩn hóa mã khoa."
        ),
        "explanation": (
            "Trong kho lưu trữ vector, tính toàn vẹn của metadata phụ thuộc vào hai yếu tố: Khóa định danh duy nhất (Unique Identification) và Tập từ vựng được kiểm soát "
            "(Controlled Taxonomy). Sự thiếu nhất quán giữa 'CS' và 'computer-science' sẽ làm hỏng các truy vấn lọc phân loại chính xác, trong khi việc thiếu nguồn gốc "
            "làm mất khả năng truy vết trách nhiệm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định từ chối bản ghi thứ ba] (1.5 điểm): Xác định đúng việc từ chối bản ghi thứ 3 vì thiếu trường bắt buộc source_url.\n"
            "- [Đưa 2 bản ghi đầu vào vùng chờ] (1.0 điểm): Nhận diện xung đột trùng lặp khóa chính và không nhất quán giá trị thuộc tính department.\n"
            "- [Quy trình chuẩn hóa cụ thể] (1.5 điểm): Nêu rõ việc chuẩn hóa taxonomy (CS vs computer-science) và phân định chunk_index cho khóa chính."
        ),
        "reference_source": "Pinecone / Milvus Documentation: 'Vector Database Metadata Schema Constraints & Ingestion Quarantine'"
    },
    "d07-q074": {
        "sample_answer": (
            "1. Danh sách các câu được tách theo quy ước (Extracted Sentences):\n"
            "Quy ước nhận các dấu ngắt `. `, `! `, `? `, dấu chấm trước `\n` và dấu chấm ở cuối văn bản:\n"
            "- Câu 1: `\"Một.\"` (tách bởi `. `)\n"
            "- Câu 2: `\"Hai!\"` (tách bởi `! `)\n"
            "- Câu 3: `\"Ba?\"` (tách bởi `? `)\n"
            "- Câu 4: `\"Bốn.\"` (tách bởi dấu chấm ngay trước ký tự xuống dòng `\n`)\n"
            "- Câu 5: `\"Năm.\"` (tách bởi dấu chấm ở cuối đầu vào)\n"
            "Tổng cộng tách được chính xác **5 câu**.\n"
            "2. Các chunk đầu ra với `max_sentences_per_chunk = 3`:\n"
            "- Chunk 1: Chứa 3 câu đầu: `\"Một. Hai! Ba?\"`\n"
            "- Chunk 2: Chứa 2 câu còn lại: `\"Bốn. Năm.\"` (hoặc `\"Bốn.\nNăm.\"` tùy theo chính sách giữ nguyên định dạng xuống dòng).\n"
            "3. Ba điều kiện kiểm thử độc lập cho trường hợp biên (Edge Case Test Conditions):\n"
            "- Test Case 1 (Từ viết tắt và số thập phân): Văn bản chứa từ viết tắt như `\"TS. Nam đến lúc 14.50.\"`. Kiểm tra bộ tách câu không được coi dấu chấm sau `TS.` hoặc trong số `14.50` là ranh giới kết thúc câu.\n"
            "- Test Case 2 (Dấu kết thúc câu liên tiếp và khoảng trắng thừa): Văn bản chứa `\"Thật sao?! Tuyệt vời... Hết.\"` hoặc nhiều dấu xuống dòng `\n\n`. Kiểm tra không sinh ra câu rỗng (`\"\"`) và xử lý mượt mà chuỗi dấu câu phức.\n"
            "- Test Case 3 (Văn bản không có dấu ngắt câu hoặc chuỗi rỗng): Đầu vào là một chuỗi dài không có bất kỳ dấu kết thúc câu nào. Kiểm tra hệ thống không rơi vào vòng lặp vô tận và trả về một chunk duy nhất chứa toàn bộ chuỗi."
        ),
        "explanation": (
            "Sentence Boundary Chunker yêu cầu thuật toán nhận diện ranh giới câu (Sentence Boundary Disambiguation) chính xác trước khi thực hiện gom cụm. "
            "Các trường hợp biên về từ viết tắt, số thập phân và dấu câu lặp là những điểm yếu kinh điển của các bộ tokenizer đơn giản."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Liệt kê chính xác 5 câu] (1.5 điểm): Xác định đúng 5 câu tách biệt: 'Một.', 'Hai!', 'Ba?', 'Bốn.', 'Năm.'.\n"
            "- [Xác định đúng 2 chunk đầu ra] (1.0 điểm): Nhóm đúng Chunk 1 (3 câu đầu) và Chunk 2 (2 câu còn lại).\n"
            "- [3 điều kiện kiểm thử biên độc lập] (1.5 điểm): Đưa ra 3 test cases biên cụ thể: từ viết tắt/số thập phân, dấu câu kép/rỗng, và chuỗi không có dấu câu."
        ),
        "reference_source": "NLTK / spaCy Documentation: 'Sentence Boundary Disambiguation (SBD)' & LangChain SentenceTransformersTokenSplitter"
    },
    "d07-q075": {
        "sample_answer": (
            "1. Theo dõi các nhánh đệ quy (Recursive Splitting Trace):\n"
            "- Tham số: `size = 18`, separators: `[\"\\n\\n\", \"\\n\", \". \", \" \", \"\"]`.\n"
            "- Mục đầu vào dài 42 ký tự (không có `\\n\\n` và `\\n`), chuyển xuống separator thứ 3 là `\". \"`.\n"
            "- Bước 1: Tách bằng `\". \"` thành hai phần:\n"
            "  + Phần 1 (P1): Độ dài 12 ký tự <= 18 -> Đạt kích thước cho phép, không cần tách tiếp, đưa vào kết quả.\n"
            "  + Phần 2 (P2): Độ dài 28 ký tự > 18 -> Cần đệ quy tiếp với danh sách separator còn lại: `[\" \", \"\"]`.\n"
            "- Bước 2: Tách P2 bằng khoảng trắng `\" \"` thành hai phần:\n"
            "  + Phần 2a (P2a): Độ dài 14 ký tự <= 18 -> Đạt kích thước, đưa vào kết quả.\n"
            "  + Phần 2b (P2b): Độ dài 13 ký tự <= 18 -> Đạt kích thước, đưa vào kết quả.\n"
            "2. Danh sách các phần đầu ra theo đúng thứ tự:\n"
            "Thứ tự trả về: `[P1, P2a, P2b]` (độ dài tương ứng: 12, 14, 13 ký tự, tất cả đều <= 18).\n"
            "3. Bất biến bảo đảm thuật toán luôn kết thúc (Termination Invariant):\n"
            "Thuật toán bảo đảm dừng hữu hạn dựa trên hai đại lượng giảm đơn điệu nghiêm ngặt (Strictly Monotonic Decreasing Quantities):\n"
            "(a) Chiều dài của đoạn văn bản cần xử lý giảm sau mỗi lần phân tách thành công (`len(chunk) < len(parent)`);\n"
            "(b) Danh sách dấu phân tách (separators list) thu hẹp dần sau mỗi tầng đệ quy; khi rơi về separator rỗng `\"\"` (ký tự đơn lẻ), độ dài mỗi phần tử là 1 ký tự <= `size` (với `size >= 1`), bảo đảm thuật toán luôn chạm điều kiện dừng."
        ),
        "explanation": (
            "Thuật toán Recursive Character Text Splitter hoạt động bằng cách thử lần lượt các dấu phân tách có tính ngữ nghĩa cao nhất. "
            "Bất biến bảo đảm dừng của thuật toán đệ quy là sự kết hợp giữa việc giảm độ dài chuỗi và sự cạn kiệt của tập dấu phân tách, tránh lỗi tràn ngăn xếp (stack overflow)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Theo dõi nhánh đệ quy chính xác] (1.5 điểm): Mô tả đúng quy trình: tách P1 (12) và P2 (28) bằng '. ', sau đó tách P2 thành P2a (14) và P2b (13) bằng dấu cách.\n"
            "- [Liệt kê thứ tự đầu ra] (1.0 điểm): Liệt kê đúng thứ tự các phần tử: P1, P2a, P2b với kích thước đều thỏa mãn <= 18.\n"
            "- [Bất biến bảo đảm kết thúc] (1.5 điểm): Phát biểu rõ hai bất biến giảm: chiều dài chuỗi và tập phân tách cạn kiệt về ký tự đơn rỗng."
        ),
        "reference_source": "LangChain Source Code & Documentation: 'RecursiveCharacterTextSplitter Implementation Details' (https://python.langchain.com)"
    },
    "d07-q076": {
        "sample_answer": (
            "1. Thiết kế cấu trúc Chunk (Hierarchical Scoped Chunking):\n"
            "- Mục `### Điều kiện` dài vượt ngân sách kích thước được chia thành các chunk con bằng Recursive Separator: `Chunk_Cond_1`, `Chunk_Cond_2`.\n"
            "- Ghi chú ngoại lệ ở cuối tạo thành một chunk riêng biệt: `Chunk_Exception` (hoặc gắn kèm vào chunk điều kiện liền kề nếu kích thước cho phép).\n"
            "2. Thiết kế Metadata bảo toàn phạm vi phân cấp (Metadata Breadcrumb Contract):\n"
            "Mỗi chunk sinh ra đều được gắn trường metadata có cấu trúc bảo toàn cây phả hệ tiêu đề:\n"
            "```json\n"
            "{\n"
            "  \"chunk_id\": \"admissions::scholarship::exception_01\",\n"
            "  \"ancestor_headings\": [\"Tuyển sinh\", \"Học bổng\", \"Điều kiện\"],\n"
            "  \"breadcrumb\": \"Tuyển sinh > Học bổng > Điều kiện > Ngoại lệ\",\n"
            "  \"section_scope\": \"scholarship\",\n"
            "  \"is_exception\": true,\n"
            "  \"context_prefix\": \"[Tuyển sinh - Học bổng - Điều kiện - Ghi chú ngoại lệ]: \"\n"
            "}\n"
            "```\n"
            "3. Cơ chế giúp truy vấn ngoại lệ tìm đúng phạm vi:\n"
            "- Bổ sung Tiền tố ngữ cảnh (Contextual Chunk Enrichment): Chèn chuỗi `breadcrumb` vào đầu nội dung chunk trước khi đưa vào mô hình embedding. Khi người dùng hỏi 'Ngoại lệ điều kiện học bổng', vector của chunk sẽ khớp chính xác nhờ có từ khóa 'Học bổng' và 'Điều kiện'.\n"
            "- Lọc trước theo phạm vi (Pre-filtering): Cho phép hệ thống áp dụng bộ lọc `section_scope = 'scholarship'` để ngăn chặn việc trả về ngoại lệ của mục `Hồ sơ`."
        ),
        "explanation": (
            "Khi tài liệu phân cấp sâu bị chia nhỏ, các đoạn văn bản phía dưới (đặc biệt là các ghi chú ngoại lệ ngắn) sẽ mất hoàn toàn ngữ cảnh cha nếu "
            "không được kế thừa tiêu đề. Việc chèn chuỗi đường dẫn (Breadcrumb Injection) vào cả nội dung văn bản và metadata là kỹ thuật chuẩn công nghiệp "
            "giúp mô hình vector và LLM hiểu chính xác phạm vi áp dụng của ngoại lệ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế chia chunk hợp lý] (1.0 điểm): Chia mục Điều kiện vượt kích thước thành các sub-chunk và giữ ngoại lệ thành chunk có neo giữ.\n"
            "- [Đặc tả Metadata phân cấp đầy đủ] (1.5 điểm): Thiết kế metadata chứa ancestor_headings, breadcrumb, section_scope và is_exception.\n"
            "- [Cơ chế truy vấn đúng phạm vi] (1.5 điểm): Nêu giải pháp contextual prefix enrichment và bộ lọc phạm vi để truy vấn ngoại lệ không bị nhầm sang mục khác."
        ),
        "reference_source": "LlamaIndex Documentation: 'Node Parser with Metadata & Sub-Question Retrieval' & Anthropic: 'Contextual Retrieval'"
    },
    "d07-q077": {
        "sample_answer": (
            "1. Kiểm tra và chỉ ra các sai phạm trong phép so sánh (Flaw Identification):\n"
            "- Sai phạm 1 (Bất bình đẳng dữ liệu đầu vào / Uncontrolled Input Baseline): Cửa sổ cố định chạy trên văn bản thô 960 ký tự, trong khi hai chiến lược còn lại chạy trên văn bản đã làm sạch 900 ký tự. Sự chênh lệch 60 ký tự (chứa nhiễu hoặc khoảng trắng) làm sai lệch hoàn toàn số lượng chunk và độ dài trung bình, khiến kết quả so sánh vô giá trị khoa học.\n"
            "- Sai phạm 2 (Thiếu tính kiểm chứng / Không lưu giữ Chunk Artifacts): Đầu ra chỉ báo 2 con số tổng kết (số lượng, độ dài trung bình) mà không lưu lại danh sách các chunk thực tế được tạo ra. Không thể kiểm tra được chất lượng ngữ nghĩa, điểm cắt có gãy câu hay không và mức độ toàn vẹn của thông tin.\n"
            "2. Thiết kế lần chạy lại có kiểm soát tối thiểu (Minimal Controlled Re-run):\n"
            "- Bước 1 (Chuẩn hóa đầu vào): Chọn duy nhất một phiên bản văn bản đã được làm sạch chuẩn (900 ký tự) làm đầu vào cố định cho cả ba chiến lược.\n"
            "- Bước 2 (Cố định siêu tham số ngân sách): Thiết lập cùng một kích thước chunk mục tiêu (ví dụ `target_size = 150` ký tự, `overlap = 30` ký tự nếu áp dụng).\n"
            "- Bước 3 (Lưu trữ và đối chiếu Artifact): Lưu toàn bộ danh sách các chunk đầu ra của từng chiến lược vào tệp JSON: `{strategy, chunk_index, text, char_length, token_length}`.\n"
            "- Bước 4 (Đánh giá đa chiều): Ngoài số lượng và độ dài trung bình, bổ sung các phép đo: Số lượng câu bị cắt ngang (Broken Sentence Count) và Độ tương đồng ngữ nghĩa nội tại."
        ),
        "explanation": (
            "Một phép so sánh khoa học phải tuân thủ nghiêm ngặt nguyên tắc đối chứng chuẩn (Controlled Experiment Baseline): cùng dữ liệu đầu vào, "
            "cùng quy chuẩn tiền xử lý và lưu giữ đầy đủ hiện vật đầu ra (artifacts) để phục vụ kiểm toán độc lập và tái lập kết quả."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chỉ rõ lỗi không cùng dữ liệu đầu vào] (1.5 điểm): Nhận diện sự sai lệch nghiêm trọng khi so sánh trên văn bản thô 960 ký tự và văn bản sạch 900 ký tự.\n"
            "- [Chỉ rõ lỗi thiếu Artifacts đầu ra] (1.0 điểm): Nêu rõ việc không lưu giữ các chunk thực tế khiến không thể kiểm chứng chất lượng cắt câu.\n"
            "- [Thiết kế lần chạy lại chuẩn hóa] (1.5 điểm): Cố định tập dữ liệu sạch 900 ký tự cho cả 3 chiến lược, lưu trữ đầy đủ artifacts và bổ sung metric đánh giá ranh giới ngữ nghĩa."
        ),
        "reference_source": "Google SRE / ML Engineering: 'Reproducibility and Controlled Experimentation in ML Pipelines'"
    },
    "d07-q078": {
        "sample_answer": (
            "1. Theo dõi luồng xử lý chi tiết (Pipeline Execution Flow Tracing):\n"
            "- Giai đoạn 1 (Tokenization): Văn bản gốc tạo ra 12 tokens: `[T_0, T_1, ..., T_11]`.\n"
            "- Giai đoạn 2 (Truncation Pipeline): Pipeline phát hiện giới hạn đầu vào của embedder là 8 tokens. Hệ thống thực hiện cắt cụt (truncation), chỉ giữ lại 8 tokens đầu tiên: `[T_0, ..., T_7]`; bốn tokens cuối `[T_8, T_9, T_10, T_11]` bị loại bỏ vĩnh viễn ngay tại đây.\n"
            "- Giai đoạn 3 (Transformer Encoder Forward Pass): Bộ mã hóa chỉ nhận 8 tokens, sinh ra 8 vector trạng thái ẩn tương ứng: `[h_0, h_1, ..., h_7]` (mỗi vector có số chiều `d`).\n"
            "- Giai đoạn 4 (Mean-Pooling): Tính toán vector trung bình: `v_mean = (1/8) * sum_{i=0..7} h_i`.\n"
            "- Giai đoạn 5 (L2 Normalization): Chuẩn hóa L2: `v_norm = v_mean / ||v_mean||_2` để đưa độ dài vector về 1.\n"
            "2. Thông tin bị thất thoát trước khi vector được tạo ra:\n"
            "- **Thông tin bị mất vĩnh viễn ở Giai đoạn 2 (Truncation)**: Toàn bộ nội dung ngữ nghĩa, từ khóa và các thực thể nằm trong 4 tokens cuối `[T_8, T_9, T_10, T_11]` bị mất hoàn toàn. Bộ mã hóa và các bước mean-pool phía sau hoàn toàn 'mù' đối với 4 tokens này.\n"
            "- **Thông tin bị nén mờ ở Giai đoạn 4 (Mean-pooling)**: Bước gộp trung bình làm mất thứ tự tuần tự (word order) và các mối quan hệ tương tác tinh tế giữa các từ trong 8 tokens còn lại."
        ),
        "explanation": (
            "Quá trình sinh vector embedding trải qua nhiều biến đổi làm suy hao thông tin. Trong đó, việc cắt cụt token (Truncation) là nguyên nhân gây thất thoát "
            "thông tin nghiêm trọng nhất vì nó hoàn toàn loại bỏ một phần văn bản khỏi sự chú ý của mô hình. Cần đảm bảo kích thước chunking luôn nhỏ hơn "
            "ngưỡng `max_seq_length` của bộ mã hóa."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Theo dõi chuẩn xác 5 giai đoạn luồng] (1.5 điểm): Mô tả đúng tuần tự: Tokenize (12 tokens) -> Truncate (còn 8) -> Encode (8 states) -> Mean-pool -> Normalize.\n"
            "- [Chỉ rõ vị trí mất thông tin sớm nhất] (1.5 điểm): Xác định chính xác 4 token cuối bị mất ngay tại bước Truncation trước khi đưa vào encoder.\n"
            "- [Phân tích tác động của Mean-pooling] (1.0 điểm): Nêu rõ việc mean-pooling nén phẳng các trạng thái và làm mờ cấu trúc vị trí từ."
        ),
        "reference_source": "Hugging Face Transformers Documentation: 'BertTokenizer Truncation and Sentence Embeddings Mean Pooling'"
    },
    "d07-q080": {
        "sample_answer": (
            "1. Thiết kế Bản ghi Danh tính (Record Identity Contract):\n"
            "Khóa chính (Primary Key / Record ID) phải là sự kết hợp duy nhất giữa mã tài liệu, phiên bản và chỉ số chunk: `\"{doc_id}::{version}::{chunk_index}\"`.\n"
            "- Chunk thuộc v2: `\"policy_admission::v2::chunk_0\"`\n"
            "- Chunk thuộc v3: `\"policy_admission::v3::chunk_0\"`\n"
            "2. Thiết kế Metadata có cấu trúc (Structured Metadata Schema):\n"
            "```json\n"
            "{\n"
            "  \"doc_id\": \"policy_admission\",\n"
            "  \"version\": \"v3\",\n"
            "  \"is_active\": true,\n"
            "  \"effective_date\": \"2026-09-01\",\n"
            "  \"supersedes\": \"v2\",\n"
            "  \"source_url\": \"https://edu.vn/policies/v3.pdf\"\n"
            "}\n"
            "```\n"
            "3. Cơ chế tìm kiếm, trích dẫn và quản lý vòng đời không trộn lẫn:\n"
            "- Khi tìm kiếm (Search Isolation): Sử dụng Metadata Pre-filtering bắt buộc `WHERE is_active = true` (hoặc phân vùng theo Namespace/Collection `policies_v3`), đảm bảo chỉ có bản ghi của v3 được xếp hạng.\n"
            "- Khi trích dẫn (Citation Traceability): LLM trích dẫn kèm số phiên bản cụ thể từ metadata: `[Nguồn: policy_admission v3, hiệu lực từ 01/09/2026]`, phân biệt rạch ròi với v2.\n"
            "- Quản lý vòng đời (Lifecycle Management): Khi v3 được kích hoạt, hệ thống cập nhật bản ghi của v2 thành `is_active: false` hoặc xóa bỏ v2 qua lệnh `delete_many(filter={\"version\": \"v2\"})` mà không ảnh hưởng tới v3."
        ),
        "explanation": (
            "Nội dung trùng lặp ('Hạn nộp là 30/9') giữa các phiên bản là bài toán kinh điển trong quản trị vòng đời tài liệu. Khóa định danh của bản ghi "
            "bắt buộc phải bao gồm thông tin phiên bản để tránh hiện tượng ghi đè (overwrite) và cho phép quản lý vòng đời (giữ, lọc, vô hiệu hóa, xóa) "
            "từng phiên bản hoàn toàn độc lập."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế Record ID độc lập phiên bản] (1.5 điểm): Định nghĩa khóa duy nhất kết hợp doc_id, version và chunk_index để không bị ghi đè.\n"
            "- [Đặc tả Metadata Schema vòng đời] (1.0 điểm): Thiết kế đầy đủ các trường version, is_active, effective_date, supersedes.\n"
            "- [Cơ chế tìm kiếm, trích dẫn & xóa độc lập] (1.5 điểm): Trình bày rõ ràng cách pre-filter is_active=true, trích dẫn có version và API xóa theo phiên bản."
        ),
        "reference_source": "Pinecone Documentation: 'Namespaces and Metadata Versioning' & Milvus Partition Management"
    },
    "d07-q081": {
        "sample_answer": (
            "1. Hành vi Dừng sớm (Fail-Fast / Early Abort Behavior):\n"
            "Hệ thống phải lập tức chặn đứng quá trình khởi động (Fail-fast / Crash immediately), không cho phép nhận yêu cầu từ người dùng và không âm thầm fallback sang bộ nhớ chứa dữ liệu test cũ.\n"
            "- Lý do: Ứng dụng yêu cầu bộ sưu tập `policies-v3` gắn embedder E3. Việc kết nối nhầm sang `policies-v2` gắn embedder E2 sẽ gây ra hai thảm họa: (a) Không tương thích vector (Dimension/Embedding Mismatch hoặc ô nhiễm không gian vector giữa E2 và E3); (b) Trả về dữ liệu chính sách cũ đã hết hạn hoặc dữ liệu test giả mạo cho người dùng thật.\n"
            "2. Điều kiện kiểm tra an toàn lúc khởi động (Startup Healthcheck Invariants):\n"
            "Hệ thống chỉ chuyển sang trạng thái Sẵn sàng (Readiness Probe = 200 OK) khi thỏa mãn đồng thời 4 điều kiện:\n"
            "- Điều kiện 1 (Collection Identity Verification): Kiểm tra tên collection thực tế trả về từ backend phải khớp chính xác với cấu hình mong đợi (`assert client.collection_name == 'policies-v3'`).\n"
            "- Điều kiện 2 (Embedder Model & Dimension Match): Kiểm tra định danh embedder và số chiều vector thực tế của collection phải khớp chính xác với mô hình E3 (`assert client.embedding_dim == E3.dimension`).\n"
            "- Điều kiện 3 (Environment/Tenant Isolation): Xác nhận kết nối đang trỏ vào môi trường Production, từ chối mọi fallback âm thầm sang Mock/In-Memory Test Store.\n"
            "- Điều kiện 4 (Readiness Ping): Thực hiện một truy vấn kiểm tra (canary search) trên collection mục tiêu thành công."
        ),
        "explanation": (
            "Nguyên tắc 'Fail-Safe Defaults' trong kiến trúc hệ thống tin cậy: khi phát hiện cấu hình sai lệch giữa các thành phần trọng yếu "
            "(Collection version, Embedding model), hệ thống phải dừng sớm để bảo vệ người dùng, thay vì tự ý fallback về dữ liệu test hoặc phiên bản cũ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Hành vi dừng sớm dứt khoát] (1.5 điểm): Khẳng định hệ thống phải fail-fast ngay lập tức, cấm âm thầm fallback sang bộ nhớ test cũ hoặc policies-v2.\n"
            "- [Cảnh báo rủi ro kỹ thuật] (1.0 điểm): Nêu rõ rủi ro mismatch embedding giữa E2 và E3 cùng nguy cơ trả dữ liệu sai lệch cho người dùng.\n"
            "- [Bộ điều kiện kiểm tra an toàn khởi động] (1.5 điểm): Thiết lập 4 điều kiện kiểm tra toàn diện: tên collection, embedder identity/dimension, môi trường cách ly, canary test."
        ),
        "reference_source": "Google SRE Book: 'Fail-Safe Design and Readiness Probes' & Kubernetes Documentation: 'Configure Liveness and Readiness Probes'"
    },
    "d07-q082": {
        "sample_answer": (
            "1. Trạng thái và bản ghi tạo mới sau hai lần thêm:\n"
            "- Trạng thái ban đầu: Kho có **1 bản ghi**: `{\"id\": \"X::0\"}`.\n"
            "- Lần thêm thứ nhất (Nhận `A::0` và `B::0` cùng nội dung 'Chính sách hoàn tiền' nhưng khác metadata/doc_id):\n"
            "  + Bản ghi tạo mới: Cả hai bản ghi `A::0` và `B::0` đều được thêm thành công vào kho. Vì hệ thống định danh bản ghi bằng Khóa chính (Primary Key / Record ID) chứ không định danh bằng nội dung văn bản. Do đó, việc trùng lặp nội dung không gây ghi đè hay thay thế bản ghi.\n"
            "  + Trạng thái kho sau lần 1: Gồm **3 bản ghi**: `X::0`, `A::0`, `B::0`.\n"
            "- Lần thêm thứ hai (Nhận `A::1` với nội dung khác):\n"
            "  + Bản ghi tạo mới: Bản ghi `A::1` được thêm mới thành công (đây là chunk thứ 2 của tài liệu A, có ID hoàn toàn mới so với `A::0`).\n"
            "  + Trạng thái kho sau lần 2: Gồm **4 bản ghi**: `X::0`, `A::0`, `B::0`, `A::1`.\n"
            "2. Các điều kiện kiểm thử cần xác nhận (Verification Invariants):\n"
            "- Kiểm thử số lượng (Count Invariant): `assert store.count() == 4` sau hai lần thêm.\n"
            "- Kiểm thử tính toàn vẹn danh tính (ID Distinctness): 4 ID `['X::0', 'A::0', 'B::0', 'A::1']` đều tồn tại và độc lập.\n"
            "- Kiểm thử bảo toàn nội dung và metadata: Truy xuất `A::0` và `B::0`, xác nhận cả hai đều giữ nguyên nội dung 'Chính sách hoàn tiền' nhưng mang `doc_id` tương ứng là `'A'` và `'B'`."
        ),
        "explanation": (
            "Cơ sở dữ liệu vector hoạt động dựa trên hợp đồng định danh bản ghi (Record Contract): Khóa chính (ID) quyết định việc tạo mới (Insert) "
            "hay cập nhật (Upsert). Hai bản ghi có nội dung hoàn toàn giống nhau nhưng mang ID khác nhau sẽ cùng tồn tại độc lập trong không gian chỉ mục, "
            "cho phép trích dẫn chính xác nguồn gốc của từng tài liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Trạng thái sau lần thêm thứ nhất] (1.5 điểm): Xác định kho có 3 bản ghi (X::0, A::0, B::0); giải thích trùng nội dung không ghi đè vì khác ID.\n"
            "- [Trạng thái sau lần thêm thứ hai] (1.0 điểm): Xác định kho có 4 bản ghi (thêm mới A::1).\n"
            "- [Các điều kiện kiểm thử toàn vẹn] (1.5 điểm): Thiết lập kiểm thử kiểm tra số lượng bản ghi (count=4), tính phân biệt của ID và tính bảo toàn của metadata."
        ),
        "reference_source": "Pinecone Documentation: 'Upsert Limits and Record Uniqueness' & Milvus 'Insert Entities'"
    },
    "d07-q083": {
        "sample_answer": (
            "1. Hành vi đúng của API nhận Document ID (Correct Behavior):\n"
            "- Khi giao diện truyền nhầm `chunk_id = 'P::1'` vào API xóa tài liệu (`delete_by_doc_id`):\n"
            "  + API nhận diện không có tài liệu nào có `doc_id == 'P::1'` (vì tài liệu gốc có `doc_id == 'P'`).\n"
            "  + Hành vi an toàn: Không xóa bất kỳ bản ghi nào trong kho (xóa 0 bản ghi), hoặc trả về mã lỗi `400 Bad Request / 404 Not Found` cảnh báo ID truyền vào không hợp lệ. Tuyệt đối không được tự ý xóa chunk `P::1` khi hợp đồng API quy định xóa cấp tài liệu.\n"
            "2. Kiểm soát cần có để ngăn chặn nhầm lẫn (Preventive Controls):\n"
            "- Kiểm soát kiểu dữ liệu và định dạng ID (ID Schema Validation): Áp dụng regex kiểm tra tham số: `doc_id` không được chứa ký tự phân cách chunk (`::`). Nếu phát hiện chuỗi có dạng `*::*`, hệ thống lập tức từ chối và cảnh báo giao diện đang truyền nhầm chunk ID.\n"
            "- Tách biệt rõ ràng hai Endpoint API:\n"
            "  + `DELETE /documents/{doc_id}`: Xóa toàn bộ các chunk có `metadata.doc_id == doc_id`.\n"
            "  + `DELETE /chunks/{chunk_id}`: Chỉ xóa duy nhất 1 chunk cụ thể.\n"
            "3. Trạng thái sau khi thực hiện xóa P hợp lệ (`delete_by_doc_id('P')`):\n"
            "- Hệ thống tìm và xóa toàn bộ các bản ghi có `doc_id == 'P'` (bao gồm 3 bản ghi: `P::0`, `P::1`, `P::2`).\n"
            "- Trạng thái còn lại trong kho: Duy nhất **1 bản ghi**: `Q::0`."
        ),
        "explanation": (
            "Sự bất tương thích giữa đơn vị tài liệu (Document-level) và đơn vị phân đoạn (Chunk-level) trong các thao tác vòng đời (CRUD) "
            "dễ dẫn đến lỗi xóa nhầm hoặc xóa sót dữ liệu. Việc xác thực chặt chẽ cú pháp ID tại API Gateway và phân tách rõ ràng endpoint là biện pháp "
            "phòng vệ sống còn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- [Hành vi đúng khi truyền nhầm ID] (1.0 điểm): Chỉ ra API không xóa bản ghi nào hoặc báo lỗi do không tìm thấy doc_id='P::1'.\n"
            "- [Kiểm soát kỹ thuật ngăn chặn] (1.0 điểm): Đề xuất validation cú pháp ID (chặn ký tự '::' trong doc_id) và tách biệt rõ API cấp document vs cấp chunk.\n"
            "- [Trạng thái sau khi xóa P hợp lệ] (1.0 điểm): Xác định đúng kho còn lại duy nhất bản ghi Q::0 (đã xóa sạch P::0, P::1, P::2)."
        ),
        "reference_source": "Qdrant Documentation: 'Points Deletion and Filter-based Deletion' & REST API Design Guidelines"
    },
    "d07-q084": {
        "sample_answer": (
            "1. Chẩn đoán hậu quả của các lỗi metadata (Defect Impact Diagnosis):\n"
            "- Lỗi 1: Chunk thứ hai bị mất trường `audience=staff`:\n"
            "  + Hậu quả: Khi cán bộ/nhân viên truy vấn chính sách hoàn phí với bộ lọc bảo mật `audience=staff`, chunk thứ hai sẽ bị bộ lọc metadata loại bỏ hoàn toàn. Người dùng chỉ đọc được nửa đầu của chính sách và mất nửa sau, gây đứt gãy thông tin nghiêm trọng.\n"
            "- Lỗi 2: Cả hai chunk đều dùng chung `chunk_index=0`:\n"
            "  + Hậu quả: Gây xung đột khóa chính (Primary Key Collision) nếu ID được sinh theo công thức `{doc_id}::{chunk_index}` (`refund::0`), dẫn đến chunk sau ghi đè chunk trước. Nếu ID ngẫu nhiên, hệ thống sẽ không thể tái lập đúng thứ tự đọc của tài liệu khi nạp vào context của LLM.\n"
            "2. Đặc tả các bản ghi sau khi đã sửa chữa (Corrected Records):\n"
            "- Bản ghi 1 (Chunk 0):\n"
            "  + `id`: `\"refund::chunk_0\"`\n"
            "  + `metadata`: `{\"doc_id\": \"refund\", \"source_url\": \"/v4\", \"audience\": \"staff\", \"chunk_index\": 0, \"total_chunks\": 2}`\n"
            "- Bản ghi 2 (Chunk 1):\n"
            "  + `id`: `\"refund::chunk_1\"`\n"
            "  + `metadata`: `{\"doc_id\": \"refund\", \"source_url\": \"/v4\", \"audience\": \"staff\", \"chunk_index\": 1, \"total_chunks\": 2}`\n"
            "3. Điều kiện kiểm tra trong Ingestion Pipeline (Validation Invariants):\n"
            "- Invariant 1: Toàn bộ các trường cấp tài liệu (`doc_id`, `source_url`, `audience`) phải được kế thừa 100% trên mọi chunk con.\n"
            "- Invariant 2: `chunk_index` phải là một chuỗi số nguyên tăng dần liên tục không trùng lặp: `0, 1, ..., total_chunks - 1`."
        ),
        "explanation": (
            "Lỗi thất thoát metadata (Metadata Dropping) và trùng lặp chỉ số chunk (Index Duplication) trong quá trình nạp dữ liệu là nguyên nhân phổ biến "
            "khiến hệ thống RAG hoạt động sai lệch. Việc thiết lập kiểm thử tính bất biến (Assertion Invariants) ngay tại pipeline nạp dữ liệu giúp phát hiện "
            "và loại bỏ lỗi này trước khi đưa vào chỉ mục vector."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán hậu quả mất audience] (1.0 điểm): Nêu rõ việc chunk 2 bị filter loại bỏ khiến người dùng mất nửa sau chính sách.\n"
            "- [Chẩn đoán hậu quả trùng chunk_index=0] (1.0 điểm): Nêu rõ nguy cơ ghi đè bản ghi và mất thứ tự đọc tài liệu.\n"
            "- [Đặc tả 2 bản ghi chuẩn hóa] (1.0 điểm): Viết đúng schema của cả 2 chunk với đầy đủ audience=staff và chunk_index là 0 và 1.\n"
            "- [Thiết lập điều kiện kiểm tra Ingestion] (1.0 điểm): Định nghĩa 2 invariant kiểm tra kế thừa metadata cấp doc và chỉ số chunk liên tục."
        ),
        "reference_source": "LlamaIndex Documentation: 'Ingestion Pipeline Assertions and Transformations' (https://docs.llamaindex.ai)"
    },
    "d07-q085": {
        "sample_answer": (
            "1. Rà soát các lỗi nghiêm trọng trong bản nháp kiểm thử (Flaw Audit):\n"
            "- Lỗi 1 (Câu hỏi mơ hồ, không có căn cứ đánh giá): Truy vấn 'Chính sách nào tốt nhất?' mang tính chủ quan cảm tính, không có tiêu chí định lượng khách quan.\n"
            "- Lỗi 2 (Tự viết đáp án chuẩn không qua thẩm định nguồn): Đáp án do mô hình tự sinh mà không có chuyên gia đối chiếu văn bản gốc dễ chứa ảo giác.\n"
            "- Lỗi 3 (Thiếu Ground-Truth Document ID): Để trống trường tài liệu mong đợi khiến không thể đo lường các chỉ số truy xuất cốt lõi (Recall@K, MRR).\n"
            "- Lỗi 4 (Rò rỉ dữ liệu và thiên vị thực nghiệm cực kỳ nghiêm trọng): Sửa truy vấn sau khi thấy Chiến lược B thắng để 'hợp thức hóa' đầu ra của B là hành vi gian lận khoa học (Data Leakage / Contamination), làm mất hoàn toàn giá trị của bộ benchmark.\n"
            "2. Viết lại quy trình xây dựng bộ kiểm thử chuẩn hóa (Redesigned Benchmark Protocol):\n"
            "- Bước 1 (Thiết kế câu hỏi dựa trên nhu cầu thực tế): Chọn câu hỏi có tính thực tế cao, ví dụ: 'Quy trình và điều kiện xin học bổng khuyến khích học tập học kỳ 1 năm học 2026?'.\n"
            "- Bước 2 (Xác định Ground-Truth Document & Facts từ nguồn gốc): Chuyên gia tra cứu tài liệu chính sách gốc, chỉ định chính xác danh sách các `expected_chunk_ids` và viết câu trả lời chuẩn có trích dẫn điều khoản cụ thể.\n"
            "- Bước 3 (Đóng băng bộ dữ liệu kiểm thử - Benchmark Freezing): Phiên bản hóa bộ dữ liệu kiểm thử (ví dụ: `gold_v1.0.json`) và khóa quyền chỉnh sửa.\n"
            "- Bước 4 (Thực hiện đánh giá đối chứng mù): Chạy độc lập tất cả các chiến lược (Chiến lược A, B, C...) trên bộ dữ liệu đã đóng băng, đo lường tự động bằng Recall@K, Context Precision và Faithfulness mà không được sửa đổi câu hỏi."
        ),
        "explanation": (
            "Một bộ benchmark đánh giá RAG chỉ có giá trị khi nó được xây dựng độc lập với các hệ thống được đánh giá. Việc thay đổi câu hỏi theo đầu ra "
            "của một mô hình chiến thắng là hành vi vi phạm nghiêm trọng tính toàn vẹn nghiên cứu (Research Integrity), biến benchmark thành công cụ tự chứng minh sai lệch."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Rà soát đầy đủ 4 lỗi của bản nháp] (1.5 điểm): Chỉ ra câu hỏi mơ hồ, đáp án tự sinh thiếu kiểm duyệt, thiếu expected docs, và đặc biệt là lỗi rò rỉ dữ liệu khi sửa truy vấn theo Chiến lược B.\n"
            "- [Quy trình 4 bước chuẩn hóa] (1.5 điểm): Thiết kế lại quy trình: câu hỏi thực tế, ground-truth từ tài liệu gốc, đóng băng dữ liệu, đánh giá đối chứng độc lập.\n"
            "- [Nguyên tắc toàn vẹn dữ liệu] (1.0 điểm): Nhấn mạnh quy tắc bất di bất dịch: không bao giờ thay đổi benchmark sau khi quan sát kết quả thử nghiệm."
        ),
        "reference_source": "Es et al. (2023): 'Ragas: Automated Evaluation of Retrieval Augmented Generation' & NeurIPS Benchmark Guidelines"
    },
    "d07-q086": {
        "sample_answer": (
            "1. Chấm điểm từng chunk về độ đầy đủ ngữ nghĩa và mức độ liên quan (Evaluation):\n"
            "Query: 'Ai được miễn phí trễ hạn?'\n"
            "- **R1**: Mức liên quan: Trung bình / Ngữ nghĩa: Không đầy đủ. R1 chỉ chứa danh sách đối tượng nhưng thiếu tiêu đề quy định ngữ cảnh; người đọc không thể biết danh sách này áp dụng cho 'miễn phí trễ hạn', 'miễn phí tài liệu' hay một chính sách khác.\n"
            "- **R2**: Mức liên quan: Cao / Ngữ nghĩa: Bị đứt gãy nghiêm trọng (Dangling Clause). R2 có tiêu đề đúng nhưng câu ngoại lệ cốt lõi bị cắt cụt ngay sau từ 'trừ khi...', làm mất hoàn toàn điều kiện miễn trừ thực tế.\n"
            "- **R3**: Mức liên quan: Sai / Không hợp lệ (Irrelevant / Wrong Context). R3 hoàn chỉnh về câu chữ nhưng thuộc về một quy ước/chính sách khác (ví dụ: quy ước năm cũ hoặc quy định của đơn vị khác), không áp dụng cho đối tượng của câu hỏi.\n"
            "2. Đề xuất sửa chữa theo từng tầng kiến trúc (Layer-wise Repair Proposals):\n"
            "- Sửa tầng Phân đoạn (Chunking Boundary Repair) cho R2:\n"
            "  + Thay thế bộ cắt văn bản bằng Sentence Splitter hoặc tăng `chunk_overlap` từ 0 lên 50 ký tự để câu ngoại lệ không bị cắt cụt sau 'trừ khi'.\n"
            "- Sửa tầng Ngữ cảnh & Cấu trúc (Context Enrichment) cho R1:\n"
            "  + Bổ sung tiền tố tiêu đề tổ tiên (Ancestor Heading / Breadcrumb Injection) vào đầu chunk R1 trước khi sinh embedding để chunk luôn mang ngữ cảnh của quy định cha.\n"
            "- Sửa tầng Lọc Metadata (Metadata Filtering) cho R3:\n"
            "  + Bổ sung bộ lọc tiền truy vấn `policy_domain` và `version` để loại bỏ các tài liệu thuộc quy ước không liên quan."
        ),
        "explanation": (
            "Một chunk hoàn chỉnh về mặt ngữ pháp (như R3) vẫn có thể hoàn toàn sai nếu không đúng phạm vi quy định. Ngược lại, chunk đúng chủ đề nhưng "
            "bị đứt gãy cú pháp (như R2) hoặc thiếu ngữ cảnh cha (như R1) đều đòi hỏi các giải pháp sửa chữa chuyên biệt ở từng tầng: metadata filtering, "
            "sentence chunking và breadcrumb enrichment."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chấm điểm chính xác 3 chunks] (1.5 điểm): Nhận diện đúng: R1 thiếu tiêu đề/ngữ cảnh cha, R2 bị cắt cụt mệnh đề sau 'trừ khi', R3 hoàn chỉnh nhưng sai quy ước áp dụng.\n"
            "- [Đề xuất sửa tầng Chunking cho R2] (1.0 điểm): Áp dụng sentence boundary chunking hoặc tăng overlap để cứu câu ngoại lệ.\n"
            "- [Đề xuất sửa tầng Metadata & Breadcrumbs cho R1 và R3] (1.5 điểm): Tiêm breadcrumb cho R1 và áp dụng bộ lọc metadata phiên bản/domain cho R3."
        ),
        "reference_source": "Anthropic Documentation: 'Contextual Retrieval' & TruLens 'Context Relevance Evaluation'"
    },
    "d07-q087": {
        "sample_answer": (
            "1. Diễn giải kết quả thực nghiệm (Empirical Result Interpretation):\n"
            "- Tổng hợp Recall@5: Chiến lược Heading đạt 0.80, Chiến lược Fixed-300 đạt 0.79 (chênh lệch chỉ 0.01 - gần như tương đương nếu chỉ nhìn con số tổng thể).\n"
            "- Phân rã theo nhóm câu hỏi (Sub-cohort Analysis):\n"
            "  + Ở nhóm truy vấn ngoại lệ (8 queries): Heading thắng áp đảo (thắng 6/8, hòa 2, thua 0). Lý do: Cấu trúc heading giữ trọn vẹn ngữ cảnh lồng nhau giữa điều kiện và ngoại lệ.\n"
            "  + Ở nhóm truy vấn FAQ ngắn (6 queries): Fixed-300 thắng áp đảo (thắng 5/6, hòa 1, thua 0). Lý do: FAQ ngắn chỉ cần các đoạn cố định nhỏ gọn, không bị loãng vector bởi các phần văn bản dài của cả section.\n"
            "  + Ở 6 truy vấn còn lại: Hai bên hòa nhau (6/6).\n"
            "2. Quy tắc Quyết định Kỹ thuật Không thổi phồng (Objective Decision Rule):\n"
            "- **Không tuyên bố** 'Chiến lược Heading vượt trội' chỉ dựa trên Recall tổng hợp 0.80 vs 0.79 vì con số trung bình đã che giấu sự thất bại ở nhóm FAQ.\n"
            "- Quy tắc triển khai nghiệp vụ: Nếu hệ thống định tuyến (Query Router) nhận diện được loại câu hỏi:\n"
            "  + Truy vấn tìm kiếm điều khoản / ngoại lệ chính sách: Định tuyến tìm kiếm trên Collection chia theo Heading.\n"
            "  + Truy vấn câu hỏi đáp ngắn / FAQ: Định tuyến tìm kiếm trên Collection chia theo Fixed-300.\n"
            "3. Thiết kế Thử nghiệm Kế tiếp (Next Controlled Experiment):\n"
            "- Thử nghiệm chiến lược phân đoạn lai (Hybrid / Hierarchical Chunking): Sử dụng Heading Chunking làm Parent Document kết hợp Fixed-length Chunking làm Child Document (Parent-Child Retriever), đo lường trên cả 20 truy vấn với mục tiêu đạt Recall@5 >= 0.90 trên cả hai nhóm câu hỏi."
        ),
        "explanation": (
            "Hiện tượng nghịch lý Simpson và lỗi tổng hợp trung bình (Aggregation Smoothing) thường xuyên làm lu mờ các đặc tính đối lập của từng thuật toán. "
            "Một kỹ sư AI có năng lực chuyên môn cao sẽ không bao giờ vội vã kết luận dựa trên con số tổng thể gần bằng nhau, mà phải phân rã hiệu năng theo từng nhóm "
            "đặc thù để thiết kế chiến lược định tuyến truy xuất hoặc kiến trúc lai phù hợp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Diễn giải sâu sắc hiện tượng phân rã] (1.5 điểm): Phân tích rõ việc con số tổng thể (0.80 vs 0.79) che giấu ưu thế tuyệt đối của Heading ở nhóm ngoại lệ (6/8) và của Fixed ở nhóm FAQ ngắn (5/6).\n"
            "- [Quy tắc quyết định không overclaim] (1.0 điểm): Không overclaim; đề xuất cơ chế định tuyến truy xuất dựa trên đặc trưng câu hỏi.\n"
            "- [Thiết kế thử nghiệm kế tiếp với Parent-Child] (1.5 điểm): Đề xuất thử nghiệm cụ thể với Parent-Child Retriever để dung hòa ưu điểm của cả hai chiến lược."
        ),
        "reference_source": "LlamaIndex Documentation: 'Auto-merging & Hierarchical Retrievers' & Kohavi et al.: 'Trustworthy Online Controlled Experiments'"
    }
}
