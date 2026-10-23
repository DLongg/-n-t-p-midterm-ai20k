# scripts/day12_part1_b1.py
# -*- coding: utf-8 -*-
"""
Day 12 Part 1 Questions 11 to 23 (d12-q023 to d12-q048)
"""

DAY12_PART1_B1 = {}

# 11. d12-q023 (4 pts)
DAY12_PART1_B1["d12-q023"] = {
    "sample_answer": (
        "1. Thiết kế Runtime Container Non-Root và Phân quyền Tối thiểu:\n"
        "   - Cấu hình Dockerfile với User không đặc quyền:\n"
        "     ```dockerfile\n"
        "     RUN groupadd -g 10001 appgroup && \\\n"
        "         useradd -u 10001 -g appgroup -s /sbin/nologin -M appuser && \\\n"
        "         mkdir -p /data/jobs && \\\n"
        "         chown -R 10001:10001 /data/jobs && \\\n"
        "         chmod 700 /data/jobs\n"
        "     USER 10001:10001\n"
        "     ```\n"
        "   - Ràng buộc Runtime Security Context (Docker/Kubernetes):\n"
        "     + `read_only_root_filesystem: true` (Toàn bộ root filesystem chỉ đọc, ngoại trừ volume mount `/data/jobs`).\n"
        "     + `drop_capabilities: [\"ALL\"]` (Tước bỏ toàn bộ đặc quyền Linux capabilities như `CAP_NET_BIND_SERVICE`, `CAP_SYS_ADMIN`).\n"
        "     + `no_new_privileges: true` (Ngăn chặn tiến trình nâng quyền thông qua setuid binaries).\n"
        "2. Thiết kế Bộ kiểm thử các Thao tác Phải bị Từ chối (Negative Test Matrix):\n"
        "   - Test 1 (Ghi vào thư mục hệ thống): Thực thi lệnh `touch /etc/hacked.txt` hoặc `touch /usr/local/bin/test` -> Kết quả mong đợi: Bị từ chối với lỗi `Read-only file system` hoặc `Permission denied` (EACCES).\n"
        "   - Test 2 (Bind cổng đặc quyền mạng < 1024): Cho agent chạy socket listener trên port 80 hoặc 443 -> Kết quả mong đợi: Lập tức bị từ chối với lỗi `Permission denied` do thiếu `CAP_NET_BIND_SERVICE`.\n"
        "   - Test 3 (Cài đặt package hệ điều hành): Chạy `apt-get install -y curl` hoặc `su / sudo` -> Kết quả mong đợi: Lỗi `Permission denied: Are you root?` hoặc command không tồn tại.\n"
        "   - Test 4 (Positive Test - Ghi hợp lệ vào `/data/jobs`): Chạy lệnh `echo '{\"job_id\": \"1\"}' > /data/jobs/job_1.json` -> Kết quả mong đợi: Ghi thành công hoàn toàn với quyền sở hữu `appuser:appgroup`."
    ),
    "explanation": (
        "Nguyên tắc Đặc quyền Tối thiểu (Principle of Least Privilege) trong bảo mật container yêu cầu cô lập triệt để tiến trình ứng dụng khỏi root host. Bằng cách gán non-root UID 10001, tước bỏ toàn bộ Linux capabilities và khóa rootfs ở chế độ Read-Only, hệ thống triệt tiêu nguy cơ container breakout ngay cả khi mã nguồn của Agent có lỗ hổng thực thi mã từ xa (RCE)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Cấu hình runtime non-root hoàn chỉnh: USER UID 10001, chown riêng `/data/jobs`, read-only rootfs và cap_drop ALL.\n"
        "- [1.5 điểm] Thiết kế bộ negative test matrix chi tiết chứng minh bị từ chối khi ghi `/etc`, bind port < 1024 và cài package.\n"
        "- [1.5 điểm] Kiểm thử positive test xác nhận ghi file thành công tại `/data/jobs` và kích hoạt cờ no-new-privileges."
    ),
    "reference_source": "CIS Docker Benchmark v1.6.0 & Kubernetes Security Context Best Practices: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/"
}

# 12. d12-q025 (4 pts)
DAY12_PART1_B1["d12-q025"] = {
    "sample_answer": (
        "1. Phân tích Xung đột và Thiết kế Boundary Loại trừ trong `.dockerignore`:\n"
        "   - Vấn đề: Rule `**/*.sql` loại trừ mù quáng tất cả các file SQL, khiến thư mục `app/migrations/*.sql` cần cho quá trình khởi tạo lược đồ cơ sở dữ liệu runtime bị thiếu hụt.\n"
        "   - Thiết kế quy tắc `.dockerignore` kết hợp phủ định (Negation Pattern `!`):\n"
        "     ```dockerignore\n"
        "     # 1. Loại bỏ các file nhạy cảm và secret môi trường\n"
        "     **/.env*\n"
        "     **/*.pem\n"
        "     **/*.key\n"
        "     **/*.crt\n"
        "     **/*.dump\n"
        "     dumps/\n"
        "     # 2. Loại bỏ các file SQL tùy tiện hoặc database backups ngoài ý muốn\n"
        "     **/*.sql\n"
        "     # 3. Ngoại lệ rõ ràng cho các file migration bắt buộc của runtime\n"
        "     !app/migrations/*.sql\n"
        "     !app/migrations/**/*.sql\n"
        "     ```\n"
        "2. Thiết kế Bộ kiểm thử Image Verification:\n"
        "   - Test 1 (Positive Verification - File bắt buộc hiện diện):\n"
        "     Chạy lệnh `docker run --rm <built_image> ls -la /app/migrations` -> Kiểm tra exit code = 0 và danh sách tệp hiển thị đầy đủ các file như `001_initial_schema.sql`.\n"
        "   - Test 2 (Negative Verification - Secret và SQL rác hoàn toàn vắng mặt):\n"
        "     Chạy lệnh `docker run --rm <built_image> find / -name '*.env*' -o -name '*.key' -o -name '*.pem'` -> Kỳ vọng trả về danh sách rỗng (0 matches).\n"
        "     Chạy lệnh `docker run --rm <built_image> find / -path '/app/migrations' -prune -o -name '*.sql' -print` -> Xác nhận không có bất kỳ file SQL nào ngoài thư mục migrations lọt vào image.\n"
        "   - Test 3 (Layer History Inspection):\n"
        "     Chạy `docker history --no-trunc <built_image>` -> Kiểm tra các lệnh COPY để chắc chắn không có layer nào vô tình copy secret vào rồi xóa ở layer sau."
    ),
    "explanation": (
        "File `.dockerignore` là ranh giới phòng thủ đầu tiên ngăn chặn rò rỉ bí mật vào Docker Build Context. Cú pháp phủ định `!` cho phép tạo ra quy tắc loại trừ có chọn lọc (Selective Whitelisting): Chặn toàn bộ file SQL nguy hiểm (như database dumps, test queries) nhưng giữ lại các file migration cốt lõi trong đường dẫn xác định, đảm bảo tính toàn vẹn của ứng dụng khi triển khai."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác xung đột loại trừ của rule `**/*.sql` và sửa `.dockerignore` với cú pháp phủ định `!app/migrations/*.sql`.\n"
        "- [1.5 điểm] Thiết lập ranh giới loại trừ toàn diện chặn triệt để secret (.env, .pem, .key, dumps) không lọt vào context.\n"
        "- [1.5 điểm] Xây dựng bộ kiểm tra Docker run/find và layer history chứng minh migration có mặt còn secret vắng bóng 100%."
    ),
    "reference_source": "Docker Documentation - .dockerignore file: https://docs.docker.com/build/building/context/#dockerignore-files và OWASP Docker Security Cheat Sheet"
}

