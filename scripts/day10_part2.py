# scripts/day10_part2.py
# -*- coding: utf-8 -*-
"""
Day 10: Data Pipeline & Observability
Questions 25 to 48 (d10-q059 to d10-q108)
"""

DAY10_PART2 = {}

# 25. d10-q059
DAY10_PART2["d10-q059"] = {
    "sample_answer": (
        "1. Các điểm không nhất quán (Inconsistencies):\n"
        "   - Điểm không nhất quán 1 (Toán học nội bộ - Internal Line Sum Invariant): Tổng các dòng hàng là 50 + 60 = 110 VND, trong khi trường `Order.total` lại ghi nhận 120 VND (chênh lệch 10 VND giữa tổng đơn hàng và tổng chi tiết các mục hàng).\n"
        "   - Điểm không nhất quán 2 (Trạng thái đa hệ thống - Cross-System State Invariant): Hệ thống CRM ghi nhận trạng thái đơn hàng là `paid` (đã thanh toán), nhưng Hệ thống Sổ cái (General Ledger) lại ghi nhận trạng thái là `pending` (đang chờ xử lý).\n"
        "2. Nguồn dùng để giải quyết từng điểm (Authoritative Resolution Source):\n"
        "   - Đối với trạng thái thanh toán: Theo bối cảnh đề bài, 'sổ cái là nguồn có thẩm quyền cho thanh toán' (General Ledger is the Authoritative Source of Truth). Do đó, trạng thái chuẩn xác phải là `pending`. Hệ thống CRM phải được đồng bộ lại theo sổ cái.\n"
        "   - Đối với giá trị tiền đơn hàng: Cần kiểm tra bản ghi gốc của giao dịch hóa đơn/dòng hàng trên cơ sở dữ liệu bán hàng (Order Management System - OMS); nếu không có phí phụ thu/thuế (10 VND), thì tổng chi tiết các dòng (110 VND) hoặc hóa đơn kế toán là căn cứ để điều chỉnh `Order.total`."
    ),
    "explanation": (
        "Trong thiết kế kiểm thử tính nhất quán dữ liệu (Data Consistency Check), kỹ sư cần phân định rõ hai loại bất biến (invariants): Bất biến nội bộ (Intra-record arithmetic invariant) và Bất biến liên hệ thống (Inter-system state invariant). Khi xảy ra xung đột giữa các hệ thống phân tán, việc phân xử bắt buộc phải căn cứ vào 'Nguồn có thẩm quyền được chỉ định' (Designated System of Record / Authoritative Source) thay vì dùng đa số biểu quyết hay phỏng đoán ngẫu nhiên."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Chỉ ra chính xác 2 điểm không nhất quán: chênh lệch số học giữa tổng order (120) và tổng dòng (110), cùng xung đột trạng thái giữa CRM (paid) và Sổ cái (pending).\n"
        "- [1.5 điểm] Xác định đúng nguồn giải quyết trạng thái thanh toán là Sổ cái (Ledger - thẩm quyền tối cao), đưa trạng thái về 'pending'.\n"
        "- [1.0 điểm] Đưa ra phương án đối soát và điều chỉnh trường số tiền dựa trên dữ liệu dòng hàng/hóa đơn gốc."
    ),
    "reference_source": "Martin Kleppmann, Designing Data-Intensive Applications - Consistency Guarantees & Systems of Record; Enterprise Integration Patterns - Canonical Data Model"
}

# 26. d10-q062
DAY10_PART2["d10-q062"] = {
    "sample_answer": (
        "1. Tính đúng thời gian trễ (Data Freshness Latency):\n"
        "   - Thời điểm dữ liệu có hiệu lực tại nguồn: 10:00.\n"
        "   - Thời điểm dữ liệu thực sự được xuất bản tới người dùng/agent (Publish Time): 10:22.\n"
        "   - Thời gian trễ thực tế đối với người dùng (End-to-End Freshness Latency) = 10:22 - 10:00 = 22 phút.\n"
        "   - Lưu ý phân biệt: Thời gian chạy của job (Job Runtime) từ 10:01 đến 10:04 chỉ là 3 phút. Tuy nhiên, dữ liệu nằm chờ từ 10:04 đến 10:22 mới được publish (mất thêm 18 phút ở bước staging/indexing/approval). Do đó, chỉ số 3 phút trên dashboard chỉ là 'Execution Time', hoàn toàn không phải 'Freshness Latency'.\n"
        "2. Phân loại kết quả đối với SLA:\n"
        "   - Ngưỡng cam kết (SLA): Tối đa 10 phút.\n"
        "   - Thực tế: 22 phút > 10 phút.\n"
        "   - Kết luận: VI PHẠM SLA NGHIÊM TRỌNG (SLA Breach / Violated), vượt ngưỡng 12 phút (gấp hơn 2.2 lần giới hạn cho phép)."
    ),
    "explanation": (
        "Sai lầm phổ biến nhất trong việc giám sát độ tươi của dữ liệu (Data Freshness Monitoring) là dùng thời gian thực thi của tác vụ (Job Execution Duration) để thay thế cho độ trễ dữ liệu từ góc nhìn người dùng (End-to-End Freshness). Người dùng dữ liệu hoặc AI Agent chỉ quan tâm: 'Dữ liệu tôi đang đọc cách thời điểm phát sinh thực tế tại thế giới thực bao lâu?'. Đồng hồ độ tươi phải bắt đầu chạy từ khi nguồn có hiệu lực và chỉ dừng lại khi dữ liệu đã xuất bản sẵn sàng để truy vấn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán chính xác thời gian trễ thực tế là 22 phút (10:22 - 10:00), chỉ ra sự khác biệt bản chất so với thời gian chạy job 3 phút.\n"
        "- [1.5 điểm] Phân loại chính xác kết quả là Vi phạm SLA (SLA Breach) vì 22 phút vượt xa ngưỡng cam kết 10 phút.\n"
        "- [1.0 điểm] Phân tích được nguyên nhân chậm trễ nằm ở khoảng thời gian sau khi làm sạch đến khi xuất bản (18 phút delay)."
    ),
    "reference_source": "Google SRE Book - Service Level Objectives (SLOs) & Latency Measurement: https://sre.google/sre-book/service-level-objectives/ và Monte Carlo Data Observability - Freshness Metrics: https://www.montecarlodata.com/"
}

# 27. d10-q064
DAY10_PART2["d10-q064"] = {
    "sample_answer": (
        "1. Phân loại tính chính xác (Classification):\n"
        "   - Trường hợp ngày 15/6 mang giá trị 3 triệu là: KHÔNG CHÍNH XÁC (Inaccurate / Outdated Data).\n"
        "   - Căn cứ: Trang policy có thẩm quyền tối cao (Authoritative Policy Page) quy định hạn mức 5 triệu có hiệu lực từ ngày 01/06. Vì ngày phát sinh sự việc là ngày 15/06 (nằm sau mốc ngày 01/06), chính sách mới 5 triệu đã có hiệu lực bắt buộc thi hành. Giá trị 3 triệu là giá trị của chính sách cũ đã bị thay thế (superseded policy) tồn đọng trong file PDF lưu đệm (cached PDF).\n"
        "2. Giữ lại xung đột phục vụ kiểm toán (Conflict Record Architecture):\n"
        "   - Ghi nhận bản ghi xung đột (Data Conflict Log) lưu trữ: `case_date='2026-06-15'`, `evaluated_value=3000000`, `authoritative_value=5000000`, `authoritative_source='Official Policy Page'`, `conflicting_source='Cached PDF'`, `discrepancy_reason='Stale cache used post-effective date'`.\n"
        "   - Xử lý: Xóa cache PDF cũ, tái lập chỉ mục tìm kiếm với chính sách mới và đưa trường hợp 15/6 vào diện xử lý lại để áp dụng đúng hạn mức 5 triệu."
    ),
    "explanation": (
        "Trong đánh giá chất lượng dữ liệu về khía cạnh Tính chính xác (Accuracy), việc so sánh hai giá trị không thể tách rời khỏi trục thời gian hiệu lực (Effective Date Range) và thứ bậc nguồn thẩm quyền (Source of Truth Hierarchy). Một giá trị từng đúng trong quá khứ sẽ trở thành sai lệch nếu được áp dụng cho một sự kiện xảy ra sau ngày chính sách mới có hiệu lực. Hệ thống phải chủ động phát hiện sự không đồng bộ giữa bộ đệm (cache) và nguồn gốc để ngăn ngừa sai phạm nghiệp vụ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Phân loại chính xác giá trị 3 triệu vào ngày 15/6 là KHÔNG CHÍNH XÁC (Inaccurate).\n"
        "- [1.5 điểm] Lập luận chặt chẽ dựa trên mốc ngày hiệu lực 01/06 của trang policy thẩm quyền tối cao và xác định nguyên nhân do cache PDF bị cũ (stale).\n"
        "- [1.0 điểm] Thiết lập cấu trúc bản ghi lưu vết xung đột (conflict record) đầy đủ thông tin phục vụ kiểm toán và khắc phục."
    ),
    "reference_source": "DAMA-DMBOK: Data Quality Dimensions - Accuracy and Temporal Consistency; ISO 8000-61: Data Quality Management Processes"
}

