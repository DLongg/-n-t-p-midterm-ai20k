# scripts/day12_part1.py
# -*- coding: utf-8 -*-
"""
Day 12: Cloud Services & Deployment
Questions 1 to 36 (d12-q002 to d12-q077)
"""

DAY12_PART1 = {}

# 1. d12-q002
DAY12_PART1["d12-q002"] = {
    "sample_answer": (
        "1. Chẩn đoán ba giả định sai lầm của môi trường Local (Local Assumptions Gap):\n"
        "   - Giả định 1 (Local Environment Variables File): Nghĩ rằng file cấu hình `.env` cục bộ sẽ tự động tồn tại trên cloud instance mới. Thực tế trong môi trường containerized/cloud, instance mới là ephemeral và không chứa file nhạy cảm cục bộ (vi phạm 12-Factor App).\n"
        "   - Giả định 2 (In-memory Session State): Coi bộ nhớ RAM của một tiến trình duy nhất là nơi lưu trữ trạng thái phiên (Session). Khi instance bị restart hoặc scale out nhiều replica, toàn bộ session của người dùng bị bốc hơi hoàn toàn.\n"
        "   - Giả định 3 (Shallow Process Health Check): Nghĩ rằng 'tiến trình PID còn sống' đồng nghĩa với việc ứng dụng sẵn sàng phục vụ. Thực tế tiến trình có thể bị treo (deadlock), mất kết nối cơ sở dữ liệu hoặc cạn kiệt connection pool nhưng process vẫn tồn tại.\n"
        "2. Nêu phép kiểm có thể quan sát được cho từng giả định:\n"
        "   - Phép kiểm 1 (Config Injection Test): Khởi tạo instance mới hoàn toàn từ image sạch không có file `.env`, truyền biến môi trường qua Secret Manager/K8s ConfigMap; xác nhận app khởi động thành công (HTTP 200).\n"
        "   - Phép kiểm 2 (State Persistence Test): Đăng nhập tạo session, thực hiện restart container (`docker restart`); gửi request tiếp theo và xác nhận session vẫn tồn tại (nhờ đã externalize ra Redis/Postgres).\n"
        "   - Phép kiểm 3 (Deep Health Check Test): Cố tình ngắt mạng tới cơ sở dữ liệu phụ thuộc; xác nhận endpoint `/health/readiness` lập tức phản hồi HTTP 503 Service Unavailable để Load Balancer ngừng định tuyến traffic.\n"
        "3. Bổ sung phép kiểm Concurrency và Chi phí trước Production:\n"
        "   - Concurrency Test: Sử dụng k6/Locust bắn đồng thời 500 yêu cầu đồng thời (concurrent streams), đo lường P99 latency và xác nhận worker pool không bị cạn kiệt bộ nhớ hoặc crash do rò rỉ kết nối I/O.\n"
        "   - Cost Budget Limit Test: Thiết lập giới hạn trần chi phí gọi model API (Token Spend Hard Cap) và kiểm tra xem hệ thống có tự động ngắt (circuit break) khi chi phí vượt hạn mức ngân sách hay không."
    ),
    "explanation": (
        "Khoảng cách giữa môi trường cục bộ (Localhost) và Môi trường Sản xuất Đám mây (Cloud Production Gap) là nguyên nhân hàng đầu gây sập hệ thống trong ngày đầu phát hành. Ứng dụng AI Agent đòi hỏi sự tuân thủ nghiêm ngặt phương pháp luận 12-Factor App: Tách biệt cấu hình khỏi mã nguồn, ngoại biên hóa trạng thái phiên ra kho lưu trữ độc lập (State Externalization), và xây dựng Deep Health Check đánh giá tính sẵn sàng thực sự thay vì chỉ kiểm tra PID tiến trình."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Chẩn đoán chính xác 3 giả định sai lầm của local: file .env biến mất, session trong memory bị mất và health check nông chỉ xem process.\n"
        "- [1.5 điểm] Thiết kế phép kiểm quan sát được cho cả 3 giả định: config injection, restart persistence và deep readiness check.\n"
        "- [1.5 điểm] Bổ sung đầy đủ 2 phép kiểm tiên quyết trước production: Concurrency load testing và Token Cost Budget hard cap."
    ),
    "reference_source": "The Twelve-Factor App Methodology: https://12factor.net/ và Google Cloud Architecture Framework - Reliability & Production Readiness"
}

