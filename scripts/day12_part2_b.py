# scripts/day12_part2_b.py
# -*- coding: utf-8 -*-
"""
Day 12 Part 2 Sub-part B: Questions 49 to 60 (d12-q107 to d12-q130)
"""

DAY12_PART2_B = {}

# 49. d12-q107 (4 pts)
DAY12_PART2_B["d12-q107"] = {
    "sample_answer": (
        "1. Thiết kế Thí nghiệm Hỗn loạn có Kiểm soát (Controlled Chaos Engineering Experiment):\n"
        "   - Nhận định cần kiểm chứng (Hypothesis): 'Sự cố suy giảm hiệu năng hoặc chậm trễ nghiêm trọng của dịch vụ Search không được phép làm gián đoạn hay ảnh hưởng tới tính khả dụng của dịch vụ Thanh toán (Payment).'\n"
        "   - Kiểm soát Phạm vi Ảnh hưởng (Blast Radius Control):\n"
        "     Thí nghiệm được thực thi trên môi trường Pre-Production / Staging có lưu lượng tải mô phỏng, hoặc trên một tập hợp lưu lượng thử nghiệm nhỏ (1-2% synthetic canary traffic) trên production có gắn cờ thử nghiệm.\n"
        "   - Kịch bản Tiêm Lỗi (Fault Injection Scenario):\n"
        "     Sử dụng công cụ tiêm lỗi chuyên dụng (như Chaos Mesh, Toxiproxy hoặc Envoy Fault Injection Filter) can thiệp vào tầng mạng của Search Service:\n"
        "     + Tiêm độ trễ mạng nhân tạo: Thêm 15.000ms (15 giây) vào 100% các yêu cầu gửi tới Search Service.\n"
        "     + Tiêm lỗi sập kết nối: Giả lập Search Service trả về mã phản hồi `HTTP 504 Gateway Timeout`.\n"
        "2. Giám sát Chỉ số và Điều kiện Hủy Bỏ Khẩn cấp (Observability & Emergency Abort Conditions):\n"
        "   - Chỉ số Giám sát Trọng yếu (Steady-State Metrics):\n"
        "     + `payment_success_rate`: Tỷ lệ thành công của dịch vụ Payment (Kỳ vọng: Giữ vững $\\ge 99.99\\%$).\n"
        "     + `payment_latency_p99`: Độ trễ P99 của Payment (Kỳ vọng: Không tăng quá 5% so với mức cơ sở bình thường).\n"
        "     + `search_timeout_count`: Số lượng cuộc gọi search bị timeout ngắt mạch thành công.\n"
        "   - Điều kiện Dừng Khẩn cấp (Emergency Abort Threshold):\n"
        "     Nếu tại bất kỳ thời điểm nào tỷ lệ thành công của Payment giảm xuống dưới 99.5% hoặc độ trễ Payment P99 tăng quá 20%, hệ thống tự động kích hoạt ngắt thí nghiệm (Auto-Rollback) trong vòng dưới 3 giây.\n"
        "3. Kết luận và Tiêu chí Đánh giá Thành công:\n"
        "   - Thí nghiệm thành công khi: Search Service bị tắc nghẽn 15s nhưng hệ thống ngắt mạch sớm tại 1.5s, giao diện người dùng hiển thị thông báo giảm cấp nhẹ (degraded), và 100% các giao dịch Payment được hoàn tất trơn tru."
    ),
    "explanation": (
        "Thực hành Chaos Engineering có kiểm soát là phương pháp khoa học duy nhất để xác thực khả năng tự phục hồi và tính cô lập lỗi của kiến trúc phân tán. Bằng cách chủ động tiêm độ trễ vào các thành phần phi trọng yếu (như Search) dưới sự kiểm soát chặt chẽ của cơ chế dừng khẩn cấp, doanh nghiệp bảo đảm rằng các chức năng huyết mạch (như Payment) sẽ không bao giờ sụp đổ dây chuyền trong thực tế."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Xây dựng giả định kiểm chứng rõ ràng và thiết lập kiểm soát phạm vi ảnh hưởng (Blast Radius) chặt chẽ.\n"
        "- [1.5 điểm] Thiết kế kịch bản tiêm lỗi cụ thể (tiêm latency 15s / HTTP 504) bằng Toxiproxy hoặc Chaos Mesh.\n"
        "- [1.5 điểm] Xác định rõ các chỉ số giám sát cốt lõi của Payment và thiết lập cơ chế dừng khẩn cấp (Emergency Abort) tự động."
    ),
    "reference_source": "Principles of Chaos Engineering: https://principlesofchaos.org/ và Netflix Chaos Engineering Architecture Guide"
}

# 50. d12-q109 (4 pts)
DAY12_PART2_B["d12-q109"] = {
    "sample_answer": (
        "1. Thiết kế Lược đồ Sự kiện Phân tán (Distributed Tracing Event Schema - OpenTelemetry Standard):\n"
        "   - Cấu trúc bản ghi sự kiện JSON chuẩn hóa gắn cho từng bước chặng (Span Event):\n"
        "     ```json\n"
        "     {\n"
        "       \"trace_id\": \"4bf92f3577b34da6a3ce929d0e0e4736\",\n"
        "       \"span_id\": \"00f067aa0ba902b7\",\n"
        "       \"parent_span_id\": \"5fb397be34d23b0f\",\n"
        "       \"service_name\": \"agent_worker\",\n"
        "       \"operation_name\": \"invoke_tool\",\n"
        "       \"timestamp_start\": \"2026-10-23T15:30:00.120000Z\",\n"
        "       \"timestamp_end\": \"2026-10-23T15:30:02.450000Z\",\n"
        "       \"duration_ms\": 2330,\n"
        "       \"status\": {\"code\": \"ERROR\", \"http_status\": 502},\n"
        "       \"attributes\": {\n"
        "         \"hop.order\": 4,\n"
        "         \"hop.path\": \"gateway -> agent -> model -> tool\",\n"
        "         \"target.tool_name\": \"enterprise_database_query\",\n"
        "         \"error.type\": \"UpstreamConnectionRefused\",\n"
        "         \"error.message\": \"Tool endpoint returned HTTP 502 Bad Gateway due to connection timeout\"\n"
        "       }\n"
        "     }\n"
        "     ```\n"
        "2. Phép Truy vấn Chỉ số Metric Xác định Nguồn gốc Lỗi 502 (PromQL Metrics Queries):\n"
        "   - Truy vấn 1: Xác định dịch vụ cụ thể phát sinh lỗi 502 đầu tiên trong chuỗi phân tán:\n"
        "     ```promql\n"
        "     sum by (service_name, target_endpoint) (\n"
        "       rate(http_requests_total{status=\"502\"}[5m])\n"
        "     ) / sum by (service_name, target_endpoint) (\n"
        "       rate(http_requests_total[5m])\n"
        "     )\n"
        "     ```\n"
        "   - Truy vấn 2: Phân tích độ trễ P95 của các chặng dẫn tới lỗi 502:\n"
        "     ```promql\n"
        "     histogram_quantile(0.95, sum by (le, service_name) (\n"
        "       rate(http_request_duration_seconds_bucket{status=\"502\"}[5m])\n"
        "     ))\n"
        "     ```\n"
        "   - Truy vết gốc rễ (Root Cause Drilldown): Khi dashboard cảnh báo tỷ lệ lỗi 502 tăng vọt ở tầng Gateway, kỹ sư tra cứu `trace_id` trên Jaeger/Tempo; lược đồ span chỉ rõ điểm gãy nằm tại chặng cuối `tool` bị mất kết nối, làm lan truyền mã lỗi 502 ngược dòng về Model, Agent và Gateway."
    ),
    "explanation": (
        "Trong các hệ thống AI Agent nhiều tầng (Multi-Hop Agent Architecture), một mã lỗi 502 Bad Gateway tại cửa ngõ thường là hậu quả của sự cố ở mắt xích sâu nhất bên trong đồ thị gọi (như Tool hoặc Model). Việc áp dụng mô hình Distributed Tracing tuân thủ chuẩn OpenTelemetry kết hợp với các truy vấn PromQL phân tầng cho phép cô lập nguyên nhân gốc rễ chỉ trong vài giây."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Thiết kế Event Schema phân tán chuẩn OpenTelemetry với trace_id, span_id, parent_span_id và HTTP status.\n"
        "- [1.5 điểm] Định nghĩa đầy đủ các trường ngữ cảnh chặng (hop.path, service_name, error attributes) xác định điểm gãy tại tool.\n"
        "- [1.5 điểm] Xây dựng phép truy vấn PromQL chính xác tính tỷ lệ lỗi 502 theo từng dịch vụ và phương pháp drilldown qua trace_id."
    ),
    "reference_source": "OpenTelemetry Specification - Spans & Trace Semantic Conventions: https://opentelemetry.io/docs/specs/otel/trace/semantic_conventions/ và Prometheus PromQL Basics"
}

