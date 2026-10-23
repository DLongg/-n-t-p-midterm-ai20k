# scripts/day12_part2_c.py
# -*- coding: utf-8 -*-
"""
Day 12 Part 2 Sub-part C: Questions 61 to 73 (d12-q132 to d12-q159)
"""

DAY12_PART2_C = {}

# 61. d12-q132 (4 pts)
DAY12_PART2_C["d12-q132"] = {
    "sample_answer": (
        "1. Phân loại Trạng thái Hoàn tất (Completion Classification) cho Ba Timeline:\n"
        "   - Timeline A (Timeout xảy ra trước khi kết nối mạng được thiết lập - Connect Timeout):\n"
        "     + Phân loại: CHẮC CHẮN CHƯA HOÀN TẤT (Definitely Not Completed).\n"
        "     + Phân tích: Yêu cầu chưa từng rời khỏi máy khách để tới máy chủ nhà cung cấp (chưa hoàn tất TCP/TLS handshake), không có socket nào được kết nối thành công.\n"
        "   - Timeline B (Nhà cung cấp đã trả biên lai xác nhận - Provider Receipt Received):\n"
        "     + Phân loại: CHẮC CHẮN ĐÃ HOÀN TẤT (Definitely Completed).\n"
        "     + Phân tích: Giao dịch đã được tiếp nhận, xử lý và cam kết thành công phía máy chủ, biên lai giao dịch chính thức đã nằm an toàn tại client.\n"
        "   - Timeline C (Timeout xảy ra sau khi gửi dữ liệu nhưng chưa nhận được phản hồi - Post-Send Unknown Timeout):\n"
        "     + Phân loại: TRẠNG THÁI KHÔNG RÕ RÀNG / LƠ LỬNG (In-Doubt / Indeterminate Completion State).\n"
        "     + Phân tích: Yêu cầu đã được gửi qua mạng nhưng timeout đứt kết nối xảy ra trước khi nhận được phản hồi. Không thể biết máy chủ đích đã commit giao dịch vào cơ sở dữ liệu trước khi đứt mạng hay chưa.\n"
        "2. Đánh giá Mức độ An toàn khi Thử lại (Retry Safety Evaluation):\n"
        "   - Timeline A: AN TOÀN TUYỆT ĐỐI ĐỂ THỬ LẠI (Safe to Retry immediately). Vì nhà cung cấp chưa hề nhận được yêu cầu, việc gửi lại yêu cầu không gây ra bất kỳ tác dụng phụ trùng lặp nào.\n"
        "   - Timeline B: TUYỆT ĐỐI KHÔNG THỬ LẠI THỰC THI (Do Not Re-execute / Unsafe to Retry). Nếu cần xác nhận lại dữ liệu, chỉ thực hiện truy vấn đọc trạng thái (`GET /receipts/{id}`) hoặc gửi lại kèm Idempotency Key để nhận lại receipt cũ, cấm tạo transaction mới.\n"
        "   - Timeline C: NGUY HIỂM NẾU RETRY MÙ QUÁNG - CHỈ ĐƯỢC RETRY KÈM KHÓA LŨY ĐẲNG (Conditional Retry with Idempotency Key Only). Bắt buộc phải gắn cùng một `Idempotency-Key` duy nhất, hoặc gọi API đối soát kiểm tra trạng thái trước khi quyết định thực thi tiếp nhằm tránh bị trừ tiền hoặc tạo đơn hàng hai lần."
    ),
    "explanation": (
        "Trong mạng phân tán, sự cố Timeout không đồng nghĩa với Thất bại (Timeout does not mean Failure). Việc phân biệt chính xác thời điểm xảy ra timeout (trước khi kết nối hay sau khi phát dữ liệu) là nền tảng để thiết lập chiến lược thử lại an toàn, ngăn ngừa triệt để các thảm họa trùng lặp tác vụ ngoài ý muốn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân loại chuẩn xác trạng thái hoàn tất cho cả 3 timeline: A chưa hoàn tất, B chắc chắn hoàn tất, C lơ lửng không rõ.\n"
        "- [1.5 điểm] Đánh giá retry safety cho Timeline A (an toàn tuyệt đối) và Timeline B (cấm retry thực thi tạo mới).\n"
        "- [1.5 điểm] Đánh giá retry safety cho Timeline C: Nguy hiểm nếu retry mù quáng, bắt buộc dùng Idempotency Key hoặc API đối soát."
    ),
    "reference_source": "Designing Data-Intensive Applications (Martin Kleppmann) - Unreliable Networks & Idempotent Message Processing Patterns"
}

# 62. d12-q135 (4 pts)
DAY12_PART2_C["d12-q135"] = {
    "sample_answer": (
        "1. Theo dõi Lần Thực thi Đầu tiên (First Attempt Execution & Atomic Commit):\n"
        "   - Khi Attempt 1 đến với ý định nghiệp vụ và `Idempotency-Key: K`:\n"
        "   - Hệ thống tra cứu bảng lưu trữ khóa lũy đẳng (`idempotency_store`) trong cơ sở dữ liệu. Không tìm thấy khóa `K`.\n"
        "   - Hệ thống mở một DB Transaction nguyên tử (Atomic Unit of Work):\n"
        "     + Thực thi tác động nghiệp vụ (State Effect): Tạo bản ghi đơn hàng mới, cập nhật số dư tài khoản.\n"
        "     + Ghi nhận bản ghi kết quả vào bảng idempotency:\n"
        "       `INSERT INTO idempotency_records (key, status, response_body, payload_hash) VALUES ('K', 'COMMITTED', '{\"order_id\": \"ORD-999\", \"status\": \"success\"}', 'hash_sha256')`.\n"
        "     + Commit Transaction thành công 100% vào cơ sở dữ liệu.\n"
        "   - Sự cố xảy ra: Kết nối mạng bị ngắt đột ngột ngay sau khi commit, khiến phản hồi mạng (HTTP 200) bị mất trên đường truyền và client không nhận được.\n"
        "2. Theo dõi Các Lần Phát lại Tiếp theo (Subsequent Replay Attempts):\n"
        "   - Client gặp timeout và gửi lại Attempt 2, sau đó là Attempt 3 với cùng `Idempotency-Key: K` và cùng payload:\n"
        "   - Khi Attempt 2 và Attempt 3 đến máy chủ:\n"
        "     + Hệ thống kiểm tra `idempotency_store` và tìm thấy ngay khóa `K` với trạng thái `COMMITTED`.\n"
        "     + Kiểm tra tính toàn vẹn: Đối chiếu `payload_hash` của request mới với hash đã lưu để bảo đảm cùng ý định nghiệp vụ.\n"
        "     + Cơ chế Phát lại (Idempotent Replay): Hệ thống TUYỆT ĐỐI KHÔNG CHẠY LẠI BẤT KỲ LOGIC NGHIỆP VỤ NÀO (Không tạo đơn hàng mới, không trừ tiền lần 2). Hệ thống đọc trực tiếp `response_body` đã lưu và gửi trả lại cho client kèm header `Idempotent-Replayed: true`.\n"
        "     + Kết quả: Cả 3 attempt đều nhận được cùng một kết quả nhất quán, trong khi tác động thực tế ở phía hạ nguồn chỉ xảy ra duy nhất đúng 1 lần (Exactly-Once Effect)."
    ),
    "explanation": (
        "Xử lý lũy đẳng hai pha (Idempotency Record & Replay Pattern) bảo đảm rằng ngay cả khi các gói tin phản hồi bị mất trên đường truyền dẫn đến việc client gửi lại nhiều lần, trạng thái hệ thống vẫn hoàn toàn bất biến sau lần thực thi nguyên tử đầu tiên. Các yêu cầu đến sau chỉ đóng vai trò kích hoạt việc đọc lại kết quả đã lưu mà không bao giờ tái sinh tác dụng phụ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Mô tả chính xác lần thực thi đầu tiên: Tạo state effect và lưu kết quả nguyên tử trong cùng một DB transaction trước khi mất mạng.\n"
        "- [1.5 điểm] Theo dõi cơ chế xử lý khi Attempt 2 và 3 đến: Kiểm tra khóa K, đối chiếu payload hash và phát hiện trạng thái COMMITTED.\n"
        "- [1.5 điểm] Khẳng định hành vi Replay: Trả về kết quả cũ kèm header replay, cam kết tác động thực tế chỉ diễn ra đúng 1 lần duy nhất."
    ),
    "reference_source": "Stripe Engineering Blog - Designing robust and predictable APIs with idempotency: https://stripe.com/blog/idempotency và IETF Draft: The Idempotency-Key HTTP Header Field"
}

