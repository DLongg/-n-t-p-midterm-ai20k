"""
Authoring module for Day 02 essay questions - Part 1 (42 questions).
Generates sample_answer, explanation, rubric, reference_source for d02-q002 through d02-q064.
"""

def get_day02_part1_data():
    data = {}

    # 1. d02-q002 (3 pts) [kc-problem-first-reframing]
    data["d02-q002"] = {
        "sample_answer": (
            "- Viết lại thành câu hỏi khám phá vấn đề (Problem Discovery Question):\n"
            "\"Làm thế nào để [nhân viên và quản lý các phòng ban - Người thực hiện] có thể [tìm khung giờ trống phù hợp và thống nhất lịch họp liên phòng ban - Quy trình] "
            "mà không gặp phải [tình trạng xung đột lịch, tốn 20-30 phút gửi email qua lại trao đổi qua nhiều kênh - Điểm đau], "
            "nhằm đạt được [việc chốt lịch họp nhanh chóng dưới 2 phút với tỷ lệ tham dự đúng giờ trên 90% - Kết quả mong muốn]?\"\n\n"
            "- Hai giả định phải kiểm chứng trước khi chọn giải pháp AI:\n"
            "1. Giả định về dữ liệu nguồn: Lịch cá nhân trên Google Calendar / Outlook của nhân viên đã được cập nhật chính xác và đầy đủ các khung giờ bận thực tế hay chưa? "
            "(Nếu dữ liệu lịch rác hoặc không được cập nhật, AI cũng sẽ xếp lịch sai).\n"
            "2. Giả định về giải pháp phi AI: Liệu một công cụ xếp lịch tất định truyền thống (như Calendly, Doodle, hoặc thuật toán tìm khoảng trống giao nhau trong API lịch) "
            "đã đủ giải quyết 80% vấn đề mà không cần đến sự phức tạp và chi phí của LLM hay không?"
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Phương pháp 'Problem-First Thinking' (tư duy xuất phát từ vấn đề) cảnh báo bẫy 'Solution-in-search-of-a-problem' "
            "(có búa AI đi tìm đinh). Trước khi quyết định đầu tư tác nhân AI, người làm sản phẩm phải định hình rõ ràng tác nhân, quy trình, điểm ma sát đo đếm được "
            "và kiểm định tính khả thi của các phương án kỹ thuật đơn giản hơn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Câu hỏi khám phá vấn đề đủ 4 yếu tố (1.5 điểm): Xác định rõ người thực hiện, quy trình, điểm đau cụ thể và kết quả mong muốn đo lường được.\n"
            "- Hai giả định kiểm chứng then chốt (1.5 điểm): Nêu đúng giả định về chất lượng dữ liệu lịch nguồn và giả định về giải pháp phần mềm tất định đơn giản (phi AI)."
        ),
        "reference_source": "Torres, T. (2021). Continuous Discovery Habits. Product Talk LLC (https://www.producttalk.org/); Harvard Business Review - Stop the Meeting Madness (https://hbr.org/2017/07/stop-the-meeting-madness)"
    }

    # 2. d02-q004 (3 pts) [kc-user-workflow-pain-observation]
    data["d02-q004"] = {
        "sample_answer": (
            "Phân tích dữ liệu quan sát quy trình kế toán:\n"
            "- Người thực hiện (Actors): Nhân viên kế toán (tiếp nhận hóa đơn và nhập liệu), Quản lý kế toán (kiểm tra phê duyệt và trả lại hóa đơn sai).\n"
            "- Bước trong quy trình (Workflow step): Bước 2 (Kế toán sao chép số tiền thủ công từ PDF vào bảng tính) và Bước 3 (Quản lý phát hiện sai sót và trả lại hồ sơ).\n"
            "- Điểm đau (Pain point): Tỷ lệ nhập liệu sai số tiền cao dẫn đến việc hóa đơn bị từ chối phê duyệt, phát sinh lãng phí thời gian sửa chữa và làm chậm trễ chu kỳ thanh toán cho nhà cung cấp.\n"
            "- Bằng chứng thực nghiệm quan sát được (Empirical evidence): 6/20 hóa đơn bị trả lại vì sai số tiền (tỷ lệ lỗi 30%); mỗi lượt sửa chữa tiêu tốn trung bình 12 phút (tổng lãng phí 72 phút cho 20 hóa đơn).\n"
            "- Một điều vẫn chỉ là giả định (Unverified assumption): Giả định rằng nguyên nhân sai sót là do kế toán gõ nhầm bất cẩn. Thực tế có thể do file PDF chất lượng kém, bản scan mờ, cấu trúc bảng phức tạp, hoặc cách thể hiện định dạng số (dấu chấm phân tách phần nghìn vs dấu phẩy thập phân) gây hiểu nhầm."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong thiết kế trải nghiệm người dùng (UX Research & Workflow Mapping), việc phân biệt rạch ròi giữa "
            "'Dữ kiện quan sát được' (Fact/Evidence) và 'Suy đoán nguyên nhân' (Hypothesis) là tối quan trọng để tránh đưa ra các giải pháp tự động hóa lệch đích."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xác định đúng người thực hiện và bước quy trình (1.0 điểm): Nêu rõ kế toán/quản lý và các bước nhập liệu/kiểm tra.\n"
            "- Chỉ ra điểm đau và bằng chứng định lượng (1.0 điểm): Nêu đúng tỷ lệ lỗi 30% (6/20 hóa đơn) và thời gian sửa 12 phút/hóa đơn.\n"
            "- Phân định giả định chưa kiểm chứng (1.0 điểm): Nhận diện đúng giả định ngầm định về nguyên nhân lỗi gõ tay thay vì lỗi do định dạng tài liệu."
        ),
        "reference_source": "Nielsen Norman Group - Workflow Mapping & Usability Testing (https://www.nngroup.com/articles/workflow-testing/); Dumas, J. S., & Redish, J. (1999). A Practical Guide to Usability Testing."
    }

    # 3. d02-q005 (3 pts) [kc-stakeholder-discovery-interview]
    data["d02-q005"] = {
        "sample_answer": (
            "Bốn câu hỏi khám phá vấn đề (Discovery Questions) không gợi ý giải pháp:\n"
            "1. Khám phá sự cố gần đây: \"Anh/chị có thể chia sẻ chi tiết về lần gần đây nhất một máy móc bị hỏng bất ngờ diễn ra như thế nào, máy thuộc dây chuyền nào và triệu chứng ban đầu là gì?\"\n"
            "2. Khám phá quy trình và điểm bàn giao: \"Khi phát hiện máy có dấu hiệu bất thường, kỹ thuật viên vận hành thông báo cho đội bảo trì bằng cách nào, và các bước bàn giao hiện trường diễn ra theo quy trình nào?\"\n"
            "3. Khám phá tần suất, tác động và rủi ro: \"Trung bình mỗi tháng có bao nhiêu sự cố dừng máy đột xuất, mỗi lần dừng máy gây gián đoạn sản xuất bao lâu và ước tính thiệt hại kinh tế là bao nhiêu?\"\n"
            "4. Khám phá người chịu trách nhiệm và bằng chứng thành công: \"Ai là người chịu trách nhiệm cuối cùng về chỉ số sẵn sàng của thiết bị (OEE/Uptime), và nếu vấn đề dừng máy được cải thiện thì số liệu cụ thể nào sẽ chứng minh dự án thành công?\""
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Kỹ năng phỏng vấn khám phá bên liên quan (Stakeholder Discovery) tuân thủ nguyên tắc 'Problem Space over Solution Space'. "
            "Thay vì thảo luận về thuật toán Machine Learning hay cảm biến IoT, người làm sản phẩm tập trung đào sâu sự cố thực tế, tổn thất kinh tế và thước đo thành công nghiệp vụ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Câu 1 & 2 về sự cố và quy trình bàn giao (1.5 điểm): Hỏi đúng sự cố cụ thể gần nhất và luồng bàn giao công việc giữa vận hành - bảo trì.\n"
            "- Câu 3 & 4 về tác động, người chịu trách nhiệm và tiêu chí thành công (1.5 điểm): Khai thác đúng tần suất/thiệt hại và xác định rõ owner cùng bằng chứng thành công mà không gợi ý giải pháp AI."
        ),
        "reference_source": "Fitzpatrick, R. (2013). The Mom Test. Robfitz Ltd (http://momtestbook.com/); Teresa Torres - Continuous Discovery Habits (https://www.producttalk.org/)"
    }

    # 4. d02-q006 (3 pts) [kc-stakeholder-discovery-interview]
    data["d02-q006"] = {
        "sample_answer": (
            "1. Tách biệt dữ kiện đã có khỏi giả định còn thiếu bằng chứng:\n"
            "- Dữ kiện đã có (Facts): (1) 4/10 hợp đồng phải hỏi lại điều khoản thanh toán (tỷ lệ 40%); (2) Nhân viên pháp chế mất trung vị 25 phút để tra cứu; (3) Chưa có số liệu phân rã thời gian giữa khâu tìm kiếm và khâu phê duyệt.\n"
            "- Giả định thiếu bằng chứng (Assumptions): (1) Giả định việc đọc hiểu hợp đồng là nút thắt chính gây chậm trễ (thay vì do mẫu hợp đồng thiếu chuẩn hóa hoặc đối tác cố tình kéo dài đàm phán); (2) Giả định việc đưa AI vào đọc hợp đồng sẽ giảm được thời gian tra cứu và giải quyết được tận gốc nguyên nhân phải hỏi lại.\n\n"
            "2. Ba câu hỏi tiếp theo để phân biệt nút thắt, hậu quả và quyền quyết định:\n"
            "- Phân biệt nút thắt: \"Trong 25 phút tra cứu của pháp chế, thời gian lật tìm trang tài liệu chiếm bao nhiêu phút so với thời gian đối chiếu quy định pháp luật và chính sách tín dụng nội bộ?\"\n"
            "- Đánh giá hậu quả: \"Việc 4/10 hợp đồng phải hỏi lại điều khoản gây chậm tiến độ ký kết trung bình bao nhiêu ngày, và có dẫn đến khiếu nại hoặc mất hợp đồng không?\"\n"
            "- Xác định quyền quyết định: \"Ai là người có thẩm quyền phê duyệt cuối cùng để chấp nhận ngoại lệ thanh toán hoặc chuẩn hóa lại mẫu hợp đồng?\"\n\n"
            "3. Ngưỡng bằng chứng cần đạt trước khi đánh giá giải pháp: Phải có dữ liệu đo lường thời gian phân rã chứng minh khâu tìm kiếm thủ công chiếm > 60% tổng thời gian (tối thiểu 15 phút) trên cỡ mẫu từ 50 hợp đồng trở lên."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Đề xuất 'Dùng AI đọc hợp đồng' thường là phản xạ vội vàng trước các triệu chứng bề mặt. Bằng cách thiết lập "
            "ngưỡng bằng chứng định lượng (Evidence Threshold) và phân tách nút thắt quy trình, đội ngũ sản phẩm tránh lãng phí nguồn lực vào các giải pháp đắt đỏ không trúng đích."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Tách bạch dữ kiện và giả định (1.0 điểm): Liệt kê đủ 3 dữ kiện quan sát và 2 giả định ngầm định chưa kiểm chứng.\n"
            "- Đặt 3 câu hỏi khám phá sâu (1.0 điểm): Hỏi đúng về nút thắt thời gian, hậu quả chậm trễ và người có quyền quyết định.\n"
            "- Nêu ngưỡng bằng chứng định lượng (1.0 điểm): Đưa ra chỉ số định lượng cụ thể (tỷ lệ thời gian tìm kiếm, cỡ mẫu hợp đồng) cần xác minh trước khi chọn giải pháp."
        ),
        "reference_source": "Cagan, M. (2017). Inspired: How to Create Tech Products Customers Love. Wiley (https://www.svpg.com/books/inspired/); Teresa Torres - Continuous Discovery Habits (https://www.producttalk.org/)"
    }

    # 5. d02-q009 (3 pts) [kc-first-principles-problem-decomposition]
    data["d02-q009"] = {
        "sample_answer": (
            "Phân rã bài toán theo nguyên tắc nền tảng (First Principles Problem Decomposition):\n"
            "1. Bóc tách bản chất nhu cầu và các ràng buộc cốt lõi:\n"
            "- Giả định sai lầm hiện tại: 'Dịch vụ hỗ trợ bắt buộc phải có con người trực tổng đài 24/7' chỉ vì đối thủ làm như vậy (tư duy bắt chước theo quy ước cũ).\n"
            "- Nhu cầu cơ bản thật sự của khách hàng: Khi gặp thắc mắc vào ban đêm, khách hàng cần nhận được câu trả lời chính xác, tức thì cho các vấn đề thông thường; và khi gặp sự cố tài chính, họ cần sự an tâm rằng yêu cầu đã được tiếp nhận an toàn và sẽ được xử lý đúng cam kết.\n"
            "- Ràng buộc pháp lý và an toàn bất biến: Khiếu nại tài chính (liên quan đến hoàn tiền, bồi thường, rủi ro gian lận) bắt buộc phải do nhân sự có thẩm quyền phê duyệt, không thể giao toàn quyền cho AI hay nhân viên trực ca đêm không đủ thẩm quyền.\n\n"
            "2. Đề xuất phương án tiếp cận mới:\n"
            "- Xây dựng hệ thống Hỗ trợ Đa tầng Phân cấp (Tiered Support Architecture):\n"
            "+ Tầng 1 (Tự động 24/7): Triển khai AI Chatbot/RAG tra cứu trực tiếp từ tài liệu chuẩn để giải đáp 100% câu hỏi phổ biến tức thì cho khách hàng mọi lúc.\n"
            "+ Tầng 2 (Thu thập có cấu trúc cho sự cố tài chính): Đối với khiếu nại tài chính phát sinh ngoài giờ, bot hướng dẫn khách hàng cung cấp chứng từ có cấu trúc (ticket) và gửi email xác nhận đã ghi nhận an toàn, cam kết nhân sự có thẩm quyền sẽ liên hệ xử lý trong 2 giờ đầu của ngày làm việc tiếp theo."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tư duy First Principles đòi hỏi đập vỡ các hình thức vận hành truyền thống ('phải có người trực 24/7') "
            "để trở về các chân lý nền tảng: nhu cầu thông tin tức thì và ràng buộc phê duyệt tài chính. Giải pháp phân tầng giúp giảm 70% chi phí nhân sự "
            "mà vẫn đảm bảo 100% tính tuân thủ pháp lý."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân rã nguyên tắc nền tảng (1.5 điểm): Phân biệt rõ nhu cầu giải đáp tức thì với ràng buộc pháp lý của khiếu nại tài chính, bác bỏ tư duy sao chép đối thủ.\n"
            "- Đề xuất phương án tiếp cận phân tầng (1.5 điểm): Thiết kế giải pháp kết hợp AI tự động giải đáp 24/7 cho câu hỏi chuẩn và thu thập ticket có cấu trúc để người có thẩm quyền duyệt."
        ),
        "reference_source": "Aristotelian First Principles in Systems Design; Porter, M. E. (1996). What Is Strategy? Harvard Business Review (https://hbr.org/1996/11/what-is-strategy)"
    }

    # 6. d02-q010 (3 pts) [kc-first-principles-problem-decomposition]
    data["d02-q010"] = {
        "sample_answer": (
            "1. Chỉ ra giả định ẩn (Hidden Assumption):\n"
            "Giả định sai lầm là: Lãnh đạo cần và sẽ đọc hết một tài liệu PDF dài 20 trang để nắm bắt tình hình hoạt động; định dạng PDF 20 trang được coi là biểu hiện của sự kỹ lưỡng, "
            "trong khi thực tế lãnh đạo bị quá tải thông tin và không thể phát hiện sớm các bất thường.\n\n"
            "2. Các ràng buộc thật sự (True Constraints):\n"
            "- Ràng buộc thời gian: Lãnh đạo phải phát hiện được độ lệch KPI trước thời điểm giao ban sáng thứ Hai.\n"
            "- Ràng buộc dữ liệu: Dữ liệu nguồn đã có cấu trúc trong cơ sở dữ liệu/kho dữ liệu.\n"
            "- Ràng buộc kiểm toán: Mọi quyết định rủi ro cao dựa trên số liệu báo cáo bắt buộc phải có khả năng truy vết nguồn gốc (audit trail) về từng bản ghi dữ liệu gốc.\n\n"
            "3. Phương án dựng lại quy trình (Re-engineered Workflow):\n"
            "- Thay thế file PDF 20 trang bằng Bảng điều khiển KPI tự động (Live Dashboard) kết hợp Báo cáo Tóm tắt Điều hành (Executive Exception Summary) 1 trang gửi qua email/Slack vào 7h sáng thứ Hai.\n"
            "- Hệ thống sử dụng quy tắc và thuật toán phát hiện bất thường (Anomaly Detection) để chỉ làm nổi bật các chỉ số bị lệch ngưỡng cho phép (Exception-based Reporting).\n"
            "- Mỗi chỉ số lệch chuẩn đều đính kèm một đường link định danh (deep link) cho phép lãnh đạo nhấp vào để kiểm tra dữ liệu nguồn và lịch sử phê duyệt khi cần ra quyết định."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Management by Exception' kết hợp First Principles loại bỏ hoàn toàn các 'tài liệu rác' (wasteful artifacts). "
            "Chuyển đổi từ tài liệu tĩnh 20 trang sang báo cáo ngoại lệ theo thời gian thực giải phóng thời gian cho đội ngũ và tăng tốc độ phản ứng của ban giám đốc."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nhận diện đúng giả định ẩn (1.0 điểm): Chỉ ra việc ngộ nhận lãnh đạo cần đọc hết 20 trang PDF để nắm bắt KPI.\n"
            "- Nêu đủ các ràng buộc thật sự (1.0 điểm): Liệt kê đúng ràng buộc thời gian (trước thứ Hai), dữ liệu có cấu trúc và khả năng truy vết kiểm toán.\n"
            "- Thiết kế quy trình mới tinh gọn (1.0 điểm): Đề xuất Dashboard/Tóm tắt ngoại lệ 1 trang tự động có deep link truy vết dữ liệu gốc."
        ),
        "reference_source": "Drucker, P. F. (1954). The Practice of Management; Martin Fowler - Information Dashboards & Continuous Delivery (https://martinfowler.com/articles/patterns-of-distributed-systems/)"
    }

    # 7. d02-q014 (3 pts) [kc-impact-effort-prioritization]
    data["d02-q014"] = {
        "sample_answer": (
            "1. Giải thích quyết định tạm thời của nhóm:\n"
            "Nhóm chọn cơ hội X dựa trên ma trận Impact-Effort truyền thống vì trên lý thuyết điểm số, X có tỷ suất lợi ích trên chi phí vượt trội (Tỷ lệ Impact/Effort = 5/2 = 2,5 "
            "so với Y là 4/3 = 1,33). X rơi vào góc phần tư 'Quick Win' (tác động tối đa với nỗ lực tối thiểu), tạo sức hút lớn cho các quyết định ngắn hạn.\n\n"
            "2. Phép kiểm chứng tối thiểu có thể làm đảo lộn thứ hạng:\n"
            "- Điểm yếu cốt tử của X là ước lượng hoàn toàn dựa trên phỏng đoán cảm tính (conjecture), trong khi Y được bảo chứng bởi dữ liệu nhật ký (log) thực tế 3 tháng.\n"
            "- Phép kiểm chứng tối thiểu: Thực hiện một thử nghiệm dò đường kỹ thuật (Technical Spike / Prototype) kéo dài 2-3 ngày để thử nghiệm trích xuất dữ liệu thực tế cho X, "
            "đồng thời phân tích 100 trường hợp người dùng gần nhất.\n"
            "- Kịch bản làm đảo thứ hạng: Nếu phép kiểm chứng phát hiện dữ liệu cho X bị thiếu cấu trúc, tỷ lệ ngoại lệ cao khiến Nỗ lực thực tế nhảy từ 2 lên 5 (Effort = 5), "
            "hoặc nhu cầu thực tế của người dùng thấp khiến Tác động giảm từ 5 xuống 2 (Impact = 2), tỷ lệ của X sẽ tụt xuống dưới Y (2/5 = 0,4 < 1,33). Khi đó Y sẽ được chọn."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong khung ưu tiên sản phẩm (RICE, Impact-Effort), chỉ số 'Độ tin cậy' (Confidence Score) là nhân tố quyết định. "
            "Một ước lượng Impact 5 nhưng Confidence 20% luôn có rủi ro cao hơn nhiều so với Impact 4 nhưng Confidence 90% từ log thực nghiệm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Giải thích quyết định chọn X (1.5 điểm): Nêu rõ việc chọn X vì tỷ lệ Impact/Effort lý thuyết vượt trội (Quick Win 5/2 vs 4/3).\n"
            "- Đề xuất phép kiểm chứng và kịch bản đảo thứ hạng (1.5 điểm): Nêu phép đo spike/phân tích mẫu thực tế để chứng minh sự mong manh của phỏng đoán, chỉ ra khi nỗ lực tăng hoặc tác động giảm thì Y sẽ vượt lên."
        ),
        "reference_source": "Intercom - RICE: Simple prioritization for product managers (https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/); Cagan, M. (2017). Inspired."
    }

    # 8. d02-q015 (3 pts) [kc-candidate-problem-prioritization]
    data["d02-q015"] = {
        "sample_answer": (
            "Tạo danh sách ngắn ưu tiên bài toán ứng viên có đối chiếu bằng chứng:\n\n"
            "- Danh sách ngắn ưu tiên:\n"
            "1. Ưu tiên số 1: Bài toán A.\n"
            "2. Ưu tiên số 2: Bài toán C.\n"
            "3. Loại bỏ / Chưa chọn: Bài toán B.\n\n"
            "- Phân tích chi tiết từng bài toán:\n"
            "+ Bài toán A: Bằng chứng mạnh với 28 ticket thực tế cùng chung điểm đau, tác nhân và quy trình đều đã được xác định rõ ràng. "
            "Điều chưa chắc chắn: Chưa đo lường quy mô hậu quả tài chính. Điểm bất đồng: Không có. Lý do chọn: Bằng chứng thực nghiệm cao nhất, có thể định lượng tài chính nhanh chóng qua phỏng vấn 28 ca.\n"
            "+ Bài toán C: Bằng chứng gồm 9 trường hợp có quy trình rõ, hậu quả tuân thủ pháp lý cao. "
            "Điều chưa chắc chắn: Cỡ mẫu nhỏ (9 ca). Điểm bất đồng: Tranh chấp về người chịu trách nhiệm chính (ownership). Lý do xếp sau A: Cần giải quyết dứt điểm quyền sở hữu và thẩm quyền trước khi bắt tay xây dựng giải pháp.\n"
            "+ Bài toán B: Bằng chứng gần như bằng 0 (chỉ là con số ước tính cảm tính 500 giờ từ stakeholder, không có log chứng minh, không có người thực hiện cụ thể). "
            "Lý do loại/chưa chọn: Vi phạm nguyên tắc ra quyết định dựa trên bằng chứng; nguy cơ cao là giải quyết một bài toán ảo."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Ưu tiên hóa vấn đề phải dựa trên thứ bậc độ tin cậy của bằng chứng (Hierarchy of Evidence): "
            "Nhật ký/Ticket thực tế (Empirical Behavior) > Ý kiến phỏng đoán của Stakeholder (Opinion/Conjecture). Đầu tư vào bài toán thiếu owner "
            "hoặc thiếu dữ liệu sẽ dẫn đến dự án bị đình trệ khi chuyển giao."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Lập danh sách ngắn chuẩn xác (1.0 điểm): Xếp thứ tự A (ưu tiên 1), C (ưu tiên 2), B (loại/chưa chọn).\n"
            "- Phân tích bằng chứng và điều chưa chắc chắn của A và C (1.0 điểm): Nêu rõ bằng chứng 28 ticket của A và rủi ro tuân thủ/tranh chấp owner của C.\n"
            "- Lý do loại bài toán B (1.0 điểm): Phân tích con số 500 giờ của B chỉ là suy đoán thiếu log và thiếu actor cụ thể."
        ),
        "reference_source": "Teresa Torres - Opportunity Solution Tree (https://www.producttalk.org/opportunity-solution-tree/); Cagan, M. (2020). Empowered. Wiley (https://www.svpg.com/books/empowered/)"
    }

    # 9. d02-q016 (3 pts) [kc-candidate-problem-prioritization]
    data["d02-q016"] = {
        "sample_answer": (
            "- Quyết định chọn bài toán tạm thời: Chọn THẺ A.\n\n"
            "- Lý do lựa chọn Thẻ A:\n"
            "Thẻ A có bằng chứng thực nghiệm rõ ràng từ người dùng thực (12 phiếu hỗ trợ xác thực) và tác nhân thực hiện (actor) đã được xác định cụ thể. "
            "Điều này khẳng định vấn đề có thật trong vận hành hàng ngày, tác nhân có thể tiếp cận ngay để phỏng vấn sâu và khảo sát quy trình.\n\n"
            "- Điều chưa chắc chắn (Uncertainty) của Thẻ A:\n"
            "Tổng tác động định lượng (tổng số giờ lãng phí, chi phí tài chính phát sinh) chưa được đo lường chính xác. Tuy nhiên, điều chưa chắc chắn này "
            "có thể được kiểm chứng nhanh chóng bằng cách phỏng vấn 12 người đã gửi phiếu hỗ trợ để đo thời gian tiêu tốn trung bình cho mỗi phiếu.\n\n"
            "- Lý do chưa chọn Thẻ B:\n"
            "Con số 'tiết kiệm 200 giờ' của Thẻ B là một chỉ số ảo (phantom metric) hoàn toàn thiếu căn cứ khi chưa xác định được tác nhân (ai làm?) "
            "và quy trình (diễn ra ở bước nào?). Khi không có tác nhân và quy trình cụ thể, đội ngũ không thể tiến hành quan sát thực địa và có nguy cơ cao "
            "xây dựng giải pháp cho một vấn đề không tồn tại trong thực tế."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tiêu chí cốt lõi của một bài toán sản phẩm hợp lệ là tính có thể kiểm chứng được (Verifiability). "
            "Vấn đề có Actor và Evidence dù chưa đo được Impact vẫn có giá trị hơn rất nhiều so với một lời hứa hẹn Impact khổng lồ nhưng không gắn với "
            "bất kỳ con người hay quy trình nghiệp vụ cụ thể nào."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn đúng Thẻ A và nêu lý do (1.0 điểm): Chọn Thẻ A vì có actor rõ ràng và 12 ticket minh chứng thực tế.\n"
            "- Chỉ ra điều chưa chắc chắn của Thẻ A (1.0 điểm): Nêu rõ tác động tài chính/thời gian tổng thể chưa được định lượng nhưng kiểm chứng được.\n"
            "- Phân tích lý do bác bỏ Thẻ B (1.0 điểm): Chỉ ra Thẻ B thiếu cả actor và workflow, con số 200 giờ là suy đoán vô căn cứ."
        ),
        "reference_source": "Torres, T. (2021). Continuous Discovery Habits (https://www.producttalk.org/); Bland, D. J., & Osterwalder, A. (2019). Testing Business Ideas. Wiley (https://www.strategyzer.com/library/testing-business-ideas)"
    }

    # 10. d02-q018 (3 pts) [kc-rapid-problem-validation]
    data["d02-q018"] = {
        "sample_answer": (
            "1. Kết luận kiểm chứng cân bằng (Balanced Validation Finding):\n"
            "Vấn đề thời gian duyệt nghỉ phép kéo dài KHÔNG PHẢI là vấn đề hệ thống mang tính phổ quát đối với mọi nhân viên, mà là sự phân hóa hành vi rõ rệt giữa hai nhóm: "
            "nhóm gặp khó khăn (3/5 người mất trên 20 phút) do không tiếp cận được công cụ chuẩn, và nhóm tối ưu (2/5 người chỉ mất dưới 3 phút nhờ sử dụng biểu mẫu có sẵn). "
            "Điều này chứng minh bản thân quy trình đã có giải pháp nhanh hiệu quả, điểm nghẽn nằm ở khâu nhận thức, đào tạo và sự sẵn có của biểu mẫu chuẩn hóa.\n\n"
            "2. Sửa lại bài toán ứng viên (Reframed Candidate Problem):\n"
            "- Đề bài ban đầu chưa sửa: 'Ứng dụng AI để tự động hóa toàn bộ quy trình xin nghỉ phép'.\n"
            "- Bài toán đã sửa chuẩn xác: 'Làm thế nào để chuẩn hóa và đưa biểu mẫu nghỉ phép có sẵn tích hợp trực tiếp vào giao diện làm việc hàng ngày của 100% nhân viên, "
            "kết hợp tự động điền sẵn thông tin cá nhân cơ bản để giảm thời gian tạo đơn của nhóm 3 người từ trên 20 phút xuống dưới 3 phút như nhóm sử dụng mẫu?'"
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Khám phá nhanh (Rapid Validation) giúp ngăn ngừa việc phức tạp hóa vấn đề bằng AI. "
            "Khi một bộ phận người dùng đã thực hiện công việc cực nhanh nhờ công cụ đơn giản (mẫu sẵn), giải pháp đúng đắn là nhân rộng mẫu chuẩn "
            "thay vì đầu tư một hệ thống tự động hóa cồng kềnh."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Kết luận kiểm chứng cân bằng khách quan (1.5 điểm): Nhận diện đúng sự phân hóa giữa 2 nhóm, quy trình đã có cách làm nhanh (dưới 3 phút nhờ mẫu) nên không phải nút thắt hệ thống.\n"
            "- Sửa lại bài toán ứng viên chuẩn xác (1.5 điểm): Chuyển trọng tâm từ tự động hóa AI toàn bộ sang chuẩn hóa và phổ biến biểu mẫu có sẵn để đưa thời gian về dưới 3 phút."
        ),
        "reference_source": "Bland, D. J., & Osterwalder, A. (2019). Testing Business Ideas. Wiley (https://www.strategyzer.com/library/testing-business-ideas); Nielsen Norman Group - Discovery Phase (https://www.nngroup.com/articles/discovery-phase/)"
    }

    # 11. d02-q019 (3 pts) [kc-existing-solution-gap-research]
    data["d02-q019"] = {
        "sample_answer": (
            "Ghi chú nghiên cứu giải pháp hiện có (Solution Gap Analysis):\n\n"
            "1. Phạm vi quy trình đã được chứng minh (Demonstrated Scope):\n"
            "- Luồng chuẩn thuận lợi (Happy Path): Tự động tiếp nhận email -> Sử dụng mô hình ngôn ngữ để trích xuất mã vận đơn/đơn hàng -> Gọi API truy vấn trạng thái đơn -> Tự động soạn thảo email trả lời khách hàng dưới dạng bản nháp.\n\n"
            "2. Khoảng trống quy trình và rủi ro vận hành (Gaps & Risks):\n"
            "- Khoảng trống xử lý lỗi hệ thống (Fault Tolerance Gap): Không có kịch bản xử lý khi API tra cứu bị timeout, trả mã lỗi 500 hoặc đơn hàng không tồn tại, có thể khiến bot sinh ảo giác xin lỗi sai lệch.\n"
            "- Rủi ro bảo mật và toàn vẹn dữ liệu: Không xử lý yêu cầu thay đổi địa chỉ giao hàng (yêu cầu nhạy cảm liên quan đến gian lận chuyển hướng đơn) do thiếu xác thực danh tính chủ tài khoản.\n"
            "- Rủi ro giao tiếp: Thiếu bước phê duyệt của con người (Human-in-the-loop review) trước khi gửi thư, dẫn đến nguy cơ gửi thông tin sai lệch trực tiếp tới khách hàng.\n\n"
            "3. Bài học có thể tái sử dụng cho thiết kế mới (Reusable Lessons):\n"
            "- Kế thừa khả năng trích xuất thực thể (NER) và soạn nháp tự động từ email.\n"
            "- Bắt buộc phải bổ sung: (1) Cơ chế Retry và Fallback an toàn khi API lỗi; (2) Cơ chế xác thực OTP/chuyển tiếp nhân viên cho các tác vụ thay đổi thông tin đơn hàng; (3) Giao diện 'Một cú nhấp chuột' (One-click approval) để tư vấn viên kiểm duyệt nháp trước khi phát đi."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Phân tích khoảng trống giải pháp (Solution Gap Research) giúp kế thừa những thành phần đã được chứng minh hiệu quả "
            "trong khi chủ động nhận diện và bọc lót các điểm mù kiến trúc (Edge Cases, API Failures, State Mutation Risks) trước khi đưa vào sản xuất."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phạm vi đã chứng minh (1.0 điểm): Nêu rõ luồng trích xuất mã, gọi API tra cứu và sinh bản nháp trả lời email.\n"
            "- Khoảng trống và rủi ro trọng yếu (1.0 điểm): Chỉ ra thiếu xử lý lỗi API, rủi ro khi đổi địa chỉ và thiếu khâu phê duyệt trước khi gửi.\n"
            "- Bài học tái sử dụng cụ thể (1.0 điểm): Đề xuất tái sử dụng phần trích xuất nháp và bổ sung fallback khi lỗi API cùng giao diện duyệt human-in-the-loop."
        ),
        "reference_source": "Google Cloud Architecture Center - Patterns for Resilient AI Architectures (https://cloud.google.com/architecture); Nygard, M. T. (2018). Release It!. Pragmatic Bookshelf (https://pragprog.com/titles/mnee2/release-it-second-edition/)"
    }

    # 12. d02-q020 (3 pts) [kc-existing-solution-gap-research]
    data["d02-q020"] = {
        "sample_answer": (
            "Ghi chú nghiên cứu và thẩm định giải pháp nhà cung cấp:\n\n"
            "1. Phạm vi đã được chứng minh (Demonstrated Scope):\n"
            "Hệ thống của nhà cung cấp chỉ mới chứng minh được khả năng Hỗ trợ nhận thức (Cognitive Augmentation): Tự động phân loại nhãn và định tuyến ticket hỗ trợ, "
            "kèm theo đề xuất câu trả lời mẫu dưới dạng bản nháp nội bộ cho tổng đài viên.\n\n"
            "2. Khoảng trống thực tế (Reality Gaps):\n"
            "Hoàn toàn thiếu bằng chứng về việc thực thi hành động tự động (Autonomous Actions), thiếu quy trình chuyển cấp có kiểm soát (Escalation Framework) cho các ca phức tạp, "
            "và không có dữ liệu kiểm định về tỷ lệ ảo giác, tỷ lệ lỗi xử lý hoặc phản ứng khi người dùng giận dữ.\n\n"
            "3. Rủi ro triển khai (Deployment Risks):\n"
            "Khẳng định 'tự động hóa toàn bộ' là chiêu bài quảng cáo quá đà (AI Marketing Overpromise). Nếu công ty giao toàn quyền tự động trả lời cho khách hàng, "
            "các lỗi trả lời sai chính sách, cam kết sai thông tin tài chính hoặc giọng điệu thiếu đồng cảm sẽ phá hủy trải nghiệm khách hàng và gây khủng hoảng thương hiệu.\n\n"
            "4. Bài học có thể sử dụng (Actionable Lessons):\n"
            "Chỉ nên mua và tích hợp giải pháp này ở vai trò 'Trợ lý hỗ trợ nhân viên' (Copilot Mode) để tăng tốc độ phân loại và soạn thảo của tổng đài viên, "
            "tuyệt đối không bật chế độ tự hành hoàn toàn (Auto-pilot)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: 'Caveat Emptor' trong kỷ nguyên AI. Người làm sản phẩm phải biết lột bỏ lớp vỏ tiếp thị 'Full Automation' "
            "để soi chiếu vào các bằng chứng kỹ thuật thực tế. Giữ vai trò con người trong vòng lặp (Human-in-the-loop) là nguyên tắc an toàn sống còn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xác định đúng phạm vi đã chứng minh (1.0 điểm): Nêu rõ chỉ mới phân loại ticket và đề xuất bản nháp (mức hỗ trợ/copilot).\n"
            "- Chỉ ra khoảng trống và rủi ro tiếp thị quá đà (1.0 điểm): Nhận diện việc thiếu hành động/escalation/đo lỗi và rủi ro uy tín nếu tự động hóa toàn bộ.\n"
            "- Đưa ra bài học ứng dụng đúng mức (1.0 điểm): Khuyến nghị chỉ áp dụng ở vai trò copilot/hỗ trợ nhân viên, không bật chế độ tự hành gửi tin trực tiếp."
        ),
        "reference_source": "Cagan, M. (2017). Inspired (https://www.svpg.com/books/inspired/); Davenport, T., & Ronanki, R. (2018). Artificial Intelligence for the Real World. Harvard Business Review (https://hbr.org/2018/01/artificial-intelligence-for-the-real-world)"
    }

    # 13. d02-q021 (3 pts) [kc-current-workflow-mapping]
    data["d02-q021"] = {
        "sample_answer": (
            "1. Sơ đồ quy trình hiện trạng (Current Workflow Mapping):\n"
            "- Bước 1: [Khách hàng] -> Đầu vào: Yêu cầu mua hàng -> [Kinh doanh] nhận biểu mẫu -> Đầu ra: Biểu mẫu khách hàng.\n"
            "- Bước 2: [Kinh doanh] -> Đầu vào: Biểu mẫu -> Công cụ: Bảng tính (Spreadsheet) -> Đầu ra: Dữ liệu đơn nhập vào bảng tính.\n"
            "- Bước 3 (Điểm bàn giao 1): [Kỹ sư giải pháp] đọc bảng tính -> Công cụ: ERP -> Đối soát số dư tồn kho -> Đầu ra: Kết quả kiểm tra tồn kho.\n"
            "- Bước 4 (Vòng lặp ma sát): Nếu thiếu hàng, [Kỹ sư giải pháp] gửi email phản hồi -> [Kinh doanh] tiếp nhận email.\n"
            "- Bước 5 (Điểm bàn giao 2): [Kinh doanh] sửa đổi biểu mẫu yêu cầu -> gửi lại cho Kỹ sư giải pháp.\n\n"
            "2. Đánh giá điểm ma sát và tính xác thực của nút thắt:\n"
            "- Điểm ma sát có bằng chứng (Empirical Friction Point): Vòng lặp chuyển giao qua lại giữa Bước 4 và Bước 5 xảy ra với tần suất cao: 11/30 yêu cầu bị trả lại (tỷ lệ lỗi vòng lặp lên tới 36,7%).\n"
            "- Đã đủ dữ liệu để gọi là nút thắt (Bottleneck) hay chưa?: CHƯA ĐỦ DỮ LIỆU. Mặc dù tỷ lệ lặp lại cao (36,7%), nhưng dữ liệu hiện tại chưa đo lường thời gian xử lý của từng bước (thời gian Kỹ sư tra ERP, thời gian email chờ phản hồi, thời gian sửa biểu mẫu). "
            "Một điểm chỉ được kết luận là nút thắt hệ thống khi nó chiếm tỷ trọng áp đảo trong tổng thời gian trễ (Lead Time) của toàn chu trình.\n\n"
            "3. Điều chưa biết cần thu thập thêm: Thời gian chờ phản hồi email trung bình giữa Kinh doanh và Kỹ sư; nguyên nhân vì sao khách/kinh doanh chọn hàng thiếu tồn kho (do bảng giá cũ hay không xem được tồn kho thời gian thực?)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong lý thuyết các điểm hạn chế (Theory of Constraints - TOC), tỷ lệ phát sinh lại công việc (Rework Rate) "
            "là dấu hiệu của ma sát, nhưng Nút thắt thực sự được định nghĩa bởi lưu lượng dòng chảy và thời gian chờ (Cycle Time / Wait Time). "
            "Cần đo lường thời gian phân đoạn trước khi vội vã đưa AI vào giải quyết."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Lập sơ đồ quy trình đủ các yếu tố (1.0 điểm): Trình bày rõ các bước kèm người thực hiện, đầu vào/đầu ra, công cụ và điểm bàn giao.\n"
            "- Nhận diện điểm ma sát có bằng chứng (1.0 điểm): Nêu rõ vòng lặp trả lại ở bước 4 chiếm 11/30 đơn (36,7%).\n"
            "- Phân tích vì sao chưa thể kết luận nút thắt (1.0 điểm): Chỉ ra thiếu số liệu thời gian từng bước và nêu điều chưa biết cần đo thêm."
        ),
        "reference_source": "Goldratt, E. M. (1984). The Goal: A Process of Ongoing Improvement (https://www.tocico.org/); Lean Enterprise Institute (https://www.lean.org/)"
    }

    # 14. d02-q022 (3 pts) [kc-current-workflow-mapping]
    data["d02-q022"] = {
        "sample_answer": (
            "1. Quy trình hiện trạng chi tiết:\n"
            "- Bước 1: [Khách hàng] -> Yêu cầu gửi qua email -> [CSKH] tiếp nhận.\n"
            "- Bước 2: [CSKH] -> Sao chép nội dung từ email -> Công cụ: Hệ thống CRM -> Đầu ra: Ticket hồ sơ trong CRM.\n"
            "- Bước 3: [CSKH / Chuyên viên] -> Đọc ticket -> Công cụ: Wiki nội bộ -> Đầu ra: Điều khoản chính sách áp dụng.\n"
            "- Bước 4: [CSKH] -> Soạn thảo câu trả lời nháp -> Đầu ra: Bản nháp email phản hồi.\n"
            "- Bước 5 (Điểm bàn giao kiểm soát): Nếu giá trị hồ sơ > 10 triệu đồng -> [CSKH] bàn giao ticket cho [Trưởng nhóm] duyệt -> [Trưởng nhóm] phê duyệt -> [CSKH] gửi thư cho khách.\n\n"
            "2. Đánh giá định lượng nút thắt:\n"
            "- Điểm đáng đo thêm: (1) Thời gian tra cứu tài liệu trên wiki ở Bước 3; (2) Thời gian chờ Trưởng nhóm phê duyệt ở Bước 5; (3) Tỷ lệ hồ sơ có giá trị trên 10 triệu đồng so với toàn bộ yêu cầu.\n"
            "- Đã đủ dữ liệu để định lượng nút thắt chưa?: CHƯA ĐỦ DỮ LIỆU. Nhật ký mới chỉ ghi nhận trình tự các bước thực hiện, hoàn toàn chưa có dấu thời gian (timestamps) "
            "cho từng chặng, chưa có tỷ lệ lỗi hoặc số lượng yêu cầu bị ứ đọng tại hàng đợi phê duyệt của Trưởng nhóm.\n"
            "- Điều còn thiếu: Phân rã thời gian xử lý thực tế (Active Handling Time) của CSKH so với thời gian hồ sơ nằm chờ ở trạng thái nhàn rỗi (Idle Wait Time) tại Bước 5."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Lập bản đồ chuỗi giá trị (Value Stream Mapping - VSM) phân biệt giữa 'Thời gian tạo giá trị' "
            "(Touch Time: đọc wiki, soạn nháp) và 'Thời gian chờ lãng phí' (Queue/Wait Time: chờ sếp duyệt). Không thể tối ưu hóa quy trình "
            "nếu không có số liệu phân rã giữa hai loại thời gian này."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Lập sơ đồ quy trình hiện trạng chuẩn (1.0 điểm): Trình bày đủ 5 bước với người thực hiện, đầu vào/ra và điểm bàn giao phê duyệt.\n"
            "- Chỉ ra các điểm đáng đo thêm (1.0 điểm): Đề xuất đo thời gian tra wiki, thời gian chờ duyệt và tỷ lệ hồ sơ trên 10 triệu đồng.\n"
            "- Khẳng định chưa đủ dữ liệu nút thắt (1.0 điểm): Nêu rõ việc thiếu timestamp, thiếu thời gian hàng đợi chờ duyệt (wait time) để định vị nút thắt."
        ),
        "reference_source": "Rother, M., & Shook, J. (2003). Learning to See: Value Stream Mapping. Lean Enterprise Institute (https://www.lean.org/lexicon-terms/value-stream-mapping/)"
    }

    # 15. d02-q023 (4 pts) [kc-future-workflow-redesign]
    data["d02-q023"] = {
        "sample_answer": (
            "1. Thiết kế quy trình tương lai với ranh giới rõ ràng giữa AI, Luật tự động và Con người:\n"
            "- Phân ranh giới kỹ thuật:\n"
            "+ Tự động hóa bằng API/Luật (Deterministic Rules): Tự động đồng bộ yêu cầu từ email vào CRM qua webhook/API (loại bỏ khâu chép tay thủ công); tự động phân loại ngưỡng giá trị hồ sơ (8% rủi ro cao vs 92% rủi ro thấp) dựa trên trường dữ liệu số tiền.\n"
            "+ Tác nhân AI (RAG / Copilot): Tự động đọc nội dung ticket, thực hiện tìm kiếm ngữ nghĩa trên 3 trang wiki nghiệp vụ và trích xuất đúng điều khoản liên quan, sau đó soạn sẵn một bản nháp trả lời hoàn chỉnh kèm trích dẫn nguồn (giải quyết triệt để nút thắt 18 phút tra cứu).\n"
            "+ Con người (Human-in-the-loop):\n"
            "  * Đối với 92% yêu cầu rủi ro thấp: CSKH chỉ cần xem nhanh bản nháp do AI soạn, chỉnh sửa nếu cần và bấm gửi (bỏ khâu Trưởng nhóm duyệt toàn bộ).\n"
            "  * Đối với 8% yêu cầu rủi ro cao: Hệ thống tự động chuyển tiếp hồ sơ và bản nháp đã chuẩn bị sẵn cho Trưởng nhóm thẩm định và phê duyệt trước khi gửi đi.\n\n"
            "2. Đường lui khi hệ thống AI gặp sự cố (Fallback Mechanism):\n"
            "Nếu hệ thống AI bị timeout hoặc độ tin cậy trích xuất wiki thấp (< 0,7), hệ thống tự động đánh dấu cờ cảnh báo và trả về giao diện tra cứu wiki truyền thống với các đường link gợi ý để CSKH tự tra cứu thủ công mà không làm gián đoạn luồng công việc.\n\n"
            "3. Hai chỉ số đo lường trước / sau cải tiến:\n"
            "- Chỉ số 1 (Thời gian chu trình): Thời gian xử lý trung bình mỗi yêu cầu của CSKH (Handling Time) — Mục tiêu: Giảm từ 25 phút xuống dưới 6 phút.\n"
            "- Chỉ số 2 (Thời gian hàng đợi): Thời gian chờ phê duyệt trung bình của hồ sơ (Queue Wait Time) — Mục tiêu: Giảm 85% do giải phóng Trưởng nhóm khỏi 92% hồ sơ rủi ro thấp."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tái thiết kế quy trình (Business Process Re-engineering) tập trung giải quyết đúng điểm nghẽn nặng nhất "
            "(tra wiki 18/25 phút) và chuyển đổi từ mô hình 'Kiểm soát toàn diện 100%' sang 'Kiểm soát theo rủi ro' (Risk-based Exception Approval). "
            "Kết quả là giải phóng thời gian cho quản lý và tăng năng suất cho nhân viên tuyến đầu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Phân định ranh giới AI, Luật và Con người chuẩn xác (1.5 điểm): Luật phân loại 8% rủi ro cao; AI RAG tra 3 wiki và soạn nháp; Con người kiểm duyệt theo phân cấp rủi ro.\n"
            "- Thiết kế đường lui khi AI lỗi (1.0 điểm): Nêu cơ chế fallback về giao diện tra cứu thủ công có gợi ý link khi AI timeout/độ tin cậy thấp.\n"
            "- Hai chỉ số đo lường trước/sau cụ thể (1.5 điểm): Nêu rõ chỉ số thời gian xử lý yêu cầu (giảm từ 25 phút xuống dưới 6 phút) và thời gian chờ duyệt của trưởng nhóm."
        ),
        "reference_source": "Hammer, M. (1990). Reengineering Work: Don't Automate, Obliterate. Harvard Business Review (https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate); Google Cloud AI Adoption Framework (https://cloud.google.com/ai-adoption)"
    }

    # 16. d02-q024 (4 pts) [kc-future-workflow-redesign]
    data["d02-q024"] = {
        "sample_answer": (
            "1. Ba điểm không an toàn nghiêm trọng trong đề xuất ban đầu:\n"
            "- Điểm không an toàn 1: Mô hình tự động loại hồ sơ mà không lưu lý do cho điểm, vi phạm nghiêm trọng tính giải trình (Explainability) và tính tuân thủ pháp lý lao động (nguy cơ thiên kiến/phân biệt đối xử ngầm mà không kiểm toán được).\n"
            "- Điểm không an toàn 2: Mô hình tự động ra quyết định loại bỏ (Autonomous rejection without human oversight) đối với các hồ sơ < 0,6 trong khi các mô hình AI sàng lọc CV có sai số và ảo giác cao.\n"
            "- Điểm không an toàn 3: Khi dịch vụ AI gặp sự cố, hồ sơ bị âm thầm bỏ khỏi hàng đợi, làm mất mát dữ liệu ứng viên và phá vỡ tính sẵn sàng của hệ thống.\n\n"
            "2. Vẽ lại ranh giới Người - Máy an toàn:\n"
            "- Máy móc (AI System): Đóng vai trò là công cụ trích xuất và đề xuất (Scoring & Feature Extraction). Khi chấm điểm, AI bắt buộc phải tạo ra bảng phân tích tiêu chí chi tiết (ví dụ: số năm kinh nghiệm, kỹ năng khớp, chứng chỉ) kèm trích dẫn từ CV làm cơ sở giải trình. AI TUYỆT ĐỐI KHÔNG tự động loại hồ sơ.\n"
            "- Con người (HR Recruiter): Là người đưa ra quyết định từ chối hoặc mời phỏng vấn cuối cùng dựa trên bảng tóm tắt tiêu chí do AI gợi ý.\n\n"
            "3. Thiết kế đường lui khi dịch vụ gặp sự cố (Fallback Mechanism):\n"
            "Khi dịch vụ mô hình AI bị lỗi hoặc quá tải, toàn bộ CV ứng viên được đẩy vào hàng đợi dự phòng (Dead Letter Queue / Fallback Ingestion Queue) "
            "và chuyển sang luồng tiếp nhận truyền thống an toàn để nhân viên tuyển dụng xem xét thủ công tuần tự, bảo đảm không bao giờ làm mất bất kỳ hồ sơ nào.\n\n"
            "4. Hai chỉ số theo dõi rủi ro (Risk Monitoring Metrics):\n"
            "- Chỉ số 1 (Tỷ lệ sai sót loại trừ - False Rejection Rate): Tỷ lệ ứng viên tiềm năng bị mô hình chấm điểm dưới 0,6 nhưng thực tế đạt tiêu chuẩn khi chuyên viên nhân sự kiểm tra ngẫu nhiên (Audit sample).\n"
            "- Chỉ số 2 (Độ trôi và phân phối điểm - Score Distribution Drift): Theo dõi tỷ lệ hồ sơ rơi vào nhóm < 0,6 theo thời gian và theo các nhóm nhân khẩu học để phát hiện sớm hiện tượng thiên kiến (Bias/Fairness drift)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tuyển dụng là lĩnh vực rủi ro cao (High-risk AI System theo EU AI Act). Mọi quyết định ảnh hưởng đến quyền lợi "
            "con người bắt buộc phải có sự giám sát của con người (Human Oversight) và giải trình được lý do (Right to Explanation). Thiết kế hệ thống AI có trách nhiệm "
            "bắt đầu từ việc bảo đảm quyền tự quyết của con người."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Chỉ ra 3 điểm không an toàn (1.0 điểm): Nhận diện đúng việc tự loại không lưu lý do, thiếu giải trình và việc làm rơi mất hồ sơ khi lỗi.\n"
            "- Vẽ lại ranh giới Người - Máy chuẩn mực (1.0 điểm): AI chỉ trích xuất tiêu chí và giải trình; Con người giữ quyền quyết định loại bỏ cuối cùng.\n"
            "- Cơ chế đường lui dự phòng (1.0 điểm): Đưa hồ sơ vào fallback queue và xử lý thủ công an toàn khi dịch vụ AI lỗi.\n"
            "- Hai chỉ số kiểm soát rủi ro (1.0 điểm): Nêu rõ chỉ số tỷ lệ loại oan (False Rejection) và chỉ số trôi dạt phân phối/thiên kiến (Bias drift)."
        ),
        "reference_source": "EU Artificial Intelligence Act (High-Risk AI Requirements) (https://artificialintelligenceact.eu/); Barocas, S., et al. (2019). Fairness and Machine Learning (https://fairmlbook.org/)"
    }

    # 17. d02-q026 (3 pts) [kc-baseline-bottleneck-quantification]
    data["d02-q026"] = {
        "sample_answer": (
            "1. Kế hoạch thiết lập Đường cơ sở – Mục tiêu – Đo lường trung thực:\n"
            "- Chỉ số đo lường chính (Metric): Thời gian chu trình xử lý yêu cầu (Resolution Lead Time).\n"
            "- Đơn vị đo: Phút (hoặc Giờ).\n"
            "- Điểm đo (Measurement Points): Bắt đầu bấm giờ ngay khi yêu cầu được ghi nhận vào hệ thống (Timestamp Tiếp nhận) và kết thúc khi câu trả lời được gửi thành công cho khách hàng (Timestamp Hoàn tất).\n"
            "- Khoảng thời gian thu thập đường cơ sở: Thu thập liên tục trên toàn bộ 2.000 yêu cầu trong vòng 30 ngày để lấy mẫu đại diện đầy đủ các ngày trong tuần và khung giờ cao điểm.\n"
            "- Phân rã dữ liệu đo: Đo riêng thời gian chờ trong hàng đợi (Wait Time) và thời gian xử lý tích cực của nhân viên (Active Touch Time), kèm phân loại theo loại yêu cầu và tỷ lệ lỗi.\n"
            "- Mục tiêu cải tiến: Chỉ thiết lập mục tiêu phần trăm (ví dụ giảm 40% thời gian xử lý P50 và P95) SAU KHI đã có số liệu baseline chính thức.\n\n"
            "2. Vì sao chưa thể kết luận nút thắt ở thời điểm hiện tại:\n"
            "Bởi vì hiện tại hoàn toàn chưa có số liệu đo lường thời gian phân đoạn và chưa thống kê tỷ lệ lỗi của từng khâu. "
            "Một nút thắt chỉ có thể được kết luận khi có bằng chứng định lượng chứng minh khâu đó chiếm tỷ trọng thời gian lớn nhất hoặc gây ứ đọng hàng đợi nghiêm trọng nhất. "
            "Mọi nhận định về nút thắt lúc này chỉ là phỏng đoán cảm tính."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: 'Nếu bạn không thể đo lường nó, bạn không thể cải tiến nó' (Lord Kelvin). "
            "Trong cải tiến quy trình Lean Six Sigma, giai đoạn Đo lường (Measure) phải đi trước giai đoạn Phân tích (Analyze) và Cải tiến (Improve). "
            "Thiết lập mục tiêu cải tiến khi chưa có baseline là vi phạm nguyên tắc cơ bản của khoa học quản trị."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Kế hoạch đo lường baseline trung thực (1.5 điểm): Nêu đủ tên chỉ số, đơn vị (phút/giờ), điểm đo (timestamp bắt đầu - kết thúc) và khoảng thu thập 30 ngày.\n"
            "- Giải thích vì sao chưa thể kết luận nút thắt (1.5 điểm): Phân tích việc chưa có dữ liệu thời gian phân đoạn và tỷ lệ lỗi khiến mọi kết luận về nút thắt chỉ là suy đoán cảm tính."
        ),
        "reference_source": "George, M. L. (2002). Lean Six Sigma. McGraw-Hill; Google SRE Book - Service Level Indicators (https://sre.google/sre-book/service-level-objectives/)"
    }

    # 18. d02-q027 (3 pts) [kc-output-input-metrics]
    data["d02-q027"] = {
        "sample_answer": (
            "1. Hai chỉ số đầu vào (Input Metrics) mà đội ngũ có thể tác động trực tiếp:\n"
            "- Chỉ số đầu vào 1: Tỷ lệ hồ sơ được chuẩn hóa và tự động kiểm tra tính đầy đủ của trường dữ liệu trước khi gửi (Input Data Validation Pass Rate).\n"
            "- Chỉ số đầu vào 2: Tỷ lệ tài liệu tham chiếu/chính sách được cập nhật mới nhất và gắn thẻ metadata chính xác trong kho tri thức RAG (Knowledge Base Freshness & Coverage Rate).\n\n"
            "2. Giả thuyết nối chỉ số đầu vào với chỉ số kết quả sản phẩm:\n"
            "\"NẾU chúng ta tăng tỷ lệ hồ sơ có dữ liệu đầu vào đầy đủ và chuẩn hóa lên trên 95% thông qua bộ kiểm tra biểu mẫu tự động, "
            "THÌ tỷ lệ hồ sơ được duyệt đúng ngay lần đầu (First-Time-Right Approval Rate - Output Metric) sẽ tăng tối thiểu 20%, "
            "bởi vì việc loại bỏ các thông tin thiếu sót hoặc mơ hồ từ đầu vào sẽ giúp người thẩm định không phải trả lại hồ sơ để yêu cầu bổ sung thông tin.\"\n\n"
            "3. Phép kiểm tra để tránh đồng nhất độ chính xác mô hình với kết quả sản phẩm:\n"
            "Thực hiện đo lường độc lập hai chỉ số song song: Đo Độ chính xác kỹ thuật của mô hình (Model F1-score/Accuracy trên tập test) VÀ Đo Tỷ lệ hồ sơ thực tế được duyệt thành công ngoài đời thực. "
            "Nếu mô hình đạt độ chính xác 95% nhưng tỷ lệ duyệt đúng lần đầu vẫn không tăng (ví dụ do người dùng không tin tưởng gợi ý của AI, hoặc do chính sách nội bộ bị thay đổi ngoài phạm vi mô hình), "
            "điều đó chứng minh độ chính xác kỹ thuật của mô hình không đồng nhất với giá trị thực tế của sản phẩm."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Phân biệt giữa Input Metrics (những việc ta có thể trực tiếp kiểm soát/thao tác) và Output Metrics (kết quả nghiệp vụ ta mong muốn). "
            "Đồng thời, tránh 'Bẫy đo lường AI' (AI Metric Fallacy): Mô hình có độ chính xác 99% nhưng đặt vào một quy trình nghiệp vụ sai lầm thì sản phẩm vẫn thất bại."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nêu 2 chỉ số đầu vào tác động được (1.0 điểm): Nêu đúng tính đầy đủ của dữ liệu đầu vào và độ phủ của tri thức tham chiếu.\n"
            "- Viết giả thuyết có cấu trúc nối input -> output (1.0 điểm): Viết giả thuyết rõ ràng 'Nếu... thì... bởi vì...'.\n"
            "- Phép kiểm tra phân biệt độ chính xác mô hình với kết quả sản phẩm (1.0 điểm): Đưa ra phép đối chứng giữa Model Accuracy và Tỷ lệ duyệt thực tế của quy trình."
        ),
        "reference_source": "Doerr, J. (2018). Measure What Matters (https://www.whatmatters.com/); Google PAIR Guidebook - Success Metrics (https://pair.withgoogle.com/guidebook/)"
    }

    # 19. d02-q028 (3 pts) [kc-output-input-metrics]
    data["d02-q028"] = {
        "sample_answer": (
            "1. Chọn hai chỉ số đầu vào (Input Metrics) hợp lý:\n"
            "- Chỉ số đầu vào 1: Tỷ lệ câu trả lời của trợ lý có đính kèm trích dẫn nguồn bằng chứng có thể kiểm chứng từ tài liệu chính thức (Evidence Grounding Rate).\n"
            "- Chỉ số đầu vào 2: Tỷ lệ người dùng xác nhận đã hiểu và hài lòng với giải pháp ngay tại phiên hỗ trợ đầu tiên (First-Contact Confirmation Rate).\n\n"
            "2. Giả thuyết có thể kiểm chứng (Testable Hypothesis):\n"
            "\"Nếu hệ thống nâng tỷ lệ câu trả lời có trích dẫn bằng chứng cụ thể từ 60% lên trên 90%, thì tỷ lệ yêu cầu phải mở lại (Re-open Rate) "
            "được kỳ vọng sẽ giảm từ mức 18% hiện tại xuống dưới 8% trong giai đoạn thử nghiệm A/B kéo dài 4 tuần.\"\n\n"
            "3. Thận trọng về quan hệ nhân quả:\n"
            "Giả thuyết trên chỉ phát biểu một mối tương quan kỳ vọng có thể quan sát và đo lường được trong thực nghiệm. Chúng ta KHÔNG KHẲNG ĐỊNH quan hệ nhân quả tuyệt đối, "
            "bởi vì việc khách hàng mở lại yêu cầu có thể xuất phát từ nhiều nguyên nhân ngoại cảnh khác (như chất lượng dịch vụ vận chuyển bên thứ ba, sự cố kỹ thuật của sản phẩm, "
            "hoặc tâm lý người dùng) vốn nằm ngoài tầm kiểm soát của nội dung phản hồi từ AI."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tư duy khoa học thực nghiệm trong quản trị sản phẩm AI đòi hỏi người làm sản phẩm phải khiêm tốn trước dữ liệu. "
            "Việc thiết lập giả thuyết giúp định hướng hành động cải tiến, nhưng luôn phải thừa nhận các biến số gây nhiễu ngoại cảnh trước khi tuyên bố quan hệ nhân quả."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn 2 chỉ số đầu vào hợp lý (1.0 điểm): Nêu đúng tỷ lệ trích dẫn bằng chứng và xác nhận của người dùng tại phiên đầu.\n"
            "- Viết giả thuyết kiểm chứng rõ ràng (1.0 điểm): Trình bày giả thuyết định lượng kỳ vọng giảm tỷ lệ mở lại trong khung thời gian đo lường cụ thể.\n"
            "- Thận trọng khoa học về quan hệ nhân quả (1.0 điểm): Khẳng định đây là tương quan kỳ vọng, nêu rõ các yếu tố ngoại cảnh gây nhiễu không thể khẳng định nhân quả tuyệt đối."
        ),
        "reference_source": "Kohavi, R., et al. (2020). Trustworthy Online Controlled Experiments (https://exp-platform.com/); Harvard Business Review - A Step-by-Step Guide to Smart Business Experiments (https://hbr.org/2011/03/a-step-by-step-guide-to-smart-business-experiments)"
    }

    # 20. d02-q030 (3 pts) [kc-ai-task-suitability]
    data["d02-q030"] = {
        "sample_answer": (
            "1. Phân chia nhiệm vụ phù hợp giữa AI, Luật tất định và Con người:\n"
            "- Bước 1 (Đọc lý do viết tự do) -> DÙNG AI (LLM): Lý do hoàn tiền của khách hàng sử dụng ngôn ngữ tự nhiên không cấu trúc, đa dạng văn phong, tiếng lóng hoặc ẩn ý. "
            "LLM phù hợp nhất để đọc hiểu ngữ nghĩa, phân loại lý do chính (sản phẩm lỗi, giao trễ, đổi ý) và trích xuất các thực thể thông tin cần thiết.\n"
            "- Bước 2 (Đối chiếu số ngày với chính sách) -> DÙNG LUẬT TẤT ĐỊNH (Deterministic Business Logic / Code): Việc so sánh 'Số ngày kể từ khi nhận hàng' với ngưỡng 'Chính sách 7 ngày hoặc 30 ngày' "
            "là phép so sánh toán học và logic thời gian cứng ($Date_{request} - Date_{delivery} \\le PolicyDays$). Sử dụng code Python/SQL để đảm bảo độ chính xác tuyệt đối 100%, không bao giờ dùng LLM để tính toán vì rủi ro ảo giác số học.\n"
            "- Bước 3 (Quyết định trả tiền) -> PHÂN CẤP CON NGƯỜI & LUẬT:\n"
            "  * Đối với các trường hợp hợp lệ thỏa mãn 100% điều kiện và số tiền nhỏ dưới hạn mức: Luật phần mềm tự động kích hoạt API hoàn tiền.\n"
            "  * Đối với các trường hợp ngoại lệ, số tiền lớn hoặc nghi ngờ gian lận: Chuyển giao diện cho Chuyên viên tài chính (Con người) xem xét và bấm nút phê duyệt cuối cùng.\n\n"
            "2. Một ràng buộc có thể khiến KHÔNG NÊN dùng AI ở Bước 1: Ràng buộc bảo mật dữ liệu cá nhân (GDPR/Luật Bảo vệ Dữ liệu Cá nhân), "
            "nếu lý do hoàn tiền của khách hàng chứa các thông tin nhạy cảm (như bệnh án y tế, số tài khoản ngân hàng, thông tin cá nhân) mà doanh nghiệp không có hạ tầng AI on-premises "
            "hoặc cơ chế ẩn danh hóa (masking/PII redaction) đạt chuẩn."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc phân rã tác vụ (Task Allocation Principle): Giao phần ngôn ngữ tự nhiên mơ hồ cho AI xác suất, "
            "giao phần logic điều kiện và số học cho Mã nguồn tất định, và giao quyền chi tiền/phê duyệt rủi ro cho Con người và Luật kiểm soát. "
            "Không bao giờ dùng LLM làm những việc mà một câu lệnh `if-else` có thể làm tốt hơn và rẻ hơn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân bổ chính xác AI, Luật và Con người (2.0 điểm): Gán đúng AI cho đọc lý do tự nhiên; Luật cho so sánh số ngày; Luật/Con người cho bước chi tiền.\n"
            "- Nêu ràng buộc khiến không dùng AI (1.0 điểm): Chỉ ra ràng buộc bảo vệ dữ liệu cá nhân nhạy cảm (PII/GDPR) hoặc thiếu hạ tầng bảo mật."
        ),
        "reference_source": "Google PAIR Guidebook - Task Allocation (https://pair.withgoogle.com/guidebook/); OWASP Top 10 for LLM - LLM06: Sensitive Information Disclosure."
    }

    # 21. d02-q032 (3 pts) [kc-llm-boundary-support-selection]
    data["d02-q032"] = {
        "sample_answer": (
            "1. Trách nhiệm cốt lõi của Mô hình ngôn ngữ lớn (LLM):\n"
            "Đóng vai trò là Bộ xử lý giao diện tự nhiên và Điều phối nhận thức (Natural Language Interface & Reasoning Engine): "
            "Hiểu ý định (intent), sở thích du lịch và trích xuất các thực thể tham số (điểm đến, ngày đi, ngân sách, số lượng khách) từ câu hỏi tự do của người dùng; "
            "tổng hợp thông tin từ các công cụ hỗ trợ và giải thích lịch trình đề xuất một cách mạch lạc, thân thiện.\n\n"
            "2. Ba cơ chế hỗ trợ kỹ thuật bắt buộc để bảo đảm hệ thống vận hành đúng đắn:\n"
            "- Cơ chế 1: Công cụ gọi API dữ liệu thời gian thực (Real-time Tool Integration): Kết nối API bảng giá vé máy bay/khách sạn để lấy giá chính xác tại thời điểm hiện tại, "
            "vì LLM tĩnh có knowledge cutoff và không thể tự biết giá biến động theo thời gian thực.\n"
            "- Cơ chế 2: Thuật toán tối ưu hóa lịch trình tất định (Deterministic Constraint Optimization Engine): Sử dụng thuật toán quy hoạch tuyến tính hoặc mã nguồn giải quyết bài toán TSP/Lập lịch "
            "để sắp xếp thứ tự điểm tham quan theo đúng khung giờ mở/đóng cửa và khoảng cách địa lý, ngăn chặn việc LLM ảo giác về thời gian biểu.\n"
            "- Cơ chế 3: Cổng phê duyệt và xác thực của người dùng (Human-in-the-loop Confirmation Gate): Một giao diện UI hiển thị bản tóm tắt đặt vé rõ ràng và bắt buộc người dùng "
            "phải bấm nút 'Xác nhận đặt vé' trước khi gọi API thanh toán/xuất vé, tuyệt đối không để LLM tự động kích hoạt hành động tài chính không thể đảo ngược."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mẫu hình kiến trúc 'LLM as Orchestrator with Deterministic Guardrails': LLM xử lý phần tương tác mềm dẻo, "
            "nhưng mọi hành động thay đổi trạng thái thế giới (State Mutation) hoặc đòi hỏi độ chính xác tuyệt đối (Toán học, Lập lịch, Thanh toán) "
            "bắt buộc phải được ủy quyền cho các dịch vụ chuyên dụng và cổng xác nhận của con người."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Nêu đúng trách nhiệm của LLM (1.0 điểm): Hiểu ý định người dùng, trích xuất tham số và tổng hợp giải thích lịch trình.\n"
            "- Nêu đủ 3 cơ chế hỗ trợ kỹ thuật (2.0 điểm): Liệt kê chính xác API giá real-time, thuật toán tối ưu lịch tất định và cổng xác nhận của người dùng trước khi đặt vé."
        ),
        "reference_source": "Anthropic Claude Documentation - Building Systems with Tools (https://docs.anthropic.com/en/docs/build-with-claude/tool-use); LangChain Tool Boundaries (https://python.langchain.com/docs/concepts/tools/)"
    }

    # 22. d02-q034 (3 pts) [kc-ai-readiness-evidence]
    data["d02-q034"] = {
        "sample_answer": (
            "Rà soát từng khoảng trống sẵn sàng và gán bước kiểm chứng cùng người chịu trách nhiệm:\n\n"
            "1. Khoảng trống: 500 nhật ký không rõ sự đồng ý sử dụng dữ liệu (Data Consent Gap)\n"
            "- Bước kiểm chứng: Rà soát điều khoản dịch vụ (Terms of Service) và chính sách quyền riêng tư hiện hành; thực hiện phân loại và làm sạch dữ liệu để loại bỏ thông tin định danh cá nhân (PII Redaction); nếu cần, gửi thông báo xin phép bổ sung.\n"
            "- Người chịu trách nhiệm: Chuyên viên Pháp chế / Cán bộ Bảo vệ Dữ liệu (DPO / Legal Counsel).\n\n"
            "2. Khoảng trống: Bộ kiểm thử chỉ có các trường hợp thuận lợi (Evaluation Bias Gap)\n"
            "- Bước kiểm chứng: Biên soạn bổ sung tối thiểu 100 trường hợp kiểm thử đối kháng (Adversarial Test Cases), các trường hợp biên (Edge Cases), dữ liệu lỗi, mơ hồ và độc hại để đánh giá tính bền bỉ của mô hình.\n"
            "- Người chịu trách nhiệm: Kỹ sư Kiểm thử Đảm bảo Chất lượng AI (AI QA / Test Engineer).\n\n"
            "3. Khoảng trống: Chưa có người chịu trách nhiệm khi hệ thống gặp lỗi (Accountability & Operations Gap)\n"
            "- Bước kiểm chứng: Xây dựng ma trận trách nhiệm RACI và quy trình ứng phó sự cố (Incident Response Runbook); thiết lập kênh tiếp nhận lỗi khẩn cấp và phân công người trực vận hành khi hệ thống sai lệch.\n"
            "- Người chịu trách nhiệm: Quản lý Sản phẩm (Product Manager) phối hợp cùng Trưởng nhóm Vận hành Kỹ thuật (Engineering/Ops Lead)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Khung đánh giá độ sẵn sàng AI (AI Readiness Framework) đòi hỏi sự hội tụ của 4 trụ cột: "
            "Dữ liệu hợp pháp (Legal/Consent), Năng lực kỹ thuật đã kiểm chứng (Robust Evaluation), Quy trình vận hành có người chịu trách nhiệm (Accountability), "
            "và Giá trị kinh doanh đối chứng với đường cơ sở (Baseline). Thiếu bất kỳ trụ cột nào cũng tiềm ẩn rủi ro đình chỉ dự án sau này."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Xử lý khoảng trống pháp lý dữ liệu (1.0 điểm): Nêu bước rà soát ToS/PII redaction và gán trách nhiệm cho Legal/DPO.\n"
            "- Xử lý khoảng trống bộ kiểm thử (1.0 điểm): Đề xuất bổ sung edge cases/adversarial testing và gán trách nhiệm cho QA Engineer.\n"
            "- Xử lý khoảng trống trách nhiệm sự cố (1.0 điểm): Xây dựng runbook ứng phó sự cố/RACI và gán trách nhiệm cho Product Manager/Ops Lead."
        ),
        "reference_source": "NIST AI Risk Management Framework (NIST AI 100-1); Google Responsible AI Practices (https://ai.google/responsibility/principles/)."
    }

    # 23. d02-q035 (3 pts) [kc-ai-build-buy-decision]
    data["d02-q035"] = {
        "sample_answer": (
            "1. Chọn phương án ở thời điểm hiện tại: Chọn phương án MUA DỊCH VỤ / TẬN DỤNG CÓ SẴN (BUY / SAAS API).\n"
            "Giải thích: Tác vụ tóm tắt biên bản họp là năng lực phổ biến (commodity capability), không phải là yếu tố tạo ra lợi thế cạnh tranh cốt lõi của doanh nghiệp. "
            "Đội ngũ kỹ thuật cực kỳ mỏng (chỉ có 2 kỹ sư) và thời hạn thử nghiệm (pilot) rất gấp trong vòng 3 tuần, trong khi dữ liệu nội bộ đã được cấp phép bảo mật để sử dụng API bên ngoài. "
            "Tự xây dựng (Build) hoặc tự huấn luyện lại mô hình trong bối cảnh này là hoàn toàn bất khả thi và lãng phí nguồn lực.\n\n"
            "2. Đánh đổi chính (Trade-offs):\n"
            "- Ưu điểm: Tốc độ triển khai cực nhanh (có thể tích hợp trong vài ngày), chi phí đầu tư ban đầu thấp, tận dụng được năng lực của các mô hình thương mại hàng đầu.\n"
            "- Rủi ro: Phụ thuộc vào nhà cung cấp bên thứ ba (Vendor lock-in) và chất lượng xử lý tiếng Việt chuyên ngành chưa được chứng minh trên dữ liệu thực tế của công ty.\n\n"
            "3. Bằng chứng thực tế có thể làm ĐẢO QUYẾT ĐỊNH (chuyển sang Tinh chỉnh trên nền có sẵn - Boost/Fine-tune hoặc Tự xây):\n"
            "Nếu trong quá trình thử nghiệm pilot 3 tuần, kết quả đánh giá cho thấy nhà cung cấp tạo ra tỷ lệ lỗi/ảo giác trên 25% đối với các thuật ngữ tiếng Việt chuyên ngành đặc thù, "
            "hoặc chi phí API gọi hàng tháng vượt quá ngân sách dự kiến khi nhân rộng, đội ngũ sẽ chuyển sang phương án 'Boost' (sử dụng mô hình mã nguồn mở như Llama/Qwen kết hợp RAG hoặc LoRA fine-tuning cục bộ)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Khung quyết định Build vs Buy vs Boost (Wardley Mapping & Core vs Context): "
            "Nếu tính năng thuộc vùng 'Context' (không phải cốt lõi khác biệt), nguồn lực mỏng và thời gian gấp -> luôn ưu tiên BUY để kiểm chứng thị trường. "
            "Chỉ chuyển dịch sang BUILD/BOOST khi có bằng chứng định lượng về sự thất bại của giải pháp mua sẵn."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn đúng phương án BUY ở hiện tại (1.0 điểm): Lựa chọn BUY dịch vụ API và lập luận dựa trên tính phổ thông của tác vụ, đội ngũ mỏng (2 người) và hạn 3 tuần.\n"
            "- Phân tích rõ các đánh đổi kỹ thuật (1.0 điểm): Nêu rõ ưu điểm triển khai nhanh đối trọng với rủi ro phụ thuộc vendor và tiếng Việt chuyên ngành.\n"
            "- Bằng chứng định lượng làm đảo quyết định (1.0 điểm): Đưa ra bằng chứng tỷ lệ lỗi tiếng Việt chuyên ngành cao (>25%) hoặc chi phí vượt trần để chuyển sang Boost/Build."
        ),
        "reference_source": "Wardley, S. (2016). Wardley Maps (https://learn.wardleymaps.com/); Cagan, M. - Build vs Buy in Product Management (https://www.svpg.com/buy-vs-build/)"
    }

    # 24. d02-q036 (3 pts) [kc-ai-build-buy-decision]
    data["d02-q036"] = {
        "sample_answer": (
            "1. Chọn phương án ở thời điểm hiện tại: Chọn phương án ĐIỀU CHỈNH TRÊN NỀN CÓ SẴN CỤC BỘ (BOOST / ON-PREMISES OPEN-WEIGHT ADAPTATION).\n"
            "Giải thích: Chẩn đoán lỗi thiết bị là 'khác biệt cốt lõi' của sản phẩm (Core Differentiator), đòi hỏi doanh nghiệp phải nắm giữ và làm chủ tài sản trí tuệ. "
            "Đặc biệt, ràng buộc cứng về an ninh là dữ liệu tuyệt đối không được rời mạng riêng (Private Network), loại bỏ hoàn toàn khả năng sử dụng API đám mây công cộng (Buy SaaS). "
            "Đội ngũ có năng lực Machine Learning mạnh; tuy nhiên, với thời hạn bản trình diễn rất gấp (chỉ 6 tuần), việc tự xây dựng và huấn luyện mô hình nền tảng từ đầu (Build from scratch) là bất khả thi. "
            "Do đó, phương án tối ưu nhất là 'Boost': Lấy một mô hình mã nguồn mở chất lượng cao (như Llama 3, Qwen 2.5), triển khai cục bộ trong mạng riêng và tinh chỉnh (Fine-tuning qua LoRA / RAG) trên dữ liệu thiết bị của công ty.\n\n"
            "2. Bằng chứng có thể làm ĐẢO QUYẾT ĐỊNH (chuyển sang Tự xây hoàn toàn - Build from scratch dài hạn):\n"
            "Nếu kết quả thử nghiệm 6 tuần cho thấy các kiến trúc mô hình ngôn ngữ tổng quát có sẵn không thể giải quyết được các dạng dữ liệu cảm biến chuỗi thời gian (time-series sensor data) "
            "hoặc tín hiệu dao động vật lý đặc thù của thiết bị, và công ty huy động được ngân sách R&D lớn để phát triển một kiến trúc học sâu chuyên biệt hoàn toàn."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mô hình 'Boost' (đứng trên vai người khổng lồ) là chiến lược cân bằng hoàn hảo giữa tính bảo mật dữ liệu nội bộ "
            "(On-premises constraints), quyền sở hữu năng lực cốt lõi (Core IP) và áp lực thời gian ra mắt sản phẩm (Time-to-market). "
            "Tự xây từ đầu trong 6 tuần là ảo tưởng kỹ thuật nguy hiểm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn đúng phương án BOOST cục bộ (1.5 điểm): Lựa chọn tinh chỉnh mô hình mã nguồn mở cục bộ (Boost), thỏa mãn ràng buộc dữ liệu mạng riêng, năng lực ML mạnh và hạn 6 tuần.\n"
            "- Phân tích vì sao loại trừ Build và Buy (1.0 điểm): Giải thích rõ dữ liệu không được ra ngoài loại bỏ Buy SaaS; thời hạn 6 tuần loại bỏ Build from scratch.\n"
            "- Nêu bằng chứng làm đảo quyết định (0.5 điểm): Chỉ ra dữ liệu cảm biến vật lý đặc thù mà mô hình open-weights không xử lý được để chuyển sang tự xây dài hạn."
        ),
        "reference_source": "Gartner Research - Decision Framework for Generative AI (https://www.gartner.com/); NIST AI Risk Management Framework (https://www.nist.gov/itl/ai-risk-management-framework)"
    }

    # 25. d02-q037 (3 pts) [kc-rag-finetuning-selection]
    data["d02-q037"] = {
        "sample_answer": (
            "1. Lựa chọn kiến trúc: Chọn TRUY HỒI / CÔNG CỤ (RETRIEVAL-AUGMENTED GENERATION - RAG).\n"
            "Giải thích: Vấn đề cốt lõi của hệ thống là 'Kiến thức thay đổi động' (chính sách cập nhật liên tục), trong khi mô hình đã làm rất tốt về mặt 'Hành vi và định dạng' khi được cung cấp đúng ngữ cảnh. "
            "Hơn nữa, dự án hoàn toàn chưa có tập dữ liệu huấn luyện có nhãn được rà soát. RAG là giải pháp duy nhất cho phép cập nhật tri thức mới tức thì (Zero-day knowledge update) "
            "chỉ bằng cách cập nhật cơ sở dữ liệu vector mà không cần nạp lại trọng số mô hình.\n\n"
            "2. Cách kiểm chứng thực nghiệm (Validation Method):\n"
            "Xây dựng bộ benchmark gồm 30 câu hỏi về các chính sách vừa mới thay đổi; so sánh câu trả lời của mô hình khi có RAG và khi không có RAG. "
            "Đo lường chỉ số 'Độ chính xác trích dẫn' (Citation Precision) và 'Tính trung thực với ngữ cảnh' (Faithfulness Rate > 95%).\n\n"
            "3. Đánh đổi kỹ thuật (Trade-offs):\n"
            "- Ưu điểm: Cập nhật tri thức tức thời, chi phí vận hành rẻ, loại bỏ ảo giác và có nguồn trích dẫn đối chiếu minh bạch.\n"
            "- Đánh đổi: Tăng độ trễ phản hồi (latency thêm 200-500ms cho khâu embedding/retrieval) và tăng độ phức tạp của hạ tầng đường ống dữ liệu (Vector DB, chunking pipeline)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Ma trận quyết định RAG vs Fine-tuning: "
            "'RAG dùng để cung cấp Kiến thức (Knowledge/Facts), Fine-tuning dùng để định hình Phong cách/Hành vi (Style/Format)'. "
            "Cố gắng dùng Fine-tuning để cập nhật tri thức thường xuyên thay đổi là một phản mẫu kiến trúc (Anti-pattern) tốn kém và không hiệu quả."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Chọn đúng RAG và giải thích thỏa đáng (1.5 điểm): Chọn RAG vì kiến thức biến động liên tục, mô hình đã chuẩn format và thiếu dataset huấn luyện.\n"
            "- Cách kiểm chứng và đánh đổi kỹ thuật (1.5 điểm): Nêu phương pháp kiểm chứng bằng tập test chính sách mới (đo Faithfulness) và phân tích đánh đổi độ trễ/hạ tầng."
        ),
        "reference_source": "Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS 2020. https://arxiv.org/abs/2005.11401; OpenAI - RAG vs Fine-tuning Guide."
    }

    # 26. d02-q038 (3 pts) [kc-rag-finetuning-selection]
    data["d02-q038"] = {
        "sample_answer": (
            "1. Đề xuất bước thích nghi: Kết hợp TINH CHỈNH MÔ HÌNH (SUPERVISED FINE-TUNING - SFT / LORA) TRÊN NỀN RAG HIỆN CÓ (HYBRID RAG + FINE-TUNING).\n"
            "Giải thích: Mô hình đã truy hồi đúng tài liệu pháp lý (RAG đã hoàn thành xuất sắc nhiệm vụ cung cấp kiến thức), nhưng thất bại ở khâu 'Tuân thủ định dạng báo cáo chuyên ngành' (Output Formatting & Stylistic Alignment). "
            "Đội ngũ đang sở hữu tài sản vô cùng giá trị là 8.000 cặp dữ liệu đầu vào-đầu ra chuẩn mực đã được kiểm duyệt. Do đó, phương án tối ưu là sử dụng 8.000 mẫu này để fine-tune mô hình "
            "(thông qua kỹ thuật LoRA/QLoRA), dạy mô hình nắm vững cú pháp cấu trúc và văn phong báo cáo chuyên ngành.\n\n"
            "2. Cách kiểm chứng thực nghiệm (Validation):\n"
            "Chia 8.000 mẫu thành tập Train/Validation/Test (tỷ lệ 80/10/10). Sử dụng tập Test độc lập để đo lường tỷ lệ vượt qua bài kiểm tra cấu trúc (Schema Compliance Rate) "
            "và điểm đánh giá định dạng từ chuyên gia pháp lý (Domain Expert Rubric Score), mục tiêu đạt > 98% tuân thủ định dạng.\n\n"
            "3. Đánh đổi kỹ thuật (Trade-offs):\n"
            "- Lợi ích: Khắc phục triệt để lỗi định dạng báo cáo, giảm độ dài prompt hướng dẫn (tiết kiệm token input) và tăng tốc độ suy luận.\n"
            "- Đánh đổi: Tốn chi phí tính toán GPU cho quá trình huấn luyện, nguy cơ suy giảm năng lực tổng quát (Catastrophic Forgetting) và phải quản lý phiên bản trọng số fine-tuned riêng biệt."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tách biệt triệt để giữa 'What to know' (Nội dung tri thức -> RAG đảm nhiệm) và 'How to speak' "
            "(Cách diễn đạt và định dạng chuyên ngành -> Fine-tuning đảm nhiệm). Khi đã có sẵn 8.000 cặp dữ liệu vàng, Fine-tuning là giải pháp bền vững "
            "để 'đóng bánh' định dạng vào trọng số mô hình thay vì nhồi nhét prompt dài dòng."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Đề xuất phương án thích nghi chuẩn xác (1.5 điểm): Đề xuất Fine-tuning (SFT/LoRA) dựa trên 8.000 mẫu để sửa định dạng, duy trì RAG để lấy tài liệu pháp lý.\n"
            "- Phương pháp kiểm chứng và đánh đổi (1.5 điểm): Thiết lập tập test đo tỷ lệ tuân thủ schema và phân tích đánh đổi chi phí GPU/quản lý checkpoint."
        ),
        "reference_source": "Hu, E. J., et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. ICLR 2022. https://arxiv.org/abs/2106.09685; Anthropic Guide on Fine-tuning vs Prompting."
    }

    # 27. d02-q039 (3 pts) [kc-ai-system-component-decomposition]
    data["d02-q039"] = {
        "sample_answer": (
            "1. Phân rã bốn thành phần kiến trúc hệ thống trợ lý bảo trì:\n"
            "- Mô hình (Model): LLM cơ sở (Foundation LLM) đóng vai trò là bộ suy luận nhận thức (Reasoning Core) để phân tích triệu chứng lỗi, diễn giải số đo cảm biến và tạo nội dung khuyến nghị.\n"
            "- Ngữ cảnh (Context / Knowledge Retrieval): Hệ thống RAG kết nối kho tài liệu sổ tay kỹ thuật (Manuals) được lập chỉ mục kèm siêu dữ liệu (Metadata) phân định chính xác số hiệu model và phiên bản thiết bị (Firmware/Hardware version).\n"
            "- Bước lập kế hoạch (Planning / Workflow Orchestrator): Đồ thị trạng thái hữu hạn (State Machine / Deterministic Workflow) quản lý tuần tự các bước kiểm tra theo quy chuẩn bảo trì kỹ thuật, kiểm soát các điều kiện tiên quyết trước khi chuyển bước.\n"
            "- Công cụ (Tools / APIs): (1) API Gateway đọc dữ liệu cảm biến thời gian thực (IoT Sensor Telemetry API); (2) API tạo phiếu công việc trên hệ thống CMMS/ERP sau khi được cấp phép.\n\n"
            "2. Ranh giới và phần phụ thuộc quan trọng còn thiếu:\n"
            "- Thiếu Bộ lọc đối soát phiên bản (Version Gating Boundary): Cần cơ chế tự động đọc số serial của thiết bị để khóa cứng phiên bản sổ tay tra cứu, tránh trường hợp LLM tra nhầm sổ tay đời cũ.\n"
            "- Thiếu Cổng phê duyệt của con người (Human Approval Gate): Cần giao diện xác thực chữ ký điện tử của kỹ thuật viên trước khi kích hoạt công cụ tạo lệnh công việc trên ERP, ngăn ngừa tạo lệnh rác tự động."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Một ứng dụng AI cấp công nghiệp (Enterprise AI Assistant) không bao giờ chỉ là 'LLM + Chat History'. "
            "Nó đòi hỏi kiến trúc 4 lớp vững chắc: Tầng nhận thức (Model), Tầng tri thức neo đậu (Context), Tầng điều phối trạng thái (Planning), "
            "và Tầng tương tác thế giới thực (Tools) với các chốt kiểm soát an toàn nghiêm ngặt."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân rã đủ 4 thành phần kiến trúc (1.5 điểm): Gán chính xác vai trò của Model, Context (sổ tay metadata), Planning (luồng kiểm tra), và Tools (IoT API, CMMS API).\n"
            "- Chỉ ra ranh giới và phụ thuộc còn thiếu (1.5 điểm): Nêu rõ cơ chế khóa phiên bản thiết bị và cổng phê duyệt của con người trước khi tạo lệnh công việc."
        ),
        "reference_source": "LangChain StateGraph Architecture (https://python.langchain.com/docs/concepts/architecture/); Google Cloud - Industrial GenAI Assistant Design (https://cloud.google.com/architecture)"
    }

    # 28. d02-q040 (3 pts) [kc-ai-system-component-decomposition]
    data["d02-q040"] = {
        "sample_answer": (
            "1. Phân rã bốn thành phần cấu trúc của trợ lý mua hàng:\n"
            "- Thành phần Ngân sách (Memory & Policy State): Dịch vụ quản lý trạng thái tài chính (Financial State Service) lưu trữ ngân sách còn lại của phòng ban từ cơ sở dữ liệu kế toán, không dựa vào bộ nhớ ngữ cảnh dễ trôi của LLM.\n"
            "- Thành phần Tra cứu tồn kho (Inventory Tool): Công cụ API kết nối trực tiếp vào hệ thống quản lý kho (WMS/ERP) để kiểm tra số lượng khả dụng thời gian thực.\n"
            "- Thành phần Phê duyệt (Approval Gate / Workflow Node): Cơ chế định tuyến phê duyệt (Approval Engine) gửi thông báo kèm nút duyệt tới người có thẩm quyền qua Slack/Email khi đơn hàng vượt hạn mức quy định.\n"
            "- Thành phần Đặt hàng (Procurement Execution Tool): API giao dịch idempotent kết nối với nhà cung cấp để phát hành Purchase Order (PO).\n\n"
            "2. Ranh giới còn thiếu khiến quy trình chưa đáng tin cậy:\n"
            "- Thiếu Ranh giới kiểm soát giao dịch và ủy quyền (Authorization & Transaction Boundary): Hiện tại LLM chỉ có lời nhắc (prompt) nên rất dễ bị Prompt Injection hoặc ảo giác tự ý gọi API đặt hàng mà không qua kiểm tra số dư ngân sách thực tế trong DB.\n"
            "- Ranh giới bất biến bắt buộc: API đặt đơn chỉ được phép cấp quyền thực thi (Execution Token) KHI VÀ CHỈ KHI có chữ ký phê duyệt hợp lệ từ cổng kiểm soát của con người."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tách biệt quyền suy luận (Reasoning Authority) khỏi quyền tài chính (Financial Authority). "
            "LLM chỉ được phép đề xuất giỏ hàng (Cart Proposal); việc khóa ngân sách và phát hành lệnh mua phải tuân thủ giao dịch ACID "
            "và cổng ủy quyền nhiều lớp của hệ thống backend doanh nghiệp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân rã đủ 4 thành phần nghiệp vụ (1.5 điểm): Nêu đúng dịch vụ quản lý ngân sách, API tồn kho ERP, cổng phê duyệt và API đặt đơn.\n"
            "- Chỉ ra ranh giới ủy quyền còn thiếu (1.5 điểm): Phân tích việc LLM thiếu kiểm soát ủy quyền, nguy cơ tự đặt đơn và yêu cầu bắt buộc phải có chữ ký phê duyệt trước khi giao dịch."
        ),
        "reference_source": "Martin Fowler - Patterns of Enterprise Application Architecture (https://martinfowler.com/eaaCatalog/); OWASP Top 10 for LLMs - LLM08: Excessive Agency (https://owasp.org/www-project-top-10-for-large-language-model-applications/)"
    }

    # 29. d02-q042 (3 pts) [kc-deterministic-probabilistic-task-allocation]
    data["d02-q042"] = {
        "sample_answer": (
            "Thiết kế phân việc và các điểm kiểm soát cho quy trình duyệt chi phí:\n\n"
            "1. Phân việc hợp lý giữa AI xác suất và Logic tất định:\n"
            "- Phần giao cho AI (LLM Probabilistic Task): Đọc và trích xuất thông tin phi cấu trúc từ mô tả hóa đơn/chứng từ viết tự do (tên nhà cung cấp, loại chi phí, lý do công tác) chuyển thành đối tượng JSON có cấu trúc.\n"
            "- Phần giao cho Mã nguồn tất định (Deterministic Code / Assertions): Kiểm tra toàn bộ các điều kiện bất biến (Invariants) bằng code Python/SQL, tuyệt đối không dùng LLM để thẩm định các quy tắc này.\n\n"
            "2. Ba điểm kiểm soát bất biến (Invariant Control Gates):\n"
            "- Điểm kiểm soát 1 (Toán học số học): `assert round(total_amount, 2) == round(sum(item.amount for item in line_items), 2)`. Nếu lệch dù chỉ 1 đồng, tự động từ chối và báo lỗi tính toán.\n"
            "- Điểm kiểm soát 2 (Tách biệt quyền hạn - Segregation of Duties): `assert approver_id != submitter_id`. Nếu trùng lặp định danh, hệ thống tự động chặn và ném ngoại lệ xung đột lợi ích.\n"
            "- Điểm kiểm soát 3 (Phân cấp thẩm quyền chi tiêu): `if total_amount > 50_000_000: assert 'CFO' in approver_roles`. Nếu số tiền trên 50 triệu mà không có phê duyệt của CFO, hệ thống khóa không cho giải ngân."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Deterministic Invariants Guarding Probabilistic Outputs': "
            "Các quy tắc nghiệp vụ tài chính và tuân thủ pháp lý là các bất biến tuyệt đối (Hard Invariants). "
            "Mọi đầu ra do LLM trích xuất bắt buộc phải đi qua các cổng kiểm tra xác thực (Validation Gates) bằng mã nguồn tất định "
            "trước khi được ghi nhận vào sổ cái kế toán."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân việc đúng bản chất AI và Luật (1.0 điểm): Giao AI đọc mô tả tự nhiên trích JSON; giao code tất định kiểm tra các điều kiện bất biến.\n"
            "- Thiết kế đủ 3 điểm kiểm soát bất biến (2.0 điểm): Nêu rõ code/logic kiểm tra tổng bằng chi tiết, người duyệt khác người nộp và khoản > 50 triệu bắt buộc có CFO duyệt."
        ),
        "reference_source": "Meyer, B. (1992). Applying 'Design by Contract'. IEEE Computer (https://www.eiffel.com/values/design-by-contract/); Google Cloud Architecture - Financial Processing AI Patterns (https://cloud.google.com/architecture)"
    }

    # 30. d02-q045 (3 pts) [kc-prompt-chaining-design]
    data["d02-q045"] = {
        "sample_answer": (
            "1. Thiết kế chuỗi 3 lượt gọi có đầu vào / đầu ra rõ ràng:\n"
            "- Bước 1 (Phân loại): Đầu vào = Văn bản hợp đồng thô. Đầu ra = JSON `{contract_type: 'NDA' | 'Vendor' | 'Employment'}`.\n"
            "- Bước 2 (Trích xuất có điều kiện): Đầu vào = Văn bản hợp đồng + `contract_type`. Đầu ra = JSON chứa các trường điều khoản tương ứng (bảo mật, thanh toán, phạt vi phạm, hiệu lực).\n"
            "- Bước 3 (Tóm tắt rủi ro): Đầu vào = Dữ liệu các điều khoản đã trích xuất hợp lệ. Đầu ra = Báo cáo phân tích rủi ro có cấu trúc kèm điểm cảnh báo.\n\n"
            "2. Điểm kiểm soát chất lượng (Quality Checkpoints):\n"
            "- Giữa Bước 1 và 2: Kiểm tra `contract_type` phải thuộc danh mục hợp lệ. Nếu là 'Khác/Không xác định', dừng chuỗi và chuyển cho chuyên viên pháp chế rà soát thủ công.\n"
            "- Giữa Bước 2 và 3: Sử dụng JSON Schema Validator (code tất định) để kiểm tra xem đã trích xuất đầy đủ 100% các trường bắt buộc hay chưa. "
            "Nếu thiếu trường, tự động kích hoạt thử lại (Retry) với prompt chuyên biệt trích xuất riêng trường bị thiếu; nếu thử lại thất bại thì đánh dấu cờ cảnh báo hồ sơ khiếm khuyết.\n\n"
            "3. Sự phụ thuộc và đánh đổi (Dependencies & Trade-offs):\n"
            "- Sự phụ thuộc: Bước sau phụ thuộc nghiêm ngặt vào dữ liệu của bước trước (Sequential Pipeline).\n"
            "- Đánh đổi: Tăng độ trễ tổng thể (Latency tăng gấp 3 do chạy nối tiếp qua 3 lượt gọi LLM) để đổi lấy khả năng kiểm soát chặt chẽ từng chặng (Granular Controllability), "
            "dễ dàng gỡ lỗi (debuggability) và ngăn chặn ảo giác tích lũy dây chuyền."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mẫu hình Prompt Chaining (Chuỗi lời nhắc) chia nhỏ bài toán lớn thành các bước con tuần tự. "
            "Việc chèn các cổng kiểm soát schema tất định giữa các bước ngăn ngừa hiện tượng 'Garbage In, Garbage Out' lan truyền "
            "trong các đường ống xử lý ngôn ngữ tự nhiên."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Hợp đồng đầu vào/đầu ra từng bước rõ ràng (1.0 điểm): Định nghĩa chuẩn xác input/output cho phân loại, trích xuất và tóm tắt rủi ro.\n"
            "- Điểm kiểm soát từ chối/thử lại (1.0 điểm): Đặt validator giữa các bước để kiểm tra loại hợp đồng và độ đầy đủ của trường bắt buộc.\n"
            "- Phân tích phụ thuộc và đánh đổi độ trễ vs kiểm soát (1.0 điểm): Phân tích rõ việc chấp nhận tăng latency gấp 3 để đạt khả năng kiểm soát chất lượng và debug cao."
        ),
        "reference_source": "Anthropic Claude Prompt Engineering Guide - Chaining Prompts (https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering); LangChain LCEL Chains."
    }

    # 31. d02-q046 (3 pts) [kc-prompt-chaining-design]
    data["d02-q046"] = {
        "sample_answer": (
            "1. Phản biện thiết kế một lượt gọi duy nhất (Single-call monolithic design):\n"
            "Thiết kế 'gộp tất cả làm một' vi phạm nguyên tắc phân tách trách nhiệm (Separation of Concerns). Khi giao cho LLM vừa kiểm tra, vừa phán xét, vừa giải thích trong một prompt: "
            "(1) Mô hình dễ bị quá tải nhận thức dẫn đến ảo giác và bỏ qua các trường dữ liệu thiếu; (2) Thiếu khả năng truy vết nguồn gốc (không thể biết quyết định dựa trên bằng chứng nào trong hồ sơ); "
            "(3) Thiếu tính co giãn khi lỗi (All-or-nothing failure) — nếu xảy ra lỗi mạng hoặc lỗi định dạng ở cuối, toàn bộ kết quả bị hủy và phải chạy lại từ đầu rất tốn kém.\n\n"
            "2. Chuyển đổi thành chuỗi 3 bước chuẩn mực:\n"
            "- Bước 1: [Trích xuất & Kiểm tra tính đầy đủ - Extraction & Schema Validation]\n"
            "  + Input: Hồ sơ ứng viên thô. Output: JSON chứa các trường chuẩn hóa. Điểm kiểm soát: Code kiểm tra đủ trường bắt buộc. Đường lui: Nếu thiếu, lập tức trả trạng thái 'Hồ sơ thiếu thông tin' và gửi thông báo yêu cầu bổ sung.\n"
            "- Bước 2: [Đối chiếu tiêu chuẩn - Evidence Evaluation]\n"
            "  + Input: JSON hồ sơ chuẩn + Bộ tiêu chí đánh giá. Output: Bảng đối soát từng tiêu chí (Đạt/Không đạt) kèm trích dẫn nguyên văn bằng chứng. Điểm kiểm soát: Kiểm tra mọi tiêu chí đều có bằng chứng trích dẫn.\n"
            "- Bước 3: [Tổng hợp quyết định & Tạo giải trình - Decision & Explanation]\n"
            "  + Input: Bảng đối soát từ Bước 2. Output: Quyết định chung cuộc và thư giải thích minh bạch.\n\n"
            "3. Đánh đổi về độ trễ: Chấp nhận độ trễ tăng từ ~2 giây lên ~5-6 giây (do chạy 3 lượt nối tiếp) để đổi lại tính minh bạch tuyệt đối, "
            "khả năng kiểm toán 100% và giảm 90% chi phí tính toán khi hồ sơ thiếu trường bị ngắt sớm ngay từ Bước 1."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tái cấu trúc từ Monolithic Prompt sang Micro-Prompts. "
            "Bằng cách đưa khâu kiểm tra trường bắt buộc lên bước đầu (Early Exit / Fail-Fast), hệ thống tiết kiệm tài nguyên "
            "và đảm bảo mỗi quyết định Đạt/Không đạt đều có bằng chứng cụ thể neo đậu trong dữ liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phản biện sâu sắc thiết kế monolithic (1.0 điểm): Chỉ ra lỗi quá tải nhận thức, thiếu truy vết bằng chứng và lỗi all-or-nothing khi fail.\n"
            "- Thiết kế chuỗi 3 bước kèm điểm kiểm soát & đường lui (1.0 điểm): Trình bày rõ bước trích xuất (early exit nếu thiếu), đối chiếu bằng chứng và tổng hợp quyết định.\n"
            "- Phân tích đánh đổi độ trễ (1.0 điểm): Nêu rõ việc chấp nhận tăng latency nối tiếp để đổi lại tính giải trình, minh bạch và khả năng ngắt sớm."
        ),
        "reference_source": "Anthropic - Building Effective Agents: Prompt Chaining Workflow (https://www.anthropic.com/research/building-effective-agents); Martin Fowler - Monolith to Microservices Pattern (https://martinfowler.com/articles/monolith-to-microservices.html)"
    }

    # 32. d02-q047 (3 pts) [kc-routing-pattern-design]
    data["d02-q047"] = {
        "sample_answer": (
            "1. Thiết kế các nhánh xử lý, ngưỡng và phương án dự phòng:\n"
            "- Bộ định tuyến (Intent & Risk Router) sử dụng phân tích đa tín hiệu: Phân loại ý định kết hợp kiểm tra từ khóa rủi ro khẩn cấp và trạng thái đơn hàng.\n"
            "+ Nhánh 1 (Khẩn cấp - Rủi ro cao): 'Báo mất thẻ thanh toán'\n"
            "  * Ngưỡng kích hoạt: Bất kỳ khi nào phát hiện từ khóa rủi ro liên quan đến mất thẻ/gian lận hoặc cờ rủi ro `risk_flag == HIGH` (không phụ thuộc vào độ tin cậy của intent).\n"
            "  * Xử lý: Lập tức gọi API khóa thẻ tạm thời tất định và chuyển ngay cuộc gọi/chat cho chuyên viên an ninh tài chính 24/7 (Human Escalate). Không bao giờ để LLM trả lời tự do.\n"
            "+ Nhánh 2 (Tác vụ thay đổi trạng thái có điều kiện): 'Thay đổi địa chỉ trước khi giao'\n"
            "  * Ngưỡng kích hoạt: Intent confidence >= 0,85 VÀ `order_status == 'PENDING_DISPATCH'` (đơn hàng chưa giao cho shipper).\n"
            "  * Xử lý: Yêu cầu xác thực OTP của khách hàng -> Cho phép sửa địa chỉ trong DB -> Gửi xác nhận. Nếu đơn đã ở trạng thái 'IN_TRANSIT', tự động từ chối và hướng dẫn liên hệ tổng đài.\n"
            "+ Nhánh 3 (Tác vụ đọc thông tin an toàn): 'Tra trạng thái đơn hàng'\n"
            "  * Ngưỡng kích hoạt: Intent confidence >= 0,80.\n"
            "  * Xử lý: Gọi API tra cứu trạng thái và dùng template phản hồi nhanh cho khách.\n"
            "- Phương án dự phòng (Fallback): Nếu độ tin cậy ý định < 0,80 hoặc tín hiệu mơ hồ, bot hiển thị menu chọn nhanh 3 nút bấm tương ứng trên giao diện.\n\n"
            "2. Hậu quả khi chuyển nhầm nhánh:\n"
            "- Chuyển nhầm từ 'Báo mất thẻ' sang 'Tra đơn': Thẻ của khách hàng không được khóa kịp thời, dẫn đến rủi ro phát sinh giao dịch gian lận tài chính hàng chục triệu đồng và trách nhiệm pháp lý nghiêm trọng.\n"
            "- Chuyển nhầm từ 'Đổi địa chỉ' sang nhánh khác: Hàng bị giao sai địa chỉ cũ, phát sinh chi phí hoàn hàng và làm mất lòng tin của khách hàng."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mẫu hình Routing Pattern trong kiến trúc Agent tuân thủ nguyên tắc 'Ưu tiên Rủi ro trước Chi phí' "
            "(Safety-First Routing). Các sự kiện an ninh và thay đổi trạng thái tài sản phải được phân luồng xử lý với các chốt kiểm tra nghiệp vụ cứng, "
            "tuyệt đối không áp dụng cùng một cơ chế đối xử cho các tác vụ có mức độ thiệt hại chênh lệch nhau."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Thiết kế đủ 3 nhánh xử lý kèm ngưỡng điều kiện (1.5 điểm): Phân nhánh báo mất thẻ (ưu tiên rủi ro cao/khóa thẻ ngay), đổi địa chỉ (kèm điều kiện trạng thái đơn/OTP) và tra đơn hàng.\n"
            "- Phương án dự phòng và phân tích hậu quả chuyển nhầm (1.5 điểm): Nêu fallback menu nút bấm và phân tích sâu sắc hậu quả tài chính khi chuyển nhầm nhánh mất thẻ."
        ),
        "reference_source": "Anthropic - Building Effective Agents: Routing Workflow (https://www.anthropic.com/research/building-effective-agents); Google SRE - Risk-Based Traffic Routing (https://sre.google/sre-book/)"
    }

    # 33. d02-q048 (3 pts) [kc-routing-pattern-design]
    data["d02-q048"] = {
        "sample_answer": (
            "1. Thiết kế các nhánh xử lý theo mức độ rủi ro và độ tin cậy:\n"
            "- Nhánh 1 (FAQ - Rủi ro thấp): Ngưỡng tin cậy >= 0,80 -> Tự động truy xuất kho tri thức RAG và trả lời tức thì cho khách hàng.\n"
            "- Nhánh 2 (Đặt lại mật khẩu - Rủi ro bảo mật trung bình): Ngưỡng tin cậy >= 0,85 -> Tuyệt đối không cho LLM tự cấp mật khẩu; hệ thống chỉ tự động gửi đường link đặt lại mật khẩu bảo mật (secure reset token) về email/SĐT đã đăng ký của khách hàng.\n"
            "- Nhánh 3 (Khiếu nại tài chính - Rủi ro cao): Bất kể điểm tin cậy -> Tự động tạo ticket phân loại ưu tiên cao, thu thập mã giao dịch và chuyển thẳng cho nhân viên hỗ trợ chuyên trách xử lý.\n"
            "- Nhánh 4 (Lớp Không chắc chắn - Uncertainty / Disambiguation Fallback): Khi độ tin cậy của router rơi vào vùng mấp mé hoặc thấp (< 0,80), hệ thống KHÔNG ĐOÁN MÒ mà kích hoạt phản hồi làm rõ với 3 nút bấm lựa chọn trực tiếp: '[1] Hỏi đáp thông tin', '[2] Quên mật khẩu', '[3] Khiếu nại giao dịch'.\n\n"
            "2. Rủi ro khi chuyển nhầm nhánh:\n"
            "- Chuyển nhầm 'Khiếu nại tài chính' sang 'FAQ': Bot trả lời chung chung giáo điều trong khi khách hàng đang bức xúc về việc bị trừ tiền oan, đẩy sự bức xúc lên cao trào và dẫn đến nguy cơ khiếu kiện truyền thông.\n"
            "- Chuyển nhầm 'Đặt lại mật khẩu' sang 'FAQ': Làm lộ hướng dẫn bảo mật không đúng bối cảnh hoặc làm gián đoạn quyền truy cập tài khoản của người dùng.\n\n"
            "3. Phương án dự phòng: Nút bấm 'Gặp nhân viên hỗ trợ' luôn hiển thị cố định ở mọi nhánh để khách hàng có thể thoát khỏi bot bất kỳ lúc nào (Escape Hatch)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: 'Uncertainty-Aware Routing'. Một bộ định tuyến thông minh không phải là bộ định tuyến luôn cố gắng "
            "ra quyết định phân loại, mà là bộ định tuyến biết khi nào mình 'không chắc chắn' để dừng lại, chủ động làm rõ ý định hoặc kích hoạt lối thoát khẩn cấp."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Thiết kế các nhánh phân luồng và lớp không chắc chắn (1.5 điểm): Phân luồng đúng FAQ, Reset mật khẩu (link bảo mật), Khiếu nại (chuyển người) và lớp đệm Disambiguation khi confidence thấp.\n"
            "- Nêu rõ rủi ro chuyển nhầm và phương án dự phòng (1.5 điểm): Phân tích hậu quả khách hàng giận dữ khi khiếu nại bị chuyển nhầm sang FAQ và cung cấp nút thoát (Escape Hatch) gặp nhân viên."
        ),
        "reference_source": "Nielsen Norman Group - Error Prevention in AI Interfaces (https://www.nngroup.com/articles/error-prevention-ai/); Anthropic - Routing Pattern Guidelines (https://www.anthropic.com/research/building-effective-agents)"
    }

    # 34. d02-q051 (3 pts) [kc-orchestrator-workers-pattern-design]
    data["d02-q051"] = {
        "sample_answer": (
            "Thiết kế mô hình Orchestrator–Workers để lập hồ sơ cạnh tranh thị trường mới:\n\n"
            "1. Cách sinh và giới hạn nhiệm vụ con (Subtask Generation & Bounds):\n"
            "- Orchestrator nhận chủ đề thị trường mới, thực hiện lượt tìm kiếm tổng quan đầu tiên để xác định danh sách các đối thủ tiềm năng sơ bộ.\n"
            "- Giới hạn số lượng worker (Concurrency Cap): Thiết lập ngưỡng cứng tối đa không quá 8 worker song song (đại diện cho top 8 đối thủ đáng chú ý nhất). "
            "Nếu phát hiện thêm đối thủ, Orchestrator đưa vào hàng đợi ưu tiên thay vì sinh worker không giới hạn.\n\n"
            "2. Hợp đồng đầu vào / đầu ra của Worker (Worker Interface Contract):\n"
            "- Input Contract: JSON `{competitor_name: str, domain_url: str, research_aspects: ['pricing', 'core_features', 'target_customers']}`.\n"
            "- Output Contract: JSON nghiêm ngặt tuân thủ schema:\n"
            "  `{competitor_name: str, founded_year: int, pricing_model: str, key_features: list[str], strengths: list[str], weaknesses: list[str], sources: list[str]}`.\n\n"
            "3. Cơ chế loại trùng và tổng hợp kết quả (Deduplication & Synthesis):\n"
            "- Orchestrator chuẩn hóa tên đối thủ và domain để gộp các kết quả trùng lặp.\n"
            "- Sử dụng ma trận so sánh (Comparison Matrix) để tổng hợp thông tin; nếu hai worker phát hiện thông tin mâu thuẫn (ví dụ giá bán khác nhau), "
            "Orchestrator bảo toàn cả hai nguồn và ghi rõ sự sai lệch kèm mốc thời gian để người đọc đánh giá.\n\n"
            "4. Ngân sách, điều kiện dừng và xử lý lỗi:\n"
            "- Ngân sách cứng (Budget): Tối đa 50.000 token và thời gian timeout tối đa 90 giây cho toàn bộ phiên phân tích.\n"
            "- Điều kiện dừng: Hoàn tất thu thập đủ thông tin của top đối thủ HOẶC chạm ngưỡng ngân sách token/thời gian.\n"
            "- Xử lý lỗi: Nếu 1 worker bị lỗi timeout hoặc không tìm thấy nguồn, Orchestrator ghi nhận trạng thái 'Thiếu dữ liệu' cho đối thủ đó và tiếp tục tổng hợp các worker còn lại (Graceful Partial Degradation)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mẫu hình Orchestrator-Workers phân tán là giải pháp cho các bài toán phân tích mở không xác định trước số lượng. "
            "Thành công của mô hình nằm ở Hợp đồng giao tiếp có cấu trúc (Strict JSON Contracts), Cơ chế điều tiết lưu lượng (Throttling) "
            "và Dung sai lỗi từng phần (Partial Failure Tolerance)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Sinh và giới hạn worker chuẩn mực (1.0 điểm): Nêu rõ việc Orchestrator tìm kiếm sơ bộ và đặt trần tối đa (ví dụ 8 worker) có hàng đợi ưu tiên.\n"
            "- Hợp đồng đầu vào/đầu ra JSON rõ ràng (1.0 điểm): Định nghĩa schema cụ thể cho worker gồm tên đối thủ, tính năng, giá và mảng trích dẫn nguồn.\n"
            "- Loại trùng, tổng hợp mâu thuẫn, ngân sách và xử lý lỗi (1.0 điểm): Trình bày đủ cách xử lý thông tin mâu thuẫn, ngân sách token/thời gian và dung sai lỗi từng phần."
        ),
        "reference_source": "Anthropic - Building Effective Agents: Orchestrator-Workers Pattern (https://www.anthropic.com/research/building-effective-agents); OpenAI Swarm Multi-Agent Framework (https://github.com/openai/swarm)"
    }

    # 35. d02-q052 (4 pts) [kc-orchestrator-workers-pattern-design]
    data["d02-q052"] = {
        "sample_answer": (
            "1. Bốn rủi ro nghiêm trọng của thiết kế đề xuất ban đầu:\n"
            "- Rủi ro 1: Bùng nổ chi phí và nghẽn tài nguyên (Cost Explosion & Rate Limiting): Khởi tạo đồng loạt 50 worker làm cạn kiệt ngân sách token và gây lỗi nghẽn hạn mức API (HTTP 429 Rate Limit Exceeded) từ nhà cung cấp LLM.\n"
            "- Rủi ro 2: Ô nhiễm dữ liệu và ảo giác không thể kiểm soát (Garbage Accumulation): Worker tự do tìm nguồn không có bộ lọc kiểm chứng, dễ thu thập thông tin rác, lỗi thời hoặc giả mạo từ Internet.\n"
            "- Rủi ro 3: Bất đồng nhất cấu trúc dữ liệu: Thiếu hợp đồng đầu ra chung khiến mỗi worker trả về một kiểu (JSON, Markdown, gạch đầu dòng), khiến bộ tổng hợp không thể phân tích và so sánh có ý nghĩa.\n"
            "- Rủi ro 4: Báo cáo hỗn độn, nuốt mâu thuẫn: Bộ tổng hợp chỉ 'nối chuỗi văn bản' (concatenation) sẽ tạo ra tài liệu dài dòng, trùng lặp hàng chục lần và triệt tiêu các mâu thuẫn dữ liệu quan trọng, khiến người ra quyết định bị hiểu lầm.\n\n"
            "2. Đề xuất các rào chắn kỹ thuật bảo vệ hệ thống:\n"
            "- Rào chắn số nhánh (Concurrency Throttling): Giới hạn tối đa 5-8 worker chạy song song; chia thành các đợt (batches) có điều tiết lưu lượng.\n"
            "- Rào chắn Hợp đồng đầu ra (Enforced Output Schema): Bắt buộc mọi worker phản hồi theo định dạng JSON Schema chuẩn gồm các trường: thực thể, luận điểm chính, số liệu và trích dẫn URL nguồn gốc có thể kiểm chứng.\n"
            "- Rào chắn Tổng hợp bằng chứng (Evidence Grounding & Conflict Resolution): Bộ tổng hợp chạy thuật toán loại trùng (deduplication) và chủ động trích xuất các điểm mâu thuẫn giữa các nguồn ra một mục riêng 'Bất đồng quan điểm cần lưu ý'.\n"
            "- Rào chắn Điều kiện dừng & Ngân sách (Hard Budget & Termination): Đặt ngân sách tối đa 40.000 token và thời gian chạy tối đa 60 giây; nếu chạm ngưỡng, dừng sinh mới và tổng hợp ngay lập tức các dữ liệu đã thu thập được."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Tác nhân tự trị không có rào chắn là công thức tạo ra thảm họa chi phí và dữ liệu rác. "
            "Một kiến trúc Multi-Agent sản xuất bắt buộc phải áp dụng nguyên tắc quản trị phân tán: Định mức tài nguyên (Resource Quotas), "
            "Ranh giới cấu trúc dữ liệu (Schema Boundaries) và Giải quyết xung đột thông tin (Conflict Transparency)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Chỉ ra đủ 4 rủi ro thực tế (2.0 điểm): Nhận diện đúng bùng nổ chi phí/rate limit, rác nguồn, format bất đồng nhất và nối chuỗi nuốt mâu thuẫn.\n"
            "- Đề xuất 4 rào chắn bảo vệ tương ứng (2.0 điểm): Nêu rõ giới hạn worker song song, hợp đồng JSON bắt buộc, bộ tổng hợp loại trùng/bảo toàn mâu thuẫn và giới hạn ngân sách dừng cứng."
        ),
        "reference_source": "Anthropic - Building Effective Agents: Evaluating Agent Architectures (https://www.anthropic.com/research/building-effective-agents); OWASP Top 10 for LLMs - LLM04: Model Denial of Service (https://owasp.org/www-project-top-10-for-large-language-model-applications/)"
    }

    # 36. d02-q054 (3 pts) [kc-evaluator-optimizer-pattern-design]
    data["d02-q054"] = {
        "sample_answer": (
            "Thiết kế vòng lặp Evaluator–Optimizer cho soạn thảo thư điện tử pháp lý:\n\n"
            "1. Bộ tiêu chí đánh giá có thể quan sát được (Evaluator Rubric Criteria):\n"
            "- Tiêu chí 1 (Tính hợp lệ của trích dẫn - Citation Validity): 100% điều khoản trích dẫn phải tồn tại chính xác trong văn bản luật/chính sách được cung cấp (kiểm tra regex số hiệu điều khoản và đối soát văn bản).\n"
            "- Tiêu chí 2 (Không hứa hẹn vượt chính sách - Policy Boundary Compliance): Email không được chứa các từ ngữ cam kết tuyệt đối, bảo đảm bồi thường ngoài phạm vi hoặc từ bỏ quyền miễn trừ trách nhiệm của công ty.\n"
            "- Tiêu chí 3 (Ngôn ngữ rõ ràng, chuẩn mực - Clarity & Tone): Điểm độ đọc hiểu (Flesch-Kincaid / Readability) đạt chuẩn, cấu trúc đoạn mạch lạc, không dùng từ ngữ tối nghĩa.\n\n"
            "2. Cơ chế phản hồi có cấu trúc cho Optimizer (Structured Feedback Loop):\n"
            "Nếu Evaluator chấm 'Không đạt' ở bất kỳ tiêu chí nào, nó KHÔNG chỉ nói chung chung mà sinh ra phản hồi có cấu trúc JSON:\n"
            "```json\n"
            "{\n"
            "  \"passed\": false,\n"
            "  \"violations\": [\n"
            "    {\"criterion\": \"Policy Boundary\", \"problematic_phrase\": \"Công ty sẽ đền bù toàn bộ chi phí\", \"instruction\": \"Sửa thành: Công ty sẽ hỗ trợ xem xét theo quy trình khiếu nại tại Điều 4\"}\n"
            "  ]\n"
            "}\n"
            "```\n"
            "Optimizer nhận JSON này và thực hiện chỉnh sửa đúng các câu vi phạm.\n\n"
            "3. Điều kiện dừng an toàn (Termination Conditions):\n"
            "- Dừng thành công: Khi bài viết vượt qua 100% các tiêu chí kiểm tra (Passed == True).\n"
            "- Dừng thất bại (Circuit Breaker): Tối đa 3 vòng lặp (Max iterations = 3). Nếu sau 3 lần sửa vẫn không đạt chuẩn pháp lý, dừng vòng lặp tự động và chuyển email nháp kèm lịch sử phản hồi vi phạm cho Luật sư nội bộ xử lý thủ công."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Mẫu hình Evaluator-Optimizer áp dụng cơ chế tự sửa lỗi có định hướng (Targeted Self-Correction). "
            "Evaluator đóng vai trò là một 'bộ lọc phê bình độc lập' đưa ra phản hồi mang tính hành động (Actionable Feedback). "
            "Bộ ngắt mạch (Circuit Breaker sau 3 lần) bảo vệ hệ thống khỏi vòng lặp vô tận gây lãng phí chi phí token."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Tiêu chí đánh giá khách quan, đo lường được (1.0 điểm): Định nghĩa rõ tiêu chí trích dẫn hợp lệ, tuân thủ chính sách và độ rõ ràng của ngôn ngữ.\n"
            "- Phản hồi có cấu trúc mang tính hành động (1.0 điểm): Thiết kế phản hồi JSON chỉ rõ câu vi phạm và hướng dẫn sửa cụ thể cho optimizer.\n"
            "- Điều kiện dừng và cơ chế ngắt mạch (1.0 điểm): Đặt điều kiện dừng khi pass 100% hoặc chạm ngưỡng tối đa 3 vòng lặp để escalate cho luật sư."
        ),
        "reference_source": "Anthropic - Building Effective Agents: Evaluator-Optimizer Workflow (https://www.anthropic.com/research/building-effective-agents); Madaan, A., et al. (2023). Self-Refine. NeurIPS 2023 (https://arxiv.org/abs/2303.17651)"
    }

    # 37. d02-q055 (3 pts) [kc-automation-augmentation-role-selection]
    data["d02-q055"] = {
        "sample_answer": (
            "Phân công vai trò Tự động hóa (Automate) và Hỗ trợ con người (Augment) trong quy trình xử lý khiếu nại y tế:\n\n"
            "1. Bước 1 (Trích mã hồ sơ bệnh án) -> TỰ ĐỘNG HÓA (AUTOMATE):\n"
            "- Bản chất: Tác vụ trích xuất thực thể tất định (Regex / OCR NER), hoàn toàn có thể đảo ngược và không gây tác động bên ngoài.\n"
            "- Trách nhiệm: Hệ thống phần mềm chịu trách nhiệm tự động trích xuất.\n"
            "- Chỉ số đo lường: Tỷ lệ trích xuất mã chính xác (Extraction Accuracy / Precision & Recall >= 99%).\n\n"
            "2. Bước 2 (Gom tài liệu liên quan) -> TỰ ĐỘNG HÓA (AUTOMATE):\n"
            "- Bản chất: Truy vấn và kết hợp dữ liệu có sẵn trong kho lưu trữ y tế (Database indexing & Retrieval), không thay đổi trạng thái hồ sơ.\n"
            "- Trách nhiệm: Hệ thống RAG/Search chịu trách nhiệm tổng hợp đầy đủ tài liệu.\n"
            "- Chỉ số đo lường: Tỷ lệ thu hồi tài liệu liên quan (Document Retrieval Recall >= 98%).\n\n"
            "3. Bước 3 (Đề xuất mức độ ưu tiên) -> HỖ TRỢ CON NGƯỜI (AUGMENT):\n"
            "- Bản chất: Đòi hỏi phán đoán lâm sàng và phân loại tính cấp bách dựa trên tình trạng sức khỏe bệnh nhân; sai lệch có thể ảnh hưởng tính mạng.\n"
            "- Trách nhiệm: AI đề xuất mức ưu tiên kèm giải thích; Bác sĩ/Điều dưỡng trưởng rà soát và xác nhận mức ưu tiên chính thức.\n"
            "- Chỉ số đo lường: Tỷ lệ bác sĩ chấp thuận gợi ý của AI (Physician Recommendation Acceptance Rate).\n\n"
            "4. Bước 4 (Gửi quyết định cuối cho bệnh nhân) -> HỖ TRỢ CON NGƯỜI / THỰC THI BỞI CON NGƯỜI (AUGMENT / HUMAN-IN-THE-LOOP):\n"
            "- Bản chất: Hành động tạo tác động ngoại vi vĩnh viễn (Irreversible external action), mang tính pháp lý y tế và ảnh hưởng tâm lý người bệnh.\n"
            "- Trách nhiệm: AI soạn sẵn bản thảo quyết định và tóm tắt chuyên môn; Lãnh đạo hội đồng chuyên môn ký duyệt và trực tiếp gửi cho bệnh nhân.\n"
            "- Chỉ số đo lường: Tỷ lệ khiếu nại tái diễn và mức độ hài lòng của bệnh nhân (Patient Satisfaction Score - CSAT)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc phân định ranh giới tự động hóa theo mức độ tác động và tính có thể đảo ngược: "
            "Tác vụ thu thập thông tin nội bộ (Reversible Internal Tasks) -> Tự động hóa tối đa; Tác vụ phán đoán lâm sàng và hành động đối ngoại không thể đảo ngược "
            "(Irreversible High-Stakes Actions) -> Bắt buộc giữ con người làm trung tâm quyết định (Human Agency)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phân bổ chính xác Automate và Augment cho 4 bước (1.5 điểm): Gán đúng Automate cho bước 1 & 2; Gán Augment cho bước 3 & 4.\n"
            "- Nêu rõ trách nhiệm và chỉ số đo lường riêng biệt (1.5 điểm): Nêu đủ trách nhiệm phân cấp và chỉ số đo lường tương ứng cho từng bước (Precision, Recall, Acceptance rate, CSAT)."
        ),
        "reference_source": "Parasuraman, R., et al. (2000). A Model for Types and Levels of Human Interaction with Automation (https://ieeexplore.ieee.org/document/844357); WHO Guidance on AI in Health (https://www.who.int/publications/i/item/9789240029200)"
    }

    # 38. d02-q056 (3 pts) [kc-automation-augmentation-role-selection]
    data["d02-q056"] = {
        "sample_answer": (
            "1. Phản biện đề xuất tự động hóa tín dụng ban đầu:\n"
            "Đề xuất trên cực kỳ nguy hiểm và thiếu trách nhiệm: (1) Ngưỡng 100 triệu là con số tài chính lớn, để mô hình tự động duyệt mà không có kiểm toán sẽ dẫn đến nguy cơ gian lận tín dụng có tổ chức và nợ xấu tăng vọt; "
            "(2) Tự động từ chối ngay khi thiếu giấy tờ mà không hướng dẫn bổ sung sẽ gây ức chế và đánh mất khách hàng tiềm năng; "
            "(3) Đẩy con người về thế bị động (chỉ xem khi khách khiếu nại) biến nhân viên thành người đi dập lửa hậu quả thay vì người kiểm soát rủi ro.\n\n"
            "2. Phân công lại theo 4 bước chuẩn mực:\n"
            "- Bước 1 (Trích dữ liệu) -> TỰ ĐỘNG HÓA (AUTOMATE): AI đọc hồ sơ, trích xuất căn cước, sao kê thu nhập thành JSON chuẩn. Trách nhiệm: Hệ thống phần mềm.\n"
            "- Bước 2 (Phát hiện thiếu giấy tờ) -> TỰ ĐỘNG HÓA KÈM HỖ TRỢ (AUTOMATE WITH USER LOOP): Hệ thống tự động kiểm tra đối chiếu danh mục giấy tờ. Nếu thiếu, tự động gửi thông báo thân thiện hướng dẫn khách nộp bổ sung trực tiếp, KHÔNG tự ý từ chối hồ sơ.\n"
            "- Bước 3 (Đề xuất hạn mức) -> HỖ TRỢ CON NGƯỜI (AUGMENT): AI tính toán điểm tín dụng nội bộ và đề xuất hạn mức kèm bảng giải thích rủi ro. Trách nhiệm: Chuyên viên tín dụng thẩm định đề xuất.\n"
            "- Bước 4 (Quyết định giải ngân) -> CON NGƯỜI GIỮ QUYỀN DUYỆT (HUMAN APPROVAL GATE): Bắt buộc phải có chữ ký số của Chuyên viên hoặc Trưởng phòng tín dụng trước khi lệnh giải ngân được gửi sang hệ thống Core Banking.\n\n"
            "3. Điểm chặn bắt buộc (Hard Gate): Cổng giải ngân tại Core Banking yêu cầu mã xác thực phê duyệt của con người, không chấp nhận lệnh gọi tự động từ dịch vụ AI.\n\n"
            "4. Ba chỉ số bắt buộc phải theo dõi:\n"
            "- Tỷ lệ nợ xấu (Non-Performing Loan Rate - NPL) của các hồ sơ được AI hỗ trợ.\n"
            "- Tỷ lệ từ chối sai lệch (False Rejection Rate) do lỗi trích xuất giấy tờ.\n"
            "- Tỷ lệ chuyên viên tín dụng ghi đè / bác bỏ gợi ý hạn mức của AI (Override Rate)."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Trong các hệ thống tài chính tín dụng (Credit Underwriting), rủi ro đạo đức và rủi ro quy định (Regulatory Compliance) "
            "đòi hỏi sự phân định rạch ròi giữa 'Gợi ý tính toán' (Scoring Suggestion) và 'Quyền cam kết tài chính' (Financial Commitment). "
            "Một hạn mức 100 triệu giải ngân sai sẽ không thể thu hồi."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Phản biện sâu sắc đề xuất cũ (1.0 điểm): Chỉ ra rủi ro nợ xấu khi tự duyệt 100 triệu, việc từ chối oan khi thiếu giấy tờ và vai trò bị động của nhân viên.\n"
            "- Viết lại phân công 4 bước chuẩn xác (1.0 điểm): Trích dữ liệu (auto), phát hiện thiếu (auto hỗ trợ bổ sung), đề xuất hạn mức (augment) và giải ngân (human gate).\n"
            "- Nêu điểm chặn bắt buộc và 3 chỉ số theo dõi (1.0 điểm): Nêu rõ chốt chặn chữ ký con người tại Core Banking và 3 chỉ số (nợ xấu, từ chối oan, tỷ lệ override)."
        ),
        "reference_source": "Basel Committee on Banking Supervision - Credit Risk Management (https://www.bis.org/publ/bcbs75.htm); Federal Reserve SR 11-7: Model Risk Management (https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)"
    }

    # 39. d02-q059 (3 pts) [kc-clarification-control-placement]
    data["d02-q059"] = {
        "sample_answer": (
            "Câu hỏi làm rõ ngắn nhất và chuẩn xác nhất để chọn nhánh tìm vé:\n\n"
            "\"Bạn muốn khởi hành vào đầu giờ chiều (13h – 16h) hay cuối giờ chiều (16h – 19h)?\"\n\n"
            "Giải thích thiết kế giao diện hội thoại (Conversational UX Rationale):\n"
            "- Hệ thống đã biết đầy đủ các thông tin: Điểm đi, Điểm đến, Ngày khởi hành (chiều mai) và Ngân sách tối đa (2 triệu đồng). "
            "Do đó, tuyệt đối KHÔNG hỏi lại những thông tin người dùng đã cung cấp.\n"
            "- Trường dữ liệu duy nhất còn thiếu để định tuyến chính xác giữa hai nhánh tìm kiếm là Khung giờ khởi hành cụ thể trong buổi chiều. "
            "Câu hỏi được thiết kế ngắn gọn, trực diện, đưa ra sẵn hai lựa chọn đóng (closed choices: 13h-16h vs 16h-19h) giúp người dùng có thể nhấp chọn ngay "
            "với một thao tác chạm mà không cần phải gõ lại văn bản dài dòng."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Minimal Cognitive Load & Non-redundancy' trong thiết kế hội thoại AI: "
            "Chỉ làm rõ trường dữ liệu còn thiếu cuối cùng ngăn cản việc kích hoạt nhánh nghiệp vụ. Đưa ra các tùy chọn phân nhánh cụ thể "
            "thay vì đặt câu hỏi mở mơ hồ giúp tối ưu tỷ lệ chuyển đổi tác vụ."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Câu hỏi làm rõ chuẩn xác, ngắn gọn (2.0 điểm): Đặt đúng câu hỏi chọn giữa khung giờ 13–16h hay 16–19h mà không hỏi lại các thông tin đã biết.\n"
            "- Giải thích nguyên lý thiết kế hội thoại (1.0 điểm): Giải thích việc chỉ hỏi trường còn trống và đưa ra lựa chọn đóng để giảm tải nhận thức cho người dùng."
        ),
        "reference_source": "Google Conversational AI Design Guidelines - Asking Clarifying Questions (https://developers.google.com/assistant/conversation-design); Nielsen Norman Group - Chatbot UX (https://www.nngroup.com/articles/chatbots/)"
    }

    # 40. d02-q060 (3 pts) [kc-clarification-control-placement]
    data["d02-q060"] = {
        "sample_answer": (
            "1. Câu hỏi làm rõ chuẩn xác dành cho người dùng:\n"
            "\"Bạn muốn gửi [Tên tệp báo cáo] tới nhóm nào (ví dụ: Nhóm Dự án, Nhóm Kinh doanh hay Ban Giám đốc), "
            "và bạn muốn gửi dưới dạng Bản nháp để góp ý hay Bản chính thức phê duyệt?\"\n\n"
            "2. Điều kiện bắt buộc để tiếp tục thực thi hành động gửi (Gating Conditions):\n"
            "- Điều kiện 1 (Đầy đủ người nhận): Trường `recipient_group_id` được xác định chính xác và tương ứng với một nhóm có thật trong danh bạ phân quyền của tổ chức.\n"
            "- Điều kiện 2 (Xác nhận trạng thái tài liệu): Người dùng xác nhận rõ ràng giá trị cờ `is_final_version` (True nếu là bản chính thức, False nếu là bản nháp).\n"
            "- Điều kiện 3 (Xác nhận trước khi gửi đối ngoại - Pre-send Confirmation): Nếu là bản chính thức hoặc gửi cho nhóm đối tác/lãnh đạo, "
            "hệ thống phải hiển thị một hộp thoại tóm tắt (Preview Modal) kèm nút 'Xác nhận gửi' để người dùng kiểm tra lại lần cuối trước khi file được phát đi."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Defensive Dispatching' trong tương tác người-máy. "
            "Gửi tài liệu là hành động đối ngoại không thể thu hồi hoàn toàn. Việc thiếu đối tượng nhận và trạng thái tài liệu là rủi ro rò rỉ thông tin nghiêm trọng; "
            "hệ thống bắt buộc phải dừng lại ở cổng làm rõ trước khi thực thi lệnh phát tán tài liệu."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Câu hỏi làm rõ đủ 2 thông tin thiếu (1.5 điểm): Hỏi rõ nhóm nhận cụ thể và trạng thái gửi bản nháp hay bản chính thức.\n"
            "- Điều kiện tiên quyết để tiếp tục (1.5 điểm): Định nghĩa rõ các điều kiện về xác thực nhóm nhận hợp lệ, xác định cờ phiên bản và cổng xác nhận preview của người dùng."
        ),
        "reference_source": "Microsoft HAX Toolkit - Guideline 10: Scope of Action (https://www.microsoft.com/en-us/haxtoolkit/); Nielsen Norman Group - Confirmation Dialogs (https://www.nngroup.com/articles/confirmation-dialog/)"
    }

    # 41. d02-q062 (3 pts) [kc-evidence-transparency-control]
    data["d02-q062"] = {
        "sample_answer": (
            "Viết lại câu trả lời với mức độ minh bạch bằng chứng chuẩn xác:\n\n"
            "\"Theo dữ liệu bảng giá thu thập từ 8 tháng trước, Nhà cung cấp A hiện có mức giá dịch vụ cơ bản thấp nhất trong các đơn vị được khảo sát. "
            "Tuy nhiên, kết luận này có hai giới hạn quan trọng cần lưu ý:\n"
            "1. Dữ liệu đã cũ (8 tháng trước) và giá thực tế của các nhà cung cấp có thể đã thay đổi.\n"
            "2. So sánh hiện tại chưa bao gồm chi phí hỗ trợ kỹ thuật của Nhà cung cấp B do thiếu thông tin trong hồ sơ.\n"
            "Khuyến nghị: Bạn nên yêu cầu bảng báo giá cập nhật mới nhất kèm chi phí hỗ trợ trọn gói từ cả hai nhà cung cấp trước khi đưa ra quyết định lựa chọn.\"\n\n"
            "Giải thích: Câu trả lời mới tuân thủ nguyên tắc minh bạch bằng chứng: Tách biệt rõ ràng điều dữ liệu chứng minh được (giá cơ bản cũ) "
            "khỏi các điểm mù và giả định chưa kiểm chứng (thời gian trôi qua, thiếu phí hỗ trợ của B), giúp người dùng không bị đánh lừa bởi một kết luận tuyệt đối sai lệch."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Nguyên tắc 'Epistemic Humility & Evidence Transparency' trong AI: "
            "Hệ thống không được phép đưa ra các kết luận tuyệt đối mang tính phán xét ('A rẻ nhất') khi dữ liệu nền tảng bị khiếm khuyết. "
            "Công khai ranh giới tri thức giúp bảo vệ người dùng khỏi các quyết định tài chính sai lầm."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 3 điểm):\n"
            "- Viết lại câu trả lời minh bạch (2.0 điểm): Trình bày rõ giá cơ bản của A rẻ nhất theo dữ liệu cũ, chỉ rõ giới hạn 8 tháng và việc thiếu phí hỗ trợ của B.\n"
            "- Khuyến nghị hành động kiểm chứng (1.0 điểm): Đưa ra khuyến nghị cập nhật báo giá mới trước khi quyết định, giải thích nguyên lý minh bạch dữ liệu."
        ),
        "reference_source": "Google PAIR Guidebook - Set Expectations on Limitations (https://pair.withgoogle.com/guidebook/); ISO/IEC 42001 - Artificial Intelligence Management System."
    }

    # 42. d02-q064 (4 pts) [kc-manual-approval-control]
    data["d02-q064"] = {
        "sample_answer": (
            "1. Thiết kế màn hình phê duyệt hàng loạt an toàn (Bulk Approval Interface Design):\n"
            "- Tiêu đề cảnh báo rủi ro cao: 'XÁC NHẬN PHÊ DUYỆT: XÓA 1.200 TÀI KHOẢN KHÔNG HOẠT ĐỘNG'.\n"
            "- Bảng tóm tắt định lượng: Hiển thị tiêu chí lọc ('Tài khoản không đăng nhập > 24 tháng, số dư = 0'), tổng số tài khoản bị ảnh hưởng (1.200).\n"
            "- Bảng dữ liệu xem trước (Preview Table): Hiển thị danh sách 50 tài khoản mẫu đầu tiên (UserID, Email ẩn danh, Ngày đăng nhập cuối) kèm nút 'Tải file CSV danh sách đầy đủ 1.200 tài khoản' để kiểm toán trước khi duyệt.\n"
            "- Cơ chế an toàn kép: Bắt buộc người phê duyệt phải gõ đúng chuỗi chữ 'XOA 1200 TAI KHOAN' vào ô xác nhận trước khi nút hành động được kích hoạt (ngăn chặn bấm nhầm vô thức).\n\n"
            "2. Hành vi chi tiết của hệ thống theo từng lựa chọn:\n"
            "- Khi người dùng CHẤP THUẬN (Approve):\n"
            "  + Hệ thống không xóa vật lý ngay lập tức (Hard Delete) mà chuyển trạng thái sang 'Xóa mềm / Tạm khóa' (Soft Delete) trong vòng 30 ngày để cho phép phục hồi nếu có sai sót.\n"
            "  + Ghi nhật ký kiểm toán bất biến (Audit Log) lưu rõ: AdminID, Timestamp, Tiêu chí xóa và Snapshot danh sách tài khoản.\n"
            "- Khi người dùng TỪ CHỐI (Reject):\n"
            "  + Hủy bỏ hoàn toàn tác vụ xóa trong hàng đợi; mở hộp thoại yêu cầu Admin ghi lý do từ chối để làm dữ liệu tinh chỉnh cho agent.\n"
            "  + Gửi thông báo an toàn xác nhận không có bất kỳ tài khoản nào bị thay đổi trạng thái.\n"
            "- Khi người dùng CHỈNH SỬA (Modify / Exclude):\n"
            "  + Cung cấp tính năng loại trừ (Exclusion list): Cho phép Admin lọc bỏ hoặc bỏ chọn một số tài khoản đặc biệt (ví dụ tài khoản VIP, tài khoản đối tác) ra khỏi danh sách xóa.\n"
            "  + Hệ thống cập nhật lại số lượng (ví dụ từ 1.200 xuống 1.185 tài khoản) và yêu cầu xác nhận lại trên danh sách mới."
        ),
        "explanation": (
            "Phân tích theo nguyên lý thiết kế: Đối với các hành động phá hủy hàng loạt (Destructive Bulk Actions), nguyên tắc Human-Centered Safety "
            "đòi hỏi màn hình phê duyệt phải có: Bằng chứng tác động rõ ràng (Impact Transparency), Cơ chế xác nhận có ma sát chủ ý (Friction-based Confirmation), "
            "Khả năng chỉnh sửa loại trừ linh hoạt, và Cơ chế xóa mềm phục hồi được (Soft-delete Safety Net)."
        ),
        "rubric": (
            "👉 Tiêu chí chấm (Rubric 4 điểm):\n"
            "- Thiết kế màn hình phê duyệt đầy đủ thông tin (1.5 điểm): Trình bày tiêu chí lọc, bảng preview, nút xuất CSV và cơ chế gõ chữ xác nhận chống bấm nhầm.\n"
            "- Hành vi khi Chấp thuận (1.0 điểm): Thực hiện Soft delete an toàn kèm ghi audit log bất biến.\n"
            "- Hành vi khi Từ chối (0.5 điểm): Hủy bỏ lệnh an toàn, ghi nhận lý do từ chối.\n"
            "- Hành vi khi Chỉnh sửa (1.0 điểm): Cho phép lọc bỏ tài khoản ngoại lệ, cập nhật lại số lượng và yêu cầu xác nhận danh sách mới."
        ),
        "reference_source": "Nielsen Norman Group - Confirmation Dialogs and Destructive Actions (https://www.nngroup.com/articles/confirmation-dialog/); Microsoft HAX Toolkit - Support Efficient Correction (https://www.microsoft.com/en-us/haxtoolkit/)"
    }

    return data