# 2. d12-q004 (5 POINTS)
DAY12_PART1["d12-q004"] = {
    "sample_answer": (
        "1. Gán từng thành phần và ranh giới tin cậy vào các lớp tài nguyên đám mây:\n"
        "   - Lớp Công cộng (Public Ingress / Edge Tier):\n"
        "     + Thành phần: Public HTTP/REST Endpoint phục vụ client bên ngoài, Cloud API Gateway, Web Application Firewall (WAF), TLS Termination Proxy.\n"
        "     + Ranh giới tin cậy: Vùng không tin cậy (Untrusted Public Zone), chỉ tiếp nhận lưu lượng đã qua xác thực token và rate limiting.\n"
        "   - Lớp Tính toán Nội bộ (Application & Worker Compute Tier):\n"
        "     + Thành phần: Agent Worker Instances (Kubernetes Pods / Cloud Run), Execution Engine điều phối các công cụ.\n"
        "     + Ranh giới tin cậy: Mạng riêng ảo (Private VPC Subnet), không có IP công khai, giao tiếp nội bộ qua mã hóa mTLS.\n"
        "   - Lớp Dịch vụ Đối tác Ngoại bộ (External Model Provider Tier):\n"
        "     + Thành phần: OpenAI / Anthropic API Endpoint.\n"
        "     + Ranh giới tin cậy: Egress Boundary bảo vệ bằng NAT Gateway và Proxy kiểm soát tên miền tin cậy (Egress Allowlist).\n"
        "   - Lớp Dữ liệu Riêng tư (Private Data & Storage Tier):\n"
        "     + Thành phần: Private Document Storage (S3 / Cloud Storage / Private Vector DB) chứa tài liệu nhạy cảm của doanh nghiệp.\n"
        "     + Ranh giới tin cậy: Vùng dữ liệu tối mật (Zero-Trust Data Tier) được bảo vệ bằng Private Endpoint / VPC Endpoint, cấm hoàn toàn truy cập từ Internet.\n"
        "2. Tìm Dependency còn thiếu trong bối cảnh:\n"
        "   - Phân tích: Đề bài chỉ rõ 'worker chưa có identity để truy cập storage'.\n"
        "   - Dependency còn thiếu: 'Danh tính Tác vụ Đám mây có Thẩm quyền' (Managed Workload Identity / IAM Service Account Role) được gán trực tiếp cho Agent Worker.\n"
        "   - Giải pháp: Cần cấu hình AWS IAM Role for Service Accounts (IRSA) hoặc Google Cloud Workload Identity Federation để cấp quyền `s3:GetObject` tối thiểu cho worker truy cập Private Document Storage mà không cần hardcode secret key vào container."
    ),
    "explanation": (
        "Kiến trúc tài nguyên đám mây hiện đại áp dụng mô hình 'Zero Trust và Phân tầng Quốc phòng' (Defense-in-Depth Resource Layering). Việc phân chia rạch ròi giữa Public Edge, Compute Worker, Egress Provider và Private Storage ngăn chặn việc xâm nhập một tầng làm sụp đổ toàn bộ hệ thống. Thiếu danh tính tác vụ (Workload Identity) là điểm nghẽn cốt tử khiến các thành phần không thể giao tiếp an toàn, buộc kỹ sư phải thiết lập IAM Role theo nguyên tắc Least Privilege."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 5 điểm):\n"
        "- [1.0 điểm] Phân tầng tài nguyên chính xác vào 4 lớp: Public Ingress, Compute Worker, External Provider và Private Storage.\n"
        "- [2.0 điểm] Xác định rõ ràng các ranh giới tin cậy (Trust Boundaries): Private VPC, Egress Proxy, Private Link Endpoint.\n"
        "- [2.0 điểm] Chỉ ra chính xác dependency còn thiếu là Managed Workload Identity / IAM Service Account và nêu giải pháp cấp quyền tối thiểu."
    ),
    "reference_source": "AWS Well-Architected Framework - Security Pillar: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/ và Google Cloud Workload Identity Federation: https://cloud.google.com/iam/docs/workload-identity-federation"
}