# 63. d12-q137 (4 pts)
DAY12_PART2_C["d12-q137"] = {
    "sample_answer": (
        "1. Phân loại Bốn Yêu cầu R1 - R4 theo Ý định Nghiệp vụ (Business Intent Classification):\n"
        "   - Cặp R1 và R2: CÙNG MỘT Ý ĐỊNH NGHIỆP VỤ (SAME INTENT).\n"
        "     + Phân tích: Cả hai yêu cầu đều áp dụng trên cùng đơn hàng O7, cùng người ủy quyền hợp pháp (Same Authority), và cùng mục đích hoàn trả 100% toàn bộ giá trị đơn hàng (Full Refund). Sự khác biệt câu chữ giữa 'hoàn tiền toàn bộ' và 'hoàn toàn bộ đơn' chỉ là biến thể ngôn ngữ tự nhiên, bản chất nghiệp vụ hoàn toàn đồng nhất.\n"
        "   - Yêu cầu R3: Ý ĐỊNH KHÁC BIỆT HOÀN TOÀN (DIFFERENT INTENT).\n"
        "     + Phân tích: R3 yêu cầu 'hoàn tiền 20%' (Partial Refund). Đây là một hành động tài chính với số tiền hoàn toàn khác biệt so với việc hoàn tiền toàn bộ 100% của R1/R2.\n"
        "   - Yêu cầu R4: Ý ĐỊNH MƠ HỒ / CHƯA XÁC ĐỊNH (AMBIGUOUS / UNCONFIRMED INTENT).\n"
        "     + Phân tích: R4 chỉ ghi 'hoàn tiền như cũ' nhưng không có bất kỳ ý định hoặc giao dịch nào trước đó đã được hệ thống xác nhận thành công. Không thể tự suy diễn R4 thuộc nhóm toàn bộ hay một phần mà không có căn cứ đối soát.\n"
        "2. Thiết kế Cách Sử dụng Identity và Quản lý Khóa Lũy đẳng:\n"
        "   - Quy tắc Ánh xạ Khóa Định danh (Idempotency Key Synthesis):\n"
        "     + Đối với R1 và R2: Chuẩn hóa ý định thành một Khóa Định danh Doanh nghiệp Duy nhất (Canonical Business Key): `idempotency:order:O7:refund_full`. Khi R1 được xử lý, khóa được ghi nhận. Khi R2 đến, hệ thống nhận diện cùng Intent Key và trả về kết quả replay của R1 mà không thực hiện hoàn tiền lần 2.\n"
        "     + Đối với R3: Cấp phát một Khóa Định danh riêng biệt: `idempotency:order:O7:refund_partial_20`. Cho phép thực thi độc lập (hoặc từ chối hợp lệ nếu đơn hàng đã được R1 hoàn tất 100%).\n"
        "     + Đối với R4: BẮT BUỘC TỪ CHỐI TIẾP NHẬN (Reject with HTTP 422 Unprocessable Entity). Yêu cầu client cung cấp mã giao dịch tham chiếu rõ ràng (`referenced_intent_id`) hoặc số tiền cụ thể trước khi cấp phát Identity."
    ),
    "explanation": (
        "Xử lý ngôn ngữ tự nhiên trong các hệ thống Agent giao dịch đòi hỏi phải phân tách giữa lớp ngữ nghĩa văn bản và lớp định danh nghiệp vụ. Bằng việc chuẩn hóa các văn bản có cùng ý nghĩa thành một khóa định danh doanh nghiệp duy nhất và từ chối các câu lệnh mơ hồ, hệ thống bảo vệ toàn vẹn sổ cái tài chính và ngăn ngừa thất thoát kinh tế."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân loại chính xác: R1 và R2 cùng intent (hoàn 100%), R3 là intent khác biệt (hoàn 20%), R4 là intent chưa xác định.\n"
        "- [1.5 điểm] Thiết kế khóa định danh Canonical Business Key gộp R1 và R2 chống trùng lặp hoàn tiền, và cấp key riêng cho R3.\n"
        "- [1.5 điểm] Xử lý an toàn cho R4: Từ chối tiếp nhận (HTTP 422) do ý định mơ hồ và yêu cầu client bổ sung tham chiếu rõ ràng."
    ),
    "reference_source": "Enterprise Integration Patterns - Canonical Data Model & Martin Fowler - Event Sourcing and Intent-based APIs"
}

