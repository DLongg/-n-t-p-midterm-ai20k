# scripts/day10_part1.py
# -*- coding: utf-8 -*-
"""
Day 10: Data Pipeline & Observability
Questions 1 to 24 (d10-q001 to d10-q057)
"""

DAY10_PART1 = {}

# 1. d10-q001
DAY10_PART1["d10-q001"] = {
    "sample_answer": (
        "1. Lần chuyển dữ liệu sai đầu tiên có bằng chứng: Bước chuyển từ 'manifest ingestion' (ghi đúng 2026) sang 'dòng canonical sau cleaning' (bị đổi thành 2025). Bằng chứng cụ thể là artifact manifest ingestion vẫn lưu giá trị 2026 khớp với bản ghi nguồn, nhưng ngay tại đầu ra của cleaning stage (canonical dataset), trường policy_version đã bị ghi đè/biến đổi thành 2025. Các giai đoạn index, retrieval và câu trả lời của agent chỉ là cascading failure kế thừa dữ liệu sai từ canonical artifact.\n"
        "2. Bước kiểm tra tiếp theo để xác nhận: Kiểm tra mã nguồn và bộ rule biến đổi (transformation/normalization script) của giai đoạn cleaning, cụ thể là các hàm parse date/regex hoặc hardcoded default value đối với policy_version; đồng thời chạy unit test tái hiện (regression test) với input payload chứa 'policy_version=2026' qua hàm clean để xác nhận logic nào đã biến đổi 2026 thành 2025."
    ),
    "explanation": (
        "Trong kiến trúc Data Pipeline cho hệ thống RAG/Agent, lỗi Data Cascade xảy ra khi một khiếm khuyết dữ liệu ở tầng sớm lan truyền không kiểm soát xuống các tầng sau (vector index, retrieval chunk, LLM answer). Để định vị điểm lỗi gốc (root cause localization), nguyên lý bất biến là đối soát từng artifact trung gian theo thứ tự thời gian và lineage: nguồn gốc (2026) -> manifest ingestion (2026) -> canonical cleaning (2025). Sự chênh lệch (diff) đầu tiên xuất hiện tại đầu ra của cleaning, chứng minh bước làm sạch dữ liệu đã áp dụng phép biến đổi sai lệch hoặc áp dụng sai logic fallback/lookup."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Xác định chính xác bước chuyển sai đầu tiên là từ manifest ingestion sang canonical artifact (bước cleaning/transformation).\n"
        "- [1.5 điểm] Phân tích bằng chứng đối soát dữ liệu (data lineage audit) giữa các artifact để loại trừ nguyên nhân từ nguồn gốc và chứng minh tầng sau chỉ là cascading error.\n"
        "- [1.5 điểm] Nêu rõ bước kiểm tra cụ thể tiếp theo: soi code/rule biến đổi của cleaning pipeline và chạy test case cô lập với payload mẫu 2026."
    ),
    "reference_source": "Google SRE / Data Quality Fundamentals - Root Cause Analysis in Data Cascades: https://sre.google/sre-book/postmortem-culture/ và Great Expectations Data Contract Standards: https://docs.greatexpectations.io/"
}

# 2. d10-q005
DAY10_PART1["d10-q005"] = {
    "sample_answer": (
        "1. Vai trò chịu trách nhiệm: Release Manager / Data Platform Ops (kỹ sư vận hành đường ống dữ liệu phục vụ model/serving). Vai trò này chịu trách nhiệm quản lý commit boundary của serving layer và kiểm soát định tuyến alias giữa các snapshot.\n"
        "2. Artifact bằng chứng: Bản ghi triển khai hoặc lệnh switch alias có gắn audit trail (Deployment Manifest / Audit Log / GitOps PR), ghi rõ: commit hash, snapshot_id mới đã vượt qua quality checks, timestamp chuyển đổi, và danh tính người thực hiện (hoặc service account thực thi CI/CD).\n"
        "3. Điều kiện chấp nhận bàn giao (Handover Acceptance Criteria): (a) Có tài liệu Runbook chuẩn hóa quy định rõ thẩm quyền và thủ tục switch alias; (b) Kiểm thử routing tự động xác nhận serving alias phân giải về đúng snapshot mới; (c) Bản ghi bàn giao có chữ ký/phê duyệt của Data Lead và ML Serving Lead trước khi đóng incident."
    ),
    "explanation": (
        "Sự cố 'canonical data đã đạt chuẩn nhưng serving alias vẫn trỏ vào snapshot cũ' là vấn đề điển hình của việc thiếu ranh giới trách nhiệm (RACI) và thiếu cơ chế chuyển giao nguyên tử (atomic cutover). Trong kiến trúc phục vụ dữ liệu, việc tạo ra snapshot sạch và việc chuyển hướng traffic (alias pointer swap) phải được phân tách rõ ràng. Người nắm giữ quyền commit boundary phải cung cấp bằng chứng bất biến (immutable deployment record) và tuân thủ tiêu chí chấp nhận bàn giao để tránh tình trạng dữ liệu mồ côi hoặc không rõ ai có thẩm quyền kích hoạt."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Gán đúng vai trò chịu trách nhiệm (Data Platform Ops / Release Engineer / Serving Owner) có thẩm quyền kiểm soát commit boundary.\n"
        "- [1.5 điểm] Chỉ định rõ artifact bằng chứng (Deployment Audit Log / Alias Mapping Manifest / GitOps PR) ghi nhận sự kiện chuyển đổi.\n"
        "- [1.5 điểm] Thiết lập đầy đủ điều kiện chấp nhận bàn giao: runbook rõ ràng, kiểm thử phân giải alias tự động và ký duyệt nghiệm thu giữa các bên."
    ),
    "reference_source": "Martin Kleppmann, Designing Data-Intensive Applications (O'Reilly) - Dataflow, Immutability & Serving Layer Boundaries; Google Cloud Architecture Framework: https://cloud.google.com/architecture/framework"
}

# 3. d10-q006
DAY10_PART1["d10-q006"] = {
    "sample_answer": (
        "Bản đồ method -> failure -> monitor -> owner:\n"
        "1. DB snapshot hằng đêm:\n"
        "   - Method: Batch export / Snapshot dump từ cơ sở dữ liệu nguồn.\n"
        "   - Failure: Snapshot bị chậm/trễ (stale data), thiếu dữ liệu (missing rows), hoặc dump file bị hỏng (corrupted dump).\n"
        "   - Monitor: Kiểm tra kích thước file dump (size threshold), số lượng bản ghi (record count check), và độ trễ snapshot so với thời gian chốt (freshness timestamp alert).\n"
        "   - Owner: Database Administrator (DBA) / Core Data Engineering Team.\n"
        "2. API phân trang có 429:\n"
        "   - Method: HTTP REST pagination ingestion (offset/cursor-based).\n"
        "   - Failure: Rate limiting (HTTP 429 Too Many Requests), cạn kiệt hạn ngạch (quota exhaustion) hoặc rớt kết nối giữa các page.\n"
        "   - Monitor: Tỷ lệ mã phản hồi HTTP 429/5xx (API error rate metric), số lần retry vượt ngưỡng và consumer backoff time qua OpenTelemetry HTTP metrics.\n"
        "   - Owner: Integration Engineer / Ingestion Pipeline Team.\n"
        "3. Thư mục PDF có OCR:\n"
        "   - Method: File watcher / Object storage ingestion kết hợp pipeline OCR parsing.\n"
        "   - Failure: OCR parsing failure, font encoding lỗi, trích xuất thiếu bảng biểu (table structure loss) hoặc điểm tin cậy thấp (low confidence score < 0.8).\n"
        "   - Monitor: Tỷ lệ tài liệu có OCR confidence score thấp, phân phối độ dài văn bản sau OCR và số lượng file rơi vào thư mục lỗi / quarantine queue.\n"
        "   - Owner: Unstructured Data / ML Data Preparation Team."
    ),
    "explanation": (
        "Mỗi phương thức thu nạp (ingestion method) có các cơ chế lỗi (failure mode) vật lý và logic hoàn toàn khác biệt. Việc giám sát không thể dùng chung một chỉ số tổng thể mà phải dựa trên tín hiệu đặc trưng (characteristic signal) của lỗi đó: DB snapshot phụ thuộc vào tính toàn vẹn và độ tươi của file; API phụ thuộc vào giao thức mạng và rate limit; OCR phụ thuộc vào chất lượng thị giác và điểm tin cậy mô hình. Gán owner chính xác đảm bảo khi alert kích hoạt, đúng kỹ sư chuyên trách sẽ nhận sự cố để xử lý kịp thời theo SLA."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết lập đầy đủ bản đồ cho 3 nguồn với cấu trúc method -> failure -> monitor -> owner rõ ràng.\n"
        "- [1.5 điểm] Chỉ số giám sát (monitor) phân biệt chính xác đặc trưng hỏng hóc của từng nguồn (file size/freshness cho DB, HTTP 429 rate cho API, confidence/structure cho OCR).\n"
        "- [1.5 điểm] Phân định vai trò owner chuyên môn hóa tương ứng cho từng nguồn, tránh dồn chung trách nhiệm mơ hồ."
    ),
    "reference_source": "OpenTelemetry Instrumentation Standards for Ingestion Pipelines: https://opentelemetry.io/docs/specs/semconv/ và SRE Workbook - Practical Alerting & On-Call: https://sre.google/workbook/alerting-on-slos/"
}

