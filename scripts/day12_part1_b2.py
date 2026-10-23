# scripts/day12_part1_b2.py
# -*- coding: utf-8 -*-
"""
Day 12 Part 1 Questions 24 to 36 (d12-q050 to d12-q077)
"""

DAY12_PART1_B2 = {}

# 24. d12-q050 (4 pts)
DAY12_PART1_B2["d12-q050"] = {
    "sample_answer": (
        "1. Thiết kế lại Đường đi Yêu cầu qua Kiến trúc BFF (Backend-for-Frontend):\n"
        "   - Vấn đề: SPA chạy trên trình duyệt máy khách là môi trường hoàn toàn không tin cậy. Nếu SPA gọi trực tiếp Model Provider, API Key bí mật sẽ bị lộ qua Network DevTools, đồng thời không thể kiểm soát hạn ngạch (quota) và phạm vi quyền (scope) của từng người dùng riêng lẻ.\n"
        "   - Luồng kiến trúc mới:\n"
        "     `SPA Client` --(1. HTTP + User Short-Lived JWT)--> `BFF Gateway` --(2. Policy Enforcement & Secret Injection)--> `Model Provider API`\n"
        "   - Quy trình xử lý tại BFF:\n"
        "     + Bước 1: BFF xác thực tính hợp lệ của User JWT (kiểm tra chữ ký số, issuer, expiration, user_id, tenant_id).\n"
        "     + Bước 2: Kiểm tra Scope & Quyền hạn (Scope Validation): Xác nhận user có quyền truy cập model yêu cầu hay không (ví dụ: scope `model:query` hay `model:fine_tune`).\n"
        "     + Bước 3: Kiểm tra và Trừ Quota Cá nhân: Tra cứu số dư token/request trong Redis. Nếu đã cạn kiệt, từ chối ngay lập tức.\n"
        "     + Bước 4: Tiêm Bí mật Nhà cung cấp (Provider Secret Injection): Lấy Model API Key từ Cloud Secret Manager/KMS và đính kèm vào header cuộc gọi ngược dòng tới Model Provider.\n"
        "     + Bước 5: Kiểm duyệt nội dung phản hồi (Response Moderation) và stream dữ liệu về SPA.\n"
        "2. Thiết kế Bộ kiểm thử Boundary và Phân lập Bí mật:\n"
        "   - Test 1 (Client Secret Isolation Test): Phân tích toàn bộ mã nguồn JavaScript bundle và network traffic của SPA; khẳng định Provider API Key hoàn toàn không xuất hiện ở phía client.\n"
        "   - Test 2 (Scope Enforcement Test): Gửi request với User JWT có scope `model:basic` nhưng gọi endpoint yêu cầu model nâng cao; BFF phải từ chối với `HTTP 403 Forbidden` trước khi bất kỳ cuộc gọi provider nào diễn ra.\n"
        "   - Test 3 (Quota Exhaustion Test): Gửi request khi người dùng đã tiêu thụ 100% hạn ngạch ngày; BFF trả về `HTTP 429 Too Many Requests`, và số lượng cuộc gọi tới Provider API tăng đúng 0 (zero provider call).\n"
        "   - Test 4 (Invalid/Expired Token Test): Gửi request không có token hoặc token giả mạo; BFF trả về `HTTP 401 Unauthorized`."
    ),
    "explanation": (
        "Mẫu thiết kế Backend-for-Frontend (BFF Pattern) là ranh giới bảo mật bắt buộc khi kết nối các ứng dụng máy khách công khai (như SPA hoặc Mobile App) với các dịch vụ AI đám mây. BFF chịu trách nhiệm chuyển đổi danh tính người dùng (User Identity) thành quyền truy cập tài nguyên, bảo vệ bí mật dịch vụ tuyệt đối phía máy chủ và thực thi các chính sách phân quyền và hạn ngạch chi tiết."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích điểm yếu của kiến trúc SPA gọi trực tiếp và thiết kế lại luồng qua BFF Gateway an toàn.\n"
        "- [1.5 điểm] Mô tả đầy đủ quy trình xử lý tại BFF: xác thực User JWT, phân quyền scope, kiểm tra quota người dùng và tiêm secret.\n"
        "- [1.5 điểm] Xây dựng bộ kiểm thử boundary toàn diện: chống rò rỉ secret, chặn sai scope (403), chặn hết quota (429 với 0 provider call) và lỗi auth (401)."
    ),
    "reference_source": "OWASP API Security Top 10 (Broken Object Level Authorization) & Sam Newman - Building Microservices (BFF Pattern)"
}

# 25. d12-q053 (4 pts)
DAY12_PART1_B2["d12-q053"] = {
    "sample_answer": (
        "1. Thiết kế Cơ chế Routing và Phát hiện Mất Mạng (Network Loss Detection):\n"
        "   - Khi thiết bị đang thực thi một tác vụ đã được người dùng đồng thuận (consent) gửi lên cloud nhưng phát hiện mất kết nối mạng (Socket Timeout / TCP RST):\n"
        "   - Bộ điều phối tác vụ (Task Orchestrator) ngay lập tức đóng băng tiến trình, kiểm tra Ma trận Yêu cầu Năng lực Tác vụ (Task Capability Requirements Matrix):\n"
        "     + Tác vụ Phù hợp: Yêu cầu tóm tắt ngắn (Short Summary) nằm trong khả năng hỗ trợ của mô hình cục bộ (Local Model).\n"
        "     + Tác vụ Vượt ngưỡng: Yêu cầu phân tích sâu, suy luận logic phức tạp hoặc gọi công cụ doanh nghiệp vượt ngoài năng lực mô hình cục bộ.\n"
        "2. Thiết kế Phương án Dự phòng Cục bộ (Local Fallback Execution):\n"
        "   - Đối với tác vụ tóm tắt ngắn: Chuyển hướng luồng dữ liệu (route fallback) sang mô hình AI cục bộ trên thiết bị.\n"
        "   - Thực thi sinh kết quả tóm tắt cục bộ với độ trễ thấp và đính kèm nhãn minh bạch trong giao diện người dùng:\n"
        "     *\"Chế độ Ngoại tuyến: Bản tóm tắt nhanh được tạo bởi mô hình cục bộ do kết nối đám mây bị gián đoạn.\"*\n"
        "3. Thiết kế Cơ chế Leo thang và Hàng đợi Ngoại tuyến (Escalation & Offline Queueing):\n"
        "   - Đối với các tác vụ phức tạp vượt ngoài năng lực cục bộ: TUYỆT ĐỐI KHÔNG ép mô hình cục bộ chạy để tránh sinh ra thông tin ảo giác (hallucination) nguy hiểm.\n"
        "   - Đưa tác vụ vào Hàng đợi Ngoại tuyến Bền vững (Offline Persistent Queue) với trạng thái `QUEUED_OFFLINE`.\n"
        "   - Kích hoạt thông báo xin ý kiến người dùng (Escalation Dialog):\n"
        "     *\"Tác vụ phân tích chuyên sâu cần kết nối đám mây để hoàn tất. Bạn có muốn lưu tác vụ vào hàng đợi để tự động thực thi khi có mạng trở lại hay hủy bỏ?\"*\n"
        "   - Khi mạng phục hồi, background sync worker tự động gửi tác vụ lên cloud mà không làm mất trạng thái phiên."
    ),
    "explanation": (
        "Chiến lược thiết kế hệ thống AI hoạt động theo nguyên lý 'Chấp nhận suy giảm duyên dáng' (Graceful Degradation). Khi gặp sự cố mất mạng, việc nhận diện chính xác giới hạn năng lực của mô hình cục bộ giúp hệ thống linh hoạt chuyển sang fallback cho tác vụ đơn giản, đồng thời kích hoạt hàng đợi đồng bộ và xin chỉ đạo từ người dùng đối với các tác vụ phức tạp, bảo đảm tính toàn vẹn của kết quả suy luận."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế cơ chế phát hiện ngắt mạng và phân loại tác vụ dựa trên ma trận năng lực của mô hình cục bộ.\n"
        "- [1.5 điểm] Xây dựng luồng Local Fallback an toàn cho tác vụ tóm tắt ngắn kèm thông báo giao diện minh bạch.\n"
        "- [1.5 điểm] Thiết kế cơ chế Escalation và Hàng đợi ngoại tuyến bền vững cho tác vụ phức tạp, xin ý kiến người dùng và đồng bộ khi có mạng."
    ),
    "reference_source": "Offline-First Software Architecture Principles & Google People + AI Guidebook (Handling Errors and Graceful Degradation)"
}