# 51. d12-q111 (4 pts)
DAY12_PART2_B["d12-q111"] = {
    "sample_answer": (
        "1. Gắn Nhãn Các Giai đoạn và Ranh giới Pipeline (Stage Labeling Matrix):\n"
        "   - Giai đoạn 1 (Pull Request CI Verification Stage):\n"
        "     + Nhãn: `ci-validation` (Môi trường kiểm thử ephemeral trên nhánh PR).\n"
        "     + Thực thi: Linter, unit tests, security scans. Phê duyệt bắt buộc: Tối thiểu 2 Senior Engineers duyệt mã nguồn.\n"
        "   - Giai đoạn 2 (Immutable Artifact Creation Stage):\n"
        "     + Nhãn: `build-and-package` (Kích hoạt khi merge vào nhánh `main`).\n"
        "     + Thực thi: Build OCI Container Image một lần duy nhất, tạo ra mã băm bất biến `Digest D` (`image@sha256:...`). Ký số hình ảnh bằng Cosign/Sigstore.\n"
        "   - Giai đoạn 3 (Staging Environment Promotion Stage):\n"
        "     + Nhãn: `staging-deployment`.\n"
        "     + Cơ chế: Tự động hoàn toàn (Automated Gate). Ngay khi Digest D được tạo và vượt qua bài quét lỗ hổng nghiêm trọng (No High/Critical CVEs), image được deploy ngay lập tức lên cụm Staging để chạy Integration và End-to-End Test Suite.\n"
        "   - Giai đoạn 4 (Production Environment Promotion Stage):\n"
        "     + Nhãn: `production-deployment`.\n"
        "     + Cơ chế: Cổng phê duyệt thủ công kết hợp điều kiện tự động (Manual Approval & Quality Gate).\n"
        "2. Mô tả Con đường Thăng cấp Bản phát hành (Promotion Pathway):\n"
        "   - Nguyên tắc Bất biến: 'Xây dựng Một lần, Triển khai Mọi nơi' (Build Once, Deploy Everywhere). Tuyệt đối cấm rebuild image khi thăng cấp từ Staging lên Production; chính xác Image Digest D đã được kiểm thử ở Staging sẽ được deploy lên Production.\n"
        "   - Điều kiện Tiên quyết để Mở Cổng Production:\n"
        "     + 100% các bài E2E test và Synthetic Canary trên Staging đạt kết quả PASS.\n"
        "     + Không phát hiện bất kỳ suy thoái độ trễ nào trong 2 giờ chạy thử trên Staging.\n"
        "     + Có văn bản phê duyệt điện tử (Electronic Sign-off) từ Release Manager / Tech Lead trên CI/CD console.\n"
        "   - Lộ trình Triển khai Production: Triển khai Canary 10% lưu lượng trong 30 phút -> Nếu ổn định, tự động thăng cấp lên 100% toàn hệ thống."
    ),
    "explanation": (
        "Quy trình thăng cấp phần mềm (Artifact Promotion Pipeline) bảo đảm tính toàn vẹn tuyệt đối của chuỗi cung ứng phần mềm. Bằng việc khóa danh tính bằng mã băm Digest bất biến và thiết lập các cổng kiểm duyệt phân cấp (tự động cho Staging, kiểm soát chặt chẽ cho Production), doanh nghiệp loại trừ hoàn toàn nguy cơ sai lệch nhị phân giữa môi trường kiểm thử và môi trường thực tế."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Gắn nhãn chính xác 4 giai đoạn vòng đời từ PR CI, Tạo Digest D bất biến, Staging đến Production.\n"
        "- [1.5 điểm] Phân định rạch ròi cơ chế cổng kiểm duyệt: Cổng tự động cho Staging và Cổng phê duyệt thủ công có kiểm soát cho Production.\n"
        "- [1.5 điểm] Mô tả đường promotion tuân thủ nguyên tắc Build Once Deploy Everywhere (giữ nguyên Digest D) kèm lộ trình Canary."
    ),
    "reference_source": "Continuous Delivery Principles by Jez Humble and David Farley & SLSA (Supply-chain Levels for Software Artifacts) Framework"
}