# 64. d12-q139 (4 pts)
DAY12_PART2_C["d12-q139"] = {
    "sample_answer": (
        "1. Theo dõi Phần Việc Đã ghi và Chưa ghi trong Sổ Nhật ký (Journal Logging State):\n"
        "   - Phần việc Đã ghi vào Nhật ký (Committed Journal Record):\n"
        "     + Bản ghi bắt đầu gọi công cụ: `JOURNAL_RECORD { event: 'TOOL_INVOCATION_START', tool_name: 'T', idempotency_key: 'IDEM-T-777', timestamp: '...' }` đã được ghi đĩa bền vững trước khi phát request mạng.\n"
        "   - Phần việc Chưa ghi vào Nhật ký (Uncommitted / Missing Record):\n"
        "     + Bản ghi hoàn tất: `TOOL_INVOCATION_SUCCESS` kèm kết quả trả về của Provider CHƯA ĐƯỢC COMMIT vào nhật ký đĩa cứng do tiến trình bị crash đột ngột ở khoảng cách giữa thời điểm nhận phản hồi mạng và thao tác ghi đĩa.\n"
        "2. Theo dõi Tác động Bên ngoài và Quy trình Đối soát Phục hồi (External Effect Reconciliation):\n"
        "   - Đánh giá Tác động Bên ngoài (External Effect):\n"
        "     Nhà cung cấp bên ngoài (External Provider) có thể ĐÃ THỰC THI THÀNH CÔNG tác vụ (ví dụ: đã gửi tin nhắn SMS, đã tạo bản ghi trên Salesforce, hoặc đã trừ tiền thẻ tín dụng).\n"
        "   - Quy trình Phục hồi sau Khởi động lại (Crash Recovery Protocol):\n"
        "     + Bước 1: Khi tiến trình khởi động lại, công cụ phục hồi đọc Journal và phát hiện tác vụ Tool T đang ở trạng thái treo (`IN_PROGRESS / PENDING`).\n"
        "     + Bước 2 (Nguyên tắc Cốt tử): TUYỆT ĐỐI KHÔNG GỌI LẠI TOOL T NGAY LẬP TỨC vì sẽ gây trùng lặp tác động bên ngoài (Double External Effect).\n"
        "     + Bước 3 (Thực hiện Truy vấn Đối soát): Gửi một yêu cầu kiểm tra trạng thái (Status Check / Reconciliation Query) tới Provider sử dụng `idempotency_key: 'IDEM-T-777'`.\n"
        "     + Bước 4 (Xử lý Kết quả Đối soát):\n"
        "       * Nếu Provider xác nhận tác vụ ĐÃ HOÀN TẤT: Kéo kết quả về, ghi bù bản ghi `TOOL_INVOCATION_SUCCESS` vào Journal và cho phép workflow tiếp tục bước sau.\n"
        "       * Nếu Provider xác nhận CHƯA NHẬN ĐƯỢC yêu cầu: Thực hiện gọi lại Tool T an toàn với cùng khóa `idempotency_key`."
    ),
    "explanation": (
        "Vấn đề crash giữa chừng (Crash-Fault Tolerance) là thách thức kinh điển trong kiến trúc giao tác phân tán. Quy trình ghi nhật ký trước (Write-Ahead Logging) kết hợp với cơ chế đối soát trạng thái qua khóa lũy đẳng bảo đảm rằng hệ thống luôn có thể khôi phục trạng thái nhất quán và không bao giờ thực hiện lặp lại một hành động đã diễn ra trong thế giới thực."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân định chính xác: Phần đã ghi là bước bắt đầu gọi Tool T; phần chưa ghi là kết quả trả về và bước hoàn tất.\n"
        "- [1.5 điểm] Phân tích tác động bên ngoài: Provider có thể đã hoàn tất hành động trong thực tế trước khi client crash.\n"
        "- [1.5 điểm] Thiết kế quy trình phục hồi đúng đắn: Cấm gọi lại ngay, thực hiện truy vấn đối soát qua Idempotency Key trước khi commit bù."
    ),
    "reference_source": "Database Recovery Techniques - Write-Ahead Logging (WAL) & Temporal.io Architecture - Durable Execution and Crash Recovery"
}

# 65. d12-q141 (4 pts)
DAY12_PART2_C["d12-q141"] = {
    "sample_answer": (
        "1. So sánh Độ mịn của Hai Mô hình Điểm kiểm tra (Granularity Comparison):\n"
        "   - Mô hình 1: Điểm Kiểm tra Cấp Node (Coarse-Grained Node-Level Checkpointing):\n"
        "     + Điểm lưu trạng thái: Chỉ lưu trữ trạng thái sau khi toàn bộ một Node hoàn tất thành công.\n"
        "     + Trạng thái sau sự cố: Node A đã hoàn tất và có checkpoint. Node B chứa 2 cuộc gọi con (Call 1 và Call 2). Khi tiến trình sập sau Call 1, hệ thống KHÔNG CÓ BẤT KỲ ĐIỂM KIỂM TRA NÀO ghi nhận Call 1 đã chạy.\n"
        "     + Hành vi khi phục hồi: Hệ thống bắt buộc phải ROLLBACK VỀ CHECKPOINT CỦA NODE A VÀ CHẠY LẠI TOÀN BỘ NODE B TỪ ĐẦU. Do đó, Call 1 sẽ BỊ GỌI LẠI LẦN THỨ HAI. Nếu Call 1 có tác dụng phụ ngoài (như gửi email hoặc trừ phí), nó sẽ gây ra sự cố lặp tác động nghiêm trọng và lãng phí chi phí token.\n"
        "   - Mô hình 2: Sổ Nhật ký Cấp Cuộc gọi (Fine-Grained Call-Level Journaling / Event Sourcing):\n"
        "     + Điểm lưu trạng thái: Mỗi cuộc gọi riêng lẻ bên trong Node (Call 1, Call 2) đều được ghi nhận nguyên tử vào Journal ngay khi có kết quả.\n"
        "     + Trạng thái sau sự cố: Kết quả thành công của Call 1 đã nằm an toàn trong Journal.\n"
        "     + Hành vi khi phục hồi: Hệ thống đọc lại Journal, phát hiện Call 1 đã hoàn tất nên chỉ cần PHÁT LẠI (REPLAY) kết quả của Call 1 mà không cần gọi mạng, và TIẾP TỤC THỰC THI DUY NHẤT Call 2 còn thiếu.\n"
        "2. Đánh giá Tính Đúng đắn và Hiệu quả Tài nguyên:\n"
        "   - Call-Level Journaling vượt trội hoàn toàn về tính an toàn: Loại trừ 100% rủi ro lặp lại tác dụng phụ ngoài của Call 1.\n"
        "   - Tiết kiệm chi phí và thời gian: Giảm một nửa thời gian phục hồi của Node B và không tiêu tốn thêm quota API của nhà cung cấp."
    ),
    "explanation": (
        "Độ mịn của cơ chế lưu vết (Checkpoint Granularity) quyết định mức độ tin cậy của các workflow AI phức tạp. Trong khi Checkpoint cấp Node chỉ phù hợp cho các luồng xử lý dữ liệu hàng loạt không có tác dụng phụ, thì Nhật ký cấp Cuộc gọi (Call-Level Journaling) là tiêu chuẩn bắt buộc cho các Agent điều phối các công cụ bên ngoài, bảo đảm tính lũy đẳng ở mức độ chi tiết nhất."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] So sánh chính xác độ mịn: Node Checkpoint lưu ở biên node; Call-Level Journal lưu ở từng cuộc gọi riêng lẻ.\n"
        "- [1.5 điểm] Phân tích hạn chế của Node Checkpoint: Buộc phải chạy lại toàn bộ Node B từ đầu, làm lặp lại Call 1 và gây side-effects ngoài.\n"
        "- [1.5 điểm] Khẳng định ưu thế của Call-Level Journal: Replay kết quả Call 1 từ đĩa và chỉ thực thi tiếp Call 2, bảo vệ tính lũy đẳng."
    ),
    "reference_source": "Temporal.io Workflow Execution Model: https://docs.temporal.io/workflows và Martin Fowler - Event Sourcing Pattern"
}