# 13. d12-q027 (4 pts)
DAY12_PART1_B1["d12-q027"] = {
    "sample_answer": (
        "1. Quyết định Phát hành có Điều kiện (Conditional Release Governance Decision):\n"
        "   - Không cấp ngoại lệ vô điều kiện. Phê duyệt Ngoại lệ Bảo mật có Giới hạn Thời gian (Time-boxed Security Exception) tối đa 48 giờ đối với Digest D2, với điều kiện bắt buộc phải triển khai Biện pháp Giảm thiểu Bù đắp (Compensating Controls):\n"
        "     + Cách ly mạng (Egress/Ingress Isolation): Chặn đường tấn công trực tiếp tới module dính High CVE tại tầng WAF/API Gateway bằng quy tắc regex/payload filter.\n"
        "     + Giới hạn môi trường: Chỉ phát hành canary hoặc giới hạn lưu lượng, cấm mở rộng quy mô public toàn phần.\n"
        "   - Nếu không có compensating control khả thi nào để ngăn chặn khả năng khai thác của CVE reachable này: Quyết định dứt khoát là CHẶN PHÁT HÀNH (REJECT RELEASE).\n"
        "2. Bằng chứng Kiểm toán Bắt buộc Cần Lưu giữ (Audit Evidence Trail):\n"
        "   - Khóa danh tính bất biến bằng Image Digest: Ghi nhận chính xác `image@sha256:D2...` (không chấp nhận mutable tag như `:latest`).\n"
        "   - Hồ sơ Ngoại lệ Bảo mật (Security Exception Ticket): Lưu trữ chữ ký phê duyệt đồng thuận từ Security Lead / CISO và Business Product Owner, đính kèm báo cáo đánh giá rủi ro (Risk Assessment) và mô tả chi tiết compensating controls.\n"
        "   - Báo cáo Quét lỗ hổng (Vulnerability Scan Report): File xuất JSON từ scanner (Trivy/Grype) lưu trữ CVE ID, CVSS v3 score, vector khai thác và phân tích khả năng tiếp cận (Reachability Proof).\n"
        "3. Lịch Kiểm tra lại và Cơ chế Thu hồi Tự động (Re-check & Revocation Schedule):\n"
        "   - Mốc T+48 Giờ: Policy Controller (như Kyverno hoặc OPA Gatekeeper) tự động kích hoạt hết hạn ngoại lệ (Exception Expiration). Nếu image D2 chưa được thay thế, admission controller lập tức chặn restart pod và gửi cảnh báo đỏ P1.\n"
        "   - Mốc T+5 Ngày: Kích hoạt pipeline build tự động kéo bản vá upstream, tạo Image Digest D3 mới, chạy quét sạch CVE và thực hiện rolling update thay thế hoàn toàn D2."
    ),
    "explanation": (
        "Quản trị ngoại lệ bảo mật (Vulnerability Exception Governance) trong quy trình CI/CD là cầu nối giữa rủi ro an ninh và nhu cầu kinh doanh. Khóa cứng bằng Immutable Digest bảo đảm ngoại lệ chỉ áp dụng cho đúng mã nhị phân cụ thể đó mà không bị trôi tag. Cơ chế hết hạn tự động (Time-boxed TTL) ngăn ngừa việc ngoại lệ tạm thời biến thành lỗ hổng vĩnh viễn bị lãng quên trong môi trường production."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Đưa ra quyết định phát hành có điều kiện chặt chẽ kèm biện pháp giảm thiểu bù đắp (Compensating Controls) trong 48h.\n"
        "- [1.5 điểm] Lưu giữ đầy đủ bằng chứng kiểm toán: Immutable Image Digest sha256, vé ngoại lệ có chữ ký CISO/PO và báo cáo scan CVE.\n"
        "- [1.5 điểm] Thiết lập lịch kiểm tra lại tự động tại mốc T+48h (thu hồi ngoại lệ) và mốc T+5 ngày (triển khai bản vá D3 mới)."
    ),
    "reference_source": "NIST SP 800-190 (Application Container Security Guide) & CNCF Software Supply Chain Best Practices"
}