# 52. d12-q113 (5 pts) - 5 POINTS
DAY12_PART2_B["d12-q113"] = {
    "sample_answer": (
        "1. Dựng Đồ thị Có hướng Không chu trình (CI/CD Pipeline DAG Specification):\n"
        "   ```yaml\n"
        "   name: Secure Enterprise CI/CD Pipeline\n"
        "   on:\n"
        "     push:\n"
        "       branches: [ main ]\n"
        "     pull_request:\n"
        "       branches: [ main ]\n"
        "\n"
        "   jobs:\n"
        "     lint:\n"
        "       runs-on: ubuntu-latest\n"
        "       steps:\n"
        "         - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # Pinned full commit SHA\n"
        "         - name: Run Linters (Ruff / Flake8)\n"
        "           run: ruff check .\n"
        "\n"
        "     test:\n"
        "       runs-on: ubuntu-latest\n"
        "       steps:\n"
        "         - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11\n"
        "         - name: Run Test Suite (Pytest)\n"
        "           run: pytest tests/\n"
        "\n"
        "     build-image:\n"
        "       needs: [lint, test] # Phụ thuộc cả lint và test\n"
        "       runs-on: ubuntu-latest\n"
        "       steps:\n"
        "         - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11\n"
        "         - name: Build and Push OCI Image with Digest\n"
        "           run: docker build -t enterprise-agent:digest .\n"
        "\n"
        "     deploy:\n"
        "       needs: [build-image]\n"
        "       runs-on: ubuntu-latest\n"
        "       # Ràng buộc bảo mật nghiêm ngặt: Chỉ chạy trên main, trusted event và repository chính thức\n"
        "       if: github.ref == 'refs/heads/main' && github.event_name == 'push' && github.repository == 'enterprise/core-agent'\n"
        "       steps:\n"
        "         - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11\n"
        "         - name: Deploy to Cloud Production\n"
        "           run: ./scripts/deploy.sh\n"
        "   ```\n"
        "2. Mô tả Các Đường đi khi có Lỗi và Rẽ nhánh (Failure Paths & Security Branching):\n"
        "   - Đường đi 1 (Lỗi Linting - Lint Failure Path):\n"
        "     Khi `lint` phát hiện vi phạm cú pháp -> Job `lint` trả về exit code 1 (FAILED). Do `build-image` yêu cầu `needs: [lint, test]`, các job `build-image` và `deploy` lập tức bị HỦY BỎ (SKIPPED). Pipeline dừng lại ngay tại chốt kiểm soát đầu tiên.\n"
        "   - Đường đi 2 (Lỗi Kiểm thử - Test Failure Path):\n"
        "     Nếu `lint` thành công nhưng `test` thất bại (có unit test bị fail) -> Job `test` bị FAILED. Job `build-image` bị SKIPPED, ngăn chặn tuyệt đối việc đóng gói mã nguồn lỗi thành image container.\n"
        "   - Đường đi 3 (Nhánh Pull Request An toàn - Non-Main Branch Path):\n"
        "     Khi một PR được mở từ feature branch: Các job `lint`, `test` và `build-image` được thực thi đầy đủ để kiểm tra chất lượng. Tuy nhiên, khi tới job `deploy`, điều kiện `if` đánh giá thấy `github.ref != 'refs/heads/main'` -> Job `deploy` được ĐÁNH DẤU BỎ QUA (SKIPPED) một cách an toàn.\n"
        "   - Đường đi 4 (Sự kiện Không Tin cậy - Untrusted Fork Event Isolation):\n"
        "     Nếu kẻ tấn công gửi PR từ một fork repository bên ngoài nhằm kích hoạt deploy để đánh cắp secret, điều kiện `github.event_name == 'push'` và `github.repository` bảo đảm job `deploy` không bao giờ được phép khởi chạy."
    ),
    "explanation": (
        "Bảo mật quy trình CI/CD là tuyến phòng thủ cốt tử chống lại các cuộc tấn công vào chuỗi cung ứng phần mềm (Software Supply Chain Attacks). Việc ghim cứng mã băm commit SHA cho các hành động bên thứ ba (Pinned Actions) loại bỏ rủi ro bị xâm nhập qua cập nhật tag giả mạo, trong khi việc ràng buộc điều kiện nhánh và sự kiện tin cậy ngăn chặn việc rò rỉ quyền triển khai sản xuất ra các môi trường không được kiểm soát."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 5 điểm):\n"
        "- [1.0 điểm] Thiết kế cấu trúc DAG chuẩn xác với các quan hệ phụ thuộc: lint và test chạy song song -> build-image -> deploy.\n"
        "- [2.0 điểm] Thực thi đầy đủ các ràng buộc bảo mật cho deploy: chỉ chạy trên main, sự kiện push tin cậy và pinned actions với full SHA hash.\n"
        "- [2.0 điểm] Mô tả toàn diện 4 nhánh rẽ khi có lỗi: lint fail, test fail, PR branch skipped deploy và untrusted fork isolation."
    ),
    "reference_source": "GitHub Actions Security Hardening Guide: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions và OpenSSF Scorecard Standards"
}

# 53. d12-q115 (4 pts)
DAY12_PART2_B["d12-q115"] = {
    "sample_answer": (
        "1. Xếp Các Bài Kiểm tra vào Đúng Giai đoạn Vòng đời Pipeline (Test Phase Mapping):\n"
        "   - Giai đoạn 1: Giai đoạn Tiền Xây dựng (Pre-Build / CI Source Validation):\n"
        "     + Bài kiểm tra: `Unit Test dùng Mock`.\n"
        "     + Lý do: Chạy trực tiếp trên mã nguồn thô trong vài giây, sử dụng mock để cô lập các dịch vụ bên ngoài, kiểm tra logic thuật toán nội bộ trước khi tiêu tốn tài nguyên đóng gói.\n"
        "   - Giai đoạn 2: Giai đoạn Đóng gói (Build & Packaging Stage):\n"
        "     + Tác vụ: `Build Container`.\n"
        "     + Lý do: Đóng gói mã nguồn và dependencies thành OCI Container Image, chạy bảo mật quét lỗ hổng lớp image.\n"
        "   - Giai đoạn 3: Giai đoạn Hậu Triển khai (Post-Deployment Verification Stage):\n"
        "     + Bài kiểm tra: `Smoke Test trên Public URL`.\n"
        "     + Lý do: Bắt buộc phải chạy SAU KHI container đã được triển khai lên môi trường chạy thực tế và endpoint công khai đã sẵn sàng nhận kết nối mạng.\n"
        "2. Phân tích Sai sót và Cách Sửa Bài Kiểm tra Tự Tham chiếu (Self-Referential Test Fix):\n"
        "   - Phân tích Sai sót (Chicken-and-Egg Flaw):\n"
        "     Bài kiểm tra kiểm tra badge hoặc trạng thái 'Success' của chính workflow khi bản thân workflow đó CÒN CHƯA HOÀN TẤT là một lỗi thiết kế nghiêm trọng về mặt logic (Self-Referential / Paradoxical Flaw). Tại thời điểm test đang chạy, trạng thái của workflow chỉ có thể là `in_progress` hoặc trạng thái của commit cũ; việc kỳ vọng nhận được trạng thái `success` của chính lần chạy hiện tại sẽ gây ra lỗi Fail giả tạo (False Negative) hoặc tạo ra vòng lặp bế tắc vô lý.\n"
        "   - Cách Sửa Triệt để (Architectural Remediation):\n"
        "     + Giải pháp Chuẩn mực: LOẠI BỎ HOÀN TOÀN bài test tự kiểm tra trạng thái khỏi chuỗi công việc của chính nó.\n"
        "     + Phương án Thay thế 1 (Asynchronous Status Badge Verification): Chuyển tác vụ kiểm tra hiển thị badge sang một Cron Job hoặc External Health Monitor độc lập chạy định kỳ bên ngoài pipeline.\n"
        "     + Phương án Thay thế 2 (Check Previous Commit Status): Nếu bắt buộc phải kiểm tra trong pipeline, chỉ kiểm tra trạng thái hoàn tất của lần chạy trước đó trên nhánh chính (`workflow_runs(status=completed, branch=main).conclusion == success`)."
    ),
    "explanation": (
        "Thiết kế quy trình kiểm thử tự động đòi hỏi tính logic nhân quả nghiêm ngặt. Việc sắp xếp đúng thứ tự từ Unit Test (cô lập) đến Build (đóng gói) và Smoke Test (môi trường sống) bảo đảm tính hiệu quả của chu trình phản hồi. Loại bỏ các phép kiểm tra tự tham chiếu giải quyết các nghịch lý logic và ngăn chặn các báo động giả trong hệ thống CI/CD."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân loại chính xác 3 bài kiểm tra vào 3 giai đoạn: Unit test (Pre-build), Build container (Build), Smoke test (Post-deploy).\n"
        "- [1.5 điểm] Chỉ ra chính xác nghịch lý logic của bài kiểm tra tự tham chiếu (workflow chưa kết thúc không thể có trạng thái success).\n"
        "- [1.5 điểm] Nêu giải pháp sửa triệt để: loại bỏ khỏi pipeline hiện tại, chuyển sang external cron monitor hoặc kiểm tra commit trước đó."
    ),
    "reference_source": "Google Testing Blog - Test Sizes & Pipeline Ordering và Martin Fowler - Continuous Integration Guide"
}

