# UX Design Team Workflow

## Giới thiệu
Team thiết kế ưu tiên **Nguyên lý Design Thinking (Tư duy Thiết kế)** và **JTBD (Jobs-to-be-Done - Việc Cần Hoàn Thành)** để tạo ra các luồng (UX flows) mang lại giá trị lõi cao nhất cho sản phẩm. Đồng thời viết tài liệu mô tả hệ thống hoặc Copywriting tương ứng.

## Framework Nền tảng
- **Design Thinking:** Trải qua lần lượt các giai đoạn (Empathize, Define -> Nghiên cứu bởi UR), (Ideate, Prototype -> Thiết kế bởi UX), (Test -> Đánh giá bởi CR).
- **JTBD (Jobs-to-be-Done):** Chuyển dịch tư duy từ việc "Thiết kế tính năng" sang "Thiết kế làm sao để giải quyết 'công việc' hoặc 'nhu cầu thực sự' của người dùng". Đồng thời định vị giải pháp dựa trên thực tiễn các sản phẩm đối thủ (competitor benchmarks).

## Các vai trò (Roles)
1. **PM (Project Manager)**
   - Nhận yêu cầu từ BOSS.
   - Quản lý tiến độ (sprint progress), cập nhật `WHITEBOARD.md`.
   - Điều phối giao tiếp giữa UR, UX, TW, CR.

2. **UR (UX Researcher)**
   - Khởi đầu quy trình. Sử dụng JTBD và Design Thinking.
   - Phân tích insight, khảo sát đối thủ, luồng của các app tượng tự.
   - Hình thành JTBD Profiles và hướng dẫn UX cho Designer.

3. **UX (UX Designer)**
   - Phân tích kết quả của UR.
   - Vẽ luồng trải nghiệm người dùng (UX Flows) bằng text, markdown, hoặc mermaid JS.
   - Thử nghiệm các ý tưởng (Ideate) & Tạo nguyên mẫu cấp phát luồng (Prototype flows).

4. **TW (Technical Writer / Content Writer)**
   - Nhận luồng UX để viết thành tài liệu mô tả chi tiết, Copywriting cho UI.

5. **CR (Code/Quality Reviewer / UX Tester)**
   - Đóng vai trò Test trong Design Thinking. Test lại luồng có giải quyết đúng Job được UR phân tích không?
   - Đảm bảo MECE (Mutually Exclusive, Collectively Exhaustive).

## Quy trình Làm việc theo Design Thinking (Sprint Workflow)
1. **BOSS → PM**: BOSS đưa ý tưởng / yêu cầu thiết kế vào file / chat (qua dấu `>>> `).
2. **PM → UR**: (Giai đoạn Empathize & Define). PM giao nhiệm vụ cho UR nghiên cứu insight khách hàng và phân tích đối thủ cạnh tranh trên thị trường đối với yêu cầu này.
3. **UR**: Áp dụng JTBD. Viết tài liệu nghiên cứu và Benchmark competitor.
4. **UR → PM**: Báo cáo PM.
5. **PM → UX**: (Giai đoạn Ideate & Prototype). PM chuyển tài liệu nghiên cứu của UR cho UX để làm chất liệu thiết kế luồng (Flows).
6. **UX**: UX tạo luồng phù hợp với chân dung người dùng, áp dụng học hỏi từ đối thủ.
7. **UX → PM**: Báo UX flow hoàn tất.
8. **PM → CR**: (Giai đoạn Test). Chuyển cho CR đánh giá bản nháp.
9. **CR ↔ PM ↔ UX ↔ UR**: CR lấy tài liệu của UR đối chiếu với bản vẽ của UX. Nếu UX không giải quyết được JTBD, đánh rớt (Reject). Vòng lặp tối ưu thiết kế liên tục diễn ra.
10. **PM → TW**: Sau khi UX thông qua, PM giao UX Flow và JTBD Context cho TW viết Documents.
11. **TW ↔ PM ↔ CR**: TW làm việc và CR thẩm định bộ document.
12. **PM → Boss**: Kết thúc Sprint, PM gửi toàn bộ hồ sơ (Nghiên cứu thị trường của UR + Luồng của UX + Tài liệu của TW) cho Boss duyệt vòng ngoài.
