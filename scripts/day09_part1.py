# -*- coding: utf-8 -*-
"""
Day 09 Part 1: Questions 1 to 24 (d09-q002 to d09-q054)
"""

DAY_09_PART1 = {
    "d09-q002": {
        "sample_answer": (
            "1. Chẩn đoán các triệu chứng quá tải có bằng chứng (Overload Symptoms with Trace Evidence):\n"
            "- **Triệu chứng 1: Ô nhiễm ranh giới trách nhiệm và rủi ro quyền hạn (Role Contamination & Security Boundary Overreach)**:\n"
            "  Bằng chứng: Một agent duy nhất vừa đọc chính sách, vừa gọi API thanh toán (Payment API có tác động tài chính), vừa viết email và tự xác nhận thao tác của chính mình (Self-Approving Execution). Việc không có cơ chế tách biệt quyền lực (Separation of Concerns / Dual-Control) vi phạm nghiêm trọng nguyên tắc kiểm soát nội bộ.\n"
            "- **Triệu chứng 2: Nghẽn cổ chai độ trễ do thực thi tuần tự (Latency Bottleneck via Serial Execution)**:\n"
            "  Bằng chứng: Hai nguồn policy độc lập bị đọc nối tiếp (Sequential Reading) thay vì song song hóa (Parallelization), làm tăng gấp đôi độ trễ I/O.\n"
            "- **Triệu chứng 3: Thiếu khả năng quan sát và kiểm toán trung gian (Observability Deficit)**:\n"
            "  Bằng chứng: Trace chỉ ghi nhận kết quả cuối cùng (`final answer`), che giấu toàn bộ các bước tra cứu, tham số gọi API thanh toán và nội dung email, khiến không thể gỡ lỗi khi thanh toán sai.\n"
            "2. Thiết kế tách biệt trách nhiệm xử lý trực tiếp từng triệu chứng:\n"
            "- **PolicyRetrievalWorker**: Đọc song song hai nguồn policy độc lập (xử lý Triệu chứng 2).\n"
            "- **CustomerCommunicationWorker**: Chuyên trách soạn thảo nội dung email phản hồi.\n"
            "- **FinancialApprovalGate / Human-in-the-Loop**: Kiểm tra tính hợp lệ của bằng chứng trước khi chuyển giao lệnh cho PaymentToolWorker.\n"
            "- **PaymentToolWorker**: Nhận lệnh đã được phê duyệt để thực hiện giao dịch thanh toán (xử lý Triệu chứng 1).\n"
            "- **Orchestration Trace Logger**: Ghi vết chuyển trạng thái (State Transition Traces) qua từng worker (xử lý Triệu chứng 3)."
        ),
        "explanation": (
            "Một tác tử đơn lẻ gánh vác quá nhiều chức năng (God-Agent Anti-Pattern) vừa gây tắc nghẽn hiệu năng vừa vi phạm bảo mật khi tự phê duyệt "
            "các tác vụ có tác dụng phụ (Side-effects). Phân rã thành các tác tử chuyên biệt (Specialized Workers) có ranh giới thẩm quyền và khả năng quan sát "
            "từng bước là nguyên lý nền tảng của hệ thống Multi-Agent."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán đủ 3 triệu chứng quá tải] (1.5 điểm): Chỉ ra lỗi tự phê duyệt hành động tài chính, lỗi nghẽn độ trễ đọc tuần tự, và lỗi trace thiếu tính quan sát.\n"
            "- [Thiết kế tách trách nhiệm có căn cứ] (1.5 điểm): Đưa ra các worker chuyên biệt: PolicyWorker (song song), CommunicationWorker, ApprovalGate, PaymentWorker.\n"
            "- [Khả năng quan sát và phân quyền bảo mật] (1.0 điểm): Nhấn mạnh ranh giới tách biệt phê duyệt - thực thi và ghi log chuyển trạng thái minh bạch."
        ),
        "reference_source": "LangGraph Documentation: 'Multi-Agent Architectures and Separation of Concerns' & Google SRE Principles"
    },
    "d09-q004": {
        "sample_answer": (
            "1. Quyết định: **ĐỒNG Ý CHUYỂN ĐỔI SANG MULTI-AGENT (ADOPT MULTI-AGENT ARCHITECTURE)**:\n"
            "Căn cứ: Mặc dù hệ thống đa tác tử có chi phí phức tạp hơn, nhưng kịch bản này hội tụ đủ 3 điều kiện tiên quyết mà một kiến trúc Single-Agent không thể đáp ứng được.\n"
            "2. Biện minh chi tiết bằng Lợi ích, Chi phí và Hàng rào bảo vệ (Trade-off Justification):\n"
            "- **Lợi ích kỹ thuật (Performance & Isolation Benefits)**:\n"
            "  + Tối ưu hóa độ trễ nhảy vọt: Ba kho dữ liệu độc lập (mỗi kho 8s) hiện chạy nối tiếp mất 24s. Khi tách thành 3 Worker chạy song song (Parallel Fan-out), thời gian truy xuất chỉ còn `max(8s, 8s, 8s) = 8s`, giúp hạ độ trễ p95 từ 27s xuống khoảng 11-12s (giảm hơn 55% thời gian phản hồi!).\n"
            "  + Cô lập lỗi (Fault Isolation): Lỗi ở Transaction Tool không làm chết toàn bộ tiến trình hay làm mất các bằng chứng thu được từ 3 kho retrieval.\n"
            "  + Phân định quyền sở hữu rõ ràng: Policy/Legal Worker và Transaction Worker thuộc hai nhóm chủ quản khác nhau, cho phép phát triển, kiểm thử và phân quyền API độc lập.\n"
            "- **Chi phí phát sinh (Overhead Costs)**: Chi phí token tăng nhẹ do trao đổi trạng thái có cấu trúc và chi phí vận hành điều phối (Orchestration Engine overhead).\n"
            "- **Hàng rào bảo vệ (Guardrails)**: Cổng kiểm tra hợp đồng dữ liệu (Schema Validation Gate) giữa các worker và cơ chế timeout độc lập 10s cho mỗi kho.\n"
            "3. Phép đo sau thay đổi và Điều kiện kết luận nó không đáng (Reversal Condition):\n"
            "- Phép đo xác minh: Đo độ trễ `p95 <= 13s` và Tỷ lệ hoàn thành tác vụ khi tool lỗi.\n"
            "- **Điều kiện kết luận nó không đáng**: Nếu sau khi triển khai, chi phí token/độ trễ điều phối tăng gấp đôi mà không giảm được p95 xuống dưới 18s do các kho dữ liệu bị nghẽn mạng chung."
        ),
        "explanation": (
            "Multi-Agent không phải là trào lưu kiến trúc để áp dụng tùy tiện; nó chỉ thực sự đáng giá khi giải quyết được sự cô lập lỗi giữa các chủ thể (Owners) "
            "khác nhau và song song hóa được các tác vụ I/O dài (I/O-bound Parallelization). Phân tích đánh đổi định lượng là phẩm chất cốt lõi của kỹ sư phần mềm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định chọn Multi-Agent có căn cứ] (1.0 điểm): Quyết định áp dụng dựa trên 3 kho độc lập, khác biệt chủ quản và yêu cầu cô lập lỗi.\n"
            "- [Biện minh lợi ích giảm trễ từ 27s xuống ~11s] (1.5 điểm): Chứng minh việc chạy song song 3 kho 8s giúp giảm trễ hơn một nửa và cô lập lỗi tool.\n"
            "- [Phân tích chi phí và Guardrails] (1.0 điểm): Nêu chi phí token điều phối và thiết lập guardrail schema/timeout.\n"
            "- [Phép đo và điều kiện thoái lui] (0.5 điểm): Đưa ra metric p95 và điều kiện đảo ngược quyết định nếu không đạt hiệu quả cam kết."
        ),
        "reference_source": "Wu et al. (2023): 'AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation' & LangGraph Multi-Agent Tradeoffs"
    },
    "d09-q006": {
        "sample_answer": (
            "1. Phân tích nguyên nhân lỗi thiết kế hiện tại:\n"
            "WorkerA đang gánh đồng thời hai trách nhiệm thuộc hai miền hoàn toàn khác biệt: đọc chính sách (Policy Knowledge) và đọc hồ sơ khách hàng (CRM Data), rồi tự phán quyết điều kiện đủ (Eligibility). Khi kết quả phán quyết sai, hệ thống gặp hiện tượng **Mất dấu nguồn lỗi (Ambiguous Attribution Defect)**: không thể biết sai do tài liệu chính sách trích xuất sai, do dữ liệu CRM bị lỗi thời, hay do quy tắc suy luận điều kiện bị sai.\n"
            "2. Thiết kế lại Bản đồ tác vụ thành các Trách nhiệm Độc lập (Redesigned Task Map):\n"
            "- **1. PolicyRetrievalWorker (Domain: Legal/Policy Tri thức)**:\n"
            "  + Trách nhiệm duy nhất: Nhận câu hỏi, tìm kiếm và trích xuất đúng các điều khoản chính sách có liên quan.\n"
            "  + Đầu ra: `policy_rules: List[RuleChunk]` kèm `policy_version` và citations.\n"
            "  + Test boundary: Kiểm thử độc lập bằng bộ testset retrieval (Recall@K, Grounding).\n"
            "- **2. CustomerDataWorker (Domain: CRM/Dữ liệu giao dịch)**:\n"
            "  + Trách nhiệm duy nhất: Gọi API CRM tra cứu lịch sử mua hàng và thông tin khách hàng.\n"
            "  + Đầu ra: `customer_profile: CustomerRecord` có cấu trúc chuẩn hóa.\n"
            "  + Test boundary: Kiểm thử hợp đồng API (Mock CRM responses).\n"
            "- **3. EligibilityDecisionWorker (Domain: Business Logic Suy luận)**:\n"
            "  + Trách nhiệm: Nhận `policy_rules` và `customer_profile` để đối chiếu và đưa ra phán quyết điều kiện đủ.\n"
            "  + Đầu ra: `{\"is_eligible\": bool, \"reason\": str, \"matched_rule_id\": str}`.\n"
            "  + Test boundary: Kiểm thử bảng quyết định (Unit tests với ma trận điều kiện biên).\n"
            "- **4. CommunicationWorker**: Chịu trách nhiệm định dạng JSON và soạn email phản hồi."
        ),
        "explanation": (
            "Nguyên tắc Trách nhiệm Đơn lẻ (Single Responsibility Principle) trong Multi-Agent: Mỗi tác tử phải có một miền sở hữu (Domain Ownership) "
            "và ranh giới kiểm thử (Test Boundary) độc lập. Tách rời tầng thu thập dữ liệu (Policy, CRM) khỏi tầng ra quyết định (Decision Engine) "
            "giúp định vị chính xác nguồn gốc lỗi khi phát sinh sự cố."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chẩn đoán lỗi mất dấu nguồn gốc ở WorkerA] (1.0 điểm): Chỉ ra WorkerA gộp cả policy và CRM khiến không thể truy vết lỗi do đâu.\n"
            "- [Tách biệt 4 Worker có Domain Ownership rõ] (2.0 điểm): Định nghĩa rõ: PolicyWorker (tri thức), CustomerDataWorker (CRM), EligibilityWorker (logic), CommunicationWorker (soạn thảo).\n"
            "- [Xác định ranh giới kiểm thử độc lập] (1.0 điểm): Nêu rõ cách viết test boundary riêng biệt cho từng worker (Retrieval benchmark, API mock, Decision table)."
        ),
        "reference_source": "CrewAI Documentation: 'Role-Playing and Task Decomposition' & Martin Fowler: 'Single Responsibility Principle in Distributed Systems'"
    },
    "d09-q008": {
        "sample_answer": (
            "1. Vẽ Sơ đồ Phụ thuộc và Lịch chạy (Dependency & Execution Graph):\n"
            "Sơ đồ luồng đồ thị DAG (Directed Acyclic Graph) phân tách rõ ràng giữa đọc song song và ghi tuần tự:\n"
            "```text\n"
            "       [START]\n"
            "       /     \\\n"
            "  (Fan-out: Đọc song song)\n"
            "     /         \\\n"
            " [fetch_hr]   [fetch_legal]\n"
            "     \\         /\n"
            "  (Fan-in: Hợp nhất bằng chứng)\n"
            "       \\     /\n"
            "       [merge]\n"
            "          |\n"
            "          v\n"
            "      [approve]  (Xác nhận điều kiện / Human Gate)\n"
            "          |\n"
            "          v\n"
            "    [write_case] (Tuần tự hóa - Điểm cam kết kết quả có tác dụng phụ)\n"
            "          |\n"
            "        [END]\n"
            "```\n"
            "2. Bất biến ngăn chặn ghi hai lần (Double-Write Prevention Invariant):\n"
            "- **Bất biến Khóa Trạng thái và Khóa Lũy thừa (Idempotency Key & State Lock Invariant)**:\n"
            "  `write_case` là thao tác có tác dụng phụ (Side-effect Commit Point). Để đảm bảo không bao giờ chạy 2 lần, hệ thống áp dụng 2 cơ chế kiểm soát:\n"
            "  (a) **Khóa chuyển trạng thái nghiêm ngặt (Strict State Transition)**: Node `write_case` chỉ được phép kích hoạt khi `state.status == 'approved'` VÀ `state.case_written == False`. Khi bắt đầu chạy, nó lập tức cập nhật trạng thái tạm thời thành `writing` (hoặc giữ Distributed Mutex Lock trên `case_id`).\n"
            "  (b) **Mã khóa Idempotency Key (Idempotent API Call)**: Lệnh ghi vào cơ sở dữ liệu được gửi kèm `idempotency_key = hash(case_id + approval_timestamp)`. Nếu node bị kích hoạt lại ngẫu nhiên, hệ thống cơ sở dữ liệu backend sẽ từ chối thao tác ghi trùng lặp và trả về kết quả đã ghi trước đó."
        ),
        "explanation": (
            "Mẫu kiến trúc Parallel-Read Serialized-Write (Đọc song song - Ghi tuần tự) là khuôn mẫu kinh điển trong các hệ thống giao dịch. "
            "Các tác vụ thu thập thông tin được tối ưu hóa tốc độ bằng cơ chế Fan-out song song, nhưng bước phát sinh tác dụng phụ (Commit) "
            "bắt buộc phải qua rào cản đồng bộ hóa (Barrier/Fan-in) và bảo vệ bằng Idempotency Key để chống Double-Spending / Double-Write."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Vẽ đúng cấu trúc đồ thị DAG] (1.5 điểm): Thể hiện rõ fan-out song song fetch_hr/fetch_legal, fan-in tại merge, đi qua approve rồi tới write_case tuần tự.\n"
            "- [Xác định điểm cam kết kết quả write_case] (1.0 điểm): Nhận diện write_case là side-effect commit point đòi hỏi kiểm soát nghiêm ngặt.\n"
            "- [Bất biến Idempotency & State Lock chống ghi 2 lần] (1.5 điểm): Thiết lập cờ trạng thái case_written, mutex lock và mã Idempotency Key gửi kèm lệnh ghi."
        ),
        "reference_source": "LangGraph Documentation: 'Graph Branching, Merging & State Reducers' & Designing Data-Intensive Applications (Kleppmann)"
    },
    "d09-q011": {
        "sample_answer": (
            "1. Có nên thêm tầng phân cấp (Hierarchy) không?\n"
            "**CÓ, HOÀN TOÀN NÊN THÊM.**\n"
            "Căn cứ: Một Supervisor duy nhất điều phối trực tiếp (flat routing) 14 workers độc lập đã vượt quá dung lượng ngữ cảnh hiệu quả (Context Overload) của mô hình định tuyến. Danh sách worker dài làm tăng token prompt, gây nhầm lẫn ngữ nghĩa giữa các năng lực và là nguyên nhân trực tiếp khiến tỷ lệ định tuyến sai (misroute rate) tăng vọt. Sự hiện diện của cụm 6 workers Finance có chính sách dùng chung là tín hiệu hoàn hảo để trừu tượng hóa phân cấp.\n"
            "2. Đề xuất cấu trúc phân cấp tối thiểu (Minimal Hierarchical Structure):\n"
            "Thiết lập cấu trúc 2 tầng (Two-Tier Hierarchical Multi-Agent Architecture):\n"
            "- **Tầng 1 (Top-level Root Supervisor)**: Chỉ quản lý **9 thực thể** (thay vì 14):\n"
            "  + 8 General/Domain Workers độc lập.\n"
            "  + 1 Sub-Supervisor: `FinanceSupervisor` (đại diện cho toàn bộ miền tài chính).\n"
            "- **Tầng 2 (Finance Subgraph)**: Được điều phối bởi `FinanceSupervisor`, quản lý nội bộ 6 Finance Workers với chính sách dùng chung.\n"
            "3. Hệ thống chỉ số xác minh hiệu quả (Verification Metrics):\n"
            "- **Top-level Misroute Rate**: Tỷ lệ định tuyến sai của Root Supervisor giảm xuống mức tối thiểu (mục tiêu < 2%).\n"
            "- **Prompt Token Reduction**: Dung lượng token danh sách worker trong system prompt của Root Supervisor giảm ít nhất 35%.\n"
            "- **End-to-End Task Success Rate**: Tỷ lệ hoàn thành tác vụ chính xác toàn trình tăng đáng kể trên toàn bộ 14 nghiệp vụ."
        ),
        "explanation": (
            "Quy tắc Sizing trong hệ thống tác tử: Khi số lượng worker vượt quá ngưỡng 7-10 tác tử, mô hình ngôn ngữ làm nhiệm vụ điều phối bắt đầu "
            "bị suy giảm độ chính xác định tuyến. Gom cụm các tác tử có chung miền chính sách và trách nhiệm vào một Subgraph có Sub-Supervisor riêng "
            "giúp giảm tải nhận thức (Cognitive Load) cho Root Supervisor và tăng tính module hóa của hệ thống."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Quyết định thêm Hierarchy có căn cứ] (1.5 điểm): Khẳng định nên thêm phân cấp vì 14 workers làm quá tải prompt và tăng misroute; nhận diện cụm 6 Finance workers có shared policy.\n"
            "- [Thiết kế cấu trúc 2 tầng tối thiểu] (1.5 điểm): Mô tả rõ Root Supervisor quản lý 8 workers + FinanceSupervisor; FinanceSupervisor quản lý 6 Finance workers.\n"
            "- [Chỉ số xác minh thực nghiệm] (1.0 điểm): Đưa ra 3 metric cụ thể: Misroute rate giảm, token prompt giảm 35%, Task success rate tăng."
        ),
        "reference_source": "Wu et al. (2023): 'AutoGen: Hierarchical Multi-Agent Group Chat' & LangGraph Subgraph Composition"
    },
    "d09-q013": {
        "sample_answer": (
            "1. Chỉ ra hai lỗi vi phạm ranh giới trách nhiệm (Boundary Violations):\n"
            "- **Lỗi 1: Supervisor kiêm nhiệm xử lý nghiệp vụ (Domain Logic Contamination)**:\n"
            "  Supervisor hiện 'tự trả lời policy' khi cảm thấy tự tin. Đây là lỗi vi phạm nghiêm trọng ranh giới: Supervisor chỉ có vai trò điều phối luồng (Flow Orchestration), tuyệt đối không được kiêm nhiệm vai trò tri thức miền (Domain Worker). Khi tự trả lời, supervisor dễ sinh ra ảo giác và bỏ qua các quy tắc trích dẫn chuẩn.\n"
            "- **Lỗi 2: Thiếu bộ định tuyến chuyên biệt & Đổ dồn yêu cầu (Default Dump / Catch-all Routing Defect)**:\n"
            "  Supervisor 'chỉ gọi worker khi thiếu tự tin và đẩy mọi request còn lại vào RetrievalWorker'. Việc coi RetrievalWorker là thùng chứa rác (catch-all) làm mất vai trò của các worker khác (nếu có) và biến hệ thống thành một luồng tùy tiện không thể kiểm soát.\n"
            "2. Viết lại Hợp đồng Định tuyến (Rewritten Routing Contract):\n"
            "Nguyên tắc cốt lõi: 'Supervisor giữ luồng điều phối; Worker giữ tri thức và năng lực miền'.\n"
            "Hợp đồng bắt buộc Supervisor chỉ xuất ra cấu trúc JSON định tuyến, cấm tự viết câu trả lời trực tiếp:\n"
            "```json\n"
            "{\n"
            "  \"next_worker\": \"PolicyWorker\" | \"RetrievalWorker\" | \"SynthesisWorker\" | \"FINISH\",\n"
            "  \"routing_reason\": \"string giải thích căn cứ điều phối\",\n"
            "  \"delegation_payload\": {\"sub_task\": \"string\", \"context_keys\": [\"...\"]}\n"
            "}\n"
            "```\n"
            "- Nếu yêu cầu là câu hỏi chính sách: Bắt buộc định tuyến sang `PolicyWorker` (hoặc `RetrievalWorker`).\n"
            "- Khi tất cả các worker đã hoàn tất dữ liệu: Định tuyến sang `SynthesisWorker` để tổng hợp phản hồi cuối cùng."
        ),
        "explanation": (
            "Mẫu thiết kế Supervisor-Worker đòi hỏi sự phân định nghiêm ngặt: Supervisor là trọng tài điều phối luồng, "
            "không được tự ý ra sân thi đấu thay cho cầu thủ (Workers). Việc Supervisor tự trả lời là biểu hiện của sự lỏng lẻo trong prompt contract, "
            "làm mất tính tất định và phá hủy khả năng kiểm thử của từng tác tử."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chỉ rõ 2 lỗi vi phạm ranh giới] (1.5 điểm): Nhận diện đúng lỗi Supervisor tự trả lời (vi phạm vai trò điều phối) và lỗi coi RetrievalWorker là bãi rác catch-all.\n"
            "- [Nguyên tắc kiến trúc Supervisor-Worker] (1.0 điểm): Nhấn mạnh nguyên tắc: Supervisor giữ flow điều phối, Worker giữ domain skill.\n"
            "- [Viết lại Routing Contract chuẩn xác] (1.5 điểm): Thiết kế JSON schema định tuyến tường minh (next_worker, routing_reason) cấm supervisor tự sinh text trả lời."
        ),
        "reference_source": "LangChain Documentation: 'Supervisor Multi-Agent Pattern' & AutoGen GroupChatManager Architecture"
    },
    "d09-q015": {
        "sample_answer": (
            "1. Lựa chọn Mẫu Thiết kế (Pattern Selection):\n"
            "Chọn **Deterministic Sequential Pipeline (Đường ống Tuần tự Tất định)**. Tuyệt đối **KHÔNG CẦN VÀ KHÔNG NÊN DÙNG DYNAMIC SUPERVISOR ROUTER**.\n"
            "2. Biện minh vì sao Dynamic Router hoàn toàn không cần thiết:\n"
            "- Bản chất luồng công việc: Quy trình `parse -> validate -> publish` luôn luôn thực thi theo cùng một thứ tự tuyến tính cố định cho mọi đầu vào. Ranh giới giữa các bước là bất biến.\n"
            "- Router chỉ có giá trị khi cần rẽ nhánh động (Branching) dựa trên nội dung câu hỏi hoặc phân loại trạng thái. Trong một quy trình tuyến tính cố định, một Dynamic Router LLM không có bất kỳ quyết định nào để đưa ra; việc đưa nó vào chỉ làm lãng phí token, tăng thêm 500-1000 ms độ trễ cho mỗi bước và tạo ra nguy cơ mô hình định tuyến nhầm sang một thứ tự vô lý (ví dụ: nhảy từ `parse` sang thẳng `publish`).\n"
            "3. Thiết lập Điểm lưu Checkpoint và Hành vi khi có Lỗi (Checkpoint & Error Behavior):\n"
            "- **Checkpoint 1 (Sau Parse)**: Lưu `state.parsed_artifact`. Nếu Parse thất bại -> Lập tức kết thúc với `status = 'failed_parse'`, không gọi tiếp.\n"
            "- **Checkpoint 2 (Sau Validate)**: Lưu `state.validation_result`. Nếu Validation không hợp lệ -> Kết thúc với `status = 'failed_validation'`, kích hoạt thông báo cho người dùng.\n"
            "- **Điểm cam kết Publish (Side-effect Gate)**: Chỉ kích hoạt `publish` khi và chỉ khi `state.validation_passed == True`. Áp dụng cơ chế giao dịch (Transactional Commit) để nếu publish lỗi mạng, hệ thống có thể thử lại an toàn dựa trên checkpoint của Validate mà không cần parse lại từ đầu."
        ),
        "explanation": (
            "Quy tắc Kỹ thuật: 'Đừng dùng tác tử thông minh LLM để giải quyết bài toán mà một đoạn code tuần tự đơn giản có thể làm tốt hơn'. "
            "Pipeline tuần tự tất định với các điểm lưu Checkpoint rõ ràng mang lại tính tin cậy 100%, độ trễ tối thiểu và khả năng phục hồi lỗi hoàn hảo."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Lựa chọn Sequential Pipeline & Bác bỏ Dynamic Router] (1.5 điểm): Chọn Pipeline tất định; giải thích Router không có gì để quyết định vì luồng cố định, chỉ gây tốn trễ và rủi ro misroute.\n"
            "- [Thiết lập Checkpoints rõ ràng sau từng bước] (1.5 điểm): Đặt checkpoint sau Parse và sau Validate để lưu trạng thái trung gian phục vụ phục hồi.\n"
            "- [Hành vi xử lý lỗi và bảo vệ bước Publish] (1.0 điểm): Dừng sớm nếu parse/validate lỗi, chỉ publish khi pass validation kèm cơ chế retry."
        ),
        "reference_source": "LangGraph Documentation: 'Sequential Workflows vs. Multi-Agent Graphs' & Fowler: 'Pipes and Filters Architecture'"
    },
    "d09-q017": {
        "sample_answer": (
            "1. Phân tích sai lầm của cơ chế Đa số Thắng (Majority Voting Flaw):\n"
            "Nguyên tắc: 'Một ý kiến sai lặp lại hai lần không trở thành chân lý' (Duplicate Hallucination Trap). Hai agent cùng dùng chung một prompt/mô hình đã sinh ra hai câu trả lời đồng thuận ảo do cùng chia sẻ một thiên kiến (Model Bias). Trong khi đó, Agent thứ ba tuy là thiểu số (1 phiếu) nhưng lại dẫn nguồn tài liệu chính sách có thẩm quyền (Authoritative Citation) và chứng minh được tính đúng đắn. Cơ chế majority vote thuần túy đã đàn áp sự thật và chọn câu trả lời sai.\n"
            "2. Thiết kế lại Quy tắc Tranh luận và Đánh giá (Redesigned Debate & Judging Rules):\n"
            "- **Thay thế Majority Vote bằng Bằng chứng Trọng tài (Evidence-Based Adjudication)**:\n"
            "  Thẩm phán độc lập (Judge / Meta-Agent) đánh giá các câu trả lời dựa trên Thang bậc Bằng chứng (Hierarchy of Evidence):\n"
            "  + Trọng số 1 (Thẩm quyền cao nhất): Mệnh đề có trích dẫn văn bản chính sách chính thức được xác thực (Verified Statutory Citation).\n"
            "  + Trọng số 2: Lập luận logic không mâu thuẫn.\n"
            "  + Không tính điểm số lượng bản sao: Hai câu trả lời giống nhau từ cùng prompt chỉ được tính là một nguồn dữ liệu duy nhất.\n"
            "- **Vòng tranh biện đối chất (Cross-Examination Round)**: Thẩm phán gửi trích dẫn của Agent 3 cho Agent 1 và 2: 'Agent 3 dẫn chứng Điều 5 Quy định X trái ngược với câu trả lời của bạn. Bạn có tài liệu chính thức nào phủ nhận Điều 5 không?'. Nếu hai agent không dẫn được nguồn phản bác, Agent 3 thắng cuộc.\n"
            "3. Điều kiện dừng hữu hạn (Stopping Conditions):\n"
            "- Điều kiện 1: Các bên đạt được sự đồng thuận dựa trên bằng chứng tối thượng.\n"
            "- Điều kiện 2: Đạt giới hạn tối đa **2 vòng tranh biện (Max Rounds = 2)**. Nếu vẫn bất đồng, Judge ưu tiên bên có trích dẫn thẩm quyền và đánh dấu cờ kiểm tra cho con người."
        ),
        "explanation": (
            "Trong hệ thống tác tử tranh luận (Debate Pattern), sự thật khách quan phải được xác định bằng tính vững chắc của bằng chứng (Evidence Grounding), "
            "hoàn toàn không thể giải quyết bằng cơ chế bỏ phiếu dân chủ (Majority Voting) giữa các mô hình ngôn ngữ vốn dễ mắc lỗi đồng thuận ảo (Sycophancy)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phê phán cơ chế Majority Vote] (1.5 điểm): Chỉ ra việc 2 agent cùng prompt sinh đồng thuận ảo đè bẹp agent thứ 3 có nguồn chính sách thẩm quyền.\n"
            "- [Quy tắc Judging dựa trên thang bậc bằng chứng] (1.5 điểm): Thiết kế thẩm phán đánh giá dựa trên nguồn trích dẫn được xác thực và vòng đối chất phản biện.\n"
            "- [Điều kiện dừng hữu hạn] (1.0 điểm): Giới hạn tối đa 2 vòng debate và cơ chế fallback chuyển cấp con người nếu bất đồng kéo dài."
        ),
        "reference_source": "Du et al. (2023): 'Improving Factuality and Reasoning in Language Models through Multiagent Debate' & Anthropic Constitutional Principles"
    },
    "d09-q020": {
        "sample_answer": (
            "1. Đánh giá đề xuất thêm 2 tầng Supervisor (Evaluation of Over-Engineering):\n"
            "Đề xuất này là **MỘT THIẾT KẾ DƯ THỪA TAI HẠI (Premature Optimization & Over-Engineering Anti-pattern)**:\n"
            "- Căn cứ thực tế: Hệ thống hiện tại chỉ có 4 workers độc lập và độ chính xác định tuyến (Routing Accuracy) đang đạt mức lý tưởng 99%. Không có bất kỳ vấn đề nào về hiệu năng, độ chính xác hay quá tải prompt xảy ra trong hệ thống.\n"
            "- Tác hại của việc thêm 2 tầng Supervisor:\n"
            "  + Tăng thêm 2 chặng mạng/LLM (Extra Hops), làm tăng độ trễ p95 thêm ít nhất 1.000 ms đến 2.000 ms cho mỗi yêu cầu.\n"
            "  + Làm tăng gấp đôi chi phí token điều phối.\n"
            "  + Làm tăng nguy cơ lỗi tích lũy giữa các tầng (Error Cascading) và giảm độ chính xác từ 99% xuống thấp hơn do thêm điểm thất bại tiềm tàng.\n"
            "2. Các tín hiệu kỹ thuật (Signals) thực sự làm phân cấp trở nên đáng cân nhắc trong tương lai:\n"
            "Chỉ xem xét thêm tầng phân cấp (Hierarchy) khi xuất hiện ít nhất một trong ba tín hiệu sau:\n"
            "- **Tín hiệu 1 (Bùng nổ số lượng Worker)**: Số lượng worker mở rộng vượt quá 10-12 workers khiến system prompt của supervisor bị quá tải token và tỷ lệ misroute tăng cao (> 5%).\n"
            "- **Tín hiệu 2 (Hình thành các Cụm nghiệp vụ chuyên biệt có ranh giới rõ ràng)**: Xuất hiện các nhóm worker có chung chính sách, chung cơ sở dữ liệu nội bộ và quyền hạn riêng biệt (ví dụ: Cụm Kế toán 5 workers, Cụm Pháp chế 4 workers).\n"
            "- **Tín hiệu 3 (Yêu cầu Cô lập Bảo mật / Tenant Boundaries)**: Khi các nhóm worker thuộc các bộ phận khác nhau không được phép chia sẻ chung không gian trạng thái hoặc log truy vết."
        ),
        "explanation": (
            "Nguyên lý YAGNI (You Aren't Gonna Need It) trong Kiến trúc Multi-Agent: Đừng bao giờ xây dựng hệ thống phân cấp phức tạp cho tương lai 'scale sau này' "
            "khi bài toán hiện tại đang hoạt động hoàn hảo với 4 worker phẳng. Thêm tầng điều phối đồng nghĩa với việc thêm độ trễ, chi phí và điểm gãy của hệ thống."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đánh giá dư thừa của đề xuất 2 tầng] (1.5 điểm): Bác bỏ đề xuất: 4 worker phẳng đang đạt 99% accuracy; thêm tầng chỉ làm tăng trễ 1-2s và tốn token vô ích.\n"
            "- [Tác hại của việc phân cấp sớm] (1.0 điểm): Nêu rõ rủi ro tích lũy lỗi qua nhiều hop (Error Cascading) và chi phí vận hành tăng cao.\n"
            "- [3 Tín hiệu kích hoạt phân cấp thực sự] (1.5 điểm): Liệt kê 3 tín hiệu chuẩn xác: số lượng worker > 10 làm giảm accuracy, xuất hiện cụm nghiệp vụ có shared state/policy, và yêu cầu cách ly bảo mật."
        ),
        "reference_source": "Google SRE Principles: 'Simplicity and Premature Optimization' & Martin Fowler: 'YAGNI (You Aren't Gonna Need It)'"
    },
    "d09-q022": {
        "sample_answer": (
            "1. Phân định thành phần Tĩnh và thành phần Động trong Đồ thị:\n"
            "- **Phần Tĩnh (Static Graph Topology / Compile-time Invariants)**:\n"
            "  + Tập hợp các Node cố định đã được khai báo và biên dịch trong đồ thị: `{classify, route, worker_pool, merge}`.\n"
            "  + Các cạnh kết nối cấu trúc bất biến: `START -> classify -> route` và `worker -> merge -> END`.\n"
            "  + Lược đồ trạng thái chung (State Schema Definition) quy định kiểu dữ liệu của các trường trong graph.\n"
            "- **Phần Động (Dynamic Execution Routing / Runtime Selection)**:\n"
            "  + Quyết định rẽ nhánh tại node `route`: Node `route` đọc nhãn phân loại runtime (ví dụ `label = 'billing'`) để chọn cạnh có điều kiện (Conditional Edge) kích hoạt worker cụ thể (`BillingWorker`).\n"
            "  + Dữ liệu payload thực tế được truyền qua các node trong một lần chạy cụ thể.\n"
            "2. Các điều kiện kiểm thử bất biến bắt buộc cần có (Test Invariants):\n"
            "- **Invariant 1: Tính Đóng kín của Nhãn Điều phối (Finite Closed-set Routing Invariant)**:\n"
            "  `assert route_label in ALLOWED_WORKER_LABELS` — Nhãn sinh ra từ node `classify` bắt buộc phải thuộc danh mục các worker tồn tại thực tế trong đồ thị. Nếu nhãn lạ, bắt buộc rẽ về nhánh `fallback_worker`.\n"
            "- **Invariant 2: Bảo toàn Dòng chảy Hợp nhất (Merge Convergence Invariant)**:\n"
            "  Dù bất kỳ worker động nào được kích hoạt, 100% các nhánh rẽ đều phải hội tụ về node `merge` trước khi kết thúc (không có nhánh cụt treo trạng thái).\n"
            "- **Invariant 3: Tính Bất biến Cấu trúc Đồ thị**: Đồ thị không được tự ý sửa đổi danh sách node tại thời điểm chạy (No runtime graph mutation)."
        ),
        "explanation": (
            "Trong LangGraph và các framework điều phối hiện đại, cấu trúc đồ thị (Nodes & Edges) là cấu trúc tĩnh được kiểm tra chặt chẽ khi khởi tạo (Build-time), "
            "trong khi việc chọn đường đi giữa các cạnh có điều kiện là hành vi động (Runtime Decision). Phân định rõ hai yếu tố này giúp thiết lập các kiểm thử bất biến "
            "đảm bảo hệ thống không bao giờ bị rơi vào trạng thái treo (Deadlock / Dangling State)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân định phần Tĩnh] (1.5 điểm): Xác định rõ cấu trúc nodes (classify, route, merge), các cạnh cố định và State schema là phần tĩnh compile-time.\n"
            "- [Phân định phần Động] (1.0 điểm): Xác định việc chọn worker tại conditional edge dựa trên runtime label là phần động.\n"
            "- [Thiết lập 3 Test Invariants bắt buộc] (1.5 điểm): Định nghĩa các invariant: tập nhãn đóng có fallback, mọi đường chạy đều hội tụ về merge, và không tự biến đổi đồ thị runtime."
        ),
        "reference_source": "LangGraph Documentation: 'Conditional Edges and Static Graph Compilation' (https://langchain-ai.github.io/langgraph/)"
    },
    "d09-q024": {
        "sample_answer": (
            "1. Viết lại ranh giới trách nhiệm của Supervisor (Rewritten Supervisor Boundary):\n"
            "Supervisor là Bộ điều phối dòng chảy trung lập (Pure Orchestration Controller). Trách nhiệm duy nhất của nó là: Tiếp nhận yêu cầu, phân loại ý định, lựa chọn worker phù hợp nhất trong danh sách đã cấp và theo dõi trạng thái hoàn thành của toàn trình.\n"
            "- **Hợp đồng Đầu ra của Supervisor (Chỉ trả JSON Điều phối)**:\n"
            "  ```json\n"
            "  {\n"
            "    \"action\": \"ROUTE\",\n"
            "    \"target_worker\": \"RetrievalWorker\" | \"PolicyWorker\" | \"RefundPaymentWorker\" | \"SynthesisWorker\",\n"
            "    \"instruction_payload\": {\"task_summary\": \"...\"}\n"
            "  }\n"
            "  ```\n"
            "2. Các phần BẮT BUỘC PHẢI CHUYỂN ĐI (Mandatory Responsibilities to Evict):\n"
            "- **Phần 1: Chuyển bỏ 'Tự trả lời nếu biết' sang `SynthesisWorker` hoặc `PolicyWorker`**:\n"
            "  Tuyệt đối xóa bỏ câu lệnh 'nếu biết thì tự trả lời' khỏi prompt của supervisor. Supervisor không giữ tri thức chính sách; mọi câu trả lời nghiệp vụ phải do `PolicyWorker` thẩm định và `SynthesisWorker` soạn thảo dựa trên tài liệu trích xuất.\n"
            "- **Phần 2: Chuyển bỏ quyền 'Gọi API hoàn tiền' sang một Worker chuyên biệt có Guardrail (`RefundPaymentWorker`)**:\n"
            "  Supervisor không được nắm giữ tool thanh toán tài chính (vi phạm Least Privilege). Quyền gọi API hoàn tiền phải được chuyển sang một `RefundPaymentWorker` độc lập, có cổng kiểm duyệt Human-in-the-loop hoặc xác thực hạn mức trước khi thực thi."
        ),
        "explanation": (
            "Việc trao quyền gọi công cụ tác động tài chính và quyền tự trả lời cho Supervisor là lỗi kiến trúc nguy hiểm (Over-privileged Controller Anti-pattern). "
            "Ranh giới sạch (Clean Boundary) yêu cầu tách rời hoàn toàn quyền điều phối khỏi quyền thao tác dữ liệu nhạy cảm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đặc tả ranh giới sạch của Supervisor] (1.5 điểm): Định nghĩa Supervisor là bộ điều phối thuần túy, chỉ xuất JSON routing có cấu trúc.\n"
            "- [Chuyển bỏ việc tự trả lời] (1.0 điểm): Xóa bỏ chỉ thị tự trả lời, chuyển nhiệm vụ này cho Policy/Synthesis Worker.\n"
            "- [Chuyển bỏ quyền gọi API hoàn tiền] (1.5 điểm): Tước quyền gọi API hoàn tiền của Supervisor, chuyển sang RefundPaymentWorker độc lập có cổng kiểm soát bảo mật."
        ),
        "reference_source": "LangChain Multi-Agent Architecture Guidelines & NIST SP 800-53 Principle of Least Privilege"
    },
    "d09-q026": {
        "sample_answer": (
            "1. Tách hoặc Viết lại `UniversalWorker` thành các Worker có Ranh giới có thể Kiểm thử (Narrow Workers Decomposition):\n"
            "`UniversalWorker` là một 'God-Worker' gộp quá nhiều quyền và giữ state ẩn. Cần phân rã thành 3 worker độc lập, hoàn toàn phi trạng thái (Stateless Function Workers):\n"
            "- **1. RetrievalWorker**:\n"
            "  + Đầu vào: `{query: str, filters: dict}`. Đầu ra: `{chunks: List[dict]}`.\n"
            "  + Kiểm thử: Đo Recall@K trên tập benchmark ngữ liệu độc lập.\n"
            "- **2. SupportTicketWorker**:\n"
            "  + Đầu vào: `{ticket_payload: dict, idempotency_key: str}`. Đầu ra: `{ticket_id: str, status: str}`.\n"
            "  + Kiểm thử: Mock API endpoint của hệ thống phiếu hỗ trợ, kiểm tra schema request/response.\n"
            "- **3. AnswerSynthesisWorker**:\n"
            "  + Đầu vào: `{query: str, context_chunks: List[dict], user_intent: str}`. Đầu ra: `{final_answer: str, citations: List[str]}`.\n"
            "  + Kiểm thử: Kiểm thử độ bám bằng chứng (Faithfulness) và format markdown.\n"
            "2. Trạng thái (State) nào TUYỆT ĐỐI KHÔNG ĐƯỢC ẨN trong Worker:\n"
            "- **Bộ nhớ đệm hội thoại (Conversation Cache / Message History)**: Tuyệt đối không được lưu ẩn trong biến cục bộ (`self.cache` hoặc bộ nhớ tiến trình của worker).\n"
            "- **Quy tắc**: Toàn bộ lịch sử hội thoại và ngữ cảnh phiên làm việc bắt buộc phải được đưa lên **Lược đồ Trạng thái Chung của Đồ thị (Global Graph State / Checkpointed State Store)**.\n"
            "- Căn cứ: Một worker phải là một hàm thuần túy hoặc hàm đơn định (Pure / Idempotent Function): có thể chạy lại chính xác chỉ từ các tham số đầu vào được truyền vào trong lượt gọi đó, không phụ thuộc vào trạng thái ẩn trong bộ nhớ."
        ),
        "explanation": (
            "Nguyên tắc Thiết kế Worker Hẹp và Phi Trạng thái (Stateless Narrow Workers): Ẩn trạng thái hội thoại bên trong worker phá hủy hoàn toàn "
            "khả năng tái lập lỗi, làm vô hiệu hóa cơ chế phục hồi checkpoint (Resume) của LangGraph và gây ra xung đột dữ liệu khi worker được scale ngang (Horizontal Scaling)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân rã thành 3 worker hẹp độc lập] (1.5 điểm): Tách thành RetrievalWorker, SupportTicketWorker, và AnswerSynthesisWorker có input/output/test boundary rõ ràng.\n"
            "- [Chỉ rõ bộ nhớ đệm hội thoại không được ẩn] (1.5 điểm): Khẳng định cấm ẩn conversation cache bên trong worker; bắt buộc đưa lên Shared Graph State.\n"
            "- [Nguyên lý Worker phi trạng thái tái lập] (1.0 điểm): Nhấn mạnh nguyên lý worker phải chạy lại được chỉ từ input truyền vào lần gọi đó."
        ),
        "reference_source": "LangGraph Documentation: 'Stateless Nodes and Checkpointer Architecture' & Twelve-Factor App: Stateless Processes"
    },
    "d09-q028": {
        "sample_answer": (
            "1. Viết lại Contract sửa lỗi cho Worker (Strict Worker Input/Output Contract):\n"
            "Worker bị lỗi âm thầm chọn bản 2023 vì hợp đồng đầu vào quá lỏng lẻo. Cần định nghĩa lại schema với các trường bắt buộc và xác thực chặt chẽ (Pydantic Schema):\n"
            "```json\n"
            "{\n"
            "  \"input_schema\": {\n"
            "    \"question\": {\"type\": \"string\", \"required\": true},\n"
            "    \"employee_type\": {\"type\": \"string\", \"enum\": [\"permanent\", \"seasonal\", \"contractor\"], \"required\": true},\n"
            "    \"target_year\": {\"type\": \"integer\", \"minimum\": 2023, \"required\": true}\n"
            "  },\n"
            "  \"output_schema\": {\n"
            "    \"status\": \"SUCCESS\" | \"MISSING_INPUT\" | \"POLICY_NOT_FOUND\",\n"
            "    \"data\": {\"leave_duration_days\": \"integer\", \"policy_version\": \"string\"},\n"
            "    \"missing_fields\": [\"string\"],\n"
            "    \"clarification_prompt\": \"string\"\n"
            "  }\n"
            "}\n"
            "```\n"
            "2. Hai dữ kiện chỉ Người gọi (Caller / User Session) có thể biết:\n"
            "- **Dữ kiện 1: Loại hình nhân viên của người hỏi (`employee_type`)**: Là nhân viên chính thức hay nhân viên thời vụ (chỉ hồ sơ nhân sự của caller mới biết).\n"
            "- **Dữ kiện 2: Năm áp dụng hoặc Thời điểm phát sinh thai sản (`target_year` / `effective_date`)**: Người hỏi đang hỏi cho chế độ của năm 2023 hay chính sách mới 2025.\n"
            "3. Phản hồi chuẩn mực khi thiếu thông tin đầu vào (Response for Missing Input):\n"
            "Tuyệt đối cấm âm thầm tự chọn. Worker phải trả về phản hồi yêu cầu làm rõ (Clarification Response):\n"
            "```json\n"
            "{\n"
            "  \"status\": \"MISSING_INPUT\",\n"
            "  \"missing_fields\": [\"employee_type\", \"target_year\"],\n"
            "  \"clarification_prompt\": \"Để cung cấp thời gian nghỉ thai sản chính xác, vui lòng cho biết bạn là nhân viên chính thức hay thời vụ, và bạn cần tra cứu chính sách năm 2023 hay 2025?\"\n"
            "}\n"
            "```"
        ),
        "explanation": (
            "Nguyên tắc Hợp đồng Tác tử: 'Cấm suy đoán âm thầm khi thiếu dữ kiện nghiệp vụ' (Silent Defaulting Anti-pattern). "
            "Khi các tham số phân định chính sách thuộc về ngữ cảnh của người gọi, worker phải trả về trạng thái MISSING_INPUT kèm câu hỏi làm rõ có cấu trúc."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chỉ rõ 2 dữ kiện chỉ caller biết] (1.0 điểm): Xác định đúng employee_type (thời vụ/chính thức) và target_year (chính sách 2023 hay 2025).\n"
            "- [Đặc tả Contract đầu vào/đầu ra nghiêm ngặt] (1.5 điểm): Thiết kế schema có kiểu dữ liệu, bắt buộc truyền 2 trường trên, cấm silent default.\n"
            "- [Thiết kế phản hồi MISSING_INPUT làm rõ] (1.5 điểm): Soạn thảo response chuẩn có status MISSING_INPUT, mảng missing_fields và câu hỏi làm rõ thân thiện."
        ),
        "reference_source": "Anthropic Tool Use Specifications & Pydantic / OpenAPI Schema Validation Standards"
    },
    "d09-q031": {
        "sample_answer": (
            "1. Lựa chọn Ngữ cảnh Tối thiểu cần gửi (Context Minimization Selection):\n"
            "Áp dụng Nguyên tắc Tối thiểu hóa Ngữ cảnh (Principle of Least Context / Data Minimization): Chỉ gửi chính xác **3 trường dữ liệu** cần thiết cho việc thẩm định quy tắc:\n"
            "- `policy_result`: Bắt buộc. Chứa các điều khoản quy định đã trích xuất từ văn bản chính sách để đối chiếu.\n"
            "- `employee_type`: Bắt buộc. Phân loại loại hình lao động của nhân viên để áp đúng khung điều kiện trong chính sách.\n"
            "- `request_date`: Bắt buộc. Ngày nộp đơn/yêu cầu để xác định phiên bản chính sách có hiệu lực và tính toán số ngày thâm niên.\n"
            "2. Giải thích vì sao BỎ RƠI toàn bộ hội thoại, địa chỉ nhà và access token:\n"
            "- **Toàn bộ lịch sử hội thoại (Full Chat History)**: Bỏ qua vì làm ô nhiễm context window bằng các câu chào hỏi râu ria, tốn token vô ích và làm xao nhãng mô hình.\n"
            "- **Địa chỉ nhà (Home Address - PII)**: Bỏ qua vì hoàn toàn không liên quan đến điều kiện hưởng chính sách, vi phạm nghiêm trọng quy chuẩn bảo vệ dữ liệu cá nhân (GDPR/Nghị định 13) nếu truyền tùy tiện giữa các worker.\n"
            "- **Access Token**: Bỏ qua vì PolicyWorker là một hàm suy luận logic thuần túy, không có quyền gọi dịch vụ ngoài. Việc truyền token vi phạm bảo mật nghiêm trọng (Credential Leakage Vulnerability).\n"
            "3. Cách xử lý nếu khuyết thiếu `request_date` (Handling Missing Request Date):\n"
            "- Kiểm tra hợp đồng đầu vào (Pre-condition Assertion): Nếu thiếu `request_date`, PolicyWorker từ chối xử lý và trả về mã lỗi: `{\"status\": \"ERROR\", \"code\": \"MISSING_REQUEST_DATE\", \"message\": \"request_date is required to determine policy temporal validity\"}`.\n"
            "- Phương án dự phòng có kiểm soát (Defaulting with Audit Flag): Nếu nghiệp vụ cho phép, Supervisor có thể điền mặc định bằng `current_system_date()` nhưng bắt buộc phải gắn cờ cảnh báo: `\"date_inferred\": true` trong payload."
        ),
        "explanation": (
            "Trong hệ thống Multi-Agent, việc truyền bừa bãi toàn bộ đối tượng trạng thái (State Dump) chứa PII và Access Token giữa các node "
            "là một lỗ hổng an ninh thông tin nghiêm trọng. Mỗi tác tử chỉ được nhận đúng tập dữ liệu tối thiểu cần thiết để hoàn thành nhiệm vụ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chọn đúng 3 trường dữ liệu tối thiểu] (1.0 điểm): Giữ lại policy_result, employee_type, request_date.\n"
            "- [Biện minh chi tiết loại bỏ 3 trường nhạy cảm] (1.5 điểm): Giải thích rõ: loại bỏ chat history chống loãng context, loại bỏ địa chỉ bảo vệ PII, loại bỏ token chống rò rỉ quyền.\n"
            "- [Quy trình xử lý thiếu request_date] (1.5 điểm): Đưa ra cách xử lý: báo lỗi từ chối rõ ràng hoặc gán ngày hiện tại có kèm cờ cảnh báo kiểm toán."
        ),
        "reference_source": "OWASP Top 10 for LLM: LLM06 Sensitive Information Disclosure & Google Cloud Data Minimization Guide"
    },
    "d09-q033": {
        "sample_answer": (
            "1. Thiết kế lại Lược đồ Trạng thái Chung có Kiểu dữ liệu Chặt chẽ (Typed Graph State Schema):\n"
            "Thay thế schema lỏng lẻo `{messages, data, done}` bằng TypedDict / Pydantic schema phân rã các artifact ngữ nghĩa rõ ràng:\n"
            "```python\n"
            "from typing import Annotated, List, Optional, TypedDict\n"
            "from langgraph.graph.message import add_messages\n"
            "\n"
            "class PolicyChunk(TypedDict):\n"
            "    chunk_id: str\n"
            "    content: str\n"
            "    policy_version: str\n"
            "\n"
            "class SharedGraphState(TypedDict):\n"
            "    messages: Annotated[List[dict], add_messages]      # Lịch sử hội thoại\n"
            "    user_query: str                                     # Câu hỏi gốc của người dùng\n"
            "    employee_context: Optional[dict]                    # Dữ liệu nhân viên từ CRM\n"
            "    retrieved_policies: Optional[List[PolicyChunk]]     # Artifact chính sách trích xuất\n"
            "    eligibility_decision: Optional[dict]                # Phán quyết điều kiện đủ\n"
            "    final_answer: Optional[str]                         # Câu trả lời cuối cùng\n"
            "    current_step: str                                   # Bước điều phối hiện tại\n"
            "    is_completed: bool                                  # Cờ kết thúc hoàn tất\n"
            "```\n"
            "2. Phân định quyền Đọc/Ghi ở từng chuyển trạng thái (State Transition Permissions):\n"
            "- **Node 1: UserInputNode / Router**:\n"
            "  + Ghi: `user_query`, `current_step = 'routing'`.\n"
            "- **Node 2: RetrievalWorker**:\n"
            "  + Đọc: `user_query`.\n"
            "  + Ghi độc quyền: `retrieved_policies` (Bảo đảm artifact chính sách được ghi nhận độc lập, không bị mất khi resume).\n"
            "- **Node 3: PolicyWorker**:\n"
            "  + Đọc: `retrieved_policies`, `employee_context`.\n"
            "  + Ghi độc quyền: `eligibility_decision`.\n"
            "- **Node 4: SynthesisWorker**:\n"
            "  + Đọc: `retrieved_policies`, `eligibility_decision`.\n"
            "  + Ghi: `final_answer`, `is_completed = True`."
        ),
        "explanation": (
            "Việc sử dụng một trường `data: any` cho mọi node ghi đè là nguồn gốc của các lỗi mất mát trạng thái khi hệ thống khôi phục sau sự cố (Resume failure). "
            "Một lược đồ trạng thái mạnh (Strongly-typed State Schema) phân rã từng artifact thành các thuộc tính riêng biệt và gán quyền sở hữu độc quyền "
            "cho từng bước chuyển trạng thái."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Đặc tả Typed State Schema chi tiết] (2.0 điểm): Định nghĩa schema có kiểu dữ liệu rõ ràng, tách riêng user_query, retrieved_policies, eligibility_decision, final_answer.\n"
            "- [Phân định quyền Đọc/Ghi cho từng Node] (1.5 điểm): Chỉ rõ quyền đọc/ghi độc quyền của từng node qua từng bước chuyển trạng thái.\n"
            "- [Khắc phục lỗi mất policy result khi resume] (0.5 điểm): Khẳng định việc tách trường độc quyền giúp checkpoint lưu giữ nguyên vẹn kết quả khi chạy lại."
        ),
        "reference_source": "LangGraph Documentation: 'Defining State Schemas with TypedDict & Pydantic' & Checkpointing Architecture"
    },
    "d09-q035": {
        "sample_answer": (
            "1. Phân tích xung đột ghi đè âm thầm (Silent Overwrite Defect):\n"
            "- Xung đột 1 (`sources`): Cả RetrievalWorker và PolicyWorker đều ghi vào trường `sources`. Khi PolicyWorker chạy sau, nó ghi đè hoàn toàn danh sách nguồn của RetrievalWorker, làm mất các tài liệu tham khảo ban đầu.\n"
            "- Xung đột 2 (`final_answer`): Supervisor ghi đè câu trả lời đã được tra cứu kỹ của worker.\n"
            "- Xung đột 3 (Retry Loss): Khi thử lại (Retry), hệ thống khởi tạo lại mảng rỗng, làm xóa sạch các nguồn thành công ở lần thử trước.\n"
            "2. Thiết kế Quy tắc Sở hữu và Cơ chế Gộp dữ liệu (Ownership & Reducer Rules):\n"
            "- **Quy tắc Sở hữu Đơn quyền (Single-Writer Ownership Principle)**:\n"
            "  + Trường `final_answer`: Chỉ DUY NHẤT một node có thẩm quyền ghi, đó là `SynthesisWorker`. Supervisor tuyệt đối cấm ghi đè vào trường này.\n"
            "  + Tách trường nguồn dữ liệu theo chủ quản: Tách `sources` thành hai trường phân biệt: `retrieval_sources: List[dict]` (do RetrievalWorker sở hữu) và `policy_rule_citations: List[dict]` (do PolicyWorker sở hữu).\n"
            "- **Ngữ nghĩa Gộp dữ liệu khi Thử lại (Additive / Append Reducer Semantics)**:\n"
            "  + Sử dụng hàm gộp Reducer (ví dụ `operator.add` hoặc hàm gộp khử trùng lặp có nhận biết retry) cho danh sách nguồn:\n"
            "    ```python\n"
            "    def merge_sources(existing: List[dict], new_items: List[dict]) -> List[dict]:\n"
            "        # Gộp và khử trùng lặp theo source_id, giữ lại cả nguồn cũ và mới\n"
            "        combined = {item['source_id']: item for item in existing}\n"
            "        for item in new_items:\n"
            "            combined[item['source_id']] = item\n"
            "        return list(combined.values())\n"
            "    ```\n"
            "  + Khi có lần thử lại (Retry), các nguồn hợp lệ từ lần chạy trước không bị xóa mà được tích lũy bổ sung vào danh sách."
        ),
        "explanation": (
            "Trong lập trình điều phối tác tử phân tán, tài nguyên trạng thái chia sẻ (Shared State) phải được bảo vệ bằng các hàm Reducer xác định "
            "và nguyên tắc Đơn quyền sở hữu. Tránh ghi đè tùy tiện bằng cách quy định rõ node nào được phép cập nhật thuộc tính nào."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phân tích đúng 3 xung đột ghi đè] (1.0 điểm): Chỉ ra xung đột sources giữa 2 worker, supervisor ghi đè final_answer, và retry làm mất nguồn cũ.\n"
            "- [Quy tắc Single-Writer & Tách trường sources] (1.5 điểm): Cấm supervisor ghi đè final_answer; tách sources thành retrieval_sources và policy_citations.\n"
            "- [Thiết kế Reducer gộp dữ liệu khi Retry] (1.5 điểm): Cung cấp logic reducer tích lũy và khử trùng lặp nguồn khi thử lại, bảo đảm không thất thoát dữ liệu."
        ),
        "reference_source": "LangGraph Documentation: 'State Reducers and Annotations' (https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers)"
    },
    "d09-q038": {
        "sample_answer": (
            "1. Phê phán cơ chế định tuyến hiện tại (Flaw of Substring Matching):\n"
            "Việc Classifier trả về các chuỗi tự do mập mờ (`next='maybe-tools'`, câu giải thích dài) và đồ thị dùng cách so khớp chuỗi con (`substring in output`) là một thiết kế lỏng lẻo, cực kỳ dễ vỡ (Brittle String Parsing): Một câu như 'Tôi không nghĩ nên gọi tools' vẫn chứa chuỗi con 'tools' và khiến đồ thị rẽ nhầm nhánh!\n"
            "2. Định nghĩa Schema Đầu ra Định tuyến Tường minh (Explicit Routing Schema Contract):\n"
            "Bắt buộc Classifier xuất ra đối tượng JSON theo một tập giá trị đóng hữu hạn (Finite Enum) qua Pydantic / Structured Outputs:\n"
            "```json\n"
            "{\n"
            "  \"type\": \"object\",\n"
            "  \"properties\": {\n"
            "    \"next_node\": {\n"
            "      \"type\": \"string\",\n"
            "      \"enum\": [\"retrieval_node\", \"billing_tool_node\", \"direct_answer_node\", \"human_review_node\", \"UNKNOWN\"]\n"
            "    },\n"
            "    \"confidence_score\": {\"type\": \"number\", \"minimum\": 0.0, \"maximum\": 1.0},\n"
            "    \"decision_reason\": {\"type\": \"string\"}\n"
            "  },\n"
            "  \"required\": [\"next_node\", \"confidence_score\"]\n"
            "}\n"
            "```\n"
            "3. Cơ chế Kiểm tra và Xử lý Giá trị Không biết (Validation & Unknown Handling):\n"
            "- **Bộ kiểm tra hợp đồng (Schema Validator)**: Đọc đầu ra. Nếu không parse được JSON hoặc `next_node` không thuộc tập Enum cho phép, gán ngay `next_node = 'UNKNOWN'`.\n"
            "- **Nhánh kết thúc cho giá trị không biết (Safe Fallback / Dead-Letter Branch)**:\n"
            "  Đồ thị định tuyến: Nếu `next_node == 'UNKNOWN'` hoặc `confidence_score < 0.60`, đồ thị lập tức rẽ nhánh an toàn sang `fallback_clarification_node` (Yêu cầu người dùng làm rõ câu hỏi) hoặc chuyển cấp sang `human_review_node`, tuyệt đối không tự ý chạy bừa một tool nào."
        ),
        "explanation": (
            "Tín hiệu định tuyến (Routing Signal) trong đồ thị tác tử phải là một tín hiệu số tất định (Deterministic Enum Signal). "
            "Tuyệt đối không được dựa dẫm vào việc bóc tách chuỗi văn xuôi tự do. Khái niệm 'Dead-Letter Branch' cho các tín hiệu lạ bảo đảm hệ thống "
            "luôn có lối thoát an toàn khi gặp tình huống bất định."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phê phán cách so khớp chuỗi con] (1.0 điểm): Chỉ ra rủi ro sai lệch của substring matching khi classifier trả văn xuôi dài.\n"
            "- [Đặc tả Schema với tập Enum hữu hạn] (1.5 điểm): Thiết kế schema JSON ràng buộc trường next_node thuộc tập Enum đóng có cấu trúc.\n"
            "- [Xử lý giá trị không biết & Fallback branch] (1.5 điểm): Thiết lập cơ chế kiểm tra schema và định tuyến giá trị UNKNOWN về nhánh an toàn/làm rõ/con người."
        ),
        "reference_source": "LangChain Documentation: 'Structured Outputs and Conditional Routing' & Pydantic Enums"
    },
    "d09-q040": {
        "sample_answer": (
            "1. Phân tích nguyên nhân prompt hiện tại thất bại:\n"
            "Prompt `Bạn là supervisor thông minh. Hãy xử lý yêu cầu tốt nhất` là một prompt không có hợp đồng (Contract-less Prompt), quá mơ hồ và không định hình vai trò. Mô hình không biết khi nào cần điều phối và khi nào cần trả lời, dẫn đến hành vi ngẫu nhiên không tất định (lúc trả tên worker, lúc tự viết câu trả lời).\n"
            "2. Viết lại Prompt Contract Định tuyến Tất định (Rewritten Supervisor Prompt Contract):\n"
            "```markdown\n"
            "# VAI TRÒ:\n"
            "Bạn là Supervisor Điều phối Luồng Tác tử (Agent Flow Orchestrator). Bạn CHỈ CÓ NHIỆM VỤ ĐỊNH TUYẾN. Bạn TUYỆT ĐỐI KHÔNG ĐƯỢC tự viết câu trả lời cho người dùng.\n"
            "\n"
            "# DANH SÁCH WORKER CHO PHÉP VÀ NĂNG LỰC:\n"
            "1. `PolicyWorker`: Tra cứu và giải thích quy chế đào tạo, sổ tay sinh viên.\n"
            "2. `EnrollmentToolWorker`: Tra cứu số dư chỗ ngồi và đăng ký tín chỉ.\n"
            "3. `SynthesisWorker`: Soạn thảo câu trả lời khi tất cả dữ liệu đã được thu thập đầy đủ.\n"
            "4. `FINISH`: Kết thúc phiên làm việc.\n"
            "\n"
            "# QUY TẮC BẮT BUỘC:\n"
            "- Đầu ra của bạn BẮT BUỘC là một JSON object hợp lệ, TUYỆT ĐỐI KHÔNG thêm lời giải thích ngoài khối JSON.\n"
            "- Trường `next_worker` chỉ được chọn từ danh sách: [\"PolicyWorker\", \"EnrollmentToolWorker\", \"SynthesisWorker\", \"FINISH\"].\n"
            "\n"
            "# ĐỊNH DẠNG ĐẦU RA:\n"
            "{\n"
            "  \"next_worker\": \"<Tên worker duy nhất được chọn>\",\n"
            "  \"reason\": \"<Căn cứ ngắn gọn 1 câu giải thích vì sao chọn worker này>\",\n"
            "  \"task_instruction\": \"<Chỉ thị cụ thể chuyển tiếp cho worker>\"\n"
            "}\n"
            "```\n"
            "3. Kiểm soát chấp nhận hoặc từ chối (Acceptance / Rejection Gate):\n"
            "Hệ thống bọc lệnh gọi bằng bộ kiểm tra Pydantic: Nếu đầu ra không phải JSON hoặc `next_worker` nằm ngoài danh mục 4 từ khóa trên, lập tức từ chối và kích hoạt retry với thông báo lỗi cụ thể."
        ),
        "explanation": (
            "Nguyên tắc Prompt Engineering cho Tác tử Điều phối: Biến mô hình ngôn ngữ thành một máy trạng thái hữu hạn (Finite State Machine). "
            "Ràng buộc vai trò dứt khoát, giới hạn tập hành động cho phép và ép định dạng JSON là ba trụ cột bảo đảm tính tất định."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Phê phán prompt mơ hồ hiện tại] (1.0 điểm): Nhận diện lỗi prompt thiếu ràng buộc khiến mô hình hành xử tùy tiện.\n"
            "- [Soạn thảo Prompt Contract đầy đủ] (1.5 điểm): Viết lại prompt có định nghĩa vai trò điều phối thuần túy, danh sách worker năng lực rõ ràng, và cấm tự trả lời.\n"
            "- [Đặc tả JSON Schema & Cổng kiểm tra tự động] (1.5 điểm): Ràng buộc định dạng JSON chuẩn (next_worker, reason) và cơ chế validator chấp nhận/từ chối."
        ),
        "reference_source": "Anthropic Claude Prompt Engineering Guide: 'System Prompts and Structured Outputs' & OpenAI Function Calling"
    },
    "d09-q042": {
        "sample_answer": (
            "1. Lựa chọn Hợp đồng Đúng cho Ranh giới Liên tác tử (Cross-Boundary Contract Selection):\n"
            "- Quyết định: **SỬ DỤNG HỢP ĐỒNG TIN NHẮN TÁC TỬ CÓ CẤU TRÚC (Structured Agent-to-Agent / A2A Message Contract)**, ví dụ JSON-RPC hoặc REST Task Contract. TUYỆT ĐỐI KHÔNG GỬI TOÀN BỘ LANGGRAPH STATE CỤC BỘ.\n"
            "- Lý do: Agent đối tác là một hệ thống bên ngoài ranh giới tin cậy (External Trust Boundary). Gửi toàn bộ LangGraph state cục bộ là lỗi rò rỉ ranh giới (Encapsulation Leak), vừa lộ toàn bộ cấu trúc biến nội bộ, vừa đối mặt rủi ro nhận lại văn xuôi tùy tiện làm sập đồ thị.\n"
            "2. Danh mục các Trường CẦN TRUYỀN (Required Outbound Fields):\n"
            "- `task_id`: Mã định danh nhiệm vụ duy nhất để theo dõi tương quan.\n"
            "- `query_statement`: Yêu cầu nghiệp vụ cụ thể cần đối tác thực hiện.\n"
            "- `parameters`: Tập tham số đầu vào được lọc sạch (chỉ chứa dữ liệu cần thiết cho tác vụ đó).\n"
            "- `callback_url` / `timeout_seconds`: Thông số kỹ thuật của cuộc gọi.\n"
            "3. Danh mục các Trường TUYỆT ĐỐI KHÔNG ĐƯỢC TRUYỀN (Forbidden Outbound Fields):\n"
            "- Toàn bộ biến nội bộ của LangGraph (`checkpoint_id`, `thread_id`, `node_history`, `internal_flags`).\n"
            "- Dữ liệu nhạy cảm của người dùng (PII, Auth tokens, session cookies).\n"
            "- Dữ liệu thô của các worker nội bộ khác không liên quan.\n"
            "4. Xử lý phản hồi từ đối tác:\n"
            "Phản hồi từ đối tác bắt buộc phải tuân thủ Schema kết quả: `{task_id, status: 'SUCCESS'|'ERROR', result_payload: dict}`. Phải có bộ Parser xác thực schema trước khi ánh xạ kết quả vào LangGraph state cục bộ, cấm gán nguyên văn xuôi vào state."
        ),
        "explanation": (
            "Ranh giới giữa các tác tử thuộc các tổ chức/hệ thống khác nhau (Cross-Agent Trust Boundary) phải là ranh giới thông điệp lỏng lẻo "
            "(Loosely Coupled Message Protocol). Chia sẻ không gian bộ nhớ/state trực tiếp phá hủy tính bao gói và tạo ra các lỗ hổng bảo mật nghiêm trọng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chọn đúng A2A Message Contract] (1.5 điểm): Chọn hợp đồng thông điệp có cấu trúc (JSON-RPC/REST), bác bỏ việc gửi LangGraph state cục bộ.\n"
            "- [Liệt kê các trường được truyền] (1.0 điểm): Xác định đúng task_id, query_statement, parameters sạch.\n"
            "- [Liệt kê các trường cấm truyền] (1.0 điểm): Cấm truyền biến LangGraph nội bộ, PII và auth tokens.\n"
            "- [Cơ chế parse response có cấu trúc] (0.5 điểm): Yêu cầu parse và validate schema response trước khi map vào state nội bộ, cấm nhận văn xuôi tùy tiện."
        ),
        "reference_source": "Anthropic / Model Context Protocol: 'Trust Boundaries' & Enterprise Integration Patterns: 'Message-Based Integration'"
    },
    "d09-q044": {
        "sample_answer": (
            "1. Thiết kế Trạng thái Chờ Kiểm tra (Interrupt / Paused State):\n"
            "Trong LangGraph, sử dụng cơ chế `interrupt_before=['execute_refund']` hoặc gắn nhãn trạng thái:\n"
            "- Trạng thái: `state.status = 'AWAITING_HUMAN_REVIEW'`.\n"
            "- Điều kiện kích hoạt rẽ nhánh vào trạng thái này:\n"
            "  `if refund_amount >= 1_000_000 or policy_evidence.has_conflicts == True:`\n"
            "2. Thiết kế Payload Cung cấp cho Người duyệt (Reviewer Payload Contract):\n"
            "Payload gửi lên giao diện quản trị viên (Admin Review Dashboard) phải súc tích, đầy đủ bằng chứng để ra quyết định ngay lập tức:\n"
            "```json\n"
            "{\n"
            "  \"case_id\": \"REF-2026-9981\",\n"
            "  \"user_id\": \"USR-4412\",\n"
            "  \"amount\": 1500000,\n"
            "  \"trigger_reason\": \"EXCEEDS_THRESHOLD_1M\",\n"
            "  \"evidence_summary\": {\n"
            "    \"policy_clause\": \"Điều 8.2: Hoàn phí đặc biệt khi có xác nhận y tế\",\n"
            "    \"conflict_flag\": false,\n"
            "    \"source_citations\": [\"policy_v3.pdf#page=12\"]\n"
            "  },\n"
            "  \"created_at\": \"2026-10-23T14:30:00Z\"\n"
            "}\n"
            "```\n"
            "3. Thao tác Chấp thuận / Từ chối và Cách Tiếp tục Chạy an toàn (Resume Protocol):\n"
            "- Người vận hành nhấn nút trên UI gửi API request:\n"
            "  + **Nếu Chấp thuận (Approve)**: Gửi payload `{action: 'APPROVE', reviewer_id: 'AD-09', note: 'Đủ điều kiện y tế'}`. Hệ thống cập nhật `state.status = 'APPROVED'`, ghi nhật ký kiểm toán và kích hoạt lệnh tiếp tục chạy từ checkpoint: `graph.invoke(Command(resume={'approved': True}), config=thread_config)` để gọi `PaymentToolWorker`.\n"
            "  + **Nếu Từ chối (Reject)**: Gửi payload `{action: 'REJECT', reviewer_id: 'AD-09', reason: 'Thiếu bệnh án gốc'}`. Hệ thống cập nhật `state.status = 'REJECTED'`, chuyển thẳng sang node thông báo từ chối cho học viên, không gọi tool thanh toán."
        ),
        "explanation": (
            "Cơ chế Con người trong Vòng lặp (Human-in-the-Loop - HITL) là hàng rào phòng thủ tối thượng cho các hành động có rủi ro tài chính cao. "
            "Framework điều phối hiện đại (như LangGraph) sử dụng cơ chế Checkpointing và Resume Interrupt để đóng băng trạng thái an toàn, "
            "chờ phê duyệt có xác thực danh tính trước khi giải phóng tác dụng phụ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Thiết kế State AWAITING_HUMAN_REVIEW] (1.0 điểm): Định nghĩa điều kiện kích hoạt: tiền >= 1 triệu hoặc bằng chứng mâu thuẫn.\n"
            "- [Đặc tả Payload cho người duyệt đầy đủ] (1.5 điểm): Thiết kế JSON payload hiển thị cho admin: case_id, amount, trigger_reason, policy clause, citations.\n"
            "- [Thao tác Approve/Reject & Cơ chế Resume an toàn] (1.5 điểm): Trình bày rõ ràng luồng resume từ checkpoint khi approve (gọi payment) và rẽ nhánh từ chối khi reject."
        ),
        "reference_source": "LangGraph Documentation: 'Human-in-the-Loop & Breakpoints' (https://langchain-ai.github.io/langgraph/how-tos/human-in-the-loop/)"
    },
    "d09-q047": {
        "sample_answer": (
            "1. Phân tích Phần mà Chuẩn MCP (Model Context Protocol) THỰC SỰ GIẢI QUYẾT:\n"
            "MCP là một **Giao thức Chuẩn hóa Giao diện và Khả năng Tương tác (Interface Interoperability Protocol)**. Nó giải quyết xuất sắc:\n"
            "- Chuẩn hóa cách máy khách (Client) khám phá các công cụ (Tool Discovery).\n"
            "- Chuẩn hóa khuôn dạng đóng gói lời gọi (JSON-RPC 2.0 encapsulation) và định dạng truyền nhận dữ liệu (`tools/call`, `tools/list`).\n"
            "- Tách rời mã nguồn của Agent khỏi mã nguồn của Server cung cấp dịch vụ qua các transport chuẩn (stdio, SSE).\n"
            "2. Ba Phần BẮT BUỘC VẪN PHẢI THIẾT KẾ ĐỘC LẬP (What MCP Does NOT Solve):\n"
            "- **Phần 1: Kiểm soát Phân quyền & Thẩm quyền (Authorization & Access Control - RBAC/ABAC)**:\n"
            "  MCP chỉ là đường ống truyền lệnh; nó không biết ai đang gọi. Bắt buộc phải thiết kế lớp xác thực danh tính người dùng/agent và kiểm tra quyền hạn (User Authorization Check): Agent có quyền hoàn tiền hay không? Hạn mức hoàn tiền của phiên này là bao nhiêu?\n"
            "- **Phần 2: Xác thực Ràng buộc Nghiệp vụ và Schema Dữ liệu (Business Logic & Payload Validation)**:\n"
            "  MCP server vẫn có thể nhận tham số độc hại hoặc sai lệch logic (ví dụ: `amount = -5000000` hoặc `order_id` giả mạo). Server phải tự cài đặt bộ kiểm tra schema và logic kiểm tra hợp lệ của giao dịch.\n"
            "- **Phần 3: Cổng Phê duyệt Tác dụng phụ (Human-in-the-loop / Side-Effect Approval Gate)**:\n"
            "  Hành động hoàn tiền làm thất thoát tiền thật từ tài khoản công ty. Một lời gọi MCP tool không thể tự ý coi là đã được duyệt; bắt buộc phải có cổng phê duyệt chính sách trước khi tiền được chuyển."
        ),
        "explanation": (
            "Một ngộ nhận nguy hiểm trong cộng đồng phát triển AI là đánh đồng 'Chuẩn giao thức kết nối' (Protocol Standardization) với 'Bảo mật nghiệp vụ' (Business Security). "
            "Bọc một API bằng MCP không làm cho API đó an toàn hơn nếu thiếu vắng các lớp kiểm soát quyền hạn và xác thực dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Xác định đúng phần MCP giải quyết] (1.0 điểm): Nêu rõ MCP chỉ chuẩn hóa interface discovery, cú pháp JSON-RPC và tách rời transport kết nối.\n"
            "- [Phân tích Phần 1: Authorization & RBAC] (1.0 điểm): Nhấn mạnh MCP không thay thế được việc kiểm tra quyền và hạn mức tài chính.\n"
            "- [Phân tích Phần 2: Business Logic & Schema Validation] (1.0 điểm): Nhấn mạnh sự cần thiết của kiểm tra tham số (số tiền âm, ID giả).\n"
            "- [Phân tích Phần 3: Human Approval Gate] (1.0 điểm): Nhấn mạnh tác vụ tài chính có side-effect bắt buộc phải có cổng phê duyệt con người."
        ),
        "reference_source": "Anthropic Model Context Protocol (MCP) Specification: 'Security and Trust Architecture' (https://modelcontextprotocol.io)"
    },
    "d09-q049": {
        "sample_answer": (
            "1. Gán Primitive Chuẩn của MCP cho từng thành phần (MCP Primitive Assignment):\n"
            "- `refund_policy.pdf` -> Gán là **MCP Resource (Tài nguyên)**: `resource://docs/refund_policy.pdf`.\n"
            "  + Bản chất: Dữ liệu văn bản tĩnh chỉ đọc (Read-only Context), dùng để nạp vào ngữ cảnh của mô hình ngôn ngữ.\n"
            "- `issue_refund(amount, order_id)` -> Gán là **MCP Tool (Công cụ)**: `tools/issue_refund`.\n"
            "  + Bản chất: Hàm thực thi có tác dụng phụ (Executable Action with Side-effects), làm thay đổi trạng thái cơ sở dữ liệu và biến động dòng tiền thực tế.\n"
            "- `draft_refund_reply` -> Gán là **MCP Prompt (Mẫu Prompt)**: `prompts/draft_refund_reply`.\n"
            "  + Bản chất: Mẫu cấu trúc hướng dẫn tương tác được tiêu chuẩn hóa có tham số hóa để người dùng hoặc agent bắt đầu một phiên hội thoại.\n"
            "2. Yêu cầu Phân quyền (Authorization) khác nhau giữa các Primitive:\n"
            "- **Với Resource (`refund_policy.pdf`)**: Phân quyền Chỉ Đọc (Read-only Permissions). Bất kỳ agent hoặc người dùng nào có quyền tra cứu thông tin đều được phép đọc mà không gây rủi ro an toàn.\n"
            "- **Với Tool (`issue_refund`)**: Phân quyền Thực thi Nghiêm ngặt (Strict Execution Authorization & Transaction Scope). Bắt buộc phải có token phân quyền quản trị viên tài chính (Finance Admin Scope) và kiểm tra hạn mức tiền tệ.\n"
            "3. Điều TUYỆT ĐỐI KHÔNG NÊN GỘP:\n"
            "- Tuyệt đối không được gộp Resource đọc chính sách và Tool hoàn tiền vào cùng một đặc tả quyền hạn (Scope).\n"
            "- Lý do: Nếu gộp chung, một agent chỉ cần quyền đọc tài liệu chính sách sẽ vô tình được cấp luôn quyền gọi lệnh hoàn tiền, vi phạm nghiêm trọng Nguyên tắc Đặc quyền Tối thiểu (Principle of Least Privilege)."
        ),
        "explanation": (
            "Ba thành phần cốt lõi của MCP (Resources, Tools, Prompts) đại diện cho ba mô hình tương tác hoàn toàn khác nhau: Đọc dữ liệu thụ động (Resources), "
            "Thực thi hành động chủ động có tác dụng phụ (Tools), và Cấu trúc hóa giao tiếp (Prompts). Việc phân tách rành mạch này là nền tảng "
            "để áp dụng các chính sách phân quyền bảo mật chuyên biệt."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Gán đúng 3 MCP Primitives] (1.5 điểm): Gán chính xác refund_policy là Resource, issue_refund là Tool, và draft_reply là Prompt.\n"
            "- [Phân tích khác biệt về Authorization] (1.5 điểm): Chỉ ra Resource chỉ cần quyền đọc rộng rãi, còn Tool issue_refund bắt buộc kiểm soát quyền thực thi tài chính nghiêm ngặt.\n"
            "- [Cảnh báo cấm gộp Scope] (1.0 điểm): Nhấn mạnh việc cấm gộp quyền đọc và quyền hoàn tiền để bảo đảm Principle of Least Privilege."
        ),
        "reference_source": "Model Context Protocol Specification: 'Architecture - Resources, Prompts, and Tools' (https://modelcontextprotocol.io/docs/concepts/architecture)"
    },
    "d09-q051": {
        "sample_answer": (
            "1. Mô tả luồng thực thi trong thời gian chạy (Runtime Execution Flow):\n"
            "- Bước 1 (Discovery Phase - Khám phá Năng lực): Client khởi động kết nối MCP tới Server và gọi phương thức `tools/list` để nhận danh sách công cụ và JSON Schema mới nhất của từng công cụ.\n"
            "- Bước 2 (Contract Comparison / Validation): Client phát hiện server đã cập nhật `search_policy` với 3 trường bắt buộc: `{query, employee_type, effective_year}`.\n"
            "- Bước 3 (Call Attempt & Detection): Lớp logic cũ của Client gọi cứng `search_policy(q=...)` -> Client phát hiện tham số `q` không khớp với schema mới, thiếu `query`, `employee_type`, `effective_year`.\n"
            "- Bước 4 (Execution Decision): Nếu Client gửi lệnh gọi cũ lên Server, MCP Server sẽ trả về mã lỗi JSON-RPC chuẩn: `-32602 Invalid params: Missing required fields [employee_type, effective_year]`.\n"
            "2. Cách xử lý lời gọi cũ và Cơ chế Chuyển tiếp Tương thích ngược (Backward Compatibility & Migration):\n"
            "- **Bộ điều hợp Tương thích ngược tại Client hoặc Server (Schema Adapter / Polyfill)**:\n"
            "  + Thiết lập lớp ánh xạ tham số: Nếu phát hiện lời gọi cũ có tham số `q`, tự động đổi tên thành `query = q`.\n"
            "  + Điền giá trị mặc định an toàn cho các trường mới: `employee_type = 'permanent'`, `effective_year = current_year` (kèm theo log cảnh báo Deprecation Warning).\n"
            "- **Chính sách Phiên bản hóa Công cụ (Tool Versioning Protocol)**:\n"
            "  Server không nên phá vỡ schema cũ đột ngột. Cần công bố `search_policy_v2` hoặc hỗ trợ cả hai cú pháp trong thời gian chuyển tiếp (Deprecation Window)."
        ),
        "explanation": (
            "Sức mạnh của MCP nằm ở khả năng Khám phá Thời gian chạy (Runtime Discovery): Client không nên phụ thuộc vào các hàm gán cứng (Hardcoded Calls), "
            "mà phải đọc và xác thực với JSON Schema được công bố động qua `tools/list`. Khi schema thay đổi, cần có cơ chế Adapter và Versioning "
            "để duy trì tính ổn định của hệ thống."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Mô tả luồng Discovery & Schema Mismatch] (1.5 điểm): Mô tả rõ luồng client gọi tools/list, phát hiện schema mới và server trả lỗi invalid params nếu gọi tham số cũ.\n"
            "- [Cơ chế Adapter ánh xạ tham số cũ] (1.5 điểm): Đưa ra giải pháp adapter ánh xạ q sang query và điền mặc định an toàn cho employee_type, effective_year.\n"
            "- [Chính sách Versioning & Deprecation] (1.0 điểm): Nhấn mạnh quy tắc phiên bản hóa công cụ (tool versioning) để duy trì tương thích ngược."
        ),
        "reference_source": "Model Context Protocol Specification: 'Dynamic Tool Discovery & Error Handling' & JSON-RPC 2.0 Specification"
    },
    "d09-q053": {
        "sample_answer": (
            "1. Lựa chọn Transport Phù hợp cho Dịch vụ Từ xa (Transport Selection):\n"
            "Chọn **Server-Sent Events qua HTTP (SSE Transport)** hoặc **WebSocket Transport** có reverse proxy (Nginx/Envoy). TUYỆT ĐỐI BÃI BỎ stdio qua SSH.\n"
            "- Căn cứ kỹ thuật: `stdio` được thiết kế thuần túy cho giao tiếp tiến trình cục bộ (Local Subprocess / Child Process). Việc chạy stdio qua SSH cho một dịch vụ từ xa phục vụ nhiều client dẫn đến việc các client tranh chấp cùng một stream I/O, khóa tiến trình (Process Contention), rò rỉ session SSH và hoàn toàn thiếu cơ chế quản lý vòng đời mạng chuẩn.\n"
            "2. Mô tả Vòng đời Khởi tạo và Quản lý Kết nối (Initialization Lifecycle):\n"
            "- Client gửi HTTP POST/GET tới `/sse` để thiết lập kênh nhận sự kiện một chiều từ server.\n"
            "- Server cấp phát một `session_id` duy nhất cho client và trả về endpoint gửi lệnh: `/messages?session_id=...`.\n"
            "- Client gửi gói tin `initialize` chứa phiên bản giao thức và khả năng (capabilities); server phản hồi `initialized` xác nhận sẵn sàng.\n"
            "3. Cơ chế Xử lý Lỗi và Kết nối lại Tự động (Healthcheck & Reconnection):\n"
            "- Gửi tín hiệu nhịp tim định kỳ (Heartbeat / Ping-Pong): Server gửi comment `:ping` mỗi 15 giây; nếu sau 45 giây không nhận được, client chủ động ngắt kết nối.\n"
            "- Tự động kết nối lại với lũy thừa giãn cách (Exponential Backoff with Jitter): Client tự động reconnect kèm theo header `Last-Event-ID` để server phát lại các message bị gián đoạn.\n"
            "4. Quy trình Tắt Dịch vụ Mềm (Graceful Shutdown):\n"
            "- Server gửi thông báo `notifications/cancelled` cho các tác vụ đang chạy, hoàn tất các lời gọi dở dang trong thời gian chờ (Drain Period: 10s), sau đó đóng kênh SSE an toàn với HTTP 200."
        ),
        "explanation": (
            "Quản lý vòng đời truyền tải (Transport Lifecycle) trong MCP đòi hỏi chọn đúng công cụ cho đúng môi trường. "
            "Stdio dành cho local execution; SSE/HTTP dành cho distributed multi-client architecture. Một hệ thống từ xa chuyên nghiệp bắt buộc "
            "phải có cơ chế định danh phiên (Session ID), nhịp tim kiểm tra liveness và quy trình phục hồi kết nối tự động."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- [Chọn đúng SSE/HTTP Transport & Phê phán stdio/SSH] (1.5 điểm): Bác bỏ stdio qua SSH do tranh chấp process; chọn SSE/HTTP chuẩn cho dịch vụ từ xa.\n"
            "- [Mô tả quy trình khởi tạo với Session ID] (1.0 điểm): Mô tả rõ quy trình handshake SSE, cấp session_id và initialize.\n"
            "- [Cơ chế Heartbeat & Reconnect có Backoff] (1.0 điểm): Thiết lập ping/pong định kỳ và tự động kết nối lại với exponential backoff.\n"
            "- [Quy trình tắt dịch vụ mềm Graceful Shutdown] (0.5 điểm): Mô tả việc hoàn tất tác vụ dở dang và giải phóng tài nguyên an toàn."
        ),
        "reference_source": "Anthropic Model Context Protocol: 'Transports - SSE vs. Stdio' (https://modelcontextprotocol.io/docs/concepts/transports)"
    }
}