# 28. d10-q065
DAY10_PART2["d10-q065"] = {
    "sample_answer": (
        "Viết Data Contract vận hành được mà không tự chế tạo ngưỡng giả:\n"
        "```yaml\n"
        "dataset: tickets\n"
        "consumer: sla_assistant_agent\n"
        "contract_version: 1.0.0\n"
        "schema:\n"
        "  - field: ticket_id\n"
        "    type: string\n"
        "    required: true\n"
        "  - field: status\n"
        "    type: string\n"
        "    enum: [open, pending, resolved, closed]\n"
        "  - field: updated_at\n"
        "    type: timestamp_iso\n"
        "    required: true\n"
        "service_level_agreements:\n"
        "  freshness:\n"
        "    metric: current_time - MAX(updated_at)\n"
        "    status: UNCONFIRMED_BY_BUSINESS\n"
        "    target_threshold: TBD_PENDING_BUSINESS_APPROVAL\n"
        "    operational_fallback:\n"
        "      action: log_metric_and_warn_only\n"
        "      hard_gate_blocking: false\n"
        "      escalation_owner: business_ops_lead@company.com\n"
        "      decision_gate_deadline: 2026-05-01\n"
        "```\n"
        "Giải thích cơ chế vận hành: Hợp đồng ghi rõ trường `freshness.status = UNCONFIRMED_BY_BUSINESS`. Trong giai đoạn này, pipeline vẫn đo lường và ghi nhận chỉ số trễ liên tục (telemetry) nhưng không áp dụng hard-block làm sập hệ thống. Việc thiếu ngưỡng được chuyển hóa thành một hạng mục quyết định có người phụ trách (escalation owner) và thời hạn phê duyệt rõ ràng."
    ),
    "explanation": (
        "Một sai lầm nghiêm trọng trong Data Engineering là khi nghiệp vụ chưa đưa ra chỉ số, kỹ sư tự tiện gán một con số tưởng tượng (ví dụ tự điền 15 phút). Điều này dẫn đến false alerts hoặc hiểu lầm tai hại về cam kết chất lượng. Thiết kế Data Contract chuẩn mực cho phép ghi nhận các trường ở trạng thái 'Unconfirmed / TBD' nhưng vẫn vận hành được nhờ cơ chế fallback mềm (warn-only, thu thập baseline dữ liệu thực tế) và gán trách nhiệm giải trình rõ ràng cho đại diện nghiệp vụ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xây dựng Data Contract có cấu trúc đầy đủ, rõ ràng (schema fields, SLAs, SLA status).\n"
        "- [1.5 điểm] Tuyệt đối không tự ý bịa ra con số ngưỡng giả; mô hình hóa trạng thái chưa xác nhận thành trường quản trị rõ ràng (UNCONFIRMED / TBD).\n"
        "- [1.0 điểm] Thiết lập cơ chế vận hành an toàn: chế độ cảnh báo mềm (warn-only), thu thập baseline và chỉ định escalation owner cùng deadline cụ thể."
    ),
    "reference_source": "Data Contracts: Building Production-Ready Data Platforms (Chad Sanderson) và Open Data Contract Standard (ODCS): https://bitol.io/odcs/"
}

# 29. d10-q068
DAY10_PART2["d10-q068"] = {
    "sample_answer": (
        "Kế hoạch nâng cấp Schema Evolution (đổi `dept` -> `department`):\n"
        "1. Versioning & Transition Phase (Giai đoạn chuyển tiếp tương thích ngược):\n"
        "   - Ban hành Schema v2 hỗ trợ đồng thời cả hai trường (Dual-Write / Computed Aliasing). Trong bảng hoặc stream, cột `department` mới được bổ sung, đồng thời trường `dept` cũ vẫn được duy trì dưới dạng view alias hoặc được pipeline tự động sao chép (`department = COALESCE(new.department, old.dept)`).\n"
        "   - Cho phép 3 consumer triển khai nâng cấp theo lịch trình độc lập mà không bị gián đoạn hoạt động.\n"
        "2. Migration & Backfill (Xử lý 2 năm lịch sử):\n"
        "   - Chạy job batch backfill ngoài giờ cao điểm: `UPDATE table SET department = dept WHERE department IS NULL;` cho toàn bộ phân vùng 2 năm lịch sử.\n"
        "   - Kiểm tra tính đầy đủ: Xác nhận 100% dòng trong lịch sử có `department IS NOT NULL`.\n"
        "3. Monitoring (Giám sát chuyển dịch):\n"
        "   - Theo dõi log truy vấn hoặc Kafka metrics để đo lường tỷ lệ các consumer còn gọi trường cũ `dept`.\n"
        "   - Đặt mốc thời gian Deprecation (ví dụ sau 30 ngày) khi mọi consumer đã chuyển sang đọc `department`.\n"
        "4. Rollback Plan (Phương án quay lui):\n"
        "   - Nếu một consumer gặp sự cố sau release, consumer đó rollback về code cũ và vẫn đọc bình thường từ trường `dept` vì trường này chưa hề bị xóa."
    ),
    "explanation": (
        "Đổi tên cột (Column Rename) trong hệ thống phân tán là một 'Breaking Change' nếu thực hiện trực tiếp. Khi các ứng dụng tiêu thụ (consumers) có lịch release độc lập, giải pháp chuẩn mực là áp dụng mẫu hình 'Expand and Contract' (Mở rộng và Co hẹp): (1) Expand: Thêm trường mới, hỗ trợ cả hai; (2) Migrate & Backfill: Cập nhật dữ liệu lịch sử và chuyển đổi dần các consumer; (3) Contract: Chỉ xóa trường cũ sau khi kiểm chứng không còn ai sử dụng. Cách tiếp cận này đảm bảo Zero Downtime và cho phép rollback tức thời."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế giai đoạn tương thích ngược (Expand phase / dual-field / view aliasing) cho phép các consumer deploy lệch lịch.\n"
        "- [1.0 điểm] Xây dựng kế hoạch backfill an toàn cho 2 năm lịch sử và kiểm tra tính toàn vẹn.\n"
        "- [1.0 điểm] Thiết lập cơ chế giám sát lưu lượng sử dụng trường cũ trước khi tiến hành deprecation (Contract phase).\n"
        "- [1.0 điểm] Xây dựng phương án rollback chi tiết, đảm bảo không làm gián đoạn hệ thống."
    ),
    "reference_source": "Martin Fowler, Evolutionary Database Design - Parallel Change / Expand and Contract: https://martinfowler.com/bliki/ParallelChange.html và Confluent Schema Registry Compatibility Rules: https://docs.confluent.io/platform/current/schema-registry/avro.html"
}

# 30. d10-q069
DAY10_PART2["d10-q069"] = {
    "sample_answer": (
        "1. Tính toán Evidence từ dữ liệu thực tế:\n"
        "   - Tổng số bản ghi của lần chạy R7 (Scope Run): N = 1.000 dòng.\n"
        "   - Số bản ghi bị thiếu `source_id`: 25 dòng.\n"
        "   - Số bản ghi có `source_id` hợp lệ (Numerator): 1.000 - 25 = 975 dòng.\n"
        "   - Tỷ lệ thực tế đạt được: Observed Value = 975 / 1.000 = 0.975 (97.5%).\n"
        "   - Ngưỡng kỳ vọng của Hợp đồng dữ liệu (Clause Threshold): Expected Value >= 0.990 (99.0%).\n"
        "2. Kết quả Expectation và Quyết định hệ quả (Consequence Gate):\n"
        "   - Trạng thái kiểm thử: FAILED (Vi phạm ngưỡng chất lượng: 97.5% < 99.0%, thiếu hụt 1.5% tương đương 15 dòng dưới chuẩn).\n"
        "   - Quyết định theo Severity Hard Gate: LẬP TỨC CHẶN PIPELINE (Hard Gate Block / Abort Pipeline). Toàn bộ dữ liệu của Run R7 KHÔNG ĐƯỢC PHÉP xuất bản (no publish) sang bảng serving hoặc vector index của RAG Agent. Đẩy toàn bộ batch hoặc 25 dòng lỗi vào Quarantine, phát tín hiệu P1 Alert cho Data Engineering On-call để xử lý."
    ),
    "explanation": (
        "Một 'Executable Data Expectation' không chỉ dừng lại ở việc tính toán thống kê mà phải gắn liền với một hành động chế tài cụ thể (Automated Enforcement Consequence). Với mức độ nghiêm trọng 'Hard Gate', bất kỳ sự vi phạm ngưỡng nào dù chỉ 1.5% cũng đồng nghĩa với việc toàn bộ lô dữ liệu không đạt tiêu chuẩn chất lượng. Việc tự động chặn xuất bản giúp bảo vệ các mô hình hạ tầng downstream (Agent, Analytics) khỏi việc bị nhiễm độc dữ liệu rác."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán chính xác toàn bộ số liệu: tử số là 975, tỷ lệ thực tế đạt 97.5% so với ngưỡng hợp đồng 99.0%.\n"
        "- [1.5 điểm] Kết luận chính xác trạng thái kiểm thử là FAILED do vi phạm tiêu chuẩn cam kết.\n"
        "- [1.0 điểm] Thực thi đúng hệ quả của Hard Gate: chặn xuất bản dữ liệu run R7, cách ly dữ liệu lỗi và gửi cảnh báo khẩn."
    ),
    "reference_source": "Great Expectations Documentation - Evaluation Engine & Actions: https://docs.greatexpectations.io/ và Great Expectations Hard vs Soft Gates Design Patterns"
}