# 14. d12-q029 (4 pts)
DAY12_PART1_B1["d12-q029"] = {
    "sample_answer": (
        "1. Sửa Contract Docker Compose (`docker-compose.yml`):\n"
        "   ```yaml\n"
        "   version: '3.8'\n"
        "   services:\n"
        "     redis:\n"
        "       image: redis:7-alpine\n"
        "       command: [\"redis-server\", \"--appendonly\", \"yes\"]\n"
        "       volumes:\n"
        "         - redis_data:/data\n"
        "       healthcheck:\n"
        "         test: [\"CMD\", \"redis-cli\", \"ping\"]\n"
        "         interval: 5s\n"
        "         timeout: 3s\n"
        "         retries: 3\n"
        "     agent:\n"
        "       image: enterprise-agent:v1.2\n"
        "       deploy:\n"
        "         replicas: 3\n"
        "       environment:\n"
        "         - REDIS_URL=redis://redis:6379/0\n"
        "       depends_on:\n"
        "         redis:\n"
        "           condition: service_healthy\n"
        "       healthcheck:\n"
        "         test: [\"CMD\", \"curl\", \"-f\", \"http://localhost:8000/health/readiness\"]\n"
        "         interval: 5s\n"
        "         timeout: 3s\n"
        "         retries: 3\n"
        "         start_period: 10s\n"
        "     proxy:\n"
        "       image: nginx:alpine\n"
        "       ports:\n"
        "         - \"80:80\"\n"
        "       depends_on:\n"
        "         - agent\n"
        "   volumes:\n"
        "     redis_data:\n"
        "   ```\n"
        "2. Cấu hình Proxy Định tuyến theo Readiness và Service Discovery:\n"
        "   - Cấu hình Nginx/Traefik upstream trỏ tới DNS `agent:8000` (Docker DNS tự động cân bằng tải giữa các container có IP khỏe mạnh).\n"
        "   - Thiết lập proxy chỉ forward traffic tới các replica có trạng thái `healthy` (HTTP 200 từ `/health/readiness`).\n"
        "3. Phương pháp Xác minh Thực tế:\n"
        "   - Xác minh 1 (Session Persistence Test): Gửi request tạo session trên container Agent-1 (ghi session data vào Redis). Chạy `docker compose stop agent_1` để hủy container; gửi request tiếp theo qua proxy, proxy tự động chuyển sang Agent-2 hoặc Agent-3; kiểm tra session vẫn tồn tại nguyên vẹn.\n"
        "   - Xác minh 2 (Zero-Downtime Readiness Test): Trong quá trình khởi động lại từng replica (rolling update), liên tục bắn HTTP requests; quan sát proxy log để xác nhận 100% request đều trả về HTTP 200, không có bất kỳ phản hồi 502 Bad Gateway nào do proxy không định tuyến tới container chưa ready."
    ),
    "explanation": (
        "Kiến trúc Stateless Agent với Redis Persistent Storage tuân thủ nguyên tắc Factor VI (Stateless Processes) và Factor IX (Disposability) của 12-Factor App. Bằng việc phân tách trạng thái phiên ra Redis volume và kết hợp điều kiện `service_healthy` cùng Deep Readiness Probe, hệ thống bảo đảm khả năng co giãn ngang (horizontal scaling) lên 3 replica mà không bao giờ làm gián đoạn trải nghiệm người dùng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Sửa Compose contract chính xác: cấu hình Redis persistent volume và Agent deploy scale replicas = 3.\n"
        "- [1.5 điểm] Thiết lập cơ chế Deep Readiness Healthcheck cho Agent và dependency condition `service_healthy`.\n"
        "- [1.5 điểm] Trình bày phương pháp xác minh toàn diện: kiểm thử session sống qua container restart và proxy zero-downtime routing."
    ),
    "reference_source": "Docker Compose File Specification: https://docs.docker.com/compose/compose-file/ và NGINX Reverse Proxy Health Checks Guide"
}

# 15. d12-q031 (4 pts)
DAY12_PART1_B1["d12-q031"] = {
    "sample_answer": (
        "1. Lựa chọn Mô hình Vòng đời Giao tiếp (Lifecycle Model):\n"
        "   - Lựa chọn Server-Sent Events (SSE) trên nền HTTP Streaming (MIME type: `text/event-stream`).\n"
        "   - Biện minh: Chat completion là luồng dữ liệu đơn hướng (Unidirectional Stream) từ máy chủ về máy khách sau yêu cầu POST khởi tạo. SSE nhẹ hơn, dễ cấu hình qua proxy/WAF hơn WebSocket (không cần nâng cấp protocol phức tạp), hỗ trợ native reconnection và xử lý backpressure hiệu quả.\n"
        "2. Mô tả Hành vi Chi tiết ở Các Cột mốc Vòng đời:\n"
        "   - Mốc 1 (First Token Latency - 300ms):\n"
        "     + Máy chủ gửi ngay HTTP status 200 với các headers: `Content-Type: text/event-stream`, `Cache-Control: no-cache`, `Connection: keep-alive`, `X-Accel-Buffering: no` (vô hiệu hóa proxy buffer).\n"
        "     + Đẩy ngay chunk đầu tiên: `event: delta\\ndata: {\"token\": \"Xin\"}\\n\\n` và flush socket ngay lập tức để client hiển thị từ đầu tiên trong vòng 300ms.\n"
        "   - Mốc 2 (Hoàn tất thành công - 20s):\n"
        "     + Khi LLM kết thúc sinh dữ liệu, máy chủ phát sự kiện hoàn tất chuẩn: `event: done\\ndata: {\"finish_reason\": \"stop\", \"total_tokens\": 512, \"duration_ms\": 20000}\\n\\n`.\n"
        "     + Máy chủ đóng HTTP stream một cách duyên dáng (Graceful TCP Close) và ghi log kiểm toán giao dịch thành công.\n"
        "   - Mốc 3 (Client Chủ động Ngắt Kết nối - Disconnect Handling):\n"
        "     + Lắng nghe sự kiện ngắt kết nối socket (FastAPI/ASGI `request.is_disconnected()` hoặc asyncio `CancelledError`).\n"
        "     + Hành vi dứt khoát: Ngay lập tức gửi tín hiệu hủy (Abort Signal) tới Model Provider API để dừng việc sinh token tiếp theo, tránh lãng phí chi phí token downstream.\n"
        "     + Hủy bỏ các tác vụ nền liên quan và ghi log trạng thái `status: client_aborted` kèm số lượng token đã tiêu thụ thực tế."
    ),
    "explanation": (
        "Xử lý vòng đời HTTP Streaming cho AI Agent đòi hỏi sự phối hợp chặt chẽ giữa giảm thiểu độ trễ phản hồi ban đầu (Time-to-First-Token) và quản lý tài nguyên khi xảy ra ngắt kết nối đột ngột. Việc lắng nghe tín hiệu client disconnect để hủy cuộc gọi model ngược dòng (Upstream Abort) là biện pháp then chốt giúp doanh nghiệp ngăn chặn rò rỉ ngân sách GPU/API."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Lựa chọn chính xác mô hình Server-Sent Events (SSE) và giải thích ưu thế so với WebSocket cho chat streaming.\n"
        "- [1.5 điểm] Mô tả chính xác hành vi tại TTFT 300ms (flush socket, disable proxy buffer) và khi hoàn tất 20s (event done, usage metadata).\n"
        "- [1.5 điểm] Thiết kế quy trình xử lý ngắt kết nối phía client: phát hiện disconnect, abort upstream LLM để tiết kiệm chi phí và ghi log."
    ),
    "reference_source": "W3C Server-Sent Events Specification: https://html.spec.whatwg.org/multipage/server-sent-events.html và OpenAI Streaming API Best Practices"
}