# 26. d12-q055 (3 pts) - 3 POINTS
DAY12_PART1_B2["d12-q055"] = {
    "sample_answer": (
        "1. Lựa chọn Runtime Tier Phù hợp Nhất:\n"
        "   - Lựa chọn: Serverless Container Platform / Container-as-a-Service (ví dụ: Google Cloud Run hoặc AWS ECS Fargate / Azure Container Apps).\n"
        "   - Biện minh quyết định:\n"
        "     + Đặc thù workload: Tác vụ HTTP hoàn toàn stateless và thời gian chạy ngắn (2 giây) là môi trường lý tưởng nhất cho Serverless Container.\n"
        "     + Traffic bursty: Serverless container cung cấp khả năng tự động co giãn cực nhanh từ mức thấp lên hàng chục container trong vài giây để đáp ứng lưu lượng tăng đột biến mà không cần dự phòng lãng phí.\n"
        "     + Quy mô đội ngũ nhỏ (Small team): Không có nguồn lực vận hành cụm Kubernetes phức tạp (No K8s cluster management overhead, không phải vá lỗi node OS hay quản lý control plane).\n"
        "2. Các Thông tin Thực tế Cần Xác minh tại Thời điểm Quyết định:\n"
        "   - Độ trễ Khởi động nguội (Cold Start Latency): Đo đạc thực tế P95/P99 cold start của container image khi co giãn từ 0 để đảm bảo không làm đứt gãy trải nghiệm người dùng.\n"
        "   - Biểu giá và Định mức Hiện hành (Current Pricing & Limits): Kiểm tra đơn giá tính trên vCPU-giây và GiB-giây, định mức miễn phí hàng tháng (Free Tier), và chi phí concurrency per container tại thời điểm triển khai.\n"
        "   - Giới hạn Cứng của Nền tảng (Platform Hard Quotas): Xác minh giới hạn thời gian chạy tối đa (request timeout), số kết nối đồng thời tối đa trên mỗi container instance (concurrency limit) và băng thông mạng ra (egress bandwidth).\n"
        "   - Chi phí Kết nối Mạng Nội bộ (VPC Egress Pricing): Xác minh chi phí và độ trễ của Serverless VPC Connector khi cần kết nối tới cơ sở dữ liệu nội bộ."
    ),
    "explanation": (
        "Đối với các nhóm phát triển tinh gọn có khối lượng công việc phi trạng thái thời lượng ngắn và lưu lượng biến động mạnh, việc lựa chọn nền tảng Serverless Container giúp tối đa hóa hiệu quả kinh tế và giải phóng hoàn toàn gánh nặng vận hành hạ tầng. Tuy nhiên, kỹ sư phải chủ động xác minh các thông số định lượng thực tế như cold start và bảng giá hiện hành tại thời điểm đưa ra quyết định kiến trúc."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
        "- [1.0 điểm] Lựa chọn chuẩn xác runtime tier là Serverless Container (Cloud Run / AWS Fargate) và biện minh thuyết phục theo 3 yếu tố: stateless 2s, bursty traffic, small team.\n"
        "- [1.0 điểm] Nêu các chỉ số kỹ thuật thực tế cần đo đạc: Cold start latency P95/P99 và giới hạn cứng (timeout, max concurrency per instance).\n"
        "- [1.0 điểm] Xác minh các thông tin tài chính và mạng thực tế tại thời điểm triển khai: biểu giá hiện hành vCPU-s/RAM-s và chi phí VPC Egress."
    ),
    "reference_source": "CNCF Serverless Whitepaper & Google Cloud Run Architecture Guidelines: https://cloud.google.com/run/docs/about-instance-autoscaling"
}

