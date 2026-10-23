# scripts/day12_part2_a.py
# -*- coding: utf-8 -*-
"""
Day 12 Part 2 Sub-part A: Questions 37 to 48 (d12-q079 to d12-q104)
"""

DAY12_PART2_A = {}

# 37. d12-q079 (4 pts)
DAY12_PART2_A["d12-q079"] = {
    "sample_answer": (
        "1. Sắp xếp Quy trình Ứng phó Sự cố Lộ API Key (Incident Response Sequence):\n"
        "   - Bước 1 (Emergency Containment - Ngăn chặn Khẩn cấp):\n"
        "     + Truy cập ngay bảng điều khiển của nhà cung cấp model (Provider Dashboard).\n"
        "     + Thu hẹp quyền hạn của API Key bị lộ (K1): Gán ngay IP Whitelist hoặc hạn chế CORS nếu hỗ trợ, hoặc đặt Rate Limit khắt khe để giảm thiểu thiệt hại khai thác.\n"
        "   - Bước 2 (Credential Generation & Dual-Key Deployment - Tạo và Triển khai Khóa Mới):\n"
        "     + Tạo API Key mới (K2) tuân thủ nguyên tắc quyền tối thiểu (Least Privilege), chỉ cấp các quyền cần thiết cho ứng dụng.\n"
        "     + Cập nhật K2 vào hệ thống quản lý bí mật trung tâm (Cloud Secret Manager / Vault).\n"
        "     + Kích hoạt quy trình cập nhật cấu hình cho các consumer production mà không cần dừng dịch vụ (Zero-Downtime Secret Rotation). Duy trì song song K1 và K2 trong một cửa sổ ngắn (12-24 giờ).\n"
        "   - Bước 3 (Hard Revocation of Compromised Key - Thu hồi Triệt để Khóa Lộ):\n"
        "     + Theo dõi telemetry: Khi số lượng request sử dụng K1 giảm về 0, thực hiện thu hồi vĩnh viễn (Revoke / Delete) K1 trên console nhà cung cấp. Bất kỳ ai cố gắng dùng K1 đều sẽ bị từ chối với HTTP 401.\n"
        "   - Bước 4 (Repository Sanitization & Log Cleanup - Làm sạch Lịch sử Mã nguồn):\n"
        "     + Sử dụng công cụ chuyên dụng như `git-filter-repo` hoặc BFG Repo-Cleaner để loại bỏ hoàn toàn chuỗi bí mật khỏi toàn bộ commit history của git, sau đó force-push lên repository trung tâm.\n"
        "     + Xóa các log build CI/CD đã lưu trữ có chứa chuỗi bí mật.\n"
        "2. Các Bước Xác minh Thực tế (Verification Steps):\n"
        "   - Xác minh 1 (Key Revocation Verification): Gửi HTTP request trực tiếp tới Model Provider bằng API key cũ K1 -> Xác nhận nhận mã lỗi `HTTP 401 Unauthorized`.\n"
        "   - Xác minh 2 (Production Traffic Continuity): Kiểm tra dashboard ứng dụng và log hệ thống, xác nhận 100% các consumer production đang giao tiếp thành công với K2 (HTTP 200).\n"
        "   - Xác minh 3 (Secret Scanning Verification): Chạy công cụ quét bí mật tự động (Gitleaks / TruffleHog) trên toàn bộ git repo và CI pipelines -> Khẳng định kết quả 0 findings."
    ),
    "explanation": (
        "Khi sự cố rò rỉ thông tin xác thực xảy ra trong môi trường sản xuất có nhiều người dùng phụ thuộc, việc vội vàng thu hồi khóa ngay lập tức có thể gây ra sự cố gián đoạn dịch vụ diện rộng (Self-Inflicted Outage). Quy trình luân chuyển khóa hai giai đoạn (Dual-Key Rotation) kết hợp ngăn chặn khẩn cấp và làm sạch lịch sử git bảo đảm an ninh tối đa mà vẫn duy trì tính liên tục của hoạt động kinh doanh."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân định rạch ròi quy trình ứng phó theo thứ tự: Ngăn chặn khẩn cấp -> Tạo khóa mới K2 -> Thu hồi khóa cũ K1 -> Dọn dẹp git history.\n"
        "- [1.5 điểm] Xử lý an toàn quá trình luân chuyển khóa cho nhiều production consumer mà không gây gián đoạn dịch vụ (Zero-Downtime Rotation).\n"
        "- [1.5 điểm] Nêu rõ các bước xác minh độc lập: kiểm tra K1 trả về 401, consumer chạy ổn định với K2, và quét sạch repo với Gitleaks/TruffleHog."
    ),
    "reference_source": "NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide) & OWASP Secrets Management Cheat Sheet"
}