# 66. d12-q143 (4 pts)
DAY12_PART2_C["d12-q143"] = {
    "sample_answer": (
        "1. Lập Chuỗi Giao dịch Phân tán Saga (Saga Flow & Compensating Transactions):\n"
        "   - Bước 1 ($T_1$): `Đặt Chuyến bay (Book Flight)` -> Giao dịch bù trừ tương ứng ($C_1$): `Hủy chuyến bay và hoàn tiền (Cancel Flight & Refund)`.\n"
        "   - Bước 2 ($T_2$): `Đặt Khách sạn (Book Hotel)` -> Giao dịch bù trừ tương ứng ($C_2$): `Hủy phòng khách sạn và hoàn tiền (Cancel Hotel & Refund)`.\n"
        "   - Bước 3 ($T_3$): `Mua Vé Sự kiện Không Hoàn tiền (Buy Non-refundable Event Ticket)` -> KHÔNG CÓ GIAO DỊCH BÙ TRỪ ($C_3$ không tồn tại do chính sách vé không hoàn trả).\n"
        "2. Xác định Điểm Pivot Không thể Đảo ngược (Irreversible Pivot Step):\n"
        "   - Điểm Pivot chính là: `Bước 3: Mua vé sự kiện không hoàn tiền ($T_3$)`.\n"
        "   - Ý nghĩa kiến trúc: Đây là ranh giới phân định một chiều (Point of No Return). Một khi bước này đã được kích hoạt thành công, hệ thống không thể hoàn tác hay hủy bỏ. Do đó, nguyên tắc tối thượng của mẫu thiết kế Saga là BẮT BUỘC ĐẶT BƯỚC KHÔNG THỂ BÙ TRỪ VÀO VỊ TRÍ CUỐI CÙNG của chuỗi sau khi tất cả các bước có thể hoàn tác đã thành công mỹ mãn.\n"
        "3. Xử lý khi Bước Khách sạn Gặp Lỗi (Hotel Booking Failure Handling):\n"
        "   - Diễn biến sự cố: Bước 1 ($T_1$) thành công. Đến Bước 2 ($T_2$ - Đặt khách sạn) thì gặp lỗi sập hệ thống hoặc hết phòng.\n"
        "   - Cơ chế Hoàn tác Ngược dòng (Backward Compensation Execution):\n"
        "     + Vì sự cố xảy ra TRƯỚC KHI chạm tới Điểm Pivot ($T_3$ chưa từng được thực thi), toàn bộ chuỗi giao dịch được bảo vệ an toàn.\n"
        "     + Saga Coordinator tự động kích hoạt giao dịch bù trừ $C_1$: Gửi lệnh hủy vé máy bay đã đặt ở Bước 1 và hoàn tiền về thẻ của khách hàng.\n"
        "     + Trạng thái kết thúc: Workflow kết thúc an toàn với trạng thái `COMPENSATED_CANCELLED`. Người dùng được hoàn lại 100% tiền và không bị kẹt bất kỳ chi phí vé sự kiện không hoàn lại nào."
    ),
    "explanation": (
        "Mẫu thiết kế Saga (Saga Pattern) điều phối các giao dịch phân tán dài hạn bằng cách kết hợp các giao dịch thuận chiều và các giao dịch bù trừ (Compensating Transactions). Nhận diện chính xác Điểm Pivot (hành động không thể hoàn tác) và bố trí nó ở cuối chuỗi giúp hệ thống luôn có khả năng hoàn tác sạch sẽ nếu các bước phụ trợ phía trước gặp sự cố."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết lập chuỗi Saga hoàn chỉnh gồm 3 bước thuận và định nghĩa chính xác hành động bù trừ C1 (hủy bay) và C2 (hủy khách sạn).\n"
        "- [1.5 điểm] Xác định chính xác Điểm Pivot không thể đảo ngược là Bước 3 (Mua vé sự kiện không hoàn tiền) và giải thích nguyên tắc đặt ở cuối chuỗi.\n"
        "- [1.5 điểm] Xử lý sự cố khách sạn lỗi trước pivot: Kích hoạt hoàn tác C1 hủy chuyến bay, bảo đảm khách hàng không bị mất tiền oan."
    ),
    "reference_source": "Sagas (Hector Garcia-Molina & Kenneth Salem, 1987) & Microservices.io - Pattern: Saga: https://microservices.io/patterns/data/saga.html"
}

# 67. d12-q145 (4 pts)
DAY12_PART2_C["d12-q145"] = {
    "sample_answer": (
        "1. Phân tích Bản chất Các Bước và Xác định Điểm Pivot Không Thể Đảo Ngược:\n"
        "   - `Tạo report`: Hành động nội bộ, thuần túy tính toán, hoàn toàn có thể chạy lại hoặc hủy bỏ.\n"
        "   - `Reserve resource`: Hành động khóa tạm tài nguyên hạ tầng, có thể bù trừ bằng cách giải phóng (Release Hold).\n"
        "   - `Publish public`: Hành động công khai báo cáo ra Internet/mạng xã hội. ĐÂY LÀ ĐIỂM PIVOT KHÔNG THỂ THU HỒI (Irreversible Pivot). Một khi thông tin đã phát tán công khai ra bên ngoài, không thể hoàn tác lại trạng thái chưa công bố.\n"
        "   - `Cleanup`: Hành động dọn dẹp các tệp tin tạm thời.\n"
        "2. Sắp xếp Lại Thứ tự Chuẩn mực (Optimal Execution Sequence):\n"
        "   - Bước 1: `Tạo report (Generate Draft Report)` - Soạn thảo và tổng hợp nội dung báo cáo trong vùng nhớ tạm.\n"
        "   - Bước 2: `Reserve resource (Reserve Distribution Resources)` - Giữ chỗ băng thông và máy chủ phân phối.\n"
        "   - BƯỚC TRUNG GIAN BẮT BUỘC: `CỔNG PHÊ DUYỆT CỦA CON NGƯỜI (Human-in-the-Loop Approval Gate)`.\n"
        "   - Bước 3: `Publish public (Irreversible Pivot Action)` - Chỉ được thực thi sau khi nhận được sự phê duyệt chính thức.\n"
        "   - Bước 4: `Cleanup (Release Temporary Workspaces)` - Dọn dẹp tài nguyên sau khi đã phát hành thành công.\n"
        "3. Thiết kế Cổng Duyệt cho Pivot (Approval Gate Specification):\n"
        "   - Vị trí Cổng duyệt: Đặt chính xác ngay sau Bước 2 (khi bản thảo và tài nguyên đã sẵn sàng) và ngay TRƯỚC Bước 3 (`Publish public`).\n"
        "   - Cơ chế Hoạt động:\n"
        "     + Tiến trình workflow tạm dừng, chuyển trạng thái sang `AWAITING_HUMAN_APPROVAL`.\n"
        "     + Hệ thống gửi bản xem trước (Preview Draft) tới Người có Thẩm quyền (Reviewer/Editor).\n"
        "     + Kịch bản Chấp thuận (Approved): Reviewer nhấn duyệt -> Kích hoạt Bước 3 (Publish) và chuyển sang Bước 4 (Cleanup).\n"
        "     + Kịch bản Bác bỏ (Rejected): Reviewer từ chối -> Kích hoạt nhánh bù trừ: Giải phóng tài nguyên đã reserve ở Bước 2, xóa bản draft ở Bước 1 và chuyển trạng thái sang `REJECTED_CANCELLED` mà không có bất kỳ thông tin nào bị rò rỉ ra ngoài."
    ),
    "explanation": (
        "Trong các hệ thống tự động hóa sử dụng AI Agent, nguyên tắc 'Human-in-the-Loop' tại các điểm không thể đảo ngược (Irreversible Pivots) là ranh giới an toàn tối quan trọng. Bằng cách tách biệt giai đoạn chuẩn bị có thể bù trừ khỏi giai đoạn phát hành không thể thu hồi và chèn cổng phê duyệt ở giữa, doanh nghiệp ngăn chặn triệt để các rủi ro phát tán nội dung sai lệch ra công chúng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác bản chất của từng bước và xác định `Publish public` là Điểm Pivot không thể đảo ngược.\n"
        "- [1.5 điểm] Sắp xếp lại thứ tự logic chuẩn mực: Tạo report -> Reserve resource -> Cổng duyệt -> Publish public -> Cleanup.\n"
        "- [1.5 điểm] Thiết kế cơ chế Cổng duyệt con người (Human Gate) chi tiết: Xử lý nhánh duyệt (chạy publish) và nhánh từ chối (bù trừ release tài nguyên)."
    ),
    "reference_source": "Human-in-the-Loop AI Architecture Guidelines & Enterprise Workflow Governance Standards"
}

