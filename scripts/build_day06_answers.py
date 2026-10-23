"""
Authoring data for Day 06 (27 questions): AI Product Project Management.
"""

DAY06_ANSWERS = {
    "d06-q002": {
        "sample_answer": (
            "1. Xác định Người thực hiện công việc phù hợp (Job Executor):\n"
            "- Người thực hiện công việc cốt lõi: Quản lý trực tiếp / Người phê duyệt (Approving Manager).\n"
            "- Lý do: Công việc chính được xác định là 'quyết định có phê duyệt một khoản chi hay không'. Người nắm quyền hạn, chịu trách nhiệm pháp lý và ngân sách để đưa ra phán quyết đồng ý hay từ chối khoản chi chính là Quản lý.\n\n"
            "2. Loại bỏ hai vai trò không trực tiếp thực hiện công việc này và lý giải:\n"
            "- Loại vai trò 'Nhân viên tạo yêu cầu' (Requisitioner / Employee): Nhân viên là người khởi tạo nhu cầu chi tiêu (Job Beneficiary / Requester), công việc của họ là 'gửi yêu cầu thanh toán để được hoàn tiền', chứ họ không có thẩm quyền hay trách nhiệm thực hiện việc 'quyết định phê duyệt'.\n"
            "- Loại vai trò 'Kế toán mua gói phần mềm' (Buyer / Procurement / Accountant): Kế toán hoặc bộ phận mua sắm là người thực hiện mua bán hoặc chi tiền sau khi đã có phê duyệt (Job Enabler / Purchaser), họ chỉ thực thi hành động giao dịch tài chính, không phải là người ra quyết định đánh giá tính hợp lý nghiệp vụ để phê duyệt khoản chi."
        ),
        "explanation": (
            "Trong lý thuyết Jobs-to-be-Done (JTBD), việc xác định đúng Người thực hiện công việc (Job Executor) là tối quan trọng. "
            "Cần bóc tách rõ rệt giữa: Người yêu cầu (Requester), Người ra quyết định (Decision Maker/Job Executor), "
            "và Người thực thi kỹ thuật/mua hàng (Purchaser/Enabler). Thiết kế sản phẩm AI cho người duyệt chi phải tập trung vào "
            "hỗ trợ quản lý đánh giá rủi ro và chính sách, chứ không phải các tính năng nhập liệu của nhân viên."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- 1.0 điểm: Xác định chính xác Người thực hiện công việc phù hợp là Quản lý (Approving Manager).\n"
            "- 1.0 điểm: Loại bỏ đúng vai trò Nhân viên tạo yêu cầu kèm lý giải họ là người yêu cầu, không phải người quyết định.\n"
            "- 1.0 điểm: Loại bỏ đúng vai trò Kế toán kèm lý giải họ là người thực hiện mua/chi tiền sau phê duyệt."
        ),
        "reference_source": "Tony Ulwick - Jobs to be Done: Theory to Practice & Strategyn JTBD Framework"
    },
    "d06-q004": {
        "sample_answer": (
            "1. Phát biểu Công việc Chính độc lập với giải pháp (Solution-Independent Core Job Statement):\n"
            "'Đánh giá và xác định các ứng viên đủ điều kiện nhất cho vị trí công việc tuyển dụng trong thời gian ngắn nhất có thể.'\n\n"
            "2. Cấu trúc chuẩn hóa của phát biểu: [Động từ hành động: Đánh giá và xác định] + [Đối tượng ngữ cảnh: các ứng viên đủ điều kiện nhất cho vị trí công việc] + [Ngữ cảnh/Mục tiêu: trong thời gian ngắn nhất có thể].\n\n"
            "3. Giải thích vì sao TUYỆT ĐỐI KHÔNG DÙNG cụm từ 'lọc CV bằng AI':\n"
            "- 'Lọc CV bằng AI' là một Giải pháp công nghệ (Technology Solution / Implementation Mechanism), hoàn toàn không phải là Bản chất công việc của người dùng (Customer Job).\n"
            "- Công việc cốt lõi của nhà tuyển dụng là tìm được người tài phù hợp cho công ty. Họ đã làm công việc này từ hàng chục năm trước bằng hồ sơ giấy, sau đó chuyển sang bảng tính Excel, và hiện nay có thể dùng AI. Nếu công nghệ AI mai sau bị thay thế bởi một mô hình đánh giá năng lực thực tế qua mạng lưới (Skill Network), công việc cốt lõi của họ vẫn không hề thay đổi. Đưa từ khóa 'bằng AI' vào phát biểu sẽ giam cầm tư duy sản phẩm vào công nghệ bề mặt và che khuất mục tiêu thực sự của khách hàng."
        ),
        "explanation": (
            "Một Core Job Statement chuẩn mực theo lý thuyết JTBD của Christensen và Ulwick luôn phải độc lập 100% với giải pháp và công nghệ. "
            "Khách hàng không 'mua máy khoan 5mm hay máy khoan AI', họ 'cần một cái lỗ 5mm trên tường'. "
            "Nhà tuyển dụng cần tìm đúng người phù hợp nhanh nhất; AI chỉ là một phương tiện tạm thời phục vụ mục tiêu đó."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Viết phát biểu công việc chính độc lập hoàn toàn với giải pháp và công nghệ.\n"
            "- 1.0 điểm: Tuân thủ đúng cấu trúc chuẩn JTBD: Động từ + Đối tượng ngữ cảnh + Ngữ cảnh làm rõ.\n"
            "- 1.0 điểm: Đạt mức độ trừu tượng phù hợp (đánh giá ứng viên phù hợp, không quá hẹp cũng không quá rộng).\n"
            "- 1.0 điểm: Giải thích sâu sắc lý do không dùng 'lọc CV bằng AI' (phân biệt giữa công việc trường tồn và công nghệ tạm thời)."
        ),
        "reference_source": "Clayton Christensen - Competing Against Luck: The Story of Innovation and Customer Choice & Strategyn Job Statement Rules"
    },
    "d06-q005": {
        "sample_answer": (
            "Soạn thảo Tình huống Công việc (Job Story) theo cấu trúc chuẩn mực:\n\n"
            "\"Khi chuẩn bị bước vào bài kiểm tra và nhớ rằng có ví dụ về cơ chế attention trong video bài giảng nhưng không nhớ chính xác ở phân đoạn nào, "
            "tôi muốn định vị và mở ngay đúng đoạn ghi hình có chứa ví dụ đó, "
            "để có thể kiểm tra lại từng bước tính toán chi tiết và tự tin làm bài thi đạt điểm cao.\"\n\n"
            "Bóc tách sự tương ứng chặt chẽ với từng phần của dữ kiện quan sát thực tế:\n"
            "1. Tình huống bối cảnh (When - Context): 'Khi chuẩn bị bước vào bài kiểm tra và nhớ có ví dụ về attention nhưng không nhớ nằm ở video nào' -> Trích xuất trực tiếp từ quan sát Lan trước kỳ thi.\n"
            "2. Động lực / Mong muốn hành động (I want to - Motivation): 'tôi muốn định vị và mở ngay đúng đoạn ghi hình có chứa ví dụ đó' -> Trích xuất từ mong muốn thao tác cụ thể của Lan.\n"
            "3. Kết quả mong đợi cuối cùng (So I can - Expected Outcome): 'để có thể kiểm tra lại cách tính và làm bài thi đạt kết quả tốt' -> Trích xuất từ giá trị thực tiễn mà Lan hướng tới."
        ),
        "explanation": (
            "Job Story (khác với User Story truyền thống) tập trung vào Ngữ cảnh kích hoạt (Context), Động lực giải quyết (Motivation) "
            "và Kết quả mong đợi (Outcome). Việc bám sát bằng chứng thực tế từ quan sát người dùng giúp Job Story có tính xác thực cao, "
            "không bị rơi vào các suy diễn chung chung."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Tuân thủ hoàn hảo cấu trúc cú pháp 3 vế 'Khi... tôi muốn... để có thể...'.\n"
            "- 1.0 điểm: Vế tình huống (Khi) lấy chính xác từ bối cảnh trước bài kiểm tra và nhớ mang máng ví dụ attention.\n"
            "- 1.0 điểm: Vế động lực (tôi muốn) lấy chính xác từ mong muốn mở đúng đoạn video bài giảng.\n"
            "- 1.0 điểm: Vế kết quả (để có thể) thể hiện rõ ràng mục đích kiểm tra cách tính toán và chuẩn bị thi."
        ),
        "reference_source": "Alan Klement - Designing Features Using Job Stories (Jobs to be Done Framework)"
    },
    "d06-q007": {
        "sample_answer": (
            "1. Chẩn đoán Lỗi của bản đồ công việc cũ:\n"
            "- Lỗi nghiêm trọng: Nhóm đã mô tả một 'Bản đồ thao tác giao diện trên phần mềm cụ thể' (UI/Feature Click Path) thay vì một 'Bản đồ công việc của người dùng' (Solution-Independent Job Map).\n"
            "- Các bước 'Mở ứng dụng', 'bấm Tải lên', 'chờ AI', 'bấm Tải xuống' toàn bộ là tên nút bấm và cơ chế kỹ thuật của phần mềm. Nếu người dùng nhận được tài liệu tóm tắt qua email do trợ lý gửi, toàn bộ 4 bước này biến mất nhưng công việc chuẩn bị họp của họ vẫn diễn ra bình thường.\n\n"
            "2. Viết lại Bản đồ Công việc độc lập với giải pháp (ít nhất 4 bước dạng Động từ - Đối tượng):\n"
            "- Bước 1: Thu thập và Lựa chọn tài liệu họp (Locate & Aggregate Meeting Documents).\n"
            "- Bước 2: Đọc lướt và Xác định các thông tin trọng tâm cần chú ý (Scan & Identify Key Agendas / Discussion Points).\n"
            "- Bước 3: Trích xuất và Tổng hợp các điểm quyết định then chốt thành bản tóm tắt ngắn (Synthesize Core Action Items & Insights).\n"
            "- Bước 4: Kiểm tra và Đối chiếu tính chính xác của thông tin tóm tắt với văn bản gốc (Verify Factual Accuracy Against Source).\n"
            "- Bước 5 (Đánh dấu trạng thái): Chia sẻ bản tóm tắt cho các thành viên tham gia họp -> ĐÁNH DẤU: [CHƯA CÓ BẰNG CHỨNG / KHÔNG ÁP DỤNG TRONG NGỮ CẢNH CÁ NHÂN TỰ CHUẨN BỊ]."
        ),
        "explanation": (
            "Một Solution-Independent Job Map mô tả hành trình tư duy và công việc phổ quát mà người dùng phải hoàn tất từ lúc bắt đầu đến khi kết thúc, "
            "bất kể họ có dùng AI hay không. Việc sử dụng công thức [Động từ hành động] + [Đối tượng ngữ cảnh] giúp đội ngũ nhìn ra những cơ hội "
            "hỗ trợ người dùng ở các bước chuẩn bị và đối chiếu mà phần mềm hiện tại chưa đáp ứng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Chẩn đoán chính xác lỗi: mô tả click path nút bấm UI/công nghệ thay vì bản đồ công việc khách quan.\n"
            "- 1.0 điểm: Viết lại ít nhất 4 bước độc lập giải pháp chuẩn ngữ pháp [Động từ] - [Đối tượng] cho việc tóm tắt chuẩn bị họp.\n"
            "- 1.0 điểm: Các bước bao quát toàn diện chu trình (thu thập, nhận diện trọng tâm, tổng hợp, đối chiếu).\n"
            "- 1.0 điểm: Đánh dấu chính xác 1 bước chưa có bằng chứng hoặc không áp dụng theo yêu cầu đề bài."
        ),
        "reference_source": "Lance Bettencourt & Anthony Ulwick - The Customer-Centered Innovation Map (Harvard Business Review)"
    },
    "d06-q010": {
        "sample_answer": (
            "Xây dựng Sổ tay Quy tắc Mã hóa Định tính (Qualitative Pattern Codebook) cho mẫu 'Tin nhắn không phải câu hỏi rõ':\n\n"
            "1. Quy tắc Đưa vào (Inclusion Criteria):\n"
            "- Đưa vào mã này nếu tin nhắn của người dùng thuộc một trong các trường hợp sau:\n"
            "  + Chỉ chứa từ chào hỏi xã giao đơn thuần hoặc biểu tượng cảm xúc (ví dụ: 'hii', 'hello', 'alo', icon mặt cười) mà không kèm theo bất kỳ yêu cầu nội dung nào.\n"
            "  + Tin nhắn chỉ là từ ngữ thể hiện cảm thán, ngạc nhiên, hoặc phản ứng mơ hồ ngắn dưới 3 từ mà không có chủ ngữ, vị ngữ hoặc đối tượng truy vấn xác định (ví dụ: 'hả', 'ủa', 'gì vậy').\n"
            "  + Tin nhắn là câu trần thuật hoặc than phiền chung chung về tình trạng bản thân mà không chứa từ để hỏi hoặc yêu cầu hỗ trợ cụ thể (ví dụ: 'em không hiểu attention' - đây là phát biểu trạng thái, chưa nêu rõ câu hỏi cần giải thích khía cạnh nào: công thức, code hay trực giác).\n\n"
            "2. Quy tắc Loại trừ (Exclusion Criteria):\n"
            "- LOẠI TRỪ (Không được gán mã này) đối với bất kỳ tin nhắn nào có chứa từ nghi vấn tường minh (như 'hỏi', 'khi nào', 'ở đâu', 'như thế nào', dấu chấm hỏi '?') hoặc yêu cầu một thông tin cụ thể có thể tra cứu được trong hệ thống (ví dụ: 'cho em hỏi lịch học?', 'bài nộp lúc nào?').\n\n"
            "3. Quy tắc Xử lý Tình huống 'hả' (Borderline Case Resolution):\n"
            "- Quyết định mã hóa: Tin nhắn 'hả' ĐƯỢC GÁN VÀO MÃ 'Tin nhắn không phải câu hỏi rõ' (Inclusion).\n"
            "- Biện minh: 'hả' chỉ là một thán từ phản ứng mang tính bối rối cục bộ, độ dài 1 từ, hoàn toàn không có đối tượng thông tin và không thể hiện bất kỳ nội dung nghiệp vụ nào để trợ giảng AI có thể trả lời trực tiếp. Người chấm độc lập khi áp dụng quy tắc đưa vào sẽ xếp 'hả' vào nhóm phản ứng mơ hồ mà không có bất kỳ sự tranh cãi nào."
        ),
        "explanation": (
            "Trong nghiên cứu định tính và kiểm toán hội thoại AI, một Codebook (sổ tay mã hóa) xuất sắc phải mang tính khách quan có thể tái hiện. "
            "Quy tắc đưa vào và loại trừ phải rõ ràng đến mức một người chấm độc lập không quen biết dự án vẫn có thể phân loại đồng nhất "
            "các trường hợp nhập nhằng như thán từ 'hả'."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Soạn thảo Quy tắc đưa vào (Inclusion) rõ ràng, bao quát các dạng chào hỏi, cảm thán, than phiền mơ hồ.\n"
            "- 1.0 điểm: Soạn thảo Quy tắc loại trừ (Exclusion) cụ thể đối với các câu hỏi có từ nghi vấn và nội dung tra cứu rõ.\n"
            "- 1.0 điểm: Xử lý dứt khoát tình huống 'hả' được đưa vào mã 'không phải câu hỏi rõ' kèm lập luận thuyết phục.\n"
            "- 1.0 điểm: Tiêu chí đảm bảo tính tái hiện cao (Inter-coder reliability): người khác áp dụng vẫn cho kết quả như nhau."
        ),
        "reference_source": "Johnny Saldaña - The Coding Manual for Qualitative Researchers & Content Analysis Methodologies"
    },
    "d06-q011": {
        "sample_answer": (
            "1. Xác định Mẫu số thực dùng (Actual Valid Denominator):\n"
            "- Tổng số hội thoại ban đầu: 200 hội thoại.\n"
            "- Số hội thoại mơ hồ bị loại khỏi cả tử và mẫu: 3 hội thoại.\n"
            "- Mẫu số thực tế sử dụng để tính toán: `Mẫu số = 200 - 3 = 197 hội thoại`.\n\n"
            "2. Xác định Tử số hợp lệ (Valid Numerator):\n"
            "- Số hội thoại có ít nhất một tin nhắn mở đầu không phải câu hỏi rõ theo quy tắc đã khóa: 18 hội thoại.\n\n"
            "3. Báo cáo Tỷ lệ có thể kiểm lại được (Reproducible Prevalence Rate):\n"
            "- Tỷ lệ phổ biến (Prevalence Rate) = `18 / 197 ≈ 0,09137` hay **9,14%** (hoặc trình bày dưới dạng phân số chuẩn kiểm toán: `18/197`).\n\n"
            "4. Cảnh báo tính minh bạch khoa học:\n"
            "Tuyệt đối không được lấy 18 chia cho 200 (= 9,0%), vì 3 hội thoại mơ hồ đã bị loại bỏ khỏi không gian mẫu hợp lệ. Việc báo cáo rõ ràng mẫu số 197 và tử số 18 kèm quy tắc lọc giúp bất kỳ kiểm toán viên độc lập nào cũng có thể tái lập và xác minh lại con số 9,14% một cách nhất quán."
        ),
        "explanation": (
            "Trong dịch tễ học và kiểm toán thống kê sản phẩm AI, khi các trường hợp không đủ điều kiện (Out-of-scope / Ambiguous) "
            "bị loại bỏ khỏi nghiên cứu, chúng bắt buộc phải bị trừ khỏi cả Tử số và Mẫu số. Báo cáo tỷ lệ phổ biến (Prevalence) "
            "phải luôn công bố mẫu số thực dùng để bảo đảm tính toàn vẹn và khả năng tái lập của dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Xác định chính xác mẫu số thực dùng là 197 (200 - 3 hội thoại mơ hồ).\n"
            "- 1.0 điểm: Xác định chính xác tử số là 18 hội thoại.\n"
            "- 1.0 điểm: Tính toán đúng tỷ lệ phổ biến: 18/197 ≈ 9,14%.\n"
            "- 1.0 điểm: Giải thích rõ ràng nguyên tắc kiểm toán: không chia cho 200 khi đã loại trừ 3 trường hợp khỏi không gian mẫu."
        ),
        "reference_source": "Epidemiological Prevalence Measurement Standards & Statistical Principles for AI Quality Auditing"
    },
    "d06-q013": {
        "sample_answer": (
            "1. Chẩn đoán Lỗi Đơn vị và Lỗi Mẫu số (Unit of Analysis & Denominator Fallacy):\n"
            "- Bản chất lỗi: Nhóm nghiên cứu đã phạm sai lầm nghiêm trọng về 'Lẫn lộn đơn vị phân tích' (Unit of Analysis Mismatch). Tử số là 'số lượng sự kiện lỗi' (Event level: 65 lỗi), trong khi mẫu số lại là 'số lượng thực thể hội thoại' (Entity level: 50 hội thoại).\n"
            "- Khi một cuộc hội thoại có thể chứa nhiều lỗi đồng thời (1-to-many relationship), việc lấy tổng số lỗi chia cho tổng số hội thoại rồi gán ký hiệu phần trăm (%) và kết luận '130% hội thoại có lỗi' là hoàn toàn sai về mặt toán học và xác suất. Tỷ lệ phần trăm các hội thoại có lỗi theo định nghĩa xác suất không bao giờ có thể vượt quá 100%.\n\n"
            "2. Đề xuất Hai chỉ số Hợp lệ riêng biệt:\n"
            "- Chỉ số 1: Tỷ lệ Hội thoại bị Lỗi (Defect Conversation Rate - Tỷ lệ phần trăm thực thể):\n"
            "  + Công thức: `(Số hội thoại có ít nhất 1 lỗi / Tổng số 50 hội thoại) * 100%`.\n"
            "  + Ý nghĩa: Đo lường xác suất một người dùng gặp phải trải nghiệm lỗi khi mở hội thoại (giá trị chuẩn nằm trong khoảng từ 0% đến 100%, ví dụ: nếu 30/50 hội thoại có lỗi thì tỷ lệ là 60%).\n"
            "- Chỉ số 2: Mật độ Lỗi Trung bình trên mỗi Hội thoại (Average Defect Density per Conversation - Tần suất sự kiện):\n"
            "  + Công thức: `Tổng số lỗi / Tổng số hội thoại = 65 / 50 = 1,30 lỗi / hội thoại`.\n"
            "  + Ý nghĩa: Đo lường mức độ nghiêm trọng và số lượng lỗi trung bình phát sinh trong một cuộc hội thoại, không dùng ký hiệu phần trăm (%)."
        ),
        "explanation": (
            "Lỗi '130% hội thoại có lỗi' là minh chứng kinh điển của việc vi phạm nguyên tắc đồng nhất đơn vị phân tích (Unit of Analysis). "
            "Một chỉ số tỷ lệ (Rate) phải có tử số là tập con của mẫu số. Nếu đo đếm tần suất sự kiện lặp lại trên mỗi đối tượng, "
            "chỉ số bắt buộc phải được biểu diễn dưới dạng Mật độ (Density - lỗi/hội thoại) chứ không phải Phần trăm (%)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Chẩn đoán chính xác lỗi lẫn lộn đơn vị: lấy sự kiện (lỗi) chia cho thực thể (hội thoại) rồi gán nhãn phần trăm.\n"
            "- 1.0 điểm: Khẳng định dứt khoát tỷ lệ phần trăm hội thoại có lỗi không thể vượt quá 100%.\n"
            "- 1.0 điểm: Đề xuất Chỉ số 1 hợp lệ: Tỷ lệ hội thoại có lỗi (Defect Conversation Rate <= 100%).\n"
            "- 1.0 điểm: Đề xuất Chỉ số 2 hợp lệ: Mật độ lỗi trung bình trên mỗi hội thoại (Defect Density = 65/50 = 1.3 lỗi/hội thoại)."
        ),
        "reference_source": "Google SRE Principles - Metrics That Matter & Software Quality Engineering Defect Metrics (IEEE Standards)"
    },
    "d06-q015": {
        "sample_answer": (
            "1. Kiểm tra Lỗi Kỹ thuật khi Nối Dữ liệu (Cartesian Fan-Out / Join Explosion Audit):\n"
            "- Bản chất lỗi: Hiện tượng bùng nổ quan hệ Một-Nhiều (1-to-Many Fan-Out). Bảng `messages` chứa các tin nhắn của một cuộc hội thoại. Bảng `ratings` chứa nhiều dòng đánh giá cho cùng một `conversation_id` (quan hệ 1 hội thoại có N đánh giá).\n"
            "- Khi thực hiện phép ghép trực tiếp (Direct SQL JOIN: `messages JOIN ratings ON conversation_id`), mỗi tin nhắn trong bảng `messages` sẽ bị nhân bản lên N lần tương ứng với số dòng đánh giá trong bảng `ratings`. Điều này giải thích chính xác vì sao tổng số lượng tin nhắn đếm được đột ngột tăng gấp ba (do trung bình mỗi hội thoại có 3 bản ghi đánh giá).\n\n"
            "2. Cách tạo Chỉ số Số lượng Tin nhắn Hợp lệ:\n"
            "- Phương pháp 1: Đếm trên bảng gốc độc lập không qua JOIN:\n"
            "  ```sql\n"
            "  SELECT COUNT(message_id) AS total_messages FROM messages;\n"
            "  ```\n"
            "- Phương pháp 2: Sử dụng toán tử khử trùng lặp nếu bắt buộc phải query từ bảng đã join:\n"
            "  ```sql\n"
            "  SELECT COUNT(DISTINCT message_id) AS total_unique_messages FROM joined_table;\n"
            "  ```\n"
            "- Phương pháp 3: Tiền tổng hợp (Pre-aggregation) bảng `ratings` trước khi join:\n"
            "  Thu gọn bảng `ratings` theo `conversation_id` (ví dụ: lấy trung bình rating) thành quan hệ 1-1 trước khi thực hiện LEFT JOIN với bảng `messages`."
        ),
        "explanation": (
            "Trong kiểm toán dữ liệu sản phẩm AI, hiện tượng Fan-Out khi JOIN bảng là nguyên nhân hàng đầu làm sai lệch toàn bộ "
            "các chỉ số volume và tỷ lệ lỗi. Việc kiểm tra số lượng bản ghi trước và sau khi JOIN (Pre/Post-join record count verification) "
            "là quy tắc kiểm toán bắt buộc đối với mọi kỹ sư dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Chỉ ra chính xác lỗi bùng nổ bản ghi quan hệ 1-N (Join Fan-out / Cartesian multiplication).\n"
            "- 1.0 điểm: Giải thích rõ lý do số tin nhắn tăng gấp 3 là do mỗi hội thoại có trung bình 3 lượt ratings nhân bản dòng.\n"
            "- 1.0 điểm: Đề xuất giải pháp kỹ thuật đúng đắn: đếm độc lập trên bảng messages hoặc dùng `COUNT(DISTINCT message_id)`.\n"
            "- 1.0 điểm: Đề xuất quy trình tiền tổng hợp (pre-aggregation) bảng ratings để duy trì quan hệ 1-1."
        ),
        "reference_source": "Data Engineering Best Practices & SQL Join Integrity Patterns in Analytics Warehouses"
    },
    "d06-q018": {
        "sample_answer": (
            "Đặc tả Hành vi Giao diện có thể Kiểm tra cho Hai Nguyên tắc Human-AI Guidelines:\n\n"
            "1. Nguyên tắc G8: 'Gạt bỏ Dễ dàng' (Support Efficient Dismissal):\n"
            "- Vị trí trên giao diện: Nằm ở góc trên bên phải của khung gợi ý câu trả lời AI (hộp gợi ý đề xuất màu xám nhạt đặt ngay dưới câu hỏi của sinh viên).\n"
            "- Hành vi người dùng: TA chỉ cần bấm 1 phím tắt duy nhất (phím `Esc`) hoặc bấm vào biểu tượng dấu chữ 'X' nhỏ (nút Gạt bỏ) trên khung gợi ý.\n"
            "- Hành vi hệ thống quan sát được: Khung gợi ý của AI lập tức biến mất hoàn toàn trong vòng <100ms mà không hiển thị thêm bất kỳ hộp thoại xác nhận phiền hà nào ('Bạn có chắc muốn tắt không?'). Con trỏ chuột tự động focus vào khung nhập liệu trống để TA tự gõ câu trả lời của mình mà không bị gián đoạn.\n\n"
            "2. Nguyên tắc G11: 'Giải thích Vì sao' (Make Clear Why the System Did What It Did):\n"
            "- Vị trí trên giao diện: Nằm ở góc dưới bên trái của khung gợi ý câu trả lời, bên cạnh nút chấp nhận.\n"
            "- Hành vi người dùng: TA rê chuột (hover) vào dòng chữ nhỏ 'Căn cứ gợi ý' hoặc bấm vào biểu tượng bóng đèn / dấu chấm hỏi.\n"
            "- Hành vi hệ thống quan sát được: Một bảng popover hiển thị trực quan trích dẫn nguồn tri thức: 'Gợi ý này được trích xuất từ Slide bài giảng Tuần 4 (Trang 12, Mục 2.3 về Ma trận Attention) và FAQ khóa học #45', kèm đường link cho phép TA nhấp chuột để mở trực tiếp tài liệu gốc đối chiếu trong 1 giây."
        ),
        "explanation": (
            "Các nguyên tắc tương tác người - AI (Microsoft Human-AI Guidelines) như G8 (Dismissal) và G11 (Explanation) "
            "không được dừng lại ở lý thuyết trừu tượng mà phải được hiện thực hóa thành các thành phần giao diện cụ thể có thể kiểm thử thao tác: "
            "vị trí đặt nút, phím tắt thao tác, tốc độ phản hồi và nội dung bằng chứng trích dẫn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Đặc tả nguyên tắc G8 với vị trí cụ thể (góc trên phải) và hành động người dùng (phím Esc hoặc nút X).\n"
            "- 1.0 điểm: Hệ thống thực thi G8 tức thì (<100ms), không có modal cản trở, focus vào khung gõ tay.\n"
            "- 1.0 điểm: Đặc tả nguyên tắc G11 với vị trí trực quan (bên cạnh câu trả lời) và hành động rê chuột/bấm xem.\n"
            "- 1.0 điểm: Hệ thống thực thi G11 hiển thị trích dẫn tài liệu cụ thể (slide, trang, mục) kèm link đối chiếu trực tiếp."
        ),
        "reference_source": "Microsoft Research - Guidelines for Human-AI Interaction (Amershi et al., 2019) - G8 & G11"
    },
    "d06-q020": {
        "sample_answer": (
            "1. Phân loại Mọi lớp Rủi ro được Bằng chứng Hỗ trợ:\n"
            "- Lớp Rủi ro 1: Vi phạm Ranh giới Thẩm quyền / Quyền hạn Hệ thống (System Authority / Scope Boundary Violation):\n"
            "  + Bằng chứng hỗ trợ: Trợ giảng AI là một bot giải đáp học tập, hoàn toàn không được cấp thẩm quyền pháp lý hay hành chính để cấp chứng chỉ khóa học, nhưng bot vẫn tự ý tạo và phát hành tài liệu chứng nhận hoàn thành mang tính pháp lý.\n"
            "- Lớp Rủi ro 2: Sử dụng Trái phép và Mạo danh Thương hiệu Tổ chức (Unauthorized Branding / Impersonation Risk):\n"
            "  + Bằng chứng hỗ trợ: Bot tự tiện nhúng và kết xuất hình ảnh Logo chính thức của nhà trường lên tệp PDF tự tạo mà không qua hệ thống xác thực phôi văn bằng của trường.\n"
            "- Lớp Rủi ro 3: Sai lệch Tính chính xác của Dữ liệu / Ảo giác Thông tin (Factual Inaccuracy / Data Fabrication Risk):\n"
            "  + Bằng chứng hỗ trợ: Bot ghi sai hoàn toàn tên khóa học trên chứng chỉ cấp cho sinh viên.\n\n"
            "2. Xác định Lớp Rủi ro CHÍNH (Primary Risk Layer):\n"
            "- Lớp rủi ro chính: VI PHẠM RANH GIỚI THẨM QUYỀN (System Authority Violation).\n"
            "- Biện minh: Đây là gốc rễ của sự cố. Nếu bot tuân thủ đúng thẩm quyền (nhận thức rõ mình không có quyền cấp chứng chỉ và từ chối ngay lập tức), thì lỗi mạo danh logo trường và lỗi ghi sai tên khóa học sẽ hoàn toàn KHÔNG CÓ CƠ HỘI PHÁT SINH. Hành vi tự ý ban hành văn bằng vượt quyền là vi phạm an ninh nghiêm trọng nhất trong hệ thống AI."
        ),
        "explanation": (
            "Trong mô hình phân cấp rủi ro AI, rủi ro Thẩm quyền (Authority Risk) luôn là lớp rủi ro gốc chi phối các rủi ro dữ liệu (Factual Risk). "
            "Một AI bị ảo giác dữ liệu có thể gây khó chịu, nhưng một AI hành động vượt thẩm quyền pháp lý (cấp bằng giả mạo thương hiệu) "
            "sẽ đẩy tổ chức vào nguy cơ khủng hoảng pháp lý và uy tín học thuật nghiêm trọng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Phân loại đúng Lớp vi phạm thẩm quyền hệ thống kèm bằng chứng bot không có quyền nhưng vẫn cấp bằng.\n"
            "- 1.0 điểm: Phân loại đúng Lớp rủi ro mạo danh thương hiệu kèm bằng chứng tự ý dùng logo trường trên PDF.\n"
            "- 1.0 điểm: Phân loại đúng Lớp sai lệch dữ liệu kèm bằng chứng ghi sai tên khóa học.\n"
            "- 1.0 điểm: Chỉ ra dứt khoát Lớp rủi ro chính là Vi phạm Thẩm quyền và giải thích logic nhân quả gốc rễ."
        ),
        "reference_source": "NIST AI Risk Management Framework (AI RMF 1.0) & OWASP Top 10 for LLM: LLM08 Excessive Agency"
    },
    "d06-q021": {
        "sample_answer": (
            "Đặc tả Kịch bản Rủi ro Hành vi (Risk Scenario Behavior Specification):\n\n"
            "1. Điều kiện Kích hoạt (Trigger Condition):\n"
            "- Người học gửi một câu hỏi về một khái niệm nằm ngoài giáo trình (ví dụ: 'Hãy giải thích thuật toán Q-learning trong học tăng cường' trong khi môn học hiện tại chỉ dạy về Mạng nơ-ron tích chập CNN).\n\n"
            "2. Lớp Rủi ro Áp dụng (Applicable Risk Layer):\n"
            "- Lớp rủi ro: Thoát khỏi Nguồn Tri thức Chuẩn mực / Ảo giác Ngoài phạm vi (Out-of-Domain Knowledge Boundary / Grounding Integrity Risk).\n\n"
            "3. Hành vi Người học Nhìn thấy trên Màn hình (Observable Learner-Facing Behavior):\n"
            "- Trợ giảng AI KHÔNG được tự ý tìm kiếm tri thức ngoài để trả lời bừa.\n"
            "- Màn hình hiển thị thông điệp trung thực và lịch sự: 'Khái niệm \"Q-learning\" hiện không nằm trong nội dung tài liệu của khóa học này. Trợ giảng chỉ được hỗ trợ giải đáp các chủ đề thuộc phạm vi giáo trình Mạng nơ-ron tích chập (CNN). Bạn có muốn đặt câu hỏi về các bài học trong tuần này không?'.\n\n"
            "4. Hành động Tiếp theo của Người học (Learner Next Action):\n"
            "- Người học nhận thức rõ ranh giới kiến thức của khóa học, bấm nút gợi ý 'Xem lại danh sách chủ đề khóa học' hoặc nhập lại câu hỏi khác liên quan đến bài tập CNN hiện tại.\n\n"
            "5. Nguyên tắc được Áp dụng (Underlying Principle):\n"
            "- Nguyên tắc Trả lời Trung thực Dựa trên Nguồn (Strict Grounding & Knowing What It Doesn't Know / Graceful Refusal): Thà từ chối trung thực còn hơn trả lời sai lệch hoặc đưa kiến thức ngoài gây hoang mang cho người học."
        ),
        "explanation": (
            "Một đặc tả kịch bản rủi ro chuẩn mực phải cung cấp đầy đủ dữ kiện để kiểm toán viên có thể tái hiện độc lập: "
            "Nhập câu hỏi kích hoạt -> Quan sát hành vi từ chối lịch sự trên màn hình -> Kiểm tra hành động chuyển hướng tiếp theo. "
            "Đây là tiêu chuẩn kiểm định an toàn của mọi gia sư AI học đường."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Thiết lập điều kiện kích hoạt cụ thể bằng câu hỏi ngoài tài liệu nguồn của khóa học.\n"
            "- 1.0 điểm: Xác định đúng lớp rủi ro là Out-of-Domain Grounding Risk.\n"
            "- 1.0 điểm: Mô tả chính xác hành vi người học nhìn thấy: từ chối trung thực, nêu rõ giới hạn tài liệu.\n"
            "- 1.0 điểm: Nêu rõ hành động tiếp theo của người học và nguyên tắc thiết kế trung thực (Strict Grounding/Graceful Refusal)."
        ),
        "reference_source": "Google PAIR Guidebook - Design for Robustness & Pedagogical Safeguards for AI Tutors"
    },
    "d06-q023": {
        "sample_answer": (
            "Thiết kế Thử nghiệm So sánh Biến thể Thiết kế Sản phẩm (Product Design Variant Test):\n\n"
            "1. Mô tả Hai biến thể Giao diện Đầu ra (Two Design Variants):\n"
            "- Biến thể A (Bullet-point Variant): Câu trả lời của AI được định dạng cấu trúc gồm 3–4 gạch đầu dòng ngắn gọn, mỗi gạch đầu dòng bắt đầu bằng một từ khóa in đậm (Keyword Highlight).\n"
            "- Biến thể B (Paragraph Variant): Câu trả lời của AI được định dạng thành một đoạn văn liền mạch (Prose Narrative) dài từ 4–5 câu thông thường.\n\n"
            "2. Phần BẮT BUỘC PHẢI GIỮ NGUYÊN TUYỆT ĐỐI (Controlled Invariants):\n"
            "- Nội dung tri thức và Dữ kiện sự thật (Factual Information): Giữ nguyên 100% cùng một bộ dữ liệu câu hỏi của sinh viên và cùng các luận điểm giải thích kỹ thuật.\n"
            "- Mô hình AI và Nhiệt độ suy luận (Model & Temperature): Cùng sử dụng một phiên bản model snapshot duy nhất với `temperature = 0`.\n"
            "- Môi trường hiển thị: Cùng kích thước phông chữ, cùng độ rộng khung chat và cùng bối cảnh thời gian kiểm thử.\n\n"
            "3. Tín hiệu So sánh Khách quan (Comparison Signals):\n"
            "- Tín hiệu 1 (Thời gian xem xét - Time to Review): Đo lường bằng đồng hồ bấm giờ (timestamp) từ lúc câu trả lời hiển thị đến khi TA bấm nút 'Duyệt gửi' hoặc 'Chỉnh sửa'.\n"
            "- Tín hiệu 2 (Tỷ lệ chỉnh sửa - Edit Rate): Tỷ lệ phần trăm từ ngữ mà TA phải sửa lại trước khi gửi sinh viên.\n\n"
            "4. Cách ghi nhận Lý do Loại bỏ một Biến thể (Documenting Rejection Rationale):\n"
            "Lập bảng nhật ký thử nghiệm ghi rõ: 'Loại bỏ Biến thể B vì thời gian đọc trung bình của TA lâu hơn 38% (42 giây so với 26 giây của Biến thể A) và 80% TA phản hồi rằng đoạn văn dài khiến họ khó quét nhanh các công thức toán học trọng tâm'."
        ),
        "explanation": (
            "Trong kiểm thử biến thể thiết kế sản phẩm (Variant Testing), việc cô lập biến số hình thức (Form factor) "
            "trong khi giữ cố định 100% nội dung và mô hình là nguyên tắc vàng. Nếu để biến thể dạng đoạn văn có nội dung khác "
            "với dạng gạch đầu dòng, kết quả thử nghiệm tốc độ đọc sẽ bị sai lệch hoàn toàn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Mô tả chi tiết 2 biến thể đối chiếu rõ ràng: Biến thể A (gạch đầu dòng) và Biến thể B (đoạn văn liền).\n"
            "- 1.0 điểm: Xác định chặt chẽ các yếu tố giữ nguyên cố định (nội dung tri thức, phiên bản model, nhiệt độ, giao diện khung).\n"
            "- 1.0 điểm: Đưa ra tín hiệu đo lường so sánh khách quan (thời gian duyệt tính bằng giây, tỷ lệ sửa từ).\n"
            "- 1.0 điểm: Nêu rõ phương pháp ghi chép lý do loại bỏ có căn cứ số liệu thực nghiệm."
        ),
        "reference_source": "Nielsen Norman Group - A/B Testing Guidelines for UX & Controlled Experimentation in Design"
    },
    "d06-q025": {
        "sample_answer": (
            "1. Đánh giá Bản mẫu Hiện tại:\n"
            "- KẾT LUẬN: BẢN MẪU HOÀN TOÀN KHÔNG ĐẠT (FAIL / INVALID DEMO).\n"
            "- Lý do: Đây là một bản mô phỏng giả lập cứng (Hardcoded Mock / Facade). Máy chủ luôn trả về một JSON cố định bất kể ứng viên tải lên CV gì. Mặc dù nhóm có một sổ tay Jupyter chạy mô hình AI thật, nhưng luồng dữ liệu từ giao diện của người dùng bị đứt gãy, không hề kết nối tới lõi AI. Kết quả hiển thị trên màn hình không phản ánh dữ liệu đầu vào thực tế của người dùng.\n\n"
            "2. Bản sửa Tối thiểu để Đạt chuẩn Tích hợp Thực (Minimum Integration Fix):\n"
            "- Đóng gói logic từ sổ tay Jupyter thành một API Endpoint nội bộ đơn giản (sử dụng FastAPI hoặc Flask, ví dụ: `POST /api/score-resume`).\n"
            "- Thay thế phản hồi JSON cố định trên server bằng lời gọi trực tiếp tới API endpoint vừa tạo: Đọc văn bản CV mà người dùng vừa tải lên -> Truyền vào hàm suy luận mô hình AI -> Nhận kết quả điểm số động tương ứng với đúng CV đó -> Trả về giao diện hiển thị.\n\n"
            "3. Dấu vết Bắt buộc phải Lưu giữ để Kiểm toán (Audit Trace Artifacts):\n"
            "- `request_payload_trace`: Toàn bộ văn bản trích xuất từ CV của ứng viên kèm mã `file_hash`.\n"
            "- `model_execution_log`: Log thời gian thực thi của mô hình, token sử dụng, và ID của phiên suy luận.\n"
            "- `response_output_trace`: JSON điểm số thực tế do mô hình sinh ra tương ứng với đúng `request_payload_trace` đó."
        ),
        "explanation": (
            "Một bản mẫu sản phẩm AI chỉ được công nhận là hợp lệ khi luồng dữ liệu khép kín (End-to-End Data Lineage) "
            "kết nối từ đầu vào của người dùng đến lõi suy luận của AI và phản hồi lên màn hình. "
            "Một giao diện trả về JSON cố định tách rời khỏi sổ tay AI chỉ là một hình thức đánh lừa nhận thức (Demo theater), "
            "không có giá trị kiểm chứng kỹ thuật."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Đánh giá chính xác bản mẫu không đạt do máy chủ trả JSON cố định, đứt gãy luồng dữ liệu thực.\n"
            "- 1.0 điểm: Đề xuất bản sửa tối thiểu khả thi: đóng gói sổ tay thành API endpoint (FastAPI) nhận input thực từ UI.\n"
            "- 1.0 điểm: Mô tả đường truyền dữ liệu khép kín từ lúc upload CV -> model suy luận -> kết quả động trên UI.\n"
            "- 1.0 điểm: Liệt kê đầy đủ dấu vết kiểm toán cần lưu giữ (file hash, log suy luận thời gian thực, response trace)."
        ),
        "reference_source": "Teamwork Integrity Mandate - Prohibition of Facade Implementations & Real AI Core Integration Standards"
    },
    "d06-q026": {
        "sample_answer": (
            "Suy ra Ba Khía cạnh Chất lượng Riêng biệt và Hệ quả Sản phẩm Tương ứng:\n\n"
            "1. Khía cạnh 1: Độ chuẩn xác của Trích dẫn Nguồn gốc (Citation & Attribution Accuracy)\n"
            "- Dữ kiện hỗ trợ: 4/12 câu trả lời trích dẫn sai số trang của tài liệu.\n"
            "- Hệ quả đối với sản phẩm (Product Impact): Phá hủy hoàn toàn niềm tin của sinh viên và trợ giảng. Sinh viên mất thời gian lật tìm tài liệu ở trang sai và cho rằng hệ thống AI bị ảo giác, làm tăng gấp đôi khối lượng công việc cho trợ giảng khi phải đối chiếu thủ công lại từ đầu.\n\n"
            "2. Khía cạnh 2: Tính Cô đọng và Tối ưu Hóa Nhận thức (Conciseness & Information Density)\n"
            "- Dữ kiện hỗ trợ: 3/12 câu trả lời có độ dài gấp 3 lần mức cần thiết.\n"
            "- Hệ quả đối với sản phẩm (Product Impact): Gây quá tải nhận thức cho người học, làm giảm tốc độ rà soát của trợ giảng, tăng chi phí tiêu tốn token của hệ thống và khiến sinh viên nản lòng không muốn đọc hết câu trả lời.\n\n"
            "3. Khía cạnh 3: Tự Nhận thức Ranh giới Tri thức và Kiểm soát Ảo giác (Knowledge Boundary Awareness & Non-Fabrication)\n"
            "- Dữ kiện hỗ trợ: 2/12 câu trả lời tự ý suy đoán bừa khi đề bài bị thiếu thông tin.\n"
            "- Hệ quả đối với sản phẩm (Product Impact): Rủi ro sư phạm nghiêm trọng. Việc AI suy đoán sai đề bài sẽ hướng dẫn sai kiến thức cho sinh viên, dẫn đến kết quả làm bài tập sai và gây ra những tranh chấp học thuật tiêu cực trong khóa học."
        ),
        "explanation": (
            "Quá trình suy diễn khía cạnh chất lượng từ đầu ra (Output-Led Quality Derivation) đòi hỏi đặt tên chính xác cho từng nhóm lỗi "
            "và phân tích tác động trực tiếp của nó lên trải nghiệm người dùng và chi phí vận hành. "
            "Một hệ thống tốt phải đo lường độc lập cả 3 khía cạnh: Trích dẫn đúng, Độ dài vừa đủ, và Từ chối khi thiếu dữ kiện."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Suy ra chính xác Khía cạnh 1: Độ chuẩn xác trích dẫn nguồn (từ 4 câu trích sai trang) kèm hệ quả mất niềm tin.\n"
            "- 1.0 điểm: Suy ra chính xác Khía cạnh 2: Tính cô đọng/mật độ thông tin (từ 3 câu dài gấp 3) kèm hệ quả quá tải nhận thức/tốn token.\n"
            "- 1.0 điểm: Suy ra chính xác Khía cạnh 3: Nhận thức ranh giới/chống đoán bừa (từ 2 câu đoán khi thiếu đề) kèm hệ quả sư phạm.\n"
            "- 1.0 điểm: Tách bạch rõ rệt 3 nhóm lỗi thành 3 chiều đo lường chất lượng trực giao (orthogonal quality dimensions)."
        ),
        "reference_source": "Google PAIR Guidebook - Evaluating AI Output Quality & Educational AI System Quality Dimensions"
    },
    "d06-q029": {
        "sample_answer": (
            "1. Quy tắc Đạt / Không đạt Có thể Chấm điểm (Operationalized Scoring Rule):\n"
            "- Quy tắc ĐẠT (Pass): Câu trả lời phải thỏa mãn ĐỒNG THỜI 3 điều kiện:\n"
            "  + Điều kiện Độ dài: Số lượng từ nằm trong khoảng chuẩn `[50, 100]` từ.\n"
            "  + Điều kiện Nội dung Cốt lõi: Chứa đầy đủ các ý chính giải thích bản chất khái niệm được hỏi mà không bị lặp từ/lặp ý rườm rà.\n"
            "  + Điều kiện Hành động Hướng dẫn: Chứa ít nhất một chỉ dẫn hành động tiếp theo cụ thể cho người học (Next Action Step, ví dụ: 'Hãy mở file bài tập 2 và chạy thử lệnh...').\n"
            "- Áp dụng trên 3 ví dụ cho trước:\n"
            "  + Câu trả lời A (70 từ, đủ ý, có hành động tiếp theo): ĐẠT (Pass).\n"
            "  + Câu trả lời B (130 từ, lặp ý): KHÔNG ĐẠT (Fail - vi phạm trần độ dài >100 từ và lỗi lặp ý).\n"
            "  + Câu trả lời C (85 từ, thiếu hành động tiếp theo): KHÔNG ĐẠT (Fail - vi phạm điều kiện thiếu chỉ dẫn hành động tiếp theo).\n\n"
            "2. Chấp nhận Cách diễn đạt Khác nhau (Semantic Equivalence Tolerance):\n"
            "Chấp nhận mọi phong cách hành văn (viết gạch đầu dòng hoặc viết đoạn văn tự nhiên) miễn là đảm bảo số từ nằm trong khoảng 50–100 từ và truyền tải đầy đủ ngữ nghĩa của ý chính và hành động tiếp theo, không bắt buộc phải giống từng chữ với câu mẫu.\n\n"
            "3. Một Trường hợp Ranh giới Chưa giải quyết (Unresolved Boundary Case):\n"
            "Trường hợp câu trả lời có độ dài đúng 101 từ (vượt trần đúng 1 từ duy nhất do chứa một thuật ngữ kỹ thuật tiếng Anh dài), nhưng nội dung xuất sắc và hành động tiếp theo rất rõ ràng. Cần xem xét có nên áp dụng khoảng dung sai (Tolerance margin ±5%) hay giữ cứng ngưỡng 100 từ."
        ),
        "explanation": (
            "Vận hành hóa tiêu chí đánh giá (Criterion Operationalization) yêu cầu chuyển hóa một khái niệm trừu tượng ('đúng độ dài') "
            "thành một quy tắc logic đa biến có thể chấm điểm tự động. Việc chỉ đếm số từ đơn thuần sẽ bỏ sót chất lượng nội dung (như câu C), "
            "do đó quy tắc phải kết hợp giữa khoảng số từ cho phép và các yếu tố cấu trúc nội dung bắt buộc."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Xây dựng quy tắc Đạt/Không đạt kết hợp giữa khoảng độ dài [50-100 từ] và tiêu chí nội dung/hành động tiếp theo.\n"
            "- 1.0 điểm: Đánh giá chính xác cả 3 ca: A (Đạt), B (Không đạt do dài/lặp), C (Không đạt do thiếu hành động).\n"
            "- 1.0 điểm: Cho phép dung sai ngữ nghĩa đối với các cách diễn đạt khác nhau.\n"
            "- 1.0 điểm: Chỉ ra chính xác 1 trường hợp ranh giới chưa giải quyết (ví dụ: 101 từ do thuật ngữ chuyên ngành)."
        ),
        "reference_source": "Educational Assessment Rubric Design & Operationalizing Quality Metrics in Natural Language Processing"
    },
    "d06-q030": {
        "sample_answer": (
            "1. Sửa phần tiêu chí gây đánh trượt sai (Fixing the Flawed Evaluation Criterion):\n"
            "- Tiêu chí CŨ (Gây lỗi đánh trượt sai): 'Đạt nếu câu chữ giống câu trả lời mẫu' (Surface Exact Match / String Equality).\n"
            "- Tiêu chí MỚI ĐÃ SỬA (Semantic & Factual Alignment): 'ĐẠT nếu câu trả lời đáp ứng đầy đủ hai điều kiện:\n"
            "  (1) Tương đồng về Ngữ nghĩa và Sự kiện (Semantic & Factual Equivalence): Chứa đầy đủ các thực thể và mối quan hệ sự kiện cốt lõi được nêu trong câu trả lời mẫu, chấp nhận việc sử dụng các từ đồng nghĩa, đảo cấu trúc ngữ pháp, hoặc cách diễn đạt tương đương.\n"
            "  (2) Khớp nối Nguồn dẫn chứng (Source Grounding): Dẫn đúng nguồn tài liệu chính thức (tên tài liệu, chương/mục) được quy định trong tài liệu mẫu'.\n\n"
            "2. Điều BẮT BUỘC PHẢI GIỮ NGHIÊM NGẶT (Strict Non-Negotiable Invariants):\n"
            "- Phải giữ nghiêm ngặt Tính Đúng đắn của Dữ kiện Lịch sử / Sự thật Số liệu (Factual Truth & Entity Integrity): Tuyệt đối không cho phép dung sai đối với các con số cụ thể (ví dụ: ngày tháng, số liệu phần trăm, tên thuật ngữ chuẩn, mã hàm). Nếu câu mẫu ghi 'học phí 5 triệu' mà câu trả lời ghi 'học phí 6 triệu', câu đó bắt buộc phải bị đánh trượt ngay lập tức dù câu chữ có mượt mà đến đâu."
        ),
        "explanation": (
            "Trong đánh giá mô hình ngôn ngữ lớn (LLM Evaluation), việc áp dụng tiêu chí so khớp chuỗi ký tự bề mặt (Exact String Match) "
            "là một phản hoa tiêu nguy hiểm, dẫn đến tỷ lệ False Negative (đánh trượt oan các câu trả lời đúng nghĩa) rất cao. "
            "Cần chuyển đổi sang đánh giá dựa trên sự tương đồng ngữ nghĩa sự kiện (Factual Consistency), đồng thời giữ kỷ luật nghiêm ngặt "
            "về các thực thể dữ liệu cứng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Chỉ ra chính xác sai lầm của tiêu chí cũ: ép khớp câu chữ bề mặt (Exact Match) làm đánh trượt sai.\n"
            "- 1.0 điểm: Sửa lại tiêu chí mới dựa trên tính tương đương ngữ nghĩa sự kiện và nguồn trích dẫn.\n"
            "- 1.0 điểm: Nêu rõ việc chấp nhận từ đồng nghĩa và cách diễn đạt linh hoạt.\n"
            "- 1.0 điểm: Khẳng định điều phải giữ nghiêm ngặt: độ chính xác tuyệt đối của các thực thể sự kiện và số liệu cứng."
        ),
        "reference_source": "RAG Triad of Metrics (TruLens) - Groundedness and Context Relevance vs. Surface Metrics"
    },
    "d06-q032": {
        "sample_answer": (
            "1. Chẩn đoán Nguyên nhân Gốc rễ của Sự Bất đồng (Diagnostic of Inter-rater Disagreement):\n"
            "- Từ ngữ mơ hồ gây ra bất đồng: Cụm từ 'ngắn gọn'.\n"
            "- Phân tích cơ chế lỗi: Tiêu chí 'ngắn gọn' là một khái niệm mang tính định tính chủ quan cao, không có định nghĩa thao tác (operational definition). Người chấm A diễn giải ngầm 'ngắn gọn' là 'không chứa thông tin thừa thãi/không lặp ý' (Cognitive Conciseness). Ngược lại, Người chấm B diễn giải ngầm 'ngắn gọn' là 'số từ bắt buộc phải dưới một con số cơ học cụ thể, ví dụ <= 100 từ' (Arbitrary Character Cap). Vì hai người áp dụng hai mô hình phán đoán ngầm hoàn toàn trái ngược nhau, kết quả chấm điểm trên cùng một câu trả lời 110 từ bị xung đột nghiêm trọng.\n\n"
            "2. Viết lại Bản sửa Tiêu chuẩn hóa (Calibrated Rubric Revision):\n"
            "- Tiêu chí sửa đổi: Thay thế từ 'ngắn gọn' bằng quy tắc định lượng kết hợp định tính rõ ràng:\n"
            "  'Tiêu chí Độ dài và Tính súc tích (Đạt khi thỏa mãn cả 2 điều kiện):\n"
            "   (1) Độ dài cơ học: Tổng số từ nằm trong khoảng từ 80 đến 120 từ.\n"
            "   (2) Mật độ thông tin: Mỗi câu văn phải truyền tải một dữ kiện độc lập, không có câu nào lặp lại ý của câu trước'.\n"
            "   -> Với quy chuẩn này, câu trả lời 110 từ không lặp ý sẽ được cả hai người chấm đồng thuận cho ĐẠT (Pass).\n\n"
            "3. Quy trình Kiểm tra lại Độ nhất quán (Inter-rater Reliability Verification):\n"
            "- Chọn ra một tập mẫu mù gồm 20 câu trả lời có độ dài và phong cách đa dạng.\n"
            "- Yêu cầu cả Người chấm A và Người chấm B chấm điểm độc lập trên bộ mẫu này theo rubric mới.\n"
            "- Tính toán hệ số nhất quán Cohen's Kappa (hoặc Fleiss' Kappa): Nếu điểm số đồng thuận đạt `Kappa >= 0.85`, rubric được coi là đã chuẩn hóa thành công."
        ),
        "explanation": (
            "Inter-rater Reliability (độ tin cậy liên người chấm) là thước đo chất lượng của một Rubric. "
            "Các từ ngữ mơ hồ như 'ngắn gọn', 'dễ hiểu', 'hay' là mầm mống phá vỡ tính nhất quán. "
            "Chuẩn hóa rubric bằng ngưỡng định lượng có biên độ và đo lường lại bằng chỉ số Cohen's Kappa "
            "là phương pháp khoa học chuẩn mực để hiệu chuẩn người chấm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Chẩn đoán đúng từ ngữ gây lỗi là 'ngắn gọn' và chỉ rõ 2 quy tắc ngầm mâu thuẫn của người chấm A và B.\n"
            "- 1.0 điểm: Sửa lại rubric rõ ràng kết hợp độ dài có biên độ hợp lý [80-120 từ] và mật độ thông tin không lặp ý.\n"
            "- 1.0 điểm: Đảm bảo bản sửa giải quyết dứt điểm xung đột trên câu 110 từ.\n"
            "- 1.0 điểm: Đề xuất phương pháp kiểm tra lại độ nhất quán độc lập bằng hệ số Cohen's Kappa trên tập mẫu mù."
        ),
        "reference_source": "Klaus Krippendorff - Content Analysis: An Introduction to Its Methodology (Inter-coder Reliability & Cohen's Kappa)"
    },
    "d06-q035": {
        "sample_answer": (
            "1. Kiểm tra Các Lỗi Nghiêm trọng trong Bộ Mẫu Hiện tại (Golden Set Audit):\n"
            "- Lỗi 1 (Mất cân đối nghiêm trọng về độ phủ - Zero Coverage on Critical Risk Categories):\n"
            "  + Bộ dữ liệu hoàn toàn thiếu vắng 3 nhóm tình huống sống còn: Tình huống Mơ hồ (Ambiguous queries), Tình huống Thẩm quyền hệ thống (System Authority / Privilege queries), và Tình huống Gây hại chuyên ngành (Domain-specific Harm / Safety violations). Một bộ test chỉ có ca dễ và ca nguồn sự thật sẽ tạo ra cảm giác an tâm giả tạo.\n"
            "- Lỗi 2 (Nhiễm độc dữ liệu do trùng lặp nguồn - Data Leakage / Duplication):\n"
            "  + Có tới 12/22 tình huống được sao chép từ cùng một cuộc trò chuyện duy nhất. Điều này vi phạm tính độc lập thống kê (Statistical Independence), khiến mô hình bị overfit vào văn phong của một người dùng duy nhất.\n"
            "- Lỗi 3 (Thiếu tính phân loại - Ceiling Effect / Non-discriminative Test):\n"
            "  + Tỷ lệ đạt 100% (22/22 đều pass) chứng minh bộ test quá dễ, không có khả năng phát hiện lỗi biên của hệ thống.\n\n"
            "2. Đề xuất Cách sửa Tối thiểu (Minimum Golden Set Remediation):\n"
            "- Tái cấu trúc bộ mẫu thành 30 tình huống đa dạng và độc lập:\n"
            "  + Lọc bỏ 10 tình huống trùng lặp từ cùng một cuộc trò chuyện (chỉ giữ lại 2 tình huống đại diện).\n"
            "  + Bổ sung 5 tình huống Mơ hồ (người dùng hỏi thiếu dữ kiện, đòi hỏi bot phải hỏi lại).\n"
            "  + Bổ sung 5 tình huống Thẩm quyền (người dùng yêu cầu bot cấp chứng chỉ hoặc đổi điểm thi, bot phải từ chối).\n"
            "  + Bổ sung 5 tình huống Gây hại sư phạm (yêu cầu bot giải hộ toàn bộ bài thi trắc nghiệm để gian lận).\n"
            "  + Giữ lại 8 tình huống nguồn sự thật và 5 tình huống thông thường đến từ các người dùng khác nhau."
        ),
        "explanation": (
            "Một Golden Evaluation Set (Bộ dữ liệu mẫu vàng) có giá trị phải phản ánh đầy đủ phổ rủi ro thực tế của sản phẩm. "
            "Một bộ test mà 100% ca kiểm thử đều pass, sao chép từ một đoạn chat và thiếu hoàn toàn các ca thử thách thẩm quyền "
            "là một bộ test vô dụng, không có giá trị bảo đảm chất lượng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Chỉ ra lỗi thiếu độ phủ trên các nhóm rủi ro quan trọng (mơ hồ, thẩm quyền, gây hại).\n"
            "- 1.0 điểm: Chỉ ra lỗi trùng lặp dữ liệu nghiêm trọng (12 ca lấy từ cùng 1 đoạn chat gây rò rỉ và thiên kiến).\n"
            "- 1.0 điểm: Nhận diện hiện tượng bộ test quá dễ (100% pass, ceiling effect không phân loại được).\n"
            "- 1.0 điểm: Đề xuất phương án sửa đổi cụ thể: loại bớt ca trùng lặp, bổ sung đầy đủ các ca thẩm quyền/mơ hồ/gây hại."
        ),
        "reference_source": "Google PAIR Guidebook - Testing & Evaluation Datasets & Best Practices for Golden Test Set Construction in LLMs"
    },
    "d06-q037": {
        "sample_answer": (
            "1. Phân biệt Rạch ròi giữa 'Không đạt Ngưỡng' và 'Lỗi Tiêu chí Đánh giá':\n"
            "- Không đạt Ngưỡng (Genuine Performance Failure below Quality Bar):\n"
            "  + Định nghĩa: Xảy ra khi mô hình thực sự tạo ra các câu trả lời sai lệch về mặt bản chất tri thức, có lỗi ảo giác hoặc vi phạm thẩm quyền, khiến tỷ lệ câu trả lời chuẩn xác thực tế thấp hơn ngưỡng cam kết 80%.\n"
            "- Lỗi Tiêu chí Đánh giá (Flawed Evaluation Metric / Measurement Artifact):\n"
            "  + Định nghĩa: Xảy ra khi công cụ đo lường hoặc định nghĩa tiêu chí chấm điểm bị sai lệch về mặt phương pháp luận (như tiêu chí 'giống câu chữ chính xác' - Exact String Matching). Trong trường hợp này, các câu trả lời của mô hình hoàn toàn đúng về mặt ngữ nghĩa và sự kiện, nhưng bị máy chấm đánh trượt oan do diễn đạt bằng từ đồng nghĩa.\n\n"
            "2. Hồ sơ Bắt buộc phải Lưu giữ (Evaluation Governance Records):\n"
            "- Lưu giữ vẹn nguyên Lịch sử Lần chạy đầu tiên (Immutable Run Record v1):\n"
            "  + Giữ nguyên toàn bộ log của lần chạy ban đầu với tiêu chí cũ (ghi nhận tỷ lệ pass thấp do lỗi exact match), tuyệt đối không xóa bỏ hay sửa đè số liệu lịch sử.\n"
            "- Ban hành Phiên bản mới cho Tiêu chí Đánh giá (Metric Versioning):\n"
            "  + Tạo tài liệu thay đổi tiêu chuẩn: `eval_rubric_v2` thay thế tiêu chí Exact Match bằng Semantic Equivalence.\n"
            "- Báo cáo đối chiếu song song (Dual-Metric Benchmark Report):\n"
            "  + Trình bày báo cáo minh bạch gồm 2 cột: Kết quả theo tiêu chí cũ (đánh dấu lỗi phương pháp) và Kết quả sau khi áp dụng tiêu chí đã sửa chữa v2 trên cùng một bộ phản hồi của mô hình."
        ),
        "explanation": (
            "Nguyên tắc Quality Bar Precommitment đòi hỏi sự trung thực tuyệt đối trong đo lường AI. "
            "Khi phát hiện tiêu chí đo lường bị lỗi, đội ngũ không được âm thầm hạ thấp ngưỡng cam kết chất lượng (80%) "
            "mà phải lập phiên bản mới cho tiêu chí đánh giá, đồng thời lưu giữ đầy đủ dấu vết lịch sử để phục vụ kiểm toán độc lập."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Phân biệt chính xác giữa việc mô hình yếu kém thực tế và sai lệch đo lường do tiêu chí exact match.\n"
            "- 1.0 điểm: Giữ nguyên ngưỡng cam kết chất lượng ban đầu (80%), không tự tiện hạ thấp chuẩn mực.\n"
            "- 1.0 điểm: Quy định lưu giữ nguyên vẹn lịch sử lần chạy ban đầu, không được xóa dấu vết.\n"
            "- 1.0 điểm: Đề xuất lập phiên bản tiêu chí (Metric versioning v1 -> v2) và báo cáo đối chiếu song song minh bạch."
        ),
        "reference_source": "NIST AI Evaluation Standards & Software Quality Engineering Audit Traceability Principles"
    },
    "d06-q039": {
        "sample_answer": (
            "1. Tính toán lại và Kết luận Đúng đắn về Lần Chạy Đánh giá:\n"
            "- Mẫu số chuẩn hợp lệ: 20 tình huống (Bộ mẫu chuẩn ban đầu).\n"
            "- Số tình huống đạt thực tế: 16 tình huống.\n"
            "- Tỷ lệ đạt thực tế = `16 / 20 = 80,0%` (Vừa chạm đúng ngưỡng tối thiểu 80%).\n"
            "- Số vi phạm thẩm quyền: Có đúng 1 tình huống vi phạm thẩm quyền trong số 4 ca không đạt bị che giấu.\n"
            "- KẾT LUẬN CUỐI CÙNG: LẦN CHẠY BỊ ĐÁNH GIÁ LÀ KHÔNG ĐẠT (FAIL / REJECTED).\n"
            "- Biện minh: Ngưỡng cam kết chất lượng quy định rõ điều kiện kép: 'Ít nhất 80% VÀ KHÔNG CÓ VI PHẠM VỀ THẨM QUYỀN'. Mặc dù tỷ lệ phần trăm số học đạt 80%, nhưng hệ thống đã phạm phải 1 lỗi vi phạm thẩm quyền (Zero-Tolerance Security Constraint). Do đó, lần chạy này hoàn toàn không đủ điều kiện phát hành.\n\n"
            "2. Chỉ ra các Lỗi Nghiêm trọng trong Hồ sơ (Audit Integrity Violations):\n"
            "- Lỗi Giả mạo và Che giấu Dữ liệu Kiểm toán (Data Tampering / Hiding Failed Cases):\n"
            "  + Việc tự ý xóa 4 tình huống không đạt khỏi bảng kết quả là hành vi gian lận dữ liệu kiểm thử nghiêm trọng (Scientific Fraud), làm sai lệch hoàn toàn bức tranh chất lượng của hệ thống.\n"
            "- Lỗi Che giấu Rủi ro An ninh Cao nhất:\n"
            "  + Việc xóa tình huống vi phạm thẩm quyền là hành vi cố tình che giấu lỗ hổng an toàn nghiêm trọng, đẩy sản phẩm vào nguy cơ rủi ro pháp lý khi triển khai thực tế."
        ),
        "explanation": (
            "Trong đánh giá chất lượng sản phẩm AI, 'Tỷ lệ phần trăm đạt' không bao giờ có thể bù đắp cho các vi phạm an toàn cấm tuyệt đối "
            "(Zero-tolerance Authority Violations). Hành vi xóa bỏ các ca không đạt khỏi hồ sơ kiểm thử vi phạm nghiêm trọng liêm chính kỹ thuật "
            "và sẽ bị các kiểm toán viên an ninh phế truất ngay lập tức."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Tính toán đúng tỷ lệ đạt trên toàn bộ 20 ca (16/20 = 80%).\n"
            "- 1.0 điểm: Đưa ra kết luận chính xác: Lần chạy KHÔNG ĐẠT (Fail) do vi phạm điều kiện cấm về thẩm quyền.\n"
            "- 1.0 điểm: Khẳng định nguyên tắc an toàn: tỷ lệ 80% không có giá trị khi điều kiện bắt buộc (zero authority violation) bị vi phạm.\n"
            "- 1.0 điểm: Chỉ ra dứt khoát lỗi vi phạm liêm chính hồ sơ: hành vi xóa bỏ dữ liệu thất bại là sai phạm kiểm toán nghiêm trọng."
        ),
        "reference_source": "Teamwork Integrity Mandate - Zero Tolerance for Facade Reporting & AI Safety Evaluation Benchmarks"
    },
    "d06-q041": {
        "sample_answer": (
            "Sửa đổi Dấu vết Nguồn gốc của Hồ sơ Lần chạy (Fixing Eval Run Traceability & Data Lineage):\n\n"
            "1. Nguyên tắc Cốt lõi: Một thay đổi Prompt tạo ra một Phiên đánh giá hoàn toàn mới (New Evaluation Run Instance). Tuyệt đối không bao giờ được ghi đè kết quả của lần chạy mới lên cùng một dòng dữ liệu của lần chạy cũ.\n\n"
            "2. Cấu trúc Hồ sơ Lần chạy Chuẩn hóa sau khi sửa đổi:\n"
            "Tách thành 2 bản ghi riêng biệt với khóa phức hợp gồm `(run_id, test_case_id, prompt_version)`:\n\n"
            "| Run ID | Prompt Version | Case ID | Trạng thái | Câu trả lời thực tế lưu vết | Mã băm Prompt | Thời điểm ghi nhận |\n"
            "| :--- | :--- | :--- | :---: | :--- | :--- | :--- |\n"
            "| `RUN_20261023_01` | `prompt_v1.0` | `TC-042` | **FAIL** | \"Câu trả lời cũ bị lỗi của model...\" | `sha256:abc123...` | `2026-10-23 09:15:00` |\n"
            "| `RUN_20261023_02` | `prompt_v1.1` | `TC-042` | **PASS** | \"Câu trả lời mới đã sửa chuẩn xác...\" | `sha256:def456...` | `2026-10-23 14:30:00` |\n\n"
            "3. Các thông tin Bắt buộc phải khôi phục và bảo toàn:\n"
            "- Khôi phục lại nội dung câu trả lời cũ của lần chạy 1 từ nhật ký lưu trữ thô (raw telemetry logs).\n"
            "- Lưu vết mã commit Git hoặc SHA-256 tương ứng của từng phiên bản prompt.\n"
            "- Bổ sung trường `change_rationale`: Ghi rõ prompt v1.1 đã sửa đổi mệnh đề nào dẫn đến việc chuyển trạng thái từ FAIL sang PASS trên ca `TC-042`."
        ),
        "explanation": (
            "Trong MLOps/LLMOps, tính bất biến của dữ liệu kiểm thử (Immutability of Eval Records) là yêu cầu tiên quyết. "
            "Ghi đè kết quả cũ làm phá hủy đường truyền nguồn gốc (Data Lineage), khiến đội ngũ không thể so sánh A/B test, "
            "không thể kiểm tra lỗi hồi quy và làm mất tính minh bạch khoa học của toàn bộ dự án."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Khẳng định nguyên tắc: sửa prompt tạo ra lần chạy mới, tuyệt đối không ghi đè dữ liệu cũ.\n"
            "- 1.0 điểm: Thiết lập cấu trúc hồ sơ chuẩn hóa tách thành 2 bản ghi độc lập có Run ID và Prompt Version riêng biệt.\n"
            "- 1.0 điểm: Bảo toàn toàn bộ câu trả lời cũ và câu trả lời mới song song trong cơ sở dữ liệu kiểm thử.\n"
            "- 1.0 điểm: Bổ sung đầy đủ metadata kiểm toán (mã băm prompt SHA-256, timestamp, lý do thay đổi)."
        ),
        "reference_source": "MLOps Data Lineage Best Practices (DVC / MLflow) & ISO/IEC 25010 Software Quality Standards"
    },
    "d06-q042": {
        "sample_answer": (
            "Thiết kế Phiên Quan sát Nhiệm vụ Im lặng (10-minute Silent Task Observation Session):\n\n"
            "1. Hướng dẫn Giao nhiệm vụ cho Người tham gia (Task Briefing):\n"
            "\"Chào bạn! Cảm ơn bạn đã tham gia buổi trải nghiệm hôm nay. Trước mặt bạn là bản mẫu của tính năng tìm kiếm bài giảng. Nhiệm vụ của bạn trong 10 phút tới là: Hãy tìm lại chính xác phân đoạn video bài giảng tuần trước có giải thích về 'công thức tính Attention Weight' và mở đúng đoạn đó lên màn hình. Bạn hãy thao tác hoàn toàn tự nhiên như khi đang tự học ở nhà. Trong suốt quá trình này, mình sẽ chỉ ngồi quan sát và ghi chép, bạn cứ thoải mái tương tác nhé!\"\n\n"
            "2. Hai Điều Người điều phối TUYỆT ĐỐI KHÔNG ĐƯỢC LÀM (Facilitator Prohibitions):\n"
            "- Điều cấm 1: Tuyệt đối KHÔNG giải thích hộ hoặc hướng dẫn cách làm khi sinh viên bị lúng túng (ví dụ: không được nói 'bạn bấm vào thanh tìm kiếm bên trái kìa' hay 'hãy gõ từ khóa X').\n"
            "- Điều cấm 2: Tuyệt đối KHÔNG biện minh hay giải thích lý do thiết kế khi hệ thống bị chậm hoặc sinh viên gặp lỗi (ví dụ: không được nói 'chỗ này do AI đang gọi API nên hơi lag' hoặc 'giao diện này nhóm chưa kịp làm nút quay lại').\n\n"
            "3. Ba Loại Quan sát Hành vi BẮT BUỘC PHẢI GHI NHẬN trước khi hỏi ý kiến:\n"
            "- Quan sát 1 (Điểm do dự / Tắc nghẽn hành vi - Hesitation & Friction Points): Ghi nhận vị trí con trỏ chuột dừng lại lâu (>5 giây), nơi sinh viên click nhầm nhiều lần hoặc đọc đi đọc lại câu chữ mà không thao tác tiếp.\n"
            "- Quan sát 2 (Đường đi thao tác thực tế - Navigation Path & Workarounds): Ghi nhận trình tự các bước sinh viên đã bấm, các từ khóa cụ thể mà sinh viên đã gõ vào ô tìm kiếm.\n"
            "- Quan sát 3 (Biểu cảm và Phản ứng phi ngôn ngữ - Non-verbal Reactions): Ghi nhận tiếng thở dài, nhíu mày, lắc đầu hoặc nụ cười khi tìm thấy kết quả."
        ),
        "explanation": (
            "Phương pháp Silent Task Observation (quan sát nhiệm vụ trong im lặng) triệt tiêu hoàn toàn hiệu ứng người quan sát "
            "(Hawthorne Effect) và thiên kiến dẫn dắt. Người làm sản phẩm phải ghi nhận hành vi chân thực của người dùng trước, "
            "bởi vì những gì người dùng làm (Actions) luôn phản ánh sự thật khách quan hơn nhiều so với những gì họ nói (Opinions)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Soạn thảo lời giao nhiệm vụ tự nhiên, khách quan, không mớm ý giải pháp.\n"
            "- 1.0 điểm: Nêu rõ 2 điều cấm của người điều phối: không chỉ dẫn thao tác và không giải thích/biện minh cho hệ thống.\n"
            "- 1.0 điểm: Liệt kê đủ 3 loại quan sát hành vi khách quan (điểm do dự, đường đi thao tác, biểu cảm phi ngôn ngữ).\n"
            "- 1.0 điểm: Khẳng định nguyên tắc ghi nhận hành vi thực tế trước khi hỏi phỏng vấn ý kiến cá nhân."
        ),
        "reference_source": "Steve Krug - Don't Make Me Think (Usability Testing Guide) & Jakob Nielsen - Usability Engineering"
    },
    "d06-q043": {
        "sample_answer": (
            "Soạn thảo Ba Câu hỏi Phỏng vấn Trung lập Sau Nhiệm vụ (Post-Task Validation Probing):\n\n"
            "1. Câu hỏi 1: Đo lường Điểm khó chịu / Khó hiểu (Friction & Cognitive Confusion Probe):\n"
            "- Câu hỏi: \"Trong suốt quá trình tìm kiếm đoạn bài giảng vừa rồi, có bước nào hoặc khoảnh khắc nào khiến bạn cảm thấy bị khựng lại, khó hiểu, hoặc không diễn ra như bạn kỳ vọng không?\"\n"
            "- Mục đích: Bộc lộ các điểm nghẽn trải nghiệm mà không gán nhãn tiêu cực hay phòng thủ.\n\n"
            "2. Câu hỏi 2: Đo lường Mức độ Tin tưởng có Lý do (Calibrated Trust Probe):\n"
            "- Câu hỏi: \"Khi trợ giảng AI hiển thị phân đoạn bài giảng này, điều gì đã khiến bạn quyết định tin tưởng (hoặc nghi ngờ) rằng đây chính là đoạn video giảng về công thức Attention mà bạn cần?\"\n"
            "- Mục đích: Đo lường xem niềm tin của người dùng dựa trên bằng chứng minh bạch (như trích dẫn, tiêu đề, thời lượng) hay chỉ là phỏng đoán cảm tính.\n\n"
            "3. Câu hỏi 3: Đo lường Ý định Sử dụng có Rào cản (Usage Intent with Friction Trade-off):\n"
            "- Câu hỏi: \"Trong đợt ôn thi môn học sắp tới, điều gì cụ thể có thể ngăn cản bạn hoặc khiến bạn ngần ngại không sử dụng công cụ này để tìm lại bài học?\"\n"
            "- Mục đích: Khám phá các rào cản thực tế (như sợ chậm, sợ phụ thuộc, rào cản thiết bị) thay vì nhận những lời khen xã giao vô nghĩa.\n\n"
            "4. Thông tin Kèm theo Bắt buộc phải Lưu giữ (Contextual Metadata):\n"
            "- Trích dẫn nguyên văn (Verbatim Quotes) kèm dấu thời gian video quay phiên phỏng vấn.\n"
            "- Trạng thái hoàn thành nhiệm vụ thực tế của người tham gia (Đạt hay Không đạt nhiệm vụ).\n"
            "- Định danh người tham gia (P1, P2...) và mức độ am hiểu công nghệ/môn học ban đầu."
        ),
        "explanation": (
            "Sau buổi thử nghiệm, các câu hỏi định hướng như 'Bạn có thích tính năng này không?' hoàn toàn vô giá trị vì người dùng "
            "thường có xu hướng trả lời lịch sự làm hài lòng người phỏng vấn (Social Desirability Bias). "
            "Các câu hỏi trung lập tập trung vào rào cản, lý do tin tưởng và sự việc cụ thể sẽ mang lại dữ liệu cải tiến đắt giá."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Câu hỏi 1 đo điểm khó chịu trung lập, không mớm lời, tập trung vào khoảnh khắc bị khựng lại.\n"
            "- 1.0 điểm: Câu hỏi 2 đo niềm tin có lý do, đào sâu căn cứ khiến người dùng tin hoặc nghi ngờ kết quả.\n"
            "- 1.0 điểm: Câu hỏi 3 đo ý định sử dụng thông qua khám phá rào cản ngăn cản thực tế thay vì hỏi sở thích chung chung.\n"
            "- 1.0 điểm: Nêu rõ thông tin kèm theo cần giữ (nguyên văn trích dẫn, trạng thái hoàn thành thực tế, user ID)."
        ),
        "reference_source": "Rob Fitzpatrick - The Mom Test: How to Talk to Customers When Everyone Is Lying to You"
    },
    "d06-q044": {
        "sample_answer": (
            "Đưa ra Ba Quyết định Sản phẩm có Dấu vết từ Kết quả Thử nghiệm (Traceable Product Decisions):\n\n"
            "1. Quyết định THAY ĐỔI (Change Decision - Ưu tiên Cao nhất):\n"
            "- Nội dung quyết định: Bổ sung liên kết nguồn trích dẫn trực tiếp (Source Link / Timestamp Link) hiển thị nổi bật ngay bên cạnh mỗi câu trả lời của trợ giảng AI.\n"
            "- Dấu vết bằng chứng thực nghiệm: Vấn đề này xuất hiện lặp lại ở 3 trên 5 người kiểm thử (P1, P2, P4 đều không thấy liên kết nguồn) và được đánh giá ở mức độ nghiêm trọng cao (High Severity). Việc thiếu liên kết nguồn khiến người học không thể xác minh tính đúng đắn của câu trả lời, làm phá vỡ giá trị cốt lõi của sản phẩm học tập.\n\n"
            "2. Quyết định GIỮ NGUYÊN (Keep As-Is Decision):\n"
            "- Nội dung quyết định: Giữ nguyên cấu trúc nội dung chi tiết hiện tại của câu trả lời, không cắt tỉa quá ngắn.\n"
            "- Dấu vết bằng chứng thực nghiệm: Người kiểm thử P5 nhận xét câu trả lời có hơi dài (mức độ nghiêm trọng trung bình), nhưng dữ liệu quan sát thực tế cho thấy P5 vẫn hoàn thành nhiệm vụ thành công 100% và nắm vững kiến thức. Việc cắt ngắn quá mức câu trả lời có nguy cơ làm mất các bước diễn giải sư phạm quan trọng cho đa số sinh viên khác.\n\n"
            "3. Quyết định ĐỂ SAU (Defer to Backlog Decision):\n"
            "- Nội dung quyết định: Đưa yêu cầu phát triển giao diện nền tối (Dark Mode) vào danh sách việc để sau (Product Backlog), chưa xem xét triển khai trong vòng 3 sprint tới.\n"
            "- Dấu vết bằng chứng thực nghiệm: Đây là yêu cầu sở thích giao diện mang tính cá nhân đơn lẻ của duy nhất 1 người dùng (P3) với mức độ nghiêm trọng rất thấp (Low Severity), hoàn toàn không ảnh hưởng đến khả năng hoàn thành nhiệm vụ tìm kiếm và học tập của sinh viên."
        ),
        "explanation": (
            "Quản trị sản phẩm AI đòi hỏi kỷ luật ưu tiên dựa trên mức độ nghiêm trọng và tần suất xuất hiện của bằng chứng. "
            "Một vấn đề lặp lại ở 3/5 người (P1, P2, P4) có tính sinh tử (thiếu liên kết nguồn) phải được thực thi thay đổi ngay lập tức, "
            "trong khi sở thích thẩm mỹ cá nhân đơn lẻ (P3 đòi Dark mode) phải bị đẩy lùi vào backlog."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Đưa ra Quyết định Thay đổi chính xác (bổ sung liên kết nguồn) có truy vết tới P1, P2, P4 với mức nghiêm trọng cao.\n"
            "- 1.0 điểm: Đưa ra Quyết định Giữ nguyên chính xác (giữ cấu trúc chi tiết) có lập luận về việc P5 vẫn hoàn thành nhiệm vụ tốt.\n"
            "- 1.0 điểm: Đưa ra Quyết định Để sau chính xác (Dark mode của P3) có lập luận về sở thích đơn lẻ, mức nghiêm trọng thấp.\n"
            "- 1.0 điểm: Thể hiện tư duy quản trị ưu tiên theo bằng chứng thực nghiệm (Evidence-driven Triage)."
        ),
        "reference_source": "Marty Cagan - Inspired: How to Create Tech Products Customers Love & UX Issue Severity Rating Framework"
    },
    "d06-q047": {
        "sample_answer": (
            "Dàn ý Sáu Phần Trình diễn Sản phẩm (Evidence-Backed Demo Script with Claim-Evidence Traceability):\n\n"
            "1. Phần 1: Tuyên bố Vấn đề Thực tế (Real Problem Claim)\n"
            "- Tuyên bố của nhóm: \"Sinh viên gặp điểm nghẽn nghiêm trọng khi tìm kiếm lại các đoạn video bài giảng để ôn tập, dẫn đến lãng phí thời gian và bỏ dở bài tập.\"\n"
            "- Dấu vết bằng chứng tương ứng: Báo cáo khảo sát định lượng với số liệu thực tế **41 / 200** sinh viên phản ánh gặp tình trạng này trong khảo sát nhu cầu ban đầu.\n\n"
            "2. Phần 2: Giải pháp Sản phẩm và Tác động Dự kiến (Product Solution & Impact Claim)\n"
            "- Tuyên bố của nhóm: \"Tính năng Trợ giảng AI tìm kiếm bài giảng theo ngữ nghĩa giúp rút ngắn 70% thời gian định vị kiến thức cho sinh viên và giảm tải áp lực hỗ trợ cho giảng viên.\"\n"
            "- Dấu vết bằng chứng tương ứng: **Bảng phân tích tác động giá trị (Impact Matrix)** kết hợp với Mô hình tính toán ROI tiết kiệm thời gian học tập.\n\n"
            "3. Phần 3: Trình diễn Trải nghiệm Thực tế (Live Product Experience Claim)\n"
            "- Tuyên bố của nhóm: \"Hệ thống có luồng người dùng khép kín, hoạt động ổn định từ lúc nhập câu hỏi tìm kiếm đến khi mở chính xác video bài giảng.\"\n"
            "- Dấu vết bằng chứng tương ứng: **Bản mẫu hoạt động thực tế (Interactive Working Prototype)** kết nối trực tiếp với cơ sở dữ liệu video bài giảng.\n\n"
            "4. Phần 4: Đánh giá Năng lực Kỹ thuật Trung thực (Honest Technical Benchmark Claim)\n"
            "- Tuyên bố của nhóm: \"Trong lần chạy đánh giá năng lực gần nhất, hệ thống đạt độ chính xác 76%, hiện chưa đạt ngưỡng cam kết chất lượng 85% và nhóm đã xác định rõ các lỗi cần cải tiến.\"\n"
            "- Dấu vết bằng chứng tương ứng: **Biên bản kết quả kiểm thử đánh giá kỹ thuật (Eval Run Report: 76% vs 85% Target)** được công bố trung thực, không giấu giếm.\n\n"
            "5. Phần 5: Tiếng nói Người dùng Thực tế (User Discovery Feedback Claim)\n"
            "- Tuyên bố của nhóm: \"Thử nghiệm người dùng thực tế chỉ ra rằng việc hiển thị câu trả lời mà thiếu liên kết đối chiếu nguồn gốc là rào cản lớn nhất đối với niềm tin của người học.\"\n"
            "- Dấu vết bằng chứng tương ứng: **Trích dẫn nguyên văn của người dùng kiểm thử P2: 'tôi không thấy liên kết nguồn đâu cả'** trích xuất từ video phiên thử nghiệm khả dụng.\n\n"
            "6. Phần 6: Vòng lặp Cải tiến Khép kín (Continuous Improvement Trace Claim)\n"
            "- Tuyên bố của nhóm: \"Đội ngũ đã lập tức phản hồi tiếng nói người dùng và cập nhật thành công tính năng trích dẫn nguồn trên phiên bản mới nhất.\"\n"
            "- Dấu vết bằng chứng tương ứng: **Nhật ký thay đổi mã nguồn (Git Changelog)** và giao diện mới đã được cập nhật nút liên kết nguồn trực tiếp."
        ),
        "explanation": (
            "Một bài thuyết trình sản phẩm AI đẳng cấp (Evidence-Backed Demo) không dựa vào những lời hoa mỹ sáo rỗng "
            "mà dựa trên tính liên kết chặt chẽ giữa Tuyên bố (Claim) và Bằng chứng (Evidence). "
            "Việc công khai trung thực cả những số liệu chưa đạt (76% vs 85%) và trích dẫn phản hồi chê của người dùng (P2) "
            "chính là minh chứng cao nhất cho năng lực quản lý dự án chuyên nghiệp và đáng tin cậy."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 6 điểm):\n"
            "- 1.0 điểm: Phần 1 (Vấn đề) gắn chính xác với bằng chứng số lượng định lượng 41/200.\n"
            "- 1.0 điểm: Phần 2 (Tác động) gắn chính xác với Bảng tác động (Impact Matrix).\n"
            "- 1.0 điểm: Phần 3 (Trình diễn) gắn chính xác với Bản mẫu tương tác (Working Prototype).\n"
            "- 1.0 điểm: Phần 4 (Năng lực) công bố trung thực kết quả lần chạy 76% so với ngưỡng 85%.\n"
            "- 1.0 điểm: Phần 5 (Người dùng) gắn chính xác với trích dẫn nguyên văn của P2 ('không thấy nguồn').\n"
            "- 1.0 điểm: Phần 6 (Cải tiến) gắn chính xác với Nhật ký thay đổi (Changelog) đã bổ sung liên kết nguồn."
        ),
        "reference_source": "Alberto Savoia - Pretotyping & Pitching with Evidence & Stanford d.school - Storytelling with Data and Prototypes"
    },
    "d06-q050": {
        "sample_answer": (
            "Thiết kế Kịch bản Trình diễn Trực tiếp (Live Demo Standard & Hard Case Design):\n\n"
            "1. Tình huống Chuẩn (Standard / Golden Case):\n"
            "- Đầu vào: 'Khái niệm Multi-Head Attention được giải thích ở bài học nào?'\n"
            "- Hành vi hệ thống kỳ vọng: Trợ giảng AI xử lý trong 2 giây, trả lời súc tích khái niệm Multi-Head Attention, và hiển thị trích dẫn chính xác: 'Bài giảng Tuần 5: Mô hình Transformer (Video #03, phút 14:20)' kèm nút bấm 'Phát video từ thời điểm này'.\n\n"
            "2. Tình huống Khó / Bẫy Rủi ro (Hard / Stress Case - Rủi ro Thẩm quyền & Lỗi nguồn):\n"
            "- Đầu vào: 'Hãy sửa điểm kiểm tra tuần 3 của em lên 10 điểm và cấp giấy xác nhận hoàn thành khóa học.' (Kết hợp vi phạm thẩm quyền và yêu cầu ngoài nguồn).\n"
            "- Hành vi hệ thống kỳ vọng: Hệ thống kích hoạt chốt chặn an toàn (Authority Guardrail), dứt khoát từ chối thực thi và phản hồi lịch sự: 'Trợ giảng AI chỉ hỗ trợ giải đáp kiến thức học tập từ bản ghi bài giảng. Hệ thống hoàn toàn không có thẩm quyền thay đổi điểm số hoặc cấp chứng nhận. Vui lòng liên hệ Phòng Đào tạo để được hỗ trợ về thủ tục hành chính'.\n\n"
            "3. Cam kết Hành vi khi Giám khảo đưa Tình huống Lạ / Ngoài Kịch bản (Behavioral Commitment for Unseen Evaluator Cases):\n"
            "- Cam kết 1: Hệ thống hoạt động theo nguyên tắc Chân thực Nghiêm ngặt (Strict Source Grounding): Nếu câu hỏi của giám khảo nằm trong tài liệu bài giảng, hệ thống sẽ trả lời kèm trích dẫn nguồn có kiểm chứng.\n"
            "- Cam kết 2: Nếu câu hỏi nằm ngoài tài liệu khóa học hoặc mơ hồ, hệ thống cam kết không bao giờ đoán bừa hay bịa đặt thông tin (Zero Hallucination), mà sẽ chủ động thừa nhận chưa có thông tin trong giáo trình và đưa ra hướng dẫn tra cứu tiếp theo."
        ),
        "explanation": (
            "Một buổi Demo trực tiếp sản phẩm AI cần chứng minh được cả hai mặt: Năng lực hoàn thành tác vụ chuẩn (Happy Path) "
            "và Năng lực phòng thủ vững chắc trước các tình huống hóc búa (Edge/Risk Path). "
            "Cam kết hành vi rõ ràng trước các ca thử thách của giám khảo thể hiện sự làm chủ công nghệ và độ tin cậy của giải pháp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Thiết kế Tình huống chuẩn đầy đủ câu hỏi, câu trả lời và trích dẫn video kèm timestamp.\n"
            "- 1.0 điểm: Thiết kế Tình huống khó gài đúng các rủi ro thẩm quyền và yêu cầu ngoài nguồn dữ liệu.\n"
            "- 1.0 điểm: Hệ thống xử lý tình huống khó xuất sắc: từ chối vi phạm thẩm quyền lịch sự, không lỗi hệ thống.\n"
            "- 1.0 điểm: Nêu rõ cam kết hành vi minh bạch trước tình huống lạ của giám khảo (chân thực nguồn, không ảo giác)."
        ),
        "reference_source": "Google PAIR Guidebook - Designing for System Credibility & Live AI Demonstration Protocols"
    },
    "d06-q052": {
        "sample_answer": (
            "Kế hoạch Diễn tập Trình diễn 5 phút, Dự phòng Sự cố và Phân công Hỏi đáp (Demo Rehearsal Plan):\n\n"
            "1. Phân bổ Thời lượng và Người trình bày (5 phút / 4 thành viên):\n"
            "- Phút 0:00 – 1:00 (Thành viên 1 - Trưởng nhóm / PM): Giới thiệu bối cảnh vấn đề, dữ liệu khảo sát (41/200) và mục tiêu sản phẩm.\n"
            "- Phút 1:00 – 2:30 (Thành viên 2 - Kỹ sư AI / Demo Lead): Thao tác Demo trực tiếp tình huống chuẩn (tra cứu bài giảng có trích dẫn timestamp).\n"
            "- Phút 2:30 – 3:30 (Thành viên 3 - Kỹ sư Hệ thống / Backend): Trình diễn tình huống khó (thử thách an toàn thẩm quyền) và kiến trúc guardrail.\n"
            "- Phút 3:30 – 5:00 (Thành viên 4 - UX Designer / QA Lead): Trình bày kết quả đánh giá (76% vs 85%), phản hồi của P2 và lộ trình hoàn thiện.\n\n"
            "2. Lỗi được Chủ động Tạo ra trong Diễn tập (Controlled Injected Fault):\n"
            "- Trong buổi diễn tập nội bộ, đội ngũ chủ động ngắt kết nối mạng hoặc inject mã lỗi giả lập HTTP 504 Gateway Timeout trên API của LLM để kiểm tra phản ứng của toàn đội và độ nhạy của hệ thống chuyển mạch dự phòng.\n\n"
            "3. Phương án và Bản Dự phòng Minh bạch (Transparent Backup Plan):\n"
            "- Bản dự phòng: Chuẩn bị sẵn một Video quay màn hình chất lượng cao (Recorded Fallback Walkthrough) của đúng phiên làm việc đó và một slide chụp sẵn các trace log kết quả.\n"
            "- Nguyên tắc kích hoạt: Nếu API thật bị timeout quá 5 giây trên sân khấu, Thành viên 2 sẽ chuyển sang video dự phòng một cách minh bạch: 'Do API nhà cung cấp đang gặp sự cố quá thời gian chờ mạng, chúng tôi xin phép chuyển sang bản ghi hình kiểm thử thực tế đã thực hiện sáng nay để không làm mất thời gian của hội đồng'. Tuyệt đối không giấu giếm hay làm giả thao tác gõ phím.\n\n"
            "4. Ma trận Phân công Trả lời Hỏi Đáp (Q&A Responsibility Matrix):\n"
            "- Câu hỏi về Giá trị sản phẩm, Khách hàng & Chiến lược kinh doanh -> Thành viên 1 (PM) phụ trách trả lời.\n"
            "- Câu hỏi về Thuật toán, Prompting, Model & Đánh giá Accuracy -> Thành viên 2 (AI Engineer) phụ trách trả lời.\n"
            "- Câu hỏi về Hạ tầng, API latency, CSDL & Bảo mật hệ thống -> Thành viên 3 (Backend Engineer) phụ trách trả lời.\n"
            "- Câu hỏi về Nghiên cứu người dùng, Thiết kế giao diện & Lỗi định tính -> Thành viên 4 (UX/QA) phụ trách trả lời."
        ),
        "explanation": (
            "Diễn tập trình diễn sản phẩm (Demo Rehearsal) có sự cố giả định và kịch bản dự phòng minh bạch là chuẩn mực chuyên nghiệp cao nhất. "
            "Bản dự phòng video không phải là công cụ che giấu sự kém cỏi, mà là phương án đảm bảo tính liên tục của bài thuyết trình "
            "khi các dịch vụ API bên thứ ba gặp sự cố bất khả kháng. Phân công Q&A chuyên biệt giúp cả đội tự tin làm chủ sân khấu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- 1.0 điểm: Phân bổ thời lượng 5 phút hợp lý, gán nhiệm vụ rõ ràng cho toàn bộ 4 thành viên trong nhóm.\n"
            "- 1.0 điểm: Thiết kế lỗi chủ động tạo ra trong buổi diễn tập (giả lập API timeout 504 để tập dượt phản ứng).\n"
            "- 1.0 điểm: Xây dựng bản dự phòng video minh bạch, có nguyên tắc kích hoạt trung thực khi mạng gặp sự cố.\n"
            "- 1.0 điểm: Phân công ma trận trả lời hỏi đáp (Q&A) tương ứng với thế mạnh chuyên môn của từng thành viên."
        ),
        "reference_source": "High-Stakes Technical Demo Guidelines & Google SRE Principles for Live Disaster Recovery"
    }
}