# 27. d12-q057 (4 pts)
DAY12_PART1_B2["d12-q057"] = {
    "sample_answer": (
        "1. Lựa chọn Mô hình Triển khai: Self-Deployed / Customer-Managed Kubernetes trên Chuẩn Mở:\n"
        "   - Lựa chọn: Tự triển khai cụm Kubernetes (Self-Managed Kubernetes / EKS Anywhere / OpenShift) trên hạ tầng private cloud hoặc dedicated compute.\n"
        "   - Biện minh đối chiếu với các ràng buộc doanh nghiệp:\n"
        "     + Private Network: Đáp ứng yêu cầu cô lập mạng riêng biệt hoàn toàn (air-gapped VPC hoặc private data center), kiểm soát 100% firewall và định tuyến.\n"
        "     + Tùy biến Observability: Cho phép cài đặt các OpenTelemetry Collectors, eBPF probes chuyên sâu, Prometheus và lưu trữ telemetry nội bộ theo quy định bảo mật riêng của doanh nghiệp.\n"
        "     + Portability nghiêm ngặt: Tránh hoàn toàn việc phụ thuộc vào các dịch vụ độc quyền (Vendor Lock-in); ứng dụng đóng gói theo chuẩn OCI và Helm Chart có thể mang sang bất kỳ hạ tầng nào.\n"
        "     + Nguồn lực SRE: Doanh nghiệp đã sở hữu đội ngũ SRE chuyên trách có đầy đủ năng lực vận hành, vá lỗi và duy trì hạ tầng 24/7.\n"
        "2. Bản đồ Phân chia Trách nhiệm (Shared Responsibility Matrix):\n"
        "   - Trách nhiệm của Nhà cung cấp Hạ tầng (Infrastructure / IaaS Provider):\n"
        "     + Bảo đảm phần cứng máy chủ vật lý, nguồn điện, làm mát, an ninh trung tâm dữ liệu và ảo hóa cấp thấp (Hypervisor/Bare-metal).\n"
        "   - Trách nhiệm của Đội ngũ Doanh nghiệp / SRE Team:\n"
        "     + Cài đặt, nâng cấp phiên bản và quản trị Control Plane Kubernetes (etcd, API server, controller manager).\n"
        "     + Cấu hình CNI mạng riêng (Cilium/Calico), mạng nội bộ và các chính sách Network Policy bảo vệ pod-to-pod.\n"
        "     + Thiết lập và vận hành toàn bộ hệ thống Observability tùy chỉnh (Prometheus, Grafana, Jaeger, Loki).\n"
        "     + Chịu trách nhiệm sao lưu định kỳ (etcd backup), phục hồi thảm họa (Disaster Recovery) và vá lỗi hệ điều hành node OS.\n"
        "3. Điều kiện và Chiến lược Rời Nền tảng (Exit Strategy & Offboarding):\n"
        "   - Điều kiện rời bỏ: Chi phí hạ tầng vượt ngân sách quá 25%, thay đổi chính sách chủ quyền dữ liệu, hoặc nhà cung cấp không đáp ứng cam kết SLA mạng.\n"
        "   - Chiến lược thực thi: 100% tài nguyên hạ tầng được định nghĩa bằng Infrastructure as Code (Terraform/OpenTofu) và GitOps (ArgoCD). Khi cần di dời, chỉ cần áp dụng Helm Charts sang cluster mới mà không phải sửa đổi bất kỳ dòng mã nguồn ứng dụng nào trong vòng 24 giờ."
    ),
    "explanation": (
        "Quyết định giữa Managed Services và Self-Deployed phụ thuộc vào sự cân bằng giữa tính linh hoạt, tuân thủ quy định và chi phí vận hành con người. Đối với doanh nghiệp có đội ngũ SRE chuyên sâu và yêu cầu kiểm soát mạng riêng biệt nghiêm ngặt, mô hình Self-Deployed chuẩn mở bảo đảm quyền tự chủ tuyệt đối về dữ liệu và khả năng di chuyển linh hoạt giữa các nhà cung cấp đám mây."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chuẩn xác mô hình Self-Deployed trên nền Kubernetes chuẩn mở và biện minh dựa trên 4 ràng buộc của bài toán.\n"
        "- [1.5 điểm] Xây dựng bản đồ phân chia trách nhiệm (Shared Responsibility Matrix) chi tiết giữa IaaS Provider và đội ngũ SRE nội bộ.\n"
        "- [1.5 điểm] Thiết lập chiến lược rời nền tảng (Exit Strategy) toàn diện dựa trên IaC chuẩn mở và quy trình di dời GitOps trong 24h."
    ),
    "reference_source": "CNCF Cloud Native Exit Strategy Guide & NIST SP 800-145 (Cloud Computing Shared Responsibility)"
}

# 28. d12-q059 (4 pts)
DAY12_PART1_B2["d12-q059"] = {
    "sample_answer": (
        "1. Thiết lập Chuỗi Kiểm chứng 4 Bước Tuần tự (4-Stage Verification Chain):\n"
        "   - Bước 1 (Runtime Secret Injection & Sanitization Verification):\n"
        "     + Thao tác: Kiểm tra biến môi trường `DATABASE_URL` đã được tiêm từ Secret Manager vào runtime context.\n"
        "     + Bằng chứng an toàn: Lệnh kiểm tra in ra thông số kết nối nhưng MẬT KHẨU PHẢI ĐƯỢC CHE GIẤU (Redacted/Masked), ví dụ: `postgresql://db_user:********@db.internal:5432/production_db`. Khẳng định tuyệt đối không có mật khẩu dạng plain-text xuất hiện trong log kiểm tra.\n"
        "   - Bước 2 (Assigned Port Binding Verification):\n"
        "     + Thao tác: Kiểm tra ứng dụng đã lắng nghe thành công trên cổng được cấp phát động (Dynamic Assigned Port, ví dụ `PORT=8080`).\n"
        "     + Bằng chứng an toàn: Lệnh `netstat -tlpn` hoặc log khởi động máy chủ ghi nhận `Application successfully bound to 0.0.0.0:8080` kèm exit code 0.\n"
        "   - Bước 3 (Readiness Deep Health Check Verification):\n"
        "     + Thao tác: Gửi HTTP GET nội bộ tới endpoint `/health` kiểm tra kết nối cơ sở dữ liệu thực tế.\n"
        "     + Bằng chứng an toàn: Lệnh `curl -s -i http://localhost:8080/health` trả về `HTTP/1.1 200 OK` với thân JSON `{\"status\": \"healthy\", \"database\": \"connected\", \"latency_ms\": 2.4}`.\n"
        "   - Bước 4 (Public API Authentication Verification):\n"
        "     + Negative Test: Gửi yêu cầu công khai không có header xác thực `curl -i http://localhost:8080/api/v1/agent` -> Nhận `HTTP/1.1 401 Unauthorized`.\n"
        "     + Positive Test: Gửi yêu cầu kèm Bearer JWT hợp lệ `curl -i -H 'Authorization: Bearer <token>' http://localhost:8080/api/v1/agent` -> Nhận `HTTP/1.1 200 OK`.\n"
        "     + Bằng chứng an toàn: Trong log kiểm tra, token được cắt ngắn hoặc hash (`Bearer eyJhbGci...***`), không để lộ toàn bộ payload nhạy cảm."
    ),
    "explanation": (
        "Quy trình kiểm chứng tính sẵn sàng triển khai (Deployment Readiness Verification) yêu cầu sự chặt chẽ từ tầng cấu hình hạ tầng đến bảo mật ứng dụng. Nguyên tắc tối thượng của chuỗi kiểm chứng là đảm bảo tính chính xác chức năng mà không bao giờ làm rò rỉ bí mật runtime hay thông tin xác thực ra hệ thống nhật ký kiểm toán (Zero-Leak Audit Logging)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết lập chuỗi kiểm chứng logic 4 bước: Secret Injection -> Port Binding -> Deep Health -> API Auth.\n"
        "- [1.5 điểm] Bảo đảm tiêu chuẩn bằng chứng an toàn tuyệt đối: che giấu mật khẩu DB URL (masking) và hash token xác thực.\n"
        "- [1.5 điểm] Thiết kế đầy đủ positive/negative test cho API auth và kiểm chứng phản hồi HTTP 200 lành mạnh từ endpoint /health."
    ),
    "reference_source": "CIS Controls - Security Configuration Management & OWASP Logging and Monitoring Cheat Sheet"
}