# 16. d12-q033 (4 pts)
DAY12_PART1_B1["d12-q033"] = {
    "sample_answer": (
        "1. Thiết kế Chuỗi Sự kiện SSE Chuẩn Hóa (Standard SSE Event Sequence):\n"
        "   ```http\n"
        "   HTTP/1.1 200 OK\n"
        "   Content-Type: text/event-stream\n"
        "   Cache-Control: no-cache\n"
        "   Connection: keep-alive\n"
        "\n"
        "   event: message\n"
        "   id: evt-001\n"
        "   data: {\"type\": \"content_delta\", \"index\": 0, \"text\": \"A\"}\n"
        "\n"
        "   event: message\n"
        "   id: evt-002\n"
        "   data: {\"type\": \"content_delta\", \"index\": 1, \"text\": \"B\"}\n"
        "\n"
        "   event: completion\n"
        "   id: evt-003\n"
        "   data: {\"type\": \"message_stop\", \"finish_reason\": \"end_turn\", \"usage\": {\"input_tokens\": 25, \"output_tokens\": 2, \"total_tokens\": 27}}\n"
        "\n"
        "   data: [DONE]\n"
        "\n"
        "   ```\n"
        "2. Thiết kế Bộ kiểm tra Toàn vẹn Chuỗi Sự kiện (Event Stream Test Suite):\n"
        "   - Test 1 (Thứ tự Tuần tự Nghiêm ngặt - Strict Ordering Test):\n"
        "     Đọc stream bằng SSE client parser; ghi nhận mảng các event nhận được. Khẳng định `received[0].data['text'] == 'A'` và `received[1].data['text'] == 'B'`. Nếu nhận B trước A thì đánh fail test.\n"
        "   - Test 2 (Đếm và Xác thực Terminal Event - Terminal Event Assertion):\n"
        "     Khẳng định sự kiện `completion` xuất hiện đúng 1 lần duy nhất trong toàn bộ vòng đời stream và luôn nằm sau tất cả các `content_delta` events.\n"
        "   - Test 3 (Cấu trúc Usage Metadata Test):\n"
        "     Phân tích JSON của event `completion`; xác nhận các trường `input_tokens`, `output_tokens`, `total_tokens` là số nguyên dương và thỏa mãn `input_tokens + output_tokens == total_tokens`.\n"
        "   - Test 4 (Stream Terminator Test):\n"
        "     Kiểm tra dòng đóng stream cuối cùng `data: [DONE]` trước khi kết nối TCP đóng hoàn toàn."
    ),
    "explanation": (
        "Thiết kế giao thức truyền phát sự kiện cho LLM đòi hỏi tính cấu trúc cao. Việc phân định rõ ràng giữa các sự kiện nội dung trung gian (`message`/`content_delta`) và sự kiện kết thúc duy nhất (`completion`) kèm siêu dữ liệu sử dụng token (`usage`) giúp client vừa hiển thị giao diện mượt mà theo thời gian thực vừa cập nhật chính xác hạn ngạch chi phí của người dùng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế định dạng chuỗi sự kiện SSE chuẩn xác với 2 chunks A, B và terminal completion event kèm usage tokens.\n"
        "- [1.5 điểm] Xây dựng bộ kiểm tra thứ tự tuần tự A -> B nghiêm ngặt và kiểm tra phân tách ranh giới các block sự kiện.\n"
        "- [1.5 điểm] Kiểm tra tính duy nhất của terminal event, tính toàn vẹn của usage metadata và ký hiệu đóng stream chuẩn [DONE]."
    ),
    "reference_source": "Anthropic Messages Streaming Protocol: https://docs.anthropic.com/en/api/messages-streaming và IETF SSE Specifications"
}

# 17. d12-q036 (4 pts)
DAY12_PART1_B1["d12-q036"] = {
    "sample_answer": (
        "1. Cơ chế Giữ Kết nối Sống Vượt qua Proxy Idle Timeout 60s:\n"
        "   - Phân tích: Proxy ngắt kết nối nếu không có byte nào được truyền trong 60 giây. Khoảng im lặng 70 giây giữa các chunk chắc chắn gây ra lỗi 504 Gateway Timeout.\n"
        "   - Thiết kế Heartbeat / Ping định kỳ:\n"
        "     + Máy chủ khởi tạo một background timer gửi SSE comment định kỳ mỗi 15 giây (< 60s): `: ping\\n\\n`.\n"
        "     + Theo đặc tả SSE, các dòng bắt đầu bằng dấu hai chấm `:` là comment và bị client bỏ qua, không ảnh hưởng đến dữ liệu hiển thị nhưng giữ cho kết nối TCP/HTTP luôn có lưu lượng, ngăn chặn reverse proxy đóng kết nối.\n"
        "2. Thiết kế Cơ chế Resume và Reconnect Không Trùng Sự kiện:\n"
        "   - Gán ID Đơn điệu (Monotonic Event IDs) phía Máy chủ:\n"
        "     + Mỗi chunk dữ liệu gửi đi được gắn kèm một ID duy nhất tăng dần: `id: evt_001`, `id: evt_002`, ...\n"
        "     + Máy chủ duy trì một bộ đệm vòng (Ring Buffer trong Redis hoặc In-memory Cache) lưu trữ các event đã phát của stream trong vòng 10 phút, lập chỉ mục theo Event ID.\n"
        "   - Cơ chế Reconnect với `Last-Event-ID` phía Máy khách:\n"
        "     + Trình duyệt/Client tự động lưu `Last-Event-ID` của event gần nhất nhận được. Khi kết nối bị đứt, client gửi lại HTTP GET kèm header `Last-Event-ID: evt_001`.\n"
        "   - Xử lý Resume phía Máy chủ:\n"
        "     + Khi nhận request có `Last-Event-ID: evt_k`, máy chủ tra cứu trong Ring Buffer.\n"
        "     + Chỉ phát lại các event có `ID > evt_k` (ví dụ từ `evt_002` trở đi). Tuyệt đối không phát lại `evt_001` đã gửi thành công trước đó.\n"
        "     + Tiếp tục stream các chunk mới theo thời gian thực mà không làm lặp từ ngữ trên màn hình người dùng."
    ),
    "explanation": (
        "Xây dựng đường truyền HTTP Streaming có khả năng tự phục hồi (Resilient Streaming) yêu cầu giải quyết đồng thời hai thách thức: Ngăn chặn timeout trung gian bằng Heartbeat Ping và đảm bảo ngữ nghĩa chính xác một lần (Exactly-Once Semantics) khi tái kết nối bằng con trỏ trạng thái `Last-Event-ID` kết hợp bộ nhớ đệm sự kiện phía máy chủ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích nguyên nhân proxy timeout 60s và thiết kế cơ chế Heartbeat ping định kỳ 15s bằng SSE comment `: ping`.\n"
        "- [1.5 điểm] Thiết kế gán Monotonic Event ID tăng dần và kiến trúc Ring Buffer lưu trữ sự kiện phía máy chủ.\n"
        "- [1.5 điểm] Xây dựng logic xử lý header Last-Event-ID khi client reconnect, đảm bảo chỉ phát bù event thiếu và chống trùng lặp."
    ),
    "reference_source": "MDN Web Docs - Server-sent events: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events và RFC 8895 (HTTP Last-Event-ID)"
}