# 68. d12-q147 (4 pts)
DAY12_PART2_C["d12-q147"] = {
    "sample_answer": (
        "1. Đánh giá và Loại bỏ Các Lộ trình Không An toàn (Flawed Paths Elimination):\n"
        "   - Lộ trình `Resume` Trực tiếp: TUYỆT ĐỐI BỊ LOẠI BỎ (CRITICAL VIOLATION). Bối cảnh ghi nhận 3 sự cố đồng thời: Token đã hết hạn (lỗi xác thực), kho hàng đã thay đổi (lỗi tính sẵn sàng của hàng hóa) và số tiền đã duyệt cũ không còn khớp với thực tế. Việc cố tình resume sẽ gây lỗi giao dịch hoặc tổn thất tài chính nghiêm trọng cho doanh nghiệp.\n"
        "   - Lộ trình `Cancel` Ngay lập tức: Quá tiêu cực và gây trải nghiệm xấu cho khách hàng nếu họ vẫn có nhu cầu giao dịch thực tế.\n"
        "2. Lựa chọn Lộ trình Tối ưu: Lộ trình Tái Lập Kế hoạch và Tái Phê duyệt (RE-PLAN -> RE-APPROVE PATH):\n"
        "   - Lựa chọn: Kết hợp quy trình Tái Lập Kế hoạch (Re-plan) và Tái Phê duyệt (Re-approve) có kiểm soát.\n"
        "3. Các Bước Thực thi Chi tiết trong Lộ trình:\n"
        "   - Bước 1 (Làm mới Danh tính Xác thực - Token Refresh):\n"
        "     Sử dụng OAuth 2.0 Refresh Token để cấp phát một Access Token mới còn thời hạn, khôi phục phiên giao dịch an toàn.\n"
        "   - Bước 2 (Tái Lập Kế hoạch Dựa trên Hiện trạng Mới - Re-plan Phase):\n"
        "     Truy vấn lại cơ sở dữ liệu Kho hàng (Inventory) để xác định số lượng tồn kho thực tế khả dụng. Tính toán lại đơn giá, phí vận chuyển và tổng số tiền giao dịch chính xác theo hiện trạng mới (`Amount_New`).\n"
        "   - Bước 3 (Kích hoạt Tái Phê duyệt Bắt buộc - Re-approve Phase):\n"
        "     Vì `Amount_New` đã thay đổi so với số tiền cũ mà người phê duyệt đã ký (`Amount_Old`), nguyên tắc tuân thủ tài chính BẮT BUỘC phải tạo một yêu cầu phê duyệt mới. Gửi thông báo tới Người phê duyệt (Approver) nêu rõ lý do chênh lệch (do thay đổi kho hàng/đơn giá) và yêu cầu ký duyệt lại số tiền mới.\n"
        "   - Bước 4 (Thực thi Giao dịch): Chỉ sau khi nhận được sự đồng thuận (Re-approval) mới, hệ thống mới cập nhật bản ghi vào Journal và thực hiện thanh toán trừ tiền."
    ),
    "explanation": (
        "Khi các điều kiện ngoại cảnh (thời hạn token, số lượng tồn kho, giá trị giao dịch) đã thay đổi trong quá trình chờ đợi, dữ liệu đã lưu trong journal trước đó không còn phản ánh đúng sự thật khách quan. Quy trình Tái lập kế hoạch kết hợp Tái phê duyệt bảo đảm tính toàn vẹn của nghiệp vụ và tuân thủ các quy tắc quản trị tài chính khắt khe."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Loại bỏ chính xác lựa chọn Resume trực tiếp do vi phạm 3 điều kiện: Token hết hạn, kho đổi và amount sai lệch.\n"
        "- [1.5 điểm] Lựa chọn chính xác lộ trình Re-Plan kết hợp Re-Approve để giải quyết căn cơ sự biến động của ngoại cảnh.\n"
        "- [1.5 điểm] Trình bày đầy đủ 4 bước thực thi: Refresh token, tính toán lại inventory/amount, xin phê duyệt lại từ Approver và commit journal."
    ),
    "reference_source": "Financial Transaction Processing Standards & Enterprise Workflow Invalidation and Re-authorization Best Practices"
}