# 54. d12-q117 (4 pts)
DAY12_PART2_B["d12-q117"] = {
    "sample_answer": (
        "1. Quyết định Quản trị Bản phát hành (Release Governance Decision):\n"
        "   - QUYẾT ĐỊNH DỨT KHOÁT: TIẾN HÀNH ROLLBACK NGAY LẬP TỨC VỀ BẢN D6 (IMMEDIATE AUTOMATED ROLLBACK).\n"
        "   - Biện minh dựa trên đánh giá tổng thể ba tín hiệu:\n"
        "     + Tín hiệu 1 (Identity): Endpoint `/version` trả về đúng Digest D7 -> Xác nhận việc triển khai kỹ thuật đã đưa đúng mã nhị phân mới lên hạ tầng.\n"
        "     + Tín hiệu 2 (Health Check): Endpoint `/health` trả về thành công -> Đây chỉ là một phép kiểm tra nông (Shallow Liveness Check), chỉ chứng minh tiến trình web server còn sống, nhưng không phản ánh được chức năng thực tế.\n"
        "     + Tín hiệu 3 (Functional Execution): Yêu cầu tối thiểu có xác thực (Critical Authenticated Path) bị lỗi sập hoàn toàn với mã lỗi `HTTP 500 Internal Server Error` -> Dịch vụ không thể phục vụ người dùng thực tế. Đây là sự cố nghiêm trọng cấp độ P1 (Blocking Severity); không thể giữ bản release D7 trong sản xuất.\n"
        "2. Thu thập và Ghi nhận Bằng chứng Kiểm toán Sự cố (Incident Audit Trail):\n"
        "   - Bằng chứng 1 (Bằng chứng Ba Tín hiệu Đối lập):\n"
        "     Lưu trữ bản ghi HTTP response song song: Lệnh gọi `/version` (Digest D7), lệnh gọi `/health` (HTTP 200) và lệnh gọi API có xác thực `curl -i -H 'Authorization: Bearer <test_token>' https://api.enterprise.com/v1/agent` trả về `HTTP/1.1 500 Internal Server Error` kèm Request Trace ID.\n"
        "   - Bằng chứng 2 (Nhật ký Truy vết Ngăn xếp Lỗi - Stacktrace Logs):\n"
        "     Trích xuất log lỗi từ container D7 tại thời điểm nhận request: Lưu lại toàn bộ traceback chi tiết (ví dụ: lỗi `KeyError: 'JWT_PUBLIC_KEY'` hoặc thiếu bảng migration mới).\n"
        "   - Bằng chứng 3 (Bản ghi Thao tác Hoàn tác - Rollback Audit Record):\n"
        "     Ghi nhật ký hệ thống: Thời điểm phát hiện sự cố, định danh người/hệ thống kích hoạt lệnh Rollback, thời gian hoàn tất chuyển hướng traffic về D6 (ví dụ: hoàn tất sau 12 giây), và xác nhận đường dẫn có xác thực trên D6 đã phục hồi trạng thái HTTP 200 hoàn hảo."
    ),
    "explanation": (
        "Trong quy trình phát hành phần mềm hiện đại, việc một ứng dụng vượt qua bài kiểm tra sức khỏe nông (Shallow Health Check) không đồng nghĩa với việc ứng dụng hoạt động chính xác. Khi các luồng nghiệp vụ cốt lõi có xác thực gặp lỗi nghiêm trọng (HTTP 500), nguyên tắc 'Fail-Safe' yêu cầu kích hoạt hoàn tác khẩn cấp ngay lập tức để bảo vệ người dùng, đồng thời lưu giữ đầy đủ bằng chứng để phục vụ công tác điều tra nguyên nhân gốc rễ (Post-Mortem)."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Đưa ra quyết định chuẩn xác: Rollback khẩn cấp về bản D6 ngay lập tức dựa trên sự cố lỗi 500 nghiêm trọng.\n"
        "- [1.5 điểm] Phân tích toàn diện 3 tín hiệu đối lập: Phân biệt sự sai khác giữa shallow health check (200) và deep authenticated failure (500).\n"
        "- [1.5 điểm] Thiết lập bằng chứng kiểm toán đầy đủ: Log 3 tín hiệu, stacktrace lỗi của container D7 và bản ghi xác nhận rollback thành công về D6."
    ),
    "reference_source": "Google SRE Book - Postmortem Culture & Incident Response: https://sre.google/sre-book/postmortem-culture/ và AWS Deployment Safety Best Practices"
}