# 18. d12-q038 (4 pts)
DAY12_PART1_B1["d12-q038"] = {
    "sample_answer": (
        "1. Theo dõi Máy trạng thái (State Machine) mà Client Quan sát được:\n"
        "   - Trạng thái 1: `QUEUED` - Yêu cầu được tiếp nhận vào hàng đợi, hệ thống trả về HTTP 202 Accepted kèm `job_id`.\n"
        "   - Trạng thái 2: `RUNNING` - Worker 1 lấy job và bắt đầu thực thi, phát heartbeat cập nhật trạng thái.\n"
        "   - Sự cố Worker 1 crash: Visibility timeout của hàng đợi hết hạn, job được tự động chuyển giao lại (redelivered). Client polling vẫn nhìn thấy trạng thái `RUNNING` (hoặc `RUNNING (Attempt 2)`), không bị chuyển ngược về trạng thái không hợp lệ.\n"
        "   - Trạng thái 3: `FAILED (Terminal)` - Worker 2 thử lại nhưng gặp lỗi không thể khắc phục hoặc vượt quá `max_retries = 3`. Trạng thái chuyển sang FAILED cuối cùng kèm `error_code` và thông điệp chi tiết.\n"
        "   - Nguyên tắc chuyển trạng thái: Phải bảo đảm tính đơn hướng (Monotonic Forward Progress) đối với client: `QUEUED -> RUNNING -> FAILED`.\n"
        "2. Phân định Ranh giới Trách nhiệm Retry (Retry Boundary & Responsibilities):\n"
        "   - Trách nhiệm của Hàng đợi / Hệ thống (Infrastructure & Queue Responsibility):\n"
        "     + Tự động retry đối với các lỗi tạm thời (Transient Failures): Worker crash đột ngột, mất kết nối mạng, container bị OOMKilled.\n"
        "     + Sử dụng cơ chế Visibility Timeout, Exponential Backoff và Dead-Letter Queue (DLQ) có giới hạn số lần thử lại tối đa.\n"
        "     + Bắt buộc các bước công việc phải có tính lũy kế (Idempotent Execution) để khi Worker 2 chạy lại không gây tác dụng phụ trùng lặp (ví dụ: không trừ tiền thẻ tín dụng 2 lần).\n"
        "   - Trách nhiệm của Client (Client Responsibility):\n"
        "     + Khi nhận trạng thái `FAILED (Terminal)`, client TUYỆT ĐỐI KHÔNG được tự động retry liên tục để tránh gây bão request (Thundering Herd Problem).\n"
        "     + Client chỉ được phép retry khi có hành động chủ động từ người dùng (User-Initiated Action) hoặc sau khi người dùng đã sửa đổi tham số đầu vào, đính kèm `Idempotency-Key` mới."
    ),
    "explanation": (
        "Quản trị trạng thái bất đồng bộ phân tán đòi hỏi sự phân định minh bạch giữa lỗi nhất thời của hạ tầng (Transient Infrastructure Errors) và lỗi vĩnh viễn của nghiệp vụ (Terminal Business Errors). Hệ thống hàng đợi chịu trách nhiệm retry nội bộ an toàn với tính lũy đẳng, trong khi client phải tôn trọng trạng thái Terminal để ngăn chặn vòng lặp retry vô tận làm tê liệt hệ thống."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế State Machine nhất quán mà client quan sát được theo một chiều từ QUEUED -> RUNNING -> FAILED terminal.\n"
        "- [1.5 điểm] Xác định rõ trách nhiệm retry của Queue/System: xử lý transient errors, visibility timeout, DLQ và idempotent execution.\n"
        "- [1.5 điểm] Phân định rõ trách nhiệm của Client: dừng retry khi nhận terminal failure, chỉ retry khi có user action với Idempotency Key mới."
    ),
    "reference_source": "Enterprise Integration Patterns - Idempotent Consumer & AWS Architecture Guide for Asynchronous Messaging"
}

# 19. d12-q040 (4 pts)
DAY12_PART1_B1["d12-q040"] = {
    "sample_answer": (
        "1. Thiết kế Ranh giới State và Ngoại biên hóa Dữ liệu (State Externalization):\n"
        "   - Tuân thủ nghiêm ngặt Factor VI (Processes are Stateless) của 12-Factor App: Tuyệt đối không lưu trữ tin nhắn hay trạng thái workflow trong RAM/Disk cục bộ của container, và KHÔNG dựa vào Sticky Session của bộ cân bằng tải.\n"
        "   - Phân chia hai ranh giới lưu trữ ngoại biên độc lập:\n"
        "     + `Conversation Messages Store` (PostgreSQL / DynamoDB): Lưu trữ toàn bộ lịch sử tin nhắn tuần tự, đảm bảo tính bền vững (durability) và toàn vẹn dữ liệu lâu dài.\n"
        "     + `Workflow Status & Execution Context` (Redis Cluster / Distributed Key-Value): Lưu trữ trạng thái máy trạng thái hiện tại (`step_id`, `state_variables`, `execution_locks`) với cơ chế TTL và khóa phân tán (Distributed Locks).\n"
        "   - Chu trình xử lý mỗi Request độc lập:\n"
        "     Nhận `conversation_id` -> Kéo state và 10 tin nhắn gần nhất từ Redis/DB -> Xử lý logic agent -> Ghi atomic commit cập nhật tin nhắn và status mới vào DB/Redis -> Trả response.\n"
        "2. Thiết kế Bộ kiểm thử Thay thế Replica (Replica Chaos & Swapping Test Suite):\n"
        "   - Bước 1 (Khởi tạo phiên trên Replica 1): Gửi Request 1 (`POST /chat`) tới Replica R1; tạo conversation C1, ghi tin nhắn M1, workflow status `awaiting_tool`. Xác nhận R1 ghi thành công vào DB và Redis.\n"
        "   - Bước 2 (Hủy diệt và Chuyển đổi Replica): Lập tức dừng tiến trình R1 (`docker stop R1`). Gửi tiếp Request 2 (`POST /chat` gửi tool output) qua Load Balancer; Load Balancer định tuyến tới Replica R2 hoàn toàn mới.\n"
        "   - Bước 3 (Kiểm tra Tính Toàn vẹn Context trên Replica 2): Khẳng định R2 truy vấn DB/Redis và tải đầy đủ ngữ cảnh tin nhắn M1 cùng trạng thái `awaiting_tool`, tiếp tục thực thi chuyển workflow sang `completed` và ghi nhận tin nhắn phản hồi M2.\n"
        "   - Bước 4 (Xác minh trên Replica 3): Gửi Request 3 tới Replica R3; xác nhận R3 trả về toàn bộ lịch sử [M1, M2] không bị mất mát hay suy thoái dữ liệu."
    ),
    "explanation": (
        "Trong môi trường điện toán đám mây hiện đại, container có thể bị hủy diệt hoặc thay thế bất kỳ lúc nào do quá trình autoscaling, rolling deploy hoặc node failure. Bằng cách ngoại biên hóa toàn bộ trạng thái vào các hệ thống lưu trữ phân tán chuyên trách, kiến trúc bảo đảm bất kỳ replica nào cũng có thể phục vụ bất kỳ request nào mà không cần duy trì kết nối dính (Sticky Sessions)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế kiến trúc Stateless Container hoàn chỉnh, bác bỏ sticky session và phân chia rõ ranh giới Messages vs Workflow Status.\n"
        "- [1.5 điểm] Mô tả chu trình đọc-xử lý-ghi atomic state với Redis và Persistent Database cho mỗi request độc lập.\n"
        "- [1.5 điểm] Xây dựng kịch bản kiểm thử Chaos Swapping đa replica chi tiết chứng minh tính toàn vẹn trạng thái khi thay thế container."
    ),
    "reference_source": "The Twelve-Factor App: Factor VI (Processes) & Martin Kleppmann - Designing Data-Intensive Applications"
}