# 69. d12-q149 (4 pts)
DAY12_PART2_C["d12-q149"] = {
    "sample_answer": (
        "1. Lựa chọn Biện pháp Kiểm soát Phá vỡ Đường dẫn Tấn công (Attack Path Disruption Control):\n"
        "   - Biện pháp Áp dụng: Cấu hình Rào chắn Mạng Egress Không Tin cậy (Zero-Trust Egress Network Policy / Security Group Firewall) ở cấp độ container/pod của Job này:\n"
        "     + CHẶN TOÀN BỘ LƯU LƯỢNG ĐI RA INTERNET CÔNG CỘNG (Block Outbound Egress `0.0.0.0/0` on Ports 80, 443 và all arbitrary IPs).\n"
        "     + THIẾT LẬP DANH SÁCH TRẮNG NỘI BỘ TỐI THIỂU (Strict Egress Allowlist):\n"
        "       * Chỉ cho phép kết nối tới Private Database Subnet qua cổng CSDL nội bộ (ví dụ: `10.0.2.0/24:5432`).\n"
        "       * Chỉ cho phép kết nối tới Dịch vụ Email Doanh nghiệp nội bộ qua Private Link / VPC Endpoint (ví dụ: AWS SES Private Endpoint hoặc Internal SMTP Relay `10.0.3.50:587`).\n"
        "2. Đánh giá Mức độ Gián đoạn Chức năng (Functional Impact Assessment):\n"
        "   - Mức độ Mất Chức năng Nghiệp vụ = 0% (Zero Functional Loss):\n"
        "     Job này theo đặc tả kiến trúc 'không cần outbound ra ngoài Internet'. Do đó, việc chặn toàn bộ Internet công cộng không làm ảnh hưởng tới bất kỳ tính năng nghiệp vụ hợp lệ nào của Job (Job vẫn đọc/ghi DB bình thường và vẫn gửi email thông báo trơn tru).\n"
        "3. Cơ chế Phá vỡ Đường dẫn Tấn công Trích xuất Dữ liệu (Data Exfiltration Path Disruption):\n"
        "   - Nếu Job bị kẻ tấn công xâm nhập (ví dụ qua Prompt Injection hoặc lỗ hổng RCE trong thư viện xử lý), mã độc sẽ cố gắng thiết lập kênh kết nối ra bên ngoài (C2 Server, ngrok, DNS tunneling, webhook công cộng) để tuồn dữ liệu nhạy cảm ra ngoài.\n"
        "   - Nhờ Egress Firewall chặn cứng ở tầng hạt nhân mạng, mọi gói tin SYN ra Internet đều bị DROP ngay tại chỗ, vô hiệu hóa hoàn toàn âm mưu trích xuất dữ liệu mà không làm gián đoạn hệ thống."
    ),
    "explanation": (
        "Kiểm soát lưu lượng đi ra (Egress Filtering) là một trong những biện pháp phòng thủ hiệu quả nhất trong kiến trúc Zero Trust. Trong khi phần lớn các kỹ sư chỉ chú trọng chặn lưu lượng vào (Ingress), việc khóa chặt lưu lượng ra của các tác vụ không cần Internet giúp phá vỡ mắt xích cuối cùng của chuỗi tấn công (Kill Chain: Data Exfiltration), bảo vệ toàn vẹn dữ liệu doanh nghiệp."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác biện pháp kiểm soát: Egress Network Policy / Security Group chặn toàn bộ Internet Outbound (0.0.0.0/0).\n"
        "- [1.5 điểm] Thiết lập allowlist nội bộ cho phép truy cập Private DB và Internal Email Relay thông qua Private VPC Endpoints.\n"
        "- [1.5 điểm] Đánh giá mức độ mất chức năng bằng 0 và chứng minh phá vỡ hoàn toàn đường dẫn trích xuất dữ liệu của kẻ tấn công."
    ),
    "reference_source": "NIST SP 800-207 (Zero Trust Architecture) & CIS Kubernetes Benchmark - Network Policies and Egress Filtering"
}

# 70. d12-q151 (4 pts)
DAY12_PART2_C["d12-q151"] = {
    "sample_answer": (
        "1. Bổ sung Bộ Ba Cơ chế Kiểm soát Phòng thủ Chiều sâu (Three-Layer Defense-in-Depth Controls):\n"
        "   - Bối cảnh: Provider proxy là kênh giao tiếp bắt buộc được phép hoạt động để trả nội dung hiển thị (rendered content) cho người dùng cuối, nhưng nội dung này có rủi ro chứa bí mật doanh nghiệp.\n"
        "   - Lớp 1 (Kiểm duyệt Khử Nhạy cảm tại Biên Công cụ - Tool Boundary Redaction):\n"
        "     Trước khi nạp dữ liệu từ cơ sở dữ liệu hay API vào context của LLM, hệ thống áp dụng bộ lọc nhận dạng PII/Secret (Regex & Entity Recognizer). Tất cả các trường nhạy cảm (mật khẩu, API key, số thẻ tín dụng, số an sinh) đều được che giấu hoặc thay thế bằng token giả định (ví dụ: `api_key: 'sk-***REDACTED***'`).\n"
        "   - Lớp 2 (Kiểm duyệt Nội dung Render tại Tầng Proxy - Rendered Content Inspection & Masking Filter):\n"
        "     Tại Provider Proxy, trước khi chuyển tiếp dữ liệu ra ngoài cho người dùng, nội dung HTML/Markdown đi qua một Middleware thanh lọc (Sanitizer Middleware):\n"
        "     + Quét đối chiếu với cơ sở dữ liệu chữ ký bí mật của doanh nghiệp (Entropy Scanner & Secret Patterns).\n"
        "     + Bóc tách triệt để các thẻ nguy hiểm (Script tags, iframes, thẻ img mang nguồn lạ) để ngăn chặn tấn công XSS và rò rỉ qua kênh ẩn (Hidden Exfiltration Channels).\n"
        "   - Lớp 3 (Chính sách Bảo mật Nội dung Phía Máy khách - Strict Content Security Policy / CSP):\n"
        "     Provider Proxy đính kèm các tiêu đề HTTP CSP nghiêm ngặt khi trả rendered content về trình duyệt:\n"
        "     `Content-Security-Policy: default-src 'none'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self';`.\n"
        "     Tiêu đề này ngăn chặn trình duyệt gửi bất kỳ yêu cầu mạng nào ra tên miền bên thứ ba ngay cả khi nội dung render bị chèn mã độc.\n"
        "2. Giữ vững Kênh Truyền Phục vụ (Preserving Allowed Channel):\n"
        "   - Bằng cách áp dụng 3 lớp kiểm soát trên, kênh truyền Provider Proxy vẫn được duy trì 100% để người dùng nhận được nội dung hiển thị trực quan đẹp mắt, trong khi rủi ro rò rỉ bí mật được triệt tiêu hoàn toàn."
    ),
    "explanation": (
        "Không thể giải quyết bài toán an ninh bằng cách loại bỏ các kênh truyền thông hợp lệ cần thiết cho trải nghiệm người dùng. Việc triển khai các cơ chế thanh lọc dữ liệu nhiều tầng (từ làm sạch dữ liệu đầu vào công cụ đến kiểm duyệt nội dung hiển thị tại proxy và cưỡng chế CSP tại trình duyệt) giúp bảo vệ an toàn thông tin tuyệt đối mà vẫn giữ nguyên luồng nghiệp vụ của doanh nghiệp."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Giữ nguyên kênh truyền hợp lệ của Provider Proxy mà không hủy bỏ kênh giao tiếp của người dùng.\n"
        "- [1.5 điểm] Thiết lập cơ chế thanh lọc tại biên công cụ (Tool Redaction) và kiểm duyệt nội dung tại Proxy (Sanitizer Middleware).\n"
        "- [1.5 điểm] Cấu hình tiêu đề Content Security Policy (CSP) nghiêm ngặt tại trình duyệt ngăn chặn exfiltration ra bên ngoài."
    ),
    "reference_source": "OWASP Top 10 for Large Language Model Applications (LLM06: Sensitive Information Disclosure) & W3C CSP Specification"
}

