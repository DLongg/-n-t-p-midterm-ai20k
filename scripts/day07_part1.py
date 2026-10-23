# -*- coding: utf-8 -*-
"""
Day 07 Part 1: Questions 1 to 23 (d07-q002 to d07-q062)
"""

DAY_07_PART1 = {
    "d07-q002": {
        "sample_answer": (
            "1. Lựa chọn phương thức cung cấp dữ liệu cho từng nguồn:\n"
            "- Kho chính sách nội bộ (đổi hàng tháng): Sử dụng RAG Pipeline (Retrieval-Augmented Generation) "
            "với cơ sở dữ liệu vector (Vector DB). Tài liệu chính sách được trích xuất văn bản, phân đoạn (chunking), "
            "gắn metadata phân loại, sinh vector embeddings và lập chỉ mục. Khi người dùng truy vấn, hệ thống tìm kiếm "
            "các đoạn văn bản tương đồng cao nhất để đưa vào ngữ cảnh (context) kèm theo trích dẫn (citations) nguồn.\n"
            "- Số dư ngày phép còn lại (đổi thời gian thực theo từng giao dịch): Sử dụng cơ chế Gọi công cụ/Hàm (Tool Calling / "
            "Function Calling) kết nối trực tiếp đến API của hệ thống Quản lý nhân sự (HRIS / Core ERP Database) thông qua "
            "REST/gRPC endpoint có định danh người dùng và xác thực bảo mật.\n"
            "2. Lý do không thể dùng một phương thức duy nhất:\n"
            "Hai nguồn dữ liệu mang đặc tính và yêu cầu vận hành hoàn toàn trái ngược nhau. Chính sách nội bộ là tri thức phi cấu trúc, "
            "tĩnh trong chu kỳ dài (hàng tháng), đòi hỏi khả năng tìm kiếm ngữ nghĩa (semantic search) và trích dẫn nguyên văn điều khoản; "
            "nếu lưu trong bảng quan hệ cứng nhắc sẽ rất khó truy vấn tự nhiên. Ngược lại, số dư ngày phép là trạng thái vận hành thời gian thực "
            "(operational state), có tính biến động cao sau từng giao dịch và đòi hỏi tính toàn vẹn, chính xác tuyệt đối (ACID). Nếu đưa số dư ngày phép "
            "vào Vector DB, dữ liệu sẽ liên tục bị lỗi thời (stale), tốn chi phí re-indexing khổng lồ và đối mặt nguy cơ mô hình ngôn ngữ ảo giác (hallucination) "
            "về số ngày phép của nhân viên."
        ),
        "explanation": (
            "Trong kiến trúc ứng dụng AI doanh nghiệp, nguyên lý phân tách nguồn dữ liệu chỉ rõ sự khác biệt giữa 'Kho tri thức' (Knowledge Base) "
            "và 'Trạng thái vận hành thời gian thực' (Operational State). Kho tri thức phi cấu trúc phù hợp với RAG Pipeline vì dữ liệu ổn định và "
            "cần trích dẫn ngữ cảnh. Trạng thái vận hành đòi hỏi tính nhất quán giao dịch và dữ liệu mới nhất (freshness) từng giây, bắt buộc phải truy xuất "
            "qua Transactional API / Tool Calling để triệt tiêu nguy cơ stale index và ảo giác dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân loại & Phương thức] (1.5 điểm): Xác định đúng RAG qua Vector DB cho chính sách tĩnh và Tool Calling/API cho số dư ngày phép thời gian thực.\n"
            "- [Bản chất dữ liệu & Bất tương thích] (1.5 điểm): Phân tích sâu sắc sự khác biệt giữa tri thức phi cấu trúc (semantic search, trích dẫn) và dữ liệu trạng thái giao dịch (ACID, biến động cao, nguy cơ stale/hallucination khi index vào Vector DB).\n"
            "- [Trích dẫn & Kiểm soát an toàn] (1.0 điểm): Nêu rõ cơ chế trích dẫn nguồn cho chính sách và xác thực danh tính bảo mật khi gọi API dữ liệu cá nhân."
        ),
        "reference_source": "OpenAI Documentation: 'Function Calling and Retrieval in Enterprise Architectures' (https://platform.openai.com/docs/guides/function-calling)"
    },
    "d07-q004": {
        "sample_answer": (
            "1. Phân loại 3 trường dữ liệu:\n"
            "- `course_policy`: Dữ liệu tri thức tham chiếu / Chính sách đào tạo tĩnh (Static Reference Knowledge). Phụ trách bởi: Phòng Đào tạo (Academic Affairs). "
            "Nhịp cập nhật: Theo học kỳ hoặc chu kỳ năm học (tần suất rất thấp, hàng quý/năm). Cách truy cập phù hợp: Lưu trữ trong Document/Vector Store và truy xuất qua RAG với bộ lọc metadata.\n"
            "- `seat_remaining`: Dữ liệu trạng thái vận hành thời gian thực (Real-time Operational State). Phụ trách bởi: Hệ thống Quản lý Đào tạo / Đăng ký tín chỉ (Core SIS/LMS Database). "
            "Nhịp cập nhật: Theo từng giao dịch đặt/hủy chỗ của sinh viên (liên tục từng giây/mili-giây). Cách truy cập phù hợp: Gọi Tool/API trực tiếp đến dịch vụ kiểm tra chỗ hoặc truy vấn Redis/SQL với cơ chế khóa dữ liệu (locking/optimistic concurrency).\n"
            "- `student_language`: Dữ liệu trạng thái phiên tương tác người dùng (Session / Ephemeral Context State). Phụ trách bởi: Client / Web UI Frontend hoặc Session Manager. "
            "Nhịp cập nhật: Theo phiên làm việc hiện tại của người học (tồn tại tạm thời trong phiên chat, không lưu lâu dài). Cách truy cập phù hợp: Tiêm trực tiếp vào system prompt/ngữ cảnh hội thoại (Context Injection) trong payload gửi tới LLM."
        ),
        "explanation": (
            "Hệ thống thông tin phân tán cần phân định ranh giới ngữ nghĩa truy cập dữ liệu (Access Semantics). Dữ liệu tham chiếu chu kỳ dài (course_policy) "
            "thuộc về hệ thống tri thức. Dữ liệu tài nguyên có thể cạnh tranh (seat_remaining) thuộc về hệ thống giao dịch thời gian thực. Trạng thái phiên cục bộ "
            "(student_language) thuộc về ngữ cảnh runtime, không làm biến đổi cơ sở dữ liệu backend."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân loại chính xác 3 trường] (1.5 điểm): Phân loại đúng course_policy là tri thức tĩnh, seat_remaining là trạng thái vận hành thời gian thực, student_language là trạng thái phiên tạm thời.\n"
            "- [Bên phụ trách & Nhịp cập nhật] (1.5 điểm): Xác định đúng chủ thể quản lý và nhịp độ thay đổi (học kỳ vs mili-giây giao dịch vs theo phiên).\n"
            "- [Phương thức truy cập kỹ thuật] (1.0 điểm): Đề xuất đúng kênh truy xuất: Vector DB RAG, Transactional API/SQL, và Session Context Injection."
        ),
        "reference_source": "Google Cloud Architecture Framework: 'Data Categorization and Access Semantics' (https://cloud.google.com/architecture/framework/system-design)"
    },
    "d07-q007": {
        "sample_answer": (
            "1. Thiết kế phép biến đổi dữ liệu trước khi tạo embeddings (Pre-embedding Transformation Pipeline):\n"
            "- Loại bỏ hoàn toàn dữ liệu định danh cá nhân (PII Elimination): Xóa bỏ các trường `advisor_name`, `student_email`, và `support_case_id`. Vì mục tiêu là so sánh các vấn đề phổ biến theo chương trình và không cần nối các ca hỗ trợ của cùng người học, các mã định danh này không mang giá trị ngữ nghĩa mà lại gây rủi ro rò rỉ dữ liệu nhạy cảm theo chuẩn GDPR/HIPAA và làm nhiễu không gian vector.\n"
            "- Chuẩn hóa và làm giàu ngữ cảnh (Contextual Normalization): Chuẩn hóa giá trị `program` (ví dụ: viết hoa thống nhất 'CS', 'AI', 'BA') và `issue_category` (chuyển thành taxonomy chuẩn hóa). Ghép tiền tố ngữ cảnh vào nội dung văn bản phản hồi, ví dụ: 'Chương trình: [program] | Chủ đề: [issue_category] | Nội dung phản hồi: [text]'.\n"
            "- Lưu trữ Metadata có cấu trúc: Đưa `program` và `issue_category` vào payload/metadata của vector để phục vụ việc lọc có điều kiện (filtered search / aggregate grouping) sau này.\n"
            "2. Lợi ích kỹ thuật: Việc loại bỏ PII giúp vector không gian chỉ tập trung vào ngữ nghĩa của vấn đề học thuật/hỗ trợ, tránh hiện tượng clustering theo tên cố vấn hay ID ca, đồng thời tuân thủ nghiêm ngặt nguyên tắc tối thiểu hóa dữ liệu (data minimization)."
        ),
        "explanation": (
            "Trước khi sinh vector embeddings, dữ liệu phải trải qua bước tiền xử lý nhằm bảo vệ quyền riêng tư và tối ưu hóa không gian biểu diễn. Dữ liệu PII "
            "vừa không có giá trị phân tích xu hướng vừa có thể bị trích xuất ngược qua các tấn công suy diễn (inversion attacks). Việc đưa thông tin phân loại vào "
            "metadata cho phép kết hợp giữa tìm kiếm tương đồng ngữ nghĩa và thống kê phân nhóm có cấu trúc."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Loại bỏ PII & Dữ liệu nhạy cảm] (1.5 điểm): Chỉ rõ việc xóa advisor_name, student_email, support_case_id và giải thích căn cứ không cần liên kết ca/người học.\n"
            "- [Tái cấu trúc & Làm giàu ngữ cảnh] (1.5 điểm): Thiết kế định dạng văn bản đưa vào embedder với tiền tố chương trình và danh mục vấn đề chuẩn hóa.\n"
            "- [Thiết kế Metadata lọc] (1.0 điểm): Chuyển program và issue_category thành trường metadata có cấu trúc để phục vụ pre-filtering/grouping."
        ),
        "reference_source": "NIST Special Publication 800-122: 'Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)' & OWASP Top 10 for LLM: LLM06 Sensitive Information Disclosure"
    },
    "d07-q010": {
        "sample_answer": (
            "1. Cách nhận diện (Detection):\n"
            "Kiểm tra nội dung văn bản trích xuất từ các thư viện PDF thông thường (như PyPDF, PDFMiner, pypdfium2). Nếu MIME type là `application/pdf` nhưng tổng số ký tự trích xuất được (character count) bằng 0 hoặc tỷ lệ ký tự/trang dưới ngưỡng tối thiểu (ví dụ < 20 ký tự/trang), đồng thời trang chứa đối tượng hình ảnh (XObject Image), hệ thống xác định đây là 'Scanned PDF' hoặc 'Image-only PDF'.\n"
            "2. Cách xử lý (Processing Strategy):\n"
            "Kích hoạt luồng xử lý dự phòng tự động (Fallback Routing): Chuyển hướng tài liệu sang bộ xử lý OCR chuyên dụng (như Tesseract, PaddleOCR, AWS Textract, hoặc Azure Document Intelligence). Chuyển từng trang PDF thành ảnh chất lượng cao (300 DPI), tiến hành tiền xử lý ảnh (khử nghiêng - deskew, khử nhiễu - denoise, tăng tương phản) và chạy OCR để trích xuất văn bản có tọa độ.\n"
            "3. Cách kiểm tra (Verification):\n"
            "So sánh kết quả đầu ra: Đo lường độ dài ký tự thu được, kiểm tra độ tin cậy của OCR (OCR confidence score > 85%), và kiểm tra tính hợp lệ về mặt từ điển ngôn ngữ. Đối chiếu bằng mắt hoặc dùng phương pháp ngẫu nhiên kiểm tra trang có bảng/chữ.\n"
            "4. Nhật ký cần lưu giữ (Audit Logging):\n"
            "Ghi log chi tiết: `{file_id, file_name, mime_type, extractor_attempted: 'native_pdf', status: 'fallback_triggered', reason: 'empty_text_layer', fallback_extractor: 'tesseract_ocr', dpi: 300, extracted_char_count: 1420, avg_confidence: 0.92, processing_time_ms: 1250}`."
        ),
        "explanation": (
            "PDF là một định dạng đóng gói bao chứa (container format). Một tệp PDF có thể chứa văn bản số (digital native text) hoặc chỉ chứa ảnh quét (raster images). "
            "Hệ thống trích xuất tài liệu bắt buộc phải có cơ chế định tuyến linh hoạt (Extractor Routing): kiểm tra lớp văn bản trước, nếu rỗng thì kích hoạt pipeline OCR "
            "kèm nhật ký kiểm toán rõ ràng để phục vụ giám sát và gỡ lỗi."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Nhận diện PDF dạng ảnh] (1.0 điểm): Nêu rõ cách phát hiện khi MIME là application/pdf nhưng độ dài chuỗi ký tự bằng 0 hoặc dưới ngưỡng kèm đối tượng ảnh.\n"
            "- [Quy trình xử lý Fallback OCR] (1.0 điểm): Mô tả rõ quy trình chuyển đổi trang sang ảnh (render DPI) và áp dụng OCR engine.\n"
            "- [Phương pháp kiểm tra chất lượng] (1.0 điểm): Nêu các tiêu chí kiểm tra: độ tin cậy OCR, độ dài ký tự, kiểm thử tính toàn vẹn.\n"
            "- [Đặc tả nhật ký/Audit Log] (1.0 điểm): Định nghĩa cấu trúc log chi tiết ghi lại sự kiện fallback, lý do, và thông số thực thi."
        ),
        "reference_source": "LangChain Documentation: 'Unstructured Document Loaders and OCR Fallbacks' (https://python.langchain.com/docs/integrations/document_loaders/unstructured_file/)"
    },
    "d07-q013": {
        "sample_answer": (
            "1. Lựa chọn dạng biểu diễn (Representation Format):\n"
            "Sử dụng định dạng Markdown có cấu trúc phân cấp (Hierarchical Markdown). Cấu trúc tiêu đề sử dụng các cấp `#`, `##`, `###` tương ứng với phân cấp chính sách. "
            "Bảng ngoại lệ được giữ nguyên dưới dạng bảng Markdown (Markdown Table) hoặc danh sách định dạng kèm ngữ cảnh rõ ràng.\n"
            "2. Phần cần giữ và phần cần bỏ:\n"
            "- Phần cần giữ: Giữ nguyên vẹn toàn bộ chuỗi tiêu đề tổ tiên (breadcrumbs/ancestor headings), nội dung điều khoản chính sách, và bảng ngoại lệ gắn liền với mục tương ứng. Mỗi bảng ngoại lệ phải được gắn kèm tiêu đề mục cha để bảo toàn phạm vi áp dụng.\n"
            "- Phần cần bỏ: Loại bỏ toàn bộ các thành phần điều hướng HTML (header, footer, navbar, sidebar, breadcrumb click elements, nút back-to-top, thẻ script, CSS style, div container vô nghĩa). Các thành phần này gây lãng phí token, làm loãng mật độ ngữ nghĩa và gây nhiễu cho mô hình embedding.\n"
            "3. Giải thích chi phí biểu diễn chấp nhận được:\n"
            "Việc giữ lại tiêu đề Markdown và bảng biểu chỉ làm tăng một lượng nhỏ overhead ký tự (khoảng 5-10% token so với văn bản thuần), nhưng mang lại giá trị sống còn: giúp retriever và LLM liên kết chính xác ngoại lệ với mục chính sách cha, ngăn chặn hoàn toàn lỗi gán nhầm ngoại lệ sang điều khoản khác."
        ),
        "explanation": (
            "Trong hệ thống RAG, biểu diễn văn bản phải tối ưu hóa giữa tỷ lệ tín hiệu trên nhiễu (Signal-to-Noise Ratio) và chi phí token. Markdown là chuẩn "
            "biểu diễn tối ưu cho LLM vì cú pháp gọn nhẹ nhưng bảo toàn đầy đủ quan hệ thứ bậc của tiêu đề và quan hệ hàng-cột của bảng dữ liệu, trong khi việc loại bỏ "
            "nhiễu giao diện HTML giúp embedding vector tập trung vào nội dung tri thức cốt lõi."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Lựa chọn dạng biểu diễn] (1.0 điểm): Chọn Markdown có cấu trúc phân cấp và bảng Markdown.\n"
            "- [Phần giữ lại có căn cứ] (1.5 điểm): Nêu rõ việc giữ tiêu đề lồng nhau và bảng ngoại lệ gắn kèm mục cha để đảm bảo truy vấn đúng phạm vi.\n"
            "- [Phần loại bỏ triệt để] (1.0 điểm): Loại bỏ các thành phần điều hướng HTML, thẻ DOM rác, header/footer.\n"
            "- [Đánh giá chi phí biểu diễn] (0.5 điểm): Phân tích chi phí overhead token nhỏ nhưng đổi lại độ chính xác ngữ cảnh cao."
        ),
        "reference_source": "LlamaIndex Documentation: 'Markdown Node Parser & Document Cleaners' (https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)"
    },
    "d07-q015": {
        "sample_answer": (
            "1. Quy ước Metadata (Metadata Schema Contract):\n"
            "Mỗi bản ghi chunk chính sách khi nhập kho phải chứa trường metadata với định dạng JSON chuẩn hóa:\n"
            "```json\n"
            "{\n"
            "  \"doc_id\": \"string (mã định danh duy nhất của chính sách)\",\n"
            "  \"department\": \"string (mã khoa/phòng ban)\",\n"
            "  \"language\": \"string (mã ngôn ngữ chuẩn ISO 639-1)\",\n"
            "  \"semester\": \"string (mã học kỳ chuẩn định dạng YYYY-S)\",\n"
            "  \"is_active\": \"boolean\"\n"
            "}\n"
            "```\n"
            "2. Tập giá trị cho phép (Allowed Values / Value Constraints):\n"
            "- `department`: Thuộc danh mục mã khoa chuẩn hóa: `[\"CS\", \"EE\", \"BA\", \"LAW\", \"MED\", \"ALL\"]` (viết hoa, không nhận biến thể tên dài).\n"
            "- `language`: Thuộc tập mã ISO 639-1 cho phép: `[\"vi\", \"en\"]`.\n"
            "- `semester`: Chuỗi theo định dạng regex `^20\\d{2}-(1|2|3|SUMMER)$` (ví dụ: `\"2026-1\"`, `\"2026-2\"`).\n"
            "3. Hai quy tắc từ chối bản ghi (Rejection / Quarantine Rules):\n"
            "- Quy tắc 1 (Thiếu trường bắt buộc hoặc giá trị ngoài danh mục): Bản ghi bị từ chối nhập kho nếu thiếu bất kỳ trường nào trong `{department, language, semester}` hoặc giá trị trường không thuộc tập giá trị cho phép (ví dụ `department=\"computer-science\"` hoặc `language=\"vn\"` thay vì `\"vi\"`).\n"
            "- Quy tắc 2 (Vi phạm định dạng thời gian/học kỳ): Bản ghi bị từ chối nếu `semester` không khớp biểu thức chính quy (ví dụ: `\"Kỳ 1 năm 2026\"` hoặc `\"2026\"`), để tránh làm gãy bộ lọc tiền truy vấn (pre-filter)."
        ),
        "explanation": (
            "Metadata contract đóng vai trò là hàng rào bảo vệ tính toàn vẹn của chỉ mục vector (vector index integrity). Nếu metadata bị ô nhiễm bởi các giá trị "
            "tự do, bộ lọc metadata pre-filtering sẽ loại bỏ sai các tài liệu hợp lệ hoặc giữ lại các tài liệu rác. Một quy ước chặt chẽ với schema validation "
            "và chính sách cách ly (quarantine) ngay tại ingestion pipeline là điều kiện tiên quyết cho hệ thống RAG doanh nghiệp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đặc tả Schema Contract] (1.5 điểm): Định nghĩa cấu trúc trường rõ ràng gồm department, language, semester với kiểu dữ liệu chuẩn.\n"
            "- [Tập giá trị cho phép] (1.5 điểm): Xác định tập giá trị đóng hoặc regex chuẩn cho từng trường (ISO ngôn ngữ, mã khoa, định dạng học kỳ).\n"
            "- [Hai quy tắc từ chối rõ ràng] (1.0 điểm): Đưa ra 2 quy tắc từ chối cụ thể khi thiếu trường, sai danh mục giá trị hoặc sai regex."
        ),
        "reference_source": "Pinecone Documentation: 'Metadata Filtering & Schema Enforcement' (https://docs.pinecone.io/guides/data/filter-by-metadata)"
    },
    "d07-q016": {
        "sample_answer": (
            "1. Tính bước trượt (Step / Stride):\n"
            "`step = chunk_size - overlap = 400 - 100 = 300` ký tự.\n"
            "2. Xác định các vị trí bắt đầu (Start Positions) và phạm vi từng chunk:\n"
            "- Chunk 1: Bắt đầu tại index 0. Kết thúc tại: `min(0 + 400, 1050) = 400`. Phạm vi: [0, 400). Độ dài: 400 ký tự.\n"
            "- Chunk 2: Bắt đầu tại index `0 + 300 = 300`. Kết thúc tại: `min(300 + 400, 1050) = 700`. Phạm vi: [300, 700). Độ dài: 400 ký tự.\n"
            "- Chunk 3: Bắt đầu tại index `300 + 300 = 600`. Kết thúc tại: `min(600 + 400, 1050) = 1000`. Phạm vi: [600, 1000). Độ dài: 400 ký tự.\n"
            "- Chunk 4: Bắt đầu tại index `600 + 300 = 900`. Kết thúc tại: `min(900 + 400, 1050) = 1050`. Phạm vi: [900, 1050). Độ dài: `1050 - 900 = 150` ký tự.\n"
            "Vị trí bắt đầu tiếp theo nếu có sẽ là `900 + 300 = 1200 >= 1050` (vượt quá độ dài văn bản), do đó dừng thuật toán.\n"
            "3. Tổng kết kết quả:\n"
            "- Bước trượt (Step): 300 ký tự.\n"
            "- Các vị trí bắt đầu: `[0, 300, 600, 900]`.\n"
            "- Độ dài chunk cuối cùng: 150 ký tự.\n"
            "- Tổng số chunk: 4 chunk."
        ),
        "explanation": (
            "Trong thuật toán phân đoạn cửa sổ trượt cố định (Fixed-size Sliding Window Chunking), cửa sổ dịch chuyển theo giá trị `step = chunk_size - overlap`, "
            "chứ không dịch chuyển theo `chunk_size`. Khi chỉ số bắt đầu cộng bước trượt đạt tới đoạn cuối của tài liệu, chunk cuối cùng sẽ được cắt ngắn tại "
            "độ dài thực tế của tài liệu (`total_length - start`), đảm bảo toàn bộ ký tự của tài liệu đều được bao phủ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Tính đúng bước trượt] (1.0 điểm): Tính chính xác step = 400 - 100 = 300 ký tự.\n"
            "- [Liệt kê các vị trí bắt đầu] (1.0 điểm): Liệt kê chính xác 4 vị trí: 0, 300, 600, 900.\n"
            "- [Tính độ dài chunk cuối] (1.0 điểm): Tính chính xác độ dài chunk 4 là 150 ký tự (từ index 900 đến 1050).\n"
            "- [Xác định tổng số chunk] (1.0 điểm): Kết luận đúng tổng số chunk là 4."
        ),
        "reference_source": "LangChain Documentation: 'CharacterTextSplitter and Chunk Overlap Arithmetic' (https://python.langchain.com/docs/how_to/character_text_splitter/)"
    },
    "d07-q023": {
        "sample_answer": (
            "1. Đề xuất chiến lược kết hợp (Hybrid / Hierarchical Chunking Strategy):\n"
            "- Cấu trúc phân đoạn theo tiêu đề kèm phân đoạn con (Heading-aware Section Chunking with Sub-chunking / Parent-Document Retrieval):\n"
            "  + Cấp độ 1 (Section Boundary): Phân chia tài liệu theo cấu trúc phân cấp tiêu đề (`#`, `##`, `###`). Mỗi mục chính sách tạo thành một Parent Document tự chứa trọn vẹn ngữ cảnh điều kiện và ngoại lệ.\n"
            "  + Cấp độ 2 (Size Budget Enforcement): Nếu một section quá dài (vượt quá ngân sách token tối ưu, ví dụ > 500 tokens), áp dụng Recursive Character Splitting để chia nhỏ thành các Child Chunks, nhưng bắt buộc gắn metadata `parent_id` và sao chép tiêu đề tổ tiên (`breadcrumbs`) vào từng child chunk.\n"
            "  + Gắn kết ngoại lệ: Các ghi chú ngoại lệ luôn được neo giữ (anchor) vào cùng block với điều kiện áp dụng tương ứng, không bị ngắt quãng giữa hai chunk.\n"
            "2. Bằng chứng quyết định dựa trên bộ kiểm thử đã đóng băng (Empirical Decision Evidence):\n"
            "- Đo lường trên bộ câu hỏi đóng băng: Đánh giá bằng 2 chỉ số cụ thể:\n"
            "  (a) Tỷ lệ câu hỏi ngoại lệ tìm thấy cả điều kiện lẫn ngoại lệ trong Top-K (Condition & Exception Co-occurrence Recall@5);\n"
            "  (b) Tỷ lệ chunk bị nhiễm chéo thông tin giữa hai chính sách khác nhau (Cross-policy Contamination Rate).\n"
            "- Điều kiện nghiệm thu chiến lược kết hợp: Đạt Co-occurrence Recall >= 95% (khắc phục lỗi của fixed-window) và Cross-policy Contamination = 0% (khắc phục lỗi của long-heading chunking)."
        ),
        "explanation": (
            "Cửa sổ cố định (fixed window) thường cắt ngang giữa điều kiện và ngoại lệ vì không hiểu ranh giới ngữ nghĩa. Ngược lại, chunking thuần túy theo "
            "tiêu đề dễ tạo ra những đoạn quá dài hoặc gộp lẫn nội dung nếu tài liệu viết lỏng lẻo. Giải pháp tối ưu là phân đoạn có cấu trúc phân cấp "
            "(Hierarchical/Parent-Child Chunking) kết hợp gắn metadata tổ tiên, được kiểm chứng bằng bộ benchmark cố định với các chỉ số đo lường lỗi cụ thể."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chiến lược kết hợp có cấu trúc] (1.5 điểm): Đề xuất phân đoạn theo heading kết hợp chia nhỏ đệ quy khi vượt budget, kèm kế thừa metadata tổ tiên.\n"
            "- [Giải pháp neo giữ ngoại lệ] (1.0 điểm): Nêu cơ chế neo giữ ngoại lệ cùng phạm vi với điều kiện chính sách, không để ngắt giữa chừng.\n"
            "- [Bằng chứng quyết định thực nghiệm] (1.5 điểm): Xác định rõ 2 chỉ số đo lường trên bộ kiểm thử đóng băng (độ phủ đồng thời điều kiện-ngoại lệ và tỷ lệ nhiễm chéo) cùng ngưỡng nghiệm thu."
        ),
        "reference_source": "LlamaIndex Documentation: 'Hierarchical Node Parser & Parent Document Retrieval' (https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)"
    },
    "d07-q026": {
        "sample_answer": (
            "1. Lựa chọn chính sách Overlap (Overlap Policy Selection):\n"
            "Chọn mức overlap nhỏ nhất đủ để bảo toàn liên kết ngữ nghĩa giữa hai chunk kề nhau, trong trường hợp này là `overlap = 40 ký tự` (hoặc mức tương đương 1-2 câu trọn vẹn ngữ nghĩa).\n"
            "- Giải thích vì sao không chọn 0: Overlap = 0 tạo ra ranh giới cứng (hard cutoff), làm đứt gãy mối liên hệ giữa điều kiện ở cuối chunk A và ngoại lệ ở đầu chunk B, khiến retriever bỏ sót thông tin liên quan khi câu hỏi yêu cầu cả hai.\n"
            "- Giải thích vì sao không chọn 180: Overlap = 180 ký tự quá lớn, chiếm tỷ lệ cao trong chunk, dẫn đến hiện tượng trùng lặp thông tin nghiêm trọng (near-duplicate chunks). Điều này làm cho danh sách Top-K bị chiếm dụng bởi 3 chunk gần giống nhau, làm giảm đa dạng ngữ cảnh (diversity), lãng phí token ngân sách và tăng chi phí LLM.\n"
            "2. Phương pháp kiểm thử và xác thực chính sách (Verification Method):\n"
            "- Kiểm thử truy xuất (Retrieval Test): Chạy bộ kiểm thử với các query liên đới biên (boundary-spanning queries) và kiểm tra xem cả hai mệnh đề (điều kiện và ngoại lệ) có xuất hiện trong cùng một chunk hoặc trong Top-2 chunk liền kề hay không.\n"
            "- Kiểm tra độ dư thừa ngữ cảnh (Redundancy / Deduplication Test): Tính toán điểm tương đồng Jaccard hoặc Cosine giữa các chunk liên tiếp; đảm bảo mức overlap không tạo ra các chunk có độ trùng lặp nội dung > 40%."
        ),
        "explanation": (
            "Nguyên tắc thiết lập chunk overlap tuân theo định lý biên ngữ nghĩa: overlap phải đủ lớn để một ý nghĩa bị cắt ngang ở cuối chunk trước xuất hiện "
            "trọn vẹn ở đầu chunk sau, nhưng phải là mức tối thiểu cần thiết để không gây ô nhiễm danh sách Top-K bằng các bản sao gần trùng lặp (redundant chunks), "
            "gây nghẽn context window của mô hình tạo sinh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định chính sách chính xác] (1.5 điểm): Chọn mức overlap nhỏ nhất giữ đủ liên kết (40 ký tự) và bác bỏ có lý lẽ mức 0 (mất liên kết) và mức 180 (trùng lặp, lãng phí top-k).\n"
            "- [Phân tích đánh đổi kỹ thuật] (1.5 điểm): Phân tích trade-off rõ ràng giữa bảo toàn ngữ nghĩa liên đoạn và sự đa dạng của tập kết quả truy xuất.\n"
            "- [Phương pháp kiểm tra thực nghiệm] (1.0 điểm): Đề xuất cách kiểm tra truy xuất mệnh đề biên và đo lường tỷ lệ trùng lặp nội dung giữa các chunk."
        ),
        "reference_source": "Pinecone Learning Center: 'Chunking Strategies for LLM Applications' (https://www.pinecone.io/learn/chunking-strategies/)"
    },
    "d07-q029": {
        "sample_answer": (
            "1. Những điều Embedding vector hỗ trợ kết luận:\n"
            "- Hỗ trợ kết luận về độ tương đồng ngữ nghĩa bề mặt và chủ đề (Semantic Topical Similarity): Vector embeddings chuyển đổi văn bản thành tọa độ trong không gian ngữ nghĩa tiềm ẩn. Điểm cosine 0,91 cao hơn 0,87 chứng minh rằng chunk 0,91 có sự tương đồng từ vựng/ngữ nghĩa gần gũi hơn với các từ khóa và ý đồ trong câu hỏi của người dùng so với chunk 0,87.\n"
            "2. Những điều Embedding vector KHÔNG hỗ trợ kết luận:\n"
            "- Không thể kết luận về tính chân thực khách quan (Factual Truth / Validity): Mô hình embedding không có cơ chế xác minh tính đúng đắn của thông tin.\n"
            "- Không thể kết luận về tính cập nhật và hiệu lực pháp lý (Temporal Freshness / Policy Lifecycle): Vector không gian hoàn toàn không có trục thời gian nội tại; nó không biết chính sách nào là bản cũ và chính sách nào là bản hiện hành đang có hiệu lực thi hành.\n"
            "- Không thể thay thế bộ lọc trạng thái nghiệp vụ: Một chính sách cũ đã bị thu hồi nhưng viết hay hơn, trùng từ khóa nhiều hơn vẫn có thể có điểm cosine cao hơn chính sách mới.\n"
            "3. Giải pháp thiết kế hệ thống bắt buộc:\n"
            "Phải tách rời việc tìm kiếm ngữ nghĩa khỏi quản lý vòng đời tài liệu: Sử dụng Metadata Filtering (ví dụ: `is_active: true`, `version: 'v3'`, `effective_date <= CURRENT_DATE`) để sàng lọc trước khi thực hiện tính điểm tương đồng vector."
        ),
        "explanation": (
            "Không gian embedding phản ánh sự tương đồng hình thức và khái niệm ngữ nghĩa, hoàn toàn bất khả tri (agnostic) đối với tính chân lý và hiệu lực thời gian. "
            "Một sai lầm phổ biến trong thiết kế RAG là đồng nhất điểm cosine cao với 'câu trả lời đúng'. Để hệ sinh thái RAG tin cậy, việc kiểm soát phiên bản và "
            "hiệu lực bắt buộc phải được giải quyết ở tầng metadata và dữ liệu có cấu trúc."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân tích vai trò của Embedding] (1.5 điểm): Nêu rõ embedding chỉ phản ánh sự tương đồng ngữ nghĩa/chủ đề trong không gian vector biểu diễn.\n"
            "- [Chỉ rõ giới hạn bản chất] (1.5 điểm): Khẳng định dứt khoát embedding không đo lường được tính đúng sai, tính cập nhật thời gian hay hiệu lực pháp lý của chính sách.\n"
            "- [Đề xuất giải pháp kiến trúc] (1.0 điểm): Đưa ra giải pháp dùng Metadata Filtering quản lý phiên bản và ngày hiệu lực để lọc trước khi truy xuất."
        ),
        "reference_source": "Reimers & Gurevych (2019): 'Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks' (EMNLP 2019) & OpenAI Embeddings Guide"
    },
    "d07-q034": {
        "sample_answer": (
            "1. Điều điểm số Cosine cho biết (Observed Fact):\n"
            "Chunk A đạt cosine 0,84 và Chunk B đạt 0,80 cho thấy: theo không gian vector của mô hình embedder hiện tại, vector biểu diễn của Chunk A có góc lệch nhỏ hơn so với vector truy vấn so với Chunk B. Điều này chỉ phản ánh mức độ trùng khớp ngữ nghĩa bề mặt (surface semantic overlap) hoặc chứa nhiều từ vựng bao quát chủ đề của câu hỏi.\n"
            "2. Điều điểm số CHƯA chứng minh (Unproven Hypotheses):\n"
            "- Chưa chứng minh Chunk A là câu trả lời tốt hơn cho người dùng. Thực tế Chunk A chỉ nói chung chung trong khi Chunk B mới chứa câu trả lời cụ thể có thể hành động được.\n"
            "- Chưa chứng minh mô hình embedder hiểu được chiều sâu nghiệp vụ; các embedder dạng bi-encoder thường bị thiên vị (bias) đối với các đoạn văn bản chứa nhiều từ khóa tần suất cao hoặc các câu khẳng định chung.\n"
            "3. Thử nghiệm kế tiếp (Next Controlled Experiment):\n"
            "- Thử nghiệm 1 (Tầng Re-ranking): Đưa cả Top-K (bao gồm Chunk A và B) qua một mô hình Cross-Encoder Re-ranker (ví dụ: BGE-Reranker-Large hoặc Cohere Rerank) để đánh giá độ liên quan thực sự ở cấp độ tương tác qua lại giữa query và document.\n"
            "- Thử nghiệm 2 (End-to-End Generation & Human/LLM Evaluation): Đưa lần lượt Chunk A và Chunk B vào context của generator và đo lường Answer Relevance / Completeness trên bộ câu hỏi thử nghiệm chuẩn hóa."
        ),
        "explanation": (
            "Điểm số Cosine từ Bi-Encoder chỉ là phép ước lượng gần đúng về sự gần gũi trong không gian tiềm ẩn (latent space), thường ưu tiên các văn bản tổng quát "
            "có mật độ từ khóa cao. Điểm số quan sát được không đồng nghĩa với giá trị thông tin thực tế. Quy trình hai tầng (Two-stage Retrieval: Bi-encoder retrieval "
            "+ Cross-encoder reranking) là giải pháp tiêu chuẩn để giải quyết sự sai lệch này."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- [Bản chất điểm quan sát] (1.0 điểm): Nêu đúng điểm cosine chỉ phản ánh góc vector trong không gian tiềm ẩn, không phản ánh độ chi tiết hữu ích.\n"
            "- [Điều chưa chứng minh] (1.0 điểm): Phân biệt rõ điểm số cao không chứng minh tính đầy đủ hay câu trả lời đúng trọng tâm nhu cầu người dùng.\n"
            "- [Thiết kế thử nghiệm tiếp theo] (1.0 điểm): Đề xuất thử nghiệm cụ thể với Cross-Encoder Reranker hoặc đo lường chất lượng câu trả lời đầu ra."
        ),
        "reference_source": "Thakur et al. (2021): 'BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models' (NeurIPS 2021)"
    },
    "d07-q038": {
        "sample_answer": (
            "1. Lựa chọn mô hình cho đợt phát hành hiện tại:\n"
            "Chọn **Mô hình A** (768 chiều, Recall@5 = 0,86, p95 latency = 45 ms).\n"
            "Căn cứ quyết định: Tiêu chí SLO kỹ thuật quy định nghiêm ngặt độ trễ `p95 <= 100 ms`. Mô hình B có Recall@5 nhỉnh hơn 2% (0,88 vs 0,86) nhưng độ trễ p95 lên tới 190 ms, vi phạm nghiêm trọng SLO kỹ thuật (vượt 90% giới hạn cho phép). Ngoài ra, Mô hình B có 3.072 chiều (gấp 4 lần Mô hình A), sẽ làm tăng gấp 4 lần dung lượng RAM lưu trữ index cho 5 triệu chunk, đẩy chi phí hạ tầng và độ trễ tìm kiếm vector lên rất cao mà không mang lại lợi ích tương xứng.\n"
            "2. Các hạn chế của Mô hình A:\n"
            "- Độ bao phủ Recall@5 thấp hơn Mô hình B 2% trên bộ kiểm thử Việt–Anh, có nguy cơ bỏ sót một số tài liệu hiếm hoặc câu hỏi đa ngữ phức tạp.\n"
            "- Khả năng biểu diễn ngữ nghĩa đa chiều trong các lĩnh vực chuyên sâu có thể kém hơn các mô hình embedding kích thước lớn (large dimensional embeddings).\n"
            "3. Điều kiện để xem xét lại lựa chọn (Re-evaluation Criteria):\n"
            "- Khi áp dụng các kỹ thuật tối ưu hóa chỉ mục cho Mô hình B thành công: như lượng tử hóa vector (Scalar Quantization SQ8 hoặc Product Quantization PQ) hoặc Matryoshka Embeddings cắt ngắn chiều xuống 768/1536 mà vẫn giữ recall cao và hạ p95 xuống dưới 80 ms.\n"
            "- Khi nâng cấp hạ tầng phần cứng (GPU indexing / HNSW acceleration) giúp hạ p95 của Mô hình B vào phạm vi SLO hợp lệ.\n"
            "- Khi có ngân sách tài chính và thời gian bảo trì được duyệt để chi trả chi phí re-embed cho toàn bộ 5 triệu chunk tài liệu."
        ),
        "explanation": (
            "Trong kỹ thuật hệ thống sản xuất (Production Engineering), việc tuân thủ SLO (Service Level Objective) là điều kiện tiên quyết bắt buộc (hard constraint). "
            "Một mô hình dù có độ chính xác cao hơn nhưng vi phạm SLO độ trễ sẽ bị loại bỏ khỏi danh sách triển khai thực tế. Việc chuyển đổi mô hình embedding trên tập "
            "dữ liệu lớn (5M chunks) phải tính toán toàn diện giữa chi phí tính toán lại, dung lượng RAM chỉ mục và độ trễ phục vụ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định chọn Model A có căn cứ] (1.5 điểm): Chọn Mô hình A vì thỏa mãn SLO p95 <= 100ms, loại Mô hình B vì vi phạm SLO (190ms) và chi phí RAM 3072d cho 5M chunk quá cao.\n"
            "- [Nhận diện hạn chế của Model A] (1.0 điểm): Nêu rõ hạn chế về Recall@5 thấp hơn 2% trên tập ngữ liệu Việt–Anh.\n"
            "- [Điều kiện xem xét lại lựa chọn] (1.5 điểm): Đưa ra các điều kiện cụ thể: kỹ thuật lượng tử hóa (quantization/Matryoshka), tối ưu hạ tầng đạt SLO latency, và ngân sách re-indexing 5M chunk."
        ),
        "reference_source": "Google SRE Book: 'Service Level Objectives and Latency Budgets' & Pinecone Benchmark: 'Embedding Dimension vs Latency and Memory Footprint'"
    },
    "d07-q044": {
        "sample_answer": (
            "1. Kết quả mong đợi cho mỗi kho dữ liệu:\n"
            "- Với Kho A (đang có 2 bản ghi, yêu cầu `top_k = 5`):\n"
            "  + Kết quả trả về: Trả về chính xác **2 bản ghi**. Thuật toán Top-K truy xuất tối đa `k` ứng viên hiện có trong kho; nếu số lượng bản ghi thỏa mãn điều kiện nhỏ hơn `k`, hệ thống chỉ trả về toàn bộ các bản ghi tìm thấy (`min(N, k)`), tuyệt đối không tự bịa thêm bản ghi giả lập hay trả về các phần tử rác.\n"
            "- Với Kho B (kho rỗng, yêu cầu `top_k = 5`):\n"
            "  + Kết quả trả về: Trả về danh sách rỗng `[]` (empty list) với mã trạng thái thành công (HTTP 200 OK), không sinh lỗi ngoại lệ hệ thống.\n"
            "2. Quy tắc sắp xếp khi điểm số tương đồng bằng nhau (Tie-breaking Rule):\n"
            "- Quy tắc: Khi hai hoặc nhiều bản ghi có điểm tương đồng cosine/similarity bằng nhau (ví dụ cùng bằng 0.8500), hệ thống áp dụng cơ chế xác định thứ tự đơn định (Deterministic Tie-breaking) bằng cách so sánh trường `record_id` theo thứ tự tăng dần (ascending order: `record_id_1 < record_id_2`).\n"
            "- Tầm quan trọng: Đảm bảo tính nhất quán và khả năng tái lập (idempotency/reproducibility) của kết quả tìm kiếm qua các lần gọi API khác nhau."
        ),
        "explanation": (
            "Giao diện tìm kiếm vector ngữ nghĩa (Vector Semantic Search) phải tuân thủ chặt chẽ hợp đồng API: trả về `min(count_matching, k)` phần tử. "
            "Khi có hiện tượng bằng điểm (tie), nếu không quy định thứ tự tie-breaking bằng một khóa đơn định duy nhất (như record_id), thứ tự trả về sẽ phụ thuộc "
            "vào cách duyệt vùng nhớ của thuật toán tìm kiếm gần đúng (ANN), gây ra lỗi không nhất quán dữ liệu giữa các lần truy vấn giống hệt nhau."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Kết quả của Kho A] (1.5 điểm): Xác định đúng Kho A trả về chính xác 2 bản ghi (áp dụng min(N, k)), không tạo bản ghi ảo.\n"
            "- [Kết quả của Kho B] (1.0 điểm): Xác định đúng Kho B trả về danh sách rỗng [] an toàn, không báo lỗi sập hệ thống.\n"
            "- [Quy tắc sắp xếp khi bằng điểm] (1.5 điểm): Nêu rõ cơ chế tie-breaking theo record_id tăng dần để đảm bảo tính tất định và khả năng tái lập."
        ),
        "reference_source": "Milvus Documentation: 'Vector Search Query Parameters, Limit/Top-K and Consistency' (https://milvus.io/docs/search.md)"
    },
    "d07-q045": {
        "sample_answer": (
            "1. So sánh chi tiết hai cơ chế lọc:\n"
            "- Lọc trước khi xếp hạng (Pre-filtering):\n"
            "  + Cơ chế: Hệ thống áp dụng bộ lọc metadata `department = 'engineering'` lên toàn bộ tập dữ liệu (hoặc sử dụng inverted index trên metadata) để lọc ra tập các ứng viên hợp lệ trước. Sau đó, thuật toán tìm kiếm vector chỉ tính toán tương đồng và xếp hạng trên tập ứng viên này để lấy `top_k = 1`.\n"
            "  + Kết quả: Kết quả Engineering tốt nhất (điểm 0.90) được trả về ở vị trí số 1. Yêu cầu của người dùng được thỏa mãn trọn vẹn.\n"
            "- Xếp hạng trước khi lọc (Post-filtering):\n"
            "  + Cơ chế: Thuật toán vector tìm kiếm `top_k = 1` trên toàn bộ kho dữ liệu trước; sau đó mới áp dụng bộ lọc `department = 'engineering'` trên danh sách kết quả trả về.\n"
            "  + Kết quả: Bước tìm kiếm vector trả về bản ghi Marketing (điểm 0.95). Bước lọc sau đó kiểm tra thấy bản ghi này không khớp phòng ban Engineering nên loại bỏ. Kết quả cuối cùng trả về danh sách rỗng `[]`, hoàn toàn bỏ lỡ bản ghi Engineering điểm 0.90!\n"
            "2. Kết luận thiết kế:\n"
            "Trong các hệ thống tìm kiếm có điều kiện ràng buộc kinh doanh nghiêm ngặt, Post-filtering cực kỳ nguy hiểm và dễ gây hiện tượng 'kết quả rỗng giả tạo' khi `k` nhỏ. Bắt buộc phải triển khai **Pre-filtering** (hoặc Single-stage Filtered Search kết hợp HNSW với payload filter như trong Qdrant/Milvus)."
        ),
        "explanation": (
            "Post-filtering (lấy Top-K rồi mới lọc) chịu rủi ro nghiêm trọng về độ phủ vì tập Top-K ban đầu có thể bị thống trị hoàn toàn bởi các tài liệu không thỏa mãn bộ lọc. "
            "Pre-filtering đảm bảo 100% các phần tử được xếp hạng đều hợp lệ. Các vector database hiện đại sử dụng kỹ thuật Single-stage filtering (lọc trực tiếp trong quá trình "
            "duyệt đồ thị HNSW) để vừa đạt hiệu năng cao vừa bảo đảm không bao giờ bỏ sót kết quả hợp lệ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân tích cơ chế Pre-filtering] (1.5 điểm): Giải thích rõ quy trình lọc ứng viên trước rồi xếp hạng, trả về đúng bản ghi Engineering (0.90).\n"
            "- [Phân tích cơ chế Post-filtering & Hậu quả] (1.5 điểm): Giải thích rõ việc lấy Top-1 Marketing (0.95) rồi lọc sẽ dẫn đến kết quả rỗng [], bỏ sót tài liệu hợp lệ.\n"
            "- [Kết luận kiến trúc] (1.0 điểm): Khẳng định ưu thế tuyệt đối của Pre-filtering trong hệ thống RAG doanh nghiệp."
        ),
        "reference_source": "Qdrant Documentation: 'Filtering Clause & Pre-filtering in Vector Search' (https://qdrant.tech/documentation/concepts/filtering/)"
    },
    "d07-q048": {
        "sample_answer": (
            "1. Kế hoạch tinh chỉnh có kiểm soát (Controlled Retrieval Tuning Plan):\n"
            "Áp dụng nguyên tắc tách biệt biến số (Single-Variable Isolation): Mỗi thí nghiệm chỉ thay đổi duy nhất một tham số, đo lường trên tập kiểm thử chuẩn hóa đã đóng băng (Frozen Gold Testset) trước khi kết hợp.\n"
            "- Bước 1: Khắc phục lỗi lọc sai thời kỳ (Eligibility Filter Fix)\n"
            "  + Hành động: Sửa điều kiện lọc `semester` để không loại bỏ đáp án mới (cho phép `semester IN ('current', 'upcoming')` hoặc bỏ lọc semester tạm thời để xác lập ground-truth).\n"
            "  + Phép đo: Xác nhận 100% truy vấn có tài liệu mới không bị chặn ở tầng metadata.\n"
            "- Bước 2: Tinh chỉnh tham số Top-K (Search Depth Tuning)\n"
            "  + Hành động: Giữ cố định không dùng similarity threshold. Thử nghiệm quét giá trị `k` từ 2 đến 8 (các bước: `k = 3, 4, 5, 6`).\n"
            "  + Phép đo: Đo Recall@k (đảm bảo không bỏ sót bằng chứng thứ ba) và Noise Ratio (tỷ lệ chunk rác lọt vào context). Xác định điểm uốn tối ưu (ví dụ `k = 4` hoặc `k = 5`).\n"
            "- Bước 3: Tinh chỉnh Ngưỡng tương đồng (Similarity Threshold Tuning)\n"
            "  + Hành động: Nhận diện ngưỡng 0.85 quá chặt làm rỗng 30% truy vấn. Hạ dần ngưỡng `threshold` từ 0.85 xuống 0.75, 0.70, 0.65 với `k` tối ưu đã tìm ở Bước 2.\n"
            "  + Phép đo: Đo Zero-result Query Rate (mục tiêu < 2%) kết hợp Context Precision.\n"
            "- Bước 4: Đánh giá tổng hợp và nghiệm thu (Integration Validation)\n"
            "  + Chạy toàn bộ pipeline tích hợp với bộ tham số tối ưu đã chọn, so sánh với baseline ban đầu."
        ),
        "explanation": (
            "Khi hệ thống truy xuất đồng thời gặp nhiều lỗi (thiếu bằng chứng, thừa nhiễu, tỷ lệ rỗng cao do threshold chặt, filter chặn sai), việc thay đổi nhiều "
            "tham số cùng lúc sẽ dẫn đến hỗn loạn thực nghiệm và không xác định được nguyên nhân gốc rễ. Quy trình chuẩn hóa yêu cầu sửa lỗi bộ lọc điều kiện tiên quyết trước, "
            "sau đó tối ưu hóa k, và cuối cùng mới điều chỉnh ngưỡng similarity."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Nguyên tắc kiểm soát biến số] (1.0 điểm): Nêu rõ nguyên tắc cô lập từng biến số trên tập testset đóng băng.\n"
            "- [Thứ tự xử lý từng tầng lỗi] (1.5 điểm): Sắp xếp đúng trình tự logic: sửa filter semester trước, quét tối ưu k, rồi mới nới lỏng similarity threshold.\n"
            "- [Chỉ số đo lường cho từng bước] (1.5 điểm): Đưa ra metric cụ thể cho từng bước: Zero-result rate, Recall@k, Noise ratio, Context Precision."
        ),
        "reference_source": "Google SRE: 'Controlled Experimentation and Tuning Principles' & Ragas Documentation: 'Retrieval Metrics'"
    },
    "d07-q051": {
        "sample_answer": (
            "1. Lựa chọn lớp triển khai (Deployment Class Selection):\n"
            "Chọn **Managed Cloud Vector Database (DBaaS)** (ví dụ: Pinecone Serverless/Standard, Qdrant Cloud Managed, hoặc AWS OpenSearch Serverless / Azure AI Search).\n"
            "Căn cứ lựa chọn:\n"
            "- Quy mô đội ngũ: Startup chỉ có 2 kỹ sư; việc tự host (self-hosted) cụm Milvus hoặc Elasticsearch phân tán đòi hỏi chi phí vận hành (ops overhead), thiết lập sharding, backup snapshot và quản lý node quá tải, vượt quá nguồn lực nhân sự.\n"
            "- Quy mô dữ liệu và độ khả dụng: 10 triệu vector đòi hỏi cụm phân tán để đảm bảo tính sẵn sàng cao (High Availability - HA) và tự động sao lưu dự phòng (Automated Backups/Disaster Recovery).\n"
            "- Độ trễ: Cần chọn nhà cung cấp có Data Plane triển khai tại cùng Region/Availability Zone với ứng dụng chính (ví dụ: `ap-southeast-1` Singapore) để đảm bảo độ trễ mạng cực thấp (< 10 ms).\n"
            "2. Các thông tin phụ thuộc phiên bản cần kiểm tra trước khi quyết định:\n"
            "- Hỗ trợ lọc Metadata có chỉ mục (Indexed Metadata Filtering) và chi phí gắn kèm trên 10 triệu bản ghi.\n"
            "- Giới hạn kích thước payload/metadata trên mỗi vector và chính sách tính phí theo dung lượng lưu trữ (Storage/Read-Write Unit pricing).\n"
            "- Cơ chế High Availability và SLA cam kết thời gian hoạt động (uptime SLA >= 99.9%).\n"
            "- Quy trình sao lưu định kỳ, restore point-in-time và chính sách mã hóa dữ liệu khi nghỉ (encryption at rest) đáp ứng compliance."
        ),
        "explanation": (
            "Quyết định chọn hạ tầng cơ sở dữ liệu vector phải cân bằng giữa năng lực vận hành của đội ngũ (team operational capacity) và các ràng buộc kỹ thuật. "
            "Với đội ngũ mỏng (2 kỹ sư), giải pháp Managed Service giúp chuyển giao gánh nặng bảo trì HA/Backup sang nhà cung cấp. Các thông số phụ thuộc phiên bản "
            "về định tuyến vùng (regional latency) và cơ chế lọc metadata là yếu tố then chốt quyết định tính khả thi dài hạn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Lựa chọn Managed DBaaS có căn cứ] (1.5 điểm): Chọn Managed Cloud Vector Database dựa trên đánh đổi năng lực 2 kỹ sư, yêu cầu HA/Backup cho 10M vectors.\n"
            "- [Ràng buộc độ trễ theo vùng] (1.0 điểm): Nhấn mạnh yêu cầu colocation cùng Cloud Region để đảm bảo latency thấp.\n"
            "- [Danh mục thông tin phiên bản cần kiểm tra] (1.5 điểm): Liệt kê các yếu tố kiểm tra trước: SLA, indexing metadata cost, payload size, SLA backup/restore."
        ),
        "reference_source": "AWS Architecture Center: 'Selecting Managed Vector Databases for Production Workloads' & Pinecone Architecture Guide"
    },
    "d07-q053": {
        "sample_answer": (
            "1. Thiết kế phân tách ranh giới Ngoại tuyến và Trực tuyến (Offline / Online Separation):\n"
            "- Pha Ngoại tuyến (Offline Ingestion Pipeline - Xử lý theo sự kiện hoặc định kỳ):\n"
            "  + Kích hoạt (Trigger): Chỉ chạy khi có sự kiện thay đổi dữ liệu nguồn (Webhook tài liệu cập nhật, CI/CD pipeline tài liệu, hoặc batch job định kỳ ban đêm). Tuyệt đối không chạy khi người dùng gửi câu hỏi!\n"
            "  + Ranh giới đầu ra đóng băng: Đầu ra của pha offline là Chỉ mục Vector có phiên bản (Versioned Vector Index, ví dụ `index_v2.1`) kèm bản đồ siêu dữ liệu (Metadata Store). Khi hoàn tất nhập liệu, hệ thống chạy kiểm thử kiểm tra tính sẵn sàng rồi chuyển cờ 'active_version' sang chỉ mục mới.\n"
            "- Pha Trực tuyến (Online Serving Pipeline - Xử lý thời gian thực per query):\n"
            "  + Kích hoạt: Người dùng gửi câu hỏi truy vấn.\n"
            "  + Luồng thực thi: Chỉ thực hiện sinh vector embedding cho chính câu hỏi (Query Embedding), áp dụng bộ lọc metadata, truy vấn Top-K trên chỉ mục vector đang hoạt động (Active Index) và đưa vào LLM để sinh câu trả lời.\n"
            "2. Xử lý bộ đệm truy vấn khi chính sách thay đổi (Cache Invalidation Strategy):\n"
            "- Cơ chế: Khi chỉ mục offline phát hành phiên bản mới, hệ thống tự động vô hiệu hóa toàn bộ cache truy vấn (Cache Invalidation) bằng cách gắn `index_version` vào khóa cache (`key = hash(query + index_version)`).\n"
            "- Kết quả: Ngăn chặn triệt để tình trạng cache query trả về kết quả thuộc chính sách cũ."
        ),
        "explanation": (
            "Một lỗi kiến trúc sơ đẳng là trộn lẫn Ingestion Pipeline vào Serving Request Path, khiến mọi câu hỏi đều phải trích xuất và embed lại toàn bộ kho tri thức, "
            "làm sập hệ thống vì độ trễ khủng khiếp. Nguyên tắc vàng của RAG là 'Embed once offline, query fast online' với cơ chế version-based cache invalidation."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế kích hoạt pha Offline] (1.5 điểm): Xác định đúng pha offline chỉ kích hoạt khi tài liệu thay đổi, tạo ra chỉ mục đóng băng có phiên bản.\n"
            "- [Thiết kế luồng pha Online] (1.0 điểm): Xác định pha online chỉ embed câu hỏi và tìm kiếm trên chỉ mục sẵn có.\n"
            "- [Cơ chế vô hiệu hóa Cache] (1.5 điểm): Đưa ra giải pháp gắn index version vào cache key để tự động invalidate cache cũ khi có chính sách mới."
        ),
        "reference_source": "Gao et al. (2023): 'Retrieval-Augmented Generation for Large Language Models: A Survey' & Martin Fowler: 'Cache Invalidation Strategies'"
    },
    "d07-q054": {
        "sample_answer": (
            "1. Thiết kế Danh tính bản ghi (Record Identity) và Metadata cho từng chunk:\n"
            "Khi tệp có thông tin đầu tệp `{doc_id: 'library', audience: 'student', source_url: 'https://edu.vn/lib'}` tạo ra 3 chunk, metadata phải được kế thừa đầy đủ:\n"
            "- Chunk 0:\n"
            "  + `record_id`: `\"library::chunk_0\"`\n"
            "  + `metadata`: `{\"doc_id\": \"library\", \"audience\": \"student\", \"source_url\": \"https://edu.vn/lib\", \"chunk_index\": 0, \"total_chunks\": 3}`\n"
            "- Chunk 1:\n"
            "  + `record_id`: `\"library::chunk_1\"`\n"
            "  + `metadata`: `{\"doc_id\": \"library\", \"audience\": \"student\", \"source_url\": \"https://edu.vn/lib\", \"chunk_index\": 1, \"total_chunks\": 3}`\n"
            "- Chunk 2:\n"
            "  + `record_id`: `\"library::chunk_2\"`\n"
            "  + `metadata`: `{\"doc_id\": \"library\", \"audience\": \"student\", \"source_url\": \"https://edu.vn/lib\", \"chunk_index\": 2, \"total_chunks\": 3}`\n"
            "2. Điều kiện kiểm tra tính toàn vẹn (Verification Invariants):\n"
            "- Điều kiện 1 (Document-level Metadata Propagation): Mọi chunk con đều phải chứa 100% các trường cấp tài liệu (`doc_id`, `audience`, `source_url`) trùng khớp với tài liệu gốc.\n"
            "- Điều kiện 2 (Chunk-level Uniqueness & Sequence): Mỗi chunk phải có `record_id` duy nhất dạng `{doc_id}::chunk_{index}` và `chunk_index` phải là dãy số liên tục từ `0` đến `total_chunks - 1`."
        ),
        "explanation": (
            "Quá trình phân đoạn (chunking) phá vỡ tài liệu lớn thành các đoạn nhỏ nhưng không được làm thất thoát ngữ cảnh cấp tài liệu. Kỹ thuật Metadata "
            "Propagation đảm bảo mọi chunk con đều mang đầy đủ thuộc tính phân quyền (`audience`) và nguồn gốc (`source_url`), giúp các bộ lọc metadata "
            "hoạt động chính xác trên từng đơn vị tìm kiếm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đặc tả ID & Metadata 3 chunk] (1.5 điểm): Thiết kế đúng định danh duy nhất (library::chunk_0, 1, 2) và sao chép đầy đủ metadata cấp tài liệu cho cả 3 chunk.\n"
            "- [Kiểm tra tính kế thừa metadata] (1.5 điểm): Nêu rõ điều kiện kiểm tra trường cấp tài liệu phải xuất hiện ở 100% các chunk con.\n"
            "- [Kiểm tra tính liên tục của index] (1.0 điểm): Kiểm tra chunk_index liên tục từ 0 đến N-1 và tính duy nhất của khóa chính."
        ),
        "reference_source": "LlamaIndex Documentation: 'Metadata Extraction and Ingestion Pipeline' (https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/)"
    },
    "d07-q056": {
        "sample_answer": (
            "1. Phân tách quy ước đọc và cập nhật (Separation of Contracts):\n"
            "- Kho Tri thức Chính sách (Policy Knowledge Base):\n"
            "  + Bản chất: Tri thức khách quan toàn cục (Global Objective Knowledge) mô tả quy định tổ chức.\n"
            "  + Quy ước đọc: Được truy cập bởi mọi người dùng; hỗ trợ tìm kiếm ngữ nghĩa kèm metadata filter (khoa, phiên bản).\n"
            "  + Quy ước cập nhật: Chỉ do Quản trị viên/Phòng ban chức năng cập nhật qua Ingestion Pipeline có kiểm duyệt.\n"
            "- Kho Bộ nhớ Người dùng (User Ephemeral / Personal Memory):\n"
            "  + Bản chất: Trạng thái chủ quan cá nhân (Personal Context / Affective State) mô tả hồ sơ hoặc cảm xúc người học.\n"
            "  + Quy ước đọc: Được phân vùng nghiêm ngặt theo `user_id` (chỉ truy xuất khi xác thực đúng phiên của Lan).\n"
            "  + Quy ước cập nhật: Tự động cập nhật theo thời gian thực từ các lượt tương tác của người dùng, có cơ chế hết hạn (TTL/expiry).\n"
            "2. Rủi ro nghiêm trọng nếu truy vấn chung (Risks of Unified Querying):\n"
            "- Rò rỉ thông tin riêng tư (PII / Privacy Leakage): Trạng thái cá nhân nhạy cảm của Lan ('đang stress') có thể bị trả về cho người dùng khác nếu câu hỏi của họ tương đồng về ngữ nghĩa với đoạn ghi chú này.\n"
            "- Ô nhiễm ngữ cảnh chính sách (Context Pollution): Khi hỏi về quy chế học vụ, việc nhầm lẫn giữa quy định chung và ghi chú tâm lý cá nhân sẽ khiến LLM đưa ra câu trả lời thiên vị hoặc sai lệch quy định đào tạo."
        ),
        "explanation": (
            "Trong hệ thống tác tử thông minh, việc nhầm lẫn giữa Bộ nhớ ngữ cảnh người dùng (User Memory) và Cơ sở tri thức (Domain Knowledge) là một lỗ hổng nghiêm trọng "
            "về quyền riêng tư và an toàn thông tin. Chúng phải được lưu trữ trong các Collection hoặc Namespace độc lập với các chính sách phân quyền truy cập (Access Control Lists) khác nhau."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Tách biệt quy ước đọc/cập nhật] (1.5 điểm): Phân định rõ kho tri thức toàn cục (quản trị viên cập nhật, công khai) và bộ nhớ cá nhân (user_id riêng, cập nhật theo phiên, TTL).\n"
            "- [Rủi ro rò rỉ quyền riêng tư] (1.5 điểm): Phân tích rủi ro nghiêm trọng khi ghi chú nhạy cảm cá nhân bị trả về cho người khác khi query chung.\n"
            "- [Rủi ro sai lệch nghiệp vụ] (1.0 điểm): Nêu rủi ro ô nhiễm context khiến câu trả lời chính sách bị thiên vị hoặc sai lệch."
        ),
        "reference_source": "LangChain Documentation: 'Agent Memory vs. Vector Store Retrievers' & OWASP LLM06: Sensitive Information Disclosure"
    },
    "d07-q057": {
        "sample_answer": (
            "1. Thiết kế cách chọn ngữ cảnh (Context Selection & Filtering Protocol):\n"
            "- Phân loại độ tin cậy và hiệu lực nguồn (Source Authority Filtering):\n"
            "  + C1 (Chính sách hiện hành): Nguồn thẩm quyền cao nhất (Primary Ground-Truth), thỏa mãn metadata `is_active: true`, được giữ lại làm ngữ cảnh cốt lõi.\n"
            "  + C2 (Blog không nguồn): Nguồn không có thẩm quyền (Unverified Secondary Source), tiềm ẩn thông tin sai lệch; bị loại bỏ hoàn toàn khỏi context prompt.\n"
            "  + C3 (Chính sách cũ): Đã hết hiệu lực (`is_active: false`); bị loại bỏ để tránh gây mâu thuẫn thông tin và ảo giác.\n"
            "- Ngữ cảnh cuối cùng đưa vào Prompt: Chỉ chứa duy nhất C1 kèm định danh trích dẫn `[Doc 1: Policy v3]`. Tuyệt đối không đưa C2 và C3 vào prompt.\n"
            "2. Hợp đồng câu trả lời có căn cứ (Answer Contract):\n"
            "- System Prompt Constraint: Yêu cầu mô hình chỉ trả lời dựa trên bằng chứng được cung cấp trong ngữ cảnh đã duyệt. Mọi mốc thời gian/deadline phải đi kèm trích dẫn chính xác `[Doc 1]`.\n"
            "- Quy tắc từ chối (Abstention Rule): Nếu ngữ cảnh hợp lệ (C1) không chứa thông tin về deadline mới được hỏi, mô hình bắt buộc phải trả lời: 'Tài liệu chính sách hiện hành không có thông tin về thời hạn này', tuyệt đối không được suy diễn từ kiến thức chung bên ngoài."
        ),
        "explanation": (
            "Hệ thống RAG tin cậy phải thực hiện thanh lọc ngữ cảnh (Context Curation) trước khi đưa vào mô hình tạo sinh. Điểm tương đồng vector cao không đồng nghĩa "
            "với nguồn tin cậy. Việc loại bỏ các nguồn không chính thức và chính sách hết hạn là tuyến phòng thủ then chốt để chống ảo giác và câu trả lời sai lệch."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Lọc ngữ cảnh theo độ tin cậy] (1.5 điểm): Giữ lại duy nhất C1 (chính sách hiện hành), loại bỏ dứt khoát C2 (blog không nguồn) và C3 (chính sách cũ).\n"
            "- [Đặc tả Answer Contract] (1.5 điểm): Thiết lập ràng buộc trích dẫn nguồn cụ thể [Doc 1] cho mọi khẳng định.\n"
            "- [Quy tắc từ chối khi thiếu bằng chứng] (1.0 điểm): Nêu rõ cơ chế từ chối trả lời (abstention) nếu C1 không chứa thông tin, cấm bịa đặt."
        ),
        "reference_source": "Lewis et al. (2020): 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' & Anthropic Claude Prompt Engineering Guide"
    },
    "d07-q059": {
        "sample_answer": (
            "1. Thiết kế 3 dòng dữ liệu kiểm thử chuẩn (Benchmark Gold Dataset):\n"
            "- Dòng 1 (Sinh viên tra cứu học vụ):\n"
            "  + `query`: 'Thời hạn sinh viên nộp đơn hoãn thi kết thúc học phần là khi nào?'\n"
            "  + `filter_criteria`: `{\"audience\": \"student\", \"department\": \"academic\"}`\n"
            "  + `expected_doc_ids`: `[\"academic_policy_2026::chunk_12\"]`\n"
            "  + `gold_answer`: 'Sinh viên phải nộp đơn trước ngày thi ít nhất 03 ngày làm việc kèm minh chứng hợp lệ.'\n"
            "- Dòng 2 (Cán bộ/Giảng viên tra cứu chế độ - Phụ thuộc Metadata):\n"
            "  + `query`: 'Quy định định mức giờ nghiên cứu khoa học bắt buộc đối với giảng viên cơ hữu.'\n"
            "  + `filter_criteria`: `{\"audience\": \"staff\", \"role\": \"faculty\"}`\n"
            "  + `expected_doc_ids`: `[\"staff_handbook_v4::chunk_45\"]`\n"
            "  + `gold_answer`: 'Giảng viên cơ hữu phải hoàn thành tối thiểu 600 giờ chuẩn nghiên cứu khoa học trong năm học.'\n"
            "- Dòng 3 (Đăng ký môn học - Trường hợp ngoại lệ):\n"
            "  + `query`: 'Điều kiện đăng ký môn học vượt số tín chỉ tối đa trong một học kỳ.'\n"
            "  + `filter_criteria`: `{\"audience\": \"student\", \"category\": \"course_registration\"}`\n"
            "  + `expected_doc_ids`: `[\"registration_rules::chunk_08\"]`\n"
            "  + `gold_answer`: 'Chỉ sinh viên có GPA tích lũy >= 3.2 mới được đăng ký tối đa 24 tín chỉ khi có phê duyệt của Trưởng khoa.'\n"
            "2. Quy tắc đóng băng bộ dữ liệu (Freezing Rules):\n"
            "- Bộ kiểm thử (câu hỏi, filter, gold chunks, gold answer) phải được phiên bản hóa và khóa chặt (frozen) trước khi thực hiện bất kỳ thử nghiệm thuật toán nào.\n"
            "- Tuyệt đối không được chỉnh sửa câu hỏi hoặc thêm bớt expected chunks sau khi quan sát kết quả của một chiến lược cụ thể nhằm tránh rò rỉ dữ liệu (benchmark contamination/overfitting)."
        ),
        "explanation": (
            "Benchmark retrieval chuẩn phải gắn liền với thực tế nghiệp vụ và bao quát cả tìm kiếm ngữ nghĩa lẫn lọc thuộc tính metadata. "
            "Quy tắc đóng băng bộ dữ liệu (Dataset Freezing) là nguyên tắc cốt lõi của phương pháp luận khoa học, ngăn ngừa hiện tượng thiên vị thực nghiệm "
            "hoặc 'chữa đề theo kết quả'."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế 3 dòng testset đầy đủ] (1.5 điểm): Xây dựng 3 dòng kiểm thử rõ ràng với câu hỏi thực tế, trong đó có 1 dòng phụ thuộc metadata (audience=staff/student).\n"
            "- [Xác định rõ ràng Gold Chunks & Ground Truth] (1.5 điểm): Cung cấp expected_doc_ids cụ thể và câu trả lời chuẩn xác thực từ nguồn.\n"
            "- [Quy tắc đóng băng nghiêm ngặt] (1.0 điểm): Nêu rõ quy tắc khóa dữ liệu trước thử nghiệm và cấm sửa đổi sau khi thấy kết quả."
        ),
        "reference_source": "Es et al. (2023): 'Ragas: Automated Evaluation of Retrieval Augmented Generation' & TREC Benchmark Guidelines"
    },
    "d07-q060": {
        "sample_answer": (
            "1. Tính toán các chỉ số xếp hạng truy xuất (Retrieval Metrics Computation):\n"
            "Theo đề bài: Danh sách Top-5 có nhãn liên quan là `[1, 0, 1, 0, 0]`. Tổng số tài liệu liên quan trong toàn bộ kho tài liệu là `N_rel = 4`.\n"
            "- **Precision@5**:\n"
            "  `Precision@5 = (Số tài liệu liên quan trong Top-5) / 5 = 2 / 5 = 0.40` (hoặc 40%).\n"
            "- **Recall@5**:\n"
            "  `Recall@5 = (Số tài liệu liên quan trong Top-5) / (Tổng số tài liệu liên quan trong kho) = 2 / 4 = 0.50` (hoặc 50%).\n"
            "- **MRR (Mean Reciprocal Rank)**:\n"
            "  Vị trí đầu tiên xuất hiện tài liệu liên quan (first relevant rank) là vị trí 1 (`rank = 1`).\n"
            "  `RR = 1 / 1 = 1.0` (hoặc 100%).\n"
            "2. Diễn giải kết quả phân tích:\n"
            "- Dấu hiệu kết quả nhiễu: Precision@5 chỉ đạt 0.40 (có tới 3 trên 5 chunk ở các vị trí 2, 4, 5 là hoàn toàn không liên quan). Điều này cho thấy tập kết quả chứa 60% nhiễu, làm lãng phí context window của LLM và tăng nguy cơ gây ảo giác.\n"
            "- Dấu hiệu mục tiêu bị bỏ sót: Recall@5 chỉ đạt 0.50, chứng minh hệ thống đã bỏ sót một nửa số tài liệu liên quan trong kho (2/4 tài liệu liên quan không lọt vào Top-5).\n"
            "- Điểm tích cực: MRR = 1.0 cho thấy hệ thống rất xuất sắc trong việc đưa ngay một tài liệu liên quan lên vị trí cao nhất (hạng 1)."
        ),
        "explanation": (
            "Các chỉ số đánh giá truy xuất phản ánh các khía cạnh khác nhau: Precision@K đo mật độ thông tin hữu ích trong vùng ngữ cảnh; Recall@K đo độ bao phủ "
            "toàn diện của bằng chứng; MRR đo tốc độ tiếp cận tài liệu đúng đầu tiên. Một hệ thống có MRR cao nhưng Precision thấp vẫn gây rủi ro lớn cho mô hình tạo sinh "
            "do lượng nhiễu trong context quá cao."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Tính đúng Precision@5] (1.0 điểm): Tính chính xác 2/5 = 0.40 (40%).\n"
            "- [Tính đúng Recall@5] (1.0 điểm): Tính chính xác 2/4 = 0.50 (50%).\n"
            "- [Tính đúng MRR] (1.0 điểm): Tính chính xác RR = 1/1 = 1.0 (100%).\n"
            "- [Diễn giải ý nghĩa nhiễu & bỏ sót] (1.0 điểm): Phân tích sâu sắc: 60% kết quả là nhiễu và bỏ sót 50% tài liệu liên quan trong kho."
        ),
        "reference_source": "Manning, Raghavan & Schütze: 'Introduction to Information Retrieval' (Cambridge University Press) - Chapter 8: Evaluation in information retrieval"
    },
    "d07-q062": {
        "sample_answer": (
            "1. Chấm điểm tính mạch lạc của từng chunk (Coherence & Boundary Assessment):\n"
            "- **Chunk A** (Kết thúc bằng 'Được hoàn phí nếu...'): Điểm kém / Lỗi đứt gãy biên ngữ nghĩa (Dangling Clause Defect). Mệnh đề điều kiện bị cắt cụt ở cuối, không cung cấp được điều kiện cụ thể để được hoàn tiền.\n"
            "- **Chunk B** (Bắt đầu bằng mức tiền nhưng thiếu điều kiện): Điểm kém / Lỗi mất ngữ cảnh dẫn nhập (Missing Antecedent Defect). Nêu con số tiền tệ nhưng không biết áp dụng cho trường hợp nào, gây rủi ro hiểu sai lệch chính sách.\n"
            "- **Chunk C** (Chứa hai chính sách không liên quan): Điểm kém / Lỗi ô nhiễm ngữ cảnh chéo (Cross-Topic Contamination Defect). Gộp hai chủ đề độc lập vào một chunk làm loãng vector embedding và gây nhiễu cho bước tạo sinh.\n"
            "2. Đề xuất sửa chữa theo đúng tầng kiến trúc (Layer-wise Repair Proposal):\n"
            "- Sửa chữa tầng Phân đoạn (Chunking Boundary Repair) cho Chunk A và B:\n"
            "  + Chuyển từ Fixed-length Chunking sang Sentence-boundary Chunking hoặc Recursive Character Splitting có phân tách theo dấu câu (`. `, `\n\n`).\n"
            "  + Áp dụng `chunk_overlap` từ 40-80 ký tự hoặc dùng Parent-Document Retriever để khi tìm thấy mệnh đề con, toàn bộ đoạn văn bản đầy đủ chứa cả điều kiện và mức tiền sẽ được đưa vào context.\n"
            "- Sửa chữa tầng Cấu trúc tài liệu (Document Structure Parsing) cho Chunk C:\n"
            "  + Bổ sung bước phân tách theo cấu trúc tiêu đề (Markdown Heading Splitter) trước khi chunking để mỗi chính sách nằm trong một ranh giới độc lập, không bị gộp chung."
        ),
        "explanation": (
            "Tính mạch lạc của chunk (Chunk Coherence) ảnh hưởng trực tiếp đến chất lượng embedding và khả năng suy luận của LLM. Các lỗi cắt ngang câu (broken syntax) "
            "và trộn lẫn chủ đề (topic contamination) phải được khắc phục tận gốc ở tầng tiền xử lý tài liệu và chiến lược phân đoạn, thay vì cố gắng xử lý bằng prompt."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đánh giá chính xác lỗi của Chunk A và B] (1.5 điểm): Chỉ ra lỗi đứt gãy mệnh đề ở Chunk A và mất ngữ cảnh dẫn nhập/điều kiện ở Chunk B.\n"
            "- [Đánh giá chính xác lỗi của Chunk C] (1.0 điểm): Nhận diện lỗi ô nhiễm ngữ cảnh chéo do gộp 2 chính sách không liên quan.\n"
            "- [Đề xuất sửa theo đúng tầng kiến trúc] (1.5 điểm): Đưa ra giải pháp chuẩn: Sentence-boundary/Parent-document cho A-B và Markdown heading splitting cho C."
        ),
        "reference_source": "LangChain Documentation: 'Text Splitters & Semantic Chunker' & LlamaIndex Document Processing Guide"
    }
}