# 20. d12-q042 (4 pts)
DAY12_PART1_B1["d12-q042"] = {
    "sample_answer": (
        "1. Thiết kế Khóa, Thứ tự, Giới hạn và TTL trong Redis (Storage Schema & Invariants):\n"
        "   - Cấu trúc Khóa phân vùng (Key Schema):\n"
        "     + Danh sách tin nhắn: `conv:{tenant_id}:{conversation_id}:messages` (Sử dụng Redis List hoặc Sorted Set).\n"
        "     + Khóa phân tán (Distributed Lock): `lock:conv:{tenant_id}:{conversation_id}`.\n"
        "   - Thứ tự Nghiêm ngặt (Strict Ordering): Lưu trữ các message theo thứ tự tăng dần thời gian (Monotonic sequence number hoặc epoch microsecond timestamp làm score trong Sorted Set `ZADD`).\n"
        "   - Giới hạn 20 Tin nhắn Tối đa (Bounded Invariant): Sử dụng lệnh cắt tỉa nguyên tử `LTRIM conv:{id}:messages -20 -1` (giữ lại đúng 20 phần tử cuối cùng) ngay sau mỗi thao tác đẩy tin nhắn mới `RPUSH`.\n"
        "   - TTL Động 24 Giờ (Sliding Expiration Invariant): Gọi lệnh `EXPIRE conv:{id}:messages 86400` sau mỗi hoạt động đọc/ghi, bảo đảm dữ liệu chỉ bị xóa sau đúng 24 giờ không có bất kỳ tương tác nào.\n"
        "2. Đảm bảo Tính Cô lập khi Hai Request Đến Đồng thời (Concurrency Isolation):\n"
        "   - Đóng gói toàn bộ chuỗi thao tác (Ghi message -> Cắt tỉa LTRIM -> Gia hạn EXPIRE) vào một Redis Lua Script thực thi nguyên tử, hoặc sử dụng Redis Mutex Lock với TTL ngắn (2 giây):\n"
        "     ```lua\n"
        "     local key = KEYS[1]\n"
        "     local message = ARGV[1]\n"
        "     local ttl = tonumber(ARGV[2])\n"
        "     redis.call('RPUSH', key, message)\n"
        "     redis.call('LTRIM', key, -20, -1)\n"
        "     redis.call('EXPIRE', key, ttl)\n"
        "     return redis.call('LLEN', key)\n"
        "     ```\n"
        "   - Lua script bảo đảm tính tuần tự hóa (Serialization): Hai request đồng thời sẽ được xếp hàng xử lý tuần tự, loại trừ hoàn toàn nguy cơ race condition làm vượt quá 20 tin nhắn.\n"
        "3. Thiết kế Bộ kiểm thử 4 Invariants (Isolation & Boundary Test Suite):\n"
        "   - Test Invariant 1 (Isolation & Order): Gửi đồng thời 2 request Req-A và Req-B trong cùng một mili-giây; xác nhận cả 2 đều được lưu thành công theo thứ tự tuần tự hóa, không có tin nhắn nào bị ghi đè hoặc mất.\n"
        "   - Test Invariant 2 (Bound Limit): Đẩy liên tiếp 25 tin nhắn vào conversation; kiểm tra `LLEN` trả về đúng bằng 20 và 5 tin nhắn đầu tiên đã bị cắt bỏ chính xác theo cơ chế FIFO.\n"
        "   - Test Invariant 3 (Sliding TTL): Kiểm tra TTL ban đầu bằng 86400; chờ 10 giây rồi gửi tin nhắn mới; kiểm tra TTL được gia hạn trở lại đúng 86400 giây."
    ),
    "explanation": (
        "Quản lý bộ nhớ đệm hội thoại với cửa sổ trượt (Sliding Window Conversation Cache) đòi hỏi sự kết hợp chặt chẽ giữa tính nguyên tử của thao tác dữ liệu và chính sách hết hạn động. Việc sử dụng Redis Lua Script để gộp các thao tác ghi, cắt tỉa và gia hạn TTL thành một khối nguyên tử duy nhất là giải pháp tối ưu giúp ngăn chặn race condition trong môi trường concurrency cao."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế key schema chuẩn xác và cơ chế tuần tự hóa thứ tự tin nhắn theo thời gian tăng dần.\n"
        "- [1.5 điểm] Thực thi nguyên tử giới hạn 20 message (LTRIM) và sliding TTL 24h (EXPIRE 86400) bằng Redis Lua Script / Lock.\n"
        "- [1.5 điểm] Xây dựng bộ kiểm thử độc lập cho cả 4 invariant: isolation khi ghi đồng thời, strict ordering, bound đúng 20 items và sliding TTL reset."
    ),
    "reference_source": "Redis Documentation - Transactions & Lua Scripting: https://redis.io/docs/manual/programmability/ và High Performance Redis Architecture Patterns"
}