# 4. d10-q007
DAY10_PART1["d10-q007"] = {
    "sample_answer": (
        "Chỉ ra lỗi và hiệu chỉnh cho từng dòng:\n"
        "1. Dòng (1) - Event stream có consumer lag nhưng chỉ theo dõi CPU của worker:\n"
        "   - Lỗi: CPU worker cao hay thấp không phản ánh trực tiếp tình trạng tồn đọng message. Worker có thể CPU thấp do bị deadlock, nghẽn I/O, hoặc CPU cao nhưng vẫn xử lý kịp.\n"
        "   - Sửa: Monitor trực tiếp chỉ số 'Consumer Group Lag' (số lượng offset chênh lệch giữa latest log end offset và committed consumer offset) trên Kafka/RabbitMQ. Owner: Streaming Platform Team / Event Pipeline Engineer.\n"
        "2. Dòng (2) - Object storage nhận file trùng tên nhưng chỉ theo dõi tên file:\n"
        "   - Lỗi: Tên file trùng nhau là trạng thái bình thường nếu có cập nhật phiên bản, nhưng chỉ theo dõi tên file không thể phát hiện ghi đè dữ liệu ngoài ý muốn (silent overwrite) hoặc race condition.\n"
        "   - Sửa: Monitor trường Content-MD5 / ETag checksum và kích hoạt Object Versioning; cảnh báo khi phát hiện checksum khác nhau cùng một key name hoặc xuất hiện event 's3:ObjectCreated:Put' ghi đè lên file đang được pipeline đọc. Owner: Data Lakehouse Storage Admin / Data Ingestion Team.\n"
        "3. Dòng (3) - SaaS export thỉnh thoảng thiếu partition nhưng alert không có owner:\n"
        "   - Lỗi: Cảnh báo không có người nhận (unowned alert) sẽ dẫn đến việc alert fatigue hoặc bị lờ đi hoàn toàn, vi phạm nguyên tắc cơ bản của SRE.\n"
        "   - Sửa: Thiết lập monitor 'Partition Completeness Check' (kiểm tra sự tồn tại của partition timestamp theo lịch hẹn) và định tuyến alert vào PagerDuty/Slack on-call cụ thể: SaaS Integration Engineer / Partner Data On-call Team."
    ),
    "explanation": (
        "Nguyên tắc cốt lõi của Observability trong hệ thống dữ liệu là 'theo dõi tín hiệu phản ánh trực tiếp trạng thái hư hỏng' (direct failure signal) thay vì chỉ số proxy gián tiếp. Consumer lag là thước đo trực tiếp của streaming bottleneck; Checksum/versioning là thước đo của xung đột lưu trữ; và bất kỳ alert nào sinh ra cũng phải có một 'On-Call Owner' với runbook xử lý tương ứng để chuyển hóa cảnh báo thành hành động khắc phục."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Chỉ ra đúng lỗi sai bản chất của cả 3 dòng trong bản đồ nháp (CPU proxy, name vs checksum, unowned alert).\n"
        "- [1.5 điểm] Đề xuất monitor thay thế chính xác: Consumer Group Lag cho stream, Checksum/ETag/Versioning cho object storage, Partition completeness schedule cho SaaS.\n"
        "- [1.5 điểm] Gán owner chịu trách nhiệm cụ thể và rõ ràng cho từng loại giám sát, đảm bảo tính khả thi vận hành."
    ),
    "reference_source": "Google SRE Book - Monitoring Distributed Systems: https://sre.google/sre-book/monitoring-distributed-systems/ và Apache Kafka Consumer Lag Monitoring: https://kafka.apache.org/documentation/#monitoring"
}

# 5. d10-q011
DAY10_PART1["d10-q011"] = {
    "sample_answer": (
        "1. Lựa chọn kiến trúc: Chọn ELT (Extract - Load - Transform). Lý do: Target lakehouse sở hữu năng lực compute mạnh mẽ, quy tắc nghiệp vụ biến động hàng tuần và yêu cầu audit bắt buộc phải replay lại từ input gốc. ELT cho phép nạp nguyên vẹn dữ liệu thô vào vùng Raw trước, sau đó dùng compute của Lakehouse chạy các script chuyển đổi (dbt/Spark/SQL) linh hoạt theo từng phiên bản rule.\n"
        "2. Vị trí lưu trữ Raw Data và Transformation Logic:\n"
        "   - Raw Data: Đặt tại vùng đệm 'Raw Zone / Bronze Layer' trên Object Storage của Lakehouse (bất biến - immutable, append-only, lưu kèm ingestion timestamp, source system, và raw payload).\n"
        "   - Transformation Logic: Đặt tại tầng 'Silver Layer' của Lakehouse, được mã hóa dưới dạng code (dbt models / Spark transformations có version control bằng Git), chạy định kỳ hoặc theo sự kiện để sinh ra dữ liệu Canonical.\n"
        "3. Guardrails cần thiết:\n"
        "   - Guardrail 1 (Access Control Boundary): Phân quyền nghiêm ngặt (IAM / RBAC) chặn hoàn toàn quyền đọc trực tiếp của RAG Agent vào Raw Zone; agent chỉ được phép đọc từ Curated/Gold serving table.\n"
        "   - Guardrail 2 (Immutability & Replayability Guard): Raw Zone được bật tính năng Write Once Read Many (WORM) hoặc bucket object lock để đảm bảo phục vụ audit và replay mà không bị sửa đổi lịch sử."
    ),
    "explanation": (
        "Mô hình ELT vượt trội hơn ETL truyền thống khi hạ tầng đích có compute có khả năng scale tốt và yêu cầu nghiệp vụ thay đổi thường xuyên. Trong ETL, việc chuyển đổi trước khi lưu trữ làm mất cấu trúc nguyên bản, khiến việc thay đổi rule đòi hỏi phải trích xuất lại từ source gốc (thường tốn kém hoặc bất khả thi). Với ELT, Raw Zone đóng vai trò là 'Source of Truth bất biến', cho phép tính toán lại lịch sử (replay) bất kỳ lúc nào. Tuy nhiên, ranh giới an toàn (guardrail) phân tầng là bắt buộc để ngăn chặn các truy vấn RAG vô tình lấy nhầm dữ liệu thô chưa làm sạch hoặc dữ liệu chứa thông tin nhạy cảm."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác kiến trúc ELT và giải thích lý do thuyết phục dựa trên compute mạnh, rule đổi hàng tuần và yêu cầu audit.\n"
        "- [1.5 điểm] Bố trí chuẩn xác vị trí Raw Data (Bronze/Object storage immutable) và Transformation Logic (Silver/dbt/code versioned).\n"
        "- [1.5 điểm] Thiết lập ít nhất 2 guardrail quan trọng: ranh giới cấm Agent truy cập trực tiếp Raw zone và chính sách bảo toàn dữ liệu thô (WORM/immutability)."
    ),
    "reference_source": "Databricks Medallion Architecture (Bronze-Silver-Gold design): https://www.databricks.com/glossary/medallion-architecture và dbt Labs Design Principles: https://docs.getdbt.com/terms/elt"
}

# 6. d10-q013
DAY10_PART1["d10-q013"] = {
    "sample_answer": (
        "1. Thiết kế luồng (Hybrid Architecture trên cùng Durable Log):\n"
        "   - Nền tảng chung: Sử dụng một durable message log trung tâm (như Apache Kafka hoặc AWS Kinesis) lưu trữ toàn bộ event `OrderCreated` với retention time tối thiểu 7 ngày.\n"
        "   - Luồng chặn gian lận (Fraud Detection): Sử dụng Stream Processing (Kafka Streams / Flink / Lightweight Python consumer), consume trực tiếp từ topic orders theo real-time offset, thực thi rule/model suy luận trong vòng < 500ms để trả kết quả chặn trước mốc 3 giây SLA.\n"
        "   - Luồng Dashboard (Business Reporting): Sử dụng Micro-batch / Batch Ingestion (ví dụ Kafka Connect S3 sink nạp parquet vào Data Lakehouse theo chu kỳ 15-30 phút), dashboard truy vấn trên dữ liệu aggregate hoàn tất.\n"
        "2. Checkpoint và Replay tối thiểu cần giữ:\n"
        "   - Checkpoint: Mỗi consumer group duy trì checkpoint offset độc lập được commit định kỳ (commit offset cho fraud group; Iceberg/Delta snapshot timestamp cho batch dashboard group).\n"
        "   - Replay Log: Durable log lưu trữ retention >= 7 ngày. Khi có sự cố thuật toán gian lận hoặc logic dashboard, nhóm chỉ cần reset consumer offset về timestamp mong muốn trên topic để replay lại toàn bộ luồng mà không cần query lại database nghiệp vụ nguồn."
    ),
    "explanation": (
        "Trong kiến trúc hướng sự kiện (Kappa Architecture), một durable commit log duy nhất có thể phục vụ đồng thời nhiều consumer có Service Level Agreement (SLA) khác nhau: consumer nhạy cảm với độ trễ (real-time stream) và consumer hướng dung lượng lớn (batch analytics). Việc duy trì consumer offset độc lập trên cùng log đảm bảo hai luồng không ảnh hưởng tài nguyên lẫn nhau (bulkhead isolation) và cho phép khả năng phát lại sự kiện (replayability) tức thời khi cần kiểm thử hồi quy hoặc khôi phục dữ liệu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế rõ ràng 2 luồng: Stream processing thời gian thực cho chặn gian lận (3s SLA) và Batch/Micro-batch cho dashboard (30m SLA).\n"
        "- [1.5 điểm] Xác định nền tảng log bền vững chung (Kafka/Kinesis) làm nguồn cung cấp dữ liệu duy nhất cho cả hai luồng.\n"
        "- [1.5 điểm] Trình bày đầy đủ cơ chế checkpoint độc lập theo consumer group và chính sách replay log (offset reset, log retention >= 7 ngày)."
    ),
    "reference_source": "Jay Kreps, 'Questioning the Lambda Architecture' (O'Reilly / Confluent): https://www.oreilly.com/radar/questioning-the-lambda-architecture/ và Apache Flink Checkpointing & State Management: https://nightlies.apache.org/flink/flink-docs-stable/"
}

