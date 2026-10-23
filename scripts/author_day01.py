"""
Authoring module for Day 01 essay questions (49 questions).
Generates sample_answer, explanation, rubric, reference_source for d01-q006 through d01-q149.
"""

def get_day01_data():
    data = {}

    # 1. d01-q006 (3 pts)
    data["d01-q006"] = {
        "sample_answer": (
            "1. Điểm nghẽn của hệ chuyên gia (Expert Systems): Xảy ra hiện tượng 'nghẽn cổ chai thu nhận tri thức' "
            "(knowledge acquisition bottleneck). Tri thức chuyên gia trong thực tế mang tính ngầm định (tacit knowledge), "
            "mơ hồ và chứa vô số ngoại lệ. Việc viết và duy trì hàng ngàn quy tắc 'if-then' thủ công dẫn đến sự bùng nổ "
            "tổ hợp (combinatorial explosion), xung đột quy tắc và hệ thống trở nên cực kỳ giòn (brittle) — chỉ cần một "
            "dữ liệu ngoài dự liệu là hệ thống tê liệt hoàn toàn, không thể tự mở rộng.\n"
            "2. Phần việc thủ công mà Deep Learning đã giảm bớt so với Machine Learning thống kê: Deep Learning loại bỏ "
            "hoàn toàn khâu trích xuất và thiết kế đặc trưng thủ công (manual feature engineering / handcrafted features). "
            "Trong ML thống kê cổ điển, kỹ sư phải tự tay thiết kế các hàm trích xuất đặc trưng (như SIFT, HOG, n-gram). "
            "Deep Learning thay thế khâu này bằng kiến trúc mạng nơ-ron nhiều tầng có khả năng học biểu diễn đặc trưng phân tầng "
            "tự động (hierarchical representation learning / end-to-end) trực tiếp từ dữ liệu thô."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Sự tiến hóa từ hệ chuyên gia sang ML thống kê và Deep Learning phản ánh quy luật "
            "chuyển giao công việc từ con người sang thuật toán tính toán. Hệ chuyên gia yêu cầu con người tự viết cả quy tắc và logic; "
            "ML thống kê giải phóng con người khỏi việc viết luật suy diễn nhưng vẫn bắt con người thiết kế đặc trưng (features); "
            "Deep Learning với kiến trúc nơ-ron phân tầng giải quyết triệt để khâu biểu diễn (representation learning), tạo điều kiện "
            "cho các mô hình nền tảng (Foundation Models) mở rộng quy mô dữ liệu và tham số không giới hạn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Điểm nghẽn hệ chuyên gia (1.5 điểm): Nêu rõ nghẽn thu nhận tri thức (knowledge acquisition bottleneck), bùng nổ tổ hợp quy tắc mâu thuẫn/ngoại lệ và tính giòn (brittle) khi mở rộng.\n"
            "- Đóng góp của Deep Learning (1.5 điểm): Nêu rõ việc loại bỏ trích xuất đặc trưng thủ công (handcrafted feature engineering) và chuyển sang học biểu diễn tự động phân tầng (end-to-end representation learning)."
        ),
        "reference_source": "LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444. https://doi.org/10.1038/nature14539; Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Pearson."
    }

    # 2. d01-q011 (3 pts)
    data["d01-q011"] = {
        "sample_answer": (
            "- Xếp hệ thống trên trục: Hệ thống nằm ở mức 'Retrieval-Augmented Chatbot' (Chatbot có bộ nhớ và truy xuất ngữ cảnh), "
            "cao hơn LLM độc lập (standalone LLM) nhưng chưa đạt tới mức Agent tự chủ (Autonomous Tool-Using Agent).\n"
            "- Hai tính năng mạnh hơn LLM độc lập: (1) Khả năng grounded tri thức bên ngoài qua truy xuất câu hỏi thường gặp (FAQ RAG), "
            "giúp giảm thiểu ảo giác và cung cấp câu trả lời chính xác theo tài liệu nghiệp vụ; (2) Lưu giữ trạng thái ngữ cảnh hội thoại "
            "qua 5 lượt trao đổi gần nhất (short-term conversation memory), cho phép hiểu các câu hỏi nối tiếp và đại từ thay thế.\n"
            "- Một năng lực còn thiếu để trở thành agent dùng công cụ: Khả năng tự chủ gọi công cụ (Tool / Function Calling) và vòng lặp "
            "phản hồi ReAct (Action -> Observation). Hiện tại hệ thống không thể tự quyết định khi nào cần gọi API bên ngoài, không thể truyền "
            "tham số có cấu trúc và không thể quan sát kết quả từ công cụ để suy luận tiếp."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Một agent thực thụ đòi hỏi chu trình ReAct (Reasoning + Acting) khép kín: Suy nghĩ (Thought) -> "
            "Hành động gọi tool (Action) -> Quan sát kết quả từ môi trường (Observation) -> Phản hồi. Hệ thống trong đề bài chỉ là luồng đường ống "
            "một chiều (static pipeline) nhúng thông tin có sẵn vào prompt trước khi gọi mô hình một lần duy nhất, không có vòng lặp hành vi tự thích ứng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân loại vị trí trên trục (1.0 điểm): Xác định đúng hệ thống là Chatbot có RAG/Memory, nằm giữa LLM độc lập và Agent.\n"
            "- Hai tính năng vượt trội (1.0 điểm): Nêu chính xác truy xuất FAQ (RAG) và bộ nhớ ngữ cảnh 5 lượt gần nhất.\n"
            "- Năng lực còn thiếu cốt lõi (1.0 điểm): Nêu rõ khả năng tự chủ gọi công cụ (tool/function calling) và xử lý kết quả quan sát môi trường."
        ),
        "reference_source": "Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629. https://arxiv.org/abs/2210.03629; LangChain Documentation - Agent Concepts (https://python.langchain.com/docs/concepts/agents/)"
    }

    # 3. d01-q017 (3 pts)
    data["d01-q017"] = {
        "sample_answer": (
            "1. Giải thích vì sao không thể chỉ đếm từ: Các mô hình ngôn ngữ lớn (LLM) không xử lý văn bản theo từng từ nguyên vẹn mà sử dụng "
            "các thuật toán token hóa sub-word (như BPE, WordPiece, Unigram). Thuật toán này băm văn bản dựa trên tần suất xuất hiện trong tập huấn luyện. "
            "Những từ hiếm, từ ghép phức tạp, từ đa âm tiết, ký tự có dấu hoặc thuật ngữ chuyên ngành sẽ bị chia tách thành nhiều sub-tokens hoặc "
            "các byte đơn lẻ. Do đó, hai chuỗi có cùng số từ (5 từ) nhưng có thể chênh lệch rất lớn về số lượng token thực tế tùy thuộc vào độ quen thuộc "
            "của từ vựng.\n"
            "2. So sánh lượng ngữ cảnh tiêu tốn:\n"
            "- Chuỗi A khi lặp 1.000 lần: 7 token × 1.000 = 7.000 token.\n"
            "- Chuỗi B khi lặp 1.000 lần: 13 token × 1.000 = 13.000 token.\n"
            "Kết luận: Chuỗi B tốn ngữ cảnh hơn chuỗi A nhiều lần (13.000 token so với 7.000 token, chênh lệch 6.000 token, tốn gấp ~1,86 lần)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Cửa sổ ngữ cảnh (context window), thông lượng (throughput) và chi phí API đều được định lượng "
            "theo đơn vị Token. Việc ước tính tài nguyên theo số từ (word count) là sai lầm phổ biến dẫn đến lỗi tràn ngữ cảnh (context overflow) "
            "hoặc vượt ngân sách chi phí khi xử lý các ngôn ngữ có hình thái phong phú hoặc dữ liệu phi tiếng Anh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Giải thích bản chất Tokenizer (1.5 điểm): Nêu rõ cơ chế sub-word tokenization (BPE/WordPiece) phụ thuộc vào tần suất từ vựng khiến cùng số từ nhưng khác số token.\n"
            "- Tính toán và kết luận chính xác (1.5 điểm): Tính đúng A = 7.000 token, B = 13.000 token và khẳng định Chuỗi B tốn ngữ cảnh hơn chuỗi A 6.000 token."
        ),
        "reference_source": "OpenAI Documentation - What are tokens and how to count them? https://platform.openai.com/docs/guides/embeddings; Sennrich, R., et al. (2016). Neural Machine Translation of Rare Words with Subword Units. https://arxiv.org/abs/1508.07909"
    }

    # 4. d01-q021 (3 pts)
    data["d01-q021"] = {
        "sample_answer": (
            "- Lỗi kỹ thuật: Lỗi Tokenizer Mismatch (không đồng nhất bộ mã hóa token giữa thư viện client và mô hình runtime). "
            "Dự án gửi request cho mô hình `alpha-chat` nhưng hàm đếm token lại khởi tạo bộ mã hóa của mô hình `beta-chat` "
            "(`encoding_for_model('beta-chat')`). Mỗi dòng mô hình có tập từ vựng (vocabulary), quy tắc phân tách regex và cơ chế ghép byte "
            "khác nhau, dẫn đến việc đếm sai lệch số lượng token thực tế mà server mô hình nhận được.\n"
            "- Số token đúng phải trả về: Chính xác 11 token (kết quả mã hóa tương ứng với mô hình `alpha-chat` thực sự phục vụ request)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tính nhất quán giữa client-side token counting và server-side model tokenizer là nguyên tắc bắt buộc "
            "để kiểm soát chi phí và ngăn ngừa lỗi tràn context window. Việc ước lượng thấp hơn thực tế (đếm ra 9 nhưng server tính 11) có thể khiến "
            "hệ thống bị từ chối phục vụ (HTTP 400 Bad Request) khi prompt tiến sát giới hạn ngữ cảnh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xác định đúng bản chất lỗi (1.5 điểm): Nêu rõ lỗi Tokenizer Mismatch do gọi bộ mã hóa không tương thích giữa alpha-chat và beta-chat.\n"
            "- Trả về chính xác số token hợp lệ (1.5 điểm): Xác định đúng số token phải trả về là 11 token."
        ),
        "reference_source": "Tiktoken Library Documentation - OpenAI. https://github.com/openai/tiktoken; OpenAI Cookbook - How to count tokens with tiktoken (https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)"
    }

    # 5. d01-q024 (3 pts)
    data["d01-q024"] = {
        "sample_answer": (
            "- Hướng thay đổi temperature: Cần TĂNG giá trị `temperature` (ví dụ từ mức thấp ~0.0 - 0.2 lên mức ~0.7 - 0.9 hoặc 1.0). "
            "Khi tăng temperature, phân phối xác suất softmax trên toàn bộ từ vựng bị làm phẳng (flattened distribution), làm giảm độ chênh lệch "
            "xác suất giữa token đứng đầu và các token đứng sau, kích thích mô hình khám phá các từ ngữ và cấu trúc câu mới mẻ, phá vỡ sự rập khuôn lặp lại.\n"
            "- Rủi ro cần theo dõi: Nguy cơ xuất hiện ảo giác (hallucination), câu văn mất tính mạch lạc/ngữ pháp (syntactic incoherence), "
            "hoặc slogan đi chệch khỏi tông giọng thương hiệu, trở nên kỳ dị hoặc vô nghĩa (unconstrained generation)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Temperature ($T$) là tham số điều tiết độ entropy trong hàm softmax: $P(w_i) = \\frac{\\exp(z_i / T)}{\\sum_j \\exp(z_j / T)}$. "
            "Khi $T$ thấp, mô hình tiến gần về greedy decoding gây lặp từ; tăng $T$ giúp tăng tính đa dạng sáng tạo (diversity), nhưng cần kết hợp "
            "với các bộ lọc hậu xử lý hoặc tham số `top_p` để kiểm soát chất lượng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Đề xuất đúng hướng tham số (1.5 điểm): Khẳng định tăng temperature và giải thích cơ chế làm phẳng phân phối xác suất softmax để tăng tính đa dạng.\n"
            "- Nhận diện đúng rủi ro kỹ thuật (1.5 điểm): Nêu rõ rủi ro mất mạch lạc, ảo giác hoặc câu văn vô nghĩa, chệch hướng yêu cầu."
        ),
        "reference_source": "Holtzman, A., et al. (2020). The Curious Case of Neural Text Degeneration (Nucleus Sampling). ICLR 2020. https://arxiv.org/abs/1904.09751; OpenAI API Reference - Sampling Parameters."
    }

    # 6. d01-q031 (3 pts)
    data["d01-q031"] = {
        "sample_answer": (
            "- Stop sequence cần thiết lập: `[\"<END_RECORD>\"]` (truyền chuỗi ký tự `\"<END_RECORD>\"` vào tham số `stop` của API gọi mô hình).\n"
            "- Phần đầu ra được giữ lại: `\"Lan|8\"` (mô hình sẽ ngắt quá trình autoregressive decoding ngay khi chuẩn bị sinh token của `\"<END_RECORD>\"`; "
            "chuỗi dừng bị loại bỏ khỏi output trả về và toàn bộ phần bản ghi phía sau `\"Minh|9\"` hoàn toàn không bị sinh ra, giúp tối ưu tối đa chi phí và độ trễ)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Stop sequence là cơ chế can thiệp sớm tại cấp độ sinh token (token-level early stopping). "
            "Thay vì để mô hình sinh toàn bộ chuỗi rồi dùng regex cắt chuỗi ở tầng backend, việc thiết lập stop sequence tại runtime của LLM "
            "giúp tiết kiệm token đầu ra (completion tokens) và giảm độ trễ Time-to-Last-Token (TTLT)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xác định đúng stop sequence (1.5 điểm): Chỉ định chính xác chuỗi dừng `\"<END_RECORD>\"`.\n"
            "- Xác định đúng đầu ra giữ lại (1.5 điểm): Nêu đúng kết quả thu được là `\"Lan|8\"` và giải thích việc ngăn chặn phần bản ghi thừa phía sau."
        ),
        "reference_source": "OpenAI API Reference - Stop Sequences (https://platform.openai.com/docs/api-reference/chat/create#chat-create-stop); Anthropic Claude Messages API - Stop Sequences."
    }

    # 7. d01-q032 (3 pts)
    data["d01-q032"] = {
        "sample_answer": (
            "1. Xác định lần gọi có vừa cửa sổ ngữ cảnh không:\n"
            "- Tổng token đầu vào = Lời nhắc (3.000) + Lịch sử hội thoại (24.000) + Ngữ cảnh truy xuất (70.000) = 97.000 token.\n"
            "- Tổng tải yêu cầu của lần gọi = Token đầu vào (97.000) + Giới hạn đầu ra (40.000) = 137.000 token.\n"
            "- So sánh với giới hạn: 137.000 token > 128.000 token (vượt quá 9.000 token).\n"
            "-> Kết luận: Lần gọi này KHÔNG vừa cửa sổ ngữ cảnh (sẽ bị API từ chối với lỗi HTTP 400 ContextWindowExceeded).\n\n"
            "2. Số token đầu vào tối thiểu cần giảm:\n"
            "- Để giữ nguyên giới hạn đầu ra 40.000 token trong dung lượng 128.000 token, ngân sách tối đa dành cho đầu vào là: 128.000 - 40.000 = 88.000 token.\n"
            "- Số token đầu vào tối thiểu cần giảm là: 97.000 - 88.000 = 9.000 token."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Cửa sổ ngữ cảnh của LLM là giới hạn cứng áp dụng cho tổng của cả chuỗi đầu vào và chuỗi đầu ra: "
            "$L_{input} + L_{max\\_output} \\le L_{context\\_window}$. Trong kiến trúc RAG quy mô lớn, bộ quản lý ngữ cảnh (Context Window Budgeter) "
            "bắt buộc phải thực hiện cắt tỉa (pruning) hoặc nén ngữ cảnh truy xuất trước khi dispatch request đến model."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Tính tổng tải và kết luận tính khả thi (1.5 điểm): Thiết lập phép tính 3.000 + 24.000 + 70.000 + 40.000 = 137.000 token và kết luận không vừa (vượt ngưỡng 128.000).\n"
            "- Tính chính xác lượng token đầu vào cần giảm (1.5 điểm): Tính đúng cần giảm tối thiểu 9.000 token đầu vào (giữ đầu vào <= 88.000 token)."
        ),
        "reference_source": "OpenAI Documentation - Managing context limits (https://platform.openai.com/docs/guides/text-generation); Anthropic Claude Documentation - Context Window Limits."
    }

    # 8. d01-q036 (3 pts)
    data["d01-q036"] = {
        "sample_answer": (
            "1. Đề xuất thay đổi về cách truy xuất / tổ chức thông tin: Thay vì gửi nguyên văn 400 trang theo thứ tự gốc, cần áp dụng RAG phân đoạn "
            "(chunking thành các đoạn nhỏ 500-1000 token có cấu trúc) kết hợp bộ lọc metadata và re-ranking. Nếu cần gửi nhiều đoạn ngữ cảnh, "
            "phải đặt điều khoản trọng yếu nhất lên đầu hoặc xuống cuối prompt nhằm khắc phục hiện tượng 'Lost in the Middle' (mô hình chú ý kém ở giữa ngữ cảnh dài).\n"
            "2. Thông tin phải giữ để câu trả lời kiểm chứng được: Bắt buộc phải giữ lại trích dẫn nguyên văn điều khoản (verbatim quote), số hiệu điều/khoản/chương, "
            "tiêu đề mục, số trang trong tài liệu gốc và phiên bản/ngày ban hành của chính sách."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Hiện tượng 'Lost in the Middle' chứng minh sự suy giảm hiệu quả chú ý của cơ chế Self-Attention "
            "khi thông tin nằm sâu giữa ngữ cảnh khổng lồ. Thiết kế hệ thống thông minh đòi hỏi phải tinh lọc ngữ cảnh tập trung (high signal-to-noise ratio) "
            "và bảo toàn siêu dữ liệu truy vết nguồn gốc (provenance metadata) để người dùng và hệ thống audit có thể đối chiếu độ tin cậy."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Đề xuất tổ chức thông tin (1.5 điểm): Nêu giải pháp chia nhỏ (chunking/RAG) và sắp xếp vị trí ưu tiên đầu/cuối để tránh hiện tượng Lost in the Middle.\n"
            "- Thông tin kiểm chứng bắt buộc (1.5 điểm): Nêu rõ trích dẫn nguyên văn, số điều khoản, số trang/mục và phiên bản tài liệu để truy vết nguồn."
        ),
        "reference_source": "Liu, N. F., et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. TACL 2024. https://arxiv.org/abs/2307.03172; LangChain RAG Architecture Guide."
    }

    # 9. d01-q038 (3 pts)
    data["d01-q038"] = {
        "sample_answer": (
            "Quy trình trả lời an toàn gồm 3 bước:\n"
            "1. Kiểm tra giới hạn tri thức (Knowledge Cutoff Check): Nhận diện truy vấn yêu cầu dữ kiện mang tính biến động thời gian thực (chức vụ lãnh đạo hiện tại) "
            "vượt ngoài mốc cutoff của trọng số tĩnh; không tự suy đoán dựa trên dữ liệu huấn luyện cũ.\n"
            "2. Kích hoạt truy xuất dữ liệu ngoài (Real-time Tool Retrieval): Gọi công cụ tìm kiếm web (Web Search tool) hoặc cơ sở dữ liệu doanh nghiệp chính thức "
            "với truy vấn có chứa mốc thời gian hiện tại để lấy thông cáo báo chí, hồ sơ quản trị mới nhất của công ty X.\n"
            "3. Phản hồi kèm mốc thời gian và trích dẫn nguồn (Time-grounded Response with Citation): Tổng hợp câu trả lời nêu rõ: 'Tính đến ngày DD/MM/YYYY theo nguồn [Tên cơ quan/báo chí], "
            "CEO hiện tại của công ty X là Ông/Bà Y', kèm đường dẫn nguồn để người dùng đối chiếu."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc Grounding & Temporal Anchoring đòi hỏi LLM phải nhận thức được ranh giới tri thức đóng (parametric knowledge cutoff). "
            "Đối với thông tin thời gian thực, câu trả lời bắt buộc phải được neo vào bằng chứng truy xuất động và công khai ngày tháng kiểm chứng để ngăn ngừa rủi ro thông tin lỗi thời."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Bước nhận diện ranh giới tri thức (1.0 điểm): Nhận diện câu hỏi vượt cutoff và từ chối suy đoán chủ quan.\n"
            "- Bước truy xuất công cụ thời gian thực (1.0 điểm): Nêu rõ việc gọi tool search/API để lấy dữ liệu mới nhất.\n"
            "- Bước phản hồi có neo thời gian và nguồn (1.0 điểm): Trình bày câu trả lời kèm mốc thời gian cụ thể và dẫn nguồn đối chiếu minh bạch."
        ),
        "reference_source": "OpenAI Documentation - Retrieval and Web Browsing Best Practices (https://platform.openai.com/docs/guides/prompt-engineering); Google Search Grounding for Gemini API."
    }

    # 10. d01-q039 (3 pts)
    data["d01-q039"] = {
        "sample_answer": (
            "- Hai chỗ kết luận vượt quá bằng chứng:\n"
            "1. Phóng đại chỉ số và mức tác động: Nguồn A chỉ ghi 'thời gian hoàn thành trung vị giảm 8%', nhưng LLM bịa ra kết luận 'tăng năng suất 30%'.\n"
            "2. Khái quát hóa quá mức phạm vi đối tượng: Nguồn A chỉ thử nghiệm trên cỡ mẫu nhỏ gồm '40 người', nhưng LLM lại khẳng định tuyệt đối cho 'mọi nhóm người dùng'.\n\n"
            "- Viết lại nhận định phù hợp với nguồn:\n"
            "\"Theo nghiên cứu thử nghiệm trên nhóm 40 người tham gia, kết quả ghi nhận thời gian hoàn thành công việc trung vị giảm 8%.\""
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Đây là hai dạng ảo giác suy diễn kinh điển trong LLM: Phóng đại số liệu (metric extrapolation hallucination) "
            "và Khái quát hóa sai phạm vi (scope overgeneralization). Trong thiết kế AI sản phẩm, mọi khẳng định định lượng phải tuân thủ nghiêm ngặt "
            "nguyên tắc trung thực với ngữ cảnh (Faithfulness/Factuality to Context)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chỉ ra 2 lỗi vượt quá bằng chứng (1.5 điểm): Nêu đúng sai lệch về chỉ số (8% giảm thời gian vs 30% năng suất) và phóng đại phạm vi (40 người vs mọi người dùng).\n"
            "- Viết lại nhận định trung thực (1.5 điểm): Viết lại câu chuẩn xác, giữ nguyên cỡ mẫu 40 người và số liệu giảm thời gian trung vị 8%."
        ),
        "reference_source": "Ji, Z., et al. (2023). Survey of Hallucination in Natural Language Generation. ACM Computing Surveys, 55(12), 1-38. https://arxiv.org/abs/2202.03629; Ragas Evaluation Metric - Faithfulness."
    }

    # 11. d01-q041 (3 pts)
    data["d01-q041"] = {
        "sample_answer": (
            "- Câu trả lời không âm thầm chọn một con số:\n"
            "\"Hiện có sự không nhất quán giữa hai tài liệu được cung cấp: Tài liệu chính thức ghi nhận giới hạn là 100 yêu cầu/phút, "
            "trong khi tài liệu SDK (phiên bản cũ) ghi nhận mức 60 yêu cầu/phút. Do sự khác biệt về nguồn và phiên bản tài liệu, hệ thống không tự ý áp dụng một con số duy nhất.\"\n\n"
            "- Bước tiếp theo cần thực hiện:\n"
            "Tiến hành kiểm tra số hiệu phiên bản của SDK hiện hành đang chạy trong dự án; thực hiện gọi thử nghiệm API (probe request) "
            "hoặc liên hệ đội ngũ quản trị dịch vụ/kênh hỗ trợ chính thức để xác nhận ngưỡng rate limit có hiệu lực thực tế cho môi trường hiện tại."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc xử lý xung đột thông tin (Conflict Transparency Principle) quy định hệ thống AI không được phép "
            "tự ý đưa ra giả định ngầm định khi dữ liệu đầu vào mâu thuẫn. Việc chỉ ra sự khác biệt và hướng dẫn quy trình xác minh phiên bản giúp bảo vệ hệ thống "
            "khỏi các lỗi giới hạn tải nghiêm trọng khi vận hành thực tế."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Trình bày câu trả lời minh bạch mâu thuẫn (1.5 điểm): Nêu rõ cả hai số liệu (100 và 60 req/min) từ hai tài liệu mà không tự ý thiên vị một số.\n"
            "- Đề xuất bước xác minh kỹ thuật tiếp theo (1.5 điểm): Đưa ra hành động cụ thể như đối chiếu phiên bản SDK, kiểm tra thực nghiệm hoặc hỏi quản trị viên."
        ),
        "reference_source": "Google SRE Book - Addressing Discrepancies and Failure Handling (https://sre.google/sre-book/); AWS Well-Architected Framework - Reliability Pillar."
    }

    # 12. d01-q043 (3 pts)
    data["d01-q043"] = {
        "sample_answer": (
            "1. Phần trong cơ chế `context + attention` có thể dùng chung: Sau khi qua các bộ chiếu (projector/linear projection), các biểu diễn của văn bản "
            "và hình ảnh đều được chuyển đổi thành các chuỗi vector liên tục có cùng số chiều không gian ẩn ($d_{model}$). Do đó, các tầng Transformer Backbone "
            "(cơ chế Self-Attention đa đầu, Feed-Forward Network, Residual Connection và LayerNorm) hoàn toàn có thể dùng chung để tính toán ma trận tương tác giữa token chữ và token ảnh.\n"
            "2. Phần không nên coi là giống hệt giữa hai loại dữ liệu: Khâu mã hóa và bản chất cấu trúc ban đầu. Văn bản là chuỗi token 1 chiều rời rạc có tính ngữ nghĩa tuần tự (1D sequence via BPE). "
            "Ngược lại, biểu đồ là dữ liệu không gian 2D liên tục (2D image patches) chứa cấu trúc hình học, tọa độ, màu sắc và mật độ pixel được trích xuất qua Vision Encoder (ViT), "
            "đòi hỏi cơ chế positional encoding 2 chiều và các phép chiếu đặc trưng riêng biệt."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Kiến trúc đa phương thức (Multimodal Transformer như CLIP, LLaVA, GPT-4V) áp dụng nguyên lý 'Unified Representation': "
            "tách biệt khâu xử lý thô riêng biệt theo phương thức (Modality-specific encoder) và hợp nhất ở tầng Transformer biểu diễn chung (Unified Attention Space). "
            "Đồng nhất hóa quá sớm bản chất dữ liệu sẽ phá vỡ tính toàn vẹn về không gian 2D của biểu đồ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nêu phần dùng chung của context + attention (1.5 điểm): Chỉ ra không gian embedding chung và các khối Transformer self-attention sau khi qua projector.\n"
            "- Nêu phần khác biệt bản chất (1.5 điểm): Phân biệt rõ tính tuần tự 1D của văn bản rời rạc với cấu trúc không gian 2D liên tục của patch ảnh biểu đồ."
        ),
        "reference_source": "Radford, A., et al. (2021). Learning Transferable Visual Models From Natural Language Supervision (CLIP). ICML 2021. https://arxiv.org/abs/2103.00020; Liu, H., et al. (2023). Visual Instruction Tuning (LLaVA)."
    }

    # 13. d01-q046 (3 pts)
    data["d01-q046"] = {
        "sample_answer": (
            "- Kết luận ĐƯỢC hỗ trợ: Trạng thái ẩn (`hidden state`) của mô hình CÓ CHỨA tương quan thông tin (statistical correlation / linear decodability) "
            "về biến Z với độ chính xác cao. Điều này chứng minh quá trình xử lý nội tại của mô hình đã trích xuất và mã hóa biểu diễn của biến Z.\n"
            "- Kết luận CHƯA ĐƯỢC hỗ trợ: Biến Z đóng vai trò nhân quả (causal mechanism / causally efficacious) trong việc tạo ra kết quả đầu ra của mô hình. "
            "Việc can thiệp (ablation/intervention) vào hướng biểu diễn của Z mà không làm thay đổi đầu ra cho thấy biểu diễn Z có thể chỉ là một biến phụ ngẫu nhiên "
            "(epiphenomenon) hoặc thông tin dư thừa mà các tầng tính toán phía sau không hề sử dụng để đưa ra quyết định."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Thí nghiệm Probing trong diễn giải mô hình (Mechanistic Interpretability) chỉ chứng minh sự tồn tại của thông tin "
            "(Correlation is not Causation). Để chứng minh một khái niệm trong mạng nơ-ron thực sự quyết định hành vi đầu ra, bắt buộc phải có thử nghiệm can thiệp "
            "(Interchange Intervention / Causal Mediation Analysis) cho thấy sự thay đổi tương ứng ở output."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Kết luận được hỗ trợ (1.5 điểm): Nêu rõ mô hình có mã hóa thông tin/tương quan về biến Z trong trạng thái ẩn.\n"
            "- Kết luận chưa được hỗ trợ (1.5 điểm): Giải thích rõ biến Z không có vai trò nhân quả (causality) vì can thiệp không làm thay đổi đầu ra (chỉ là tương quan bề mặt)."
        ),
        "reference_source": "Belinkov, Y. (2022). Probing Classifiers: Promises, Shortcomings, and Alternatives. Computational Linguistics, 48(1), 207-219. https://arxiv.org/abs/2102.12492; Geiger, A., et al. (2021). Causal Abstractions of Neural Networks."
    }

    # 14. d01-q048 (3 pts)
    data["d01-q048"] = {
        "sample_answer": (
            "- Thông tin mỗi token VẪN CÓ: Bản sắc ngữ nghĩa từ vựng độc lập (lexical/semantic identity). Mỗi token vẫn giữ nguyên vector embedding từ vựng "
            "được tra cứu từ bảng từ điển (embedding lookup table), đại diện cho ý nghĩa trừu tượng cô lập của chính từ/ký tự đó trong không gian đặc trưng.\n"
            "- Thông tin BỊ THIẾU: Toàn bộ thông tin về vị trí tuyệt đối (absolute position), thứ tự tương đối trước sau (relative order), cũng như cấu trúc ngữ pháp "
            "tuần tự trong câu. Cơ chế Self-Attention nguyên bản là phép toán bất biến với phép hoán vị (permutation-invariant); nếu không có Positional Encoding, "
            "Transformer sẽ biến thành mô hình túi từ (Bag-of-Words) và không thể phân biệt được chủ ngữ, tân ngữ hay quan hệ bổ nghĩa khi đảo trật tự từ."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Kiến trúc Transformer xử lý các phần tử đầu vào song song đồng thời (parallel processing), khác với RNN duyệt tuần tự. "
            "Do tính chất toán học của tích vô hướng ma trận Attention là hoán vị bất biến ($Attention(P X) = P Attention(X)$), tín hiệu vị trí (Positional Encoding / RoPE) "
            "là thành phần sống còn để mô hình nắm bắt cú pháp tuần tự của ngôn ngữ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Thông tin còn giữ lại (1.5 điểm): Nêu rõ token vẫn giữ thông tin bản sắc ngữ nghĩa từ điển độc lập (lexical embedding).\n"
            "- Thông tin bị mất đi (1.5 điểm): Nêu rõ mất hoàn toàn thông tin thứ tự trước sau, vị trí và cấu trúc tuần tự do tính chất hoán vị bất biến của attention."
        ),
        "reference_source": "Vaswani, A., et al. (2017). Attention Is All You Need. NeurIPS 2017. https://arxiv.org/abs/1706.03762; Su, J., et al. (2024). RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)."
    }

    # 15. d01-q053 (3 pts)
    data["d01-q053"] = {
        "sample_answer": (
            "Trong câu 'Lan đặt chiếc cốc lên bàn vì nó dễ vỡ', vai trò của Q, K, V khi token 'nó' thực hiện self-attention:\n"
            "- Query (Q) của 'nó': Đóng vai trò là câu hỏi hoặc yêu cầu tìm kiếm thông tin do chính 'nó' phát đi (Ví dụ: 'Tôi là đại từ thay thế, đối tượng nào đứng trước tôi có đặc tính tương thích với vị ngữ 'dễ vỡ'?').\n"
            "- Key (K) của các token đứng trước ('Lan', 'chiếc cốc', 'bàn'): Đóng vai trò là nhãn nhận diện hoặc hồ sơ thuộc tính để so khớp. Tích vô hướng giữa $Q_{nó}$ và $K_{chiếc\\_cốc}$ sẽ cho điểm tương đồng cao nhất vì đặc tính vật lý 'dễ vỡ' phù hợp với 'chiếc cốc' hơn là 'Lan' hay 'bàn'.\n"
            "- Value (V) của các token: Chứa đựng nội dung thông tin biểu diễn ngữ nghĩa thực sự của đối tượng. Khi trọng số chú ý softmax giữa $Q_{nó}$ và $K_{chiếc\\_cốc}$ đạt mức cao nhất, vector $V_{chiếc\\_cốc}$ sẽ được truyền tải và hòa trộn vào vector biểu diễn trạng thái mới của token 'nó'."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Cơ chế Scaled Dot-Product Attention hoạt động tương tự như một hệ thống truy vấn cơ sở dữ liệu mềm (soft database lookup): "
            "Query truy vấn qua các Key để tính trọng số tương đồng (Softmax Attention Weight), sau đó tính tổng có trọng số trên các Value để tổng hợp thông tin ngữ cảnh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Vai trò của Query (1.0 điểm): Mô tả đúng Q là nhu cầu truy vấn tìm kiếm thực thể tham chiếu phù hợp với ngữ cảnh 'dễ vỡ'.\n"
            "- Vai trò của Key (1.0 điểm): Mô tả đúng K là nhãn thuộc tính của các từ đứng trước để so khớp tương đồng qua tích vô hướng.\n"
            "- Vai trò của Value (1.0 điểm): Mô tả đúng V là nội dung ngữ nghĩa thực tế được trích xuất và hòa trộn vào biểu diễn mới của 'nó'."
        ),
        "reference_source": "Vaswani, A., et al. (2017). Attention Is All You Need. Section 3.2. https://arxiv.org/abs/1706.03762; Alammar, J. (2018). The Illustrated Transformer."
    }

    # 16. d01-q054 (3 pts)
    data["d01-q054"] = {
        "sample_answer": (
            "Thực hiện các bước tính toán Scaled Dot-Product Attention:\n"
            "1. Tính tích vô hướng và chia tỷ lệ ($d_k = 2 \\Rightarrow \\sqrt{d_k} = \\sqrt{2}$):\n"
            "- $Q \\cdot K_1 = [1, 0] \\cdot [\\sqrt{2}, 0] = 1 \\times \\sqrt{2} + 0 \\times 0 = \\sqrt{2}$.\n"
            "  Điểm sau chia tỷ lệ $S_1 = \\frac{Q \\cdot K_1}{\\sqrt{d_k}} = \\frac{\\sqrt{2}}{\\sqrt{2}} = 1.000$.\n"
            "- $Q \\cdot K_2 = [1, 0] \\cdot [0, 0] = 1 \\times 0 + 0 \\times 0 = 0$.\n"
            "  Điểm sau chia tỷ lệ $S_2 = \\frac{Q \\cdot K_2}{\\sqrt{d_k}} = \\frac{0}{\\sqrt{2}} = 0.000$.\n\n"
            "2. Tính trọng số Softmax:\n"
            "- $e^{S_1} = e^{1} \\approx 2.71828$; $e^{S_2} = e^{0} = 1.00000$. Tổng = $2.71828 + 1.00000 = 3.71828$.\n"
            "- $w_1 = \\frac{2.71828}{3.71828} \\approx 0.731$.\n"
            "- $w_2 = \\frac{1.00000}{3.71828} \\approx 0.269$.\n\n"
            "3. Tính đầu ra Attention ($w_1 V_1 + w_2 V_2$):\n"
            "- $Output = 0.731 \\times [1, 0] + 0.269 \\times [0, 1] = [0.731, 0] + [0, 0.269] = [0.731, 0.269]$."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Công thức chuẩn $Attention(Q, K, V) = \\text{softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$. "
            "Việc chia cho $\\sqrt{d_k}$ giữ phương sai của tích vô hướng ở mức 1, ngăn chặn giá trị quá lớn đẩy softmax vào vùng gradient bão hòa (vanishing gradient)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Điểm sau chia tỷ lệ (1.0 điểm): Tính chính xác $S_1 = 1.000$ và $S_2 = 0.000$.\n"
            "- Trọng số softmax (1.0 điểm): Tính chính xác $w_1 \\approx 0.731$ và $w_2 \\approx 0.269$.\n"
            "- Vector đầu ra attention (1.0 điểm): Tính chính xác vector đầu ra $[0.731, 0.269]$."
        ),
        "reference_source": "Vaswani, A., et al. (2017). Attention Is All You Need. Section 3.2.1. https://arxiv.org/abs/1706.03762"
    }

    # 17. d01-q055 (3 pts)
    data["d01-q055"] = {
        "sample_answer": (
            "Thực hiện các bước tính toán Scaled Dot-Product Attention:\n"
            "1. Tính tích vô hướng và chia tỷ lệ ($d_k = 4 \\Rightarrow \\sqrt{d_k} = \\sqrt{4} = 2$):\n"
            "- $Q \\cdot K_1 = [1, 1] \\cdot [2, 0] = 1 \\times 2 + 1 \\times 0 = 2$.\n"
            "  Điểm sau chia tỷ lệ $S_1 = \\frac{Q \\cdot K_1}{2} = \\frac{2}{2} = 1.000$.\n"
            "- $Q \\cdot K_2 = [1, 1] \\cdot [0, 1] = 1 \\times 0 + 1 \\times 1 = 1$.\n"
            "  Điểm sau chia tỷ lệ $S_2 = \\frac{Q \\cdot K_2}{2} = \\frac{1}{2} = 0.500$.\n\n"
            "2. Tính trọng số Softmax:\n"
            "- $e^{S_1} = e^{1} \\approx 2.71828$; $e^{S_2} = e^{0.5} \\approx 1.64872$. Tổng = $2.71828 + 1.64872 = 4.36700$.\n"
            "- $w_1 = \\frac{2.71828}{4.36700} \\approx 0.622$.\n"
            "- $w_2 = \\frac{1.64872}{4.36700} \\approx 0.378$.\n\n"
            "3. Tính đầu ra Attention ($w_1 V_1 + w_2 V_2$):\n"
            "- $Output = 0.62246 \\times [2, 0] + 0.37754 \\times [0, 3] = [1.245, 0] + [0, 1.133] = [1.245, 1.133]$."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Với $d_k=4$, hệ số chuẩn hóa $\\sqrt{d_k}=2$. Đầu ra là tổ hợp lồi (convex combination) "
            "của các vector Value theo phân phối xác suất sinh ra bởi softmax, định hình chính xác không gian đặc trưng tổng hợp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Điểm sau chia tỷ lệ (1.0 điểm): Tính đúng $S_1 = 1.000$ và $S_2 = 0.500$ (với $\\sqrt{d_k}=2$).\n"
            "- Trọng số softmax (1.0 điểm): Tính đúng $w_1 \\approx 0.622$ và $w_2 \\approx 0.378$.\n"
            "- Vector đầu ra attention (1.0 điểm): Tính đúng vector đầu ra $[1.245, 1.133]$ (làm tròn 3 chữ số)."
        ),
        "reference_source": "Vaswani, A., et al. (2017). Attention Is All You Need. Section 3.2.1. https://arxiv.org/abs/1706.03762"
    }

    # 18. d01-q057 (3 pts)
    data["d01-q057"] = {
        "sample_answer": (
            "- Quan hệ mạnh nhất: Quan hệ liên kết mạnh nhất là giữa đại từ 'cô ấy' và thực thể 'Mai' với trọng số chú ý áp đảo đạt 0,70 (chiếm 70% tổng phân phối attention của head này so với 0,20 tới Lan và 0,10 tới dấu chấm).\n"
            "- Một giới hạn của kết luận từ map này: Trọng số attention chỉ phản ánh sự kết hợp tuyến tính trung gian tại một head ở một tầng cụ thể, KHÔNG PHẢI là bằng chứng giải thích quan hệ nhân quả (Attention is not explanation). Ta không thể kết luận chắc chắn rằng toàn bộ mô hình thực sự quyết định 'cô ấy' chính là 'Mai' ở đầu ra cuối cùng, vì các phép biến đổi phi tuyến tính qua MLP/FFN, các head khác và các tầng sâu hơn có thể điều chỉnh hoặc ghi đè thông tin này."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Luận điểm 'Attention is not Explanation' trong cộng đồng NLP chỉ ra rằng biểu đồ nhiệt attention map "
            "không đồng nhất với cơ chế giải thích nhân quả đáng tin cậy. Các head khác nhau có thể tập trung vào dấu câu hoặc cú pháp ngẫu nhiên "
            "mà không trực tiếp định đoạt dự đoán của token tiếp theo."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xác định quan hệ mạnh nhất (1.5 điểm): Nêu đúng quan hệ giữa 'cô ấy' và 'Mai' với trọng số cao nhất 0,70.\n"
            "- Nêu giới hạn diễn giải bản chất (1.5 điểm): Giải thích rõ attention weight không tương đương với giải thích nhân quả (không phản ánh toàn bộ quyết định của mạng nơ-ron qua các tầng sau)."
        ),
        "reference_source": "Jain, S., & Wallace, B. C. (2019). Attention is not Explanation. NAACL 2019. https://arxiv.org/abs/1902.10186; Wiegreffe, S., & Pinter, Y. (2019). Attention is not not Explanation. EMNLP 2019."
    }

    # 19. d01-q062 (3 pts)
    data["d01-q062"] = {
        "sample_answer": (
            "- Sửa phát biểu sai: Phát biểu trên không chính xác. '8 heads' (8 đầu chú ý) trong Multi-Head Attention đại diện cho 8 không gian con "
            "(subspaces) hoạt động SONG SONG (in parallel) cùng một lúc bên trong MỘT layer duy nhất, chứ không phải là 8 layers xử lý nối tiếp theo chiều sâu.\n"
            "- Mục đích của 8 heads: Cho phép mô hình đồng thời chú ý (jointly attend) đến các khía cạnh thông tin khác nhau ở các vị trí khác nhau trong cùng một thời điểm. "
            "Ví dụ: một head chuyên theo dõi quan hệ cú pháp chủ-vị, một head theo dõi thực thể, một head theo dõi dấu câu hoặc liên kết ngữ nghĩa cự ly dài. "
            "Sau đó kết quả của 8 heads được ghép nối (concatenate) và nhân qua ma trận chiếu $W^O$ để tạo ra biểu diễn phong phú, đa chiều."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tương tự như việc sử dụng nhiều bộ lọc (multiple feature maps/kernels) trong mạng tích chập CNN, "
            "Multi-Head Attention chiếu Q, K, V thành $h$ không gian con có số chiều thấp hơn ($d_k = d_{model} / h$) để học các mối quan hệ đa dạng "
            "mà không làm tăng tổng chi phí tính toán."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Sửa phát biểu chính xác (1.5 điểm): Khẳng định 8 heads hoạt động song song trong 1 layer chứ không phải 8 layers nối tiếp.\n"
            "- Nêu rõ mục đích kỹ thuật (1.5 điểm): Giải thích việc cho phép mô hình đồng thời nắm bắt nhiều khía cạnh ngữ nghĩa/cú pháp khác nhau trong các không gian con."
        ),
        "reference_source": "Vaswani, A., et al. (2017). Attention Is All You Need. Section 3.2.2 Multi-Head Attention. https://arxiv.org/abs/1706.03762"
    }

    # 20. d01-q068 (3 pts)
    data["d01-q068"] = {
        "sample_answer": (
            "So sánh luồng thông tin và đường dẫn thông tin nguồn vào token đích mới:\n"
            "1. Kiến trúc Encoder–Decoder (ví dụ: T5, BART):\n"
            "- Luồng thông tin: Văn bản nguồn được xử lý trọn vẹn và hai chiều (bidirectional) bởi khối Encoder để tạo ra ma trận biểu diễn ngữ cảnh nguồn (memory).\n"
            "- Đường vào token đích: Thông tin nguồn đi vào token đích mới thông qua các tầng Cross-Attention (Encoder-Decoder Attention) nằm xen kẽ giữa Masked Self-Attention "
            "và FFN trong Decoder. Tại đây, Query đến từ Decoder và Key, Value đến từ đầu ra của Encoder.\n\n"
            "2. Kiến trúc Decoder-only (ví dụ: GPT-4, Llama):\n"
            "- Luồng thông tin: Không có khối Encoder và Cross-Attention riêng biệt. Cả chuỗi nguồn (prompt) và chuỗi đích (completion) được nối chung thành một chuỗi duy nhất.\n"
            "- Đường vào token đích: Thông tin nguồn đi vào token đích mới trực tiếp thông qua cơ chế Masked Causal Self-Attention. Token đích mới có thể nhìn ngược lại "
            "tất cả các token nguồn đứng trước nó theo ma trận tam giác nhân quả."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Sự khác biệt kiến trúc giữa Encoder-Decoder và Decoder-only phản ánh sự đánh đổi giữa hiệu quả biểu diễn hai chiều "
            "(bidirectional context trong translation) và sự tinh gọn, tối ưu bộ nhớ KV cache khi mở rộng quy mô sinh tự hồi quy (autoregressive scaling)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Luồng thông tin Encoder-Decoder (1.5 điểm): Nêu rõ thông tin nguồn đi qua khối Encoder và đi vào Decoder qua tầng Cross-Attention riêng biệt.\n"
            "- Luồng thông tin Decoder-only (1.5 điểm): Nêu rõ nguồn và đích nối chung trong một chuỗi, thông tin đi vào token mới qua Masked Causal Self-Attention."
        ),
        "reference_source": "Raffel, C., et al. (2020). Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer. JMLR. https://arxiv.org/abs/1910.10683; Brown, T., et al. (2020). Language Models are Few-Shot Learners."
    }

    # 21. d01-q071 (3 pts)
    data["d01-q071"] = {
        "sample_answer": (
            "1. Phân loại giai đoạn huấn luyện: Đây là giai đoạn Căn chỉnh chỉ dẫn có giám sát (Supervised Fine-Tuning - SFT / Instruction Tuning).\n"
            "2. Vì sao đây chưa phải là căn chỉnh theo ưu tiên (Preference Alignment):\n"
            "- Bản chất của căn chỉnh theo ưu tiên (như RLHF, DPO, KTO) đòi hỏi dữ liệu phản ánh sự so sánh sở thích (pairwise preference data) gồm các cặp câu trả lời "
            "`[chosen, rejected]` đối với cùng một prompt, kèm mô hình phần thưởng (Reward Model) hoặc hàm mất mát tối ưu hóa preference.\n"
            "- Trong bối cảnh này, tập dữ liệu chỉ bao gồm các mẫu trình diễn chuẩn mực đơn lẻ (demonstration pairs) từ giảng viên mà không có nhãn chỉ ra câu trả lời nào bị từ chối "
            "hay xếp hạng ưu tiên. Quá trình huấn luyện chỉ đơn thuần là tối đa hóa xác suất hợp lý cực đại (cross-entropy next-token loss) chứ chưa hề có cơ chế phạt câu trả lời kém."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Quy trình huấn luyện LLM tiêu chuẩn bao gồm 3 pha: Pre-training (học tự giám sát không nhãn) -> "
            "SFT (học làm theo chỉ dẫn từ dữ liệu mẫu chuẩn) -> Preference Alignment (RLHF/DPO để học theo sở thích và chuẩn mực an toàn của con người). "
            "SFT dạy mô hình 'cách hành xử theo khuôn mẫu', trong khi Preference Alignment dạy mô hình 'cách chọn phương án tối ưu khi có nhiều câu trả lời hợp lệ'."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân loại đúng giai đoạn (1.5 điểm): Xác định chính xác đây là Supervised Fine-Tuning (SFT / Instruction Tuning).\n"
            "- Giải thích vì sao chưa phải căn chỉnh ưu tiên (1.5 điểm): Nêu rõ thiếu dữ liệu so sánh sở thích (chosen vs rejected) và không sử dụng cơ chế reward/DPO để phạt phản hồi kém."
        ),
        "reference_source": "Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. NeurIPS 2022. https://arxiv.org/abs/2203.02155; Rafailov, R., et al. (2024). Direct Preference Optimization (DPO)."
    }

    # 22. d01-q077 (3 pts)
    data["d01-q077"] = {
        "sample_answer": (
            "- Phần có thể được hỗ trợ: Nhận định đúng ở chỗ RLHF (Reinforcement Learning from Human Feedback) làm giảm đáng kể xác suất và tần suất sinh ra "
            "các nội dung độc hại, thiên kiến, hoặc nguy hiểm trong các bài kiểm thử tiêu chuẩn và tương tác hội thoại thông thường thông qua việc học phạt các phản hồi vi phạm.\n"
            "- Vì sao kết luận tuyệt đối ('không thể tạo ra đầu ra nguy hiểm') là KHÔNG HỢP LỆ:\n"
            "1. Bản chất mô hình xác suất: LLM là mô hình xác suất sinh (probabilistic generative model), không gian đầu vào mở vô hạn nên luôn tồn tại xác suất khác không sinh ra nội dung nguy hại.\n"
            "2. Điểm yếu trước tấn công đối kháng: RLHF chỉ căn chỉnh bề mặt phân phối (surface-level alignment). Mô hình vẫn dễ dàng bị bẻ khóa (jailbreak) thông qua "
            "prompt injection, kỹ thuật nhập vai đối kháng (adversarial roleplay, DAN), hoặc mã hóa đối kháng (Base64, đa ngôn ngữ ít phổ biến), khiến cơ chế phòng thủ bị vô hiệu hóa."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Định lý an toàn AI chỉ ra rằng việc căn chỉnh trọng số (post-training alignment) chỉ làm giảm rủi ro chứ không thể "
            "mang lại sự đảm bảo an toàn tuyệt đối mang tính hình thức (formal verification). Một hệ thống AI production bắt buộc phải triển khai mô hình phòng thủ theo chiều sâu "
            "(Defense-in-Depth) với các bộ lọc Input/Output Guardrails độc lập."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Đánh giá phần được hỗ trợ (1.0 điểm): Thừa nhận RLHF giúp giảm thiểu tần suất vi phạm an toàn trong điều kiện thông thường.\n"
            "- Phân tích vì sao kết luận tuyệt đối không hợp lệ (2.0 điểm): Chỉ ra bản chất mô hình xác suất và nguy cơ bị jailbreak/prompt injection phá vỡ lớp vỏ an toàn bề mặt."
        ),
        "reference_source": "Wei, A., et al. (2024). Jailbroken: How Does LLM Safety Training Fail? NeurIPS 2023. https://arxiv.org/abs/2307.02483; OWASP Top 10 for Large Language Model Applications - LLM01: Prompt Injection."
    }

    # 23. d01-q081 (3 pts)
    data["d01-q081"] = {
        "sample_answer": (
            "- Phân loại trục cải tiến: Trục cải tiến tính toán tại thời điểm suy luận (Inference-Time Compute Scaling / Test-Time Compute / Best-of-N Sampling).\n"
            "- Bằng chứng quyết định: Hệ thống giữ nguyên hoàn toàn checkpoint và trọng số của mô hình (không hề có quá trình cập nhật gradient, fine-tuning hay "
            "huấn luyện thêm trước khi triển khai). Toàn bộ chi phí tính toán tăng thêm được dồn vào runtime cho từng truy vấn cụ thể: sinh song song 8 phương án ứng viên "
            "và dùng bộ kiểm chứng (Verifier/Reward Model) để chọn ra phương án có độ tin cậy cao nhất."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mở rộng khả năng của hệ thống AI hiện nay có hai trục: Trục huấn luyện (Pretraining / Post-training compute) "
            "và Trục suy luận (Inference-time compute scaling). Việc tăng tính toán suy luận (System 2 thinking / Re-ranking / Verification) cho phép "
            "đạt độ chính xác vượt bậc trên các bài toán lập luận logic phức tạp mà không cần tái huấn luyện mô hình nền tảng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân loại đúng trục cải tiến (1.5 điểm): Xác định chính xác Inference-time compute (Test-time compute scaling / Best-of-N sampling).\n"
            "- Chỉ ra bằng chứng quyết định (1.5 điểm): Nêu rõ checkpoint mô hình được giữ nguyên và tài nguyên tính toán bổ sung hoàn toàn diễn ra tại runtime trên từng truy vấn."
        ),
        "reference_source": "Brown, B., et al. (2024). Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. arXiv:2407.21787. https://arxiv.org/abs/2407.21787; Snell, C., et al. (2024). Scaling LLM Test-Time Compute Optimally."
    }

    # 24. d01-q086 (3 pts)
    data["d01-q086"] = {
        "sample_answer": (
            "- Số token đầu vào được hạch toán: 2.000 token × 100 request = 200.000 token đầu vào.\n"
            "- Vì sao không phải chỉ 2.000 token: Các giao thức API LLM thương mại hoạt động theo nguyên lý phi trạng thái (stateless HTTP requests). "
            "Mỗi request là một phiên xử lý độc lập hoàn toàn; server LLM phải đọc và chạy qua giai đoạn prefill (tính toán biểu diễn ma trận KV cache) "
            "cho toàn bộ 2.000 token của system prompt trong từng request đó. Do đó, nhà cung cấp dịch vụ hạch toán chi phí đầu vào tích lũy tuyến tính "
            "cho mỗi lượt gọi: 2.000 × 100 = 200.000 token (trừ khi có tính năng Prompt Caching được áp dụng với biểu giá chiết khấu riêng)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Bản chất phi trạng thái của HTTP API buộc các hệ thống phân tán phải trả chi phí tính toán lặp lại "
            "trên các tiền tố prompt tĩnh dài. Trong kiến trúc hiện đại, giải pháp tối ưu chi phí là kích hoạt Prompt Caching (Prefix Caching) "
            "tại gateway để tái sử dụng KV cache giữa các request có cùng tiền tố."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Tính đúng số token hạch toán (1.5 điểm): Tính chính xác 200.000 token đầu vào (2.000 × 100).\n"
            "- Giải thích bản chất hạch toán (1.5 điểm): Giải thích rõ API là stateless, mỗi request phải nạp và xử lý prefill lại toàn bộ system prompt từ đầu."
        ),
        "reference_source": "OpenAI API Pricing & Token Billing Model (https://openai.com/api/pricing/); Anthropic Claude Documentation - Prompt Caching Architecture."
    }

    # 25. d01-q091 (4 pts)
    data["d01-q091"] = {
        "sample_answer": (
            "1. Sửa đổi quy trình thử nghiệm tối thiểu có thể so sánh:\n"
            "- Chuẩn hóa tập prompt đầu vào: Sử dụng cùng một tập dữ liệu benchmark cố định, cùng nội dung và cùng một ngôn ngữ cho cả hai mô hình (loại bỏ prompt khác ngôn ngữ).\n"
            "- Đồng nhất tham số sinh: Cố định cùng một giá trị `temperature` (thường là 0.0 để đảm bảo tính tất định), cùng `top_p` và `max_tokens`.\n"
            "- Tăng số lần thử nghiệm lặp lại: Chạy lặp lại nhiều lần (ví dụ N = 10 đến 30 lượt trên mỗi prompt) để tính toán các giá trị thống kê (trung vị, trung bình, P95) thay vì chỉ chạy 1 lần duy nhất.\n"
            "- Đồng nhất ranh giới đo lường thời gian: Đo round-trip time thuần túy từ thời điểm gửi HTTP request đến khi nhận token cuối cùng, loại bỏ chi phí khởi tạo client ban đầu.\n\n"
            "2. Bốn biến kiểm soát hoặc trường thông tin cần lưu trữ trong nhật ký đánh giá:\n"
            "1) `prompt_hash`: Định danh duy nhất và nội dung chuẩn hóa của prompt đầu vào.\n"
            "2) `generation_params`: Bản ghi các tham số sinh (`temperature`, `top_p`, `seed`, `max_tokens`).\n"
            "3) `latency_breakdown`: Thời gian phản hồi phân rã (`time_to_first_token_ms`, `total_duration_ms`).\n"
            "4) `token_usage`: Số lượng token đầu vào và đầu ra thực tế (`prompt_tokens`, `completion_tokens`)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Thiết kế thí nghiệm so sánh đối chứng (A/B Testing / Benchmarking) đòi hỏi kiểm soát nghiêm ngặt "
            "nguyên tắc đơn biến (Single Variable Principle). Bất kỳ sự khác biệt nào về ngôn ngữ prompt, tham số ngẫu nhiên hay ranh giới đo lường "
            "đều tạo ra các biến gây nhiễu (confounding variables), làm vô hiệu hóa giá trị khoa học của kết quả so sánh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Sửa đổi quy trình thử nghiệm chuẩn hóa (2.0 điểm): Chuẩn hóa cùng tập prompt, cùng tham số temperature/sinh, chạy lặp lại nhiều lần và đồng nhất mốc đo độ trễ.\n"
            "- Nêu đủ 4 biến kiểm soát/trường thông tin (2.0 điểm): Liệt kê đủ 4 trường thiết yếu (prompt hash/text, tham số sinh, chỉ số latency chuẩn, token usage)."
        ),
        "reference_source": "Liang, P., et al. (2022). Holistic Evaluation of Language Models (HELM). Stanford CRFM. https://arxiv.org/abs/2211.09110; MLPerf Inference Benchmark Suite."
    }

    # 26. d01-q094 (3 pts)
    data["d01-q094"] = {
        "sample_answer": (
            "- Chế độ truy cập ưu tiên: Tự triển khai mô hình mã nguồn mở cục bộ trên hạ tầng nội bộ (On-premises / Self-hosted Open-Weight Models, "
            "chẳng hạn như Llama 3, Qwen 2.5 hoặc Mistral triển khai qua vLLM/TGI trên cụm máy chủ GPU của bệnh viện).\n"
            "- Đánh đổi chính (Trade-offs):\n"
            "1. Chi phí đầu tư và vận hành cao: Đòi hỏi chi phí vốn lớn (CapEx) cho phần cứng GPU chuyên dụng, điện năng, làm mát và đội ngũ kỹ sư chuyên trách "
            "để duy trì độ sẵn sàng, sao lưu và tối ưu throughput.\n"
            "2. Khoảng cách về năng lực mô hình: Các mô hình open-weights chạy cục bộ có thể đòi hỏi nhiều công sức fine-tuning chuyên ngành y khoa để đạt được độ chính xác "
            "tương đương với các mô hình thương mại đóng hàng đầu trên đám mây."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong lĩnh vực y tế (Healthcare), tính bảo mật dữ liệu bệnh nhân (tuân thủ tiêu chuẩn HIPAA, GDPR) "
            "và khả năng kiểm toán quá trình suy luận (auditability) là các ràng buộc cứng (Hard Constraints). Khi tổ chức có sẵn đội ngũ vận hành GPU, "
            "kiến trúc On-premises là lựa chọn tối ưu để loại bỏ hoàn toàn rủi ro rò rỉ dữ liệu qua mạng bên thứ ba."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn đúng chế độ truy cập (1.5 điểm): Xác định đúng giải pháp On-premises / Self-hosted mã nguồn mở trên cụm máy chủ bệnh viện.\n"
            "- Nêu rõ các đánh đổi kỹ thuật và chi phí (1.5 điểm): Phân tích chi phí phần cứng/vận hành hạ tầng cao và nỗ lực tối ưu năng lực mô hình so với cloud API."
        ),
        "reference_source": "HIPAA Security Rule & AI Deployment Guidance (https://www.hhs.gov/hipaa/); NIST AI Risk Management Framework (NIST AI 100-1)."
    }

    # 27. d01-q096 (3 pts)
    data["d01-q096"] = {
        "sample_answer": (
            "1. Phân biệt tổng số tham số và tham số hoạt động:\n"
            "- Tổng số tham số (`total parameters`): Là toàn bộ trọng số của mô hình được lưu trữ trong bộ nhớ VRAM của GPU (ví dụ Model D có 20B, Model M có 80B tham số).\n"
            "- Số tham số hoạt động (`active parameters`): Là lượng tham số thực tế tham gia vào các phép tính nhân ma trận (FLOPs) trong lượt tính toán (forward pass) "
            "cho một token đơn lẻ tại runtime (Model D kích hoạt toàn bộ 20B, trong khi Model M qua bộ định tuyến router chỉ kích hoạt 10B).\n\n"
            "2. Giải thích vì sao không thể kết luận M tốn lượng tính toán gấp 4:\n"
            "Khối lượng tính toán (FLOPs) và độ trễ sinh token tỷ lệ thuận trực tiếp với số tham số hoạt động (active parameters) trên mỗi token, chứ không phụ thuộc vào tổng tham số lưu trữ. "
            "Vì Model M chỉ kích hoạt 10B tham số hoạt động cho mỗi token, lượng tính toán thực tế của M chỉ bằng một nửa (1/2) so với Model D (kích hoạt 20B tham số hoạt động), "
            "mặc dù tổng dung lượng trọng số lưu trữ của M lớn gấp 4 lần D."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Kiến trúc Mixture of Experts (MoE) áp dụng nguyên lý tính toán thưa (Conditional Computation / Sparsity). "
            "Bằng cách chỉ kích hoạt một tập con các chuyên gia (experts) cho mỗi token, MoE đạt được sức chứa tri thức khổng lồ (tổng dung lượng tham số lớn) "
            "nhưng vẫn duy trì chi phí tính toán (FLOPs per token) tương đương với một mô hình dày (dense) cỡ nhỏ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân biệt total và active parameters (1.5 điểm): Định nghĩa chính xác tổng tham số lưu trữ trong VRAM so với tham số thực tế tính toán trên mỗi token.\n"
            "- Giải thích lượng tính toán thực tế (1.5 điểm): Chứng minh M kích hoạt 10B tham số nên FLOPs thực tế chỉ bằng 1/2 của D (20B), bác bỏ suy luận gấp 4 lần."
        ),
        "reference_source": "Shazeer, N., et al. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. ICLR 2017. https://arxiv.org/abs/1701.06538; Fedus, W., et al. (2022). Switch Transformers. JMLR."
    }

    # 28. d01-q098 (3 pts)
    data["d01-q098"] = {
        "sample_answer": (
            "- Quyết định chọn model: Chọn MODEL A.\n"
            "- Giải thích chi tiết theo thứ tự ưu tiên:\n"
            "1. Tiêu chí 1 (JSON hợp lệ) và Tiêu chí 2 (Đủ 4 trường) là các ràng buộc cứng bắt buộc (hard constraints / pass-fail criteria). "
            "Hệ thống yêu cầu đầu ra có cấu trúc để các dịch vụ downstream xử lý tự động; việc thiếu trường sẽ dẫn đến lỗi hệ thống (runtime schema validation crash).\n"
            "2. Model A đạt tuyệt đối 10/10 JSON hợp lệ và 10/10 đủ 4 trường (tỷ lệ thành công 100%). Ngược lại, Model B thất bại ở tiêu chí bắt buộc khi chỉ đạt 7/10 đủ trường "
            "(tỷ lệ lỗi lên tới 30%).\n"
            "3. Tiêu chí 3 (độ trễ) chỉ được xem xét sau khi các mô hình đã vượt qua toàn bộ các tiêu chí bắt buộc. Mặc dù Model B có thời gian trung vị nhanh hơn "
            "(1,1 giây so với 1,8 giây), sự vượt trội về tốc độ hoàn toàn vô nghĩa khi độ tin cậy của dữ liệu đầu ra không được bảo đảm."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc thiết kế hệ thống theo mức độ nghiêm ngặt (Lexicographic Optimization) quy định: "
            "Tính đúng đắn của dữ liệu (Data Integrity & Correctness) luôn luôn đứng trên Tốc độ (Latency). Không bao giờ được đánh đổi "
            "tỷ lệ lỗi định dạng cấu trúc 30% lấy 0,7 giây độ trễ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn đúng Model A (1.0 điểm): Lựa chọn chính xác Model A.\n"
            "- Phân tích vi phạm tiêu chí bắt buộc (1.0 điểm): Chỉ ra Model B vi phạm tiêu chí đủ 4 trường với tỷ lệ lỗi 30%, không thể triển khai production.\n"
            "- Giải thích thứ bậc ưu tiên độ trễ (1.0 điểm): Nêu rõ độ trễ chỉ được tối ưu hóa sau khi các tiêu chí hợp lệ cấu trúc đã đạt 100%."
        ),
        "reference_source": "Google SRE Book - Service Level Objectives and Error Budgets (https://sre.google/sre-book/service-level-objectives/); Martin Fowler - Structural Interface Contracts."
    }

    # 29. d01-q099 (3 pts)
    data["d01-q099"] = {
        "sample_answer": (
            "- Có nên tuyên bố model thắng không?: KHÔNG NÊN tuyên bố model nào chiến thắng ở thời điểm này. Cả hai mô hình đều có cùng điểm chất lượng (18/20), "
            "sự chênh lệch về độ trễ nằm trong khoảng phương sai sai số ngẫu nhiên (measurement noise), và biến số then chốt về chi phí vận hành vẫn chưa được thu thập.\n\n"
            "- Bước tiếp theo cần thực hiện:\n"
            "1. Thu thập và định lượng chỉ số chi phí: Đo lường chính xác lượng token tiêu thụ và chi phí API / VRAM tương ứng của từng mô hình trên mỗi request.\n"
            "2. Mở rộng kích thước mẫu và kiểm định thống kê: Tăng số lượng mẫu đánh giá và áp dụng kiểm định thống kê (ví dụ: t-test hoặc bootstrap confidence intervals) "
            "để xác định xem sự khác biệt giữa hai mô hình có ý nghĩa thống kê (statistical significance, $p < 0.05$) hay chỉ là ngẫu nhiên.\n"
            "3. Thử nghiệm trên các trường hợp biên (Stress / Edge cases): Đưa vào các prompt phức tạp, câu hỏi đa nghĩa để tìm ra điểm gãy của từng mô hình."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong đánh giá kỹ thuật (Empirical Evaluation), việc vội vàng đưa ra quyết định khi số liệu chưa đạt "
            "ý nghĩa thống kê và thiếu khía cạnh chi phí sẽ dẫn đến các quyết định kiến trúc sai lầm. Cần kiểm soát biến gây nhiễu và hoàn thiện bức tranh ROI toàn diện."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Khẳng định không tuyên bố thắng (1.0 điểm): Nêu rõ không thể chọn người thắng vì điểm bằng nhau và latency chênh lệch nằm trong biên độ nhiễu.\n"
            "- Bổ sung tiêu chí chi phí (1.0 điểm): Yêu cầu đo lường cụ thể chi phí token / tài nguyên phần cứng.\n"
            "- Đề xuất phương pháp thống kê và ca biên (1.0 điểm): Nêu bước tăng cỡ mẫu, kiểm định ý nghĩa thống kê và kiểm thử stress test."
        ),
        "reference_source": "Kohavi, R., et al. (2020). Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing. Cambridge University Press. https://exp-platform.com/; Stanford HELM (https://crfm.stanford.edu/helm/)"
    }

    # 30. d01-q101 (3 pts)
    data["d01-q101"] = {
        "sample_answer": (
            "1. Hai khoảng trống về hiệu lực (Validity Gaps):\n"
            "- Khoảng trống về ngôn ngữ và thể chế pháp lý: Benchmark tiếng Anh (như MMLU) đo lường khả năng xử lý ngữ pháp tiếng Anh và hệ thống pháp luật thông luật (Common Law), "
            "hoàn toàn không phản ánh được năng lực am hiểu văn phong hành chính, cấu trúc ngữ pháp phức tạp và hệ thống văn bản quy phạm pháp luật Dân luật (Civil Law) của Việt Nam.\n"
            "- Khoảng trống về hình thức tác vụ (Task Modality Mismatch): Câu hỏi trắc nghiệm (Multiple-Choice Questions) chỉ đo lường khả năng nhận diện xác suất trong tập lựa chọn đóng, "
            "trong khi chatbot pháp lý thực tế đòi hỏi sinh ngôn ngữ tự do, tư vấn đa lượt (multi-turn), tổng hợp ngữ cảnh và trích dẫn điều khoản chính xác.\n\n"
            "2. Bằng chứng cần bổ sung:\n"
            "Cần xây dựng bộ dữ liệu đánh giá miền pháp lý Việt Nam chuyên biệt (Vietnamese Legal Benchmark) gồm các câu hỏi tình huống thực tế, "
            "kèm sự thẩm định trực tiếp của các luật sư/chuyên gia pháp lý (Human-in-the-loop expert evaluation) về tính chính xác của trích dẫn và lập luận pháp lý."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Construct Validity' trong đo lường phần mềm chỉ ra rằng một chỉ số benchmark chỉ có giá trị "
            "khi nó đo lường đúng năng lực cần thiết trong môi trường tác nghiệp thực tế. Việc ngoại suy từ benchmark trắc nghiệm tổng quát sang "
            "ứng dụng chuyên ngành có rủi ro pháp lý cao là một sai lầm nghiêm trọng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nêu 2 khoảng trống hiệu lực (2.0 điểm): Chỉ ra đúng khoảng cách ngôn ngữ/pháp luật Việt Nam và sự lệch pha giữa trắc nghiệm đóng với tư vấn pháp lý mở.\n"
            "- Nêu bằng chứng cần bổ sung (1.0 điểm): Đề xuất xây dựng benchmark pháp lý tiếng Việt và đánh giá từ chuyên gia pháp luật độc lập."
        ),
        "reference_source": "Wang, A., et al. (2019). SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems. NeurIPS 2019. https://arxiv.org/abs/1905.00537; HELM Legal Benchmarking."
    }

    # 31. d01-q103 (3 pts)
    data["d01-q103"] = {
        "sample_answer": (
            "1. Vì sao nghi ngờ rò rỉ dữ liệu làm nhận định yếu đi:\n"
            "Hiện tượng rò rỉ dữ liệu (Data Contamination / Benchmark Leakage) xảy ra khi câu hỏi và đáp án của benchmark công khai bị thu thập vào tập dữ liệu tiền huấn luyện "
            "(pretraining corpus) của mô hình. Khi đó, điểm số gần như tuyệt đối chỉ phản ánh khả năng học vẹt và ghi nhớ nguyên văn (verbatim memorization/overfitting), "
            "chứ không hề chứng minh được năng lực suy luận tổng quát hóa (generalization) trên dữ liệu mới chưa từng thấy trong thực tế.\n\n"
            "2. Đề xuất cách kiểm tra bổ sung:\n"
            "- Tạo tập benchmark ẩn mới (private canary dataset / out-of-distribution eval) gồm các câu hỏi mới được soạn thảo độc quyền sau ngày mô hình cutoff.\n"
            "- Thực hiện biến đổi dữ liệu kiểm thử (perturbation testing): Giữ nguyên cấu trúc logic nhưng thay đổi tên thực thể, số liệu và cách diễn đạt trong các câu hỏi cũ "
            "để đo lường xem mô hình có thực sự suy luận hay chỉ dựa vào việc khớp mẫu từ vựng đã học thuộc."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Goodhart's Law: 'Khi một thước đo trở thành mục tiêu, nó không còn là một thước đo tốt nữa'. "
            "Hiện tượng Data Contamination làm xói mòn tính khách quan của các benchmark công khai, buộc các kỹ sư hệ thống phải thiết lập "
            "các bộ test nội bộ được bảo mật chặt chẽ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Giải thích tác động của rò rỉ dữ liệu (1.5 điểm): Nêu rõ hiện tượng data contamination dẫn đến học vẹt (memorization) thay vì năng lực tổng quát hóa thật sự.\n"
            "- Đề xuất phương pháp kiểm tra (1.5 điểm): Đưa ra giải pháp tạo tập benchmark ẩn mới (canary dataset) hoặc hoán đổi dữ liệu (perturbation testing)."
        ),
        "reference_source": "Jacovi, A., et al. (2023). Stop Uploading Test Data to the Internet: When Benchmarks Become Training Data. arXiv:2305.10160. https://arxiv.org/abs/2305.10160; OpenAI GPT-4 Technical Report."
    }

    # 32. d01-q106 (3 pts)
    data["d01-q106"] = {
        "sample_answer": (
            "Cấu hình tối thiểu chuẩn cho phát triển cục bộ:\n"
            "1. Key thật nằm ở đâu: Lưu trữ trong file môi trường bí mật tại máy cục bộ (file `.env` hoặc trong hệ thống quản lý Secret/Keychain của hệ điều hành), "
            "tuyệt đối không nhúng trực tiếp vào mã nguồn (hardcode).\n"
            "2. Code lấy bằng cách nào: Code nạp giá trị thông qua biến môi trường hệ thống, ví dụ sử dụng `os.getenv('OPENAI_API_KEY')` trong Python hoặc thư viện `dotenv`.\n"
            "3. Kho mã giữ file mẫu nào: Kho mã (Git repository) lưu file mẫu `.env.example` mô tả hợp đồng danh sách tên biến môi trường cần thiết kèm giá trị rỗng hoặc giá trị giả định mẫu.\n"
            "4. File nào phải bỏ theo dõi: File chứa key thật (`.env`, `.env.local`) bắt buộc phải được khai báo trong file `.gitignore` để Git không bao giờ theo dõi hay commit lên repository."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc III trong kiến trúc The Twelve-Factor App quy định: Tách biệt cấu hình và bí mật khỏi mã nguồn (Config in the Environment). "
            "Việc để lộ API key trong Git commit history là một trong những lỗ hổng bảo mật phổ biến nhất dẫn đến chiếm đoạt tài khoản và rò rỉ dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Vị trí lưu key thật và cách code lấy (1.5 điểm): Nêu rõ key lưu ở `.env` cục bộ và lấy qua biến môi trường (`os.getenv`).\n"
            "- File mẫu và file bỏ theo dõi (1.5 điểm): Nêu đúng file mẫu `.env.example` lưu trên Git và file `.env` phải đưa vào `.gitignore`."
        ),
        "reference_source": "The Twelve-Factor App - III. Config (https://12factor.net/config); OWASP Secrets Management Cheat Sheet."
    }

    # 33. d01-q109 (3 pts)
    data["d01-q109"] = {
        "sample_answer": (
            "1. Sửa đổi cần làm: Đổi tên trường trong payload JSON request từ `max_tokens` thành `max_output_tokens` để tuân thủ chính xác hợp đồng quy định của nhà cung cấp.\n"
            "2. Vì sao không nên đoán alias sẽ hoạt động:\n"
            "- Các API hiện đại thường sử dụng schema validator nghiêm ngặt (như Pydantic hoặc JSON Schema). Việc gửi trường không có trong đặc tả kỹ thuật sẽ dẫn đến lỗi "
            "HTTP 422 Unprocessable Entity hoặc HTTP 400 Bad Request.\n"
            "- Trong trường hợp API không báo lỗi, trường không xác định thường bị âm thầm bỏ qua (silently ignored). Khi đó, mô hình sẽ tự động áp dụng giá trị mặc định "
            "(default limit), có thể gây cắt cụt văn bản đột ngột hoặc sinh thừa token gây lãng phí chi phí mà lập trình viên không hề hay biết."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Strict Interface Adherence' trong kiến trúc RESTful API đòi hỏi hệ thống client phải tuân thủ nghiêm ngặt "
            "hợp đồng giao diện. Giả định ngầm định về bí danh (alias assumption) là nguồn cơn của các lỗi âm thầm (silent failures) rất khó debug trong môi trường production."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nêu đúng sửa đổi (1.5 điểm): Đổi chính xác trường `max_tokens` thành `max_output_tokens` theo API contract.\n"
            "- Giải thích vì sao không đoán alias (1.5 điểm): Phân tích nguy cơ bị từ chối request (422/400) hoặc bị lờ đi âm thầm khiến hệ thống dùng giá trị mặc định sai lệch."
        ),
        "reference_source": "OpenAPI Specification 3.0 (https://spec.openapis.org/oas/v3.0.3); Postel's Law / Robustness Principle in Software Engineering."
    }

    # 34. d01-q111 (3 pts)
    data["d01-q111"] = {
        "sample_answer": (
            "Cách xử lý chủ động không làm crash ứng dụng và không bịa nội dung:\n"
            "1. Kiểm tra điều kiện tiên quyết (Defensive Guard Check): Trước khi truy cập `choices[0]`, kiểm tra độ dài mảng:\n"
            "```python\n"
            "choices = response.get('choices', [])\n"
            "if not choices:\n"
            "    # Kiểm tra cờ từ chối do an toàn nếu có\n"
            "    prompt_filter = response.get('prompt_filter_results', [])\n"
            "    raise ValueError(f'API returned empty choices list. Safety filters triggered: {prompt_filter}')\n"
            "```\n"
            "2. Xử lý phản hồi có cấu trúc: Trả về một đối tượng lỗi có kiểm soát (Error Result Object) hoặc thông báo rõ ràng cho người dùng rằng yêu cầu "
            "không tạo ra nội dung do bị bộ lọc an toàn của nhà cung cấp chặn hoặc do sự cố kỹ thuật từ phía server, thay vì trả về một chuỗi bịa đặt hay để phát sinh ngoại lệ `IndexError`."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Lập trình phòng thủ (Defensive Programming) đòi hỏi mọi thao tác truy cập chỉ mục mảng từ dữ liệu mạng "
            "đều phải được bọc bởi guard clause. Tách biệt rõ ràng giữa 'kết quả rỗng hợp lệ' và 'sự cố bị chặn bởi bộ lọc' giúp hệ thống duy trì tính ổn định."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Kiểm tra mảng phòng thủ (1.5 điểm): Viết điều kiện kiểm tra `if not choices` trước khi truy cập index 0 để ngăn chặn `IndexError`.\n"
            "- Xử lý lỗi minh bạch không bịa đặt (1.5 điểm): Ném ngoại lệ có cấu trúc hoặc trả về mã lỗi rõ ràng báo hiệu phản hồi rỗng/bị chặn an toàn."
        ),
        "reference_source": "OpenAI API Reference - Errors and Safety Filter Responses; Fowler, M. - Refactoring: Guard Clauses (https://refactoring.com)."
    }

    # 35. d01-q113 (3 pts)
    data["d01-q113"] = {
        "sample_answer": (
            "Báo cáo số token chính xác theo đúng ý nghĩa của từng trường trong hợp đồng dữ liệu:\n"
            "- Số token đầu vào (Input Tokens): 120 token — đại diện bởi trường `prompt_tokens`, tương ứng với toàn bộ các token trong tin nhắn hệ thống, ngữ cảnh và câu hỏi của người dùng.\n"
            "- Số token đầu ra (Output / Generated Tokens): 30 token — đại diện bởi trường `completion_tokens`, tương ứng với số lượng token mà mô hình đã sinh ra trong câu trả lời.\n"
            "- Tổng số token (Total Tokens): 150 token — đại diện bởi trường `total_tokens`, là tổng cộng lượng tài nguyên token đã tiêu thụ trong lần gọi API này ($120 + 30 = 150$ token)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Việc phân định rạch ròi giữa `prompt_tokens` và `completion_tokens` là cốt lõi trong hạch toán chi phí LLM, "
            "vì hầu hết các nhà cung cấp áp dụng đơn giá cho token đầu ra đắt gấp 2 đến 4 lần so với token đầu vào."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Báo cáo token đầu vào (1.0 điểm): Xác định đúng 120 token từ `prompt_tokens`.\n"
            "- Báo cáo token đầu ra (1.0 điểm): Xác định đúng 30 token từ `completion_tokens`.\n"
            "- Báo cáo tổng token (1.0 điểm): Xác định đúng 150 token từ `total_tokens`."
        ),
        "reference_source": "OpenAI API Reference - Chat Completion Object Usage (https://platform.openai.com/docs/api-reference/chat/object#chat/object-usage)"
    }

    # 36. d01-q117 (3 pts)
    data["d01-q117"] = {
        "sample_answer": (
            "- Trạng thái hệ thống: Yêu cầu chưa hoàn thành; mô hình chưa đưa ra câu trả lời cuối cùng mà đang ở trạng thái Yêu cầu gọi công cụ (Tool Call Request). "
            "Đoạn text `'Tôi sẽ kiểm tra lịch'` chỉ là thông điệp phụ trợ/suy nghĩ trung gian, không phải là kết quả trả về cho người dùng.\n"
            "- Bước xử lý tiếp theo:\n"
            "1. Client phía backend trích xuất tên công cụ và tham số arguments từ `message.tool_calls`.\n"
            "2. Backend thực thi hàm cục bộ tương ứng (ví dụ: gọi API kiểm tra lịch trình của người dùng với các đối số nhận được).\n"
            "3. Client đóng gói kết quả thực thi thành một message có role `'tool'` kèm `tool_call_id` tương ứng, nối vào lịch sử hội thoại và gửi một request tiếp theo "
            "đến mô hình để mô hình đọc kết quả và tạo câu trả lời cuối cùng."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: `finish_reason='tool_call'` biểu thị sự chuyển giao quyền kiểm soát (Control Handoff) từ LLM sang môi trường máy chủ. "
            "Mô hình không tự thực thi mã mạng; hệ thống runtime phải đảm nhiệm việc điều phối, thực thi công cụ và hoàn trả quan sát (Observation) vào vòng lặp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nhận diện đúng trạng thái (1.5 điểm): Xác định đây là trạng thái trung gian yêu cầu gọi tool, text không phải kết quả cuối.\n"
            "- Quy trình xử lý tiếp theo (1.5 điểm): Trình bày đủ 3 bước: trích xuất args -> thực thi tool -> gửi trả message role tool để model tiếp tục sinh."
        ),
        "reference_source": "OpenAI Documentation - Function Calling Flow (https://platform.openai.com/docs/guides/function-calling); Anthropic Claude - Tool Use Integration."
    }

    # 37. d01-q119 (3 pts)
    data["d01-q119"] = {
        "sample_answer": (
            "1. Có thể kết luận lời gọi mạng của B nhanh hơn không?: KHÔNG THỂ kết luận. Phép đo của Model A bị cộng dồn thêm 0,5 giây độ trễ của khâu khởi tạo client "
            "(bao gồm khởi tạo HTTP session, phân giải DNS lookup, bắt tay TLS handshake và thiết lập connection pool), trong khi Model B tái sử dụng kết nối ấm (warm connection). "
            "Nếu loại bỏ 0,5 giây khởi tạo, thời gian gọi mạng thuần túy của A thực tế chỉ là $1,2 - 0,5 = 0,7$ giây, nhanh hơn thời gian 0,9 giây của B.\n\n"
            "2. Sửa quy trình đo để đảm bảo tính khách quan:\n"
            "- Khởi tạo và warm-up client trước cho cả hai mô hình (sử dụng connection pooling và keep-alive).\n"
            "- Chỉ bấm giờ đo thời gian thực thi của chính hàm API call (từ ngay trước lệnh gửi request đến khi nhận được response hoàn chỉnh).\n"
            "- Thực hiện lặp lại tối thiểu 20-30 lần cho mỗi mô hình và so sánh dựa trên các chỉ số phân vị (P50, P95, P99) thay vì một lần đo duy nhất."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong đo kiểm hiệu năng mạng (Benchmarking & Profiling), việc để lẫn chi phí thiết lập kết nối (cold start overhead) "
            "vào thời gian xử lý nghiệp vụ sẽ làm sai lệch hoàn toàn kết quả so sánh. Phép đo hợp lệ phải cô lập hoàn toàn thời gian mạng vòng (Round Trip Time) "
            "trên các kết nối đã được hâm nóng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Đánh giá kết luận sai lệch (1.5 điểm): Khẳng định không thể kết luận B nhanh hơn, chỉ ra A có thời gian gọi mạng thuần túy là 0,7s sau khi trừ 0,5s init client.\n"
            "- Đề xuất quy trình đo chuẩn (1.5 điểm): Nêu rõ việc warm-up/tái sử dụng client, chỉ đo round-trip của API call và đo lặp lại theo phân vị P50/P95."
        ),
        "reference_source": "Google SRE Book - Monitoring Distributed Systems & Latency Benchmarks (https://sre.google/sre-book/); High Performance Browser Networking - HTTP Connection Management."
    }

    # 38. d01-q122 (3 pts)
    data["d01-q122"] = {
        "sample_answer": (
            "Danh sách hai message chuẩn theo đúng thứ tự và vai trò (role):\n"
            "1. Message 1 (System):\n"
            "```json\n"
            "{\n"
            "  \"role\": \"system\",\n"
            "  \"content\": \"Bạn là trợ giảng ngắn gọn.\"\n"
            "}\n"
            "```\n"
            "2. Message 2 (User):\n"
            "```json\n"
            "{\n"
            "  \"role\": \"user\",\n"
            "  \"content\": \"Tóm tắt đoạn văn này: [Nội dung văn bản cần tóm tắt]\"\n"
            "}\n"
            "```\n"
            "Thứ tự bắt buộc: Tin nhắn `system` luôn đứng đầu để thiết lập ngữ cảnh định hình persona và phong cách phản hồi bền vững; tiếp theo là tin nhắn `user` chứa nhiệm vụ thực thi cụ thể của lượt tương tác."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Kiến trúc Chat Completion phân cấp rõ ràng mức độ ưu tiên của các chỉ dẫn: Role `system` thiết lập các ràng buộc nền tảng, "
            "tông giọng và ranh giới an toàn; role `user` mang tải trọng dữ liệu của tác vụ. Đặt chỉ dẫn hệ thống vào đúng vai trò giúp mô hình phân định ranh giới giữa quy tắc và dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Cấu hình message 1 đúng role và nội dung (1.5 điểm): Nêu đúng message 1 có role `'system'` với nội dung persona `Bạn là trợ giảng ngắn gọn`.\n"
            "- Cấu hình message 2 đúng role và nội dung (1.5 điểm): Nêu đúng message 2 có role `'user'` với nội dung task `Tóm tắt đoạn văn này` đứng sau message system."
        ),
        "reference_source": "OpenAI Documentation - Chat Completions Roles Architecture (https://platform.openai.com/docs/guides/chat-completions); Anthropic Claude Messages API."
    }

    # 39. d01-q125 (4 pts)
    data["d01-q125"] = {
        "sample_answer": (
            "Soạn thảo prompt tuân thủ đầy đủ cấu trúc 4 lớp chuyên nghiệp:\n\n"
            "### LỚP 1: CHỈ DẪN HỆ THỐNG / VAI TRÒ (SYSTEM INSTRUCTION / ROLE)\n"
            "Bạn là chuyên viên tư vấn nhân sự nội bộ của công ty. Nhiệm vụ của bạn là giải đáp thắc mắc của nhân viên một cách khách quan, chuẩn xác và trung thực "
            "dựa duy nhất trên tài liệu chính sách được cung cấp. Tuyệt đối không suy diễn ngoài văn bản.\n\n"
            "### LỚP 2: NGỮ CẢNH DỮ LIỆU (GROUNDING CONTEXT)\n"
            "Dưới đây là đoạn văn bản chính sách nhân sự công ty có hiệu lực hiện hành:\n"
            "\"\"\"\n"
            "{policy_document_content}\n"
            "\"\"\"\n\n"
            "### LỚP 3: NHIỆM VỤ CỤ THỂ CỦA NGƯỜI DÙNG (USER TASK / INPUT)\n"
            "Câu hỏi của nhân viên cần giải đáp:\n"
            "\"\"\"\n"
            "{employee_question}\n"
            "\"\"\"\n\n"
            "### LỚP 4: HỢP ĐỒNG ĐẦU RA VÀ RÀNG BUỘC (OUTPUT CONTRACT & CONSTRAINTS)\n"
            "Bạn bắt buộc phải phản hồi dưới định dạng JSON hợp lệ tuân thủ chính xác schema có đúng ba trường sau, không thêm bất kỳ văn bản giải thích nào ngoài JSON:\n"
            "{\n"
            "  \"answer\": \"<Câu trả lời trực tiếp, rõ ràng cho câu hỏi của nhân viên>\",\n"
            "  \"quote\": \"<Trích dẫn nguyên văn câu/đoạn trong văn bản chính sách làm căn cứ xác thực>\",\n"
            "  \"uncertainty\": \"<Nêu mức độ không chắc chắn hoặc ghi rõ nếu chính sách không đề cập đầy đủ>\"\n"
            "}"
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Cấu trúc 4 lớp (Role -> Context -> Task -> Output Contract) là mẫu thiết kế prompt công nghiệp tiêu chuẩn "
            "(Industrial Prompt Engineering Pattern). Phân tách rõ ràng giữa tri thức cơ sở (Context) và quy cách giao tiếp (Output Contract) "
            "giúp loại bỏ ảo giác và đảm bảo khả năng tích hợp tự động với các hệ thống backend."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Lớp 1 - Vai trò/Chỉ dẫn hệ thống (1.0 điểm): Thiết lập rõ persona chuyên viên nhân sự và nguyên tắc trung thực.\n"
            "- Lớp 2 - Ngữ cảnh dữ liệu (1.0 điểm): Bọc đoạn trích văn bản chính sách rõ ràng với dấu phân cách.\n"
            "- Lớp 3 - Nhiệm vụ người dùng (1.0 điểm): Định vị câu hỏi của nhân viên rõ ràng.\n"
            "- Lớp 4 - Hợp đồng đầu ra (1.0 điểm): Quy định định dạng JSON hợp lệ chứa đúng 3 trường bắt buộc: `answer`, `quote`, `uncertainty`."
        ),
        "reference_source": "Anthropic Claude Prompt Engineering Guide - Structuring Prompts (https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering); LangChain Prompt Design Patterns."
    }

    # 40. d01-q128 (3 pts)
    data["d01-q128"] = {
        "sample_answer": (
            "Thực hiện ánh xạ hợp đồng API từ Provider A sang Provider B theo quy tắc đã cho (A:`a-1` ↔ B:`b-7`):\n\n"
            "1. Request của Provider B:\n"
            "```json\n"
            "{\n"
            "  \"model_id\": \"b-7\",\n"
            "  \"system\": \"Trả ngắn\",\n"
            "  \"input\": \"Giải thích token\"\n"
            "}\n"
            "```\n\n"
            "2. Các trường Response tương ứng của Provider B:\n"
            "```json\n"
            "{\n"
            "  \"result\": {\n"
            "    \"text\": \"Đơn vị xử lý\"\n"
            "  },\n"
            "  \"metrics\": {\n"
            "    \"input_tokens\": 12,\n"
            "    \"output_tokens\": 4\n"
            "  }\n"
            "}\n"
            "```\n"
            "(Ánh xạ: `choices[0].message.content` -> `result.text` = 'Đơn vị xử lý'; `usage.prompt_tokens` -> `metrics.input_tokens` = 12; `usage.completion_tokens` -> `metrics.output_tokens` = 4)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Đây là mô hình Adapter Pattern trong kiến trúc tích hợp LLM Gateway. "
            "Gateway phải đóng vai trò trừu tượng hóa các biến thể schema khác nhau giữa các nhà cung cấp (OpenAI style vs Anthropic/Bedrock style) "
            "về một mô hình đối tượng chuẩn thống nhất của doanh nghiệp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Ánh xạ Request của B chính xác (1.5 điểm): Ghi đúng `model_id: 'b-7'`, `system: 'Trả ngắn'`, `input: 'Giải thích token'`.\n"
            "- Ánh xạ Response của B chính xác (1.5 điểm): Ghi đúng `result.text: 'Đơn vị xử lý'`, `metrics.input_tokens: 12`, `metrics.output_tokens: 4`."
        ),
        "reference_source": "Gamma, E., et al. Design Patterns: Elements of Reusable Object-Oriented Software (Adapter Pattern); LiteLLM Provider Mapping Documentation (https://docs.litellm.ai/docs/providers)"
    }

    # 41. d01-q131 (3 pts)
    data["d01-q131"] = {
        "sample_answer": (
            "Điền hai bước còn thiếu trong quy trình suy luận mô hình cục bộ với Hugging Face Transformers:\n\n"
            "1. Chỗ trống 1 (Mã hóa văn bản thành tensor đầu vào):\n"
            "```python\n"
            "inputs = tokenizer(prompt, return_tensors=\"pt\")\n"
            "```\n"
            "(Hàm tokenizer nhận chuỗi `prompt`, chuyển đổi thành các token ID và trả về đối tượng từ điển chứa PyTorch tensors `input_ids` và `attention_mask` sẵn sàng nạp vào GPU/CPU).\n\n"
            "2. Chỗ trống 2 (Giải mã token IDs sinh ra thành văn bản tự nhiên):\n"
            "```python\n"
            "text = tokenizer.decode(ids[0], skip_special_tokens=True)\n"
            "```\n"
            "(Hàm decode chuyển đổi mảng số nguyên token IDs trở lại thành chuỗi văn bản tự nhiên, tham số `skip_special_tokens=True` giúp loại bỏ các token điều khiển hệ thống như `<|endoftext|>`, `<s>`, `</s>`)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Vòng đời suy luận LLM cục bộ luôn tuân theo quy trình 3 giai đoạn đối xứng: Tokenize (Text -> Tensor) -> "
            "Model Generate (Tensor -> Token IDs) -> Detokenize/Decode (Token IDs -> Text). Việc bỏ qua `skip_special_tokens` sẽ để lộ các ký tự kỹ thuật nội bộ ra giao diện người dùng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Điền đúng chỗ trống 1 (1.5 điểm): Viết chính xác `tokenizer(prompt, return_tensors=\"pt\")`.\n"
            "- Điền đúng chỗ trống 2 (1.5 điểm): Viết chính xác `tokenizer.decode(ids[0], skip_special_tokens=True)`."
        ),
        "reference_source": "Hugging Face Transformers Documentation - Generation with LLMs (https://huggingface.co/docs/transformers/generation_strategies); PyTorch Model Inference."
    }

    # 42. d01-q132 (3 pts)
    data["d01-q132"] = {
        "sample_answer": (
            "- Chuỗi text được ứng dụng phát / ghép thành: `\"Xin chào!\"`\n"
            "Giải thích: Bắt đầu với chuỗi rỗng `\"\"` -> bỏ qua `None` -> cộng `'Xin'` -> bỏ qua `''` -> cộng `' chào'` (giữ nguyên khoảng trắng ở đầu delta) -> cộng `'!'` "
            "tạo thành chuỗi hoàn chỉnh chuẩn xác là `\"Xin chào!\"`.\n\n"
            "- Các chunk bị bỏ qua không ghép vào nội dung:\n"
            "1. Chunk có delta là `None`: Đây là chunk rỗng thường xuất hiện ở gói tin đầu tiên (metadata/role) hoặc gói tin cuối cùng báo hiệu kết thúc stream (`finish_reason`).\n"
            "2. Chunk có delta là chuỗi rỗng `''`: Không mang tải trọng văn bản mới nên cần bỏ qua để tránh xử lý dư thừa."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong xử lý luồng Server-Sent Events (SSE), các delta ký tự được truyền tải từng mảnh nhỏ. "
            "Bộ ghép chuỗi (Stream Accumulator) phải bảo toàn tuyệt đối các khoảng trắng dẫn đầu (leading whitespace) trong từng token "
            "và lọc bỏ các payload rỗng hoặc tín hiệu điều khiển kỹ thuật (`None`, `\"\"`) để không gây gián đoạn chuỗi hiển thị."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Ghép đúng chuỗi văn bản hoàn chỉnh (1.5 điểm): Xác định chính xác kết quả ghép là `\"Xin chào!\"` (bảo toàn khoảng trắng giữa 'Xin' và 'chào').\n"
            "- Xác định đúng các chunk cần bỏ qua (1.5 điểm): Nêu rõ việc lọc bỏ chunk `None` và chuỗi rỗng `''`."
        ),
        "reference_source": "W3C Server-Sent Events (SSE) Specification (https://html.spec.whatwg.org/multipage/server-sent-events.html); OpenAI API Streaming Guide (https://platform.openai.com/docs/api-reference/streaming)"
    }

    # 43. d01-q137 (3 pts)
    data["d01-q137"] = {
        "sample_answer": (
            "1. Vì sao vẫn chọn chế độ streaming:\n"
            "Mặc dù tổng thời gian hoàn tất tác vụ không đổi (vẫn mất 2 phút), streaming tối ưu hóa triệt để cảm nhận thời gian chờ đợi của người dùng (Perceived Latency). "
            "Chỉ số Thời gian đến token đầu tiên (Time to First Token - TTFT) giảm ngoạn mục xuống chỉ còn 0,5 giây. Người dùng có thể bắt đầu đọc, tiếp thu và thực hiện "
            "ngay các bước hướng dẫn ban đầu trong khi mô hình tiếp tục sinh các bước tiếp theo, loại bỏ hoàn toàn cảm giác hệ thống bị đơ hay phản hồi chậm.\n\n"
            "2. Điều gì KHÔNG ĐƯỢC khẳng định:\n"
            "KHÔNG ĐƯỢC khẳng định rằng streaming làm giảm tổng thời gian xử lý của hệ thống (Total Request Latency / Generation Time) hoặc làm tăng thông lượng (throughput) "
            "của máy chủ. Tổng thời gian chạy và lượng tính toán tiêu thụ trên GPU giữa hai chế độ là hoàn toàn như nhau."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc thiết kế trải nghiệm người dùng trong AI (HCI / UX for AI) phân biệt rõ giữa Tốc độ thực tế "
            "(Actual Performance) và Tốc độ cảm nhận (Perceived Performance). Với các tác vụ sinh nội dung dài (long-form generation), "
            "TTFT dưới 1 giây giữ người dùng ở lại trong trạng thái tập trung liên tục (flow state)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Giải thích lý do chọn streaming (1.5 điểm): Phân tích tối ưu Perceived Latency và chỉ số Time to First Token (TTFT = 0,5s) giúp người dùng đọc ngay lập tức.\n"
            "- Khẳng định điều không đúng (1.5 điểm): Nêu rõ streaming không làm giảm tổng thời gian hoàn thành (vẫn 2 phút) và không tăng throughput phần cứng."
        ),
        "reference_source": "Nielsen Norman Group - Response Times: The 3 Important Limits (https://www.nngroup.com/articles/response-times-3-important-limits/); Vercel AI SDK - UX Principles."
    }

    # 44. d01-q139 (3 pts)
    data["d01-q139"] = {
        "sample_answer": (
            "Theo chính sách lưu giữ tối đa 2 cặp user/assistant hoàn chỉnh gần nhất, lịch sử hội thoại được gửi trước `U4` là:\n"
            "```\n"
            "[U2, A2, U3, A3]\n"
            "```\n"
            "Giải thích: Lịch sử hiện tại gồm 3 cặp hoàn chỉnh: Cặp 1 (`U1, A1`), Cặp 2 (`U2, A2`), Cặp 3 (`U3, A3`). "
            "Chính sách cửa sổ trượt (Sliding Window Policy) yêu cầu chỉ giữ lại 2 cặp gần nhất, do đó cặp cũ nhất `[U1, A1]` bị loại bỏ. "
            "Request tiếp theo khi người dùng gửi `U4` sẽ chứa lịch sử gồm `[U2, A2, U3, A3]` theo sau bởi câu hỏi mới `U4`."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Quản lý bộ nhớ hội thoại theo cặp hoàn chỉnh (Conversation Pair-based Windowing) đảm bảo mô hình luôn "
            "nhận được ngữ cảnh cân bằng giữa câu hỏi và câu trả lời tương ứng. Tránh tình trạng cắt lẻ tẻ từng message làm mất tính toàn vẹn của lượt hội thoại."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xác định đúng lịch sử cần gửi (2.0 điểm): Nêu chính xác danh sách gồm 2 cặp `[U2, A2, U3, A3]`.\n"
            "- Giải thích loại bỏ cặp cũ nhất (1.0 điểm): Giải thích rõ cặp `[U1, A1]` bị cắt tỉa do vượt quá ngưỡng giới hạn 2 cặp."
        ),
        "reference_source": "LangChain Documentation - Memory: ConversationBufferWindowMemory (https://python.langchain.com/docs/modules/memory/); Semantic Kernel Context Management."
    }

    # 45. d01-q141 (3 pts)
    data["d01-q141"] = {
        "sample_answer": (
            "Tính toán các khoảng thời gian chờ thực tế giữa các lần thử theo công thức $Delay = 1 \\times 2^{(\\text{attempt\\_index} - 1)}$ giây:\n"
            "1. Lần thử 1 thất bại (attempt_index = 1): Khoảng chờ trước lần thử 2 là $1 \\times 2^{1 - 1} = 1 \\times 2^0 = 1$ giây.\n"
            "2. Lần thử 2 thất bại (attempt_index = 2): Khoảng chờ trước lần thử 3 là $1 \\times 2^{2 - 1} = 1 \\times 2^1 = 2$ giây.\n"
            "3. Lần thử 3 thất bại (attempt_index = 3): Khoảng chờ trước lần thử 4 là $1 \\times 2^{3 - 1} = 1 \\times 2^2 = 4$ giây.\n"
            "4. Lần thử 4 thành công: Không có khoảng chờ sau lần thử 4 vì tác vụ đã hoàn tất thành công.\n\n"
            "Kết luận: Các khoảng chờ thực tế lần lượt là: 1 giây, 2 giây, và 4 giây (tổng thời gian chờ giữa các lần thử là $1 + 2 + 4 = 7$ giây)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Thuật toán Exponential Backoff kéo giãn thời gian chờ theo hàm mũ sau mỗi lần lỗi, "
            "giúp hệ thống hạ lưu (downstream service) có thời gian hồi phục sau sự cố quá tải tạm thời (transient overload), "
            "ngăn chặn hiện tượng giông bão yêu cầu (Thundering Herd Problem)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Tính chính xác các khoảng chờ (2.0 điểm): Tính đúng 3 khoảng chờ lần lượt là 1 giây, 2 giây và 4 giây.\n"
            "- Giải thích không chờ sau lần 4 (1.0 điểm): Nêu rõ lần thử 4 thành công nên kết thúc quy trình, không phát sinh thời gian chờ tiếp theo."
        ),
        "reference_source": "AWS Architecture Blog - Exponential Backoff And Jitter (https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/); Google Cloud Retry Guidance."
    }

    # 46. d01-q143 (3 pts)
    data["d01-q143"] = {
        "sample_answer": (
            "1. Hành động phải làm sau lần thử thứ 3 thất bại:\n"
            "Hệ thống phải lập tức dừng quy trình retry, ghi log chi tiết lỗi cuối cùng E3 (kèm thông tin context và stack trace), "
            "và ném ra ngoại lệ thất bại (raise Exception) hoặc trả về mã lỗi thất bại dứt điểm (ví dụ HTTP 503 / 500) cho phía gọi (Fail-Fast).\n\n"
            "2. Vì sao không chờ thêm:\n"
            "Bởi vì chính sách chỉ cho phép tối đa 3 lần thử (max attempts = 3). Mọi khoảng chờ trong cơ chế retry chỉ có ý nghĩa khi có một lần thử tiếp theo "
            "được lên lịch để bù đắp. Khi đã chạm ngưỡng thử tối đa mà không còn lần thử nào nữa, việc chờ thêm là hoàn toàn vô ích, gây lãng phí tài nguyên "
            "luồng thực thi (blocked worker threads) và làm tăng độ trễ vô nghĩa cho client."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên lý Fail-Fast và Resource Conservation trong thiết kế hệ thống phân tán quy định: "
            "Khi một tác vụ đã sử dụng hết ngân sách thử lại (retry budget), hệ thống phải giải phóng tài nguyên ngay lập tức để bảo vệ "
            "tính sẵn sàng của toàn hệ thống."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Hành động sau lần thử cuối (1.5 điểm): Nêu rõ việc dừng retry, ghi log lỗi E3 và ném ngoại lệ thất bại (fail-fast).\n"
            "- Giải thích lý do không chờ thêm (1.5 điểm): Phân tích việc hết ngân sách thử (đã đủ 3 lần) khiến việc chờ thêm không phục vụ mục đích nào, gây treo tài nguyên."
        ),
        "reference_source": "Google SRE Book - Addressing Cascading Failures & Retry Budgets (https://sre.google/sre-book/addressing-cascading-failures/); Microsoft Cloud Design Patterns - Retry Pattern."
    }

    # 47. d01-q146 (4 pts)
    data["d01-q146"] = {
        "sample_answer": (
            "Bản mô tả yêu cầu kỹ thuật và tiêu chí chấp nhận cho hàm Python:\n\n"
            "### 1. GIAO DIỆN HÀM (FUNCTION SIGNATURE)\n"
            "```python\n"
            "def calculate_total_amount(csv_file_path: str) -> float:\n"
            "    \"\"\"\n"
            "    Đọc file CSV cục bộ, tính tổng các giá trị trong cột 'amount' và trả về số thực.\n"
            "    \"\"\"\n"
            "```\n\n"
            "### 2. CÁC TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)\n"
            "- Tiêu chí 1 (Happy Path - Tính tổng chuẩn xác): Khi truyền đường dẫn đến một file CSV hợp lệ có cột `amount` (ví dụ chứa các giá trị 10.5, 20.0, 5.5), hàm trả về kết quả số thực chính xác là `36.0`.\n"
            "- Tiêu chí 2 (Bỏ qua dòng trống): Các dòng hoàn toàn trống, dòng chỉ chứa khoảng trắng hoặc dấu phẩy rỗng giữa các dòng dữ liệu không được gây lỗi và phải được tự động bỏ qua khi tính toán.\n"
            "- Tiêu chí 3 (Báo lỗi khi thiếu cột bắt buộc): Nếu file CSV tồn tại nhưng không chứa cột có tiêu đề chính xác là `'amount'`, hàm phải ném ra ngoại lệ `ValueError` với thông báo rõ ràng: `\"Missing required 'amount' column\"`.\n"
            "- Tiêu chí 4 (Cô lập ngoại vi & Không kết nối mạng): Toàn bộ thao tác chỉ sử dụng thư viện chuẩn của Python (`csv` hoặc `pathlib`), thực thi 100% trên hệ thống file cục bộ, không mở bất kỳ kết nối socket/HTTP mạng nào."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Bản đặc tả kỹ thuật tiêu chuẩn (Executable Specification / Given-When-Then) cần định nghĩa ranh giới rõ ràng "
            "về kiểu dữ liệu (Type hinting), các kịch bản thành công, xử lý biên (empty rows), điều kiện lỗi (error handling) và các ràng buộc phi chức năng (no network)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Giao diện hàm rõ ràng (1.0 điểm): Định nghĩa đúng signature có kiểu dữ liệu đầu vào `csv_file_path: str` và đầu ra `float`.\n"
            "- Tiêu chí tính tổng & bỏ dòng trống (1.0 điểm): Nêu rõ test case tính đúng số tiền và bỏ qua các dòng trống an toàn.\n"
            "- Tiêu chí báo lỗi thiếu cột (1.0 điểm): Quy định ném ngoại lệ `ValueError` khi file thiếu cột `'amount'`.\n"
            "- Ràng buộc không dùng mạng (1.0 điểm): Khẳng định thực thi hoàn toàn cục bộ, không mở kết nối socket mạng."
        ),
        "reference_source": "Martin Fowler - Specification by Example (https://martinfowler.com/bliki/GivenWhenThen.html); Python Documentation - csv module."
    }

    # 48. d01-q148 (4 pts)
    data["d01-q148"] = {
        "sample_answer": (
            "1. Chỉ ra lỗi trong mã do AI sinh:\n"
            "Khi `b == 0`, hàm trả về giá trị `0` (`return 0`) thay vì ném ra ngoại lệ `ValueError` theo đúng yêu cầu đặc tả. "
            "Điều này làm sai lệch ngữ nghĩa toán học (phép chia cho 0 là không xác định) và che giấu lỗi nghiêm trọng, khiến các phép tính phía sau tiếp tục chạy với dữ liệu sai.\n\n"
            "2. Viết bài kiểm thử tối thiểu (sử dụng pytest):\n"
            "```python\n"
            "import pytest\n\n"
            "def test_safe_divide_by_zero_raises_value_error():\n"
            "    with pytest.raises(ValueError, match=\"Cannot divide by zero\"):\n"
            "        safe_divide(10, 0)\n\n"
            "def test_safe_divide_valid():\n"
            "    assert safe_divide(10, 2) == 5.0\n"
            "```\n\n"
            "3. Sửa mã nguồn chuẩn xác:\n"
            "```python\n"
            "def safe_divide(a, b):\n"
            "    if b == 0:\n"
            "        raise ValueError(\"Cannot divide by zero\")\n"
            "    return a / b\n"
            "```"
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Đây là lỗi vi phạm hợp đồng hàm (Contract Violation) rất phổ biến trong code do AI sinh: "
            "AI có xu hướng 'nuốt lỗi' bằng cách trả về giá trị mặc định (như 0 hoặc None) thay vì raise exception. Điều này vi phạm nguyên tắc "
            "Fail-Fast của kỹ nghệ phần mềm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Chỉ ra lỗi sai hợp đồng (1.5 điểm): Nêu rõ hàm trả về 0 thay vì ném ngoại lệ `ValueError` khi `b == 0`.\n"
            "- Viết bài kiểm thử pytest chuẩn (1.5 điểm): Viết test case sử dụng `pytest.raises(ValueError)` để kiểm tra ngoại lệ.\n"
            "- Sửa mã nguồn chính xác (1.0 điểm): Cập nhật code với lệnh `raise ValueError(...)` khi `b == 0`."
        ),
        "reference_source": "Python Software Foundation - Built-in Exceptions (https://docs.python.org/3/library/exceptions.html); Pytest Documentation - Asserting Expected Exceptions."
    }

    # 49. d01-q149 (4 pts)
    data["d01-q149"] = {
        "sample_answer": (
            "1. Rủi ro bảo mật:\n"
            "Lỗ hổng Path Traversal (Directory Traversal - CWE-22). Phép nối chuỗi thô `'/tmp/reports/' + name` cho phép kẻ tấn công truyền vào chuỗi "
            "`'../../secret'`. Khi chuẩn hóa đường dẫn, `'/tmp/reports/../../secret'` sẽ phân giải thành `'/secret'`, cho phép ghi đè hoặc tạo file "
            "tùy ý ra ngoài thư mục an toàn `/tmp/reports`, gây nguy cơ ghi đè cấu hình hệ thống hoặc chiếm quyền điều khiển máy chủ.\n\n"
            "2. Viết một bài kiểm thử bảo mật (pytest):\n"
            "```python\n"
            "import pytest\n"
            "from pathlib import Path\n\n"
            "def test_path_traversal_prevention(tmp_path):\n"
            "    malicious_input = \"../../secret\"\n"
            "    with pytest.raises(ValueError, match=\"Access denied: Path traversal detected\"):\n"
            "        safe_open_report(malicious_input)\n"
            "```\n\n"
            "3. Đề xuất hướng sửa mã nguồn an toàn:\n"
            "Sử dụng thư viện `pathlib.Path` để phân giải đường dẫn tuyệt đối (canonical path) và kiểm tra xem đường dẫn đích có nằm bên trong thư mục gốc hay không:\n"
            "```python\n"
            "from pathlib import Path\n\n"
            "def safe_open_report(name: str):\n"
            "    base_dir = Path(\"/tmp/reports\").resolve()\n"
            "    target_path = (base_dir / name).resolve()\n"
            "    # Kiểm tra đường dẫn đích có bắt đầu bằng thư mục an toàn\n"
            "    if not str(target_path).startswith(str(base_dir) + \"/\") and target_path != base_dir:\n"
            "        raise ValueError(\"Access denied: Path traversal detected\")\n"
            "    return open(target_path, \"w\")\n"
            "```"
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Lỗ hổng CWE-22 xảy ra khi mã nguồn tin tưởng mù quáng vào input của người dùng để ghép đường dẫn file. "
            "Biện pháp phòng ngừa chuẩn tắc là luôn chuẩn hóa đường dẫn (Canonicalization) bằng `resolve()` hoặc `os.path.realpath` "
            "và kiểm tra tính phụ thuộc thư mục (containment check) trước khi mở file."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Nhận diện đúng rủi ro Path Traversal (1.5 điểm): Gọi tên chính xác lỗ hổng Path Traversal (CWE-22) và giải thích cơ chế thoát khỏi `/tmp/reports` qua `../../`.\n"
            "- Viết test case bảo mật (1.5 điểm): Viết test kiểm tra ném ngoại lệ khi gặp input nguy hại `../../secret`.\n"
            "- Đề xuất code sửa an toàn (1.0 điểm): Sử dụng `Path.resolve()` và kiểm tra đường dẫn đích phải nằm trong `base_dir`."
        ),
        "reference_source": "OWASP Top 10 - Path Traversal (https://owasp.org/www-community/attacks/Path_Traversal); CWE-22: Improper Limitation of a Pathname to a Restricted Directory."
    }

    return data

if __name__ == "__main__":
    d1 = get_day01_data()
    print(f"Authored {len(d1)} Day 1 questions successfully.")