# 21. d12-q044 (4 pts)
DAY12_PART1_B1["d12-q044"] = {
    "sample_answer": (
        "1. Thiết kế Worker và Điều phối Concurrency Hạ nguồn (Downstream Concurrency Throttling):\n"
        "   - Provider cho phép tối đa 20 cuộc gọi đồng thời. Triển khai Bộ Semaphore Phân tán (Distributed Semaphore qua Redis) hoặc Worker Pool có kích thước cố định `concurrency = 18` (dành 2 slot đệm phòng ngừa race condition và health checks).\n"
        "   - Worker chỉ được phép rút job từ hàng đợi khi acquire thành công một token từ Semaphore. Sau khi hoàn tất cuộc gọi model, token được release ngay lập tức.\n"
        "2. Thiết kế Giới hạn Hàng đợi và Quản lý Áp lực Ngược (Bounded Queue & Backpressure):\n"
        "   - Thiết lập Bounded Queue với dung lượng tối đa cố định (ví dụ `max_capacity = 40` jobs). Tuyệt đối cấm sử dụng Unbounded Queue vì khi 100 request đến dồn dập, hàng đợi vô hạn sẽ khiến thời gian chờ phình to và P95/P99 latency tăng vọt tới vài chục giây.\n"
        "   - Thiết lập Thời gian chờ Tối đa trong Hàng đợi (Queue Wait Timeout = 3.0 giây). Nếu một job nằm trong hàng đợi quá 3 giây mà chưa có worker nào xử lý, job sẽ bị hủy và trả về lỗi sớm.\n"
        "3. Hành vi khi Quá tải (Load Shedding & Overload Behavior):\n"
        "   - Khi hàng đợi đạt ngưỡng giới hạn 40 jobs hoặc Semaphore cạn kiệt:\n"
        "     + Kích hoạt cơ chế Đào thải Tải (Load Shedding) ngay tại tầng API Gateway.\n"
        "     + Phản hồi lập tức cho client với mã lỗi `HTTP 429 Too Many Requests` hoặc `HTTP 503 Service Unavailable`.\n"
        "     + Đính kèm header chỉ dẫn `Retry-After: 5` và mã lỗi `{ \"error\": \"system_overloaded\", \"retry_after\": 5 }`.\n"
        "   - Nhờ loại bỏ các request dư thừa, 18 request đang xử lý vẫn hoàn tất mượt mà, giữ P95 latency luôn dưới ngưỡng SLO.\n"
        "4. Bộ Tín hiệu Quan sát Đa chiều (Observability Signals):\n"
        "   - Không chỉ dựa vào CPU/RAM máy chủ. Giám sát các chỉ số cốt lõi:\n"
        "     + `active_provider_calls`: Số lượng cuộc gọi đang bay tới provider (ngưỡng cảnh báo: 18/20).\n"
        "     + `queue_depth`: Độ dài hàng đợi hiện tại.\n"
        "     + `queue_wait_duration_seconds`: Thời gian chờ trung bình và P95 trong queue.\n"
        "     + `load_shedding_drops_total`: Số lượng request bị gateway từ chối do quá tải."
    ),
    "explanation": (
        "Khi làm việc với các API bên thứ ba có giới hạn đồng thời cứng (Strict Concurrency Caps), việc mở rộng worker vô tội vạ sẽ dẫn đến vi phạm rate limit và làm tê liệt hệ thống. Mô hình Bounded Queue kết hợp Load Shedding và Distributed Semaphore cho phép hệ thống duy trì thông lượng tối đa trong phạm vi cho phép, bảo vệ độ trễ P95 và trả về phản hồi lịch sự cho người dùng khi xảy ra đợt tăng đột biến (traffic burst)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế bộ giới hạn concurrency hạ nguồn (Semaphore max <= 20) bảo vệ giới hạn của provider.\n"
        "- [1.5 điểm] Thiết kế hàng đợi có giới hạn (Bounded Queue) kèm timeout chờ ngăn ngừa latency P95 tăng vọt.\n"
        "- [1.5 điểm] Xác định hành vi Load Shedding khi quá tải (HTTP 429/503 kèm Retry-After) và thiết lập hệ thống quan sát đa chiều."
    ),
    "reference_source": "Google Site Reliability Engineering (SRE) Book - Addressing Cascading Failures & Handling Overload"
}

# 22. d12-q046 (4 pts)
DAY12_PART1_B1["d12-q046"] = {
    "sample_answer": (
        "1. Biện minh Duy trì Năng lực Ấm (Warm Capacity Justification vs Scale-to-Zero):\n"
        "   - Phân tích Rủi ro Vi phạm SLO: Mô hình Scale-to-Zero gây ra độ trễ Cold Start lên tới 18 giây cho request đầu tiên (do thời gian kéo image, khởi tạo runtime Python, nạp weights mô hình và thiết lập connection pools). Độ trễ 18 giây này vi phạm nghiêm trọng cam kết SLO độ trễ là 2 giây (vượt gấp 9 lần ngưỡng cho phép), gây ảnh hưởng tiêu cực nặng nề đến trải nghiệm người dùng.\n"
        "   - Đánh giá Cân đối Kinh tế (Cost-Benefit Balance): Bối cảnh chỉ rõ việc giữ 1 warm instance (`min_instances = 1` hoặc `provisioned_concurrency = 1`) là chi phí hoàn toàn nằm trong ngân sách chấp nhận được của doanh nghiệp. Khoản chi phí nhỏ này mang lại giá trị to lớn trong việc bảo vệ cam kết SLA và tính sẵn sàng của dịch vụ.\n"
        "2. Thiết kế Hành vi Khởi động và Deep Readiness Probe:\n"
        "   - Khởi tạo Eager Initialization trong Startup Hook: Tải toàn bộ model weights, kết nối sẵn sàng tới Vector DB và cache trong giai đoạn boot, trước khi mở cổng nhận traffic.\n"
        "   - Phân tách Rạch ròi Liveness và Readiness Probes:\n"
        "     + Liveness Probe (`/health/liveness`): Trả về HTTP 200 ngay khi tiến trình container khởi chạy thành công.\n"
        "     + Deep Readiness Probe (`/health/readiness`): Bắt buộc kiểm tra model đã sẵn sàng trong RAM và các kết nối phụ thuộc đã thông. Nếu đang trong quá trình nạp 18s, probe trả về `HTTP 503 Service Unavailable` để Load Balancer tuyệt đối không định tuyến bất kỳ request nào vào instance này.\n"
        "3. Chiến lược Co giãn Đón đầu Đợt Tăng Đột biến (Scheduled Autoscaling for Hourly Bursts):\n"
        "   - Vì đợt tăng lưu lượng có tính chu kỳ xác định ('burst mỗi giờ'), cấu hình Cron Autoscaler (như KEDA Cron Scaler hoặc GCP Scheduled Autoscaler) chủ động tăng số lượng replica từ 1 lên 5 instances trước thời điểm burst 5 phút để hấp thụ tải mà không gặp cold start."
    ),
    "explanation": (
        "Chiến lược quản trị hạ tầng Serverless/Container cho các ứng dụng AI đòi hỏi sự cân nhắc kỹ lưỡng giữa tối ưu hóa chi phí và bảo đảm cam kết chất lượng dịch vụ (SLO). Provisioned Warm Capacity kết hợp với Deep Readiness Probe bảo đảm hệ thống luôn sẵn sàng phục vụ với độ trễ thấp nhất, đồng thời Scheduled Autoscaling giúp đón đầu các đợt lưu lượng có quy luật định kỳ."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Biện minh định lượng việc duy trì warm capacity dựa trên vi phạm SLO nghiêm trọng (18s cold start vs 2s SLO).\n"
        "- [1.5 điểm] Thiết kế hành vi startup với eager initialization và phân tách rạch ròi Liveness vs Deep Readiness Probes.\n"
        "- [1.5 điểm] Xây dựng cơ chế Readiness Probe chặn định tuyến khi chưa sẵn sàng và đề xuất chiến lược Scheduled Scaling đón đầu burst hàng giờ."
    ),
    "reference_source": "Google Cloud Architecture Framework - Reliability: Cold Starts & AWS Lambda Provisioned Concurrency Guide"
}