# 31. d10-q072
DAY10_PART2["d10-q072"] = {
    "sample_answer": (
        "1. Viết kết luận hợp lệ về hiện trạng dữ liệu:\n"
        "   - Kết luận hợp lệ: 'Bộ kiểm thử xác nhận tập dữ liệu 10.000 dòng thỏa mãn hoàn hảo tính toàn vẹn kỹ thuật cục bộ (Syntactic & Structural Integrity): các trường không bị rỗng, đúng kiểu dữ liệu khai báo và đạt tính duy nhất của khóa. TUY NHIÊN, bộ kiểm thử này CHƯA THỂ CHỨNG MINH tính chính xác thực tế (Real-world Semantic Accuracy) và độ tươi của dữ liệu (Data Freshness), do hoàn toàn thiếu đối chiếu với nguồn chân lý và thiếu đồng hồ đo độ trễ.'\n"
        "2. Hai Evidence bổ sung để thu hẹp khoảng trống chất lượng:\n"
        "   - Evidence 1 (Source of Truth Reconciliation Check): Thực hiện đối chiếu mẫu hoặc đối chiếu tổng kiểm (Reconciliation Reconciliation / Hash Diff) giữa dataset hiện tại và cơ sở dữ liệu nguồn gốc (Authoritative DB/CRM), đo lường tỷ lệ sai khác giá trị giữa các trường kinh doanh cốt lõi.\n"
        "   - Evidence 2 (Data Freshness Latency Metric): Thiết lập phép đo thời gian thực tế `NOW() - MAX(source_event_timestamp)` để chứng minh dữ liệu được cập nhật trong khung thời gian cho phép, phát hiện dữ liệu bị ứ đọng do pipeline bị kẹt."
    ),
    "explanation": (
        "Nguyên tắc 'Giới hạn bao phủ của bộ kiểm thử' (Quality Suite Coverage Limits) cảnh báo rằng việc vượt qua 100% các phép kiểm tra cấu trúc cơ bản (Null, Type, Uniqueness) chỉ là điều kiện cần chứ chưa phải điều kiện đủ. Dữ liệu có thể hoàn toàn 'sạch' về mặt cú pháp nhưng lại hoàn toàn 'sai' về mặt ngữ nghĩa (ví dụ: số dư tài khoản đúng format số nguyên nhưng sai số tiền thực tế) hoặc 'cũ rích' do đọc từ snapshot cũ. Cần bổ sung các phép đo khác chiều (Freshness, Ground-truth reconciliation) để đảm bảo chất lượng toàn diện."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Đưa ra kết luận khách quan, chuẩn xác: ghi nhận tính toàn vẹn cú pháp nhưng nêu rõ giới hạn chưa chứng minh được độ chính xác và độ tươi.\n"
        "- [1.5 điểm] Đề xuất Evidence 1 phù hợp: đối soát đối chiếu chéo với Source of Truth (Reconciliation check) để đo lường tính chính xác ngữ nghĩa.\n"
        "- [1.0 điểm] Đề xuất Evidence 2 phù hợp: đo lường độ tươi của dữ liệu (Freshness metric / Watermark latency clock)."
    ),
    "reference_source": "Google Research - 'Data Cascades in High-Stakes AI' (Sambasivan et al., CHI 2021) và Monte Carlo - The 5 Pillars of Data Observability"
}

# 32. d10-q074
DAY10_PART2["d10-q074"] = {
    "sample_answer": (
        "1. Tính toán Precision của Rule hiện tại:\n"
        "   - Tổng số dòng bị chặn bởi rule (Total Blocked / Predicted Positive): 100 dòng.\n"
        "   - Số dòng thực sự bị lỗi (True Positives): 40 dòng.\n"
        "   - Số dòng hợp lệ nhưng bị chặn nhầm (False Positives - tài khoản người phụ thuộc): 60 dòng.\n"
        "   - Precision = True Positives / (True Positives + False Positives) = 40 / 100 = 0.40 (40.0%).\n"
        "2. Hiệu chỉnh Rule (Rule Adjustment):\n"
        "   - Phân tích: Điểm chung của các ca bị chặn nhầm là chúng có trường phân loại tài khoản là người phụ thuộc (account_type = 'dependent').\n"
        "   - Rule mới chuẩn hóa: `IF (age < 18 AND account_type != 'dependent') THEN BLOCK;`\n"
        "3. Lựa chọn hệ quả (Consequence):\n"
        "   - Đối với 60 dòng người phụ thuộc: Mở khóa giải phóng khỏi quarantine, đưa vào canonical phục vụ agent bình thường.\n"
        "   - Đối với 40 dòng lỗi thực sự: Tiếp tục duy trì trạng thái block, chuyển vào DLQ kèm thông báo lỗi cụ thể để bộ phận CSKH liên hệ cập nhật."
    ),
    "explanation": (
        "Một luật kiểm định dữ liệu có Precision thấp (chỉ 40%) sẽ gây ra tỷ lệ báo động giả (False Positive) cao, trực tiếp làm tắc nghẽn luồng vận hành kinh doanh (chặn oan 60 khách hàng hợp lệ). Khi điều tra các ca false positive, kỹ sư dữ liệu phải tìm ra thuộc tính phân nhóm chung (ở đây là account_type='dependent') để tinh chỉnh điều kiện của luật, nâng Precision lên 100% trong khi vẫn giữ vững khả năng ngăn chặn các lỗi thực sự."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán chính xác độ chuẩn xác Precision = 40 / 100 = 40.0%.\n"
        "- [1.5 điểm] Nhận diện đúng đặc điểm chung của false positives và viết lại rule chính xác (kết hợp điều kiện loại trừ account_type='dependent').\n"
        "- [1.0 điểm] Nêu rõ hệ quả xử lý cho 2 nhóm: giải phóng 60 tài khoản người phụ thuộc và giữ chặn 40 lỗi thật."
    ),
    "reference_source": "Google SRE Book - Eliminating Alert Fatigue & Tuning Alert Rules: https://sre.google/sre-book/monitoring-distributed-systems/ và Machine Learning Evaluation Metrics (Precision/Recall in Anomaly Detection)"
}

# 33. d10-q076
DAY10_PART2["d10-q076"] = {
    "sample_answer": (
        "1. Tính toán và diễn giải các chỉ số (Signals) tại thời điểm hiện tại (10:30):\n"
        "   - Source Freshness (Độ tươi đầu nguồn): 10:30 - 10:00 = 30 phút. Nguồn đã không có dữ liệu mới trong 30 phút qua.\n"
        "   - Schedule Execution Lag: Chu kỳ chạy là 5 phút. Lần chạy thành công gần nhất là 10:05 (xuất bản 10:06). Từ 10:06 đến 10:30 là 24 phút, tương đương đã bỏ lỡ hoặc thất bại gần 5 chu kỳ chạy (chỉ số cảnh báo pipeline bị treo/stalled).\n"
        "   - Consumer Freshness Lag (Độ tươi thực tế người dùng nhìn thấy): Dữ liệu mà người dùng thực sự truy vấn được chỉ cập nhật đến mốc `watermark = 09:00`. Do đó: Consumer Latency = 10:30 - 09:00 = 1 giờ 30 phút (90 phút). Mặc dù có dữ liệu nguồn lúc 10:00 và job chạy lúc 10:05, watermark không tiến lên chứng tỏ job chạy nhưng không consume dữ liệu mới.\n"
        "2. Nêu điều chưa xác định (Unconfirmed / Unknowns):\n"
        "   - Chưa xác định được nguyên nhân vì sao Watermark bị kẹt ở 09:00 (do upstream ngừng sinh transaction, do lỗi phân quyền kết nối, hay do worker gặp poison pill khiến offset commit bị block);\n"
        "   - Chưa xác định được trạng thái của các lần chạy từ 10:06 đến 10:30 (job bị crash silently hay scheduler cron bị chết)."
    ),
    "explanation": (
        "Quan sát độ tươi của dữ liệu (Data Freshness Observability) đòi hỏi phải phân tích đa chiều: (1) Trạng thái đầu nguồn (Source timestamp); (2) Trạng thái lịch trình (Scheduler execution); (3) Mốc tiến trình thực tế được commit (Consumer Watermark). Sự chênh lệch giữa thời điểm chạy (10:05) và Watermark (09:00) là tín hiệu điển hình của việc pipeline chạy 'rỗng' (empty run) hoặc lỗi commit, khiến người dùng phải tiêu thụ dữ liệu cũ hơn 1.5 giờ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán đầy đủ và chính xác các khoảng thời gian: Source freshness 30 phút, Pipeline execution delay 24 phút, và Consumer freshness lag thực tế là 90 phút (10:30 - 09:00).\n"
        "- [1.5 điểm] Diễn giải chính xác ý nghĩa các tín hiệu: scheduler bị gián đoạn và watermark bị treo không tiến lên.\n"
        "- [1.0 điểm] Chỉ ra đúng các yếu tố chưa xác định cần điều tra thêm (nguyên nhân kẹt watermark và tình trạng scheduler)."
    ),
    "reference_source": "Tyler Akidau, Streaming Systems - Watermarks and Processing Time vs Event Time; Datadog - Monitoring Data Pipeline Freshness"
}