# 7. d10-q017
DAY10_PART1["d10-q017"] = {
    "sample_answer": (
        "1. Chẩn đoán data loss: Lỗi thuộc loại 'Unprocessed Record Skipping'. Run 08:00 xử lý dải 101-200, trong đó các bản ghi 151-175 bị fail validation (chưa được ghi thành công vào canonical store), nhưng pipeline vẫn cập nhật `last_synced_id=200`. Do đó, lần chạy tiếp theo bắt đầu từ 201, dẫn đến 25 bản ghi (151-175) bị bỏ qua vĩnh viễn (silent data drop), vi phạm nguyên tắc toàn vẹn dữ liệu.\n"
        "2. Thiết kế checkpoint đúng: Checkpoint `last_synced_id` chỉ được tăng đến bản ghi liên tục thành công lớn nhất (high watermark of contiguous processed records), ở đây là `150`. Các bản ghi lỗi từ 151-175 phải được đẩy vào Quarantine / Dead Letter Queue (DLQ) kèm error payload.\n"
        "3. Thiết kế Replay và Stall Signal:\n"
        "   - Replay: Cơ chế replay riêng cho dải lỗi (DLQ re-drive) sau khi sửa rule hoặc data; hoặc nếu batch mang tính atomic thì rollback toàn bộ batch 101-200 và chạy lại từ 101.\n"
        "   - Stall Signal: Khi tỷ lệ lỗi vượt ngưỡng (ở đây 25/100 = 25% fail), pipeline phải phát tín hiệu Stall Alert (Hard Gate Stop), dừng tiến trình sync tự động và báo động cho On-call Engineer thay vì âm thầm nhảy watermark."
    ),
    "explanation": (
        "Nguyên tắc cơ bản của Watermarking và Checkpointing trong xử lý dữ liệu tuần tự là: 'Không bao giờ được đẩy watermark vượt qua bản ghi chưa hoàn tất hợp đồng (uncommitted / failed record)'. Nếu pipeline gặp lỗi nhưng vẫn cập nhật high-watermark theo ID lớn nhất đã đọc thay vì ID lớn nhất đã xử lý thành công, toàn bộ dữ liệu lỗi ở giữa sẽ bị mất dấu (lost window). Phải tách biệt rõ ràng giữa read-watermark và commit-watermark, kết hợp với DLQ để cô lập lỗi."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Chẩn đoán chính xác nguyên nhân data loss do watermark nhảy cóc qua dải bản ghi lỗi 151-175.\n"
        "- [1.5 điểm] Thiết kế lại checkpoint: chỉ commit đến bản ghi liên tục thành công (150) hoặc cô lập vào DLQ trước khi commit.\n"
        "- [1.5 điểm] Xây dựng cơ chế replay độc lập và định nghĩa tín hiệu dừng (stall signal / error rate threshold) khi gặp lỗi nghiêm trọng."
    ),
    "reference_source": "Apache Kafka Offset Management & Exactly-Once Semantics: https://kafka.apache.org/documentation/#semantics và Tyler Akidau et al., Streaming Systems (O'Reilly) - Watermarks & Checkpointing: https://www.oreilly.com/library/view/streaming-systems/9781491983867/"
}

# 8. d10-q020
DAY10_PART1["d10-q020"] = {
    "sample_answer": (
        "1. Tính Candidate Delay: Theo công thức Exponential Backoff with Additive Jitter:\n"
        "   - Base delay = 8.0s\n"
        "   - Jitter sample = +1.5s\n"
        "   - Candidate delay = Base delay + Jitter sample = 8.0s + 1.5s = 9.5 giây.\n"
        "2. Quyết định thực tế theo Attempt Limit: KHÔNG THỰC HIỆN RETRY (Abort / Fail Fast). Lý do: Attempt hiện tại đã là attempt 3 trong giới hạn tối đa 3 lần thử (attempt 3/3). Khi một request đã chạm ngưỡng tối đa (max_attempts = 3) mà vẫn nhận mã HTTP 429 Too Many Requests, quyền retry đã bị cạn kiệt (retry budget exhausted). Pipeline phải lập tức dừng gửi request, ghi nhận lỗi 'RateLimitExceeded (Max retries reached)', đẩy task vào hàng đợi chờ hoặc Dead Letter Queue, và phát cảnh báo để tránh spam upstream API."
    ),
    "explanation": (
        "Việc tính toán được candidate delay (9.5s) chỉ là bước xác định thời gian chờ nếu còn quyền thử lại. Tuy nhiên, trong thiết kế hệ thống phân tán chịu lỗi, 'Attempt Limit' (Budget Guardrail) là điều kiện chặn cứng (hard boundary) để ngăn chặn vòng lặp vô hạn và bão retry (retry storm). Ngay khi `current_attempt >= max_attempts`, hệ thống phải chuyển sang trạng thái xử lý lỗi (circuit open / error return), bảo toàn tài nguyên cho các tác vụ khác."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán chính xác candidate delay: 8s + 1.5s = 9.5s theo công thức backoff + jitter.\n"
        "- [1.5 điểm] Đưa ra quyết định thực tế chính xác: Không retry do đã cạn kiệt lượt thử (attempt 3/3 = max limit).\n"
        "- [1.0 điểm] Nêu rõ quy trình xử lý tiếp theo: log lỗi, fail-fast và chuyển task vào hàng đợi dự phòng/DLQ."
    ),
    "reference_source": "AWS Architecture Blog - Exponential Backoff And Jitter: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ và Google Cloud API Design Guide - Retrying Requests: https://cloud.google.com/apis/design/errors#retrying_errors"
}

# 9. d10-q023
DAY10_PART1["d10-q023"] = {
    "sample_answer": (
        "1. Giải thích rủi ro Duplicate và Skip:\n"
        "   - Rủi ro Duplicate: Khi một dòng mới được chèn ở đầu bảng sau khi page 1 vừa đọc xong, toàn bộ các bản ghi trong database bị dịch chuyển chỉ số xuống 1 đơn vị. Bản ghi thứ 100 (cuối cùng của page 1) giờ đây bị đẩy sang vị trí thứ 101. Khi consumer gọi page 2 với `offset=100`, database sẽ đọc từ bản ghi thứ 101, khiến bản ghi cũ này bị đọc lại lần thứ hai (Duplicate Record).\n"
        "   - Rủi ro Skip: Ngược lại, nếu một dòng ở page 1 bị xóa, bản ghi thứ 101 sẽ bị kéo lên vị trí thứ 100 và sẽ bị bỏ sót hoàn toàn khi đọc page 2.\n"
        "2. Thiết kế Resume an toàn (Cursor/Keyset Pagination):\n"
        "   - Thay thế pagination bằng Keyset Pagination dựa trên trường bất biến có chỉ mục: `WHERE (created_at, id) < (:last_created_at, :last_id) ORDER BY created_at DESC, id DESC LIMIT 100`.\n"
        "   - Con trỏ (cursor) lưu trữ cặp giá trị `(created_at, id)` của bản ghi cuối cùng đã xử lý thành công. Khi resume, truy vấn tiếp tục chính xác từ sau mốc con trỏ đó, miễn nhiễm hoàn toàn với việc chèn hoặc xóa bản ghi ở đầu hay giữa bảng."
    ),
    "explanation": (
        "Offset-based pagination (`OFFSET N LIMIT M`) chỉ hoạt động ổn định trên tập dữ liệu tĩnh tuyệt đối. Trong hệ thống trực tuyến có dữ liệu ghi liên tục, việc dùng offset tạo ra 'cửa sổ trượt không ổn định' (shifting window anomaly). Keyset/Cursor-based pagination giải quyết triệt để vấn đề này bằng cách neo vị trí đọc vào một điểm bất biến trên không gian khóa (deterministic key space), đảm bảo tính lũy tiến và có thể resume an toàn sau sự cố mà không lo trùng lặp hay sót dữ liệu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Phân tích chính xác cơ chế dịch chuyển chỉ mục gây duplicate (bản ghi 100 thành 101 bị đọc lại ở offset 100) và rủi ro skip khi có biến động dữ liệu.\n"
        "- [1.5 điểm] Thiết kế giải pháp Keyset/Cursor-based pagination sử dụng cặp khóa (created_at, id) bất biến kèm cú pháp truy vấn cụ thể.\n"
        "- [1.0 điểm] Mô tả rõ cơ chế resume an toàn dựa trên giá trị cursor lưu trong checkpoint."
    ),
    "reference_source": "Use The Index, Luke! - Keyset Pagination: https://use-the-index-luke.com/no-offset và Martin Kleppmann, Designing Data-Intensive Applications - Secondary Indexes & Cursor Iteration"
}