# 3. d12-q006
DAY12_PART1["d12-q006"] = {
    "sample_answer": (
        "1. Chọn Service Model phù hợp:\n"
        "   - Lựa chọn: IaaS (Infrastructure as a Service) hoặc Managed Kubernetes (CaaS - Container as a Service trên Dedicated VPC, e.g. Self-managed Nodes trên AWS EKS / GCP GKE Private Cluster).\n"
        "   - Tuyệt đối KHÔNG CHỌN Public PaaS hoặc Multi-tenant Serverless/SaaS.\n"
        "   - Lý do: Ngân hàng có các yêu cầu kỹ thuật và tuân thủ đặc thù: (a) Cô lập network tùy biến (Custom VPC, Direct Connect, cấm Internet công cộng); (b) Kiểm soát lịch vá lỗi (Custom Patching Schedule không bị gián đoạn giao dịch bất ngờ); (c) Toàn quyền kiểm soát runtime mức thấp (Custom Kernel tuning, eBPF security agent); (d) Ngân hàng đã có sẵn đội ngũ kỹ sư hạ tầng chuyên trách (Platform Team).\n"
        "2. Phân chia trách nhiệm (Shared Responsibility Boundary):\n"
        "   - Trách nhiệm Giao cho Cloud Provider:\n"
        "     + Bảo mật vật lý của Trung tâm dữ liệu (Datacenter Physical Security);\n"
        "     + Hạ tầng máy chủ vật lý, phần cứng lưu trữ và hệ thống mạng cáp quang gốc;\n"
        "     + Tầng Hypervisor và Kubernetes Control Plane (nếu dùng Managed K8s).\n"
        "   - Trách nhiệm Ngân hàng Giữ lại (Platform Team Ownership):\n"
        "     + Cấu hình và quản lý mạng ảo (VPC Peering, Subnets, Security Groups, Routing Tables, Firewalls);\n"
        "     + Lập lịch và thực thi vá lỗi hệ điều hành máy ảo (OS Patching & Kernel Hardening);\n"
        "     + Quản lý vòng đời runtime container, phân quyền IAM, mã hóa dữ liệu tại chỗ (KMS Customer-Managed Keys) và giám sát an ninh SIEM 24/7."
    ),
    "explanation": (
        "Mô hình Trách nhiệm Chung trên Đám mây (Cloud Shared Responsibility Model) phân định ranh giới giữa kiểm soát và gánh nặng vận hành. Các tổ chức tài chính lớn với đội ngũ Platform chuyên môn bắt buộc phải duy trì mức kiểm soát sâu tại tầng hạ tầng (IaaS/Private K8s) để đáp ứng các tiêu chuẩn thanh tra ngân hàng (PCI-DSS, Basel III), chấp nhận gánh vác trách nhiệm vá lỗi OS và quản lý mạng đổi lấy quyền kiểm soát tuyệt đối."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác mô hình IaaS / Managed Kubernetes Private Cluster, giải thích lý do dựa trên yêu cầu kiểm soát mạng, patch schedule và nhân sự platform.\n"
        "- [1.5 điểm] Xác định rõ ràng các trách nhiệm bàn giao cho Cloud Provider: hạ tầng vật lý, phần cứng, datacenter security.\n"
        "- [1.5 điểm] Liệt kê đầy đủ các trách nhiệm ngân hàng phải giữ lại: cấu hình mạng VPC, vá lỗi OS runtime, quản lý IAM và mã hóa dữ liệu KMS."
    ),
    "reference_source": "AWS Shared Responsibility Model: https://aws.amazon.com/compliance/shared-responsibility-model/ và PCI-DSS Cloud Computing Guidelines"
}

# 4. d12-q008
DAY12_PART1["d12-q008"] = {
    "sample_answer": (
        "1. Thiết kế Quy trình Thăng cấp Môi trường (Environment Promotion Parity):\n"
        "   - Nguyên tắc Bất biến của Artifact (Immutable Artifact Parity): Image digest `D` (SHA-256 Digest bất biến đã pass Staging) BẮT BUỘC ĐƯỢC GIỮ NGUYÊN 100% khi deploy lên Production. Tuyệt đối không build lại image từ source code cho môi trường Prod.\n"
        "   - Tách biệt Cấu hình (Externalized Config Separation): Các tham số môi trường được bơm hoàn toàn từ bên ngoài thông qua Kubernetes Secrets / ConfigMaps độc lập:\n"
        "     + Replica count: Set `replicas = 10` trong Production Deployment manifest (thay vì 1 replica ở Staging);\n"
        "     + Credential: Gắn Secret chứa production database password và model API key thật từ Production KMS Vault;\n"
        "     + Database: Biến `DATABASE_URL` trỏ tới Production RDS/Aurora Multi-AZ cluster.\n"
        "2. Thiết kế Phương án Quay lui An toàn (Rollback Strategy):\n"
        "   - Giữ lại bản ghi phiên bản trước: Deployment Manifest của phiên bản ổn định trước đó (`digest D_prev`) được lưu giữ sẵn trong GitOps repository;\n"
        "   - Thao tác Rollback tức thì: Khi Production gặp lỗi sau deploy, kích hoạt lệnh rollback tự động của Kubernetes: `kubectl rollout undo deployment/agent-service` hoặc commit revert trên GitOps. Hệ thống chuyển ngay về `digest D_prev` trong vòng vài giây mà không cần thay đổi cấu hình database hay secret."
    ),
    "explanation": (
        "Phương pháp luận 12-Factor App (Yếu tố X: Dev/Prod Parity) quy định rằng mã thực thi (Binary/Container Image) phải hoàn toàn giống hệt nhau giữa các môi trường. Mọi sự khác biệt giữa Staging và Production chỉ được phép nằm ở 3 khía cạnh ngoại biên: Cấu hình (Config), Dữ liệu (Database), và Quy mô tài nguyên (Capacity). Thiết kế triển khai bất biến theo Image Digest giúp loại bỏ hiện tượng 'chạy được trên staging nhưng sập trên prod' và bảo đảm khả năng rollback tức thời."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Khẳng định nguyên tắc giữ nguyên 100% image digest D từ Staging lên Production (Immutable Artifact).\n"
        "- [1.5 điểm] Phân tách an toàn các yếu tố ngoại biên: scale 10 replicas, production credentials riêng và database production qua Secret/ConfigMap.\n"
        "- [1.0 điểm] Thiết kế đường quay lui (Rollback) nhanh chóng và tin cậy thông qua Kubernetes rollout undo hoặc GitOps."
    ),
    "reference_source": "The Twelve-Factor App - X. Dev/prod parity: https://12factor.net/dev-prod-parity và Kubernetes Documentation - Deployments & Rollout Management"
}