# 29. d12-q062 (4 pts)
DAY12_PART1_B2["d12-q062"] = {
    "sample_answer": (
        "1. Thiết kế Hosting Boundary (Remote HTTP Transport & Tenant Isolation):\n"
        "   - Chuyển đổi Giao thức: Thay thế cơ chế stdio đơn tiến trình bằng Remote HTTP Transport (kết hợp Server-Sent Events cho truyền phát dữ liệu và HTTP POST cho gọi công cụ qua mã hóa TLS 1.3).\n"
        "   - Hosting Architecture: MCP Server được triển khai dưới dạng dịch vụ đám mây tập trung trong Private VPC, đứng sau Cloud API Gateway đóng vai trò Ingress Controller.\n"
        "   - Phân lập Phiên (Session Context Boundary): Mỗi kết nối client được gán một `SessionContext` độc lập trong bộ nhớ hoặc Redis; tuyệt đối không sử dụng biến tĩnh/toàn cục (global state) để tránh rò rỉ dữ liệu giữa các tenant.\n"
        "2. Thiết kế Xác thực và Truy cập Người dùng Ủy quyền (Authentication & Delegated Access):\n"
        "   - Chuẩn Xác thực: Áp dụng OAuth 2.0 Token Exchange (RFC 8693) hoặc JSON Web Tokens (JWT) do Identity Provider (IdP) doanh nghiệp ký duyệt.\n"
        "   - Cấu trúc Claim Ủy quyền Bắt buộc trong Token:\n"
        "     + `sub`: Định danh người dùng cuối được ủy quyền (ví dụ `user_9876`).\n"
        "     + `tenant_id`: Định danh tổ chức sở hữu tài nguyên (ví dụ `tenant_alpha`).\n"
        "     + `scope`: Phạm vi công cụ MCP được phép gọi (ví dụ `mcp:tools:read mcp:tools:execute`).\n"
        "3. Thiết kế Ranh giới Khán giả Tài nguyên (Resource-Audience Boundary):\n"
        "   - Xác thực Claim Khán giả (`aud` - Audience):\n"
        "     + MCP Server bắt buộc phải kiểm tra claim `aud == https://mcp.enterprise.internal/tools`.\n"
        "     + Nếu client mang token có audience của một dịch vụ khác (ví dụ `https://api.model-provider.com`), MCP Server phải từ chối ngay lập tức với `HTTP 403 Forbidden` nhằm ngăn chặn tấn công giả mạo quyền ủy quyền (Confused Deputy Attack).\n"
        "   - Ngăn chặn Tenant-Hopping: Toàn bộ truy vấn dữ liệu từ các tool bên dưới bắt buộc phải tiêm điều kiện lọc `WHERE tenant_id = token.tenant_id` lấy từ token đã xác thực, cấm tin tưởng tenant_id gửi tự do từ request body."
    ),
    "explanation": (
        "Khi đưa Model Context Protocol (MCP) từ môi trường máy trạm đơn lẻ lên dịch vụ đám mây chia sẻ đa người thuê (Multi-Tenant Remote MCP), ranh giới bảo mật chuyển dịch từ mức tiến trình hệ điều hành sang mức giao thức mạng. Việc kết hợp xác thực đại diện người dùng (Delegated Access) và kiểm tra nghiêm ngặt Audience token bảo đảm tính toàn vẹn dữ liệu và ngăn chặn hoàn toàn việc truy cập trái phép giữa các tổ chức."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế Remote HTTP Transport cho MCP thay thế stdio và kiến trúc hosting phân lập phiên độc lập.\n"
        "- [1.5 điểm] Xây dựng cơ chế Delegated Access với OAuth 2.0 / JWT mang đầy đủ các claims: sub, tenant_id, scopes.\n"
        "- [1.5 điểm] Thiết lập chặt chẽ Resource-Audience boundary kiểm tra claim `aud` chống Confused Deputy và cô lập dữ liệu chống tenant-hopping."
    ),
    "reference_source": "Model Context Protocol Specification - Remote Transports: https://modelcontextprotocol.io/ và RFC 8693 (OAuth 2.0 Token Exchange)"
}

# 30. d12-q064 (4 pts)
DAY12_PART1_B2["d12-q064"] = {
    "sample_answer": (
        "1. Sắp xếp Luồng Kiểm duyệt Thất bại Sớm (Fail-Fast Gate Pipeline - Thứ tự Chi phí Tăng dần):\n"
        "   - Cổng 1 (Schema & Body Validation Gate - Chi phí ~0.0001 ms CPU):\n"
        "     Kiểm tra cú pháp JSON, tính đầy đủ của các trường bắt buộc và định dạng payload. Nếu thân sai định dạng -> Từ chối ngay với `HTTP 400 Bad Request`.\n"
        "   - Cổng 2 (Authentication & Signature Verification Gate - Chi phí ~0.1 ms CPU):\n"
        "     Kiểm tra header Authorization, giải mã và xác thực chữ ký JWT. Nếu thiếu hoặc sai token -> Từ chối ngay với `HTTP 401 Unauthorized`.\n"
        "   - Cổng 3 (Rate Limiting & Tier Quota Gate - Chi phí ~1 ms Redis I/O):\n"
        "     Tra cứu số lượng yêu cầu trong cửa sổ thời gian của tenant trong Redis. Nếu đã hết hạn mức tốc độ -> Từ chối ngay với `HTTP 429 Too Many Requests`.\n"
        "   - Cổng 4 (Budget & Cost Pre-Check Gate - Chi phí ~2 ms Tokenizer calculation):\n"
        "     Đếm số lượng token đầu vào (prompt tokens) và ước tính trần chi phí tối đa của request. Nếu vượt quá ngân sách còn lại của tenant -> Từ chối ngay với `HTTP 402 Payment Required` hoặc `403 Forbidden`.\n"
        "   - Cổng Cuối (Model Execution & Paid Tool Invocations - Chi phí Cực Đắt: Tốn USD thực tế và 1-20 giây tính toán):\n"
        "     Chỉ được kích hoạt KHI VÀ CHỈ KHI vượt qua toàn bộ 4 Cổng kiểm duyệt trên.\n"
        "2. Chứng minh Ngắn mạch (Short-Circuit Proof) Không Gọi Các Bước Xử lý Phía sau:\n"
        "   - Kiến trúc Middleware Interceptor ngắn mạch: Bất kỳ Cổng nào phát hiện vi phạm sẽ lập tức trả về HTTP response và ngắt chuỗi thực thi (return early), không bao giờ gọi hàm `next()`.\n"
        "   - Bộ kiểm thử chứng minh với các Dấu vết Quan sát Được (Observable Traces & Metrics):\n"
        "     + Test Gate 1 (Malformed JSON): Gửi body sai cú pháp -> Nhận HTTP 400. Dấu vết: Metric `auth_evaluations_total` không tăng (+0), `model_calls_total` = 0.\n"
        "     + Test Gate 2 (Missing Auth): Gửi body chuẩn nhưng không có token -> Nhận HTTP 401. Dấu vết: Metric `redis_quota_lookups_total` không tăng (+0), `model_calls_total` = 0.\n"
        "     + Test Gate 3 (Rate Limited): Gửi auth hợp lệ nhưng spam 50 req/s -> Nhận HTTP 429. Dấu vết: Metric `cost_estimator_calls_total` không tăng (+0), `model_calls_total` = 0.\n"
        "     + Test Gate 4 (Budget Exceeded): Gửi request prompt 100k tokens vượt ngân sách -> Nhận HTTP 402/403. Dấu vết: Metric `provider_invocations_total` không tăng (+0) và số dư tài khoản không bị trừ thêm."
    ),
    "explanation": (
        "Chiến lược phòng thủ 'Fail-Fast Pipeline' sắp xếp các chốt chặn kiểm duyệt theo thứ tự chi phí tài nguyên tăng dần (từ kiểm tra CPU cục bộ rẻ nhất đến gọi API tính tiền đắt nhất). Việc ngắn mạch tức thì khi phát hiện vi phạm bảo vệ hệ thống khỏi các cuộc tấn công gây cạn kiệt tài chính (Financial Denial of Service - FDoS) và bảo tồn tối đa ngân sách vận hành."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Sắp xếp chính xác pipeline 4 cổng kiểm duyệt theo thứ tự chi phí tăng dần: Schema (400) -> Auth (401) -> Quota (429) -> Budget (402/403).\n"
        "- [1.5 điểm] Thiết kế cơ chế ngắn mạch Middleware ngăn chặn tuyệt đối việc thực thi các bước sau khi cổng trước bị từ chối.\n"
        "- [1.5 điểm] Xây dựng bộ kiểm thử chứng minh với dấu vết metrics cụ thể khẳng định model_calls = 0 đối với từng loại lỗi từ chối."
    ),
    "reference_source": "Enterprise Integration Patterns - Fail-Fast Router & AWS Well-Architected Framework - Cost Optimization Pillar"
}