# 34. d10-q078
DAY10_PART2["d10-q078"] = {
    "sample_answer": (
        "1. Xác định vị trí sụt giảm số lượng và Định lượng (Quantification):\n"
        "   - Stage 1 (Source -> Ingest): 10.200 -> 10.180 (Sụt giảm 20 dòng, tương đương 0.20% - hao hụt mạng/batch boundary bình thường).\n"
        "   - Stage 2 (Ingest -> Clean): 10.180 -> 8.100 (SỤT GIẢM ĐỘT BIẾN: MẤT 2.080 DÒNG, tương đương giảm 20.43%). Đây là vị trí sụt giảm số lượng bất thường lớn nhất trong toàn bộ đường ống.\n"
        "   - Stage 3 (Clean -> Publish vs Quarantine): 8.100 bản ghi sau clean, trong đó 50 dòng vào Quarantine và 8.050 dòng được Publish (8.050 + 50 = 8.100 -> Hoàn toàn khớp số học 100%).\n"
        "   - Tổng kết: Điểm rơi rụng dữ liệu nghiêm trọng nằm tại Bước Chuyển Ingest -> Clean (thất thoát 2.080 bản ghi).\n"
        "2. Evidence cần xem tiếp để điều tra:\n"
        "   - Filter / Drop Log của cleaning pipeline: Kiểm tra các câu lệnh `WHERE`, regex filter hoặc inner join trong mã nguồn làm sạch để xem rule nào đã loại bỏ 2.080 dòng này mà không đưa vào Quarantine;\n"
        "   - Phân tích phân phối của 2.080 dòng bị mất: Đối chiếu diff giữa Ingest dataset và Clean dataset xem các dòng bị mất có chung thuộc tính nào (ví dụ: null trường tùy chọn, sai định dạng ngày, hoặc lỗi parse encoding)."
    ),
    "explanation": (
        "Quan sát dung lượng dữ liệu (Data Volume Observability) phải được thực hiện bằng cách đo đếm Delta (chênh lệch) giữa từng cặp công đoạn liên tiếp (Stage-to-Stage Volume Accounting). Khi một stage làm mất một lượng lớn dữ liệu (hơn 20%) mà số lượng đó không xuất hiện trong bảng cách ly (Quarantine table chỉ có 50 dòng), đây là dấu hiệu của một 'Silent Filter Drop' (bị lọc âm thầm do code lỗi) vi phạm nguyên tắc bảo toàn dữ liệu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Tính toán chính xác delta qua từng stage và định vị chính xác vị trí sụt giảm đột biến là Ingest -> Clean (mất 2.080 dòng, ~20.4%).\n"
        "- [1.5 điểm] Nhận diện việc 2.080 dòng biến mất mà không vào Quarantine (chỉ có 50 dòng) là lỗi lọc âm thầm (silent drop).\n"
        "- [1.0 điểm] Nêu rõ các bằng chứng cụ thể cần kiểm tra tiếp: filter logs, inner join conditions và phân tích diff giữa hai tập dữ liệu."
    ),
    "reference_source": "Monte Carlo - Volume Anomaly Detection in Data Pipelines: https://www.montecarlodata.com/ và Google Cloud Data Loss Prevention Standards"
}

# 35. d10-q081
DAY10_PART2["d10-q081"] = {
    "sample_answer": (
        "1. Diễn giải sự thay đổi phân phối dữ liệu (Distribution Shift):\n"
        "   - Độ dài văn bản: Trung vị sụt giảm nghiêm trọng từ 800 ký tự xuống còn 70 ký tự (giảm hơn 91% độ dài, văn bản bị ngắn bất thường).\n"
        "   - Tỷ lệ Null: Tăng nhẹ từ 1% lên 2% (trong giới hạn biến động nhỏ).\n"
        "   - Phân bố ngôn ngữ: Tỷ lệ tiếng Việt sụt giảm mạnh từ 95% xuống 40%, trong khi tỷ lệ 'không rõ ngôn ngữ' (unknown language) tăng vọt từ ~4% lên 55%.\n"
        "   - Kết luận hiện tượng: Dữ liệu văn bản đầu vào đang bị cụt lủn (truncated) hoặc bị lỗi giải mã/OCR khiến bộ phân loại ngôn ngữ không nhận diện được tiếng Việt, dẫn đến bị gán nhãn unknown.\n"
        "2. Lựa chọn hành động thận trọng (Action without Overreaching):\n"
        "   - Hành động 1 (Tạm đình chỉ xuất bản): Chặn việc đưa batch dữ liệu này vào pipeline tạo embedding cho Vector Database của RAG Agent để ngăn ô nhiễm kiến thức.\n"
        "   - Hành động 2 (Lấy mẫu điều tra thực tế): Trích xuất ngẫu nhiên 50 bản ghi thuộc nhóm 'unknown language, median length 70' để kiểm tra trực quan: xem tài liệu bị cắt cụt do parser hay do văn bản bị lỗi font (mojibake) hay do nguồn cung cấp thay đổi loại tài liệu.\n"
        "   - Tuyệt đối không vội vàng phỏng đoán nguyên nhân hoặc tự ý sửa đổi tham số mô hình phân loại ngôn ngữ khi chưa có bằng chứng thực tế."
    ),
    "explanation": (
        "Quan sát phân phối dữ liệu (Data Distribution Observability) yêu cầu kỹ sư tuân thủ kỷ luật 'Mô tả chính xác điều đã thay đổi trước khi đưa ra giả thuyết tại sao'. Sự sụt giảm đồng thời của độ dài văn bản và sự gia tăng nhãn không rõ ngôn ngữ là triệu chứng điển hình của lỗi tiền xử lý (preprocessing/parsing corruption). Việc đình chỉ xuất bản và lấy mẫu điều tra thực nghiệm là hành động chuẩn mực để kiểm soát rủi ro mà không can thiệp vội vàng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Diễn giải chính xác và khách quan các thay đổi phân phối: sụt giảm 91% độ dài văn bản trung vị và tăng vọt nhãn ngôn ngữ không xác định lên 55%.\n"
        "- [1.5 điểm] Lựa chọn hành động an toàn: tạm dừng xuất bản vào vector search và trích xuất mẫu đại diện để kiểm tra trực quan (visual inspection).\n"
        "- [1.0 điểm] Thể hiện tư duy khoa học, tránh phỏng đoán kết luận quá mức khi chưa có đủ bằng chứng từ việc rà soát mẫu."
    ),
    "reference_source": "Evidently AI - Data Drift and Distribution Monitoring: https://docs.evidentlyai.com/ và Google SRE Book - Monitoring Data Pipelines"
}

# 36. d10-q082
DAY10_PART2["d10-q082"] = {
    "sample_answer": (
        "1. Phân loại các thay đổi trong Schema:\n"
        "   - `customer_id: str`: Giữ nguyên, hoàn toàn tương thích (Compatible).\n"
        "   - `amount: int` -> `amount: string`: ĐÂY LÀ BREAKING CHANGE (Phá vỡ tính tương thích ngược). Kiểu dữ liệu bị đổi từ số nguyên sang chuỗi ký tự.\n"
        "   - `currency?: str`: NON-BREAKING CHANGE (Thay đổi tương thích ngược). Bổ sung trường tùy chọn (optional field) mới.\n"
        "2. Consumer bị ảnh hưởng:\n"
        "   - Consumer thực hiện phép tính 'cộng amount như số' (Aggregation / Financial Consumer) sẽ bị CRASH ngay lập tức với lỗi kiểu dữ liệu (TypeError: unsupported operand type for +: 'str') hoặc tệ hơn là thực hiện phép nối chuỗi ('10' + '20' = '1020' thay vì 30), dẫn đến sai lệch số liệu tài chính nghiêm trọng.\n"
        "3. Hành động cần làm ngay:\n"
        "   - Chặn xuất bản phiên bản Schema v2 dạng string trực tiếp ra kênh chung;\n"
        "   - Nếu cần lưu trữ số lớn hoặc định dạng tiền tệ, triển khai tương thích ngược: Duy trì `amount_numeric: int` cho consumer cũ và cung cấp `amount_str: str` hoặc tạo Database View tự động cast chuỗi về số;\n"
        "   - Cập nhật Consumer Code với cơ chế phòng vệ: ép kiểu an toàn `safe_cast_int(row['amount'])` kèm kiểm tra ngoại lệ trước khi tính toán."
    ),
    "explanation": (
        "Thay đổi kiểu dữ liệu của một trường hiện có từ kiểu số sang chuỗi là một trong những vi phạm tương thích schema (Schema Compatibility Violation) nghiêm trọng nhất. Các consumer dựa vào hợp đồng kiểu số sẽ bị đổ vỡ hoặc tạo ra lỗi sai số học tiềm ẩn (silent mathematical corruption). Quản trị Schema bắt buộc phải sử dụng công cụ như Confluent Schema Registry với chế độ BACKWARD compatibility để tự động chặn các thay đổi phá vỡ này."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Phân loại chính xác các thay đổi: amount đổi sang string là breaking change nguy hiểm; currency là non-breaking change.\n"
        "- [1.5 điểm] Phân tích cụ thể hậu quả đối với consumer thực hiện phép cộng số: crash TypeError hoặc tính sai do nối chuỗi ký tự.\n"
        "- [1.0 điểm] Đưa ra giải pháp khắc phục an toàn: chặn schema v2 trực tiếp, cung cấp trường tương thích ngược hoặc an toàn ép kiểu."
    ),
    "reference_source": "Confluent Schema Registry - Schema Evolution and Compatibility: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html và Apache Avro Specification"
}