# 55. d12-q119 (4 pts)
DAY12_PART2_B["d12-q119"] = {
    "sample_answer": (
        "1. Lọc và Đánh giá Ứng viên theo Chính sách Tuân thủ (Compliance & Policy Filtering):\n"
        "   - Ứng viên Primary (Nhà cung cấp Chính):\n"
        "     + Đánh giá chính sách: Thỏa mãn hoàn toàn về pháp lý và ngân sách.\n"
        "     + Trạng thái kỹ thuật: BỊ RATE LIMIT (Mã lỗi HTTP 429) -> Tạm thời không thể tiếp nhận cuộc gọi.\n"
        "   - Ứng viên F1 (Phương án Dự phòng 1):\n"
        "     + Trạng thái kỹ thuật: Đang hoạt động hoàn hảo (Healthy).\n"
        "     + Đánh giá chính sách: VI PHẠM CHÍNH SÁCH VÙNG DỮ LIỆU (Data Residency / Sovereignty Policy Violation - ví dụ: Dữ liệu bắt buộc lưu trữ tại EU nhưng F1 đặt tại US).\n"
        "     + Quyết định: LOẠI BỎ NGAY LẬP TỨC KHỎI DANH SÁCH ĐỊNH TUYẾN. Nguyên tắc tuân thủ pháp luật và an ninh dữ liệu là tuyệt đối; không bao giờ được phép vi phạm quy định chủ quyền dữ liệu chỉ để cứu vãn tính sẵn sàng của hệ thống.\n"
        "   - Ứng viên F2 (Phương án Dự phòng 2):\n"
        "     + Đánh giá chính sách dữ liệu: Tương thích hoàn toàn (đúng data region).\n"
        "     + Đánh giá chính sách tài chính: ĐÃ CHẠM TRẦN NGÂN SÁCH (Budget Cap Exhausted).\n"
        "     + Quyết định: LOẠI BỎ KHỎI DANH SÁCH ĐỊNH TUYẾN để bảo vệ doanh nghiệp khỏi nguy cơ thâm hụt tài chính.\n"
        "2. Tính toán Chuỗi Định tuyến / Chuyển hướng Dự phòng (Route & Failover Pipeline):\n"
        "   - Trình tự đánh giá logic của hệ thống:\n"
        "     `Request -> Thử nghiệm Primary (Nhận 429) -> Đánh giá F1 (LOẠI BỎ do sai Data Region) -> Đánh giá F2 (LOẠI BỎ do hết Budget) -> KẾT THÚC: KHÔNG CÒN ROUTE HỢP LỆ NÀO KHẢ DỤNG.`\n"
        "3. Kết quả Xử lý khi Không Còn Route Hợp lệ (Terminal Exhaustion Handling):\n"
        "   - Hành vi Hệ thống: Ngắn mạch ngay lập tức (Fail-Fast Short Circuit), không gửi thêm bất kỳ request nào ra ngoài Internet.\n"
        "   - Phản hồi cho Người dùng: Trả về mã phản hồi `HTTP 503 Service Unavailable` hoặc `HTTP 429 Upstream Rate Limited`.\n"
        "   - Thân phản hồi JSON chi tiết:\n"
        "     `{\"error\": \"service_unavailable\", \"reason\": \"Primary model rate limited and all fallback routes failed compliance/budget guardrails\", \"retry_after\": 15}`.\n"
        "   - Cảnh báo Hệ thống: Phát tín hiệu cảnh báo mức độ khẩn cấp (P1 Alert) tới kênh trực vận hành của đội ngũ SRE để can thiệp nâng quota hoặc bổ sung ngân sách."
    ),
    "explanation": (
        "Trong thiết kế kiến trúc chuyển hướng dự phòng (Failover Architecture) cho các dịch vụ AI doanh nghiệp, các chốt chặn tuân thủ quy định (Compliance Guardrails như Chủ quyền Dữ liệu và Giới hạn Ngân sách) có độ ưu tiên cao hơn tính sẵn sàng kỹ thuật. Một giải pháp dự phòng dù khỏe mạnh về mặt mạng nhưng vi phạm pháp lý hoặc làm thủng ngân sách bắt buộc phải bị loại bỏ dứt khoát."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính sách lọc nghiêm ngặt: Loại F1 do vi phạm Data Region và loại F2 do cạn kiệt Budget Cap.\n"
        "- [1.5 điểm] Tính toán chính xác chuỗi failover: Primary (429) -> F1 (bị chặn) -> F2 (bị chặn) dẫn tới cạn kiệt toàn bộ routes hợp lệ.\n"
        "- [1.5 điểm] Xác định chuẩn xác hành vi ngắn mạch: Phản hồi mã HTTP 503 kèm lý do minh bạch và phát cảnh báo khẩn cấp cho SRE."
    ),
    "reference_source": "AWS Well-Architected Framework - Reliability and Security Pillars & GDPR Data Residency Compliance Guidelines"
}

# 56. d12-q121 (4 pts)
DAY12_PART2_B["d12-q121"] = {
    "sample_answer": (
        "1. Phân loại Hit / Miss Dựa trên Thứ bậc Khóa Đệm Ngữ nghĩa (Semantic Cache Key Hierarchy):\n"
        "   - Cấu trúc Khóa Đệm Hoàn chỉnh (Composite Cache Key Structure):\n"
        "     Khóa lưu trữ trong Semantic Cache phải được cấu thành từ 4 yếu tố bắt buộc:\n"
        "     `Cache_Key = Hash(Model_Identity, System_Prompt_Policy_Hash, Knowledge_Source_Version, Query_Embedding)`\n"
        "   - Đối chiếu với các điều kiện trong bối cảnh:\n"
        "     + Knowledge Source: Đã được nâng cấp từ phiên bản `v3` lên `v4` (Tri thức nền tảng đã thay đổi).\n"
        "     + Policy Prompt: Đã thay đổi nội dung (Chính sách an toàn, giọng điệu hoặc định dạng đầu ra mới).\n"
        "     + Query: Có ý nghĩa ngữ nghĩa gần giống với một bản ghi cũ đã lưu.\n"
        "   - Kết luận Phân loại: CACHE MISS (hoặc CACHE ENTRY BỊ VÔ HIỆU HÓA HOÀN TOÀN).\n"
        "     Lý do: Mặc dù vector ngữ nghĩa của câu hỏi có độ tương đồng cosine rất cao ($\ge 0.95$), nhưng việc Knowledge Source và Policy Prompt thay đổi đã làm gãy ranh giới hợp lệ của bản ghi cũ. Nếu trả về kết quả cũ, hệ thống sẽ cung cấp thông tin sai lệch, lỗi thời và vi phạm chính sách mới của doanh nghiệp.\n"
        "2. Quyết định Vô hiệu hóa và Chiến lược Thực thi (Invalidation Decision & Execution):\n"
        "   - Quyết định: VÔ HIỆU HÓA TOÀN BỘ CÁC BẢN GHI ĐƯỢC TẠO DƯỚI SOURCE V3 VÀ PROMPT POLICY CŨ.\n"
        "   - Chiến lược Vô hiệu hóa Không gian Tên theo Phiên bản (Version-Based Namespacing Invalidation):\n"
        "     Thay vì phải duyệt tìm và xóa hàng triệu khóa tốn kém trong bộ nhớ, hệ thống chỉ cần cập nhật tiền tố không gian tên toàn cục (Global Cache Namespace):\n"
        "     `active_namespace = \"prompt_v2:source_v4\"`.\n"
        "     Mọi truy vấn mới sẽ tự động tra cứu trong namespace mới. Các bản ghi thuộc `source_v3` cũ sẽ tự động bị bỏ qua và được hệ thống dọn dẹp dần theo chính sách TTL tự nhiên.\n"
        "   - Luồng Thực thi Tiếp theo: Đưa yêu cầu tới Model Provider cùng tài liệu v4 và prompt policy mới, sau đó lưu kết quả phản hồi mới vào cache với khóa thuộc namespace v4."
    ),
    "explanation": (
        "Bộ nhớ đệm ngữ nghĩa (Semantic Caching) trong các ứng dụng AI đòi hỏi sự quản lý nghiêm ngặt về tính hợp lệ của tri thức. Độ tương đồng ngữ nghĩa của câu hỏi chỉ có giá trị khi ngữ cảnh tri thức nền tảng và chính sách vận hành được giữ nguyên. Việc vô hiệu hóa cache theo không gian tên phiên bản bảo đảm câu trả lời luôn cập nhật tri thức mới nhất mà không gây suy thoái hiệu năng tra cứu."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân loại chính xác CACHE MISS do sự thay đổi của Knowledge Source (v3 -> v4) và Policy Prompt.\n"
        "- [1.5 điểm] Thiết lập cấu trúc khóa cache đa thành phần kết hợp: Model, Prompt Hash, Source Version và Query Embedding.\n"
        "- [1.5 điểm] Đưa ra quyết định vô hiệu hóa toàn diện bằng chiến lược Version-Based Namespacing và định tuyến gọi model mới."
    ),
    "reference_source": "GPTCache Architectural Patterns: https://github.com/zilliztech/GPTCache và Redis Semantic Caching Best Practices"
}