# 31. d12-q066 (4 pts)
DAY12_PART1_B2["d12-q066"] = {
    "sample_answer": (
        "1. Lựa chọn Mẫu Xác thực Phù hợp: OAuth 2.0 Token Exchange (RFC 8693) / On-Behalf-Of Flow:\n"
        "   - Bối cảnh: Đối tác B2B gọi API thay mặt cho người dùng cuối. Đối tác không được dùng Master API Key tĩnh của mình để truy cập dữ liệu người dùng.\n"
        "   - Mô hình áp dụng: Đối tác B2B mang token ủy quyền của người dùng tới Identity Provider (IdP) để thực hiện Token Exchange, nhận về một Delegated Access Token (JWT) có thời hạn ngắn, phân quyền cụ thể và khán giả đích danh.\n"
        "2. Các Claim Bắt buộc Cần Kiểm tra Nghiêm ngặt (Claims Verification Matrix):\n"
        "   - Claim `iss` (Issuer): Xác minh token được phát hành đúng bởi Authorization Server tin cậy của hệ sinh thái (ví dụ `https://auth.enterprise.com`).\n"
        "   - Claim `aud` (Audience - Khán giả đích): BẮT BUỘC kiểm tra `aud == \"https://api.enterprise.com/service-A\"`. Nếu token có audience của dịch vụ khác (hoặc của Service B), API A phải lập tức từ chối với HTTP 403 Forbidden để ngăn ngừa token bị đối tác mang sang sử dụng trái phép ở API khác.\n"
        "   - Claim `exp` (Expiration Time): Kiểm tra thời hạn hiệu lực của token. Token ủy quyền B2B phải là Short-lived Token (thời gian sống từ 15 đến 30 phút). Nếu `current_time >= exp`, từ chối ngay với HTTP 401 Unauthorized.\n"
        "   - Claim `nbf` (Not Before): Xác nhận token không được sử dụng trước thời điểm chỉ định trong quá khứ.\n"
        "   - Claim `sub` (Subject - Người dùng Ủy quyền): Định danh duy nhất của người dùng cuối (`user_id`) mà đối tác đang đại diện thực thi.\n"
        "   - Claim `azp` hoặc `client_id` (Authorized Party - Đối tác B2B): Định danh của đối tác bên thứ ba được ủy quyền gọi thay.\n"
        "   - Claim `scope` / `permissions`: Xác định phạm vi các quyền năng cụ thể mà người dùng cho phép đối tác thực hiện trên API A (ví dụ: `documents:read`, không có quyền `documents:delete`)."
    ),
    "explanation": (
        "Trong kiến trúc tích hợp B2B hiện đại, việc sử dụng mã token đại diện có ràng buộc phạm vi và khán giả đích (Audience-Restricted Delegated Tokens) là tiêu chuẩn bảo mật cốt lõi. Kiểm tra nghiêm ngặt claim `aud` ngăn chặn triệt để tấn công Chuyển tiếp Token (Token Replay/Forwarding Attack), bảo đảm một token phát hành cho dịch vụ A không bao giờ có thể bị lạm dụng để gọi dịch vụ B."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác mẫu xác thực OAuth 2.0 Token Exchange / On-Behalf-Of (RFC 8693) cho kịch bản B2B ủy quyền.\n"
        "- [1.5 điểm] Phân tích chi tiết các claim an ninh cốt tử: `iss`, `aud` (bắt buộc khớp Audience A), `exp` (short-lived) và `nbf`.\n"
        "- [1.5 điểm] Thiết lập cặp định danh kép `sub` (end-user identity) kết hợp `azp/client_id` (B2B partner) cùng phạm vi quyền `scope`."
    ),
    "reference_source": "RFC 8693 (OAuth 2.0 Token Exchange) & RFC 7519 (JSON Web Token - JWT Specification)"
}