# 38. d12-q081 (5 pts) - 5 POINTS
DAY12_PART2_A["d12-q081"] = {
    "sample_answer": (
        "1. Dự đoán và Phân tích Kết quả của Từng Cơ chế Kiểm soát (Layered Security Evaluation):\n"
        "   - Cơ chế 1 (Lớp Mã hóa Kênh truyền - Transport Layer Security / TLS Termination):\n"
        "     + Đánh giá: KẾT QUẢ ĐẠT (PASS).\n"
        "     + Phân tích: Yêu cầu sử dụng giao thức HTTPS với chứng chỉ TLS hợp lệ. Quá trình bắt tay mã hóa TLS Handshake thành công, dữ liệu truyền tải giữa trình duyệt và máy chủ được mã hóa an toàn bằng thuật toán mã hóa hiện đại.\n"
        "   - Cơ chế 2 (Lớp Kiểm soát Nguồn gốc Trình duyệt - CORS / Origin Policy Enforcement):\n"
        "     + Đánh giá: KẾT QUẢ ĐẠT (PASS).\n"
        "     + Phân tích: Header `Origin` gửi từ trình duyệt nằm trong danh sách trắng (Allowlist) được máy chủ cấu hình. Máy chủ chấp thuận nguồn gốc và trả về các tiêu đề CORS hợp lệ (`Access-Control-Allow-Origin: <origin>`, `Access-Control-Allow-Credentials: true`).\n"
        "   - Cơ chế 3 (Lớp Xác thực Danh tính - Authentication / JWT Validation Middleware):\n"
        "     + Đánh giá: KẾT QUẢ ĐẠT (PASS).\n"
        "     + Phân tích: JWT Bearer Token có cấu trúc hợp lệ, chữ ký số (Signature) khớp với khóa công khai của Identity Provider, token chưa hết hạn (`exp`), thỏa mãn điều kiện `nbf` và định danh chính xác người dùng (`user_id`).\n"
        "   - Cơ chế 4 (Lớp Phân quyền và Phạm vi Thao tác - Authorization / Scope Enforcement):\n"
        "     + Đánh giá: KẾT QUẢ TỪ CHỐI / THẤT BẠI (FAIL / REJECTED).\n"
        "     + Phân tích: Thao tác người dùng yêu cầu là một hành động ghi/thay đổi trạng thái dữ liệu (đòi hỏi scope `write`). Tuy nhiên, JWT của người dùng chỉ chứa các phạm vi quyền khác (ví dụ: chỉ có scope `read`). Tầng phân quyền phát hiện thiếu hụt đặc quyền bắt buộc.\n"
        "2. Kết quả Tổng thể của Yêu cầu và Mã Phản hồi Trả về:\n"
        "   - Máy chủ lập tức ngắt chuỗi thực thi và từ chối yêu cầu.\n"
        "   - Mã trạng thái phản hồi HTTP: `HTTP/1.1 403 Forbidden`.\n"
        "   - Thân phản hồi JSON tiêu chuẩn: `{\"error\": \"insufficient_scope\", \"required_scope\": \"write\", \"message\": \"Token hợp lệ nhưng không đủ quyền hạn để thực thi thao tác ghi dữ liệu này.\"}`.\n"
        "   - Lưu ý cốt tử: Không trả về mã 401 Unauthorized vì danh tính người dùng đã được xác thực thành công; mã 403 Forbidden là chỉ báo chuẩn mực cho lỗi thiếu quyền phân bổ (Authorization Failure)."
    ),
    "explanation": (
        "Mô hình phòng thủ chiều sâu (Defense-in-Depth) phân tách rạch ròi giữa Xác thực (Authentication - bạn là ai) và Phân quyền (Authorization - bạn được phép làm gì). Một yêu cầu có thể hoàn hảo về mặt bảo mật mạng (TLS), an toàn trình duyệt (CORS) và danh tính hợp pháp (JWT Auth), nhưng vẫn phải bị chặn dứt khoát tại chốt chặn cuối cùng (Scope Enforcement) nếu không sở hữu phạm vi quyền hạn tương ứng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 5 điểm):\n"
        "- [1.0 điểm] Đánh giá chính xác kết quả PASS cho tầng truyền dẫn TLS và tầng kiểm soát nguồn gốc CORS.\n"
        "- [2.0 điểm] Đánh giá chính xác kết quả PASS cho tầng xác thực JWT Authentication (chữ ký, thời hạn, danh tính hợp lệ).\n"
        "- [2.0 điểm] Phân tích chính xác kết quả FAIL tại tầng Authorization Scope Enforcement, trả về mã chuẩn HTTP 403 Forbidden."
    ),
    "reference_source": "RFC 6750 (OAuth 2.0 Bearer Token Usage) & OWASP API Security Top 10 - Broken Function Level Authorization"
}

# 39. d12-q083 (4 pts)
DAY12_PART2_A["d12-q083"] = {
    "sample_answer": (
        "1. Lựa chọn Chiều Mở rộng (Scaling Direction Selection):\n"
        "   - Lựa chọn: Mở rộng theo Chiều Dọc (Vertical Scaling / Scale-Up).\n"
        "   - Biện minh kỹ thuật:\n"
        "     + Bối cảnh chỉ rõ: Yêu cầu đơn lẻ cần tới 20GB RAM và 'không thể chia nhỏ để chạy song song' (Monolithic Memory Footprint).\n"
        "     + Trong điều kiện này, mở rộng theo chiều ngang (Horizontal Scaling / Scale-Out thêm pods) hoàn toàn vô dụng, vì nếu mỗi pod chỉ có 4GB hay 8GB RAM thì bất kỳ pod nào tiếp nhận request cũng sẽ lập tức bị hệ điều hành tiêu diệt do tràn bộ nhớ (OOMKilled).\n"
        "     + Lưu lượng thấp càng củng cố việc nâng cấp cấu hình tài nguyên của một instance đơn lẻ (Node/Pod cấu hình RAM lớn) là giải pháp tối ưu cả về mặt kỹ thuật lẫn chi phí.\n"
        "2. Thiết lập Giới hạn Tài nguyên Mới (Resource Requests and Limits Configuration):\n"
        "   - Cấu hình Container Spec (Kubernetes / Cloud Container):\n"
        "     ```yaml\n"
        "     resources:\n"
        "       requests:\n"
        "         memory: \"24Gi\"\n"
        "         cpu: \"4\"\n"
        "       limits:\n"
        "         memory: \"32Gi\"\n"
        "         cpu: \"8\"\n"
        "     ```\n"
        "   - Dành biên độ đệm (Buffer): Request 24GB đảm bảo Kubernetes scheduler chỉ xếp pod vào các worker node có tối thiểu 24GB RAM thực tế; limit 32GB bảo vệ container khỏi crash khi xảy ra phân mảnh bộ nhớ (Memory Fragmentation) trong quá trình tính toán.\n"
        "3. Cơ chế Xử lý khi Yêu cầu Vượt Trần Tài nguyên (Handling Resource Ceiling Breach):\n"
        "   - Tiền kiểm Kích thước Yêu cầu (Pre-Admission Payload Guardrail): API Gateway kiểm tra kích thước input/context; nếu ước tính tiêu thụ > 28GB RAM, từ chối ngay với `HTTP 413 Payload Too Large` hoặc `HTTP 400 Bad Request`.\n"
        "   - Bảo vệ Cgroup Memory Limit: Nếu bộ nhớ tiêu thụ chạm ngưỡng trần 32GB, cgroup sẽ kích hoạt OOMKiller trên tiến trình con của tác vụ thay vì làm sập toàn bộ máy chủ node host. Trả về mã lỗi `HTTP 507 Insufficient Storage` hoặc `HTTP 500` kèm log cảnh báo P1 cho đội ngũ SRE."
    ),
    "explanation": (
        "Hiểu rõ bản chất của khối lượng công việc là yếu tố tiên quyết trong kiến trúc co giãn điện toán đám mây. Đối với các tác vụ AI nguyên khối không thể phân tán bộ nhớ, mở rộng chiều dọc (Vertical Scaling) kết hợp với hạn mức cgroup chặt chẽ là giải pháp duy nhất khả thi để đảm bảo tác vụ thực thi thành công mà không gây nguy cơ đổ vỡ hạ tầng dùng chung."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác chiều mở rộng Vertical Scaling (Scale-Up) và giải thích vì sao Horizontal Scaling không thể giải quyết được.\n"
        "- [1.5 điểm] Cấu hình định lượng hạn mức tài nguyên mới với requests >= 24Gi và limits >= 32Gi có biên độ đệm an toàn.\n"
        "- [1.5 điểm] Thiết kế cơ chế xử lý khi vượt trần: tiền kiểm tra payload (HTTP 413) và bảo vệ cgroup giới hạn bộ nhớ."
    ),
    "reference_source": "Kubernetes Documentation - Managing Resources for Containers: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ và Linux Kernel Cgroups v2 Memory Controller"
}

