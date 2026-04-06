# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

Xin chào BTC, anh chị mentor, theo hệ thống thì em đã nộp bài 2 lần và đây sẽ là lần thứ 3.
Lần thứ nhất, em chỉ mở ra để xem cách thức nộp bài, chưa hề thao tác gì.
Lần thứ hai, em đã nộp file hoàn chỉnh nhưng sang ngày hôm sau, em thấy báo fail và time spent của em khoảng hơn 15 giờ.
Vậy nên, em xin phép nộp lần thứ 3, mong BTC và anh chị mentor xem xét và chấm điểm tình huống này của em

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> - Temperature càng thấp thì model trả lời càng cẩn thận, dập khuôn. Temperature thấp khiến model trả lời chính xác nhất, phổ biến nhất, an toàn nhất, trả lời giống sách giáo khoa, đầy đủ số liệu nhưng khô khan
- Khi temperature lên khoảng 0,5-1,0 , model sáng tạo hơn một chút, thay vì chọn lựa chọn an toàn, phổ biến nhất, thi thoảng nó chọn cách diễn đạt hay hơn, mới lạ hơn -> kết quả là câu nghe trôi chảy, mềm mại, giống nghe kể chuyện hơn là đọc báo
- Khi temperature lên cao (1.5), model trả lời rất phóng khoáng, không bị gò bó, tuy nhiên, đôi khi lại thành lủng củng hoặc nói quá. Nếu tăng lên 2.0 hoặc nữa thì khả năng mô hình sẽ "say" =)))))

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Đối với chatbot hỗ trợ khách hàng, tùy thuộc vào lĩnh vực của sản phẩm, tôi sẽ đặt temperature phù hợp. 
 - Trong trường hợp lĩnh vực của sản phẩm liên quan đến những ngành nhạy cảm, cần độ chính xác cao như tư vấn lụât pháp, các thủ tục pháp lý. Tôi sẽ đặt temperature ở mức thấp, trong khoảng 0.0-0.1 (qua kiểm thử, nếu tăng thêm mỗi lần 0.1 hoặc 0.05 mà model vẫn đảm bảo output, có thể cân nhắc)
 - Nếu chatbot chỉ đơn giản là tư vấn những câu hỏi kiểu "tối nay tôi nên ăn gì", "kể cho tôi một câu chuyện buồn cười" thì temperature hoàn toàn có thể đặt ở mức 1.0-1.2. Ở những case này thường sẽ không có đáp án "đúng" hay "sai" , bot cần đưa ra nhiều lựa chọn đa dạng và mới lạ để tránh nhàm chán

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> Tổng số token/ngày là: 10,000×3×350=10,500,000token(tức 10.500 nghìn token).
Với đơn giá output trong bài: GPT-4o là 0,010 USD/1K token, GPT-4o-mini là 0,0006 USD/1K token.
Chi phí/ngày ước tính: GPT-4o = 10,500×0,010=105 USD; 
GPT-4o-mini = 10,500×0,0006=6,3 USD
Vậy GPT-4o đắt hơn khoảng 105/6,3≈16,7 lần.

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> Chi phí cao hơn của GPT-4o là xứng đáng trong các bài toán cần chất lượng suy luận và độ chính xác cao, ví dụ trợ lý phân tích hợp đồng/pháp lý, tổng hợp báo cáo chiến lược cho lãnh đạo, hoặc các luồng “high-stakes” mà trả lời sai có thể gây rủi ro lớn.
Ngược lại, GPT-4o-mini phù hợp hơn cho các tác vụ khối lượng lớn và yêu cầu phản hồi nhanh như FAQ chăm sóc khách hàng, phân loại ticket, tóm tắt ngắn nội dung lặp lại, hoặc chatbot nội bộ nơi mục tiêu chính là tối ưu chi phí vận hành.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất trong các tình huống hội thoại thời gian thực, đặc biệt khi câu trả lời dài hoặc người dùng đang chờ hướng dẫn từng bước, vì việc hiển thị token dần dần giúp giảm cảm giác chờ đợi, tăng độ tin cậy rằng hệ thống vẫn đang hoạt động và cải thiện trải nghiệm tương tác. Ngược lại, non-streaming phù hợp hơn khi cần kết quả hoàn chỉnh một lần để xử lý tiếp ở backend (ví dụ lưu database, hậu kiểm định dạng JSON, chạy pipeline tự động), hoặc trong các tác vụ ngắn nơi độ trễ vốn đã thấp và việc stream không mang thêm nhiều giá trị UX.


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