# 37. d10-q085
DAY10_PART2["d10-q085"] = {
    "sample_answer": (
        "1. Dựng lại chuỗi Lineage đã biết:\n"
        "   - `Chunk C7` thuộc về `Index I3` (Retrieval Layer);\n"
        "   - `Index I3` có manifest trỏ trực tiếp đến `Canonical dataset K9` (Canonical Layer);\n"
        "   - Nguồn gốc ban đầu là `Source S2` (Source Layer), nhưng S2 lại có hai phiên bản khác nhau (v1 và v2).\n"
        "2. Điểm đứt gãy Lineage đầu tiên (First Broken Link):\n"
        "   - Điểm đứt nằm tại: Liên kết giữa `Canonical K9` và `Source S2`. Nguyên nhân là `K9 thiếu run_id` (và thiếu source_snapshot_id / commit_hash). Khi không có run_id, hoàn toàn không thể xác định K9 được tạo ra từ lần chạy nào, vào thời điểm nào, và bắt nguồn từ phiên bản nào của S2 (S2 v1 hay S2 v2).\n"
        "3. Tác động của điểm đứt gãy (Impact):\n"
        "   - Mất tính bất biến và khả năng truy vết (Traceability Loss): Khi Chunk C7 bị người dùng khiếu nại là sai lệch, đội ngũ kỹ thuật không thể xác định thông tin đó xuất phát từ phiên bản nào của nguồn S2;\n"
        "   - Bất khả thi trong việc tái lập (Replayability Failure): Không thể chạy lại pipeline một cách tin cậy để sửa lỗi vì không biết đầu vào chính xác của K9 là gì."
    ),
    "explanation": (
        "Chuỗi định danh nguồn gốc dữ liệu (Data Lineage Chain) đòi hỏi tính liên tục không đứt đoạn từ Source -> Ingestion Run -> Canonical -> Index -> Chunk. Một khi bất kỳ mắt xích nào bị thiếu thuộc tính neo đậu ngữ cảnh (contextual anchor như `run_id` hay `source_version_hash`), toàn bộ tính khả tín của chuỗi truy vết phía sau sẽ sụp đổ. Dừng lại đúng điểm đứt gãy cho phép khoanh vùng chính xác nơi cần bổ sung metadata quản trị."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Dựng lại đầy đủ và chuẩn xác các mắt xích đã biết trong chuỗi lineage: C7 -> I3 -> K9 và ghi nhận sự tồn tại của S2 v1/v2.\n"
        "- [1.5 điểm] Chỉ ra chính xác điểm đứt gãy đầu tiên nằm tại K9 do thiếu run_id / source provenance trỏ về S2.\n"
        "- [1.0 điểm] Phân tích sâu sắc tác động: mất khả năng truy vết nguồn gốc khi có sự cố và không thể replay đơn định."
    ),
    "reference_source": "OpenLineage Specification - Lineage Metadata & Job Run Context: https://openlineage.io/ và W3C PROV-DM: The PROV Data Model: https://www.w3.org/TR/prov-dm/"
}

# 38. d10-q086
DAY10_PART2["d10-q086"] = {
    "sample_answer": (
        "1. Thiết kế Hai Đồng Hồ Đo Độ Tươi (Two Freshness Clocks):\n"
        "   - Đồng hồ 1 (Live Ticket Status Clock - 2 phút SLA):\n"
        "     + Điểm bắt đầu (T0): Thời điểm sự kiện trạng thái ticket phát sinh tại hệ thống nguồn (Event Timestamp `ticket.status_changed_at`).\n"
        "     + Điểm kết thúc (T1): Thời điểm dữ liệu cập nhật có mặt trong in-memory cache/database mà Agent đọc trực tiếp.\n"
        "     + Độ trễ = `T1 - T0`. Ngưỡng cảnh báo: Cảnh báo mềm khi > 90 giây; Báo động vi phạm SLA khi > 120 giây (2 phút).\n"
        "   - Đồng hồ 2 (Policy PDF Document Clock - 24 giờ SLA):\n"
        "     + Điểm bắt đầu (T0): Thời điểm file policy PDF mới được upload hoặc phê duyệt trên cổng HR/Legal (`policy.effective_or_published_at`).\n"
        "     + Điểm kết thúc (T1): Thời điểm file hoàn tất parse, chunk, embed và Vector Index Alias chuyển sang phục vụ chunk mới.\n"
        "     + Độ trễ = `T1 - T0`. Ngưỡng cảnh báo: Cảnh báo sau 18 giờ; Vi phạm SLA sau 24 giờ.\n"
        "2. Owner nhận Alert:\n"
        "   - Luồng Ticket: Realtime Streaming On-Call / Customer Support Platform Team.\n"
        "   - Luồng Policy PDF: Knowledge Base & RAG Indexing Pipeline Owner.\n"
        "3. Hành vi khi dữ liệu bị cũ (Stale Data Behavior):\n"
        "   - Đối với Ticket: Agent từ chối khẳng định tuyệt đối, phản hồi kèm cảnh báo minh bạch: 'Dữ liệu trạng thái đang cập nhật chậm hơn bình thường, vui lòng kiểm tra trực tiếp trên portal...';\n"
        "   - Đối với Policy: Khi clock vượt 24h mà chưa index bản mới, hệ thống kích hoạt fallback cảnh báo RAG Agent ghi chú nguồn tài liệu đang chờ kiểm duyệt."
    ),
    "explanation": (
        "Thiết kế SLA độ tươi (Freshness SLA Design) cho hệ thống AI Agent phải phản ánh đúng kỳ vọng nghiệp vụ của từng loại dữ liệu: dữ liệu tác nghiệp thời gian thực (Ticket) đòi hỏi phản ứng theo giây, trong khi dữ liệu tri thức tĩnh/bán tĩnh (Policy) vận hành theo chu kỳ ngày. Mỗi đồng hồ phải đo lường trọn vẹn từ lúc sự việc xảy ra ở thế giới thực đến lúc Agent có thể tiếp cận được, kèm theo hành vi phòng vệ chủ động (Graceful Degradation) khi dữ liệu rơi vào trạng thái stale."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Thiết kế chi tiết 2 đồng hồ đo độ tươi với điểm bắt đầu (business event) và điểm kết thúc (agent readable) cùng ngưỡng SLA chuẩn (2 phút cho ticket, 24 giờ cho PDF).\n"
        "- [1.5 điểm] Phân định owner tiếp nhận cảnh báo cụ thể cho từng loại pipeline tương ứng.\n"
        "- [1.0 điểm] Quy định rõ ràng hành vi phản ứng của Agent khi dữ liệu bị stale (cảnh báo người dùng, hạ cấp dịch vụ an toàn)."
    ),
    "reference_source": "Google SRE Workbook - Alerting on SLOs: https://sre.google/workbook/alerting-on-slos/ và Principles of Chaos Engineering - Graceful Degradation"
}

# 39. d10-q089
DAY10_PART2["d10-q089"] = {
    "sample_answer": (
        "1. Diễn giải phương pháp và cửa sổ dữ liệu (Window & Method Assessment):\n"
        "   - Cửa sổ dữ liệu bị lệch quy mô nghiêm trọng: Mốc tham chiếu (baseline window) là 30 ngày (tập dữ liệu lớn, độ ổn định cao), trong khi dữ liệu hiện tại chỉ là 1 ngày (mẫu nhỏ, dễ bị ảnh hưởng bởi biến động ngẫu nhiên - sample variance).\n"
        "   - Chỉ số khoảng cách phân phối: Độ phân kỳ KL Divergence cao ở trường ngôn ngữ chỉ ra sự sai khác phân phối xác suất rất lớn giữa hai tập.\n"
        "2. Đánh giá tín hiệu độc lập cùng thay đổi (Multi-Signal Correlation):\n"
        "   - Không thể coi đây chỉ là biến động ngẫu nhiên trong 1 ngày, bởi vì có hai tín hiệu đo lường độc lập khác CÙNG THAY ĐỔI THEO CHIỀU HƯỚNG XẤU: (a) Tỷ lệ OCR không rõ ngôn ngữ tăng vọt; (b) Grounding rate của Agent sụt giảm mạnh. Sự hội tụ của 3 tín hiệu độc lập này xác nhận hệ thống đang gặp sự cố thực tế nghiêm trọng ở khâu xử lý OCR/tiền xử lý.\n"
        "3. Lựa chọn hành động:\n"
        "   - Lập tức chặn việc tự động nạp dữ liệu của ngày hôm đó vào Vector Store;\n"
        "   - Kiểm tra lại các file PDF và phiên bản OCR model vừa được triển khai trong ngày để tìm nguyên nhân sinh ra văn bản rác;\n"
        "   - Rollback hoặc cách ly các chunk lỗi và đánh giá lại grounding rate sau khi sửa."
    ),
    "explanation": (
        "Khi phân tích độ lệch phân phối (Distribution Drift), nếu chỉ nhìn vào một chỉ số thống kê (như KL Divergence) trên một cửa sổ thời gian ngắn (1 ngày vs 30 ngày), người ta dễ hoài nghi về hiện tượng nhiễu mẫu. Tuy nhiên, nguyên lý 'Đồng quy tín hiệu' (Signal Convergence) chỉ ra rằng: nếu nhiều chỉ số đo lường độc lập từ các tầng khác nhau (Data layer: OCR confidence/language drift; Application layer: RAG grounding rate) cùng đồng thời báo suy thoái, thì đó chắc chắn là một sự cố hệ thống có thật đòi hỏi can thiệp khẩn cấp."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Đánh giá sâu sắc sự chênh lệch quy mô cửa sổ dữ liệu (1 ngày vs 30 ngày) và ý nghĩa của KL Divergence.\n"
        "- [1.5 điểm] Phân tích mối tương quan đồng quy giữa 3 tín hiệu độc lập: KL drift ngôn ngữ, lỗi OCR tăng và grounding rate của RAG sụt giảm.\n"
        "- [1.0 điểm] Đưa ra hành động dứt khoát: chặn nạp dữ liệu, khoanh vùng lỗi ở tầng OCR và bảo vệ chất lượng câu trả lời của agent."
    ),
    "reference_source": "Evidently AI - Drift Detection Methods (KL Divergence, PSI) & Multimodal Evaluation: https://docs.evidentlyai.com/ và Arize Phoenix - LLM Groundedness and Retrieval Evaluation"
}