# 40. d12-q085 (3 pts) - 3 POINTS
DAY12_PART2_A["d12-q085"] = {
    "sample_answer": (
        "1. Lựa chọn Chính sách Triển khai Tạm thời (Temporary Rollout Policy):\n"
        "   - Áp dụng Chính sách Kéo dài Rút cạn Kết nối (Extended Connection Draining / Deregistration Delay) kết hợp Cấu hình Khóa Phiên Dính (Sticky Sessions qua Cookie Affinity) và Chiến lược Rolling Update có kiểm soát:\n"
        "     + Thiết lập `maxUnavailable = 0` và `maxSurge = 1` trong Kubernetes Deployment.\n"
        "     + Cấu hình `terminationGracePeriodSeconds = 900` (15 phút) trên Pod, kết hợp với preStop hook gửi tín hiệu chuẩn bị dừng.\n"
        "     + Khi một replica cũ chuẩn bị thay thế: Load Balancer lập tức ngừng phân phối các kết nối mới vào replica này, nhưng VẪN DUY TRÌ các kết nối HTTP Streaming hiện tại cho đến khi stream dài hoàn tất tự nhiên hoặc chạm mốc giới hạn 15 phút.\n"
        "2. Dự đoán Lỗi Tiềm ẩn trong Giai đoạn Tạm thời:\n"
        "   - Hiện tượng Nghẽn Triển khai (Rollout Starvation / Stalling): Việc chờ đợi các stream kéo dài có thể khiến quá trình deploy phiên bản mới bị treo hàng giờ đồng hồ.\n"
        "   - Đứt gãy Trải nghiệm (Stream Disruption): Nếu stream vượt quá 15 phút grace period, tiến trình sẽ bị tiêu diệt cưỡng bức bằng `SIGKILL`, làm mất toàn bộ session trong bộ nhớ của người dùng đó.\n"
        "3. Kế hoạch Thay thế Kiến trúc Dứt điểm (Permanent Architectural Migration):\n"
        "   - Tiến hành Tách biệt và Ngoại biên hóa Hoàn toàn Trạng thái (Full State Externalization): Chuyển toàn bộ dữ liệu session từ RAM tiến trình sang Redis Cluster phân tán.\n"
        "   - Khi hoàn tất, hệ thống chuyển sang mô hình hoàn toàn Stateless, loại bỏ kết nối dính (Sticky Sessions) và cho phép các replica thay thế tức thì mà không ảnh hưởng tới tiến trình stream."
    ),
    "explanation": (
        "Quản lý việc chuyển đổi hệ thống từ đơn khối có trạng thái (Stateful Monolith) sang phi trạng thái đám mây (Stateless Cloud-Native) đòi hỏi các giải pháp chuyển tiếp an toàn. Connection Draining bảo vệ các tác vụ stream đang dở dang trong ngắn hạn, nhưng ngoại biên hóa trạng thái phiên sang bộ nhớ đệm phân tán mới là giải pháp căn cơ để đạt được khả năng triển khai liên tục không gián đoạn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
        "- [1.0 điểm] Chọn chính xác policy tạm thời: Extended Connection Draining kết hợp Sticky Sessions và Rolling Update maxUnavailable = 0.\n"
        "- [1.0 điểm] Dự đoán chính xác các rủi ro kỹ thuật: quá trình rollout bị kéo dài (starvation) và stream bị ngắt nếu vượt quá grace period.\n"
        "- [1.0 điểm] Đề xuất phương án thay thế kiến trúc bền vững: ngoại biên hóa trạng thái phiên ra Redis để đạt chuẩn stateless hoàn toàn."
    ),
    "reference_source": "Kubernetes Pod Lifecycle - Termination of Pods: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination và AWS ALB Target Group Deregistration Delay"
}

# 41. d12-q087 (4 pts)
DAY12_PART2_A["d12-q087"] = {
    "sample_answer": (
        "1. Thiết kế Lại Chính sách Mở rộng (Scaling Policy Redesign):\n"
        "   - Vấn đề cốt tử: Tiếp tục co giãn số lượng replica theo độ dài hàng đợi (Queue Length) trong khi nhà cung cấp hạ nguồn đã chạm trần 200 cuộc gọi sẽ gây ra hiện tượng bão lỗi 429 và lãng phí điện toán.\n"
        "   - Thiết kế chính sách co giãn có nhận thức hạn ngạch (Quota-Aware Autoscaling):\n"
        "     + Đặt Trần Số lượng Replica Tối đa Cứng (Hard Max Replicas Cap): Giả sử mỗi worker replica có concurrency xử lý là 4 cuộc gọi, thì `max_replicas = 200 / 4 = 50 replicas`.\n"
        "     + Tín hiệu co giãn: Kết hợp độ dài hàng đợi với tỷ lệ lỗi nhà cung cấp. Nếu `provider_429_rate > 5%`, NGAY LẬP TỨC ĐÓNG BĂNG việc scale-out (Scale-Out Freeze), bất kể hàng đợi có tăng cao đến đâu.\n"
        "2. Cách Xử lý khi Hạn ngạch Quota bị Giới hạn (Quota Saturation Handling):\n"
        "   - Bước 1 (Áp lực ngược tại Cổng vào - Ingress Backpressure & Rate Limiting):\n"
        "     Khi số lượng cuộc gọi đang hoạt động đạt ngưỡng 190/200, API Gateway lập tức kích hoạt Load Shedding: Từ chối các yêu cầu mới của người dùng với mã `HTTP 429 Too Many Requests` kèm header `Retry-After: 10`, ngăn chặn việc dồn thêm tải vào hàng đợi.\n"
        "   - Bước 2 (Hạ cấp Dịch vụ Duyên dáng - Graceful Service Degradation):\n"
        "     + Tự động định tuyến một phần yêu cầu sang Mô hình Dự phòng Nhẹ hơn (Fallback Cheaper Model) có quota riêng hoặc chạy on-premise.\n"
        "     + Tăng cường sử dụng Semantic Cache: Trả về kết quả đã được lưu đệm đối với các truy vấn có ngữ nghĩa tương đồng thay vì gọi model mới.\n"
        "   - Bước 3 (Điều tiết Tốc độ Tiêu thụ của Worker - Dynamic Worker Throttling):\n"
        "     Worker tự động tăng thời gian chờ (Exponential Backoff Polling) khi phát hiện downstream quota bị bão hòa, giải phóng áp lực cho nhà cung cấp."
    ),
    "explanation": (
        "Tự động co giãn (Autoscaling) trong hệ thống tích hợp AI không thể chỉ dựa vào các chỉ số nội bộ như độ dài hàng đợi hay CPU. Việc thiết lập chính sách co giãn có nhận thức về hạn ngạch đối tác bên ngoài (Downstream Quota-Aware Autoscaling) kết hợp với cơ chế hạ cấp dịch vụ giúp bảo vệ doanh nghiệp khỏi tình trạng sụp đổ dây chuyền do bão rate limit."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế lại chính sách mở rộng: Đặt trần replica cứng tương ứng với 200 quota và đóng băng scale-out khi gặp lỗi 429.\n"
        "- [1.5 điểm] Xử lý quá tải bằng áp lực ngược (Backpressure): Load Shedding tại API Gateway trả về 429 kèm Retry-After.\n"
        "- [1.5 điểm] Xây dựng các phương án suy giảm duyên dáng: chuyển hướng sang mô hình fallback, tối đa hóa semantic cache và worker throttling."
    ),
    "reference_source": "Google SRE Book - Addressing Cascading Failures: https://sre.google/sre-book/addressing-cascading-failures/ và Kubernetes KEDA External Scalers"
}