# 5. d12-q010
DAY12_PART1["d12-q010"] = {
    "sample_answer": (
        "1. Định nghĩa Config Contract (Hợp đồng Cấu hình Chuẩn 12-Factor):\n"
        "   - Nguyên tắc: Cùng một Docker Image duy nhất phải chạy được trên mọi môi trường mà không cần sửa một dòng code hay rebuild image. Toàn bộ cấu hình được nạp từ biến môi trường (Environment Variables):\n"
        "     + Biến Giao tiếp Cổng (Port Binding): `PORT` (Mặc định: 8080; Staging: 5000; Production: 7000). Ứng dụng tự bind vào `process.env.PORT`.\n"
        "     + Biến Endpoint Dịch vụ: `MODEL_API_ENDPOINT` (Staging: `https://mock.internal.test/v1`; Production: `https://api.openai.com/v1`).\n"
        "     + Biến Secret Bắt buộc: `MODEL_API_KEY` (Staging: mock key; Production: real production secret key).\n"
        "     + Biến Môi trường: `ENVIRONMENT` (`staging` vs `production`).\n"
        "2. Phép kiểm Parity giữa Staging và Production (Parity Verification Test):\n"
        "   - Phép kiểm 1 (Image Checksum Equality): Xác nhận `sha256(staging_image) == sha256(production_image)`.\n"
        "   - Phép kiểm 2 (Port Binding Observability): Khởi động container ở staging với `PORT=5000`, thực hiện `curl http://localhost:5000/health` -> nhận 200 OK. Khởi động chính container đó ở production với `PORT=7000`, `curl http://localhost:7000/health` -> nhận 200 OK.\n"
        "   - Phép kiểm 3 (Missing Secret Fail-Fast): Khởi động container nhưng cố tình bỏ trống biến `MODEL_API_KEY` -> Ứng dụng phải lập tức crash ở startup kèm thông báo lỗi rõ ràng `CRITICAL: Missing mandatory MODEL_API_KEY`, không được chạy trong trạng thái thiếu cấu hình."
    ),
    "explanation": (
        "Nguyên tắc 'Port Binding' và 'Config in Environment' (Yếu tố III và VII của 12-Factor) yêu cầu ứng dụng phải hoàn toàn tự chủ (Self-contained) và xuất dịch vụ ra bên ngoài bằng cách bind vào cổng được chỉ định qua biến môi trường. Việc cứng mã cổng hoặc endpoint vào mã nguồn là phản mẫu hình kiến trúc. Phép kiểm parity chứng minh tính linh hoạt của container và đảm bảo cơ chế fail-fast khi thiếu cấu hình bắt buộc."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Định nghĩa hợp đồng cấu hình đầy đủ: phân loại rõ giá trị môi trường (PORT, endpoint), secret bắt buộc (API key) và cờ environment.\n"
        "- [1.5 điểm] Khẳng định image container được giữ nguyên bản tuyệt đối giữa hai môi trường.\n"
        "- [1.0 điểm] Thiết kế các phép kiểm tra parity thực tế: kiểm tra checksum giống nhau, kiểm tra bind port động (5000 vs 7000) và kiểm tra fail-fast khi thiếu secret."
    ),
    "reference_source": "The Twelve-Factor App - III. Config & VII. Port binding: https://12factor.net/config và Kubernetes Container Port Configuration Best Practices"
}