# 40. d10-q091
DAY10_PART2["d10-q091"] = {
    "sample_answer": (
        "1. Nối chuỗi Evidence nhân quả (Causal Evidence Chain):\n"
        "   - Sự kiện ban đầu: Triển khai phát hành phiên bản mới của bộ phân tích cú pháp (Parser Release).\n"
        "   - Bằng chứng tầng Dữ liệu (Data Pipeline Metric): Tỷ lệ chuỗi văn bản rỗng/null (`null-text`) tăng vọt thêm 20% trong kho tri thức.\n"
        "   - Bằng chứng tầng Truy hồi (Retrieval Metric): Trên cùng tập kiểm định chuẩn 100 câu truy vấn (fixed evaluation benchmark), độ chính xác tìm kiếm `hit@5` sụt giảm nghiêm trọng từ 0.82 xuống 0.60 (giảm 22%).\n"
        "   - Bằng chứng tầng Ứng dụng (Agent Metric): Tỷ lệ câu trả lời có căn cứ tài liệu (`grounded-answer rate`) sụt giảm tương ứng từ 0.78 xuống 0.55 (giảm 23%).\n"
        "2. Phát biểu kết luận đúng mức (Calibrated Conclusion):\n"
        "   - 'Có bằng chứng thực nghiệm mạnh mẽ và nhất quán chứng minh rằng: Việc triển khai parser mới đã trực tiếp làm gia tăng 20% văn bản null trong pipeline dữ liệu, dẫn đến sự suy giảm nghiêm trọng chất lượng truy hồi (hit@5 giảm 22 điểm %), từ đó là nguyên nhân trực tiếp kéo tụt tỷ lệ câu trả lời có căn cứ của Agent xuống 23 điểm % trên tập benchmark 100 queries.'\n"
        "   - Hành động: Lập tức rollback parser về phiên bản trước đó và re-index lại kho dữ liệu."
    ),
    "explanation": (
        "Để chứng minh mối liên kết nhân quả giữa khuyết tật dữ liệu và Service Level Indicator (SLI) của Agent, việc duy trì một tập kiểm thử cố định (Fixed Evaluation Benchmark - 100 queries) là điều kiện tiên quyết nhằm loại bỏ yếu tố biến động từ người dùng. Chuỗi bằng chứng phải thể hiện rõ tính lan truyền từ: Code Change -> Data Quality Failure (null-text) -> Retrieval Failure (hit@5) -> Agent Performance Degradation (groundedness)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xây dựng chuỗi liên kết nhân quả chặt chẽ qua 4 tầng: Parser release -> null-text (+20%) -> hit@5 (0.82 -> 0.60) -> grounded rate (0.78 -> 0.55).\n"
        "- [1.5 điểm] Nhấn mạnh vai trò của việc giữ cố định tập đánh giá 100 queries để bảo đảm tính khoa học của phép đo lường.\n"
        "- [1.0 điểm] Đưa ra kết luận có căn cứ rõ ràng và biện pháp xử lý dứt khoát (rollback parser và re-index)."
    ),
    "reference_source": "RAGAS: Automated Evaluation of Retrieval Augmented Generation: https://docs.ragas.io/ và Google SRE Book - Linking System Metrics to User Experience"
}

# 41. d10-q092
DAY10_PART2["d10-q092"] = {
    "sample_answer": (
        "1. Bố trí vị trí các Quality Gate trong DAG (`parse -> clean -> embed -> publish`):\n"
        "   - Gate 1: 'Required-ID Schema Gate' (Hard Gate) -> Đặt NGAY SAU BƯỚC CLEAN (trước khi vào bước embed: `parse -> clean -> [GATE 1] -> embed`). Lý do: Đây là điểm sớm nhất trong DAG mà toàn bộ các trường canonical đã được hoàn tất chuẩn hóa. Đặt gate tại đây ngăn chặn hoàn toàn việc tiêu tốn chi phí compute đắt đỏ của GPU/Embedding API cho các bản ghi thiếu ID hợp lệ.\n"
        "   - Gate 2: 'Optional-Note Format Gate' (Soft Warning Gate) -> Đặt song song hoặc sau bước clean. Vì trường ghi chú tùy chọn không ảnh hưởng đến khả năng retrieval của vector search, gate này chỉ đóng vai trò audit.\n"
        "2. Xác định các nhánh rẽ khi thất bại (Failure Branches):\n"
        "   - Khi Gate 1 thất bại (Missing Required ID): Nhánh chuyển hướng lập tức: Tách bản ghi vi phạm đẩy vào `Quarantine / Dead Letter Queue` kèm nguyên nhân lỗi; KHÔNG cho phép đi tiếp vào nhánh `embed`. Nhánh chính tiếp tục xử lý các bản ghi hợp lệ còn lại.\n"
        "   - Khi Gate 2 cảnh báo (Optional Note Issue): Bản ghi VẪN ĐƯỢC PHÉP ĐI TIẾP vào nhánh `embed -> publish`, đồng thời ghi một log sự kiện vào bảng `data_quality_warnings` để đội vận hành theo dõi mà không làm gián đoạn pipeline."
    ),
    "explanation": (
        "Nguyên tắc 'Fail-Early / Shift-Left' trong thiết kế DAG dữ liệu quy định rằng: Một phép kiểm tra chất lượng phải được đặt tại điểm sớm nhất có thể mà ở đó các thuộc tính cần kiểm tra đã hội đủ điều kiện để ra quyết định. Việc ngăn chặn các bản ghi hỏng trước công đoạn embedding giúp tiết kiệm chi phí tính toán lớn và bảo vệ tính toàn vẹn của Vector Index. Đồng thời, cần phân biệt rạch ròi giữa Hard Gate (chặn và rẽ nhánh cách ly) và Soft Gate (cảnh báo nhưng cho qua)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Bố trí chính xác vị trí Gate 1 (Required-ID) ngay sau bước clean và trước bước embed, giải thích rõ nguyên lý tiết kiệm compute.\n"
        "- [1.5 điểm] Xác định đúng vị trí và tính chất của Gate 2 (Optional-note) là Soft Warning Gate không cản trở retrieval.\n"
        "- [1.0 điểm] Thiết kế đầy đủ các nhánh xử lý khi fail: cô lập vào Quarantine/DLQ cho Hard Gate và ghi log cảnh báo cho Soft Gate."
    ),
    "reference_source": "Apache Airflow Documentation - Data Quality Gates & Branching: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html và Great Expectations in Pipeline DAGs"
}

# 42. d10-q095
DAY10_PART2["d10-q095"] = {
    "sample_answer": (
        "1. Bảng yêu cầu kỹ thuật đối với Data Orchestrator:\n"
        "| Yêu cầu kỹ thuật | Mô tả chức năng cần thiết |\n"
        "|---|---|\n"
        "| Dependency & Sensor Waiting | Cần cơ chế Sensor/Event-wait thăm dò cho đến khi cả file bên ngoài và DB snapshot sẵn sàng mới kích hoạt DAG. |\n"
        "| Directed Acyclic Graph (DAG) | Quản lý thứ tự thực thi tuần tự có điều kiện: Sensor -> Transform -> Quality Gate -> Publish. |\n"
        "| Automated Retry with Backoff | Tự động thử lại tối đa 2 lần cho các lỗi mạng/timeout tạm thời ở từng task độc lập. |\n"
        "| SLA & Deadline Alerting | Giám sát mốc SLA 07:00; tự động phát cảnh báo nếu pipeline có nguy cơ không hoàn thành trước giờ cam kết. |\n"
        "| Parameterized Backfill Engine | Khả năng chạy lại (backfill) theo dải ngày tùy biến (`start_date` đến `end_date`) một cách độc lập và an toàn. |\n"
        "2. Chỉ ra điểm yếu mà cấu hình chỉ có cron thuần túy không thể biểu diễn được:\n"
        "   - Cron chỉ là một bộ kích hoạt theo thời gian mù quáng (blind time-trigger). Cron KHÔNG THỂ: (a) Biết nguồn dữ liệu đã sẵn sàng hay chưa (kích hoạt bừa bãi khi file chưa về gây crash); (b) Quản lý trạng thái và phụ thuộc giữa các bước (nếu transform fail, cron không biết cách chặn publish); (c) Tự động retry có giới hạn theo từng task; (d) Thực thi backfill theo tham số lịch sử một cách có kiểm soát."
    ),
    "explanation": (
        "Sự khác biệt căn bản giữa một hệ thống điều phối dữ liệu chuyên nghiệp (Data Orchestrator như Apache Airflow, Prefect, Dagster) và công cụ định thời truyền thống (Cron) nằm ở khả năng nhận biết trạng thái phụ thuộc (Stateful Dependency Management). Cron hoàn toàn thiếu nhận thức về dữ liệu (Data-unaware), không thể xử lý việc nguồn bị chậm trễ và không hỗ trợ khôi phục từng phần của DAG khi xảy ra sự cố."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xây dựng đầy đủ bảng yêu cầu kỹ thuật cho Orchestrator đáp ứng đủ: sensor chờ nguồn, quản lý DAG, retry 2 lần, SLA 07:00 và backfill theo date range.\n"
        "- [1.5 điểm] Phân tích sâu sắc các hạn chế cốt tử của Cron thuần: không nhận biết dữ liệu sẵn sàng, không quản lý được task dependency trong DAG.\n"
        "- [1.0 điểm] Nêu rõ các rủi ro vận hành khi chỉ dùng cron (chạy đè, crash do thiếu file, không backfill được)."
    ),
    "reference_source": "Maxime Beauchemin, 'The Rise of the Data Engineer' & Apache Airflow Architecture: https://airflow.apache.org/ và Dagster - Orchestration Design Principles: https://dagster.io/"
}