# 10. d10-q027
DAY10_PART1["d10-q027"] = {
    "sample_answer": (
        "1. Thiết kế Metadata Schema chuẩn cho tài liệu:\n"
        "   - `document_id`: UUID duy nhất cho từng bản thể lưu trữ.\n"
        "   - `canonical_name`: Tên định danh logic chuẩn (ví dụ `hr_general_policy`).\n"
        "   - `content_hash`: Chuỗi SHA-256 nội dung file (H1, H2) để xác minh tính toàn vẹn.\n"
        "   - `source_system`: Nguồn gốc xuất xứ (`hr_portal` vs `email_attachment`).\n"
        "   - `source_authority_tier`: Cấp độ thẩm quyền (ví dụ Tier 1: HR Official Portal; Tier 3: Email Personal Inbox).\n"
        "   - `effective_date`: Ngày có hiệu lực chính thức (2026-01-01 vs 2024-01-01).\n"
        "   - `lifecycle_status`: Trạng thái vòng đời (`ACTIVE`, `SUPERSEDED`, `QUARANTINED`).\n"
        "2. Quyết định Active / Superseded:\n"
        "   - File H2 từ HR portal (effective 2026): Được đánh dấu `ACTIVE` và đưa vào Vector Index phục vụ RAG. Lý do: HR Portal là nguồn có thẩm quyền cao nhất (Authoritative Source of Truth) và có ngày hiệu lực mới nhất (2026).\n"
        "   - File H1 từ email attachment (effective 2024): Được đánh dấu `SUPERSEDED` (hoặc Archived), loại bỏ khỏi active search index để tránh agent trả lời thông tin chính sách cũ đã hết hạn, nhưng vẫn giữ bản ghi trong kho lưu trữ kèm lineage phục vụ audit."
    ),
    "explanation": (
        "Tên file (`policy.pdf`) và mã băm (`hash`) chỉ là các thuộc tính vật lý, không đại diện cho thẩm quyền nghiệp vụ (business authority) hay tính hiệu lực theo thời gian. Trong quản trị tri thức cho Agent, việc xác định phiên bản hiện hành phải dựa trên 'Hierarchy of Authority' (Thứ bậc thẩm quyền nguồn) và 'Effective Timestamp'. Việc gắn nhãn siêu dữ liệu rõ ràng giúp phân định trạng thái Active/Superseded, ngăn chặn việc mô hình truy hồi phải các chính sách hết hạn được gửi qua email không chính thức."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xây dựng đầy đủ metadata schema chứa các trường cốt lõi: canonical_name, content_hash, source_authority_tier, effective_date, lifecycle_status.\n"
        "- [1.5 điểm] Ra quyết định chuẩn xác: H2 là ACTIVE (do nguồn HR portal có thẩm quyền cao và hiệu lực 2026), H1 là SUPERSEDED.\n"
        "- [1.0 điểm] Nêu rõ giải pháp bảo đảm an toàn: loại bỏ file superseded khỏi vector index phục vụ RAG và lưu trữ cho audit."
    ),
    "reference_source": "DAMA-DMBOK: Data Management Body of Knowledge - Metadata Management and Document Retention Policies; W3C PROV-O Data Lineage Model: https://www.w3.org/TR/prov-o/"
}

# 11. d10-q029
DAY10_PART1["d10-q029"] = {
    "sample_answer": (
        "1. Chọn Disposition (Biện pháp xử lý): QUARANTINE / REJECT (Tạm đình chỉ, đưa vào hàng đợi chờ người duyệt - Human-in-the-Loop review). Tuyệt đối KHÔNG xuất bản (publish) hoặc đưa văn bản này vào pipeline tạo embedding cho Vector Database.\n"
        "2. Evidence (Bằng chứng) cần giữ lại:\n"
        "   - File hình ảnh / PDF gốc của trang văn bản (visual source artifact);\n"
        "   - Toàn bộ kết quả OCR text thô kèm bounding box coordinates và confidence map của từng token (.91 overall);\n"
        "   - Báo cáo kiểm định cấu trúc (Schema/Table Structural Validation Log) chỉ rõ bảng giá bị mất cột 'đơn vị' (missing mandatory column 'unit').\n"
        "3. Exit Criterion (Tiêu chí nghiệm thu) trước khi cho phép embed:\n"
        "   - Bảng giá phải được khôi phục đầy đủ cấu trúc: cả cột đơn giá và cột 'đơn vị tính' (VND, USD, triệu đồng...) được trích xuất hoàn chỉnh;\n"
        "   - Hoặc (a) Được parser chuyên dụng cho bảng biểu (Table Transformer / PaddleOCR) parse lại thành công và vượt qua schema test, hoặc (b) Được nhân viên nghiệp vụ (Human Reviewer) xác nhận chỉnh sửa và ký duyệt thủ công."
    ),
    "explanation": (
        "Độ tin cậy tổng thể cao (.91) và độ dài văn bản bình thường là các chỉ số đánh lừa (vanity metrics) trong trích xuất OCR. Việc mất đi một trường mang tính ngữ nghĩa quyết định như 'đơn vị' trong bảng giá là một lỗi nghiêm trọng: 100 nghìn khác 100 triệu. Nếu đưa vào vector database, RAG agent sẽ tạo ra thông tin sai lệch tai hại (hallucination về giá cả). Do đó, quy tắc kiểm định cấu trúc bảng biểu phải đóng vai trò là một 'Hard Quality Gate' chặn dữ liệu trước khi embedding."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn disposition chính xác là QUARANTINE / REJECT (chặn embed, chuyển sang review).\n"
        "- [1.5 điểm] Xác định đầy đủ 3 bằng chứng cần lưu trữ: visual gốc, token bounding boxes/confidence map và log lỗi mất cột đơn vị.\n"
        "- [1.5 điểm] Định nghĩa rõ ràng tiêu chí nghiệm thu (exit criteria): bảng giá có đầy đủ cột đơn vị được schema validate hoặc có sự xác nhận của con người."
    ),
    "reference_source": "Google Cloud Document AI Documentation - Handling Table Parsing & Extraction Quality: https://cloud.google.com/document-ai/docs/handle-tables và Great Expectations Table Schema Quality Standards: https://docs.greatexpectations.io/"
}

# 12. d10-q031
DAY10_PART1["d10-q031"] = {
    "sample_answer": (
        "1. Thiết lập ranh giới Queue và Acknowledgment (Queue/Ack Boundary):\n"
        "   - Ingestion Boundary (Producer Side): Webhook API gateway nhận HTTP POST, chỉ thực hiện kiểm tra tính hợp lệ cơ bản (schema validation thô) rồi đẩy ngay message vào một Durable Message Broker (như Kafka / RabbitMQ / AWS SQS). Khi broker trả về 'Message Persisted / Write Ack', Webhook API lập tức phản hồi HTTP 202 Accepted cho đối tác trong vòng < 50ms.\n"
        "   - Processing Boundary (Consumer Side): Một nhóm worker chạy nền độc lập (background consumers) pull message từ queue, thực hiện transform tốn 2s. Worker CHỈ gửi Ack / Commit Offset cho broker SAU KHI transformation hoàn tất thành công và lưu kết quả an toàn.\n"
        "2. Giám sát (Monitoring):\n"
        "   - Ingestion Latency: P95 và P99 response time của Webhook endpoint (< 200ms).\n"
        "   - Queue Depth / Consumer Lag: Số lượng message đang tồn đọng trong queue.\n"
        "   - Worker Processing Time & Error Rate: Thời gian chạy trung bình của worker và tỷ lệ transform fail.\n"
        "3. Chính sách xử lý lỗi (Failure Policy):\n"
        "   - Lỗi tạm thời (transient): Retry với Exponential Backoff + Jitter tối đa 3 lần.\n"
        "   - Lỗi vĩnh viễn (poison pill / format lỗi): Chuyển message sang Dead Letter Queue (DLQ) kèm toàn bộ stack trace lỗi để phân tích ngoại tuyến mà không làm tắc nghẽn queue chính."
    ),
    "explanation": (
        "Nguyên tắc cốt lõi để đáp ứng SLA độ trễ cao (HTTP 202 trong 200ms) khi tác vụ xử lý tốn nhiều thời gian (2s) là 'Bất đồng bộ hóa qua hàng đợi' (Asynchronous Decoupling). Webhook Ack chỉ xác nhận 'Đã tiếp nhận vào hàng đợi an toàn', trong khi Consumer Ack xác nhận 'Đã xử lý xong nghiệp vụ'. Sự phân tách này bảo vệ hệ thống khỏi quá tải (backpressure protection) và ngăn ngừa mất dữ liệu nếu worker gặp sự cố giữa chừng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Phân định chuẩn xác hai ranh giới ack: Producer ack (HTTP 202 sau khi ghi queue) và Consumer ack (chỉ ack sau khi transform thành công).\n"
        "- [1.5 điểm] Thiết lập đầy đủ các chỉ số giám sát: API p95/p99 latency, queue depth/lag và worker failure rate.\n"
        "- [1.0 điểm] Xây dựng failure policy cụ thể: retry có giới hạn cho transient failure và chuyển sang Dead Letter Queue (DLQ) cho poison pills."
    ),
    "reference_source": "Enterprise Integration Patterns - Message Channel & Guaranteed Delivery: https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedMessaging.html và Martin Kleppmann, Designing Data-Intensive Applications (O'Reilly)"
}