# 42. d12-q090 (4 pts)
DAY12_PART2_A["d12-q090"] = {
    "sample_answer": (
        "1. Thiết kế Ba Loại Probe Chuẩn mực (Startup, Liveness, Readiness):\n"
        "   - Startup Probe (`/health/startup`):\n"
        "     + Nhiệm vụ: Đánh giá quá trình khởi động ban đầu của ứng dụng (nạp thư viện, cấu hình).\n"
        "     + Cấu hình: Kiểm tra cổng TCP hoặc endpoint nội bộ. Trong giai đoạn này, các probe khác bị tạm dừng. Khi probe này thành công một lần, nó nhường quyền cho Liveness và Readiness.\n"
        "   - Liveness Probe (`/health/liveness`):\n"
        "     + Nhiệm vụ: Kiểm tra TIẾN TRÌNH ỨNG DỤNG CÓ CÒN SỐNG VÀ KHÔNG BỊ TREO/DEADLOCK.\n"
        "     + Thiết kế: Thực thi một tác vụ bất đồng bộ nhẹ trong tiến trình (ví dụ: event loop ping, kiểm tra vòng lặp luồng). TUYỆT ĐỐI KHÔNG kiểm tra cơ sở dữ liệu ở probe này.\n"
        "     + Nếu app bị deadlock: Probe không thể phản hồi trong thời hạn timeout -> Liveness FAIL.\n"
        "   - Readiness Probe (`/health/readiness`):\n"
        "     + Nhiệm vụ: Kiểm tra TÍNH SẴN SÀNG PHỤC VỤ LƯU LƯỢNG NGƯỜI DÙNG.\n"
        "     + Thiết kế: Kiểm tra các dependency BẮT BUỘC (Cơ sở dữ liệu DB). Nếu DB ngắt kết nối -> Trả về `HTTP 503 Service Unavailable`. KHÔNG kiểm tra metrics exporter (dependency tùy chọn) trong probe này; metrics exporter lỗi thì ghi log cảnh báo nhưng Readiness vẫn trả về `HTTP 200 OK` (chạy ở chế độ degraded mode).\n"
        "2. Dự đoán Cách Xử lý của Hệ thống Điều phối (Orchestrator Behavior):\n"
        "   - Tình huống 1 (Cơ sở dữ liệu DB tạm thời không khả dụng):\n"
        "     Readiness Probe THẤT BẠI, trong khi Liveness Probe VẪN ĐẠT. Bộ điều phối (Kubernetes) sẽ GỠ BỎ POD KHỎI SERVICE ENDPOINTS (ngừng định tuyến lưu lượng vào Pod), nhưng TUYỆT ĐỐI KHÔNG RESTART POD. Khi DB phục hồi, Readiness tự động PASS trở lại và Pod tiếp tục nhận lưu lượng mà không bị khởi động lại vô nghĩa.\n"
        "   - Tình huống 2 (Ứng dụng bị Deadlock):\n"
        "     Liveness Probe THẤT BẠI liên tiếp vượt quá số lần retry cho phép. Bộ điều phối lập tức PHÁT TÍN HIỆU TIÊU DIỆT VÀ KHỞI ĐỘNG LẠI POD (Restart Container) để giải phóng deadlock.\n"
        "   - Tình huống 3 (Metrics exporter bị lỗi):\n"
        "     Cả Liveness và Readiness đều ĐẠT. Bộ điều phối duy trì Pod hoạt động bình thường, phục vụ người dùng trơn tru ở chế độ degraded."
    ),
    "explanation": (
        "Phân định rạch ròi trách nhiệm giữa Liveness Probe (kiểm tra sự sống của tiến trình) và Readiness Probe (kiểm tra tính sẵn sàng phục vụ) là nguyên tắc cốt lõi trong vận hành Kubernetes. Đưa dependency bên ngoài vào Liveness probe là lỗi sai kinh điển khiến toàn bộ cụm Pod bị khởi động lại liên hoàn (Cascading Restart Storm) khi cơ sở dữ liệu gặp sự cố tạm thời."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế chính xác 3 loại probe: Startup Probe khởi tạo, Liveness kiểm tra deadlock, Readiness kiểm tra dependencies.\n"
        "- [1.5 điểm] Phân lập đúng đắn: Liveness không phụ thuộc DB; Readiness kiểm tra DB bắt buộc và bỏ qua metrics exporter tùy chọn.\n"
        "- [1.5 điểm] Dự đoán chuẩn xác hành vi orchestrator: DB lỗi chỉ gỡ traffic không restart, deadlock kích hoạt restart pod, metrics lỗi vẫn chạy."
    ),
    "reference_source": "Kubernetes Documentation - Configure Liveness, Readiness and Startup Probes: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/"
}