# 43. d10-q098
DAY10_PART2["d10-q098"] = {
    "sample_answer": (
        "1. Chọn Điểm Chạy Lại (Rerun Point):\n"
        "   - Phân tích: Task C thất bại vì 'lỗi schema invalid có tính xác định' (Deterministic Schema Failure), nguyên nhân do output của Task B vi phạm hợp đồng dữ liệu của C. Task A và B tuy chạy thành công về mặt kỹ thuật (exit code 0) nhưng B đã sinh ra dữ liệu sai chuẩn.\n"
        "   - Quyết định điểm chạy lại: KHÔNG chạy lại từ Task C một cách mù quáng. Điểm chạy lại bắt buộc phải là TỪ TASK B (hoặc sửa code của Task B rồi chạy lại từ B). Nếu logic của B phụ thuộc vào bản chất transform của A thì giữ nguyên output A, chỉ cần sửa và chạy lại B -> C.\n"
        "2. Số lần thử lại (Attempt Count):\n"
        "   - Đối với lỗi mang tính xác định (deterministic error): Số lần tự động thử lại (Automatic Retries) = 0 LẦN. Vì dữ liệu đầu vào đã sai ngữ pháp, việc chạy lại 1.000 lần mà không sửa code/rule thì kết quả vẫn thất bại 1.000 lần, chỉ làm lãng phí tài nguyên tính toán.\n"
        "3. Cách xử lý khi lỗi kết thúc (End-state Handling):\n"
        "   - Lập tức chuyển trạng thái pipeline sang FAILED, phát cảnh báo P2 cho Data Engineer phụ trách Task B;\n"
        "   - Toàn bộ output sai định dạng của Task B bị đưa vào Quarantine, ngăn chặn việc nạp tiếp vào các downstream tasks tiếp theo."
    ),
    "explanation": (
        "Trong kỹ nghệ xử lý lỗi đường ống dữ liệu, nguyên tắc sống còn là 'Phân biệt giữa lỗi tạm thời (Transient Failure) và lỗi đơn định (Deterministic Failure)'. Lỗi tạm thời (như rớt mạng, timeout) thì cần retry có backoff. Ngược lại, lỗi vi phạm schema là lỗi logic có tính tất định: nếu không có sự can thiệp sửa đổi mã nguồn hoặc dữ liệu đầu vào, việc retry chỉ tạo ra lãng phí và nguy cơ làm nghẽn hàng đợi. Phải dừng retry tự động và yêu cầu sửa lỗi tại trạm sinh ra lỗi (Task B)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Xác định chuẩn xác điểm chạy lại phải bắt đầu từ Task B (nơi sinh ra dữ liệu vi phạm contract), không phải chạy lại từ Task C.\n"
        "- [1.5 điểm] Quyết định số lần retry tự động là 0 lần, lập luận thuyết phục dựa trên tính chất lỗi xác định (deterministic failure).\n"
        "- [1.0 điểm] Trình bày quy trình xử lý kết thúc: dừng pipeline, thông báo cho kỹ sư chịu trách nhiệm và cách ly output lỗi."
    ),
    "reference_source": "Google SRE Book - Handling Overload & Transient vs Permanent Errors: https://sre.google/sre-book/addressing-cascading-failures/ và Temporal.io Workflow Failure Handling Guides"
}

# 44. d10-q100
DAY10_PART2["d10-q100"] = {
    "sample_answer": (
        "1. Thiết kế lại Ranh giới Publish Nguyên tử (Atomic Publish Boundary):\n"
        "   - Sai lầm hiện tại: Nạp trực tiếp dữ liệu đang rebuild (600k/1M) vào Live Collection đang phục vụ truy vấn, khiến Agent đọc phải trạng thái 'dữ liệu dở dang' (partial / dirty read anomaly).\n"
        "   - Thiết kế chuẩn (Blue/Green Collection & Alias Pointer Swap):\n"
        "     + Serving Layer luôn truy vấn thông qua một alias logic cố định: `vector_index_active`.\n"
        "     + Quá trình Rebuild 1M vectors được thực hiện hoàn toàn độc lập trên một Collection ẩn / staging mới: `vector_index_v2_staging` (không có user traffic).\n"
        "     + Toàn bộ 1.000.000 vectors được nạp và build chỉ mục (HNSW / IVF-PQ) hoàn tất trên collection mới, sau đó chạy bộ kiểm thử chất lượng (Sanity & Quality Verification Check).\n"
        "     + Khi và chỉ khi 1M vectors đạt 100% chuẩn, thực hiện thao tác chuyển đổi con trỏ nguyên tử (Atomic Alias Swap): Trỏ alias `vector_index_active` từ `v1` sang `v2` trong thời gian mili-giây (Zero Downtime, Zero Partial Read).\n"
        "2. Thiết kế Cơ chế Rollback tức thì:\n"
        "   - Nếu phát hiện lỗi sau khi chuyển đổi, chỉ cần một thao tác lệnh đơn lẻ (Atomic Pointer Switch) trỏ alias `vector_index_active` quay trở lại Collection cũ `v1` (vẫn được lưu giữ nguyên vẹn trong 48 giờ)."
    ),
    "explanation": (
        "Việc cập nhật các tập dữ liệu lớn và chỉ mục tìm kiếm (Vector Indices) bắt buộc phải tuân thủ nguyên lý 'Phân tách giữa Quá trình Xây dựng và Quá trình Xuất bản' (Separation of Build Completion and Serving Activation). Sử dụng mẫu hình Blue/Green với Alias trỏ nguyên tử giúp loại bỏ hoàn toàn hiện tượng người dùng nhìn thấy dữ liệu đang nạp dở dang, đồng thời cung cấp phương án phục hồi thảm họa (instant rollback) với thời gian phục hồi gần như bằng không."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Chỉ rõ nguyên nhân gây lỗi: nạp trực tiếp vào live collection gây ra đọc dữ liệu dở dang (partial read).\n"
        "- [1.5 điểm] Thiết kế giải pháp Blue/Green Indexing hoàn chỉnh: nạp trọn vẹn 1M vectors vào staging collection và chuyển đổi bằng Atomic Alias Swap.\n"
        "- [1.0 điểm] Xây dựng phương án rollback tức thì bằng cách trỏ ngược lại alias về collection ban đầu mà không mất mát dữ liệu."
    ),
    "reference_source": "Qdrant / Milvus Vector Database Documentation - Collection Aliases & Zero-Downtime Reindexing: https://qdrant.tech/documentation/concepts/collections/#collection-aliases và Martin Kleppmann, Designing Data-Intensive Applications"
}

# 45. d10-q101
DAY10_PART2["d10-q101"] = {
    "sample_answer": (
        "1. Thiết kế Bounded Backfill an toàn không phá vỡ Production:\n"
        "   - Phạm vi giới hạn rõ ràng (Bounded Scope): Thiết lập tham số cứng `start_date='2026-04-01'` và `end_date='2026-04-03'` (chính xác 3 ngày thiếu, không quét ngoài phạm vi).\n"
        "   - Tách biệt định danh thực thi (Execution Identity Isolation): Tác vụ backfill phải chạy dưới một `run_id` và worker pool riêng biệt (ví dụ `backfill_20260401_03_run`), được giới hạn tài nguyên (CPU/Memory/IOPS limit) để không tranh chấp hoặc làm cạn kiệt tài nguyên của pipeline trực tiếp đang phục vụ thời gian thực.\n"
        "2. Điểm kết quả trở thành Production (Promotion to Production Boundary):\n"
        "   - Dữ liệu sau khi xử lý được ghi tạm vào vùng đệm staging phân vùng: `staging/partition_date=2026-04-01/`...\n"
        "   - Chạy Data Quality Gate độc lập trên 3 phân vùng này để xác nhận tính toàn vẹn.\n"
        "   - Ghi vào Production bằng thao tác ghi đè phân vùng nguyên tử (Atomic Partition Overwrite): Áp dụng lệnh `INSERT OVERWRITE TABLE ... PARTITION (dt IN ('2026-04-01', '2026-04-02', '2026-04-03'))` trên Apache Iceberg / Delta Lake. Thao tác này chỉ cập nhật metadata catalog của đúng 3 phân vùng thiếu mà không làm khóa hoặc ảnh hưởng đến các phân vùng đang nạp trực tiếp của ngày hôm nay."
    ),
    "explanation": (
        "Thực hiện bù dữ liệu lịch sử (Data Backfilling) trong khi luồng trực tiếp vẫn đang chạy đồng thời tiềm ẩn rủi ro xung đột ghi (Write Conflict) và cạn kiệt tài nguyên hệ thống. Thiết kế an toàn đòi hỏi: (1) Cách ly tài nguyên và định danh thực thi; (2) Giới hạn phạm vi phân vùng nghiêm ngặt; (3) Áp dụng cơ chế cập nhật phân vùng nguyên tử (Atomic Partition Replacement) của các định dạng bảng hiện đại (Delta/Iceberg) để loại bỏ race condition."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Giới hạn chính xác phạm vi backfill (đúng 3 phân vùng 2026-04-01..03) và cách ly định danh/tài nguyên với pipeline production trực tiếp.\n"
        "- [1.5 điểm] Thiết kế cơ chế ghi đè phân vùng nguyên tử (Atomic Partition Overwrite / Swap) trên Delta Lake / Iceberg để tránh xung đột ghi.\n"
        "- [1.0 điểm] Bổ sung quality gate kiểm định trên staging trước khi tích hợp vào serving layer."
    ),
    "reference_source": "Apache Iceberg Documentation - ACID Partition Evolution & Overwrites: https://iceberg.apache.org/ và Databricks Guide on Safe Historical Backfilling"
}