# 57. d12-q124 (4 pts)
DAY12_PART2_B["d12-q124"] = {
    "sample_answer": (
        "1. So sánh Lịch Thực thi của Static Batching và Continuous Batching:\n"
        "   - Bối cảnh: Ba yêu cầu A, B, C có độ dài sinh token đầu ra lần lượt là: A cần 2 tokens, B cần 10 tokens, C cần 3 tokens. Giả sử ban đầu batch có 2 slots xử lý A và B. Slot của A rỗng sau bước giải mã thứ 2.\n"
        "   - Kịch bản 1: Gom cụm Tĩnh Truyền thống (Static Batching):\n"
        "     + Bước 1 - 2: A và B cùng chạy trong batch. Sau bước 2, Request A hoàn tất (đủ 2 tokens).\n"
        "     + Bước 3 - 10: Do Static Batching khóa cứng toàn bộ batch cho đến khi request dài nhất (B cần 10 tokens) kết thúc hoàn toàn, slot của A bị BỎ TRỐNG LÃNG PHÍ (Wasted Idle Bubble) suốt 8 bước tiếp theo.\n"
        "     + Request C (cần 3 tokens) BỊ BẮT BUỘC PHẢI CHỜ ĐỢI trong hàng đợi ngoài cho đến hết bước 10.\n"
        "     + Bước 11 - 13: Request C mới được đưa vào batch mới và chạy trong 3 bước.\n"
        "     + Tổng thời gian hoàn tất cả 3 requests: $10 \\text{ bước (Batch 1)} + 3 \\text{ bước (Batch 2)} = 13 \\text{ bước giải mã (Decode Steps)}$.\n"
        "   - Kịch bản 2: Gom cụm Liên tục (Continuous Batching / Iteration-Level Scheduling):\n"
        "     + Bước 1 - 2: A và B cùng chạy trong batch.\n"
        "     + Bước 2: Request A hoàn tất. Hệ thống lập tức giải phóng (evict) A ra khỏi slot.\n"
        "     + Bước 3: Request C ĐƯỢC CHÈN NGAY VÀO SLOT RỖNG VỪA GIẢI PHÓNG ở cấp độ từng bước lặp (Iteration level). Slot không bị rảnh một giây nào.\n"
        "     + Bước 3 - 5: B và C chạy song song cùng nhau. Đến hết bước 5, Request C hoàn tất (đủ 3 tokens).\n"
        "     + Bước 6 - 10: Slot của C giải phóng, B tiếp tục chạy nốt 5 bước cuối cùng cho đến khi hoàn tất ở bước 10.\n"
        "     + Tổng thời gian hoàn tất cả 3 requests: CHỈ MẤT ĐÚNG 10 BƯỚC GIẢI MÃ.\n"
        "2. Đánh giá Hiệu năng và Tiết kiệm Tài nguyên:\n"
        "   - Continuous Batching tiết kiệm $13 - 10 = 3$ bước giải mã (giảm $\\approx 23\\%$ tổng thời gian thực thi).\n"
        "   - Triệt tiêu hoàn toàn hiện tượng bong bóng rỗi GPU (Zero GPU Idle Bubbles), tăng gấp đôi thông lượng phục vụ (Throughput) và giảm mạnh thời gian chờ đợi (Queue Wait Time) của Request C."
    ),
    "explanation": (
        "Kỹ thuật Continuous Batching (hay Iteration-Level Batching do vLLM và Orca tiên phong) đã thay đổi hoàn toàn cách thức phục vụ mô hình ngôn ngữ lớn. Bằng cách cho phép các yêu cầu mới gia nhập batch ngay khi có một yêu cầu khác hoàn tất ở cấp độ từng token lặp, hệ thống tối đa hóa mức độ sử dụng tính toán của GPU và loại bỏ hoàn toàn sự lãng phí tài nguyên do độ dài văn bản không đồng nhất."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác hạn chế của Static Batching: Slot A bị bỏ trống 8 bước và C phải chờ hết bước 10 mới được vào (tổng 13 bước).\n"
        "- [1.5 điểm] Mô tả chính xác cơ chế Continuous Batching: C được nạp ngay vào slot của A ở bước 3, chạy song song với B và hoàn tất ở bước 5.\n"
        "- [1.5 điểm] So sánh định lượng thời gian: Continuous Batching chỉ tốn 10 bước (tiết kiệm 23% thời gian) và triệt tiêu GPU bubbles."
    ),
    "reference_source": "Orca: A Distributed Serving System for Transformer-Based Generative Models (OSDI '22) & vLLM Continuous Batching Architecture"
}