# 6. d12-q012
DAY12_PART1["d12-q012"] = {
    "sample_answer": (
        "Lập kế hoạch chuyển đổi phụ thuộc mô hình (Model Migration Release Plan: M -> R):\n"
        "1. Đánh giá Capacity và Điểm nghẽn:\n"
        "   - Lưu lượng thực tế: Traffic = 100 rps.\n"
        "   - Hạn mức hiện tại của mô hình R: R_quota = 60 rps (Thiếu hụt 40 rps, chỉ đáp ứng được 60% tải).\n"
        "   - Quyết định: TUYỆT ĐỐI CHƯA CHUYỂN TOÀN BỘ TRAFFIC sang R ngay lập tức vì sẽ gây quá tải và sập dịch vụ (HTTP 429 Cascading Failure).\n"
        "   - Thời hạn mô hình cũ M: Còn 21 ngày (Thời gian dư dả để thực hiện chuyển dịch từng bước an toàn).\n"
        "2. Lịch trình Chuyển đổi theo 4 Giai đoạn:\n"
        "   - Tuần 1 (Kiểm chứng Hợp đồng Prompt & Hạn mức - Verification & Quota Uplift):\n"
        "     + Gửi yêu cầu tới nhà cung cấp mô hình R nâng quota từ 60 rps lên tối thiểu 150 rps (đảm bảo headroom dự phòng 50%);\n"
        "     + Chạy bộ kiểm thử tự động xác minh tương thích Prompt Contract (Prompt Regression Suite) giữa output của M và R trên 1000 mẫu đại diện.\n"
        "   - Tuần 2 (Chạy Shadow Mode / Dual-Write):\n"
        "     + Bật chế độ Shadow Traffic: 100% request vẫn do M phục vụ trả kết quả cho người dùng; đồng thời clone bất đồng bộ 20 rps sang R để đo độ trễ p95/p99 và tỷ lệ lỗi thực tế.\n"
        "   - Tuần 3 (Chuyển Traffic theo Tỷ lệ Tăng dần - Phased Canary Rollout):\n"
        "     + Ngày 15: Chuyển 10% traffic chính thức sang R, 90% ở M;\n"
        "     + Ngày 17: Chuyển 50% traffic sang R (nằm trong hạn mức 60 rps an toàn);\n"
        "     + Ngày 19: Sau khi quota mới đã được cấp, chuyển 100% traffic sang R.\n"
        "3. Phương án Quay lui Tức thì (Rollback Plan):\n"
        "   - Duy trì kết nối song song tới M cho đến tận Ngày 20. Nếu R gặp sự cố sụt giảm chất lượng hoặc lỗi rate limit ở bất kỳ giai đoạn nào, chỉ cần chuyển cờ cấu hình (Feature Flag) ở API Gateway trỏ ngược 100% lưu lượng về M trong vòng < 1 giây."
    ),
    "explanation": (
        "Chuyển đổi phụ thuộc vào các dịch vụ AI bên ngoài (Third-party Foundation Model Dependency Migration) đòi hỏi kế hoạch quản trị rủi ro chi tiết: Không bao giờ chuyển đổi khi năng lực cung ứng (Quota Capacity) chưa đáp ứng đủ lưu lượng đỉnh. Việc tận dụng cửa sổ 21 ngày còn lại cho phép triển khai kỹ thuật Shadowing và Canary Rollout có kiểm soát, kết hợp feature flag cho phép rollback tức thời về mô hình cũ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác bài toán năng lực: R chỉ có 60 rps không đủ tải cho 100 rps, yêu cầu nâng quota trước khi chuyển hoàn toàn.\n"
        "- [1.5 điểm] Xây dựng lộ trình chuyển đổi bài bản: Kiểm chứng prompt contract -> Shadow mode -> Canary rollout tăng dần theo tỷ lệ.\n"
        "- [1.5 điểm] Tận dụng hợp lý cửa sổ 21 ngày và thiết lập phương án rollback tức thì bằng feature flag quay lại M khi có sự cố."
    ),
    "reference_source": "Google SRE Book - Canarying Releases & Managing External Dependencies: https://sre.google/sre-book/canarying-releases/ và Martin Fowler, Feature Toggles"
}