# 13. d10-q033
DAY10_PART1["d10-q033"] = {
    "sample_answer": (
        "1. Thiết kế Control (Hệ thống kiểm soát áp lực ngược - Backpressure Control):\n"
        "   - Đánh giá trạng thái: Producer tốc độ 200/s, Consumer tốc độ 120/s -> Net Influx = +80 msg/s. Queue depth tăng vọt từ 1k -> 4k -> 9k trong 3 phút, đã vượt xa ngưỡng an toàn 5k (threshold=5k).\n"
        "   - Phía Producer (Admission Control): Kích hoạt cơ chế Rate Limiting / Traffic Throttling tại API Gateway. Áp dụng thuật toán Leaky Bucket / Token Bucket để giảm lưu lượng tiếp nhận từ client xuống mức tối đa 120/s. Khi queue depth > 5k, Gateway trả về HTTP 429 Too Many Requests kèm header `Retry-After: 30` đối với các request không khẩn cấp.\n"
        "   - Phía Consumer (Elastic Scaling): Kích hoạt KEDA / Kubernetes HPA scale out số lượng consumer pods dựa trên custom metric `queue_depth > 5000`, tăng từ N replicas lên tối thiểu `ceil(200 / (120/N))` để cân bằng tốc độ xử lý.\n"
        "2. Hệ quả hiển thị đối với người dùng (User-Visible Consequence):\n"
        "   - Client/Người dùng nhận thông báo trạng thái: 'Hệ thống đang tiếp nhận khối lượng công việc lớn, yêu cầu của bạn đang được xếp hàng xử lý chậm hơn bình thường' (degraded performance SLA).\n"
        "   - Các bản ghi mới được gửi lên sẽ có độ trễ cập nhật trên dashboard/agent (freshness lag tăng thêm vài phút) thay vì bị sập hệ thống hoặc mất dữ liệu."
    ),
    "explanation": (
        "Khi tốc độ sản sinh dữ liệu lớn hơn tốc độ tiêu thụ, nếu không có cơ chế backpressure quay ngược về producer, hàng đợi sẽ tăng vô hạn dẫn đến cạn kiệt bộ nhớ (OOM) hoặc sập broker. Cơ chế backpressure chuẩn mực phải tạo ra 'phản hồi ngược' (feedback loop) từ tầng hàng đợi về tầng ingress để làm chậm hoặc từ chối có kiểm soát các yêu cầu mới, đồng thời tự động co giãn tài nguyên xử lý để đưa queue depth về dưới ngưỡng an toàn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích đúng số liệu net influx (+80 msg/s) và việc queue depth (9k) đã phá vỡ ngưỡng threshold (5k).\n"
        "- [1.5 điểm] Thiết kế kiểm soát backpressure ở 2 đầu: Rate limit/throttling phía producer (HTTP 429 + Retry-After) và Autoscaling phía consumer.\n"
        "- [1.5 điểm] Trình bày rõ ràng hệ quả thấy được với người dùng (user-visible consequence): thông báo suy giảm hiệu năng và độ trễ dữ liệu tăng nhưng hệ thống không mất mát dữ liệu."
    ),
    "reference_source": "Reactive Streams Specification - Backpressure Protocol: https://www.reactive-streams.org/ và Kubernetes Event-driven Autoscaling (KEDA) Documentation: https://keda.sh/"
}

# 14. d10-q037
DAY10_PART1["d10-q037"] = {
    "sample_answer": (
        "1. Chẩn đoán nguyên nhân sự cố: Vi phạm tính đơn định và khả năng tái lập (Violation of Deterministic Replayability). Dữ liệu canonical bị can thiệp chỉnh sửa thủ công trực tiếp trên CSV (manual out-of-band edit). Thay đổi này không được mã hóa thành code, rule hay migration script và không được lưu vào kho lưu trữ raw/audit. Khi Run B được kích hoạt lại từ raw data bằng code v3, toàn bộ dữ liệu canonical bị tạo lại từ đầu (recomputed from scratch), dẫn đến mọi chỉnh sửa tay biến mất hoàn toàn.\n"
        "2. Thiết kế cơ chế Replay và Audit đúng chuẩn:\n"
        "   - Cấm hoàn toàn sửa trực tiếp vào file canonical (Immutable Canonical Layer).\n"
        "   - Mô hình hóa can thiệp con người dưới dạng 'Correction Event' trong kho lưu trữ dữ liệu thô: Tạo bảng `manual_corrections` hoặc `patch_manifest` (lưu: `record_id`, `field_name`, `old_value`, `new_value`, `reason`, `operator_id`, `approved_by`, `timestamp`).\n"
        "   - Tích hợp logic áp dụng patch vào pipeline code v4: Sau khi clean tự động, pipeline tự động join với `manual_corrections` để đè các trường đã được phê duyệt.\n"
        "   - Audit Trail: Bất kỳ lần Replay nào (Run C, Run D) từ raw + correction events đều tạo ra kết quả đồng nhất tuyệt đối (deterministic idempotency)."
    ),
    "explanation": (
        "Trong kỹ nghệ dữ liệu hiện đại, nguyên lý 'Code as Configuration' và 'Data Immutability' quy định rằng mọi trạng thái của dữ liệu phái sinh phải là một hàm thuần túy (pure function) của Dữ liệu thô và Mã xử lý: `Canonical = f(Raw, Code)`. Nếu có sự tham gia của con người để sửa sai, hành động đó phải được coi như một luồng dữ liệu đầu vào bổ sung (Data Patch / Correction Event) có version control và audit log đầy đủ, chứ không bao giờ được chỉnh sửa trực tiếp vào tầng serving."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Chẩn đoán chính xác nguyên nhân: chỉnh sửa thủ công ngoài luồng (out-of-band manual edit) không được mã hóa nên bị xóa sạch khi replay.\n"
        "- [1.5 điểm] Thiết kế giải pháp chuẩn: cấm sửa canonical, mô hình hóa can thiệp thành bảng/sự kiện hiệu chỉnh (Correction Events / Patch Manifest) có kiểm toán.\n"
        "- [1.5 điểm] Tích hợp logic áp dụng patch vào code pipeline để đảm bảo replayability hoàn toàn có tính đơn định (deterministic)."
    ),
    "reference_source": "Martin Kleppmann, Designing Data-Intensive Applications - Reproducibility, Immutability & Event Sourcing; DataOps Principles: https://dataopsmanifesto.org/"
}

# 15. d10-q040
DAY10_PART1["d10-q040"] = {
    "sample_answer": (
        "1. Disposition riêng cho từng field của bản ghi (row status=open, thiếu cả ba trường):\n"
        "   - `ticket_id`: DISPOSITION = REJECT / HARD ERROR. Theo contract, `ticket_id` là khóa bắt buộc (required primary key). Bản ghi không có định danh thì không thể tham chiếu, không thể cập nhật và không có giá trị nghiệp vụ -> Phải loại bỏ toàn bộ bản ghi khỏi canonical pipeline và chuyển vào Dead Letter Queue.\n"
        "   - `closed_at`: DISPOSITION = ACCEPT AS NULL (Hợp lệ). Theo contract, khi `status=open`, ticket chưa đóng nên `closed_at` là trường tùy chọn và mang giá trị `NULL` là đúng logic nghiệp vụ.\n"
        "   - `created_at`: DISPOSITION = RECOVER / DERIVE. Theo contract, `created_at` có thể suy diễn (derive) từ timestamp của signed event trong message metadata. Pipeline tiến hành trích xuất event timestamp từ header, format về ISO-8601 và gán vào `created_at`.\n"
        "2. Lineage cần lưu giữ:\n"
        "   - Lưu bản ghi thô gốc vào Quarantine/Audit table với cờ lỗi `REJECTED_MISSING_PRIMARY_KEY`;\n"
        "   - Ghi nhận metadata lineage: `source_event_id`, `raw_payload_hash`, `validation_rule_failed='ticket_id IS NOT NULL'`, và ghi chú đã phục hồi thử `created_at` từ event timestamp."
    ),
    "explanation": (
        "Chính sách xử lý trường thiếu (Field Missingness Policy) phải được đánh giá chi tiết theo từng thuộc tính của hợp đồng dữ liệu (data contract): (1) Khóa chính bắt buộc bị thiếu làm mất tính toàn vẹn thực thể (entity integrity), bắt buộc phải reject; (2) Trường phụ thuộc trạng thái (như closed_at khi status=open) phản ánh đúng ngữ nghĩa nghiệp vụ; (3) Trường có thể suy diễn có nguồn gốc tin cậy (như signed event timestamp) cần được tự động bù đắp kèm theo audit trail."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Phân loại đúng disposition cho cả 3 trường: ticket_id bị REJECT do thiếu required key; closed_at được CHẤP NHẬN NULL do status=open; created_at được DERIVE từ signed event timestamp.\n"
        "- [1.5 điểm] Đưa ra kết luận tổng thể cho cả bản ghi: do thiếu ticket_id nên bản ghi bị loại (quarantine/DLQ) dù 2 trường kia có thể giải quyết.\n"
        "- [1.0 điểm] Thiết lập đầy đủ thông tin data lineage và audit record phục vụ truy vết."
    ),
    "reference_source": "Great Expectations Core Concepts - Expectation Suites & Missingness Evaluation: https://docs.greatexpectations.io/ và W3C Data Quality Vocabulary: https://www.w3.org/TR/vocab-dqv/"
}