# 43. d12-q093 (5 pts) - 5 POINTS
DAY12_PART2_A["d12-q093"] = {
    "sample_answer": (
        "1. Mô tả Thứ tự Dừng Hoạt động có Trật tự (Graceful Termination Lifecycle Sequence):\n"
        "   - Bước 1 (Tín hiệu Ngừng Hoạt động & Gỡ bỏ Endpoint):\n"
        "     Bộ điều phối (Kubernetes) gửi tín hiệu `SIGTERM` tới tiến trình chính của ứng dụng và đồng thời loại bỏ Pod khỏi danh sách Endpoint của Service / Load Balancer.\n"
        "   - Bước 2 (Kích hoạt Chế độ Đóng & Chặn Yêu cầu Mới):\n"
        "     Ứng dụng bắt được `SIGTERM`, kích hoạt cờ trạng thái `is_terminating = true`. Tầng HTTP Server / Middleware lập tức từ chối mọi yêu cầu mới đến sau thời điểm này.\n"
        "   - Bước 3 (Bắt đầu Khoảng thời gian Ân hạn - Grace Period Clock):\n"
        "     Đồng hồ đếm ngược thời gian ân hạn (`terminationGracePeriodSeconds`, ví dụ 30 giây) bắt đầu chạy. Ứng dụng duy trì hoạt động để cho phép các yêu cầu đang thực thi dở dang hoàn tất bình thường.\n"
        "   - Bước 4 (Cưỡng bức Tiêu diệt sau Hết hạn Ân hạn):\n"
        "     Nếu sau 30 giây mà tiến trình vẫn chưa tự kết thúc, bộ điều phối sẽ gửi tín hiệu cưỡng bức `SIGKILL` (kill -9) để giải phóng hoàn toàn tài nguyên.\n"
        "2. Kết quả Xử lý của Từng Loại Yêu cầu:\n"
        "   - Yêu cầu Mới Đến Sau khi Nhận Tín hiệu Termination:\n"
        "     + Xử lý: Do cờ `is_terminating = true` đã bật, ứng dụng lập tức từ chối tiếp nhận và phản hồi mã lỗi `HTTP 503 Service Unavailable` kèm header `Connection: close`, hoặc đóng kết nối socket ngay lập tức.\n"
        "     + Phía Client / Ingress: Reverse Proxy nhận thấy HTTP 503 sẽ tự động chuyển hướng yêu cầu (retry / failover) sang một Pod replica khác còn khỏe mạnh, người dùng cuối không bị gián đoạn.\n"
        "   - Yêu cầu Đang Chạy Vượt Quá Thời hạn Grace Period:\n"
        "     + Xử lý: Khi hết thời gian ân hạn 30 giây, tín hiệu `SIGKILL` được phát ra tiêu diệt ngay lập tức tiến trình container.\n"
        "     + Kết quả: Kết nối TCP bị đứt gãy đột ngột (Abrupt Connection Reset / Socket Closed). Bất kỳ transaction nào đang thực hiện dở dang trong database sẽ được hệ quản trị CSDL tự động rollback.\n"
        "     + Phía Client: Trình duyệt/Client nhận lỗi `HTTP 502 Bad Gateway` hoặc lỗi mạng; client có trách nhiệm thực hiện thử lại có kiểm soát (Idempotent Retry) với request ID tương ứng."
    ),
    "explanation": (
        "Quy trình dừng hoạt động có trật tự (Graceful Termination) là cơ chế bảo vệ tính toàn vẹn dữ liệu và độ tin cậy của dịch vụ phân tán. Việc từ chối dứt khoát các yêu cầu mới đến muộn và cưỡng bức tiêu diệt các tác vụ chạy quá hạn bảo đảm tiến trình triển khai phần mềm mới diễn ra đúng tiến độ mà không để lại các tiến trình thây ma (zombie processes) ngốn tài nguyên."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 5 điểm):\n"
        "- [1.0 điểm] Trình bày đầy đủ vòng đời dừng hoạt động theo thứ tự chuẩn: SIGTERM -> Bật cờ shutdown -> Đếm ngược Grace Period -> SIGKILL.\n"
        "- [2.0 điểm] Phân tích chuẩn xác kết quả của request mới đến sau SIGTERM: Bị từ chối với HTTP 503 / Connection close và chuyển hướng an toàn.\n"
        "- [2.0 điểm] Phân tích chuẩn xác kết quả của request vượt quá grace period: Bị ngắt kết nối đột ngột bởi SIGKILL, rollback DB transaction và xử lý lỗi phía client."
    ),
    "reference_source": "Kubernetes Documentation - Pod Lifecycle & Termination of Pods: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ và UNIX Signals Guide"
}

# 44. d12-q095 (5 pts) - 5 POINTS
DAY12_PART2_A["d12-q095"] = {
    "sample_answer": (
        "1. Lựa chọn Chiến lược Triển khai Tối ưu: Blue-Green Deployment (kết hợp Canary Gate):\n"
        "   - Lựa chọn: Áp dụng chiến lược Triển khai Xanh-Xanh lam (Blue-Green Deployment) kết hợp giai đoạn thử nghiệm lưu lượng nhỏ (Canary Phase).\n"
        "   - Biện minh dựa trên các điều kiện ràng buộc của bối cảnh:\n"
        "     + Tài nguyên dồi dào: Hệ thống có đủ năng lực tính toán để chạy song song 100% hai cụm môi trường (Blue: Phiên bản cũ đang chạy; Green: Phiên bản mới hoàn chỉnh).\n"
        "     + Cơ sở dữ liệu tương thích ngược: Lược đồ CSDL tuân thủ mẫu thiết kế Mở rộng/Thu hẹp (Expand and Contract Pattern), bảo đảm cả hai phiên bản Blue và Green đều đọc/ghi an toàn trên cùng một database mà không xung đột.\n"
        "     + Rủi ro phát hành cao: Blue-Green cho phép chạy toàn bộ các bài kiểm thử xác thực trên môi trường Green trước khi mở lưu lượng, và cung cấp khả năng Rollback tức thì (dưới 1 giây) chỉ bằng cách đổi cổng định tuyến nếu phát sinh sự cố nghiêm trọng.\n"
        "2. Thứ tự Các Cổng Kiểm duyệt (Verification Gates Pipeline):\n"
        "   - Cổng 1 (Staging & Internal Smoke Gate - Green Environment Isolation):\n"
        "     Triển khai phiên bản mới lên cụm Green. Đội ngũ kiểm thử gửi các yêu cầu nội bộ có gắn HTTP Header đặc biệt (`X-Target-Env: green`) để xác thực các luồng nghiệp vụ cốt lõi, kiểm tra kết nối CSDL và tải mô hình.\n"
        "   - Cổng 2 (Canary Traffic Shift Gate - 5% Production Traffic):\n"
        "     Định tuyến 5% lưu lượng người dùng thực sang cụm Green trong vòng 30 phút. Hệ thống giám sát tự động đánh giá: Tỷ lệ lỗi HTTP 5xx phải < 0.1%, độ trễ P99 không tăng quá 5% so với Blue, và không có cảnh báo ngoại lệ nghiêm trọng.\n"
        "   - Cổng 3 (Full Traffic Cutover Gate - 100% Traffic Shift):\n"
        "     Khi Cổng 2 đạt chuẩn, chuyển toàn bộ 100% lưu lượng người dùng sang Green. Cụm Blue được đưa về trạng thái chờ (Standby) và giữ nguyên vẹn trong 24 giờ.\n"
        "3. Kế hoạch và Quy trình Rollback Tức thì (Instant Rollback Plan):\n"
        "   - Nếu tại bất kỳ thời điểm nào sau cutover, hệ thống giám sát phát hiện tỷ lệ lỗi tăng đột biến hoặc vi phạm SLO: Kỹ sư hoặc hệ thống tự động kích hoạt Rollback chỉ bằng 1 lệnh chuyển đổi định tuyến tại API Gateway / DNS trỏ ngược lại 100% về cụm Blue.\n"
        "   - Thời gian khôi phục diễn ra tức thì (< 1 giây) mà không cần phải chờ đợi quá trình build hay redeploy container."
    ),
    "explanation": (
        "Chiến lược Blue-Green Deployment là tiêu chuẩn vàng cho các bản phát hành có độ rủi ro cao khi tài nguyên hạ tầng cho phép. Nhờ việc duy trì hai môi trường giống hệt nhau và cơ sở dữ liệu tương thích ngược, kỹ sư có thể triệt tiêu hoàn toàn thời gian chết (Zero Downtime) và sở hữu một nút bấm hoàn tác khẩn cấp (Emergency Rollback Switch) tức thời khi có sự cố phát sinh."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 5 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác chiến lược Blue-Green Deployment và biện minh thuyết phục dựa trên 3 điều kiện: tài nguyên đủ, schema tương thích, rủi ro cao.\n"
        "- [2.0 điểm] Thiết kế thứ tự 3 cổng kiểm duyệt chi tiết: Smoke test nội bộ -> Canary traffic shift 5% -> Full cutover 100% kèm chỉ số giám sát.\n"
        "- [2.0 điểm] Xây dựng kế hoạch Rollback tức thì (< 1s) tại tầng định tuyến mạng và bảo đảm an toàn dữ liệu nhờ schema tương thích ngược."
    ),
    "reference_source": "Martin Fowler - BlueGreenDeployment: https://martinfowler.com/bliki/BlueGreenDeployment.html và AWS Whitepaper - Overview of Deployment Methodologies"
}