# 32. d12-q068 (4 pts)
DAY12_PART1_B2["d12-q068"] = {
    "sample_answer": (
        "1. Thiết kế Bộ Thẩm định Khóa (Client Key Verifier & Tenant Mapping):\n"
        "   - Cơ chế Lưu trữ Bảo mật: Tuyệt đối không lưu API Key dạng plain-text. Lưu trữ bảng băm: `API_KEY_HASH (SHA-256) -> TenantContext { tenant_id, name, status, quota }`.\n"
        "   - Quy trình Thẩm định tại Gateway Middleware:\n"
        "     + Bước 1: Trích xuất `X-API-Key` từ request header. Nếu thiếu header -> Trả về `HTTP 401 Unauthorized` ngay lập tức.\n"
        "     + Bước 2: Băm key bằng SHA-256 và tra cứu trong cache bộ nhớ. Nếu không tìm thấy hoặc tenant có status != `ACTIVE` -> Trả về `HTTP 401 Unauthorized` ngay lập tức.\n"
        "     + Bước 3: Nếu key hợp lệ, gắn `TenantContext` (chứa `tenant_id`) vào ngữ cảnh của request (`request.state.tenant`) và chuyển tiếp sang Controller/Worker.\n"
        "   - Bất biến Cốt tử (Core Invariant): Verifier chạy tại lớp Filter/Middleware trước khi bất kỳ tiến trình nào gọi tới Model Provider; yêu cầu bị từ chối không bao giờ chạm tới hạ tầng downstream.\n"
        "2. Thiết kế Bộ Kiểm thử (Verifier Test Suite):\n"
        "   - Test Case 1 (Tenant 1 Valid Key):\n"
        "     Gửi request với Key của Tenant 1. Khẳng định kết quả HTTP 200 OK. Metric `provider_calls_total{tenant=\"tenant_1\"}` tăng đúng 1 đơn vị.\n"
        "   - Test Case 2 (Tenant 2 Valid Key):\n"
        "     Gửi request với Key của Tenant 2. Khẳng định kết quả HTTP 200 OK. Metric `provider_calls_total{tenant=\"tenant_2\"}` tăng đúng 1 đơn vị, hoàn toàn độc lập với Tenant 1.\n"
        "   - Test Case 3 (Invalid / Forged Key - Negative Test):\n"
        "     Gửi request với Key sai `key_invalid_999`. Khẳng định kết quả `HTTP 401 Unauthorized`. Khẳng định cốt tử: Tổng số cuộc gọi `provider_calls_total` của cả hai tenant tăng đúng 0 (+0).\n"
        "   - Test Case 4 (Missing Key Header - Negative Test):\n"
        "     Gửi request không kèm header xác thực. Khẳng định kết quả `HTTP 401 Unauthorized`. Khẳng định cốt tử: Tổng số cuộc gọi `provider_calls_total` tăng đúng 0 (+0)."
    ),
    "explanation": (
        "Thiết kế xác thực đa người thuê (Multi-Tenant Authentication) yêu cầu sự phân lập tuyệt đối ngay từ cổng vào của hệ thống. Bằng cách thực thi thẩm định khóa trước khi khởi tạo bất kỳ tác vụ nào, hệ thống bảo vệ ngân sách nhà cung cấp dịch vụ khỏi các yêu cầu không hợp lệ, đồng thời gán chính xác chi phí sử dụng cho từng thực thể doanh nghiệp độc lập."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế bộ thẩm định API Key với cơ chế băm SHA-256 an toàn và ánh xạ chính xác sang Tenant Identity.\n"
        "- [1.5 điểm] Xây dựng bộ test đầy đủ 4 nhánh kiểm thử: Key đúng Tenant 1, Key đúng Tenant 2, Key sai và Thiếu key.\n"
        "- [1.5 điểm] Chứng minh nghiêm ngặt bất biến bảo vệ chi phí: các yêu cầu bị từ chối (401) làm tăng provider_calls chính xác bằng 0."
    ),
    "reference_source": "Multi-Tenant Architecture Security Patterns & OWASP API Security - Broken Authentication"
}

# 33. d12-q071 (4 pts)
DAY12_PART1_B2["d12-q071"] = {
    "sample_answer": (
        "1. Thiết kế Khóa Đếm Giới hạn Tốc độ Phân tầng (Rate Limit Key Schema):\n"
        "   - Cấu trúc khóa kết hợp gói dịch vụ, định danh tenant, route định tuyến và cửa sổ thời gian:\n"
        "     `rl:{tier}:{tenant_id}:{route_signature}:{window_epoch}`\n"
        "     Ví dụ:\n"
        "     + Route nặng cho gói Free: `rl:free:t_101:POST_/chat/completions:1698080000`\n"
        "     + Route nhẹ cho gói Pro: `rl:pro:t_202:GET_/models:1698080000`\n"
        "   - Lợi ích: Tách biệt hoàn toàn quota giữa các gói (Free vs Pro) và giữa các route, ngăn chặn việc gọi dồn dập route nhẹ làm cạn kiệt tài nguyên của route nghiệp vụ chính.\n"
        "2. Lựa chọn và Cấu hình Thuật toán Giới hạn Tốc độ:\n"
        "   - Thuật toán Áp dụng: Cửa sổ Trượt Kết hợp Token Bucket (Sliding Window Counter / Token Bucket) triển khai trên Redis.\n"
        "   - Cấu hình theo Gói (Tier Policy Parameters):\n"
        "     + Gói Free: Hạn mức khắt khe, ví dụ route `/chat` cho phép tối đa 10 requests / 60 giây (Burst = 2, Refill = 1 token mỗi 6 giây).\n"
        "     + Gói Pro: Hạn mức mở rộng, ví dụ route `/chat` cho phép 120 requests / 60 giây (Burst = 20, Refill = 2 tokens mỗi giây).\n"
        "3. Quy ước Phản hồi HTTP 429 và Headers Chuẩn Giúp Client Retry Đúng Lúc:\n"
        "   - Khi vượt quá hạn mức, Gateway trả về mã trạng thái chuẩn: `HTTP/1.1 429 Too Many Requests`.\n"
        "   - Bắt buộc trả về các Headers chuẩn hóa theo khuyến nghị IETF và RFC 6585:\n"
        "     + `Retry-After: 6` (Số giây chính xác client phải chờ trước khi thử lại).\n"
        "     + `RateLimit-Limit: 10` (Tổng hạn mức cho phép trong cửa sổ hiện tại).\n"
        "     + `RateLimit-Remaining: 0` (Số lượng yêu cầu còn lại trong cửa sổ).\n"
        "     + `RateLimit-Reset: 1698080060` (Thời điểm Unix timestamp khi hạn ngạch được làm mới hoàn toàn).\n"
        "   - Thân phản hồi JSON chi tiết:\n"
        "     `{\"error\": {\"code\": \"rate_limit_exceeded\", \"tier\": \"free\", \"retry_after_seconds\": 6, \"message\": \"Bạn đã đạt hạn ngạch gói Free (10 req/phút). Vui lòng thử lại sau 6 giây hoặc nâng cấp gói Pro.\"}}`"
    ),
    "explanation": (
        "Chiến lược kiểm soát lưu lượng phân tầng (Tiered Rate Limiting) giúp bảo vệ hạ tầng khỏi tình trạng quá tải và tối ưu hóa mô hình kinh doanh SaaS. Việc tuân thủ nghiêm ngặt các tiêu chuẩn phản hồi HTTP 429 kèm tiêu đề `Retry-After` giúp các ứng dụng máy khách tự động thiết lập thời gian chờ chính xác, loại bỏ các đợt bắn lại yêu cầu mù quáng (blind retries)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế cấu trúc khóa phân tầng kết hợp đầy đủ tier, tenant_id, route và cửa sổ thời gian.\n"
        "- [1.5 điểm] Lựa chọn thuật toán Token Bucket / Sliding Window và cấu hình tham số dung lượng/nạp rõ ràng cho từng gói Free/Pro.\n"
        "- [1.5 điểm] Quy ước phản hồi 429 chuẩn hóa quốc tế với đầy đủ các headers: Retry-After, RateLimit-Limit, RateLimit-Remaining, RateLimit-Reset."
    ),
    "reference_source": "RFC 6585 (Additional HTTP Status Codes - 429) & IETF Draft: RateLimit Header Fields for HTTP"
}