# 58. d12-q126 (4 pts)
DAY12_PART2_B["d12-q126"] = {
    "sample_answer": (
        "1. Tính toán Số lượng Block và Slot Phân bổ theo Cơ chế PagedAttention:\n"
        "   - Thông số hệ thống:\n"
        "     + Ngân sách tối đa của GPU: $160$ KV token slots.\n"
        "     + Kích thước mỗi khối bộ nhớ (Block Size): $B = 16$ tokens/block.\n"
        "     + Tổng số block bộ nhớ vật lý trên GPU: $160 / 16 = 10$ physical blocks.\n"
        "     + Số lượng chuỗi cần phục vụ: $5$ sequences, mỗi chuỗi có độ dài $L = 17$ tokens.\n"
        "   - Tính toán Phân bổ Khối cho Một Chuỗi Đơn lẻ (Per-Sequence Allocation):\n"
        "     + Vì độ dài chuỗi là 17 tokens, vượt quá dung lượng 16 tokens của một block đơn lẻ, thuật toán quản lý bộ nhớ trang (PagedAttention) bắt buộc phải cấp phát 2 blocks nguyên vẹn:\n"
        "       $\\text{Blocks required per sequence} = \\lceil 17 / 16 \\rceil = 2 \\text{ blocks}$.\n"
        "     + Tổng số slots bị cấp phát cho 1 chuỗi: $2 \\times 16 = 32$ slots.\n"
        "     + Phân tích lãng phí nội bộ (Internal Fragmentation): Trong 32 slots được cấp phát, có 17 slots chứa token thực tế, và có $32 - 17 = 15$ slots bị bỏ trống (lãng phí phân mảnh) trong block thứ hai.\n"
        "2. Đánh giá Ảnh hưởng Toàn cục Lên Năng lực Phục vụ của GPU (Capacity Impact):\n"
        "   - Tổng số block thực tế bị chiếm dụng bởi 5 chuỗi:\n"
        "     $5 \\text{ sequences} \\times 2 \\text{ blocks} = 10 \\text{ physical blocks}$.\n"
        "   - Tổng số slot bộ nhớ bị khóa chặt trên GPU:\n"
        "     $10 \\text{ blocks} \\times 16 \\text{ slots/block} = 160 \\text{ token slots}$.\n"
        "   - Đánh giá Năng lực Phục vụ Còn lại (Available Capacity):\n"
        "     $160 \\text{ slots bị chiếm} / 160 \\text{ slots ngân sách} = 100\\%$ dung lượng bộ nhớ KV Cache ĐÃ BỊ LẤP ĐẦY HOÀN TOÀN (0 block và 0 slot trống còn lại).\n"
        "   - Kết luận Tác động Kỹ thuật:\n"
        "     Mặc dù tổng số token hữu ích thực tế chỉ là $5 \\times 17 = 85$ tokens (chỉ chiếm $53.125\\%$ tổng dung lượng vật lý), nhưng do hiện tượng phân mảnh khối nội bộ ($5 \\times 15 = 75$ slots lãng phí, chiếm $46.875\\%$ dung lượng), toàn bộ GPU đã bị cạn kiệt bộ nhớ. Hệ thống KHÔNG THỂ TIẾP NHẬN THÊM BẤT KỲ YÊU CẦU MỚI NÀO và sẽ xảy ra hiện tượng OOM hoặc bắt buộc phải kích hoạt cơ chế hoán đổi (Swapping/Preemption) nếu bất kỳ chuỗi nào sinh thêm token tiếp theo."
    ),
    "explanation": (
        "PagedAttention (sử dụng trong vLLM) giải quyết triệt để sự phân mảnh bộ nhớ bên ngoài của KV Cache bằng cách phân bổ các block kích thước cố định. Tuy nhiên, sự phân mảnh bên trong (Internal Fragmentation) vẫn xảy ra khi chuỗi văn bản vượt qua ranh giới block một lượng token rất nhỏ. Hiểu rõ sự đánh đổi này giúp các kỹ sư điều chỉnh kích thước block size phù hợp với đặc thù độ dài dữ liệu của doanh nghiệp."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Tính toán chính xác mỗi sequence 17 tokens cần 2 blocks (32 slots) theo thuật toán PagedAttention.\n"
        "- [1.5 điểm] Tính toán chính xác 5 sequence chiếm trọn 10 blocks (160 slots), lấp đầy 100% ngân sách bộ nhớ GPU.\n"
        "- [1.5 điểm] Chỉ ra rõ ràng nghịch lý phân mảnh: chỉ có 85 tokens thực tế (53%) nhưng lãng phí 75 slots (47%), làm cạn kiệt năng lực nhận thêm request."
    ),
    "reference_source": "Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM Paper, SOSP '23)"
}

# 59. d12-q128 (4 pts)
DAY12_PART2_B["d12-q128"] = {
    "sample_answer": (
        "1. Phân tích Nguyên lý Hoạt động của Suy luận Đầu cơ (Speculative Decoding Principles):\n"
        "   - Cơ chế cốt lõi: Một mô hình phác thảo nhỏ và siêu nhanh (Draft Model) sinh trước một chuỗi $K$ tokens giả định với chi phí thấp. Sau đó, mô hình mục tiêu lớn (Target Model) chỉ cần chạy đúng 1 lần tính toán song song (Forward Pass) để xác thực và chấp thuận hoặc bác bỏ các token đề xuất đó.\n"
        "   - Điều kiện Tiên quyết để Đạt Tăng tốc Hiệu quả (Speedup Conditions):\n"
        "     + Tốc độ sinh của Draft Model phải nhanh hơn Target Model rất nhiều lần ($T_{draft} \\ll T_{target}$, thường nhanh hơn từ 5 đến 10 lần).\n"
        "     + Tỷ lệ Chấp thuận Token (Acceptance Rate $\\alpha$) phải ở mức cao (thường $\\alpha \\ge 65-80\\%$).\n"
        "2. So sánh Khối lượng Tính toán (Work) và Độ trễ (Latency) trong Điều kiện Đề bài:\n"
        "   - Bối cảnh đề bài: 'Draft model chậm gần bằng target ($T_{draft} \\approx T_{target}$)' và 'Tỷ lệ proposal được chấp nhận rất thấp (ví dụ $\\alpha \\approx 10-20\\%$)'.\n"
        "   - So sánh Khối lượng Công việc Tính toán (Computational Work / FLOPs):\n"
        "     Trong Speculative Decoding, hệ thống phải thực hiện tính toán trên CẢ HAI MÔ HÌNH: Chạy $K$ bước trên Draft Model, cộng thêm 1 lần chạy trên Target Model để kiểm chứng và sửa lỗi. Do phần lớn các token bị bác bỏ, tổng khối lượng tính toán (FLOPs) GẤP GẦN 2 LẦN so với phương pháp Decoding thông thường, gây lãng phí năng lượng và tài nguyên tính toán GPU cực lớn.\n"
        "   - So sánh Độ trễ Thực tế (Wall-Clock Latency):\n"
        "     Thời gian để sinh một số lượng token nhất định:\n"
        "     $T_{speculative} = K \\times T_{draft} + T_{target\\_verify} + T_{recovery}$.\n"
        "     Vì $T_{draft} \\approx T_{target}$ và hầu hết các token đề xuất đều bị vứt bỏ, thời gian bỏ ra để sinh các token nháp bị lãng phí hoàn toàn mà Target Model vẫn phải tự sinh lại từ đầu. Kết quả: ĐỘ TRỄ CỦA SPECULATIVE DECODING CAO HƠN ĐÁNG KỂ SO VỚI DECODING THÔNG THƯỜNG ($T_{speculative} > T_{standard}$).\n"
        "3. Kết luận và Khuyến nghị Kiến trúc:\n"
        "   - Trong điều kiện này, Speculative Decoding tạo ra 'Tăng tốc Âm' (Negative Speedup / Latency Penalty) và làm suy thoái nghiêm trọng hiệu năng hệ thống.\n"
        "   - Khuyến nghị: NGAY LẬP TỨC VÔ HIỆU HÓA (DISABLE) Speculative Decoding và quay trở lại phương thức Auto-Regressive Decoding thông thường của Target Model."
    ),
    "explanation": (
        "Suy luận đầu cơ (Speculative Decoding) không phải là chiếc đũa thần trong mọi trường hợp. Hiệu quả kinh tế và độ trễ của nó hoàn toàn phụ thuộc vào khoảng cách tốc độ giữa hai mô hình và độ chính xác của các đề xuất. Khi mô hình nháp quá nặng hoặc sinh sai quá nhiều, chi phí xác thực và khắc phục lỗi sẽ vượt quá lợi ích mang lại, biến tối ưu hóa thành gánh nặng."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Trình bày chính xác điều kiện tiên quyết của Speculative Decoding: Draft model phải siêu nhanh và tỷ lệ chấp thuận phải cao.\n"
        "- [1.5 điểm] Phân tích khối lượng tính toán (Work/FLOPs): Tăng gấp gần 2 lần do phải chạy cả hai mô hình mà hầu hết token bị vứt bỏ.\n"
        "- [1.5 điểm] Chứng minh độ trễ (Latency) bị suy thoái (Negative Speedup) và đưa ra quyết định kiến trúc: Tắt ngay Speculative Decoding."
    ),
    "reference_source": "Fast Inference from Transformers via Speculative Decoding (Leviathan et al., ICML 2023) & Google DeepMind Speculative Decoding Analysis"
}