# 7. d12-q014
DAY12_PART1["d12-q014"] = {
    "sample_answer": (
        "Theo dõi 4 yếu tố kiến trúc qua chu kỳ Xóa và Triển khai lại Container:\n"
        "1. Mã trong Artifact (Code in Container Image `I2`):\n"
        "   - Trạng thái: BẤT BIẾN VÀ BẢO TỒN NGUYÊN VẸN (Immutable & Preserved). Mã nguồn được đóng gói thành các layer cố định trong Docker Image `I2` lưu trên container registry. Việc xóa hay tạo mới 3 container không làm thay đổi hay mất mát mã trong image.\n"
        "2. Dữ liệu Bền vững (Persistent Data in Named Volume `V`):\n"
        "   - Trạng thái: TIẾP TỤC TỒN TẠI VÀ ĐƯỢC CHIA SẺ (Persistent & Survives Lifecycle). Named Volume `V` được quản lý độc lập với vòng đời của container. Khi container cũ bị xóa và container mới được tạo ra gắn kết với Volume `V`, toàn bộ các tệp tải lên trước đó vẫn còn nguyên vẹn 100%.\n"
        "3. Địa chỉ Service (Logical Service Endpoint Address):\n"
        "   - Trạng thái: CỐ ĐỊNH VÀ KHÔNG ĐỔI (Stable Abstract Address). Địa chỉ logic của Service (ví dụ DNS nội bộ `http://agent-service:8080` hoặc Kubernetes ClusterIP / Cloud Load Balancer IP) duy trì ổn định không đổi. Các client bên ngoài không bao giờ phải thay đổi địa chỉ kết nối.\n"
        "4. Định danh Instance (Container Instance Identity & Transient State):\n"
        "   - Trạng thái: BỊ HỦY BỎ VÀ TẠO MỚI HOÀN TOÀN (Ephemeral & Destroyed). Mỗi container có một Container ID mới, IP mạng nội bộ pod mới, và bộ nhớ RAM cục bộ mới. Dữ liệu lưu trong writable layer tạm thời của container cũ bị xóa sạch."
    ),
    "explanation": (
        "Hiểu rõ Ranh giới Vòng đời Container (Container Artifact & Runtime Boundaries) là kiến thức nền tảng trong điện toán đám mây. Kiến trúc đám mây chuẩn mực phân biệt rạch ròi 4 tầng: (1) Mã trong image là bất biến; (2) Dữ liệu lâu dài nằm ở Volume ngoài; (3) Điểm truy cập Service là trừu tượng ổn định; và (4) Instance thực thi là phù du (ephemeral cattle, not pets). Thiết kế này cho phép hệ thống tự do tái tạo, co giãn mà không mất mát dữ liệu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác trạng thái Mã trong Artifact: bất biến, bảo tồn trên registry.\n"
        "- [1.0 điểm] Phân tích chính xác trạng thái Dữ liệu bền vững trong Named Volume V: sống sót qua việc xóa container.\n"
        "- [1.0 điểm] Phân tích chính xác Địa chỉ Service: giữ nguyên ổn định qua DNS/Load Balancer trừu tượng.\n"
        "- [1.0 điểm] Phân tích chính xác Định danh Instance: mang tính phù du (ephemeral), bị hủy và cấp phát ID/IP mới khi deploy lại."
    ),
    "reference_source": "Docker Documentation - Manage data in Docker (Volumes vs Containers): https://docs.docker.com/storage/volumes/ và CNCF Container Storage Interface (CSI)"
}