# 34. d12-q073 (4 pts)
DAY12_PART1_B2["d12-q073"] = {
    "sample_answer": (
        "1. Phân tích Nguyên nhân Lỗi và Sửa Cấu trúc Member trong Redis Sorted Set:\n"
        "   - Nguyên nhân: Trong Redis Sorted Set (`ZSET`), mỗi phần tử (member) phải là một giá trị duy nhất (unique). Nếu member chỉ là chuỗi timestamp (ví dụ `\"1698080000\"`), khi hai yêu cầu đồng thời đến trong cùng một mili-giây, yêu cầu thứ hai sẽ cập nhật lại score của member đó thay vì tạo một entry mới. Kết quả là hệ thống đếm thiếu yêu cầu (chỉ đếm 1 thay vì 2), gây rò rỉ hạn ngạch.\n"
        "   - Khắc phục Cấu trúc Member: Bắt buộc kết hợp timestamp với một định danh ngẫu nhiên duy nhất (UUIDv4 hoặc Monotonic NanoID):\n"
        "     `member = f\"{timestamp_epoch}:{uuid4()}\"`\n"
        "     Score vẫn là timestamp dạng số thực (microsecond float) để phục vụ cho việc lọc theo phạm vi thời gian.\n"
        "2. Sửa Thao tác thành Khối Thực thi Nguyên tử (Atomic Lua Script):\n"
        "   - Để loại bỏ hoàn toàn hiện tượng tranh chấp điều kiện (Race Condition) giữa bước đếm số lượng và bước ghi nhận, đóng gói toàn bộ logic vào Redis Lua Script:\n"
        "     ```lua\n"
        "     local key = KEYS[1]\n"
        "     local now = tonumber(ARGV[1])\n"
        "     local window = tonumber(ARGV[2]) -- 60 seconds\n"
        "     local limit = tonumber(ARGV[3])  -- 3 requests\n"
        "     local member = ARGV[4]           -- now:uuid\n"
        "     local clearBefore = now - window\n"
        "\n"
        "     -- 1. Xóa các request cũ ngoài cửa sổ 60s\n"
        "     redis.call('ZREMRANGEBYSCORE', key, '-inf', clearBefore)\n"
        "\n"
        "     -- 2. Đếm số lượng request hiện tại\n"
        "     local currentCount = redis.call('ZCARD', key)\n"
        "\n"
        "     -- 3. Kiểm tra và thêm nguyên tử nếu chưa vượt hạn mức\n"
        "     if currentCount < limit then\n"
        "         redis.call('ZADD', key, now, member)\n"
        "         redis.call('EXPIRE', key, window)\n"
        "         return {1, limit - currentCount - 1} -- Allowed (1: Chấp nhận, số dư)\n"
        "     else\n"
        "         return {0, 0} -- Denied (0: Bị từ chối 429)\n"
        "     end\n"
        "     ```\n"
        "3. Thiết kế Kiểm tra Boundary và Isolation:\n"
        "   - Boundary Test: Gửi lần lượt 3 yêu cầu hợp lệ trong 60s -> Cả 3 nhận HTTP 200 OK. Gửi yêu cầu thứ 4 tại giây thứ 59 -> Nhận HTTP 429. Chờ đến giây thứ 61, gửi yêu cầu thứ 5 -> Nhận HTTP 200 OK do các yêu cầu cũ đã bị dọn sạch.\n"
        "   - Concurrency Isolation Test: Bắn đồng thời 2 yêu cầu Req-1 và Req-2 tại cùng một microsecond khi hệ thống đang ở mức 2/3 requests:\n"
        "     + Do member là `now:uuid_1` và `now:uuid_2`, cả hai entry được phân biệt rõ ràng.\n"
        "     + Do Lua script chạy đơn luồng nguyên tử trên Redis server, một request được ghi nhận thành công (chạm mốc 3/3), request còn lại lập tức bị từ chối 429. Không có bất kỳ entry nào bị ghi đè."
    ),
    "explanation": (
        "Triển khai thuật toán Sliding Window Log trên Redis yêu cầu hiểu sâu về đặc tính duy nhất của phần tử trong Sorted Set. Việc tạo member kết hợp timestamp và UUID cùng với việc thực thi nguyên tử qua Lua Script loại trừ hoàn toàn nguy cơ đếm thiếu và race condition trong các kịch bản lưu lượng đồng thời cao."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác lỗi ghi đè member trong Redis ZSET và khắc phục bằng member duy nhất `timestamp:uuid`.\n"
        "- [1.5 điểm] Đóng gói thao tác nguyên tử bằng Redis Lua Script kết hợp ZREMRANGEBYSCORE, ZCARD và ZADD loại bỏ race condition.\n"
        "- [1.5 điểm] Xây dựng bộ kiểm thử Boundary và Concurrency Isolation chứng minh đếm chính xác khi 2 request đến cùng timestamp."
    ),
    "reference_source": "Redis Documentation - Sorted Sets & Lua Scripting: https://redis.io/commands/zadd/ và Figma Engineering Blog - An Alternative Approach to Rate Limiting"
}

# 35. d12-q075 (4 pts)
DAY12_PART1_B2["d12-q075"] = {
    "sample_answer": (
        "1. Quyết định Tiếp nhận / Từ chối (Admission Governance Decision):\n"
        "   - Quyết định dứt khoát: TỪ CHỐI YÊU CẦU NGAY TẬP TỨC TẠI CỔNG TIỀN KIỂM (SHORT-CIRCUIT REJECTION).\n"
        "   - Mã phản hồi: Trả về `HTTP 400 Bad Request` hoặc `HTTP 403 Forbidden` (hoặc `HTTP 402 Payment Required` đối với tài khoản trả trước).\n"
        "   - Tuyệt đối KHÔNG thực hiện cuộc gọi ngược dòng (Downstream Call) tới Model Provider API.\n"
        "2. Căn cứ Giới hạn và Bằng chứng Định lượng (Evidence & Quantitative Limits Basis):\n"
        "   - Căn cứ Chính sách Trần Chi phí Yêu cầu (Pre-Execution Request Cost Ceiling Policy):\n"
        "     + Quy tắc bất biến: `Estimated_Cost <= Request_Cost_Ceiling`.\n"
        "     + Số liệu thực tế: `Estimated_Cost = 0.006 USD` > `Request_Cost_Ceiling = 0.004 USD`.\n"
        "     + Chi phí ước tính đã vượt quá trần cho phép 150% ngay trước khi thực thi.\n"
        "   - Bằng chứng Tính toán từ Bộ phân tích Tokenizer Cục bộ (Local Tokenizer Evidence):\n"
        "     + Số lượng token đầu vào (Prompt Tokens): Được đếm chính xác bằng thư viện tokenizer cục bộ (ví dụ: `tiktoken` cho OpenAI hoặc `tokenizers` cho HuggingFace) là $N_{prompt}$ tokens.\n"
        "     + Giới hạn token đầu ra tối đa (Configured Max Tokens): Được trích xuất từ tham số `max_tokens` của payload yêu cầu là $N_{max\\_output}$ tokens.\n"
        "     + Công thức ước tính bảo toàn chi phí xấu nhất (Worst-Case Cost Bound):\n"
        "       `Estimated_Cost = (N_prompt * Price_Input_Per_Token) + (N_max_output * Price_Output_Per_Token) = 0.006 USD`.\n"
        "3. Dấu vết Kiểm toán và Bảo vệ Tài chính (Audit Evidence Trail):\n"
        "   - Ghi nhật ký kiểm toán giao dịch (Structured Audit Log):\n"
        "     `{\"event\": \"REQUEST_COST_CEILING_BREACH\", \"tenant_id\": \"tenant_xyz\", \"prompt_tokens\": 3200, \"max_output_tokens\": 1000, \"estimated_cost_usd\": 0.006, \"ceiling_usd\": 0.004, \"provider_invoked\": false, \"action\": \"DENIED\"}`.\n"
        "   - Lợi ích: Ngăn chặn triệt để rủi ro thâm hụt ngân sách và các cuộc tấn công gây cạn kiệt tài chính (Financial Denial of Service - FDoS) mà không tốn bất kỳ chi phí thực tế nào."
    ),
    "explanation": (
        "Nguyên tắc tiền kiểm soát ngân sách (Pre-Flight Cost Guardrail) là tuyến phòng thủ tài chính quan trọng nhất trong các ứng dụng AI tạo sinh. Bằng cách sử dụng tokenizer cục bộ để tính toán chi phí trần kịch bản xấu nhất trước khi gọi mạng, hệ thống có thể từ chối ngay lập tức các yêu cầu vượt hạn mức, bảo vệ doanh nghiệp khỏi việc tiêu tốn ngân sách ngoài tầm kiểm soát."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Đưa ra quyết định chuẩn xác: Từ chối yêu cầu ngay tại cổng tiền kiểm và không gọi model provider.\n"
        "- [1.5 điểm] Phân tích căn cứ định lượng rõ ràng: so sánh chi phí ước tính từ tokenizer (0,006 USD) với trần ngân sách (0,004 USD).\n"
        "- [1.5 điểm] Thiết lập bằng chứng kiểm toán minh bạch (Audit Trail) ghi nhận vi phạm hạn mức chi phí kèm metric provider_invoked = false."
    ),
    "reference_source": "FinOps Foundation - Cost Allocation and Guardrails: https://www.finops.org/framework/ và OpenAI API Pricing & Usage Governance Best Practices"
}