# 45. d12-q097 (5 pts) - 5 POINTS
DAY12_PART2_A["d12-q097"] = {
    "sample_answer": (
        "1. Theo dõi Chuyển đổi Trạng thái của Circuit Breaker (State Machine Transitions):\n"
        "   - Bước 1 (CLOSED -> OPEN):\n"
        "     Ở trạng thái `CLOSED` ban đầu, mọi yêu cầu đều được chuyển tiếp tới dependency. Khi số lượng lỗi liên tiếp hoặc tỷ lệ lỗi vượt ngưỡng quy định (`failure_threshold`, ví dụ 5 lỗi 5xx trong 10s), Circuit Breaker lập tức chuyển trạng thái sang `OPEN`.\n"
        "   - Bước 2 (Duy trì Trạng thái OPEN):\n"
        "     Breaker giữ trạng thái `OPEN` trong suốt thời gian làm mát (`cooldown_duration`, ví dụ 30 giây). Bộ đếm thời gian bắt đầu chạy.\n"
        "   - Bước 3 (OPEN -> HALF-OPEN):\n"
        "     Khi hết thời gian cooldown 30 giây, Circuit Breaker tự động chuyển dịch trạng thái sang `HALF-OPEN` để thăm dò khả năng phục hồi của dependency.\n"
        "   - Bước 4 (HALF-OPEN -> CLOSED):\n"
        "     Ở trạng thái `HALF-OPEN`, một yêu cầu thăm dò (Trial Probe) được gửi đi và THÀNH CÔNG (nhận HTTP 200). Circuit Breaker ghi nhận tín hiệu lành mạnh, lập tức chuyển trạng thái trở lại `CLOSED` và reset toàn bộ bộ đếm lỗi về 0.\n"
        "2. Phân loại Trạng thái Thực thi hay Bị chặn của Từng Cuộc gọi (Invocation Flow):\n"
        "   - Các cuộc gọi đến trong giai đoạn trạng thái OPEN:\n"
        "     + Trạng thái: BỊ CHẶN HOÀN TOÀN TẠI CHỖ (Fail Fast / Blocked).\n"
        "     + Hành vi: Circuit Breaker không gửi bất kỳ gói tin mạng nào tới dependency, trả về ngay lập tức lỗi `CircuitBreakerOpenException` hoặc mã phản hồi `HTTP 503 Service Unavailable` chỉ trong < 1ms. Điều này bảo vệ dependency khỏi nguy cơ sụp đổ hoàn toàn và giải phóng tài nguyên cho ứng dụng gọi.\n"
        "   - Cuộc gọi Thăm dò (Probe Call) trong giai đoạn HALF-OPEN:\n"
        "     + Trạng thái: ĐƯỢC PHÉP THỰC THI (Allowed / Executed).\n"
        "     + Hành vi: Breaker mở cửa cho DUY NHẤT một yêu cầu này đi qua tới dependency để kiểm tra sức khỏe thực tế của dịch vụ hạ nguồn. Các yêu cầu khác đến đồng thời trong khoảnh khắc này tiếp tục bị giữ lại hoặc chặn.\n"
        "   - Các cuộc gọi tiếp theo sau khi Probe thành công:\n"
        "     + Trạng thái: ĐƯỢC PHÉP THỰC THI BÌNH THƯỜNG (Allowed / Full Flow).\n"
        "     + Hành vi: Do Breaker đã khôi phục hoàn toàn về trạng thái `CLOSED`, tất cả các yêu cầu tiếp theo đều được định tuyến thông suốt tới dependency như bình thường."
    ),
    "explanation": (
        "Mẫu thiết kế Ngắt mạch (Circuit Breaker Pattern) là cơ chế phòng thủ bắt buộc trong kiến trúc phân tán microservices và AI. Bằng cách fail-fast khi dịch vụ phụ thuộc bị lỗi và thăm dò thận trọng qua trạng thái Half-Open, mẫu thiết kế ngăn chặn hiện tượng lãng phí luồng xử lý (Thread Pool Exhaustion) và tạo không gian cho hệ thống hạ nguồn tự phục hồi sau sự cố quá tải."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 5 điểm):\n"
        "- [1.0 điểm] Mô tả chính xác và đầy đủ vòng đời chuyển trạng thái: CLOSED -> OPEN -> HALF-OPEN -> CLOSED.\n"
        "- [2.0 điểm] Phân tích chuẩn xác hành vi fail-fast của các cuộc gọi trong trạng thái OPEN (chặn tại chỗ, không gọi dependency, phản hồi < 1ms).\n"
        "- [2.0 điểm] Phân tích chuẩn xác hành vi của cuộc gọi probe trong HALF-OPEN và sự phục hồi thông suốt cho các cuộc gọi kế tiếp khi trở về CLOSED."
    ),
    "reference_source": "Martin Fowler - CircuitBreaker: https://martinfowler.com/bliki/CircuitBreaker.html và Release It! (Design and Deploy Production-Ready Software) by Michael T. Nygard"
}