# 71. d12-q154 (4 pts)
DAY12_PART2_C["d12-q154"] = {
    "sample_answer": (
        "1. Lựa chọn Cơ chế Cách ly Tối ưu (Isolation Mechanism Selection):\n"
        "   - Lựa chọn: Trình Đánh giá Cây Cú pháp Trừu tượng An toàn trong Tiến trình (In-Process Safe AST Evaluator / Restricted Expression Engine) với Danh sách Trắng Ngữ pháp (Grammar Whitelist).\n"
        "   - Biện minh dựa trên các điều kiện ràng buộc của bối cảnh:\n"
        "     + Yêu cầu độ trễ cực thấp (< 10ms): Loại bỏ hoàn toàn các giải pháp ảo hóa nặng nề như Container (Docker cold start mất hàng trăm mili-giây) hoặc MicroVM (Firecracker mất 100-200ms để boot).\n"
        "     + Ngữ pháp ngôn ngữ rất hẹp (Narrow Grammar): Biểu thức chỉ chứa các phép toán cơ bản, so sánh logic và hằng số (ví dụ: `a > 10 AND b == 'active'`). Không cần các tính năng lập trình đầy đủ.\n"
        "     + Rủi ro thấp: Chỉ là tính toán biểu thức đánh giá điều kiện.\n"
        "     + Thiết kế In-Process AST: Sử dụng trình phân tích cú pháp AST của ngôn ngữ (như module `ast` trong Python) duyệt qua cây cú pháp và CHỈ CHO PHÉP các node toán học (`Add`, `Sub`, `Compare`, `Constant`), CẤM TUYỆT ĐỐI các hàm nguy hiểm (`eval`, `exec`, `__import__`, truy cập thuộc tính `__builtins__`). Trình phân tích thực thi trong < 1ms, không cấp quyền truy cập tệp tin (File I/O) hay mạng (Network I/O).\n"
        "2. Ranh giới Tồn dư Cần Giám sát và Kiểm soát (Residual Boundary Controls):\n"
        "   - Rủi ro Tồn dư 1: Tấn công Từ chối Dịch vụ Tiêu tốn CPU (Algorithmic Complexity DoS / ReDoS):\n"
        "     Người dùng gửi biểu thức có độ phức tạp tính toán khổng lồ hoặc lũy thừa lồng nhau (ví dụ: `9 ** 999999`).\n"
        "     -> Biện pháp kiểm soát: Giới hạn độ dài chuỗi biểu thức (< 200 ký tự), giới hạn độ sâu tối đa của cây AST (< 5 cấp) và đặt thời gian ngắt luồng xử lý cứng (Execution Timeout = 5ms).\n"
        "   - Rủi ro Tồn dư 2: Tấn công Tràn Bộ nhớ (Memory Exhaustion):\n"
        "     -> Biện pháp kiểm soát: Cấm các phép toán nhân chuỗi lớn, giới hạn kích thước tối đa của kiểu số nguyên trả về."
    ),
    "explanation": (
        "Lựa chọn cơ chế cách ly thực thi mã đòi hỏi sự cân bằng tinh tế giữa mức độ an ninh và chi phí độ trễ. Khi bài toán có ngữ pháp rất hẹp và yêu cầu thời gian đáp ứng dưới 10ms, việc sử dụng trình phân tích AST hạn chế trong tiến trình mang lại hiệu năng siêu tốc và miễn nhiễm hoàn toàn với các tấn công truy cập file/mạng, trong khi các hạn chế về độ sâu cú pháp bảo vệ hệ thống khỏi các cuộc tấn công DoS CPU."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác cơ chế In-Process Safe AST Evaluator với grammar whitelist và giải thích loại bỏ container/VM do trần 10ms.\n"
        "- [1.5 điểm] Thực thi triệt để việc cấm truy cập file và network ở cấp độ cây cú pháp trừu tượng AST.\n"
        "- [1.5 điểm] Nhận diện chính xác các rủi ro ranh giới tồn dư (CPU DoS/lũy thừa lớn) và thiết lập biện pháp ngắt timeout 5ms, giới hạn độ sâu cây AST."
    ),
    "reference_source": "Python AST Security & Safe Evaluation Best Practices: https://docs.python.org/3/library/ast.html và Sandboxing Untrusted Code Architecture Patterns"
}

# 72. d12-q156 (4 pts)
DAY12_PART2_C["d12-q156"] = {
    "sample_answer": (
        "1. Sửa Bảng Quyết định theo Chính sách Hạn chế Tối đa (Restrictive Default-Deny Decision Table):\n"
        "   - Nguyên tắc Cốt tử: Mặc định Từ chối (Default-Deny). Mọi trạng thái cấu hình không hoàn hảo hoặc không chứng minh được tính hợp lệ bắt buộc phải bị từ chối tiếp cận hệ thống.\n"
        "   - Bảng Quyết định Chuẩn mực:\n"
        "     | Tình huống Kiểm thử | Đầu vào Cấu hình (Input State) | Trạng thái Đánh giá | Quyết định Thực thi | Kết quả Quan sát / Mã Lỗi |\n"
        "     | :--- | :--- | :--- | :--- | :--- |\n"
        "     | Case 1: Missing Config | File cấu hình vắng mặt hoàn toàn (`None` / 404) | Lỗi Thiếu File Cấu hình | DENY / BLOCK | Ném lỗi `ConfigMissingException` (Exit 1) |\n"
        "     | Case 2: Empty Config | File tồn tại nhưng nội dung rỗng `{}` | Thiếu quy tắc cho phép | DENY / BLOCK | Ném lỗi `PolicyNotConfiguredException` |\n"
        "     | Case 3: Invalid JSON | File chứa cú pháp JSON lỗi (`{invalid...`) | Cú pháp không hợp lệ | DENY / BLOCK | Ném lỗi `JSONDecodeError` (Exit 1) |\n"
        "     | Case 4: Populated `/tmp` | Cấu hình hợp lệ: `{\"allowed_paths\": [\"/tmp\"]}` | Đạt chuẩn và đường dẫn an toàn | ALLOW / PERMIT | Cấp quyền truy cập DUY NHẤT thư mục `/tmp` |\n"
        "     | Case 5: Path Traversal | Cấu hình hợp lệ chứa `\"/tmp/../etc\"` | Vi phạm ranh giới cho phép | DENY / BLOCK | Ném lỗi `SecurityBoundaryViolation` |\n"
        "2. Phân tích Logic Sửa đổi và Phòng vệ Fail-Closed:\n"
        "   - Sai lầm thường gặp trong các hệ thống cũ: Coi `empty config` hoặc `missing config` như một trạng thái cho phép mặc định hoặc áp dụng cấu hình dự phòng lỏng lẻo.\n"
        "   - Sửa đổi chuẩn mực (Fail-Closed Architecture): Tách biệt hoàn toàn ba trạng thái lỗi kỹ thuật (Missing, Empty, Invalid) khỏi nhánh Populated. Khi gặp bất kỳ trạng thái nào trong ba trạng thái lỗi này, hệ thống lập tức ĐÓNG BĂNG VÀ TỪ CHỐI KHỞI ĐỘNG (Fail-Safe Shutdown), không bao giờ mở quyền truy cập hệ thống tệp tin."
    ),
    "explanation": (
        "Nguyên tắc 'Fail-Closed' (Thất bại thì Đóng cửa) là nền tảng của kỹ thuật bảo mật cấu hình. Một bảng quyết định hạn chế bảo đảm rằng sự vắng mặt, trống rỗng hay lỗi cú pháp của tệp cấu hình không bao giờ bị hiểu ngầm là sự cho phép tự do. Quyền truy cập chỉ được khai mở khi và chỉ khi có một cấu hình đầy đủ, hợp lệ và đáp ứng danh sách trắng an toàn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết lập bảng quyết định hoàn chỉnh phân định rõ 4 trường hợp: Missing, Empty, Invalid JSON và Populated /tmp.\n"
        "- [1.5 điểm] Thực thi nghiêm ngặt nguyên tắc Default-Deny: 3 trường hợp Missing, Empty và Invalid JSON đều dẫn tới quyết định dứt khoát là DENY.\n"
        "- [1.5 điểm] Chỉ cho phép duy nhất nhánh Populated /tmp hợp lệ (ALLOW) và bổ sung kiểm tra chống tấn công vượt ranh giới Path Traversal."
    ),
    "reference_source": "NIST SP 800-53 Rev. 5 (Configuration Management & Least Functionality) và OWASP Secure Coding Practices Checklist"
}