# 8. d12-q017
DAY12_PART1["d12-q017"] = {
    "sample_answer": (
        "1. Thiết kế Cách Xử lý Tương thích (Architecture & Libc Compatibility Strategy):\n"
        "   - Phân tích xung đột kép:\n"
        "     + Xung đột Kiến trúc CPU: Gói chỉ có wheel cho `amd64` (x86_64), trong khi môi trường production đích là `arm64` (aarch64 / Graviton);\n"
        "     + Xung đột Thư viện Chuẩn C (C Library): Gói native được biên dịch cho `glibc` (GNU C Library), trong khi Alpine Linux sử dụng `musl libc`.\n"
        "   - Giải pháp Kiến trúc:\n"
        "     + Lựa chọn 1 (Khuyên dùng - Đổi Base Image): Thay thế Alpine bằng một bản phân phối dựa trên glibc hỗ trợ multi-arch như `Debian Slim` (e.g. `python:3.11-slim-bookworm` hoặc `Ubuntu Minimal`). Điều này giải quyết triệt để vấn đề `musl libc`.\n"
        "     + Lựa chọn 2 (Biên dịch Native Wheel cho arm64): Nếu mã nguồn gói mở, sử dụng Docker Buildx / QEMU trong CI/CD để biên dịch native wheel từ source code trực tiếp trên kiến trúc `linux/arm64`.\n"
        "2. Thiết kế Cách Xác minh Clean Build (Reproducible Clean Build Verification):\n"
        "   - Bước 1 (Pin chặt chẽ Dependencies): Sử dụng file lock chuẩn xác (`requirements.lock` hoặc `poetry.lock` / `pip-tools`) ghi rõ mã hash SHA-256 của từng gói wheel tương ứng với target platform: `--platform linux_arm64`.\n"
        "   - Bước 2 (Clean Build from Empty Cache): Chạy lệnh Docker build với cờ xóa sạch cache: `docker buildx build --platform linux/arm64 --no-cache --pull -t agent:prod .` trong môi trường CI/CD cô lập.\n"
        "   - Bước 3 (Runtime Smoke Test trên Target Arch): Chạy thử container trên máy ảo arm64 thực tế (hoặc qua emulation): import gói native đó và thực thi một hàm tính toán mẫu để xác nhận không bị lỗi `OSError: Error loading shared library`."
    ),
    "explanation": (
        "Lỗi tương thích binary giữa môi trường phát triển và môi trường đích là một cái bẫy lớn. Alpine Linux siêu nhẹ nhưng dùng `musl libc`, thường xuyên không tương thích với các gói Python native/AI vốn được đóng gói sẵn bánh xe (pre-built wheels) cho `glibc amd64`. Để có một bản build tái lập sạch (Reproducible Clean Build), giải pháp tối ưu là chuyển sang `python-slim` (glibc), kết hợp Docker Buildx đa nền tảng và khóa chặt mã băm SHA-256 của gói phụ thuộc."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Nhận diện và giải quyết chính xác xung đột kép: Kiến trúc CPU (amd64 vs arm64) và Thư viện C (glibc vs musl libc trên Alpine).\n"
        "- [1.5 điểm] Đưa ra giải pháp kỹ thuật đúng đắn: chuyển sang base image Debian Slim (glibc) hoặc build native wheel bằng Docker Buildx.\n"
        "- [1.0 điểm] Thiết lập quy trình clean build tái lập chuẩn: pin version kèm SHA-256 hash, build với --no-cache và smoke test trên kiến trúc đích."
    ),
    "reference_source": "Docker Buildx Multi-platform Documentation: https://docs.docker.com/build/building/multi-platform/ và Python Packaging User Guide - Platform compatibility tags"
}

# 9. d12-q019
DAY12_PART1["d12-q019"] = {
    "sample_answer": (
        "1. Sắp xếp Thứ tự Layer Dockerfile tối ưu Cache (Layer Cache Ordering):\n"
        "   - Nguyên tắc vàng của Docker Caching: 'Đặt các layer ít thay đổi nhất ở trên cùng, và các layer thay đổi thường xuyên nhất ở dưới cùng'.\n"
        "   - Cấu trúc Dockerfile chuẩn mực:\n"
        "     ```dockerfile\n"
        "     FROM python:3.11-slim\n"
        "     WORKDIR /app\n"
        "     # 1. Cài đặt system packages (ít đổi nhất - cache tái dùng lâu nhất)\n"
        "     RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev && rm -rf /var/lib/apt/lists/*\n"
        "     # 2. CHỈ COPY file manifest dependency (đổi hàng tháng)\n"
        "     COPY requirements.txt .\n"
        "     # 3. Cài đặt dependencies (bước tốn thời gian nhất - được cache)\n"
        "     RUN pip install --no-cache-dir -r requirements.txt\n"
        "     # 4. CUỐI CÙNG MỚI COPY toàn bộ mã nguồn ứng dụng (đổi mỗi giờ)\n"
        "     COPY app/ ./app/\n"
        "     CMD [\"python\", \"-m\", \"app.main\"]\n"
        "     ```\n"
        "   - Hiệu quả: Khi mã nguồn trong thư mục `app/` thay đổi mỗi giờ, Docker chỉ invalidate cache từ lệnh `COPY app/`, toàn bộ các layer trước đó (bao gồm cả bước cài `requirements.txt` tốn vài phút) được tái sử dụng cache 100% trong vòng < 1 giây.\n"
        "2. Thời điểm bước cài đặt dependency bắt buộc phải build lại:\n"
        "   - Bước cài đặt dependency (`RUN pip install`) CHỈ build lại khi và chỉ khi nội dung của file `requirements.txt` bị thay đổi (checksum hash của file thay đổi), hoặc khi base image được cập nhật mới (`--pull`), hoặc khi xóa cache build (`--no-cache`)."
    ),
    "explanation": (
        "Cơ chế Docker Layer Caching hoạt động dựa trên mã băm nội dung của câu lệnh và các tệp được COPY vào layer đó. Nếu ta thực hiện `COPY . .` trước lệnh `pip install`, thì bất kỳ thay đổi nào trong mã nguồn ứng dụng cũng sẽ làm nổ cache (cache busting) của layer copy, ép Docker phải tải và cài lại toàn bộ thư viện từ đầu. Bằng cách tách riêng `COPY requirements.txt` trước, ta bảo toàn cache dependency cho các lần build mã nguồn liên tục."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Sắp xếp chính xác thứ tự Dockerfile: Base OS -> COPY requirements.txt -> RUN pip install -> COPY mã nguồn app.\n"
        "- [1.5 điểm] Giải thích cơ chế cache: thay đổi mã nguồn mỗi giờ không làm vỡ cache của bước cài dependency vì đặt sau.\n"
        "- [1.0 điểm] Chỉ rõ điều kiện duy nhất khiến bước cài dependency phải build lại: file requirements.txt bị sửa đổi hoặc xóa cache."
    ),
    "reference_source": "Docker Documentation - Optimizing builds with cache: https://docs.docker.com/build/cache/ và Best practices for writing Dockerfiles"
}