# 16. d10-q041
DAY10_PART1["d10-q041"] = {
    "sample_answer": (
        "1. Canonicalize các input được hỗ trợ:\n"
        "   - Input 1: `2026-04-05` -> Đã đúng định dạng chuẩn ISO-8601 `YYYY-MM-DD`. Kết quả: `2026-04-05` (Ngày 5 tháng 4 năm 2026).\n"
        "   - Input 2: `05/04/2026` có locale metadata là `vi` (Việt Nam theo quy ước `DD/MM/YYYY`) -> Parse thành công ngày = 05, tháng = 04, năm = 2026. Kết quả emit chuẩn ISO: `2026-04-05`.\n"
        "2. Xử lý bản ghi cuối (`04/05/2026` thiếu locale provenance):\n"
        "   - Phân tích rủi ro: Chuỗi `04/05/2026` có thể là ngày 4 tháng 5 năm 2026 (nếu locale `vi`/`en-GB` theo DD/MM) hoặc ngày 5 tháng 4 năm 2026 (nếu locale `en-US` theo MM/DD). Do thiếu hoàn toàn thông tin xuất xứ locale (locale provenance), pipeline không được tự ý phỏng đoán (silent guess).\n"
        "   - Xử lý: Đánh dấu bản ghi là `AMBIGUOUS_DATE_FORMAT`, chuyển vào Quarantine Queue / Dead Letter Queue, không đưa vào canonical serving table. Gửi cảnh báo yêu cầu nguồn dữ liệu bổ sung trường header `locale` hoặc chuẩn hóa về ISO trước khi gửi lại."
    ),
    "explanation": (
        "Sự mơ hồ về định dạng ngày tháng (Date Ambiguity Anomaly) giữa quy ước MM/DD/YYYY và DD/MM/YYYY là một trong những nguyên nhân hàng đầu gây sai lệch dữ liệu thời gian. Nguyên tắc thiết kế pipeline nghiêm ngặt quy định: 'Tuyệt đối không đoán mò khi thiếu ngữ cảnh xuất xứ' (No guessing without provenance). Chỉ các chuỗi có định dạng chuẩn ISO hoặc có metadata locale rõ ràng mới được phép canonicalize; các trường hợp mơ hồ phải được cách ly để bảo toàn tính trung thực của dữ liệu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Chuẩn hóa chính xác 2 bản ghi hợp lệ sang ISO-8601 `2026-04-05` (Input 1 chuẩn ISO, Input 2 theo locale vi là DD/MM/YYYY).\n"
        "- [1.5 điểm] Nhận diện chính xác tính mơ hồ (ambiguity giữa 04/05 và 05/04) của bản ghi cuối do thiếu locale provenance.\n"
        "- [1.0 điểm] Xử lý an toàn bản ghi cuối: đưa vào quarantine/DLQ, từ chối đoán mò và yêu cầu bổ sung provenance."
    ),
    "reference_source": "ISO 8601 Date and Time Format Standard: https://www.iso.org/iso-8601-date-and-time-format.html và Python `dateutil` Parser Best Practices"
}

# 17. d10-q044
DAY10_PART1["d10-q044"] = {
    "sample_answer": (
        "1. Thiết kế phương án Recovery (Khôi phục dữ liệu):\n"
        "   - Nguyên tắc: Tuyệt đối KHÔNG cố gắng viết hàm sửa ngược từ chuỗi đã bị hỏng mojibake `Nguyá»…n` (vì các phép biến đổi chuỗi hỏng thường mất mát ký tự và thiếu tính đơn định).\n"
        "   - Giải pháp: Tận dụng Raw Bytes hoặc Visual Source còn nguyên vẹn làm Source of Truth có thẩm quyền cao nhất. Pipeline quay trở lại bản ghi Raw ban đầu, decode lại trực tiếp từ mảng bytes gốc bằng chuẩn `UTF-8` (hoặc trích xuất lại từ visual source OCR) để tái tạo chính xác tên `Nguyễn`.\n"
        "   - Vá lỗi pipeline: Tìm và sửa pipeline trung gian đã gây ra lỗi encoding (thường do đọc byte UTF-8 bằng encoding `windows-1252` hoặc `ISO-8859-1` rồi lại encode UTF-8).\n"
        "2. Thiết kế Lineage và Audit Trail:\n"
        "   - Ghi lại bản ghi audit: `field='full_name'`, `corrupted_value='Nguyá»…n'`, `restored_value='Nguyễn'`, `recovery_source='raw_bytes_blob'`, `recovery_method='utf8_redecode'`, `timestamp=NOW()`.\n"
        "   - Bổ sung Data Quality Gate: Kiểm tra tính hợp lệ của chuỗi Unicode (không chứa các mẫu mojibake phổ biến như `Ã`, `Â`, `»`, `…`) ngay tại đầu ra của mọi stage trung gian."
    ),
    "explanation": (
        "Mojibake xảy ra khi chuỗi byte được mã hóa bằng chuẩn này nhưng lại bị giải mã bằng chuẩn khác trong một trạm trung gian của pipeline. Khi nguồn raw bytes hoặc tài liệu gốc vẫn còn nguyên vẹn, giải pháp an toàn và đáng tin cậy duy nhất là 'Khôi phục từ nguồn có thẩm quyền' (Recover from Authoritative Source), thay vì cố gắng đảo ngược chuỗi hỏng bằng heuristic. Đồng thời, phải thiết lập rào chắn kiểm thử encoding tại mọi bước chuyển dữ liệu để ngăn tái diễn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xác định đúng giải pháp recovery: khôi phục trực tiếp từ raw bytes gốc/visual source, không sửa từ chuỗi mojibake đã hỏng.\n"
        "- [1.5 điểm] Chỉ ra nguyên nhân gốc ở pipeline trung gian (giải mã sai encoding) và giải pháp sửa chữa triệt để.\n"
        "- [1.0 điểm] Thiết kế lineage audit trail ghi nhận quá trình khôi phục và bổ sung quality gate kiểm tra Unicode."
    ),
    "reference_source": "Unicode Standard Annex #44 - Unicode Character Database: https://www.unicode.org/reports/tr44/ và Python Unicode HOWTO: https://docs.python.org/3/howto/unicode.html"
}

# 18. d10-q045
DAY10_PART1["d10-q045"] = {
    "sample_answer": (
        "1. Định nghĩa Business Key và Phân biệt Version vs Duplicate:\n"
        "   - Phân tích: Đơn hàng số 7 có các bản ghi với `version=1` và `version=2`. Cùng `order=7` không đồng nghĩa là trùng lặp, mà đây là các trạng thái thay đổi theo thời gian (State Progression / Event Versioning).\n"
        "   - Business Key thực sự: Cặp composite key `(order_id, version)`.\n"
        "   - Phân loại: Dòng A (7, 1, pending) là phiên bản 1; Dòng B (7, 2, paid) và Dòng D (7, 2, paid) cùng có khóa `(order=7, version=2)` và cùng nguồn/hash -> D và B là bản sao trùng lặp thực sự (True Duplicate). Dòng C (8, 1, paid) là đơn hàng khác hoàn toàn.\n"
        "2. Chọn Survivor (Bản ghi sống sót) và Audit:\n"
        "   - Nếu mô hình hóa Snapshot hiện hành (Current State): Chọn bản ghi có `order_id` duy nhất với `version` cao nhất -> Với order 7, chọn phiên bản 2 (`version=2, status=paid`); giữa B và D chỉ giữ lại 1 dòng duy nhất (Deduplication).\n"
        "   - Nếu mô hình hóa Lịch sử sự kiện (Event Log / SCD Type 2): Giữ cả A (version 1) và một bản thể duy nhất của B (version 2).\n"
        "   - Audit Trail: Ghi log dòng D bị khử trùng lặp (deduplicated) kèm `duplicate_of=B_row_id`, `dedup_rule='exact_hash_match'`, `timestamp=NOW()`."
    ),
    "explanation": (
        "Việc khử trùng lặp dữ liệu (Deduplication) đòi hỏi phải phân biệt sâu sắc giữa 'Trùng lặp kỹ thuật' (Technical Duplicate - hai bản ghi giống hệt nhau gửi lặp) và 'Tiến trình nghiệp vụ' (Business Versioning - cùng entity nhưng khác version/trạng thái). Khóa kinh doanh phải phản ánh đúng chiều thời gian hoặc phiên bản sự kiện. Việc chọn survivor phụ thuộc vào mục tiêu lưu trữ (tổng hợp trạng thái cuối hay lưu vết toàn bộ lịch sử biến đổi)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Định nghĩa đúng business key là composite `(order_id, version)` và phân biệt rõ ràng giữa versioning (A vs B) và true duplicate (B vs D).\n"
        "- [1.5 điểm] Lựa chọn bản ghi survivor chính xác theo ngữ cảnh (giữ version 2 cao nhất cho current state và khử trùng lặp giữa B và D).\n"
        "- [1.0 điểm] Thiết lập audit trail chi tiết cho bản ghi bị loại bỏ (deduplication audit log)."
    ),
    "reference_source": "Ralph Kimball, The Data Warehouse Toolkit - Slowly Changing Dimensions (SCD Type 2) và Martin Kleppmann, Designing Data-Intensive Applications - Idempotency & Deduplication"
}

