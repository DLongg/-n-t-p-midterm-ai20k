# -*- coding: utf-8 -*-
"""
Day 08 Part 1: Questions 1 to 28 (d08-q002 to d08-q058)
"""

DAY_08_PART1 = {
    "d08-q002": {
        "sample_answer": (
            "1. Lựa chọn cách xử lý cho từng vùng tài liệu:\n"
            "- Vùng 1 (Tiêu đề chữ rõ ràng): Trích xuất văn bản số trực tiếp (Digital Native Text Extraction) bằng thư viện PDF parser (như PyPDF, PDFMiner, pypdfium2) để thu nhận chuỗi ký tự nguyên bản, nhanh và chính xác 100% không qua OCR.\n"
            "- Vùng 2 (Bảng biểu trong ảnh): Sử dụng mô hình Table OCR nhận biết cấu trúc (ví dụ: Azure Document Intelligence Layout API, Table Transformer, hoặc Camelot) để nhận diện ranh giới ô, cấu trúc hàng - cột, xuất ra bảng Markdown hoặc HTML `<table>` nhằm bảo toàn mối liên hệ dữ liệu.\n"
            "- Vùng 3 (Sơ đồ mà mũi tên quyết định ý nghĩa): Không dùng OCR thuần túy. Sử dụng Mô hình Đa phương thức (Multimodal Vision-Language Model như GPT-4o, Claude 3.5 Sonnet, hoặc Gemini 1.5 Pro) với prompt chuyên biệt: 'Phân tích sơ đồ quy trình, nhận diện các nút và chiều mũi tên chỉ luồng quyết định, xuất thành mã Mermaid graph hoặc luồng tuần tự dạng If-Then-Else'.\n"
            "2. Mô tả bản trích xuất cuối cùng để không coi OCR là bằng chứng bố cục:\n"
            "Bản trích xuất cuối cùng là một tài liệu Markdown có cấu trúc ngữ nghĩa (Semantic Markdown), trong đó:\n"
            "- Tiêu đề được định dạng bằng `#` hoặc `##`.\n"
            "- Bảng biểu được chuyển thành định dạng Markdown Table chuẩn.\n"
            "- Sơ đồ được diễn giải thành luồng văn bản tường minh có thứ tự logic và khối mã `mermaid` biểu diễn đồ thị directed graph.\n"
            "Các khối dữ liệu được phân định bằng nhãn cấu trúc rõ ràng, tuyệt đối không phụ thuộc vào thứ tự dòng quét ngẫu nhiên từ OCR."
        ),
        "explanation": (
            "OCR truyền thống chỉ là bộ nhận diện ký tự quang học phẳng (Flat Character Recognizer), hoàn toàn mù đối với quan hệ không gian, thứ tự đọc hai cột, "
            "và ngữ nghĩa định hướng của mũi tên trong sơ đồ. Bộ trích xuất hiện đại phải là Layout-Aware & Multimodal Pipeline: phân vùng tài liệu thành các khối "
            "(Text, Table, Diagram) và áp dụng công cụ chuyên dụng cho từng khối để bảo toàn trọn vẹn ngữ nghĩa."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Xử lý riêng 3 vùng tài liệu] (1.5 điểm): Chọn đúng native text cho tiêu đề, table OCR cho bảng, và Multimodal VLM/Mermaid cho sơ đồ có mũi tên.\n"
            "- [Bản trích xuất cuối cùng] (1.5 điểm): Mô tả rõ định dạng Markdown cấu trúc phân cấp, bảng Markdown và đồ thị luồng quan hệ nhân quả.\n"
            "- [Không coi OCR là bằng chứng bố cục] (1.0 điểm): Khẳng định OCR thuần làm mất quan hệ mũi tên và yêu cầu cấu trúc hóa ngữ nghĩa thay vì phụ thuộc thứ tự quét."
        ),
        "reference_source": "Unstructured.io Documentation: 'Layout-Aware Document Partitioning and Multimodal Processing' & Microsoft Table-Transformer"
    },
    "d08-q004": {
        "sample_answer": (
            "1. Sửa chữa liên kết bị sai (Relational Association Repair):\n"
            "- Khắc phục lỗi rơi dấu `*`: Dấu `*` đại diện cho một ghi chú ngoại lệ (Footnote / Exception Rule). Trong bảng gốc, dấu `*` trỏ tới ngoại lệ chỉ áp dụng cho phòng Sales. Do OCR nhận diện sai vị trí làm rơi dấu sang hàng Marketing, hệ thống cần căn chỉnh lại tọa độ hình học (Bounding Box Alignment) hoặc sửa cấu trúc dữ liệu bảng: gỡ bỏ dấu `*` khỏi ô của phòng Marketing và gắn chính xác vào ô KPI tương ứng của phòng Sales.\n"
            "- Cấu trúc lại bảng: Gắn trực tiếp nội dung giải nghĩa của ghi chú chân trang `*` vào trường thuộc tính của phòng Sales: `\"phòng_ban\": \"Sales\", \"kpi\": \"...\", \"ghi_chu_ngoai_le\": \"Ngoại lệ chỉ áp dụng cho phòng Sales\"`.\n"
            "2. Các bước kiểm tra cần làm trước khi chọn cách biểu diễn lập chỉ mục (Pre-indexing Verification):\n"
            "- Kiểm tra 1 (Mối quan hệ Tiêu đề cột và Giá trị): Xác nhận mọi ô trong hàng đều ánh xạ đúng kiểu dữ liệu của tiêu đề cột (ví dụ cột có đơn vị `%` ở tiêu đề thì mọi giá trị bên dưới phải là tỷ lệ phần trăm hợp lệ từ 0 đến 100%).\n"
            "- Kiểm tra 2 (Toàn vẹn Hàng Tổng - Total Row Integrity): Kiểm tra logic tính toán: tổng các hàng phòng ban có khớp với Hàng Tổng hay không để phát hiện việc lệch hàng (Row Shift) do OCR.\n"
            "- Kiểm tra 3 (Tính cô lập của Ngoại lệ - Footnote Scoping): Đối chiếu văn bản ghi chú chân trang xem từ khóa của ghi chú (chỉ áp dụng Sales) có đồng nhất với vị trí neo dấu `*` đã sửa hay không."
        ),
        "explanation": (
            "Trong bảng biểu, dấu chú thích (Asterisk/Footnote) mang giá trị ngữ nghĩa điều kiện tối quan trọng. Nếu OCR làm trôi dạt dấu sao sang hàng khác, "
            "hệ thống RAG sẽ trả lời sai quy định cho cả hai phòng ban. Việc tiền kiểm tra quan hệ hàng-cột và kiểm chứng tính logic của hàng tổng là "
            "bước thẩm định bắt buộc trước khi đưa bảng vào chỉ mục vector."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Sửa liên kết dấu * chính xác] (1.5 điểm): Nêu rõ việc gỡ bỏ dấu * khỏi phòng Marketing và neo giữ đúng vào phòng Sales kèm giải nghĩa ngoại lệ.\n"
            "- [Kiểm tra quan hệ Tiêu đề & Đơn vị %] (1.0 điểm): Kiểm tra tính nhất quán giữa đơn vị % ở header và các giá trị trong cột.\n"
            "- [Kiểm tra logic Hàng Tổng và Footnote Scope] (1.5 điểm): Kiểm tra tính toán hàng tổng chống row-shift và xác minh phạm vi áp dụng của ghi chú."
        ),
        "reference_source": "Azure Document Intelligence Documentation: 'Table and Structure Extraction Best Practices' & LlamaIndex Table Parser"
    },
    "d08-q006": {
        "sample_answer": (
            "1. Quy tắc khiến lần chạy lại hội tụ lũy thừa (Idempotent Delta Convergence Rules):\n"
            "- Quy tắc 1 (Content-Hash Based Skip): Với 997 tệp giữ nguyên mã băm SHA-256 (`hash_current == hash_recorded`), hệ thống lập tức bỏ qua (No-Op / Skip), không trích xuất và không re-embed lại.\n"
            "- Quy tắc 2 (Transactional Upsert & Clean-up): Với 3 tệp có mã băm mới:\n"
            "  + Thao tác nguyên tử (Atomic Ingestion): Hệ thống xóa toàn bộ các chunk cũ của tài liệu qua lệnh `delete_by_doc_id(doc_id)` (hoặc sử dụng khóa ID đơn định `{doc_id}::{chunk_index}` với cơ chế overwrite).\n"
            "  + Nạp các chunk mới và ghi nhận trạng thái đã hoàn thành vào Bảng theo dõi trạng thái Ingestion (Checkpoint / State Store).\n"
            "- Tính hội tụ (Idempotency): Do mỗi tệp được xử lý độc lập và có trạng thái ghi nhận mã băm đã xử lý, khi tác vụ bị dừng lỗi và chạy lại từ đầu, hệ thống chỉ kiểm tra mã băm và tiếp tục xử lý những tệp chưa hoàn tất; kết quả cuối cùng của kho dữ liệu luôn đồng nhất dù chạy lại 1 lần hay 10 lần.\n"
            "2. Phần thuộc vòng đời độ mới chưa cần giải quyết trong câu này:\n"
            "- Vấn đề **Phát hiện và Xóa các tài liệu đã bị xóa khỏi hệ thống nguồn (Deletions / Tombstones / Pruning Lifecycle)**: Kịch bản trên chỉ đề cập đến việc đọc lại các tệp hiện có trong lô để cập nhật (Upsert/Skip). Quy trình đồng bộ các tệp bị xóa khỏi nguồn (Hard/Soft Deletes) thuộc về bài toán thu dọn rác (Garbage Collection / Tombstone Pruning) và sẽ được giải quyết ở quy trình riêng."
        ),
        "explanation": (
            "Tính lũy thừa (Idempotency) là thuộc tính sống còn của các đường ống nạp dữ liệu lớn (Big Data / RAG Ingestion). Khi có sự cố đứt gãy giữa chừng, "
            "hệ thống có thể chạy lại từ đầu mà không sinh ra dữ liệu trùng lặp (duplicate records) và không lãng phí chi phí tính toán cho các tệp không thay đổi."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quy tắc bỏ qua dựa trên Content Hash] (1.5 điểm): Nêu rõ việc so sánh mã băm để bỏ qua 997 tệp không đổi, tránh re-indexing lãng phí.\n"
            "- [Cơ chế Atomic Upsert cho 3 tệp mới] (1.5 điểm): Mô tả việc xóa chunk cũ và nạp chunk mới nguyên tử kèm lưu checkpoint hội tụ.\n"
            "- [Chỉ rõ phần vòng đời độ mới tách biệt] (1.0 điểm): Nhận diện chính xác bài toán phát hiện tài liệu bị xóa nguồn (tombstone/deletion sync) là phần tách biệt."
        ),
        "reference_source": "Databricks / Delta Lake Architecture: 'Idempotent Data Ingestion and Checkpointing' & Pinecone Data Freshness Guide"
    },
    "d08-q008": {
        "sample_answer": (
            "1. Thiết kế định danh và ánh xạ Parent-Child (Identity & Mapping Architecture):\n"
            "- Định danh Child Chunk (Search Unit): Khóa chính bao gồm thông tin phiên bản để phân biệt tuyệt đối: `child_id = \"{doc_id}::{version}::child_{idx}\"`.\n"
            "- Định danh Parent Chunk (Context Unit): `parent_id = \"{doc_id}::{version}::parent_{idx}\"`.\n"
            "- Trường ánh xạ (Explicit Foreign Key): Trong metadata của mỗi Child Chunk bắt buộc phải lưu trường tham chiếu `parent_id` trỏ chính xác về Parent Chunk của cùng phiên bản đó.\n"
            "- Quy trình truy xuất: Tìm kiếm vector được thực hiện trên các Child Chunks (đơn vị nhỏ, độ sắc nét ngữ nghĩa cao). Khi Child Chunk được chọn, hệ thống dùng `parent_id` để tra cứu trong Document Store và lấy Parent Chunk tương ứng (đơn vị lớn, ngữ cảnh đầy đủ) nạp vào prompt của LLM.\n"
            "2. Bộ lọc bắt buộc cần có (Mandatory Version Filter):\n"
            "- Bổ sung bộ lọc tiền truy vấn (Metadata Pre-filtering): `filter = {\"is_active\": true, \"version\": \"current_active_version\"}`.\n"
            "- Tác dụng: Ngăn chặn triệt để việc Child Chunk của phiên bản cũ lọt vào danh sách xếp hạng tìm kiếm, từ đó triệt tiêu hoàn toàn nguy cơ lấy nhầm Parent Chunk của chính sách đã hết hạn."
        ),
        "explanation": (
            "Kiến trúc Parent-Child Retrieval tách rời đơn vị tìm kiếm (Child Chunk: 100-200 tokens) khỏi đơn vị tạo sinh (Parent Chunk: 500-1000 tokens). "
            "Để tránh nhầm lẫn giữa các phiên bản có câu chữ tương tự, khóa tham chiếu ngoại (parent_id) phải được định danh cùng không gian phiên bản và "
            "kết hợp chặt chẽ với bộ lọc hiệu lực (is_active filter)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đặc tả ID & Quan hệ tham chiếu Parent-Child] (1.5 điểm): Thiết kế ID duy nhất gắn kèm version cho cả child và parent, có foreign key parent_id rõ ràng.\n"
            "- [Cơ chế truy xuất phân tầng] (1.0 điểm): Nêu rõ child chunk là đơn vị tìm kiếm vector và parent chunk là đơn vị đưa vào context.\n"
            "- [Thiết kế bộ lọc Metadata phiên bản] (1.5 điểm): Đưa ra bộ lọc bắt buộc is_active=true để loại bỏ triệt để child chunk phiên bản cũ."
        ),
        "reference_source": "LangChain Documentation: 'ParentDocumentRetriever' & LlamaIndex 'RecursiveRetriever and Node References'"
    },
    "d08-q010": {
        "sample_answer": (
            "1. Xác định vị trí và nguyên nhân lỗi (Defect Localization):\n"
            "- Lỗi nằm ở **Tầng Định dạng Ngữ cảnh (Context Formatting / Packaging Layer)**, cụ thể là sự không nhất quán giữa cơ chế trích dẫn của mô hình và việc thay đổi định danh của bộ định dạng (ID Remapping Defect):\n"
            "  + Bộ định dạng đã tự ý đổi mã tài liệu gốc `doc-9` thành số thứ tự cục bộ (ví dụ: `[1]`, `[2]`, `[3]`).\n"
            "  + Tuy nhiên, LLM vẫn ghi nhớ hoặc bị lẫn với ID gốc `doc-9` (hoặc do trong prompt vẫn còn sót chuỗi `doc-9`), dẫn đến việc câu trả lời trích dẫn `doc-9` trong khi ngữ cảnh hiển thị chỉ có `doc-3`.\n"
            "2. Thành phần và Thời điểm cần ghi nhật ký để tái hiện và kiểm toán (Audit Logging Strategy):\n"
            "- Thời điểm 1 (Sau bước Retrieval / Reranking): Ghi log danh sách ứng viên đã xếp hạng: `ranked_candidates = [{rank: 1, doc_id: 'doc-9', score: 0.92}, {rank: 2, doc_id: 'doc-3', score: 0.88}]`.\n"
            "- Thời điểm 2 (Sau bước Context Formatting / Prompt Assembly): Ghi log nguyên văn chuỗi ngữ cảnh được tiêm vào LLM kèm bảng ánh xạ ID (ID Mapping Table): `formatted_context = \"...\"`, `id_map = {\"[1]\": \"doc-9\", \"[2]\": \"doc-3\"}`.\n"
            "- Thời điểm 3 (Sau bước Generation): Ghi log đầu ra thô của LLM và bước Citation Validator kiểm tra xem mọi ID trích dẫn có nằm trong tập ID được phép của `formatted_context` hay không."
        ),
        "explanation": (
            "Trong hệ thống RAG phức tạp, sự trôi dạt định danh (ID Drift) giữa các tầng trung gian (Retrieval -> Formatting -> Prompt Injection -> Generation) "
            "là nguyên nhân phổ biến gây lỗi trích dẫn ảo (Phantom Citation). Việc duy trì bảng ánh xạ tường minh và log đầy đủ các artifact trung gian là "
            "bắt buộc để đảm bảo khả năng tái hiện lỗi."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Xác định đúng tầng lỗi] (1.5 điểm): Chỉ ra lỗi ở bước Context Formatting tự ý đổi ID làm mất tính nhất quán giữa prompt và citation của model.\n"
            "- [Kế hoạch Logging 3 thời điểm then chốt] (1.5 điểm): Nêu rõ log tại thời điểm sau ranking (ranked candidates), sau formatting (formatted prompt & ID map), và sau generation.\n"
            "- [Cơ chế Citation Validation] (1.0 điểm): Đề xuất bước kiểm tra tự động xem citation có thuộc tập ID hợp lệ trong context hay không."
        ),
        "reference_source": "TruLens Documentation: 'Tracking Artifacts and Traceability in RAG Pipelines' & LangSmith Observability Guide"
    },
    "d08-q012": {
        "sample_answer": (
            "1. Có nên chỉ dùng bộ trích xuất native không?\n"
            "**KHÔNG.** Tuyệt đối không chỉ dùng bộ trích xuất native trong trường hợp này. "
            "Căn cứ: Trích xuất native chỉ đọc được các chuỗi ký tự rời rạc và trả về dạng danh sách tuyến tính phẳng, làm mất hoàn toàn quan hệ cấu trúc mạng: nút nguồn -> nhãn mũi tên -> nút đích. Đối với sơ đồ quy trình, mất quan hệ mũi tên đồng nghĩa với việc mất toàn bộ logic nghiệp vụ (thứ tự bước, điều kiện rẽ nhánh).\n"
            "2. Phương án dự phòng và quy trình định tuyến (Fallback & Multimodal Pipeline):\n"
            "- Định tuyến thông minh: Khi bộ phát hiện vùng (Layout Detector) phân loại một khối là 'Diagram/Flowchart', hệ thống định tuyến khối này sang Bộ xử lý Thị giác - Đa phương thức (Multimodal VLM Pipeline như GPT-4o Vision hoặc Claude 3.5 Sonnet).\n"
            "- Kỹ thuật trích xuất: Cung cấp ảnh crop của sơ đồ kèm danh sách chữ native (làm gợi ý chống đọc sai chữ) và prompt: 'Trích xuất cấu trúc đồ thị luồng dưới dạng Mermaid flowchart hoặc danh sách các cạnh có hướng: Node A --[Điều kiện]--> Node B'.\n"
            "3. Giới hạn của kết luận (Boundary of Conclusion):\n"
            "Kết luận này áp dụng cho các sơ đồ chứa quan hệ đồ thị/hình học; đối với các khối văn bản đoạn văn thông thường trên cùng trang tài liệu, bộ trích xuất native vẫn là lựa chọn số một về tốc độ và chi phí, không nên chuyển đổi toàn bộ trang sang VLM một cách lãng phí."
        ),
        "explanation": (
            "Trích xuất văn bản từ sơ đồ là một tác vụ đa phương thức thực thụ: ý nghĩa không chỉ nằm ở ký tự mà nằm ở cấu trúc hình học và liên kết không gian (Spatial & Graph Topology). "
            "Sự kết hợp giữa Text Extractor và Multimodal VLM là giải pháp tối ưu vừa đảm bảo độ chính xác ký tự vừa bảo toàn đồ thị quan hệ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Khẳng định không chỉ dùng native] (1.0 điểm): Bác bỏ việc chỉ dùng native extractor vì làm mất quan hệ nút-mũi tên.\n"
            "- [Thiết kế Fallback Multimodal VLM] (1.5 điểm): Đề xuất pipeline kết hợp ảnh crop sơ đồ và mô hình đa phương thức xuất ra định dạng Mermaid/Graph edges.\n"
            "- [Xác định rõ giới hạn kết luận] (1.5 điểm): Nêu rõ giới hạn áp dụng: chỉ định tuyến vùng sơ đồ sang VLM, giữ native text cho các đoạn văn thông thường để tối ưu chi phí/độ trễ."
        ),
        "reference_source": "LlamaIndex Documentation: 'Multimodal Parsing and Flowchart Extraction' & Anthropic Vision Guides"
    },
    "d08-q014": {
        "sample_answer": (
            "1. Sửa chữa quy trình vòng đời đồng bộ (Freshness Lifecycle Repair):\n"
            "- Bổ sung cơ chế Đồng bộ xóa (Deletion / Tombstone Synchronization) vào tác vụ delta ingestion:\n"
            "  + Phương pháp 1 (Source Event/Webhook Triggered): Khi một tài liệu bị xóa ở hệ thống nguồn, nguồn phát sự kiện `DocumentDeleted(doc_id)`. Tác vụ delta nhận sự kiện và gọi ngay lệnh xóa triệt để: `vector_store.delete(filter={\"doc_id\": doc_id})`.\n"
            "  + Phương pháp 2 (Full Reconciliation Loop with Tombstones): Trong tác vụ batch định kỳ, lấy danh sách `active_doc_ids` từ hệ thống nguồn và so sánh với `indexed_doc_ids` trong Vector Store. Những ID tồn tại trong index nhưng không còn trong nguồn sẽ bị đưa vào danh sách xóa (Purge List) và thực hiện xóa hàng loạt.\n"
            "2. Phép kiểm phân biệt Bằng chứng cũ (Stale Evidence) với Lỗi xếp hạng ở Retrieval (Ranking Defect):\n"
            "- Kiểm tra trạng thái tồn tại của bản ghi trong nguồn (Source Existence Verification): Khi một chunk bị nghi ngờ xuất hiện trong kết quả search, thực hiện truy vấn trực tiếp vào Cơ sở dữ liệu nguồn bằng `doc_id` của chunk đó.\n"
            "  + Nếu bản ghi **không còn tồn tại trong nguồn** (đã bị xóa): Kết luận đây là **Lỗi độ tươi chỉ mục / Bằng chứng cũ (Stale Index / Deletion Lag Defect)**. Tầng retrieval không có lỗi vì nó chỉ tìm kiếm trên những gì đang có trong index.\n"
            "  + Nếu bản ghi **vẫn tồn tại trong nguồn** nhưng nội dung không liên quan mà vẫn đứng Top-1: Kết luận đây là **Lỗi xếp hạng truy xuất (Retrieval / Ranking Defect)**."
        ),
        "explanation": (
            "Vòng đời dữ liệu trong hệ thống RAG không chỉ có Insert và Update mà bắt buộc phải có Deletion Synchronization. Hiện tượng tài liệu 'ma' "
            "(Ghost Documents) vẫn xuất hiện sau khi đã bị xóa khỏi nguồn là lỗi nghiêm trọng về an toàn và bảo mật thông tin. Cần có phép kiểm tra phân định rõ "
            "giữa lỗi dữ liệu lỗi thời và lỗi thuật toán tìm kiếm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Bổ sung cơ chế đồng bộ xóa] (1.5 điểm): Thiết lập cơ chế xóa dựa trên sự kiện webhook hoặc vòng quét đối soát reconciliation loop để xóa triệt để chunk cũ.\n"
            "- [Phép kiểm tra phân biệt rạch ròi] (1.5 điểm): Tra cứu ID trong nguồn: nếu nguồn đã xóa mà index còn -> lỗi Stale Index; nếu nguồn còn mà rank cao vô lý -> lỗi Retrieval Ranking.\n"
            "- [Chính sách kiểm soát toàn vẹn] (1.0 điểm): Nhấn mạnh tầm quan trọng của việc dọn dẹp tombstone định kỳ để giữ index trong sạch."
        ),
        "reference_source": "Pinecone Learning Center: 'Managing Vector Deletions and Stale Data' & Milvus Documentation: 'Delete Entities'"
    },
    "d08-q016": {
        "sample_answer": (
            "1. Thiết kế hai cách biểu diễn bảng dữ liệu (Two Table Representations):\n"
            "- **Biểu diễn 1: Bản ghi phân rã theo hàng (Row-level Structured Representation)**:\n"
            "  + Cấu trúc: Mỗi hàng trong bảng được tách thành một chunk độc lập, kết hợp tiêu đề cột và ngữ cảnh tên bảng. Ví dụ: `[Chính sách hoàn phí] - Điều kiện: Hủy trước 7 ngày | Mức phạt: 0% | Ngoại lệ: Áp dụng cho mọi học viên`.\n"
            "  + Mục đích: Phục vụ tối ưu cho các truy vấn điều kiện chi tiết, cụ thể của người dùng, giúp vector embedding có độ hội tụ ngữ nghĩa cao và khớp chính xác từng quy định nhỏ.\n"
            "- **Biểu diễn 2: Bản tóm tắt toàn bộ bảng (Table-level Summary / Full Table Markdown)**:\n"
            "  + Cấu trúc: Một chunk duy nhất chứa toàn bộ bảng Markdown kèm đoạn văn bản tóm tắt tổng quan: `Bảng quy định toàn diện về chính sách phạt hủy khóa học bao gồm 3 trường hợp: hủy sớm, hủy sát ngày và trường hợp bất khả kháng...`.\n"
            "  + Mục đích: Phục vụ cho các truy vấn mang tính khái quát, yêu cầu tóm tắt toàn bộ chính sách hoặc so sánh tổng thể các mức phạt.\n"
            "2. Thiết kế phép kiểm tra so sánh độ phủ (Coverage Comparison Test):\n"
            "- Xây dựng tập kiểm thử gồm 2 nhóm câu hỏi chuẩn: 10 câu hỏi tra cứu điều kiện chi tiết và 10 câu hỏi tóm tắt toàn bảng.\n"
            "- Đo lường chỉ số **Fact Recall / Context Completeness**: Kiểm tra xem câu trả lời được sinh ra có bao phủ đầy đủ tất cả các mức phạt và ngoại lệ hay không. Đánh giá tỷ lệ câu hỏi chi tiết tìm thấy đúng hàng tương ứng và tỷ lệ câu hỏi tổng quát bao phủ được toàn bộ bảng."
        ),
        "explanation": (
            "Bảng biểu vừa chứa dữ liệu chi tiết ở từng ô/hàng vừa chứa bức tranh tổng thể ở cấp độ bảng. Không có một dạng biểu diễn đơn lẻ nào phục vụ hoàn hảo "
            "cả hai loại câu hỏi này. Phương pháp Multi-Vector Representation (lưu đồng thời bản tóm tắt bảng và các hàng chi tiết có liên kết cha-con) "
            "là giải pháp chuẩn hóa cho dữ liệu bảng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Biểu diễn chi tiết theo hàng] (1.5 điểm): Thiết kế biểu diễn từng hàng kết hợp tiêu đề cột để phục vụ truy vấn chi tiết.\n"
            "- [Biểu diễn tóm tắt toàn bảng] (1.5 điểm): Thiết kế biểu diễn tổng quan bảng Markdown kèm tóm tắt để phục vụ truy vấn khái quát.\n"
            "- [Thiết kế phép kiểm so sánh độ phủ] (1.0 điểm): Xây dựng testset chia 2 nhóm query và đo lường Fact Recall / Completeness."
        ),
        "reference_source": "LlamaIndex Documentation: 'Table Parsing and Multi-Vector Representation for Tables' & LangChain Table Retrievers"
    },
    "d08-q018": {
        "sample_answer": (
            "1. Thiết kế Quy tắc Kích hoạt có Điều kiện (Query Transformation Gating Rules):\n"
            "Tuyệt đối không chạy rewrite cho mọi query. Thiết lập một bộ kiểm soát cổng (Gating Classifier / Decision Tree) phân loại câu hỏi trước khi quyết định biến đổi:\n"
            "- **Điều kiện BỎ QUA Rewrite (Direct Retrieval Bypass)**:\n"
            "  + Câu hỏi có độ dài đủ lớn (ví dụ >= 6 từ), chứa rõ ràng các thực thể xác định (Named Entities như tên sản phẩm cụ thể, mã lỗi chuẩn, thuật ngữ chuyên ngành).\n"
            "  + Câu hỏi độc lập không chứa đại từ thay thế mơ hồ (anaphora như 'nó', 'chính sách này', 'bước trên').\n"
            "  + Hành động: Bỏ qua rewrite, chuyển thẳng tới Direct Retrieval để bảo toàn SLA độ trễ (tiết kiệm 350 ms) và tránh làm sai lệch tên sản phẩm.\n"
            "- **Điều kiện KÍCH HOẠT Rewrite (Transform Trigger)**:\n"
            "  + Câu hỏi trong chuỗi hội thoại đa lượt có đại từ tham chiếu ('sản phẩm đó giá bao nhiêu?').\n"
            "  + Câu hỏi quá ngắn (< 3 từ), mơ hồ hoặc có dấu hiệu sai lỗi chính tả nghiêm trọng.\n"
            "2. Cách xử lý khi lỗi và phương án dự phòng (Fallback & Error Handling):\n"
            "- Giới hạn thời gian chờ (Timeout Budget): Áp dụng timeout nghiêm ngặt cho dịch vụ rewrite (ví dụ: `timeout = 250 ms`). Nếu rewrite bị timeout hoặc lỗi mạng, hệ thống lập tức fallback sử dụng câu hỏi gốc nguyên bản của người dùng.\n"
            "- Kiểm tra tính bảo toàn thực thể (Entity Preservation Check): So khớp thực thể trước và sau rewrite. Nếu phát hiện tên sản phẩm gốc bị biến đổi hoặc mất đi, hệ thống hủy kết quả rewrite và sử dụng query gốc."
        ),
        "explanation": (
            "Query Rewriting mang lại giá trị lớn cho các câu hỏi mơ hồ nhưng lại là gánh nặng độ trễ và rủi ro xuyên tạc thực thể (Entity Hallucination) "
            "đối với các câu hỏi đã rõ ràng. Việc thiết lập cổng kiểm soát (Gating) và cơ chế bảo toàn thực thể là nguyên tắc tối ưu hóa hiệu năng trong kiến trúc RAG."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế quy tắc Gating rõ ràng] (1.5 điểm): Xác định đúng điều kiện bypass (câu hỏi dài, rõ thực thể, độc lập) và điều kiện kích hoạt (câu hỏi ngắn, đa lượt, tham chiếu đại từ).\n"
            "- [Bảo toàn tên thực thể] (1.0 điểm): Nhấn mạnh cơ chế kiểm tra bảo toàn thực thể, chống rewrite làm sai lệch tên sản phẩm.\n"
            "- [Cơ chế Fallback & Timeout] (1.5 điểm): Thiết lập timeout budget cho rewrite và fallback an toàn về query gốc khi gặp sự cố."
        ),
        "reference_source": "LangChain Documentation: 'Query Transformations and Fallback Routing' & Cohere / LlamaIndex Query Rewriting Guides"
    },
    "d08-q020": {
        "sample_answer": (
            "1. Phân tích ngữ cảnh người dùng:\n"
            "Query gốc: `vector db chi phi`.\n"
            "Ngữ cảnh quan sát được: Người dùng đang trong quá trình khảo sát và lựa chọn hạ tầng kỹ thuật (Infrastructure Selection).\n"
            "Ý định thực sự: Tìm hiểu về tổng chi phí sở hữu (Total Cost of Ownership - TCO) khi triển khai cơ sở dữ liệu vector, bao gồm chi phí bản quyền/dịch vụ đám mây (Cloud hosting / DBaaS pricing), chi phí hạ tầng phần cứng (RAM, CPU, GPU, Storage) và chi phí vận hành bảo trì; KHÔNG PHẢI chi phí tính toán độ phức tạp thuật toán khoảng cách vector (distance computation algorithmic complexity).\n"
            "2. Thiết kế mở rộng Query có kiểm soát (Contextual Query Expansion):\n"
            "Mở rộng câu hỏi bằng cách bổ sung các từ đồng nghĩa và thuật ngữ hạ tầng liên quan trực tiếp đến ngữ cảnh lựa chọn công nghệ, giữ nguyên ý định mà không bịa thêm tính năng ngoài luồng:\n"
            "- **Query mở rộng dạng từ khóa (Lexical / BM25 expansion)**:\n"
            "  `vector database chi phí giá dịch vụ cloud hosting pricing TCO hạ tầng server RAM storage`\n"
            "- **Query mở rộng dạng ngữ nghĩa đầy đủ (Dense / Semantic expansion)**:\n"
            "  `Chi phí bản quyền và hạ tầng triển khai cơ sở dữ liệu vector bao gồm giá cloud managed service và phần cứng vận hành`\n"
            "3. Ranh giới an toàn ngăn chặn bịa thêm ý định:\n"
            "- Chỉ bổ sung các khía cạnh trực thuộc khái niệm 'chi phí hạ tầng' (hosting, pricing, hardware, cloud).\n"
            "- Tuyệt đối không tự ý thêm thắt các tiêu chí so sánh hiệu năng (như latency benchmark, HNSW vs IVF, hay tính năng hybrid search) vì người dùng chưa hề yêu cầu."
        ),
        "explanation": (
            "Mở rộng truy vấn (Query Expansion) phải tuân thủ nguyên tắc bảo toàn ý định (Intent-Preserving Expansion). Bổ sung từ đồng nghĩa và thuật ngữ "
            "ngữ cảnh hạ tầng giúp hệ thống bao phủ các tài liệu báo giá và phân tích TCO, trong khi việc kiểm soát ranh giới nghiêm ngặt ngăn chặn việc làm loãng "
            "không gian tìm kiếm bằng các chủ đề không liên quan."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân tích ngữ cảnh lựa chọn hạ tầng] (1.0 điểm): Xác định đúng ý định người dùng là chi phí tài chính/hạ tầng (TCO, cloud, hosting) chứ không phải độ phức tạp tính toán.\n"
            "- [Thiết kế Query mở rộng chuẩn xác] (1.5 điểm): Đưa ra các query mở rộng hợp lý cho cả sparse và dense, bổ sung từ đồng nghĩa có kiểm soát.\n"
            "- [Ranh giới chống bịa đặt ý định] (1.5 điểm): Khẳng định không thêm thắt các tiêu chí so sánh hiệu năng/thuật toán ngoài luồng yêu cầu."
        ),
        "reference_source": "Manning, Raghavan & Schütze: 'Introduction to Information Retrieval' - Chapter 9: Relevance feedback and query expansion"
    },
    "d08-q022": {
        "sample_answer": (
            "1. Ranh giới câu hỏi con và thứ tự phụ thuộc (Query Decomposition):\n"
            "Câu hỏi gốc: 'Ai phê duyệt việc mua phần mềm và giới hạn số tiền người đó được phê duyệt là bao nhiêu?'.\n"
            "Phân tích quan hệ: Đây là bài toán truy xuất đa chặng có phụ thuộc tuần tự (Sequential Multi-hop Dependency): Vế thứ hai (giới hạn số tiền) phụ thuộc trực tiếp vào kết quả của vế thứ nhất (danh tính/vai trò người phê duyệt).\n"
            "- **Bước 1 (Truy xuất Danh tính / Vai trò người phê duyệt)**:\n"
            "  + Query con 1: `\"Vai trò hoặc cấp bậc nào có thẩm quyền phê duyệt mua sắm phần mềm?\"`\n"
            "  + Nguồn nhắm tới: Nguồn A (Quy trình mua sắm phần mềm / Phân quyền thẩm quyền).\n"
            "  + Kết quả trung gian trích xuất được: `role = \"Trưởng phòng CNTT / IT Director\"`.\n"
            "- **Bước 2 (Truy xuất Giới hạn số tiền dựa trên kết quả Bước 1)**:\n"
            "  + Query con 2: Tiêm trực tiếp kết quả của Bước 1 vào câu hỏi con thứ hai: `\"Hạn mức số tiền tối đa được phê duyệt mua sắm của Trưởng phòng CNTT (IT Director) là bao nhiêu?\"`\n"
            "  + Nguồn nhắm tới: Nguồn B (Bảng hạn mức phê duyệt tài chính theo vai trò).\n"
            "  + Kết quả trung gian trích xuất được: `limit = \"500 triệu VNĐ\"`.\n"
            "2. Tái hợp nhất câu trả lời (Recomposition & Synthesis):\n"
            "- Tổng hợp hai bằng chứng đã trích xuất từ Nguồn A và B vào câu trả lời cuối cùng: 'Theo quy định mua sắm, Trưởng phòng CNTT là người có thẩm quyền phê duyệt việc mua phần mềm [Nguồn A], và hạn mức phê duyệt tối đa của vai trò này là 500 triệu VNĐ [Nguồn B].'\n"
            "3. Ràng buộc không dùng trí nhớ nội tại của model:\n"
            "- Nếu Bước 1 không tìm thấy vai trò hoặc Bước 2 không tìm thấy hạn mức từ nguồn tài liệu, hệ thống bắt buộc phải dừng và tuyên bố thiếu bằng chứng, tuyệt đối không cho phép LLM tự 'đoán' hạn mức dựa trên kiến thức thông thường ngoài đời."
        ),
        "explanation": (
            "Với các câu hỏi phức hợp đa chặng (Multi-hop Queries), việc truy xuất một lần (Single-step Retrieval) sẽ thất bại vì nguồn B không thể tìm kiếm "
            "chính xác nếu chưa biết vai trò trích xuất được từ nguồn A. Kỹ thuật Phân rã và Tái hợp nhất (Decompose-and-Recompose / Sub-question Querying) "
            "giúp kết nối thông tin giữa các tài liệu rời rạc một cách có căn cứ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân rã đúng 2 câu hỏi con có phụ thuộc] (1.5 điểm): Xác định Bước 1 tìm vai trò ở Nguồn A và Bước 2 dùng vai trò đó để tra hạn mức ở Nguồn B.\n"
            "- [Quy trình tái hợp nhất câu trả lời] (1.0 điểm): Mô tả rõ bước tổng hợp kết quả kèm trích dẫn Nguồn A và Nguồn B.\n"
            "- [Chặn sử dụng trí nhớ mô hình] (1.5 điểm): Nhấn mạnh quy tắc không dùng kiến thức chung của LLM để lấp chỗ trống nếu tài liệu bị khuyết thiếu."
        ),
        "reference_source": "LlamaIndex Documentation: 'Sub Question Query Engine' & Press et al. (2022): 'Measuring and Reducing LLM Hallucination without Gold Answers'"
    },
    "d08-q024": {
        "sample_answer": (
            "1. Phân tích nguyên nhân truy vấn trực tiếp thất bại:\n"
            "- Query trực tiếp `E419-X` thất bại vì tài liệu hướng dẫn không liệt kê mã lỗi chi tiết cấp thấp `E419-X` trong tiêu đề hoặc văn bản chính, mà tài liệu được tổ chức phân cấp theo các khái niệm trừu tượng cấp cao: nhóm Authentication (Xác thực) và Session Expiry (Hết hạn phiên làm việc).\n"
            "2. Thiết kế Stepback Query (Khái quát hóa có định hướng):\n"
            "- Nguyên lý Step-back Prompting: Lùi lại một bước để đặt câu hỏi về nguyên lý nền tảng hoặc khái niệm chi phối (Governing Principle), nhưng giữ nguyên ngữ cảnh ứng dụng thay vì biến thành câu hỏi chung chung vô nghĩa.\n"
            "- **Query Stepback được chọn**:\n"
            "  `\"Cơ chế xử lý lỗi xác thực và chính sách hết hạn phiên làm việc (authentication and session expiry error handling)\"`\n"
            "3. Biện minh vì sao không mở rộng thành 'mọi lỗi API':\n"
            "- Nếu mở rộng thành 'mọi lỗi API' (All API Errors): Ngữ nghĩa bị loãng hoàn toàn (Semantic Dilution), hệ thống sẽ truy xuất hàng trăm chunk về lỗi 400 Bad Request, 500 Server Error, Rate Limit... làm tràn ngập context bằng thông tin rác và đẩy phần kiến thức về session đi xa khỏi Top-K.\n"
            "- Query Stepback chọn lọc ở trên vừa đủ khái quát để khớp với nhóm tài liệu Authentication/Session Expiry, vừa đủ hẹp để giữ tỷ lệ tín hiệu trên nhiễu (Signal-to-Noise Ratio) ở mức cao nhất."
        ),
        "explanation": (
            "Kỹ thuật Step-back Querying giúp giải quyết khoảng cách từ vựng (Vocabulary Mismatch) khi người dùng hỏi các chi tiết quá cụ thể "
            "mà tài liệu chỉ giải thích ở cấp độ khái niệm chi phối. Sự cân bằng giữa mức độ khái quát (Generality) và sự tập trung chuyên đề (Specificity) "
            "là chìa khóa để retrieval thành công."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán nguyên nhân thất bại] (1.0 điểm): Nhận diện lỗi từ vựng chi tiết (E419-X) không khớp với cách tổ chức phân cấp của tài liệu (Authentication/Session).\n"
            "- [Thiết kế Stepback Query chuẩn xác] (1.5 điểm): Đưa ra câu hỏi khái quát hóa đúng trọng tâm về cơ chế xác thực và hết hạn phiên.\n"
            "- [Biện minh không mở rộng thành mọi lỗi API] (1.5 điểm): Giải thích rõ việc mở rộng quá đà làm loãng ngữ nghĩa, tràn nhiễu và mất tính hữu dụng."
        ),
        "reference_source": "Zheng et al. (2023): 'Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models' & LangChain Step-Back Prompting"
    },
    "d08-q026": {
        "sample_answer": (
            "1. Đánh giá quyết định chạy HyDE cho mọi query (Evaluation of Universal HyDE):\n"
            "Quyết định này là **SAI LẦM VÀ LÃNG PHÍ KỸ THUẬT (Architectural Anti-Pattern)**:\n"
            "- Lãng phí độ trễ và chi phí: HyDE (Hypothetical Document Embeddings) đòi hỏi một lượt gọi LLM để sinh tài liệu giả định trước khi embed. Việc này làm tăng thêm từ 500 ms đến 1.500 ms độ trễ và tốn thêm token chi phí cho mỗi lượt tìm kiếm.\n"
            "- Rủi ro suy thoái chất lượng: Khi truy vấn trực tiếp đã xếp đúng nguồn ở vị trí 1 với độ trễ thấp, việc áp dụng HyDE có thể khiến tài liệu giả định sinh ra chứa các chi tiết ảo tưởng (hallucinated facts), làm lệch vector tìm kiếm ra khỏi nguồn đúng ban đầu.\n"
            "2. Điều kiện kích hoạt HyDE phù hợp (Gating / Trigger Conditions):\n"
            "Chỉ kích hoạt HyDE khi thỏa mãn một trong các điều kiện sau:\n"
            "- Điều kiện 1: Truy vấn có khoảng cách từ vựng lớn (High Vocabulary Mismatch) giữa câu hỏi và tài liệu trả lời (ví dụ: câu hỏi dạng tại sao/nguyên lý mà corpus chỉ chứa câu trả lời văn bản dài).\n"
            "- Điều kiện 2: Truy vấn trực tiếp trả về điểm tin cậy tương đồng vector quá thấp (`max_similarity_score < threshold`, ví dụ < 0.65).\n"
            "3. Phương án dự phòng và kiểm soát (Fallback Strategy):\n"
            "Nếu sau khi chạy HyDE mà kết quả tìm kiếm có điểm tương đồng thấp hơn hoặc phân tán hơn so với tìm kiếm trực tiếp, hệ thống lập tức fallback sử dụng danh sách kết quả của lượt tìm kiếm trực tiếp ban đầu."
        ),
        "explanation": (
            "HyDE được thiết kế để giải quyết bài toán bất đối xứng ngữ nghĩa giữa câu hỏi ngắn và văn bản trả lời dài. Tuy nhiên, nó là một công cụ tốn kém "
            "về tài nguyên tính toán. Việc triển khai HyDE mù quáng cho 100% truy vấn vi phạm nguyên tắc thiết kế tiết kiệm (Lean Systems) và làm giảm SLO trải nghiệm người dùng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đánh giá đúng sai lầm chạy HyDE toàn bộ] (1.5 điểm): Phê phán có căn cứ: lãng phí độ trễ (500-1500ms), tốn chi phí LLM và nguy cơ hallucination làm lệch vector đúng.\n"
            "- [Xác định điều kiện kích hoạt có chọn lọc] (1.5 điểm): Đưa ra các trigger cụ thể: khoảng cách từ vựng lớn hoặc khi direct search trả điểm tin cậy thấp.\n"
            "- [Cơ chế Fallback an toàn] (1.0 điểm): Thiết lập cơ chế fallback về direct retrieval khi HyDE không cải thiện kết quả."
        ),
        "reference_source": "Gao et al. (2022): 'Precise Zero-Shot Dense Retrieval without Relevance Labels' (HyDE Paper) & LangChain HyDE Documentation"
    },
    "d08-q028": {
        "sample_answer": (
            "1. Phân biệt hai trường hợp bản chất khác nhau:\n"
            "- **Trường hợp A: Không có kết quả trong phạm vi được cấp quyền (Out-of-Scope / Authorization Constraint)**:\n"
            "  + Bản chất: Người dùng chỉ có quyền xem chính sách đang có hiệu lực (`is_active = true`). Bộ lọc quyền (RBAC / Tenant Scope Filter) hoạt động hoàn hảo và xác nhận rằng: Trong tập các tài liệu mà người dùng *được phép xem*, hoàn toàn không có tài liệu nào chứa nội dung câu hỏi.\n"
            "  + Việc tìm kiếm không dùng filter có nhiều kết quả tốt chứng minh các kết quả đó thuộc về chính sách đã hết hạn hoặc tài liệu nội bộ mật mà người dùng này *không có quyền truy cập*.\n"
            "- **Trường hợp B: Retrieval bỏ sót kết quả (Retrieval Recall Failure)**:\n"
            "  + Bản chất: Tài liệu đúng tồn tại trong tập người dùng được phép xem, nhưng thuật toán tìm kiếm vector/BM25 kém cỏi nên không tìm ra.\n"
            "2. Lựa chọn cách xử lý và phản hồi phù hợp:\n"
            "- Hành vi hệ thống: Tuyệt đối **KHÔNG ĐƯỢC** nới lỏng hoặc gỡ bỏ bộ lọc quyền để lấy kết quả ngoài phạm vi, vì đây là hành vi vi phạm nghiêm trọng an toàn thông tin (Authorization Bypass / Data Leakage Vulnerability).\n"
            "- Phản hồi chuẩn cho người dùng: Thông báo rõ ràng: 'Không tìm thấy chính sách có hiệu lực nào phù hợp với câu hỏi trong phạm vi quyền hạn của bạn. (Lưu ý: Một số tài liệu liên quan có thể thuộc phiên bản đã hết hiệu lực hoặc khu vực hạn chế)'.\n"
            "- Ghi nhật ký kiểm toán: Ghi log sự kiện truy vấn rỗng do bộ lọc quyền để đội ngũ quản trị nội dung xem xét cập nhật chính sách hiện hành nếu cần."
        ),
        "explanation": (
            "Bảo mật đa tầng trong RAG đòi hỏi việc thực thi quyền hạn (Access Scope Enforcement) phải là một ranh giới cứng (Hard Boundary). "
            "Không bao giờ được nhầm lẫn giữa sự vắng mặt của tài liệu được phép với lỗi truy xuất của thuật toán để rồi tự ý nới lỏng bảo mật."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân biệt rạch ròi 2 trường hợp] (1.5 điểm): Phân biệt rõ kết quả rỗng do ràng buộc cấp quyền (chính sách hết hạn/mật) với lỗi thuật toán retrieval bỏ sót.\n"
            "- [Cấm gỡ bỏ bộ lọc quyền] (1.0 điểm): Khẳng định tuyệt đối không được bypass filter để tránh rò rỉ dữ liệu ngoài thẩm quyền.\n"
            "- [Cách xử lý & Phản hồi minh bạch] (1.5 điểm): Thiết kế phản hồi an toàn cho người dùng thông báo không có chính sách hiệu lực và ghi log kiểm toán."
        ),
        "reference_source": "OWASP Top 10 for LLM: LLM06 Sensitive Information Disclosure & Pinecone Multi-tenancy and Access Control"
    },
    "d08-q030": {
        "sample_answer": (
            "1. Phân tích ưu - nhược điểm đối lập của Dense và Sparse Retrieval:\n"
            "- Dense Retrieval (Vector Bi-Encoder): Rất mạnh về so khớp ngữ nghĩa và bắt được các từ đồng nghĩa/alias (ví dụ: 'máy tính xách tay' khớp với 'laptop'), nhưng rất kém khi khớp các mã định danh chính xác (Part Number, Serial, Error Code như `X-900`) vì các chuỗi ký tự này bị token hóa thành các subword rời rạc và bị phân tán trong không gian tiềm ẩn.\n"
            "- Sparse Retrieval (BM25 / Lexical): Rất mạnh về so khớp chính xác từng ký tự (Exact Keyword Match, Part Number), nhưng hoàn toàn thất bại khi gặp lỗi chính tả (typo) hoặc khi người dùng dùng từ đồng nghĩa/alias không trùng từ ngữ trong văn bản.\n"
            "2. Thiết kế Kiến trúc Hybrid Retrieval kết hợp Định tuyến (Hybrid Search Architecture):\n"
            "- **Thiết kế Pipeline Lai (Hybrid Search Pipeline)**:\n"
            "  + Chạy song song cả Dense Retriever và BM25 Retriever cho mọi truy vấn.\n"
            "  + Kết hợp kết quả bằng thuật toán Hợp nhất thứ hạng tương hỗ (Reciprocal Rank Fusion - RRF) với công thức: `RRF_Score(d) = 1/(60 + r_dense(d)) + 1/(60 + r_bm25(d))`.\n"
            "- **Bộ lọc tiền xử lý lỗi chính tả (Query Pre-processing Spellcheck)**: Tích hợp bộ sửa lỗi chính tả nhẹ (Spellchecker/SymSpell) trước khi đưa vào BM25 để giảm thiểu nhược điểm của lexical search.\n"
            "3. Hệ thống chỉ số kiểm chứng thực nghiệm (Evaluation Metrics):\n"
            "- Đo lường trên bộ kiểm thử 2 nhóm câu hỏi độc lập:\n"
            "  + Nhóm 1 (Alias & Ngữ nghĩa): Đo Recall@5 và MRR (yêu cầu Hybrid đạt kết quả tương đương Dense).\n"
            "  + Nhóm 2 (Part Number & Mã lỗi): Đo Recall@5 và Precision@1 (yêu cầu Hybrid đạt kết quả tương đương BM25).\n"
            "- Mục tiêu nghiệm thu: Hybrid Search đạt Recall@5 toàn cục cao hơn ít nhất 10% so với việc chỉ dùng riêng lẻ Dense hoặc BM25."
        ),
        "explanation": (
            "Dense Retrieval và Sparse Retrieval bổ trợ hoàn hảo cho nhau: Dense giải quyết sự bất đối xứng từ vựng và đồng nghĩa, còn Sparse giải quyết "
            "tính chính xác tuyệt đối của mã định danh và thuật ngữ hiếm. Kết hợp hai phương pháp bằng RRF là tiêu chuẩn vàng của hệ thống RAG hiện đại."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân tích đặc tính Dense vs BM25] (1.5 điểm): Chỉ ra Dense bắt được alias nhưng trượt part number; BM25 bắt part number nhưng trượt alias/typo.\n"
            "- [Thiết kế kiến trúc Hybrid với RRF] (1.5 điểm): Thiết kế pipeline chạy song song kết hợp RRF (hoặc weighted score) kèm tiền xử lý chính tả.\n"
            "- [Hệ thống metric kiểm chứng thực nghiệm] (1.0 điểm): Đưa ra phép đo Recall@5 và MRR phân tách trên 2 nhóm query để chứng minh ưu thế của Hybrid."
        ),
        "reference_source": "Cormack, Clarke & Büttcher (2009): 'Reciprocal Rank Fusion outperforms Condorcet and individual machine learning methods' & Pinecone Hybrid Search"
    },
    "d08-q033": {
        "sample_answer": (
            "1. Quyết định: **TẠM HOÃN CHỌN ALPHA TOÀN CỤC (POSTPONE GLOBAL ALPHA SELECTION)**:\n"
            "Căn cứ: Mặc dù `alpha = 0,5` có điểm trung bình tổng thể cao nhất, nhưng nó lại gây ra hiện tượng sụt giảm nghiêm trọng (Severe Performance Degradation) ở nhóm chính sách tiếng Việt. Việc hy sinh chất lượng của một phân khúc người dùng quan trọng để đổi lấy con số trung bình đẹp là một quyết định kỹ thuật thiên lệch và nguy hiểm.\n"
            "2. Báo cáo mức giảm chất lượng cần công bố minh bạch (Degradation Reporting):\n"
            "- Báo cáo rõ ràng mức sụt giảm cụ thể của từng nhóm truy vấn so với cấu hình tốt nhất của nhóm đó:\n"
            "  + Nhóm truy vấn chính sách tiếng Việt: Báo cáo mức giảm Recall@5 và MRR khi chuyển từ alpha tối ưu của tiếng Việt (ví dụ `alpha = 0,8`) sang `alpha = 0,5` (mức giảm cụ thể, ví dụ giảm 18% Recall).\n"
            "  + Nhóm truy vấn ID chính xác: Báo cáo mức giảm khi chuyển từ `alpha = 0,2` sang `0,5`.\n"
            "3. Đề xuất giải pháp kỹ thuật vượt qua bế tắc:\n"
            "- Chuyển từ Alpha Tĩnh toàn cục (Static Global Alpha) sang **Alpha Động theo phân loại truy vấn (Dynamic / Query-Class-Dependent Alpha)**:\n"
            "  + Nếu bộ phân loại phát hiện query là mã ID / Part Number / Ký tự đặc biệt: Tự động gán `alpha = 0,2` (ưu tiên BM25).\n"
            "  + Nếu query là câu hỏi ngữ nghĩa tiếng Việt: Tự động gán `alpha = 0,8` (ưu tiên Dense).\n"
            "  + Hoặc chuyển đổi hoàn toàn sang phương pháp dung hợp phi tham số không phụ thuộc alpha: **Reciprocal Rank Fusion (RRF)**."
        ),
        "explanation": (
            "Hiện tượng nghịch lý trung bình (Flaw of Averages) trong tinh chỉnh siêu tham số RAG: một giá trị trung bình có thể che giấu sự sụp đổ chất lượng "
            "ở một nhóm ngôn ngữ hoặc nhóm tác vụ đặc thù. Kỹ sư hệ thống phải báo cáo minh bạch mức suy thoái theo từng cohort và chuyển dịch sang "
            "cơ chế thích ứng động (Dynamic Alpha) hoặc RRF."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định tạm hoãn có căn cứ] (1.5 điểm): Tạm hoãn chọn alpha=0.5 vì làm giảm mạnh chất lượng ở nhóm policy tiếng Việt, không để điểm trung bình che giấu lỗi.\n"
            "- [Báo cáo mức suy thoái minh bạch] (1.0 điểm): Yêu cầu báo cáo số liệu giảm chất lượng cụ thể của nhóm tiếng Việt và nhóm ID chính xác.\n"
            "- [Đề xuất Dynamic Alpha hoặc RRF] (1.5 điểm): Đưa ra giải pháp kỹ thuật: định tuyến alpha động theo loại câu hỏi hoặc thay thế bằng RRF phi tham số."
        ),
        "reference_source": "Pinecone Documentation: 'Tuning Alpha for Hybrid Search' & Kohavi: 'Controlled Experiments and Subgroup Analysis'"
    },
    "d08-q034": {
        "sample_answer": (
            "1. Thiết kế phép thử quét nhiều giá trị Alpha (Multi-Alpha Parameter Sweep):\n"
            "- Cố định tập ngữ liệu và bộ testset chuẩn hóa đã được đánh nhãn (Frozen Evaluation Benchmark).\n"
            "- Đảm bảo điểm số từ Dense và BM25 đã được chuẩn hóa đúng (Min-Max Scaling hoặc Standard Z-Score) về cùng khoảng giá trị `[0, 1]`.\n"
            "- Thiết lập lưới quét giá trị `alpha` từ 0.0 đến 1.0 với bước nhảy 0.1: `alpha in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]` (trong đó 0.0 là thuần BM25, 1.0 là thuần Dense).\n"
            "- Đo lường các chỉ số cốt lõi tại mỗi điểm: Recall@5, Precision@5, MRR và NDCG@5 trên cả tập tổng thể và từng nhóm câu hỏi (keyword vs semantic).\n"
            "2. Nội dung cần ghi trong Bản ghi Quyết định Kỹ thuật (Architecture Decision Record - ADR):\n"
            "Tạo tài liệu `ADR-042: Lựa chọn Tham số Alpha cho Hybrid Search Corpus Mới` bao gồm:\n"
            "- **Bối cảnh & Dữ liệu thực nghiệm**: Mô tả đặc tính của corpus mới và biểu đồ hiệu năng Recall/MRR theo từng giá trị alpha được quét thực tế.\n"
            "- **Quyết định (Decision)**: Giá trị alpha được lựa chọn (kèm lý do tại sao không áp dụng con số 0.7 từ slide lý thuyết cũ).\n"
            "- **Hậu quả & Đánh đổi (Trade-offs)**: Phân tích nhóm truy vấn nào hưởng lợi nhiều nhất và nhóm nào có thể bị ảnh hưởng nhẹ.\n"
            "- **Điều kiện tái đánh giá**: Quy định khi nào cần tinh chỉnh lại alpha (ví dụ: khi kích thước corpus tăng gấp đôi hoặc khi thay đổi mô hình embedding mới)."
        ),
        "explanation": (
            "Không bao giờ được sao chép máy móc các siêu tham số từ slide lý thuyết sang một tập ngữ liệu thực tế mới mà không qua thực nghiệm chuẩn hóa. "
            "Mỗi corpus có phân phối từ vựng và đặc trưng ngữ nghĩa riêng biệt. Quy trình Architecture Decision Record (ADR) bảo đảm mọi quyết định "
            "cấu hình hệ thống đều dựa trên bằng chứng dữ liệu có thể kiểm chứng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế phép quét Alpha đa điểm] (1.5 điểm): Thiết lập lưới quét alpha từ 0.0 đến 1.0 bước 0.1 trên tập benchmark đóng băng với điểm đã chuẩn hóa.\n"
            "- [Cấu trúc bản ghi quyết định ADR] (1.5 điểm): Soạn thảo cấu trúc ADR đầy đủ: Bối cảnh, Dữ liệu thực nghiệm, Quyết định, Đánh đổi và Điều kiện xem lại.\n"
            "- [Phê phán việc lấy số từ slide] (1.0 điểm): Nhấn mạnh nguyên tắc cấm áp đặt giá trị alpha lý thuyết lên corpus mới mà không đo lường."
        ),
        "reference_source": "Michael Nygard: 'Documenting Architecture Decisions' (ADR Template) & Qdrant Hybrid Search Tuning Guide"
    },
    "d08-q036": {
        "sample_answer": (
            "1. Vai trò của IDF (Inverse Document Frequency - Nghịch đảo tần suất tài liệu):\n"
            "- Ý nghĩa: IDF đo lường mức độ quan trọng và độ hiếm của một từ khóa trong toàn bộ kho tài liệu (Corpus). Một từ xuất hiện ở hầu hết mọi tài liệu (như từ nối, từ dừng) sẽ có IDF xấp xỉ 0, không có giá trị phân biệt.\n"
            "- Ứng dụng trong bối cảnh: Vì từ trong câu hỏi là 'rất hiếm trong corpus', giá trị IDF của nó cực kỳ cao. Khi xuất hiện trong tài liệu, nó đóng vai trò là một tín hiệu định danh mạnh mẽ (Strong Discriminative Signal), giúp nâng điểm số BM25 của tài liệu lên rất cao so với các tài liệu không chứa từ này.\n"
            "2. Vai trò của việc Chuẩn hóa độ dài tài liệu (Document Length Normalization - Tham số b trong BM25):\n"
            "- Ý nghĩa: Thuật toán BM25 áp dụng cơ chế phạt các tài liệu có độ dài lớn thông qua tỷ lệ độ dài tài liệu so với độ dài trung bình toàn kho (`len(doc) / avg_len`). Một tài liệu dài chứa từ khóa nhiều khả năng là do ngẫu nhiên thống kê, trong khi tài liệu ngắn chứa từ khóa chứng tỏ mật độ thông tin và độ tập trung chủ đề rất cao.\n"
            "- So sánh giữa Tài liệu C và D: Cả C và D đều có cùng số lần xuất hiện của từ khóa hiếm, nhưng Tài liệu C ngắn hơn nhiều so với Tài liệu D. Cơ chế chuẩn hóa độ dài của BM25 sẽ ưu tiên mạnh cho Tài liệu C, giúp C đạt điểm BM25 cao hơn đáng kể so với D vì mật độ từ khóa (Term Density) của C vượt trội và không bị pha loãng bởi các nội dung râu ria."
        ),
        "explanation": (
            "BM25 là thuật toán xếp hạng xác suất dựa trên hai trụ cột: Tần suất từ có bão hòa (Saturated TF kết hợp với Length Normalization qua tham số b) "
            "và Mức độ phân biệt thông tin toàn cục (IDF). Việc hiểu rõ vai trò của việc chuẩn hóa độ dài giúp giải thích tại sao các đoạn trích ngắn, "
            "cô đọng lại được xếp hạng cao hơn các văn bản dài dòng chứa cùng số lần xuất hiện từ khóa."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Giải thích vai trò của IDF] (1.5 điểm): Nêu rõ từ hiếm có IDF cao, đóng vai trò tín hiệu phân biệt mạnh mẽ giúp tăng vọt điểm số BM25.\n"
            "- [Giải thích chuẩn hóa độ dài tài liệu] (1.5 điểm): Phân tích cơ chế phạt tài liệu dài và ưu tiên tài liệu ngắn có mật độ thông tin tập trung.\n"
            "- [Kết luận so sánh giữa C và D] (1.0 điểm): Khẳng định Tài liệu C đạt điểm cao hơn D do độ dài ngắn hơn mà không cần tính toán số học cụ thể."
        ),
        "reference_source": "Robertson & Zaragoza (2009): 'The Probabilistic Relevance Framework: BM25 and Beyond' (Foundations and Trends in Information Retrieval)"
    },
    "d08-q038": {
        "sample_answer": (
            "1. Chỉ ra hai lỗi nghiêm trọng trong quá trình thực thi (Defect Identification):\n"
            "- **Lỗi 1: Thất thoát Khóa định danh bản ghi (Missing Record ID in Search Output)**:\n"
            "  + Chi tiết: Bước tìm kiếm BM25 trả về văn bản nhưng làm rơi mất trường `record_id` (hoặc trả về `id: null`). Hậu quả là bước gộp Hybrid Search không thể đối soát và so khớp bản ghi này với bản ghi trả về từ Dense Search. Thuật toán gộp buộc phải coi đây là một bản ghi hoàn toàn mới, gây ra hiện tượng nhân bản kết quả (Duplicate Result Pollution) và làm sai lệch thuật toán RRF/Score Fusion.\n"
            "- **Lỗi 2: Vi phạm Hợp đồng Giới hạn kích thước đầu ra (Top-K Limit Violation)**:\n"
            "  + Chi tiết: Lệnh gọi API yêu cầu rõ ràng `top_k = 2`, nhưng hệ thống lại trả về tới 5 bản ghi. Điều này vi phạm nghiêm trọng hợp đồng API tìm kiếm, chứng minh thuật toán ranking đã quên bước cắt lát kết quả (`return results[:k]`).\n"
            "2. Các điều kiện kiểm tra (Assertion Invariants) cần bổ sung vào hệ thống:\n"
            "- Invariant 1 (Strict Schema & ID Presence): `assert all(r.get('record_id') is not None and len(r['record_id']) > 0 for r in search_results)` — Mọi kết quả trả về từ BM25 bắt buộc phải mang ID bản ghi hợp lệ.\n"
            "- Invariant 2 (Strict Top-K Contract): `assert len(search_results) <= top_k` — Số lượng kết quả trả về không bao giờ được vượt quá giá trị `top_k` yêu cầu."
        ),
        "explanation": (
            "Trong kiến trúc tìm kiếm phân tán, mọi Retriever (dù là Dense hay BM25) đều phải tuân thủ nghiêm ngặt Giao ước Dữ liệu (Component Contract): "
            "bảo toàn khóa định danh duy nhất để phục vụ deduplication và tôn trọng ngưỡng giới hạn Top-K. Vi phạm giao ước này sẽ phá hủy tính toàn vẹn của tầng Fusion phía sau."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chỉ rõ lỗi mất Record ID] (1.5 điểm): Nhận diện lỗi BM25 làm mất ID khiến bước gộp hybrid coi là bản ghi mới và gây duplicate.\n"
            "- [Chỉ rõ lỗi vi phạm Top-K] (1.0 điểm): Nhận diện lỗi yêu cầu top_k=2 nhưng trả về 5 bản ghi do thiếu bước slice/truncate kết quả.\n"
            "- [Bổ sung 2 Assertion Invariants cụ thể] (1.5 điểm): Viết rõ 2 điều kiện kiểm tra: bắt buộc có record_id không rỗng và độ dài danh sách <= top_k."
        ),
        "reference_source": "Elasticsearch / Lucene Documentation: 'TopDocs, ScoredDoc and API Contract Guidelines'"
    },
    "d08-q040": {
        "sample_answer": (
            "1. Mô tả Bản ghi Hợp nhất trước bước Fusion (Pre-fusion Unified Records for A, B, C):\n"
            "Dữ liệu trả về từ hai luồng xử lý song song: Dense trả về `{A: score_dense_A, C: score_dense_C}`; Sparse trả về `{B: score_sparse_B, A: score_sparse_A}`.\n"
            "Trước khi tính điểm gộp (RRF hoặc Weighted Score), hệ thống phải hợp nhất thành cấu trúc dữ liệu bản ghi thống nhất lưu vết nguồn gốc đa kênh:\n"
            "- **Bản ghi A** (Xuất hiện ở cả hai luồng):\n"
            "  + `record_id`: `\"A\"`\n"
            "  + `dense_score`: `score_dense_A`, `dense_rank`: 1 (hoặc thứ hạng tương ứng)\n"
            "  + `sparse_score`: `score_sparse_A`, `sparse_rank`: 2\n"
            "  + `retrieval_sources`: `[\"dense\", \"sparse\"]` (được bảo chứng bởi cả hai kênh)\n"
            "- **Bản ghi B** (Chỉ xuất hiện ở luồng Sparse):\n"
            "  + `record_id`: `\"B\"`\n"
            "  + `dense_score`: `None` (hoặc `0.0`), `dense_rank`: `Infinity`\n"
            "  + `sparse_score`: `score_sparse_B`, `sparse_rank`: 1\n"
            "  + `retrieval_sources`: `[\"sparse\"]`\n"
            "- **Bản ghi C** (Chỉ xuất hiện ở luồng Dense):\n"
            "  + `record_id`: `\"C\"`\n"
            "  + `dense_score`: `score_dense_C`, `dense_rank`: 2\n"
            "  + `sparse_score`: `None` (hoặc `0.0`), `sparse_rank`: `Infinity`\n"
            "  + `retrieval_sources`: `[\"dense\"]`\n"
            "2. Ý nghĩa của việc lưu vết nguồn (Provenance Tracking):\n"
            "Lưu giữ dấu vết nguồn giúp bộ gộp xếp hạng (Fusion Engine) phân biệt rõ ràng giữa các tài liệu có độ đồng thuận cao giữa hai phương pháp (như A) "
            "với các tài liệu chỉ đơn độc xuất hiện ở một phía, đồng thời hỗ trợ kiểm toán và giải thích kết quả cho người dùng."
        ),
        "explanation": (
            "Trong Hybrid Retrieval chạy song song, bước chuẩn bị dữ liệu trước khi dung hợp (Pre-fusion Aggregation) phải thực hiện Full Outer Join "
            "dựa trên `record_id`. Việc ghi nhận chi tiết thứ hạng và điểm số của từng luồng kèm mảng `retrieval_sources` là điều kiện tiên quyết để thuật toán RRF "
            "hoặc Weighted Fusion hoạt động chính xác."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đặc tả bản ghi A có 2 nguồn] (1.5 điểm): Mô tả đúng bản ghi A mang cả dense_score, sparse_score và danh sách nguồn ['dense', 'sparse'].\n"
            "- [Đặc tả bản ghi B và C nguồn đơn lẻ] (1.5 điểm): Mô tả đúng B chỉ có nguồn sparse (dense null) và C chỉ có nguồn dense (sparse null).\n"
            "- [Dấu vết nguồn và thứ hạng minh bạch] (1.0 điểm): Nhấn mạnh tầm quan trọng của provenance tracking để phục vụ tính điểm dung hợp và kiểm toán."
        ),
        "reference_source": "Pinecone Documentation: 'Reciprocal Rank Fusion Implementation' & Cormack et al. (2009)"
    },
    "d08-q042": {
        "sample_answer": (
            "1. Hành vi xác định cho trường hợp mọi điểm bằng nhau (Zero-Variance / Degenerate Case Handling):\n"
            "Khi toàn bộ điểm số của Dense Search đều bằng 0,5 (`min_score == max_score == 0.5`), công thức chuẩn hóa Min-Max: `(s - min) / (max - min)` sẽ có mẫu số bằng 0 (Division by Zero).\n"
            "- **Hành vi chuẩn hóa đúng (Deterministic Fallback)**: Hệ thống phải xử lý ngoại lệ này một cách tất định: gán toàn bộ điểm số chuẩn hóa của kênh Dense về giá trị trung tính mặc định (Neutral Default Value), cụ thể là `0.0` (hoặc `1.0` tùy quy ước hệ thống, trong đó gán `0.0` là chuẩn nhất để phản ánh rằng kênh này không cung cấp bất kỳ tín hiệu phân biệt nào giữa các tài liệu).\n"
            "- Kết quả: Tín hiệu Dense không tạo ra sự chênh lệch thứ hạng; thứ tự sắp xếp và điểm số dung hợp hoàn toàn được quyết định bởi các điểm số khác nhau của kênh Sparse (BM25).\n"
            "2. Điều TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM (Strict Prohibitions):\n"
            "- Tuyệt đối không để xảy ra lỗi ngoại lệ chưa bắt (Unhandled ZeroDivisionError) làm sập hệ thống hoặc trả mã lỗi HTTP 500 cho người dùng.\n"
            "- Tuyệt đối không tự ý cộng thêm một số epsilon ngẫu nhiên vào điểm số nếu điều đó làm xáo trộn thứ tự tự nhiên của các bản ghi.\n"
            "- Tuyệt đối không loại bỏ toàn bộ kết quả tìm kiếm chỉ vì một trong hai kênh gặp hiện tượng điểm số phẳng."
        ),
        "explanation": (
            "Hiện tượng phương sai bằng không (Zero Variance / Score Degeneracy) xảy ra khi tất cả các tài liệu đều có khoảng cách vector giống hệt nhau tới query. "
            "Một hàm chuẩn hóa điểm số bền bỉ (Robust Normalizer) bắt buộc phải có điều kiện rẽ nhánh: `if max_score == min_score: return [0.0] * len(scores)`, "
            "bảo đảm hệ thống hoạt động ổn định và tin cậy."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Xác định nguyên nhân chia cho 0] (1.0 điểm): Chỉ ra mẫu số max - min = 0 do mọi điểm bằng 0.5.\n"
            "- [Hành vi chuẩn hóa tất định] (1.5 điểm): Đưa ra xử lý chuẩn: gán điểm chuẩn hóa về 0.0 để vô hiệu hóa tín hiệu không phân biệt và để sparse quyết định thứ hạng.\n"
            "- [Các điều tuyệt đối không được làm] (1.5 điểm): Cấm để sập hệ thống (500 error), cấm thêm nhiễu ngẫu nhiên làm đảo lộn thứ tự, cấm bỏ kết quả."
        ),
        "reference_source": "Scikit-Learn Documentation: 'MinMaxScaler - Handling Zero Variance Features' & Qdrant Score Normalization Guides"
    },
    "d08-q044": {
        "sample_answer": (
            "1. Chỉ ra lỗi trong mã nguồn hiện tại (Defect Identification):\n"
            "- Thuật toán RRF (Reciprocal Rank Fusion) yêu cầu: Điểm số dung hợp của một tài liệu là **TỔNG CÁC ĐIỂM ĐÓNG GÓP TỶ LỆ NGHỊCH VỚI THỨ HẠNG** từ tất cả các danh sách tìm kiếm mà tài liệu đó xuất hiện: `RRF_Score(d) = sum_{m in Models} [ 1 / (k + rank_m(d)) ]`.\n"
            "- Đoạn code hiện tại bị lỗi **Ghi đè điểm số (Overwrite Defect)**: Khi tài liệu xuất hiện trong danh sách thứ hai, mã nguồn thay vì cộng dồn (`score += ...`) lại dùng phép gán đè (`score = ...`).\n"
            "- Hậu quả cụ thể:\n"
            "  + Tài liệu A (hạng 1 ở danh sách 1, hạng 3 ở danh sách 2): Bị ghi đè điểm số của hạng 3, mất hoàn toàn phần thưởng điểm cực lớn của hạng 1!\n"
            "  + Tài liệu B (hạng 2 ở cả hai danh sách): Bị mất một nửa điểm số vì hai lần đóng góp không được tích lũy. Cả hai tài liệu đều bị đánh giá sai lệch thứ tự nghiêm trọng.\n"
            "2. Các trường đầu ra cần lưu giữ để phục vụ kiểm tra và kiểm toán (Output Fields for Audit):\n"
            "Mỗi bản ghi đầu ra sau bước RRF phải chứa cấu trúc minh bạch sau:\n"
            "```json\n"
            "{\n"
            "  \"doc_id\": \"A\",\n"
            "  \"final_rrf_score\": 0.0325,\n"
            "  \"contributions\": [\n"
            "    {\"source\": \"dense\", \"rank\": 1, \"score_added\": 0.01639},\n"
            "    {\"source\": \"sparse\", \"rank\": 3, \"score_added\": 0.01587}\n"
            "  ],\n"
            "  \"appearance_count\": 2\n"
            "}\n"
            "```"
        ),
        "explanation": (
            "Bản chất của thuật toán RRF là cơ chế bỏ phiếu tích lũy (Cumulative Voting): một tài liệu xuất hiện ở thứ hạng cao trên nhiều danh sách độc lập "
            "phải được cộng gộp điểm để vươn lên vị trí dẫn đầu. Lỗi ghi đè điểm số làm biến RRF thành một phép lấy thứ tự của danh sách chạy sau, "
            "phá hủy hoàn toàn mục đích của Hybrid Search."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chỉ rõ lỗi ghi đè điểm số RRF] (1.5 điểm): Phân tích công thức RRF yêu cầu cộng dồn 1/(k+rank) nhưng code lại ghi đè, làm mất điểm hạng 1 của A.\n"
            "- [Hậu quả đối với tài liệu A và B] (1.0 điểm): Chỉ ra việc A và B bị hạ điểm sai lệch và mất tính công bằng trong xếp hạng.\n"
            "- [Đặc tả cấu trúc trường đầu ra kiểm toán] (1.5 điểm): Thiết kế cấu trúc JSON lưu giữ final_rrf_score, mảng contributions từng nguồn và appearance_count."
        ),
        "reference_source": "Cormack, Clarke & Büttcher (2009): 'Reciprocal Rank Fusion outperforms Condorcet and individual machine learning methods'"
    },
    "d08-q048": {
        "sample_answer": (
            "1. Chẩn đoán lỗi truy xuất cấu trúc (Defect Diagnosis):\n"
            "- Nguyên nhân: Quá trình duyệt cây cấu trúc (Tree Traversal / Structural Navigation) phụ thuộc vào tính toàn diện của bản tóm tắt mục cha (Section Summary). Bản tóm tắt mục cha đã bỏ qua (khuyết thiếu) thông tin về ngoại lệ nằm trong phụ lục. Khi thuật toán tìm kiếm duyệt từ gốc cây xuống, nó so khớp query với bản tóm tắt mục cha, thấy không liên quan nên quyết định **Cắt tỉa nhánh sớm (Early Tree Pruning)**, dẫn đến việc không bao giờ duyệt tới nút con phụ lục.\n"
            "2. Sửa chữa chỉ mục cấu trúc mà không dùng tìm kiếm quét phẳng toàn bộ tệp (Structural Index Repair):\n"
            "- Giải pháp 1 (Làm giàu bản tóm tắt mục cha - Summary Enrichment with Exceptions): Cập nhật quy trình sinh bản tóm tắt mục cha: bắt buộc trích xuất và đưa các từ khóa 'Ngoại lệ', 'Phụ lục', và các điều khoản miễn trừ đặc biệt vào phần tóm tắt của mục cha.\n"
            "- Giải pháp 2 (Bổ sung Liên kết ngang / Cross-linking & Indexing of Leaves): Thiết lập các liên kết neo ngang (Anchor Cross-references) từ mục chính sách chính trỏ thẳng tới phụ lục, đồng thời duy trì một chỉ mục phụ (Leaf-level Inverted Index) cho toàn bộ các phần phụ lục ngoại lệ để hỗ trợ duyệt thẳng khi query chứa từ khóa ngoại lệ đặc thù."
        ),
        "explanation": (
            "Trong tìm kiếm cấu trúc phân cấp (Hierarchical Tree Retrieval / PageIndex), chất lượng điều hướng phụ thuộc hoàn toàn vào độ đại diện "
            "của các nút cha (Parent Node Summaries). Nếu nút cha làm rơi rụng thông tin của nút lá, cây sẽ bị cụt nhánh tìm kiếm. Việc làm giàu tóm tắt cha "
            "và duy trì liên kết trực tiếp là giải pháp căn cơ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán đúng lỗi cắt tỉa nhánh sớm] (1.5 điểm): Chỉ ra bản tóm tắt mục cha thiếu ngoại lệ khiến thuật toán duyệt cây dừng sớm và bỏ lỡ phụ lục.\n"
            "- [Sửa bản tóm tắt mục cha] (1.5 điểm): Nêu giải pháp làm giàu tóm tắt cha bắt buộc chứa thông tin ngoại lệ và tham chiếu phụ lục.\n"
            "- [Thiết lập liên kết ngang có cấu trúc] (1.0 điểm): Bổ sung liên kết neo trực tiếp tới phụ lục mà không cần quét toàn bộ hệ thống tệp."
        ),
        "reference_source": "LlamaIndex Documentation: 'Document Summary Index & Tree-based Retrieval' (https://docs.llamaindex.ai)"
    },
    "d08-q050": {
        "sample_answer": (
            "1. Thiết kế Quy tắc Định tuyến Truy xuất (Retrieval Routing Rules):\n"
            "Không bao giờ gọi đồng thời mọi retriever cho mọi yêu cầu. Thiết lập bộ định tuyến thông minh (Smart Retriever Router) dựa trên thuộc tính tài liệu (Metadata Domain / Document Type) và đặc trưng truy vấn:\n"
            "- **Nhánh 1: Tài liệu có cấu trúc phân cấp (Hierarchical Structured Docs - Cẩm nang, Sổ tay chính sách)**:\n"
            "  + Kích hoạt: `Structural / PageIndex Retriever` (duyệt cây mục lục và các phần lồng nhau).\n"
            "  + Điều kiện dự phòng (Fallback Trigger): Nếu duyệt cấu trúc trả về điểm tin cậy thấp hoặc danh sách rỗng, kích hoạt fallback sang `Hybrid Dense+BM25 Retriever`.\n"
            "- **Nhánh 2: Nhật ký hội thoại & Dữ liệu phẳng (Flat / Conversational Logs - Chat history, Ticket support)**:\n"
            "  + Kích hoạt trực tiếp: `Hybrid Dense+BM25 Retriever` (hoặc Time-window Filtered Search).\n"
            "  + Lý do: Nhật ký hội thoại không có cấu trúc cây, việc gọi Structural Retriever là hoàn toàn vô nghĩa và lãng phí độ trễ.\n"
            "2. Điều kiện kích hoạt có thể quan sát được (Observable Routing Invariants):\n"
            "- Kiểm tra metadata phân loại nguồn: `if doc_collection.type == 'hierarchical_manual': route_to(structural_pipeline)`.\n"
            "- Tối ưu hóa tài nguyên: Tiết kiệm 100% chi phí tính toán duyệt cây cho toàn bộ các truy vấn trên nhật ký hội thoại."
        ),
        "explanation": (
            "Một kiến trúc RAG doanh nghiệp trưởng thành phải có khả năng định tuyến đa đường (Multi-route Dispatching). Việc áp dụng một chiến lược truy xuất "
            "cấu trúc phân cấp cho một loại dữ liệu phi cấu trúc phẳng như chat log là sự lãng phí tài nguyên và làm tăng độ trễ không cần thiết."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân loại định tuyến theo loại tài liệu] (1.5 điểm): Phân định rõ tài liệu hướng dẫn dùng Structural Retriever, nhật ký hội thoại dùng Hybrid Dense+BM25.\n"
            "- [Thiết kế Fallback an toàn] (1.5 điểm): Thiết lập cơ chế fallback sang Hybrid Search khi Structural search thất bại.\n"
            "- [Tiết kiệm tài nguyên và độ trễ] (1.0 điểm): Nhấn mạnh quy tắc không gọi mọi retriever một cách mù quáng để bảo vệ SLO hệ thống."
        ),
        "reference_source": "LangChain Documentation: 'Router Retrievers and Multi-Retrieval QA' & LlamaIndex 'RouterQueryEngine'"
    },
    "d08-q052": {
        "sample_answer": (
            "1. Đánh giá đề xuất chạy Cross-Encoder trên 2 triệu chunk:\n"
            "Đề xuất này là **HOÀN TOÀN BẤT KHẢ THI VÀ PHÁ VỠ HỆ THỐNG (Architecturally Unfeasible)**:\n"
            "- Phân tích độ phức tạp tính toán: Mô hình Cross-Encoder ghép cặp trực tiếp toàn bộ `(Query, Document)` và chạy qua toàn bộ các lớp Transformer Self-Attention. Nếu chạy trên 2 triệu chunk, chi phí tính toán là `2.000.000` lượt forward passes. Ngay cả trên cụm GPU cực mạnh, thời gian xử lý cho một truy vấn đơn lẻ sẽ mất từ vài phút đến hàng chục phút, vi phạm thảm khốc SLO độ trễ (thường quy định < 200 ms).\n"
            "2. Đầu ra cần có của Giai đoạn đầu (First-Stage Retrieval Output):\n"
            "- Giai đoạn đầu sử dụng Bi-Encoder (Dense) kết hợp BM25 (Sparse) với chỉ mục HNSW/Inverted Index để lọc nhanh từ 2 triệu chunk xuống tập ứng viên nhỏ gọn (Candidate Set): chính xác **Top-50 đến Top-100 chunks** (Candidate Depth).\n"
            "3. Vai trò thực sự của Cross-Encoder (Second-Stage Reranker):\n"
            "- Cross-Encoder chỉ đóng vai trò là **Bộ tái xếp hạng tinh chỉnh (Fine-grained Reranker)** ở giai đoạn hai, chỉ chấm điểm trên 50-100 ứng viên đã được chọn lọc từ giai đoạn một để đưa ra Top-5 chunk chất lượng nhất cho LLM.\n"
            "4. Các chỉ số đo lường Trade-off:\n"
            "- Độ trễ: Đo thời gian chạy p95 của Bi-Encoder vs Cross-Encoder trên Top-K ứng viên.\n"
            "- Hiệu năng: Đo NDCG@5 và MRR để định lượng mức tăng độ chính xác so với chi phí trễ tính bằng mili-giây."
        ),
        "explanation": (
            "Nguyên tắc cốt lõi của Kiến trúc Truy xuất Hai Tầng (Two-Stage Retrieval Funnel): Giai đoạn 1 (Bi-Encoder) tối ưu hóa cho Tốc độ và Độ bao phủ (High Recall, "
            "Low Latency) trên hàng triệu tài liệu; Giai đoạn 2 (Cross-Encoder) tối ưu hóa cho Độ chính xác cao (High Precision, Deep Cross-Attention) "
            "trên vài chục ứng viên."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đánh giá bất khả thi của đề xuất] (1.5 điểm): Bác bỏ đề xuất chạy Cross-Encoder trên 2M chunk vì chi phí tính toán khổng lồ và vi phạm SLO độ trễ.\n"
            "- [Xác định đầu ra giai đoạn 1] (1.0 điểm): Nêu rõ giai đoạn 1 lọc 2 triệu chunk xuống Top 50-100 candidates bằng Bi-encoder/BM25.\n"
            "- [Vai trò thực sự của Cross-Encoder & Trade-off metrics] (1.5 điểm): Xác định đúng vai trò reranker tinh chỉnh ở giai đoạn 2 và nêu các metric đo lường: Latency p95, NDCG@5, MRR."
        ),
        "reference_source": "Nogueira & Cho (2019): 'Passage Re-ranking with BERT' & Cohere Rerank Documentation"
    },
    "d08-q054": {
        "sample_answer": (
            "1. Chẩn đoán nguyên nhân lỗi (Root Cause Diagnosis):\n"
            "- Thuật toán MMR (Maximal Marginal Relevance) cân bằng giữa hai yếu tố: Độ liên quan với truy vấn (`Sim(Query, Doc)`) và Độ đa dạng / Độ mới so với các tài liệu đã chọn (`- Sim(Doc, Selected_Docs)`):\n"
            "  `MMR = argmax [ lambda * Sim(Query, d) - (1 - lambda) * max_{d_j in S} Sim(d, d_j) ]`.\n"
            "- Khi người vận hành tăng trọng số Diversity quá mức (tức là giảm `lambda` quá thấp, ví dụ `lambda = 0.1`), phần phạt trùng lặp lấn át hoàn toàn điểm liên quan. Hệ thống ưu tiên chọn một chunk chỉ vì nó 'càng khác các chunk đã chọn càng tốt', bất chấp việc chunk đó hoàn toàn lạc đề so với câu hỏi của người dùng.\n"
            "2. Điều chỉnh quy tắc lựa chọn (Selection Rule Adjustment):\n"
            "- Khôi phục trọng số cân bằng: Điều chỉnh tham số `lambda` về vùng an toàn tối ưu thực nghiệm, thường là `lambda in [0.5, 0.7]` (ưu tiên độ liên quan chiếm 50% - 70% quyết định).\n"
            "- Thiết lập Ngưỡng liên quan tối thiểu trước khi đa dạng hóa (Relevance Floor / Gating Threshold): Chỉ đưa các tài liệu có `Sim(Query, d) >= min_relevance_threshold` (ví dụ >= 0.70) vào tập ứng viên chạy MMR. Các tài liệu dưới ngưỡng này bị loại bỏ ngay từ đầu, không bao giờ được chọn dù có khác biệt đến đâu.\n"
            "3. Bước hậu kiểm bảo đảm không chọn chunk lạc đề (Post-selection Verification):\n"
            "- Chạy bộ kiểm tra tự động: `assert all(Sim(Query, doc) >= min_relevance_threshold for doc in selected_chunks)` trước khi đóng gói context chuyển sang LLM."
        ),
        "explanation": (
            "Đa dạng hóa thông tin (Diversity) chỉ có ý nghĩa khi nằm trong ranh giới của sự liên quan (Relevance). Nếu không có ngưỡng sàn về độ liên quan "
            "(Relevance Floor), việc tối đa hóa độ đa dạng sẽ nhanh chóng biến thành việc thu thập các đoạn văn bản rác và lạc đề vào ngữ cảnh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán chính xác lỗi của MMR] (1.5 điểm): Giải thích công thức MMR và chỉ ra việc giảm lambda quá thấp khiến phần phạt trùng lặp lấn át độ liên quan, chọn chunk lạc đề.\n"
            "- [Điều chỉnh tham số & Ngưỡng sàn] (1.5 điểm): Đưa lambda về khoảng 0.5-0.7 và thiết lập Relevance Floor Threshold sàng lọc ứng viên.\n"
            "- [Thiết kế bước hậu kiểm] (1.0 điểm): Định nghĩa bước assertion kiểm tra mọi chunk được chọn đều thỏa mãn ngưỡng liên quan tối thiểu."
        ),
        "reference_source": "Carbonell & Goldstein (1998): 'The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries' (SIGIR '98)"
    },
    "d08-q056": {
        "sample_answer": (
            "1. Xác định giới hạn kỹ thuật (Retriever Funnel Upper Bound):\n"
            "- Giới hạn căn bản: **Mô hình Cross-Encoder ở giai đoạn hai KHÔNG THỂ xếp hạng một tài liệu mà nó KHÔNG NHẬN ĐƯỢC từ giai đoạn một!** (Garbage In, Nothing Out Principle).\n"
            "- Recall@50 của giai đoạn đầu là trần tối đa (Upper Bound) cho toàn bộ pipeline. Nếu bằng chứng cần thiết không lọt vào Top-50 của Bi-Encoder/BM25, thì dù Cross-Encoder có thông minh và chính xác đến đâu, nó cũng hoàn toàn bất lực trong việc phục hồi bằng chứng đó. Tập trung tối ưu Cross-Encoder lúc này là đi sai tầng giải pháp.\n"
            "2. Đề xuất thí nghiệm ở đúng tầng kiến trúc (First-Stage Retrieval Experiments):\n"
            "- Thí nghiệm 1: Mở rộng độ sâu ứng viên (Candidate Pool Expansion) từ Top-50 lên Top-100 hoặc Top-200 để kiểm tra xem bằng chứng có nằm ở các thứ hạng tiếp theo hay không.\n"
            "- Thí nghiệm 2: Cải tiến tầng tìm kiếm giai đoạn đầu: Chuyển từ tìm kiếm đơn thuần sang Hybrid Search (kết hợp Dense + BM25 với RRF) hoặc áp dụng Query Expansion / HyDE để cải thiện khả năng thu hồi bằng chứng.\n"
            "- Thí nghiệm 3: Kiểm tra lại kích thước chunk và overlap ở tầng Ingestion.\n"
            "3. Thành phần cần giữ cố định khi kiểm tra (Controlled Baseline):\n"
            "- Giữ cố định 100% mô hình và trọng số của Cross-Encoder Reranker.\n"
            "- Giữ cố định tập dữ liệu kiểm thử (Evaluation Dataset) và câu hỏi truy vấn chuẩn để đo lường chính xác mức tăng Recall@Candidate của giai đoạn một."
        ),
        "explanation": (
            "Trong phễu truy xuất hai tầng (Retrieve-and-Rerank Funnel), giai đoạn 1 phụ trách Recall (độ bao phủ), giai đoạn 2 phụ trách Precision (độ chuẩn xác). "
            "Khi gặp lỗi thiếu bằng chứng (Recall Defect), mọi nỗ lực phải dồn vào việc cải tiến giai đoạn 1, vì giai đoạn 2 chỉ làm nhiệm vụ sắp xếp lại "
            "những gì đã được tìm thấy."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chỉ rõ giới hạn của Cross-Encoder] (1.5 điểm): Khẳng định Cross-Encoder không thể phục hồi tài liệu vắng mặt trong Top-50 của giai đoạn 1.\n"
            "- [Đề xuất thí nghiệm ở tầng First-stage] (1.5 điểm): Đưa ra các giải pháp đúng tầng: tăng candidate depth (Top-100/200), Hybrid search, Query expansion.\n"
            "- [Thành phần giữ cố định] (1.0 điểm): Nêu rõ việc giữ cố định Cross-Encoder và tập benchmark để đo lường đối chứng."
        ),
        "reference_source": "Cohere Rerank Documentation: 'Understanding Retrieval Funnels & Candidate Depths' & BEIR Benchmark Guidelines"
    },
    "d08-q058": {
        "sample_answer": (
            "1. Thiết kế thứ tự xử lý hai tầng (Two-Step Pipeline Order):\n"
            "Cần tách bạch rõ ràng giữa hai bài toán: Xếp hạng độ liên quan (Relevance Ranking) và Khử trùng lặp nội dung (Deduplication / Diversity):\n"
            "- **Bước 1: Chạy Cross-Encoder Reranker để lọc bỏ tài liệu không liên quan**:\n"
            "  + Hành động: Đưa toàn bộ tập candidate qua Cross-Encoder để tính điểm tương đồng ngữ nghĩa chính xác giữa Query và từng Chunk. Lọc bỏ các chunk có điểm số thấp dưới ngưỡng sàn (`score < relevance_threshold`).\n"
            "  + Lý do thực hiện trước: Cần loại bỏ các tài liệu rác và không liên quan trước để không làm lãng phí tài nguyên và không làm sai lệch bước đa dạng hóa phía sau.\n"
            "- **Bước 2: Chạy Thuật toán Đa dạng hóa / Khử trùng lặp (MMR hoặc Intra-Document Deduplication)**:\n"
            "  + Hành động: Trên tập các chunk đã đạt điểm liên quan cao, áp dụng thuật toán MMR hoặc bộ lọc trùng lặp theo tài liệu (chỉ giữ tối đa 1-2 chunk tốt nhất từ cùng một `doc_id`, hoặc khử trùng lặp dựa trên cosine similarity giữa các chunk con > 0.85).\n"
            "  + Lý do thực hiện sau: Giải quyết triệt để vấn đề 3 chunk trùng lặp từ cùng một tài liệu mà vẫn đảm bảo các chunk được giữ lại đều liên quan đến câu hỏi.\n"
            "2. Chỉ số xác nhận mỗi bước đã khắc phục đúng lỗi (Verification Metrics):\n"
            "- **Chỉ số cho Bước 1 (Khắc phục lỗi xếp hạng sai)**: Đo lường **NDCG@K** và **Precision@K** — Xác nhận các tài liệu liên quan vươn lên nhóm dẫn đầu và tài liệu rác bị đẩy xuống đáy hoặc bị loại bỏ.\n"
            "- **Chỉ số cho Bước 2 (Khắc phục lỗi trùng lặp)**: Đo lường **Intra-List Diversity (ILD)** và **Tỷ lệ tài liệu duy nhất (Unique Document Ratio in Top-K)** — Xác nhận không còn 3 chunk trùng lặp chiếm dụng context."
        ),
        "explanation": (
            "Thứ tự xử lý chuẩn mực trong Reranking Pipeline: 'Relevance First, Diversity Second'. Nếu khử trùng lặp trước khi lọc độ liên quan, "
            "hệ thống có nguy cơ giữ lại một tài liệu rác chỉ vì nó 'khác biệt' và loại bỏ một tài liệu liên quan có giá trị cao. Việc tách biệt chỉ số đánh giá "
            "cho từng bước giúp kiểm chứng độc lập hiệu quả của từng tầng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế đúng thứ tự: Rerank trước, Dedup sau] (1.5 điểm): Xác định Bước 1 chạy Cross-Encoder lọc rác, Bước 2 chạy MMR/dedup lọc trùng lặp.\n"
            "- [Biện minh logic cho thứ tự] (1.0 điểm): Giải thích rõ việc lọc độ liên quan trước để tránh giữ lại tài liệu rác chỉ vì tính khác biệt.\n"
            "- [Chỉ số kiểm chứng độc lập cho từng bước] (1.5 điểm): Đưa ra metric chuẩn: NDCG@K/Precision@K cho Bước 1 và ILD/Unique Document Ratio cho Bước 2."
        ),
        "reference_source": "Teerapittayanon et al.: 'Multi-Stage Retrieval and Reranking with Diversity Controls' & LangChain Document Compressors"
    }
}