# 23. d12-q048 (4 pts)
DAY12_PART1_B1["d12-q048"] = {
    "sample_answer": (
        "1. Vị trí Thực thi (Execution Placement) và Ranh giới Tin cậy (Trust Boundaries):\n"
        "   - Vị trí Edge / Thiết bị Cục bộ (On-Device Local Edge):\n"
        "     + Thực thi mô hình thị giác máy tính cục bộ (On-device Lightweight Computer Vision Model) trực tiếp trên chip xử lý NPU/GPU của camera.\n"
        "     + Ranh giới tin cậy: Vùng Thiết bị Không Tin cậy Hoàn toàn (Untrusted Device Boundary). Dữ liệu video thô và thông tin nhận dạng cá nhân (PII) được giữ lại 100% tại đây.\n"
        "   - Vị trí Cloud Backend (Enterprise Cloud VPC):\n"
        "     + Thực thi các tác vụ phân tích cấp cao, tổng hợp xu hướng và gọi công cụ doanh nghiệp.\n"
        "     + Ranh giới tin cậy: Vùng Doanh nghiệp An toàn (Secured Enterprise Perimeter) được bảo vệ bằng Private VPC và Zero-Trust Network.\n"
        "2. Đường đi Dữ liệu (Data Flow) và Vị trí Lưu trữ Credential:\n"
        "   - Đường đi dữ liệu:\n"
        "     `Video Frame thô (Camera Sensor)` -> Xử lý AI cục bộ tại Edge -> Trích xuất đặc trưng & Khử định danh (Anonymization/PII Redaction) -> Tạo bản tin thống kê tổng hợp (`Aggregated Event Payload`, ví dụ: 'đếm 5 người lúc 14:00') -> Gửi qua kênh mã hóa TLS 1.3 kèm User Consent Token lên Cloud API Gateway -> Cloud Agent xử lý nghiệp vụ.\n"
        "     *Lưu ý cốt tử: Video thô và hình ảnh khuôn mặt KHÔNG BAO GIỜ được gửi lên Cloud.*\n"
        "   - Vị trí Credential:\n"
        "     + Camera chỉ lưu giữ Short-lived Device Certificate hoặc Device JWT Token có phạm vi tối thiểu chỉ được phép đẩy telemetry/aggregates.\n"
        "     + Toàn bộ Enterprise Credentials, Database Passwords và API Keys của các công cụ doanh nghiệp được bảo mật 100% trong Cloud Secret Manager phía server; tuyệt đối không nạp vào firmware của camera.\n"
        "3. Phương án Dự phòng khi Mất mạng (Offline Fallback Strategy):\n"
        "   - Chế độ Cục bộ Độc lập (Standalone Local Mode): Khi mất kết nối Internet, camera tiếp tục thực thi nhận diện và kích hoạt các phản ứng cục bộ tức thì (nháy đèn báo động, đóng mở rơ-le cửa) với độ trễ siêu thấp < 20ms.\n"
        "   - Đệm Dữ liệu Bền vững (Local Persistent FIFO Buffer): Lưu các bản tin tổng hợp vào bộ nhớ flash/SQLite cục bộ. Khi kết nối mạng phục hồi, camera thực hiện đồng bộ bù (Catch-up Synchronization) có kiểm soát tốc độ để không làm nghẽn gateway."
    ),
    "explanation": (
        "Kiến trúc lai Biên - Đám mây (Edge-Cloud Hybrid Architecture) là mô hình chuẩn mực cho các hệ thống IoT/Camera thông minh. Bằng cách xử lý dữ liệu thô tại biên và chỉ gửi các bản tin tổng hợp đã khử định danh lên đám mây, hệ thống vừa đáp ứng yêu cầu độ trễ cực thấp và khả năng hoạt động offline, vừa bảo vệ tối đa quyền riêng tư của người dùng và an toàn bảo mật cho thông tin xác thực doanh nghiệp."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân định vị trí thực thi chính xác giữa On-Device Edge (low-latency offline) và Cloud Backend (aggregate analysis).\n"
        "- [1.0 điểm] Thiết lập đường đi dữ liệu an toàn: giữ video thô tại thiết bị, khử định danh trước khi truyền aggregate lên cloud.\n"
        "- [1.0 điểm] Xác định vị trí credential nghiêm ngặt: không chứa enterprise secret tại camera, quản lý tập trung ở Cloud Secret Manager.\n"
        "- [1.0 điểm] Xây dựng phương án dự phòng offline toàn diện: phản ứng cục bộ tức thì, local FIFO buffer và catch-up sync khi online."
    ),
    "reference_source": "NIST SP 800-145 Cloud Computing Guidelines & Edge AI Architecture Patterns for Privacy-Preserving Computer Vision"
}

print("Loaded Day 12 Part 1 b1 (questions 11 to 23).")