# 19. d10-q047
DAY10_PART1["d10-q047"] = {
    "sample_answer": (
        "1. Thực hiện Mapping dữ liệu theo declared contract:\n"
        "   - `ticket_id: 42` -> ép kiểu chuỗi thành `id: '42'` (thỏa mãn `id:str required`).\n"
        "   - `urgency: 'high'` -> ánh xạ theo rule `high -> P1` thành `priority: 'P1'` (thỏa mãn `priority ∈ {P1, P2, P3}`).\n"
        "   - `date: '05/04/2026'` với metadata `locale=vi` (ngày/tháng/năm) -> parse thành ngày 05 tháng 04 năm 2026, chuyển sang ISO date: `created_at: '2026-04-05'`.\n"
        "2. Validate đối chiếu với Canonical Schema:\n"
        "   - Kết quả bản ghi sau mapping: `{'id': '42', 'priority': 'P1', 'created_at': '2026-04-05'}`.\n"
        "   - Kiểm tra: `id` có kiểu chuỗi và không rỗng (PASS); `priority` thuộc tập hợp cho phép `{P1, P2, P3}` (PASS); `created_at` đúng chuẩn ISO-8601 date (PASS).\n"
        "3. Báo cáo kết quả:\n"
        "   - Trạng thái: VALID (Thành công 100%).\n"
        "   - Output Artifact: Dòng canonical hoàn chỉnh được bàn giao cho tầng tiếp theo (enrichment/indexing), kèm theo audit log mapping."
    ),
    "explanation": (
        "Mapping từ cấu trúc bản xứ (native schema) sang cấu trúc chuẩn mực (canonical schema) phải được định nghĩa bằng các hợp đồng biến đổi tường minh (explicit declared mappings), không được dựa trên việc suy đoán ngẫu nhiên. Sau khi mapping hoàn tất, bản ghi bắt buộc phải vượt qua bộ kiểm thử schema xác thực kiểu dữ liệu, các ràng buộc giá trị (enum set) và định dạng ngày chuẩn trước khi được đưa vào kho dữ liệu chính thức."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Thực hiện chính xác toàn bộ 3 phép mapping: ticket_id thành chuỗi '42', urgency 'high' thành 'P1', date thành ISO '2026-04-05'.\n"
        "- [1.5 điểm] Đối chiếu và kiểm định đầy đủ từng trường với các điều kiện ràng buộc của canonical schema.\n"
        "- [1.0 điểm] Đưa ra kết luận rõ ràng (VALID, PASS) và cấu trúc bản ghi canonical hoàn chỉnh."
    ),
    "reference_source": "Pydantic V2 Documentation - Data Validation and Settings Management: https://docs.pydantic.dev/ và Great Expectations - Expect Column Values To Be In Set: https://docs.greatexpectations.io/"
}

# 20. d10-q050
DAY10_PART1["d10-q050"] = {
    "sample_answer": (
        "1. Chọn Disposition cho từng bản ghi A-D:\n"
        "   - Bản ghi A (chỉ thừa khoảng trắng whitespace): DISPOSITION = AUTO-REPAIR / ACCEPT. Hành động: Tự động chạy hàm `strip()` loại bỏ whitespace đầu/cuối và chuẩn hóa khoảng cách giữa các từ, chuyển vào canonical dataset bình thường.\n"
        "   - Bản ghi B (mất required account_id không có nguồn khôi phục): DISPOSITION = REJECT / DROP TO DLQ. Hành động: Loại bỏ khỏi luồng chính, lưu vào Dead Letter Queue vĩnh viễn kèm log lỗi vi phạm khóa bắt buộc.\n"
        "   - Bản ghi C (OCR amount bị mờ nhưng visual gốc còn nguyên): DISPOSITION = QUARANTINE / HUMAN REVIEW. Hành động: Đưa vào hàng đợi duyệt thủ công (HITL), đính kèm file ảnh visual gốc để nhân viên kế toán đối chiếu và nhập lại số tiền chính xác.\n"
        "   - Bản ghi D (optional comment dài hơn soft limit): DISPOSITION = ACCEPT WITH WARNING / TRUNCATE WITH NOTE. Hành động: Cắt ngắn (truncate) theo độ dài cho phép hoặc lưu nguyên vẹn tùy cấu hình, ghi nhận một cảnh báo (warning log) nhưng vẫn cho phép đi tiếp vào pipeline.\n"
        "2. Nêu hệ quả ở tầng sau:\n"
        "   - Tầng Vector Index / RAG Agent: A và D được index an toàn; B không xuất hiện trong hệ thống; C bị hoãn cho đến khi con người phê duyệt xong mới được index bổ sung."
    ),
    "explanation": (
        "Chính sách phân loại bản ghi (Record Disposition Policy) cần phân biệt rạch ròi 4 cấp độ hỏng hóc: (1) Sửa chắc chắn được bằng thuật toán đơn định (whitespace -> auto-clean); (2) Lỗi nghiêm trọng không thể khắc phục (missing primary key -> reject/DLQ); (3) Mất mát thông tin nhưng nguồn gốc còn để phục hồi (OCR mờ -> quarantine review); (4) Lỗi nhẹ không ảnh hưởng toàn vẹn nghiệp vụ (soft limit -> warning pass). Phân loại chính xác giúp tối đa hóa throughput mà không làm giảm chất lượng dữ liệu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Chọn đúng disposition cho cả 4 trường hợp: A auto-repair, B reject/DLQ, C quarantine/human review, D accept with warning.\n"
        "- [1.5 điểm] Phân tích lý do kỹ thuật thuyết phục cho từng lựa chọn dựa trên mức độ nghiêm trọng và khả năng phục hồi.\n"
        "- [1.0 điểm] Trình bày rõ hệ quả đối với các tầng xử lý downstream (chỉ bản ghi sạch mới được index vào phục vụ agent)."
    ),
    "reference_source": "DAMA-DMBOK: Data Quality Management & Exception Handling Rules; Google Cloud Architecture Framework - Data Processing Error Handling"
}

# 21. d10-q052
DAY10_PART1["d10-q052"] = {
    "sample_answer": (
        "1. Thiết kế Schema Quarantine chuẩn mực:\n"
        "   - `quarantine_id`: UUID duy nhất cho sự kiện cách ly.\n"
        "   - `run_id`: Định danh của pipeline run đã phát hiện lỗi.\n"
        "   - `source_system` & `source_file_id`: Nguồn gốc sinh ra dữ liệu.\n"
        "   - `raw_payload`: Toàn bộ dữ liệu thô ban đầu (JSON string / raw bytes) để phục vụ tái hiện.\n"
        "   - `parsed_canonical_partial`: Dữ liệu đã parse một phần trước khi vấp lỗi.\n"
        "   - `failure_code` & `failure_reason`: Mã lỗi (`MISSING_REQUIRED_FIELD`, `INVALID_REGEX`) và thông điệp chi tiết.\n"
        "   - `failed_field`: Tên trường dữ liệu gây ra vi phạm.\n"
        "   - `quarantined_at`: Timestamp thời điểm bản ghi bị chuyển cách ly.\n"
        "   - `status`: Trạng thái xử lý (`PENDING`, `REPLAYED`, `DISCARDED`).\n"
        "2. Thiết kế Replay Guard (Rào chắn an toàn khi chạy lại):\n"
        "   - Điều kiện kiểm chứng tiên quyết: Trước khi replay một bản ghi từ quarantine, hệ thống phải chứng minh 'Điều gì đã thay đổi kể từ lúc lỗi xảy ra' (ví dụ: phiên bản code pipeline đã tăng từ v1.2 lên v1.3 để sửa bug parser, hoặc bản ghi đã được con người cập nhật lại trường thiếu).\n"
        "   - Khóa chống trùng lặp (Idempotency Key): Sử dụng `hash(raw_payload + new_code_version)` để đảm bảo nếu chạy lại mà code chưa sửa hoặc dữ liệu chưa đổi thì sẽ bị từ chối replay ngay lập tức."
    ),
    "explanation": (
        "Một file `dropped_rows.csv` chỉ chứa dữ liệu canonical là một thiết kế 'mù' (blind drop), bởi vì nó đã làm mất thông tin raw gốc, không biết lỗi gì và phát sinh từ run nào, khiến việc debug và replay trở nên bất khả thi. Schema cách ly (Quarantine Schema) phải lưu giữ đầy đủ ngữ cảnh thất bại và bằng chứng nguyên bản. Rào chắn Replay Guard ngăn chặn việc người vận hành chạy lại một cách mù quáng (blind retry) khi các điều kiện gây lỗi chưa hề được khắc phục."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xây dựng schema quarantine đầy đủ các trường thiết yếu: run_id, raw_payload, source_system, failure_code/reason, quarantined_at, status.\n"
        "- [1.5 điểm] Thiết kế cơ chế Replay Guard với điều kiện tiên quyết chứng minh sự thay đổi (code update hoặc data fix).\n"
        "- [1.0 điểm] Đưa ra cơ chế chống lặp (idempotency key / hash) khi replay để ngăn chặn vòng lặp lỗi tái diễn."
    ),
    "reference_source": "Enterprise Integration Patterns - Dead Letter Channel: https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html và Martin Fowler, 'Accounting Patterns' - Audit Log & Reversibility"
}