# 46. d12-q099 (4 pts)
DAY12_PART2_A["d12-q099"] = {
    "sample_answer": (
        "1. Tính toán Độ trễ (Delay) và Lên lịch Attempt Tiếp theo:\n"
        "   - Phân tích bối cảnh: Dependency trả về mã lỗi `HTTP 429 Too Many Requests` kèm tiêu đề chỉ dẫn `Retry-After: 5` giây. Yêu cầu đang sử dụng phương thức GET (có tính Idempotent an toàn), thời hạn deadline tổng thể còn lại là 12 giây, số lần thử tối đa `max_attempts = 3`. Attempt 1 vừa thất bại.\n"
        "   - Tính toán Độ trễ Thực tế (Actual Delay Calculation):\n"
        "     + Tuân thủ chỉ dẫn của server: Thời gian chờ tối thiểu bắt buộc là 5.0 giây.\n"
        "     + Bổ sung độ trôi ngẫu nhiên (Full Jitter): Thêm một khoảng ngẫu nhiên nhỏ từ 0.1 đến 0.3 giây (ví dụ: `delay = 5.2` giây) nhằm ngăn ngừa tình trạng nhiều máy khách cùng bắn lại đồng thời (Thundering Herd Problem).\n"
        "   - Đánh giá Ngân sách Thời gian (Deadline Budget Check):\n"
        "     Thời gian cần thiết để chờ và gọi lại: `5.2s + latency ước tính (0.5s) = 5.7s < 12s` (vẫn còn dư ~6.3 giây). ĐỦ ĐIỀU KIỆN thực hiện Attempt 2.\n"
        "   - Lên lịch Attempt 2: Đưa vào hàng đợi ngủ (asynchronous sleep) 5.2 giây, sau đó phát Attempt 2 vào thời điểm T+5.2s.\n"
        "2. Cách Kết thúc khi Hết Thời gian hoặc Hết Số lần Thử:\n"
        "   - Kịch bản Thành công: Nếu Attempt 2 nhận `HTTP 200 OK`, dừng chuỗi retry và trả kết quả thành công ngay lập tức.\n"
        "   - Kịch bản Hết Số lần Thử (Attempts Exhaustion):\n"
        "     Nếu Attempt 2 thất bại và Attempt 3 tiếp tục nhận lỗi -> Đạt ngưỡng tối đa 3 lần thử (`attempt >= max_attempts`). NGỪNG RETRY NGAY LẬP TỨC. Trả về mã lỗi phản hồi cho client là `HTTP 502 Bad Gateway` hoặc chuyển tiếp `HTTP 429` kèm chi tiết lỗi.\n"
        "   - Kịch bản Hết Hạn Ngạch Thời gian (Deadline / Timeout Exhaustion):\n"
        "     Nếu tại bất kỳ thời điểm nào trước khi thử lại, thời gian còn lại đến deadline nhỏ hơn thời gian `Retry-After` (ví dụ: còn 3s mà server bắt chờ 5s): NGỪNG RETRY NGAY LẬP TỨC (Short-Circuit Deadline Cancellation). Trả về mã lỗi `HTTP 504 Gateway Timeout` kèm thông điệp rõ ràng: 'Không thể hoàn tất yêu cầu trong thời hạn deadline cam kết'."
    ),
    "explanation": (
        "Chiến lược thử lại thông minh (Smart Retry Strategy) yêu cầu sự phối hợp chặt chẽ giữa việc tôn trọng tín hiệu điều tiết của hạ nguồn (`Retry-After`), bổ sung Jitter ngẫu nhiên và kiểm soát chặt chẽ ngân sách thời gian toàn cục (Global Deadline Budget). Ngắn mạch sớm khi phát hiện không còn đủ thời gian giúp tiết kiệm điện toán và tránh gây tải vô ích cho hệ thống."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Xác định chính xác độ trễ chờ là 5s (dựa trên header Retry-After) và bổ sung Jitter ngẫu nhiên ngăn ngừa thundering herd.\n"
        "- [1.5 điểm] Đánh giá ngân sách thời gian so với deadline 12s và lên lịch thực thi Attempt 2 an toàn tại T+5.2s.\n"
        "- [1.5 điểm] Xử lý kết thúc chuẩn xác cho cả hai trường hợp: hết số lần thử max 3 (HTTP 502/429) và hết deadline thời gian (ngắn mạch HTTP 504)."
    ),
    "reference_source": "RFC 6585 (Additional HTTP Status Codes - Section 4: 429 Too Many Requests) & AWS Architecture Blog - Exponential Backoff And Jitter"
}

# 47. d12-q102 (4 pts)
DAY12_PART2_A["d12-q102"] = {
    "sample_answer": (
        "1. Thiết kế Ngân sách Độ trễ (Latency Budgets) và Phân vùng Bulkhead (Bulkhead Isolation):\n"
        "   - Phân tích: Đồ thị cuộc gọi gồm 3 thành phần có đặc tính độ trễ hoàn toàn khác biệt: Payment (thao tác tài chính quan trọng), Model/LLM (sinh token độ trễ cao) và Search (tra cứu thông tin mở rộng).\n"
        "   - Thiết lập Latency Budget và Timeout độc lập cho từng dịch vụ:\n"
        "     + Dịch vụ Payment (Nghiệp vụ Trọng yếu - Zero Tolerance): Timeout ngắn và dứt khoát: `timeout = 3.0` giây. Phân vùng Bulkhead riêng với Worker Pool độc lập (ví dụ: 10 dedicated connections).\n"
        "     + Dịch vụ Model/LLM (Tác vụ Tính toán Nặng): Timeout dài: `timeout = 15.0` giây để cho phép mô hình sinh xong các đoạn văn bản dài. Phân vùng Bulkhead riêng biệt (ví dụ: 25 dedicated async workers).\n"
        "     + Dịch vụ Search (Tra cứu Mở rộng - Non-Critical): Timeout ngắn: `timeout = 1.5` giây. Phân vùng Bulkhead riêng biệt (ví dụ: 15 dedicated HTTP client sockets).\n"
        "   - Nguyên tắc Bulkhead: Phân tách rạch ròi Connection Pools, Thread Pools và Memory Queues giữa 3 dịch vụ; sự cố cạn kiệt tài nguyên ở dịch vụ này tuyệt đối không thể lây nhiễm làm nghẽn dịch vụ khác.\n"
        "2. Dự đoán Khả năng Phục vụ của Các Workload khi Xảy ra Sự cố (Fault Isolation Prediction):\n"
        "   - Tình huống Dịch vụ Search bị Nghẽn hoặc Sập Hoàn toàn (Search Latency tăng vọt lên 30s hoặc Timeout 100%):\n"
        "     + Nhờ Timeout 1.5s, các yêu cầu Search bị ngắt mạch nhanh chóng (Fail-Fast).\n"
        "     + Do Search nằm trong Bulkhead riêng, nó KHÔNG HỀ chiếm dụng bất kỳ connection nào của Payment hay Model.\n"
        "     + Workload VẪN PHỤC VỤ HOÀN TOÀN BÌNH THƯỜNG: Hệ thống kích hoạt cơ chế Suy giảm Duyên dáng (Graceful Degradation): Luồng thanh toán Payment vẫn thực hiện trơn tru 100%, luồng chat Model vẫn trả về câu trả lời cho người dùng (chỉ thiếu phần trích dẫn từ kết quả search).\n"
        "   - Tình huống Dịch vụ Model bị Nghẽn: Workload Payment độc lập vẫn tiếp tục xử lý các giao dịch thanh toán bình thường mà không bị ảnh hưởng dây chuyền."
    ),
    "explanation": (
        "Mẫu thiết kế Vách ngăn Kín nước (Bulkhead Pattern) lấy cảm hứng từ cấu trúc phân khoang của thân tàu thủy nhằm ngăn một khoang bị thủng làm chìm toàn bộ con tàu. Bằng cách gán ngân sách độ trễ riêng và phân bổ tài nguyên độc lập cho từng thành phần trong đồ thị cuộc gọi, hệ thống bảo vệ toàn vẹn các chức năng sống còn (như Payment) ngay cả khi các dịch vụ phụ trợ gặp sự cố nghiêm trọng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết lập ngân sách độ trễ (Latency Budget) và Timeout chuẩn xác cho cả 3 thành phần: Payment (3s), Model (15s), Search (1.5s).\n"
        "- [1.5 điểm] Thiết kế phân vùng Bulkhead cách ly hoàn toàn tài nguyên (Connection Pools / Thread Pools) giữa 3 dịch vụ.\n"
        "- [1.5 điểm] Dự đoán chuẩn xác khả năng phục vụ khi có sự cố: Search sập thì Payment và Model vẫn phục vụ trơn tru ở chế độ degraded mode."
    ),
    "reference_source": "Michael T. Nygard - Release It! (Bulkheads Pattern) & Microsoft Azure Architecture Patterns - Bulkhead Pattern"
}