# 60. d12-q130 (4 pts)
DAY12_PART2_B["d12-q130"] = {
    "sample_answer": (
        "1. Đánh giá Bản chất Khối lượng Công việc và Điểm nghẽn Cốt tử (Workload Bottleneck Analysis):\n"
        "   - Phân tích bối cảnh: Yêu cầu có prompt siêu ngắn là $20$ tokens nhưng sinh văn bản đầu ra siêu dài là $5.000$ tokens. Tỷ lệ giữa giai đoạn Prefill và giai đoạn Decode là $20 : 5000 = 1 : 250$.\n"
        "   - Xác định Điểm nghẽn (Primary Bottleneck):\n"
        "     + Giai đoạn Prefill (Compute-Bound): Chỉ mất $20$ tokens tính toán song song, hoàn tất trong vòng $5-10$ mili-giây trên bất kỳ GPU hiện đại nào.\n"
        "     + Giai đoạn Decode (Memory-Bound): Chiếm tới $99.8\\%$ tổng thời gian thực thi của yêu cầu (thực hiện $5.000$ bước đọc tuần tự weights và KV Cache từ VRAM).\n"
        "     + Kết luận: Điểm nghẽn duy nhất của hệ thống nằm ở BĂNG THÔNG BỘ NHỚ VRAM CỦA PHA DECODE (Memory Bandwidth Bottleneck), hoàn toàn không có hiện tượng nghẽn tính toán ở pha Prefill.\n"
        "2. Đánh giá Mô hình Tách rời Prefill/Decode (Disaggregated Serving Evaluation):\n"
        "   - Kiến trúc Tách rời (Disaggregated Architecture): Tách riêng cụm Prefill Nodes chuyên tính prompt và chuyển giao dữ liệu KV Cache qua mạng nội bộ cho cụm Decode Nodes chuyên sinh token.\n"
        "   - Rủi ro Mạng trong Bối cảnh:\n"
        "     + Độ trễ truyền tải KV Cache qua mạng: $200$ms.\n"
        "     + Tình trạng mạng: 'Mạng không ổn định' (Network Jitter, Packet Drop, Unreliable Latency).\n"
        "   - So sánh Chi phí Đánh đổi:\n"
        "     Nếu tách rời, để tiết kiệm $5-10$ms tính toán prefill, hệ thống phải trả giá bằng $200$ms chờ truyền mạng (đắt gấp 20 đến 40 lần) cộng thêm rủi ro gãy kết nối mạng khiến request bị lỗi hoặc timeout.\n"
        "3. Quyết định Kiến trúc Bố trí Tài nguyên (Placement & Disaggregation Decision):\n"
        "   - QUYẾT ĐỊNH DỨT KHOÁT: TUYỆT ĐỐI KHÔNG PHÂN TÁCH KIẾN TRÚC (DO NOT DISAGGREGATE).\n"
        "   - Bố trí Tối ưu: Áp dụng Mô hình Hợp nhất Đặt cùng Chỗ (Co-located Single-Node Placement).\n"
        "     Thực thi cả giai đoạn Prefill và toàn bộ 5.000 bước Decode trên cùng một Worker GPU / Node. Bằng cách này, KV cache được giữ nguyên trực tiếp trong bộ nhớ VRAM cục bộ với băng thông cực cao (hàng TB/s), triệt tiêu hoàn toàn 200ms độ trễ mạng và miễn nhiễm với sự thiếu ổn định của hạ tầng mạng."
    ),
    "explanation": (
        "Kiến trúc phân tách Prefill/Decode chỉ mang lại hiệu quả khi khối lượng công việc có prompt cực dài (hàng nghìn đến hàng vạn tokens) và hạ tầng mạng sở hữu băng thông siêu cao (như InfiniBand/RoCE dưới 1ms). Khi prompt ngắn và mạng không ổn định, chi phí truyền tải mạng (Network Overhead) sẽ biến việc phân tách thành một thảm họa về độ trễ và độ tin cậy."
    ),
    "rubric": (
        "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
        "- [1.0 điểm] Phân tích chính xác điểm nghẽn nằm ở giai đoạn Decode 5.000 tokens (Memory-bound) chứ không phải ở Prefill 20 tokens.\n"
        "- [1.5 điểm] So sánh chi phí đánh đổi: Thời gian truyền mạng KV 200ms lớn gấp 20-40 lần thời gian tính prefill (5-10ms) kèm rủi ro mạng chập chờn.\n"
        "- [1.5 điểm] Đưa ra quyết định chuẩn xác: Không phân tách (Do not disaggregate), giữ mô hình Co-located trên cùng một máy chủ GPU."
    ),
    "reference_source": "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving (OSDI '24) & vLLM Architecture Analysis"
}

print("Loaded Day 12 Part 2 Sub-part B (questions 49 to 60).")