# 22. d10-q053
DAY10_PART1["d10-q053"] = {
    "sample_answer": (
        "1. Tính toán các chỉ số chất lượng dữ liệu:\n"
        "   - Độ bao phủ bản ghi (Record Coverage Rate / Completeness of Rows):\n"
        "     Tỷ lệ = (Số bản ghi thực tế nhận được) / (Số bản ghi hợp đồng kỳ vọng)\n"
        "     Tỷ lệ = 90 / 100 = 0.90 (90.0%).\n"
        "   - Độ đầy đủ trường email (Email Field Completeness Rate on Received Records):\n"
        "     Tỷ lệ = (Số bản ghi có email hợp lệ trong các bản ghi đã nhận) / (Tổng số bản ghi đã nhận)\n"
        "     Tỷ lệ = 81 / 90 = 0.90 (90.0%).\n"
        "   - Độ đầy đủ trường email toàn diện (Overall Email Completeness against Contract):\n"
        "     Tỷ lệ = 81 / 100 = 0.81 (81.0%).\n"
        "2. Nêu điều chưa được chứng minh (Unproven Aspect):\n"
        "   - Việc trường email có mặt (81 bản ghi) mới chỉ chứng minh 'tính không rỗng' (non-nullness), CHƯA chứng minh được: (a) Tính hợp lệ định dạng cú pháp (valid email regex format - e.g. có chứa ký tự rác hay không); (b) Tính chính xác thực tế (email có tồn tại và thuộc về đúng user đó hay không); (c) Nguyên nhân mất 10 bản ghi đầu nguồn (10 missing records) là do source chưa gửi hay do bị rớt mạng trong quá trình truyền dẫn."
    ),
    "explanation": (
        "Trong kiểm định độ đầy đủ dữ liệu (Completeness Measurement), một sai lầm phổ biến là nhầm lẫn giữa hai mẫu số: (1) Mẫu số theo hợp đồng kỳ vọng (đo lường độ rò rỉ luồng dữ liệu - stream drop) và (2) Mẫu số theo dữ liệu thực nhận (đo lường chất lượng trường trong nội bộ batch). Phải tách biệt rõ ràng độ bao phủ bản ghi (Row Coverage) và độ đầy đủ thuộc tính (Field Completeness). Đồng thời, dữ liệu có mặt không đồng nghĩa với dữ liệu chính xác (presence != correctness)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán chính xác 2 tỷ lệ riêng biệt: Độ bao phủ bản ghi = 90/100 (90%) và Độ đầy đủ email trên bản ghi nhận được = 81/90 (90%).\n"
        "- [1.5 điểm] Nêu rõ sự khác biệt giữa hai mẫu số (mẫu số 100 của hợp đồng vs mẫu số 90 của batch nhận).\n"
        "- [1.0 điểm] Chỉ ra chính xác các điều chưa được chứng minh: tính hợp lệ cú pháp email, tính chính xác thực thể và nguyên nhân thất thoát 10 bản ghi."
    ),
    "reference_source": "ISO/IEC 25012: Data Quality Model - Completeness and Accuracy Dimensions; Great Expectations - Expect Column Values To Not Be Null"
}

# 23. d10-q056
DAY10_PART1["d10-q056"] = {
    "sample_answer": (
        "1. Thiết kế Expectation (Quy tắc kiểm thử tính hợp lệ ngữ nghĩa):\n"
        "   - Không dừng lại ở việc kiểm tra Regex định dạng: Biểu thức chính quy `^\\d{4}-\\d{2}-\\d{2}$` chỉ xác nhận chuỗi có hình dạng ngày, nhưng hoàn toàn bất lực trước các ngày không có thực trên lịch (như 30/02/2026).\n"
        "   - Expectation chuẩn (Semantic Calendar Validation): Sử dụng parser lịch thực thụ (như `datetime.strptime(val, '%Y-%m-%d')` trong Python hoặc `TO_DATE(val, 'YYYY-MM-DD')` với strict mode). Quy tắc này sẽ kích hoạt ngoại lệ `ValueError: day is out of range for month` khi gặp ngày 30 tháng 2 (năm 2026 không nhuận và tháng 2 chỉ có 28 ngày).\n"
        "2. Báo cáo vi phạm (Violation Report Schema):\n"
        "   - `expectation_name`: `expect_column_values_to_be_valid_calendar_date`\n"
        "   - `column`: `event_date`\n"
        "   - `invalid_value`: `'2026-02-30'`\n"
        "   - `violation_type`: `SEMANTIC_INVALID_DATE`\n"
        "   - `error_message`: `Date '2026-02-30' does not exist in Gregorian calendar (February 2026 has only 28 days)`\n"
        "   - `severity`: `ERROR / HARD_GATE`\n"
        "   - `disposition`: Cách ly bản ghi vào Quarantine Queue để rà soát nguồn."
    ),
    "explanation": (
        "Nguyên tắc 'Hình thức hợp lệ không bảo đảm thực tại hợp lệ' (Syntactic Validity != Semantic Validity) là bài học kinh điển trong kỹ nghệ dữ liệu. Một chuỗi ký tự khớp hoàn hảo với cấu trúc regex `YYYY-MM-DD` vẫn có thể biểu diễn một giá trị vô lý trong thế giới thực. Do đó, các bộ kiểm định dữ liệu (Data Quality Suites) bắt buộc phải sử dụng các thư viện kiểm tra ngữ nghĩa chuyên dụng (calendar parsers) và sinh ra báo cáo vi phạm chi tiết phục vụ debug."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Thiết kế expectation chính xác: phân biệt kiểm tra regex hình thức và kiểm tra parser lịch thực thụ (strict calendar date parsing).\n"
        "- [1.5 điểm] Xây dựng cấu trúc báo cáo vi phạm (violation report) đầy đủ: tên cột, giá trị vi phạm, loại lỗi và thông điệp giải thích cụ thể.\n"
        "- [1.0 điểm] Đưa ra giải pháp xử lý bản ghi vi phạm (chặn hard gate, chuyển quarantine)."
    ),
    "reference_source": "Great Expectations - Expect Column Values To Be Dateutil Parseable: https://greatexpectations.io/ và Python `datetime` Standard Library Documentation"
}

# 24. d10-q057
DAY10_PART1["d10-q057"] = {
    "sample_answer": (
        "1. Chọn Khóa Duy Nhất (Uniqueness Key):\n"
        "   - Theo hợp đồng: 'mỗi dòng hàng là duy nhất trong một đơn hàng'. Do đó, khóa duy nhất bắt buộc phải là cặp Composite Key: `(order_id, line_id)`.\n"
        "2. Phân tích các dòng dữ liệu và Tính toán:\n"
        "   - Tập dữ liệu gồm 4 dòng: D1(1, A), D2(1, B), D3(1, A), D4(2, A).\n"
        "   - Nhóm theo Composite Key `(order_id, line_id)`:\n"
        "     + Nhóm `(1, A)`: xuất hiện 2 lần (D1 và D3) -> TRÙNG LẶP.\n"
        "     + Nhóm `(1, B)`: xuất hiện 1 lần (D2) -> Duy nhất.\n"
        "     + Nhóm `(2, A)`: xuất hiện 1 lần (D4) -> Duy nhất (dù cùng line_id='A' nhưng thuộc order_id khác, hoàn toàn hợp lệ theo contract).\n"
        "   - Số nhóm trùng lặp (Duplicate Groups Count): Có đúng 1 nhóm trùng lặp, đó là nhóm khóa `(1, A)`.\n"
        "   - Số dòng dư thừa (Redundant / Duplicate Rows Count): Trong nhóm `(1, A)` có 2 dòng, chỉ giữ lại 1 dòng survivor, do đó có 1 dòng dư thừa cần bị loại bỏ (2 - 1 = 1 dòng dư)."
    ),
    "explanation": (
        "Trong các mô hình dữ liệu quan hệ và bán cấu trúc, một thuộc tính định danh cấp con (như line_id) thường chỉ có ý nghĩa trong phạm vi của một thực thể cha (như order_id). Việc chỉ chọn line_id làm khóa sẽ dẫn đến kết luận sai lầm rằng (1, A) và (2, A) bị trùng. Việc thiết lập đúng Composite Key `(order_id, line_id)` cho phép phân định chính xác số nhóm trùng lặp (1 nhóm) và số bản ghi rác cần khử (1 bản ghi dư thừa), bảo toàn tính toàn vẹn của đơn hàng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Lựa chọn chính xác composite key là (order_id, line_id) theo đúng hợp đồng nghiệp vụ.\n"
        "- [1.5 điểm] Tính toán chính xác số liệu: có đúng 1 nhóm trùng lặp (1, A) và đúng 1 dòng dư thừa cần loại bỏ.\n"
        "- [1.0 điểm] Phân biệt rõ ràng tính hợp lệ của dòng (2, A) so với (1, A) dựa trên phạm vi đơn hàng."
    ),
    "reference_source": "SQL Standards for Primary Key & Composite Constraints; Great Expectations - Expect Compound Columns To Be Unique: https://docs.greatexpectations.io/"
}

print("Loaded Day 10 Part 1 (Questions 1 to 24). Total:", len(DAY10_PART1))
