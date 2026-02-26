---
description: [Master Workflow] Quy trình kết hợp UX Design và P&G Insights để viết Spec tối ưu
---

# Master Workflow: P&G Insights x UX Design Team

Quy trình này hướng dẫn cách kết hợp sức mạnh phân tích tâm lý của `pg-insights-team` (chuyên tìm nỗi đau và sự thật ngầm hiểu) với khả năng thiết kế thực thi của `ux-design-team` (chuyên vẽ luồng và viết tài liệu kỹ thuật).
Kết quả cuối cùng sẽ là một bản **Full-stack Product Spec** có tính khả thi cao về công nghệ nhưng chạm đỉnh về mặt cảm xúc người dùng.

## Mục tiêu (Goal)
Tạo ra tài liệu Spec cho một tính năng/sản phẩm mới, đảm bảo 2 yếu tố:
1. Giải quyết đúng "Jobs-To-Be-Done" (UX Team).
2. Tạo được khoảnh khắc "Goosebumps - Nổi da gà" cho khách hàng (P&G Team).

## Quy trình Thực thi (Phối hợp chéo)

Quá trình này bẻ gãy rào cản giữa các team. Sẽ có sự làm việc xen kẽ thay vì team này làm xong mới đến lượt team khác.

### Giai đoạn 1: Tiếp nhận và Khởi tạo (Initiation)
Tham gia: `PM (UX Team)` và `BOSS`
1. **BOSS** chuẩn bị một đề bài (Brief) mô tả cơ bản về tính năng cần làm.
2. **PM** tiếp nhận đề bài, lưu trữ thông tin lên file `WHITEBOARD.md` của quá trình làm việc.
3. **PM** phân tích yêu cầu sơ bộ và ra lệnh cho `UR` bắt đầu công việc.

### Giai đoạn 2: Định vị Nỗi Đau & Tâm Lý (The "Why")
Tham gia: `UR (UX Team)` và `P&G Insights Team (MR -> IA -> SL)`
1. **UR (UX Team)**: Tiến hành thu thập dữ liệu về đối thủ (Competitor Benchmark) và vạch ra các Jobs-To-Be-Done (JTBD) cơ bản.
2. **UR** nhận thấy cần đào sâu tâm lý, bèn "thuê" team P&G:
   - **MR (P&G)**: Lấy JTBD của UR để đi tìm các "Everyday Moments" (Khoảnh khắc đời thường khách hàng gặp phải).
   - **IA (P&G)**: Phân tích các Pain-points (Nỗi đau) trong khoảnh khắc đó.
   - **SL (P&G)**: Đúc kết lại thành 1 câu **Brand Insight (Sự thật ngầm hiểu)** cốt lõi nhất.
3. **P&G Team** đóng gói Insight này và trả ngược kết quả lại cho `UR`.
4. **UR** hợp nhất dữ liệu Benchmark của mình + Brand Insight của P&G để ra một tài liệu **Research Context** hoàn chỉnh và đưa ra định hướng thiết kế.

*(Dừng lại xin phép Boss duyệt tài liệu định hướng trước khi vẽ!)*

### Giai đoạn 3: Thiết Kế Luồng & Điểm Chạm (The "How")
Tham gia: `UX Designer (UX Team)`
1. **UX** tiếp nhận bản hướng dẫn từ `UR`.
2. Dựa trên Brand Insight cốt lõi (sự thấu cảm), UX tiến hành vẽ sơ đồ luồng (User Flow / Wireframe) bằng Mermaid/Text.
3. **UX** đảm bảo mỗi bước trong luồng chạm đúng vào "Feeling" (Cảm xúc) đã định hình.

*(Dừng lại xin phép Boss duyệt bản vẽ UX Flow!)*

### Giai đoạn 4: Đóng Gói Kỹ Thuật & Cảm Xúc (The "What")
Tham gia: `TW (Technical Writer)` và `CR (Quality Reviewer)`
1. **TW**: Dựa vào bản vẽ của UX, bóp tách ra màn hình/chức năng.
2. **TW** kết hợp "Tone of Voice" từ Insight của P&G Team để viết Copywriting (câu chữ, thông báo báo lỗi) trên giao diện.
3. **TW** điền toàn bộ dữ liệu vào `Tài Liệu Mẫu (Full-stack Product Spec)`.
4. **CR**: Đóng vai trò gác cổng. Cầm bản Spec chuẩn bị phát hành và đối chiếu ngược lại với:
   - Yêu cầu ban đầu của BOSS.
   - Brand Insight của SL (P&G Team).
   - JTBD của UR (UX Team).
5. Nếu pass, xuất file Spec cuối cùng.

---
## 💡 Lệnh Mẫu Kích Hoạt (Kích hoạt Siêu Quy Trình)

Boss hãy copy đoạn prompt sau khi muốn kích hoạt sự phối hợp này:

> *"Tôi muốn khởi tạo quy trình VietDoc (Phối hợp UX Team và P&G Team) cho tính năng [TÊN TÍNH NĂNG].
> Yêu cầu công việc như sau: [MÔ TẢ NGẮN GỌN TÍNH NĂNG ĐÓ LÀ GÌ].
> 
> Hãy đóng vai các Agent theo đúng luồng sau: 
> 1. PM nhận việc -> UR phân tích đối thủ & JTBD cơ bản.
> 2. Đổi qua team P&G: MR đào sâu Moments -> IA bắt bệnh -> SL đúc rút Insight.
> 3. Đổi về team UX: UR tổng hợp lại -> UX vẽ luồng Mermaid -> TW phân rã thành file Spec chuẩn -> CR review.
> Nơi nào có Output chính, hãy dừng lại chờ tôi duyệt rồi mới đi tiếp theo luật Continuous Approval."*