# 10. d12-q021
DAY12_PART1["d12-q021"] = {
    "sample_answer": (
        "1. Thiết kế Dockerfile Đa giai đoạn (Multi-stage Build Architecture):\n"
        "```dockerfile\n"
        "# STAGE 1: Build & Compile Stage (Chứa đầy đủ compiler và build tools)\n"
        "FROM python:3.11-slim AS builder\n"
        "WORKDIR /build\n"
        "RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ build-essential libpq-dev\n"
        "COPY requirements.txt .\n"
        "RUN pip wheel --no-cache-dir --wheel-dir=/build/wheels -r requirements.txt\n"
        "\n"
        "# STAGE 2: Final Minimal Runtime Stage (Siêu nhẹ, loại bỏ compiler)\n"
        "FROM python:3.11-slim AS runtime\n"
        "WORKDIR /app\n"
        "# BẮT BUỘC: Cài đặt runtime shared libraries (không cài build tools)\n"
        "RUN apt-get update && apt-get install -y --no-install-recommends libpq5 && rm -rf /var/lib/apt/lists/*\n"
        "# Copy wheels từ builder stage và cài đặt\n"
        "COPY --from=builder /build/wheels /wheels\n"
        "RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* && rm -rf /wheels\n"
        "COPY app/ ./app/\n"
        "USER 10001:10001\n"
        "CMD [\"python\", \"-m\", \"app.main\"]\n"
        "```\n"
        "2. Xác minh Filesystem và Shared Library ở Final Image:\n"
        "   - Kiểm tra loại trừ Build Tools: `docker run --rm runtime which gcc` -> Phải trả về mã lỗi (exit code 1, không tìm thấy gcc), đảm bảo bề mặt tấn công tối thiểu.\n"
        "   - Kiểm tra liên kết Thư viện Động (Dynamic Shared Library Linkage Verification): Chạy công cụ kiểm tra phụ thuộc thư viện native của Python extension: `docker run --rm runtime ldd /usr/local/lib/python3.11/site-packages/.../*.so`. Xác nhận 100% các file `.so` đều tìm thấy thư viện chia sẻ liên kết (không có thông báo `not found`), chứng minh container không bị crash khi chạy tác vụ thực tế."
    ),
    "explanation": (
        "Multi-stage build cho phép phân tách rạch ròi giữa 'Môi trường Xây dựng' (chứa trình biên dịch nặng nề như gcc, g++) và 'Môi trường Thực thi' (chỉ chứa tệp thực thi sạch và thư viện runtime tối thiểu). Tuy nhiên, cạm bẫy lớn nhất là thiếu các shared dynamic libraries (như `libpq.so.5` cho PostgreSQL) ở stage cuối dẫn đến crash khi khởi động. Việc cài đặt đúng gói runtime shared library và kiểm tra bằng lệnh `ldd` là tiêu chuẩn vàng của containerization an toàn."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.5 điểm] Thiết kế đầy đủ 2 stage rõ ràng: Builder stage biên dịch wheel và Runtime stage tối thiểu hóa copy artifacts.\n"
        "- [1.5 điểm] Xử lý chính xác việc cài đặt runtime shared libraries ở stage cuối để ngăn chặn crash runtime.\n"
        "- [1.0 điểm] Thiết lập phương pháp xác minh filesystem: kiểm tra loại bỏ build tools (gcc) và xác nhận liên kết thư viện bằng ldd."
    ),
    "reference_source": "Docker Documentation - Multi-stage builds: https://docs.docker.com/build/building/multi-stage/ và Debian Packages Runtime Libraries"
}
from scripts.day12_part1_b1 import DAY12_PART1_B1
from scripts.day12_part1_b2 import DAY12_PART1_B2

DAY12_PART1.update(DAY12_PART1_B1)
DAY12_PART1.update(DAY12_PART1_B2)

print(f"Loaded Day 12 Part 1 complete: {len(DAY12_PART1)} questions.")