# 73. d12-q159 (3 pts) - 3 POINTS
DAY12_PART2_C["d12-q159"] = {
    "sample_answer": (
        "1. Thiết kế Danh tính và Token Đặc quyền Tối thiểu (Least-Privilege Workload Identity):\n"
        "   - Bối cảnh: Task T chỉ có nhiệm vụ đọc dữ liệu từ Bucket B trong vòng 5 phút, nhưng token hiện tại lại có audience của dịch vụ billing và quyền ghi toàn phần (`write-all`).\n"
        "   - Thu hẹp 4 Chiều Danh tính của Token Mới:\n"
        "     + Thu hẹp Chủ thể (`sub` - Subject): Gán danh tính định danh duy nhất của tác vụ: `sub: \"workload://tasks/task-T\"`.\n"
        "     + Thu hẹp Khán giả (`aud` - Audience): Đổi sang đúng khán giả đích danh của dịch vụ lưu trữ: `aud: \"https://storage.enterprise.internal/bucket-B\"` (Loại bỏ hoàn toàn audience `billing`).\n"
        "     + Thu hẹp Quyền hạn (`scope` / `permissions`): CHỈ CẤP QUYỀN ĐỌC TỐI THIỂU: `actions: [\"s3:GetObject\"]` giới hạn trên tài nguyên `resource: \"arn:aws:s3:::bucket-B/*\"` (Thu hồi 100% quyền `write-all` và xóa bỏ quyền `PutObject`/`DeleteObject`).\n"
        "     + Thu hẹp Thời hạn Sống (`exp` - Lifetime): Thiết lập thời hạn sống ngắn (Short-Lived Token): Đúng 300 giây (5 phút). Sau 5 phút, token tự động hết hạn và không thể sử dụng.\n"
        "2. Thiết kế Bộ Kiểm thử Từ chối (Rejection & Boundary Test Suite):\n"
        "   - Test 1 (Audience Rejection Test - Chống Confused Deputy):\n"
        "     Task T mang token mới gọi tới API Billing `POST /billing/invoices` -> Phản hồi mong đợi: BỊ TỪ CHỐI với `HTTP 403 Forbidden` do sai claim `aud`.\n"
        "   - Test 2 (Write Permission Rejection Test):\n"
        "     Task T cố gắng thực hiện hành động ghi tệp `s3:PutObject` lên Bucket B -> Phản hồi mong đợi: BỊ TỪ CHỐI với `HTTP 403 Access Denied` do thiếu quyền ghi.\n"
        "   - Test 3 (Storage Boundary Rejection Test):\n"
        "     Task T cố gắng đọc dữ liệu từ một Bucket C khác -> Phản hồi mong đợi: BỊ TỪ CHỐI với `HTTP 403 Forbidden` do tài nguyên nằm ngoài phạm vi cấp phép.\n"
        "   - Test 4 (Lifetime Expiration Rejection Test):\n"
        "     Tại thời điểm phút thứ 5 và 10 giây (T+310s), Task T gửi lệnh đọc `s3:GetObject` lên Bucket B -> Phản hồi mong đợi: BỊ TỪ CHỐI với `HTTP 401 Unauthorized` kèm thông báo `Token has expired`.\n"
        "   - Test 5 (Positive Verification Test):\n"
        "     Trong vòng 5 phút đầu tiên, Task T thực hiện đọc tệp hợp lệ từ Bucket B -> Kết quả: Đạt `HTTP 200 OK` thành công mỹ mãn."
    ),
    "explanation": (
        "Áp dụng nguyên tắc Đặc quyền Tối thiểu (Principle of Least Privilege) cho danh tính tác vụ đám mây yêu cầu sự thắt chặt đồng thời trên cả 4 trục: Danh tính chủ thể (Subject), Khán giả thụ hưởng (Audience), Quyền hạn thao tác (Scope) và Thời gian hiệu lực (Expiration). Bộ kiểm thử từ chối bảo đảm rằng mọi nỗ lực vượt rào phạm vi đều bị chặn đứng ngay từ tầng xác thực."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
        "- [1.0 điểm] Thu hẹp chuẩn xác cả 4 thuộc tính của token: Subject task-T, Audience bucket-B, Scope chỉ đọc (s3:GetObject), TTL đúng 5 phút.\n"
        "- [1.0 điểm] Xây dựng các bài kiểm thử từ chối (Rejection Tests) chứng minh bị từ chối khi gọi Billing, khi cố ghi Bucket B, và khi đọc Bucket C.\n"
        "- [1.0 điểm] Kiểm thử từ chối khi hết hạn sau 5 phút (401 Expired) và xác nhận đọc thành công trong thời hạn cho phép."
    ),
    "reference_source": "RFC 7519 (JSON Web Token) & AWS IAM Best Practices - Grant Least Privilege: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege"
}

print("Loaded Day 12 Part 2 Sub-part C (questions 61 to 73).")