# 36. d12-q077 (4 pts)
DAY12_PART1_B2["d12-q077"] = {
    "sample_answer": (
        "1. Thiết kế Ghi sổ Hai Giai đoạn (Two-Phase Ledger Accounting: Reserve & Reconcile):\n"
        "   - Giai đoạn 1 (Phong tỏa Tạm tính khi Tiếp nhận - Admission Reservation):\n"
        "     + Khi Tenant A gửi yêu cầu, hệ thống tính chi phí ước tính là 1.0 USD.\n"
        "     + Thực hiện phong tỏa tạm tính (Hold / Reserve): Trừ 1.0 USD từ số dư khả dụng của Tenant A và ghi vào sổ cái một bản ghi giao dịch trạng thái `PENDING_RESERVED` với mã `hold_id_123`.\n"
        "     + Cơ chế này ngăn chặn việc Tenant A gửi đồng thời nhiều yêu cầu vượt quá số dư thực tế.\n"
        "   - Giai đoạn 2 (Đối soát Thực tế và Hoàn tiền Thừa - Post-Execution Reconciliation):\n"
        "     + Sau khi model hoàn tất sinh dữ liệu, hệ thống đọc usage thực tế từ response (số token vào + ra thực tế) và tính ra chi phí thực tế là 0.7 USD.\n"
        "     + Thực hiện quyết toán nguyên tử (Atomic Settlement): Chuyển trạng thái giao dịch sang `SETTLED` với chi phí ghi nhận chính thức là 0.7 USD, đồng thời hoàn trả 0.3 USD (`1.0 USD - 0.7 USD`) vào số dư khả dụng của Tenant A.\n"
        "2. Phân lập Sổ Chi tiêu Đa Người thuê (Multi-Tenant Ledger Isolation):\n"
        "   - Mỗi tenant sở hữu một sổ chi tiêu riêng biệt, được phân vùng theo cấu trúc khóa độc lập trong cơ sở dữ liệu/Redis:\n"
        "     `ledger:{tenant_id}:{billing_period_id}`\n"
        "     Ví dụ: Sổ Tenant A: `ledger:tenant_A:2026-10`, Sổ Tenant B: `ledger:tenant_B:2026-10`.\n"
        "   - Mọi thao tác ghi sổ, phong tỏa hay đối soát của Tenant A hoàn toàn độc lập và không bao giờ gây khóa hay ảnh hưởng tới số dư của Tenant B.\n"
        "3. Thiết kế Cơ chế Chuyển kỳ Kế toán (Billing Period Rollover):\n"
        "   - Khởi tạo Khóa Kỳ Mới Tự động: Đúng vào 00:00:00 UTC ngày đầu tháng mới (ví dụ sang tháng 11/2026), hệ thống tự động khởi tạo khóa kỳ mới `ledger:{tenant_id}:2026-11` kèm hạn mức cấp phát mới.\n"
        "   - Đóng băng Kỳ cũ (Period Snapshot & Freeze): Kỳ cũ `2026-10` được chuyển sang trạng thái `CLOSED / READ_ONLY` để phục vụ công tác xuất hóa đơn và báo cáo tài chính.\n"
        "   - Xử lý Yêu cầu Vắt ngang Kỳ (In-flight Requests across Midnight): Yêu cầu được nhận vào kỳ cũ (với reservation tạo trong kỳ `2026-10`) nhưng hoàn tất ở những giây đầu của kỳ mới vẫn được đối soát và ghi nhận chính xác vào kỳ mà reservation đó đã được sinh ra (`2026-10`), bảo đảm tính toàn vẹn và không làm lệch sổ cái giữa hai tháng."
    ),
    "explanation": (
        "Quy trình kế toán tài chính phân tán (Distributed FinOps Ledger) trong các nền tảng SaaS AI đòi hỏi sự nhất quán nghiêm ngặt. Việc áp dụng mô hình hai giai đoạn (Phong tỏa tạm tính - Quyết toán đối soát) giải quyết triệt để sự chênh lệch giữa chi phí ước tính và chi phí thực tế, đồng thời cơ chế phân vùng theo kỳ kế toán bảo đảm việc chuyển tháng diễn ra mượt mà và chính xác tuyệt đối."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế quy trình ghi sổ 2 giai đoạn chuẩn xác: Reserve 1.0 USD khi admission và Reconcile hoàn dư 0.3 USD theo thực tế 0.7 USD.\n"
        "- [1.5 điểm] Thiết lập cấu trúc sổ chi tiêu phân lập nghiêm ngặt theo từng tenant_id và billing_period.\n"
        "- [1.5 điểm] Xây dựng cơ chế chuyển kỳ tự động: tạo bucket mới theo tháng, đóng băng kỳ cũ và xử lý nhất quán các giao dịch vắt ngang kỳ."
    ),
    "reference_source": "FinOps Framework - Allocation and Invoicing Standards: https://www.finops.org/framework/ và Stripe Billing Architecture - Authorize and Settle Patterns"
}

print("Loaded Day 12 Part 1 b2 (questions 24 to 36).")