# 48. d12-q104 (4 pts)
DAY12_PART2_A["d12-q104"] = {
    "sample_answer": (
        "1. Phân biệt Mục tiêu Nội bộ (SLO) với Cam kết Pháp lý Bên ngoài (SLA):\n"
        "   - SLI Thực tế Đo lường được (Service Level Indicator):\n"
        "     Trong 10.000 yêu cầu hợp lệ, có 9.950 yêu cầu đạt độ trễ $\\le 2$ giây.\n"
        "     `SLI = (9.950 / 10.000) * 100% = 99.50%`.\n"
        "   - Mục tiêu Nội bộ (Internal SLO = 99.70%):\n"
        "     Là mục tiêu kỹ thuật phấn đấu do đội ngũ kỹ thuật nội bộ tự đặt ra để đảm bảo chất lượng dịch vụ cao nhất và tạo biên độ đệm an toàn. Mục tiêu này KHÔNG đi kèm mức phạt tài chính, mà là kim chỉ nam để điều tiết tốc độ phát triển tính năng.\n"
        "   - Cam kết Bên ngoài (External SLA = 99.00%):\n"
        "     Là điều khoản cam kết dịch vụ mang tính pháp lý trong hợp đồng với khách hàng. Nếu SLI thực tế rơi xuống dưới mức 99.00%, doanh nghiệp phải chịu trách nhiệm bồi thường tài chính (Service Credits / Penalty). Mức SLA luôn được đặt thấp hơn SLO để tạo khoảng đệm an toàn bảo vệ doanh nghiệp.\n"
        "2. Đánh giá Trạng thái Tuân thủ và Tính toán Ngân sách Lỗi (Error Budget Calculation):\n"
        "   - Đánh giá Cam kết SLA Khách hàng:\n"
        "     `SLI Thực tế (99.50%) > SLA Cam kết (99.00%)`.\n"
        "     -> Kết luận: DOANH NGHIỆP TUÂN THỦ HOÀN TOÀN CAM KẾT SLA, KHÔNG BỊ PHẠT HỢP ĐỒNG.\n"
        "   - Đánh giá Mục tiêu Nội bộ SLO và Tính toán Error Budget:\n"
        "     `SLI Thực tế (99.50%) < SLO Nội bộ (99.70%)`.\n"
        "     -> Kết luận: VI PHẠM MỤC TIÊU NỘI BỘ, ĐÃ ĐỐT CHÁY QUÁ NGÂN SÁCH LỖI CHO PHÉP.\n"
        "     + Tổng số yêu cầu lỗi tối đa cho phép theo SLO (99.7%): `10.000 * (1 - 0.997) = 30` yêu cầu.\n"
        "     + Số lượng yêu cầu vi phạm độ trễ thực tế: `10.000 - 9.950 = 50` yêu cầu.\n"
        "     + Tỷ lệ đốt ngân sách lỗi (Error Budget Burn):\n"
        "       `Burn Rate = 50 / 30 = 166.67%`.\n"
        "     + Trạng thái Ngân sách Lỗi: BỊ ÂM HOÀN TOÀN (Vượt quá ngân sách lỗi cho phép 20 yêu cầu, tức âm 66.67% ngân sách).\n"
        "   - Hành động Quản trị Kỹ thuật (SRE Policy Action):\n"
        "     Kích hoạt chính sách đóng băng triển khai tính năng mới (Feature Freeze). Đội ngũ kỹ thuật chuyển 100% trọng tâm sang việc tối ưu hóa hiệu năng, giảm độ trễ P95/P99 để bù đắp lại ngân sách lỗi trong chu kỳ tiếp theo."
    ),
    "explanation": (
        "Trong phương pháp luận SRE, việc phân định ranh giới giữa SLA pháp lý và SLO nội bộ là công cụ quản trị rủi ro tối quan trọng. SLO khắt khe hơn SLA tạo ra một khoảng đệm an toàn giúp đội ngũ kỹ thuật chủ động phát hiện sự suy giảm chất lượng và hành động trước khi hệ thống chạm ngưỡng vi phạm hợp đồng phải bồi thường thiệt hại."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân biệt rõ ràng giữa SLO nội bộ (99.7% không phạt) và SLA bên ngoài (99.0% cam kết pháp lý kèm mức phạt).\n"
        "- [1.5 điểm] Tính toán chính xác SLI thực tế đạt 99.50% và khẳng định tuân thủ thành công SLA (không bị phạt hợp đồng).\n"
        "- [1.5 điểm] Tính toán chính xác trạng thái Error Budget bị âm (cho phép 30 lỗi, thực tế 50 lỗi, burn 166.7%) và nêu hành động đóng băng tính năng."
    ),
    "reference_source": "Google Site Reliability Engineering (SRE) Book - Service Level Objectives: https://sre.google/sre-book/service-level-objectives/ và The Site Reliability Workbook"
}

print("Loaded Day 12 Part 2 Sub-part A (questions 37 to 48).")