# 46. d10-q105
DAY10_PART2["d10-q105"] = {
    "sample_answer": (
        "1. Lập kế hoạch Timebox 20 phút với Stop Rule cụ thể:\n"
        "   - Phút 0 - 5 (Phân tích Logs nhanh - High-Leverage Check): Kiểm tra ngay các trường có sẵn trong log: `last_success_timestamp`, `processed_row_counts` và `schema_hash`. Mục tiêu: Xác định xem pipeline có chạy hay bị kẹt, số lượng bản ghi có bị rớt về 0 không, và schema có bị đổi không.\n"
        "   - Phút 5: ĐÁNH GIÁ STOP RULE 1 -> Nếu logs cho thấy lần chạy gần nhất fail hoặc `processed_row_counts == 0`, STOP ngay lập tức, không đào sâu thêm, chuyển sang kích hoạt Mitigation.\n"
        "   - Áp dụng Stop Rule với Lineage Query (10 phút): Truy vấn lineage mất tới 10 phút (chiếm 50% tổng thời gian). STOP RULE: LOẠI BỎ / HOÃN TRUY VẤN LINEAGE trong khung 20 phút này! Lý do: Trong tình huống khẩn cấp, nếu kết quả của lineage query không làm thay đổi quyết định giảm thiểu tức thì, thì việc đợi 10 phút là lãng phí thời gian ứng cứu.\n"
        "   - Phút 6 - 15 (Xác nhận Artifact Serving): Kiểm tra xem Index Alias đang trỏ vào snapshot nào.\n"
        "2. Bàn giao Mitigation (Giảm thiểu sự cố lúc phút 15 - 20):\n"
        "   - Thực hiện rollback serving alias về snapshot tốt đã biết trước đó (Known-Good Snapshot);\n"
        "   - Bàn giao cho nhóm Data Platform tiếp tục chạy lineage query ngoại tuyến để phân tích nguyên nhân gốc sau khi hệ thống đã an toàn."
    ),
    "explanation": (
        "Trong xử lý sự cố khẩn cấp (Incident Triage), thời gian là tài nguyên quý giá nhất. Quy tắc vàng của SRE là 'Ưu tiên Giảm thiểu sự cố trước khi Tìm nguyên nhân gốc' (Mitigate first, Root-cause later). Một bước kiểm tra chỉ được phép thực hiện nếu nó mang lại thông tin trực tiếp phục vụ quyết định giảm thiểu rủi ro. Các truy vấn tốn nhiều thời gian (như lineage query 10 phút) phải bị cắt bỏ nếu hệ thống đã có đủ thông tin từ log để thực hiện hành động khắc phục tạm thời."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Phân bổ hợp lý thời gian trong khung 20 phút, ưu tiên kiểm tra nhanh các chỉ số sẵn có trong log (last_success, counts, schema_hash).\n"
        "- [1.5 điểm] Áp dụng đúng Stop Rule loại bỏ việc chạy truy vấn lineage 10 phút vì quá tốn thời gian và không thay đổi quyết định mitigation.\n"
        "- [1.0 điểm] Đưa ra phương án mitigation bàn giao rõ ràng (rollback serving alias về snapshot ổn định trước khi hết giờ)."
    ),
    "reference_source": "Google SRE Book - Emergency Response & Managing Incidents: https://sre.google/sre-book/incident-management/ và PagerDuty Incident Response Documentation"
}

# 47. d10-q106
DAY10_PART2["d10-q106"] = {
    "sample_answer": (
        "1. Chọn Mitigation có thể đảo ngược (Reversible Mitigation):\n"
        "   - Thực hiện chuyển hướng Serving Alias (Atomic Alias Re-point) từ `index_v3` quay trở lại `index_v2`. Dù v2 cũ 1 ngày (stale 1 day), nhưng v2 là 'Known-Good' (dữ liệu chính sách đã được kiểm chứng chuẩn xác), tốt hơn vô cùng việc tiếp tục phục vụ v3 chứa chính sách sai lệch nghiêm trọng cho người dùng.\n"
        "   - Tính chất đảo ngược: Giữ nguyên v3 ở trạng thái offline/quarantine; khi nào root cause được sửa và xác nhận, chỉ cần một lệnh switch alias là có thể chuyển lại mà không làm mất dữ liệu.\n"
        "2. Cách công bố (Incident Communication):\n"
        "   - Thông báo minh bạch cho các bên liên quan và người dùng RAG Agent: 'Hệ thống tri thức hiện đang tạm thời sử dụng bản snapshot chính sách ngày hôm qua để khắc phục sự cố hiển thị. Các cập nhật trong 24 giờ qua đang được rà soát lại và sẽ có thông báo khi hoàn tất'.\n"
        "3. Tiêu chí kết thúc sự cố (Exit Criteria):\n"
        "   - Nguyên nhân gốc của việc sinh ra policy sai trong v3 được xác định, sửa chữa bằng code/rule và vượt qua bộ kiểm thử hồi quy;\n"
        "   - Tạo thành công `index_v4` từ dữ liệu đã sửa, kiểm định đạt 100% độ chính xác;\n"
        "   - Hoàn tất switch alias sang v4 và theo dõi trong 2 giờ không có lỗi phát sinh."
    ),
    "explanation": (
        "Trong quản lý sự cố dữ liệu khi chưa làm rõ nguyên nhân gốc (unclosed root cause), nguyên tắc an toàn cao nhất là 'Lùi về trạng thái ổn định đã biết' (Rollback to Known-Good State). Việc chấp nhận độ trễ thời gian (stale 1 ngày) để đổi lấy tính chính xác tuyệt đối là sự đánh đổi bắt buộc trong các miền nghiệp vụ quan trọng (pháp lý, chính sách). Mọi giải pháp ứng cứu phải có tính khả nghịch (reversible) và đi kèm tiêu chí nghiệm thu nghiêm ngặt trước khi đóng sự cố."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Lựa chọn chính xác mitigation có thể đảo ngược: chuyển serving alias về v2 (known-good), giữ v3 offline để debug.\n"
        "- [1.5 điểm] Xây dựng thông điệp công bố minh bạch và chuẩn mực cho người dùng về việc tạm thời dùng dữ liệu lùi 1 ngày.\n"
        "- [1.0 điểm] Thiết lập đầy đủ tiêu chí kết thúc sự cố: fix root cause, tạo v4 đạt chuẩn, switch alias an toàn và quan sát ổn định."
    ),
    "reference_source": "PagerDuty Incident Response Guides - Rollback and Mitigation Strategies: https://response.pagerduty.com/ và Google SRE Book - Postmortem Culture"
}

# 48. d10-q108
DAY10_PART2["d10-q108"] = {
    "sample_answer": (
        "1. Viết Causal Record (Bản ghi nguyên nhân sự cố):\n"
        "   - Sự kiện sự cố: Parser âm thầm bỏ qua một cột quan trọng sau khi schema phía nguồn đổi tên (Schema Rename Silent Drop Incident).\n"
        "   - Cơ chế phát sinh lỗi: Parser sử dụng cấu hình nới lỏng (lenient / permissive mode) hoặc truy cập thuộc tính bằng cú pháp fallback `dict.get('old_col_name', None)`. Khi cột bị rename, parser nhận `None` mà không báo lỗi, tiếp tục ghi dữ liệu thiếu vào canonical store. Đội ngũ sau đó đã can thiệp sửa tay thủ công các dòng lỗi.\n"
        "   - Điểm yếu quy trình: Sửa tay bằng cơm không tạo ra rào cản ngăn chặn tái diễn; thiếu kiểm thử hồi quy tự động.\n"
        "2. Thiết kế Prevention Control có thể test được (Testable Prevention Control):\n"
        "   - Xây dựng Data Contract Test bắt buộc trong CI/CD và Pipeline Runtime: Triển khai kiểm thử `Strict Schema Validation` bằng Pydantic hoặc Great Expectations (`expect_table_columns_to_match_ordered_set`). Cấm hoàn toàn việc bỏ qua cột bắt buộc.\n"
        "   - Kiểm chứng tính hiệu quả của Control mới: Tạo một Unit/Integration Test đưa chính payload bị lỗi (với tên cột đã rename nhưng chưa cập nhật parser) qua control mới. TIÊU CHÍ BẮT BUỘC: Control mới PHẢI FAIL (báo lỗi SchemaValidationError) ngay lập tức trên chính ca dữ liệu biến dạng này, chứng minh hệ thống không còn bị rơi vào tình trạng âm thầm bỏ sót cột nữa."
    ),
    "explanation": (
        "Một chu trình ngăn ngừa sự cố dữ liệu (Data Incident Prevention Loop) thực sự chỉ hoàn tất khi ta xây dựng được một rào kiểm soát có thể kiểm thử (Testable Control) có khả năng 'bắt được chính kẻ thù cũ'. Việc sửa tay chỉ là giải pháp tình thế (band-aid). Phép kiểm tra tính hiệu quả của cơ chế phòng vệ là: khi đưa trường hợp lỗi lịch sử vào kiểm thử hồi quy, hệ thống bắt buộc phải phát hiện và từ chối xử lý thay vì im lặng cho qua."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Lập bản ghi nguyên nhân (causal record) chỉ rõ cơ chế lỗi do parser nuốt lỗi im lặng (lenient fallback) khi schema rename và chỉ ra sự nguy hiểm của việc chỉ sửa tay.\n"
        "- [1.5 điểm] Thiết kế cơ chế kiểm soát phòng ngừa chặt chẽ (Strict Schema Enforcement / Great Expectations contract).\n"
        "- [1.0 điểm] Chứng minh tính kiểm thử được của control: bắt buộc phải fail trên chính ca biến dạng dữ liệu lịch sử trong bài kiểm thử tự động."
    ),
    "reference_source": "Google SRE Book - Incident Prevention and Postmortem Action Items: https://sre.google/sre-book/postmortem-culture/ và Great Expectations - Schema Validation Rules"
}

print("Loaded Day 10 Part 2 (Questions 25 to 48). Total:", len(DAY10_PART2))
