---
Title: Chiến lược hiển thị Widget Gói cước (Kịch bản người dùng)
Status: Draft
Tags: [Widget, Communication, Emi OS, Gói cước]
---

# Chiến lược Hiển thị Widget Gói Cước

Dựa trên cấu trúc phân tập khách hàng và vòng đời sử dụng gói cước, chiến lược nội dung trên Widget cần tuân thủ nguyên tắc: **Cá nhân hóa - Đúng ngữ cảnh - Không Spam (Right context, Right time)**. Widget nên đóng vai trò như một "trợ lý cá nhân" (Emi), giúp người dùng quản lý viễn thông một cách chủ động thay vì chỉ là công cụ bán hàng.

Dưới đây là các kịch bản (User Scenarios) cụ thể cho từng nhóm trạng thái:

## 1. Nhóm Khám phá & Chuyển đổi (Chưa có gói cước / Mới)
Mục tiêu: Kích thích đăng ký gói mới, bảo vệ người dùng khỏi chi phí phát sinh ngoài ý muốn.

*   **Kịch bản 1.1: Trạng thái bình thường (Chưa có gói)**
    *   **Context:** Người dùng thỉnh thoảng dùng app, hiện không có gói cước data nào đang kích hoạt.
    *   **Nội dung Widget:** Hiển thị gói cước phù hợp nhất (dựa trên lịch sử tiêu dùng hoặc Best Seller).
    *   **Copywriting:** "Gợi ý cho bạn: Gói [Tên gói] lướt mạng không giới hạn chỉ [Giá]đ/tháng."
    *   **CTA:** Đăng ký ngay.

*   **Kịch bản 1.2: Đang dùng cước ngoài gói (Rủi ro)**
    *   **Context:** Người dùng không có gói nhưng phát sinh lưu lượng data lẻ (chạm ngưỡng 100MB). Cước phí lúc này rất cao.
    *   **Nội dung Widget:** Trạng thái Cảnh báo (Alert). Đánh vào tâm lý sợ mất tiền oan.
    *   **Copywriting:** "Cảnh báo: Bạn đang dùng data lẻ với chi phí cao. Đăng ký ngay gói [Tên gói] để tiết kiệm đến 80% chi phí!"
    *   **CTA:** Xem gói ưu đãi.

*   **Kịch bản 1.3: User mới kích hoạt SIM (Onboarding)**
    *   **Context:** SIM mới active dưới 7 ngày, ít tương tác trên app.
    *   **Nội dung Widget:** Trạng thái Chào mừng. Nhấn mạnh vào đặc quyền cho người mới.
    *   **Copywriting:** "Chào bạn mới! Tặng riêng bạn ưu đãi độc quyền: Giảm 50% cho tháng đầu tiên đăng ký gói [Tên gói]."
    *   **CTA:** Nhận ưu đãi.

## 2. Nhóm Theo dõi & Upsell (Giữa kỳ: D11 - D20)
Mục tiêu: Đảm bảo trải nghiệm xuyên suốt, bán chéo (upsell) các gói mua thêm trước khi người dùng bị ngắt kết nối.

*   **Kịch bản 2.1: Dùng nhanh hơn nhịp chuẩn**
    *   **Context:** Mới giữa kỳ nhưng đã dùng 60-75% dung lượng, dự kiến sẽ hết data trước khi hết tháng.
    *   **Nội dung Widget:** Nhắc nhở nhẹ nhàng (Hint).
    *   **Copywriting:** "Tốc độ lướt mạng của bạn tháng này khá cao! Tham khảo gói mua thêm [X]GB để không lo bị gián đoạn giữa chừng nhé."
    *   **CTA:** Mua thêm data.

## 3. Nhóm Giữ chân & Gia hạn (Cuối kỳ: D21 - EOM)
Mục tiêu: Đảm bảo tỷ lệ gia hạn (Renewal rate), cứu nét kịp thời khi hết data đột xuất.

*   **Kịch bản 3.1: Sắp hết data, còn nhiều hạn**
    *   **Context:** Đã dùng >80% gói nhưng còn ít nhất 3 ngày nữa mới sang chu kỳ mới.
    *   **Nội dung Widget:** Trạng thái khẩn cấp nhẹ.
    *   **Copywriting:** "Data sắp cạn! Mua thêm ngay gói ngày chỉ [X]đ để tiếp tục cày phim mượt mà cuối tháng."
    *   **CTA:** Mua thêm gói ngày.

*   **Kịch bản 3.2: Hết quota nhưng còn hạn**
    *   **Context:** Đã dùng 100% dung lượng data tốc độ cao, đang bị ngắt kết nối hoặc bóp băng thông chờ ngày gia hạn.
    *   **Nội dung Widget:** Nổi bật, giải pháp "Cứu nét".
    *   **Copywriting:** "Bạn đã dùng hết data tốc độ cao của kỳ này. Mua thêm [X]GB để khôi phục tốc độ lướt mạng ngay lập tức!"
    *   **CTA:** Khôi phục tốc độ.

*   **Kịch bản 3.3: Gói sắp hết hạn (<= 7 ngày hoặc <= 3 ngày)**
    *   **Context:** Gói chuẩn bị hết hạn. Cần phân nhánh dựa trên Số dư TKC.
    *   **Nội dung Widget:** 
        *   *Nếu TKC đủ:* "Gói [Tên gói] của bạn sẽ tự động gia hạn sau [X] ngày nữa." (Trạng thái an tâm).
        *   *Nếu TKC không đủ:* Chuyển sang kịch bản 3.5.

*   **Kịch bản 3.4: Hôm nay là ngày hết hạn**
    *   **Context:** Trong vòng 24h gói sẽ hết hạn.
    *   **Nội dung Widget:** Tạo tính cấp bách (Urgency).
    *   **Copywriting:** "Gói cước của bạn sẽ hết hạn vào 23:59 hôm nay. Đảm bảo số dư để tự động gia hạn nhé!"

*   **Kịch bản 3.5: Tài khoản chính (TKC) không đủ gia hạn**
    *   **Context:** Gói sắp hết hạn NHƯNG số dư TKC hiện tại < giá gói đang dùng. Đây là điểm rơi quan trọng (Drop-off point) cần xử lý khéo.
    *   **Nội dung Widget:** Trạng thái Cảnh báo + Kêu gọi hành động trực tiếp.
    *   **Copywriting:** "Số dư không đủ để gia hạn gói [Tên gói] vào ngày mai. Nạp thêm tối thiểu [X]đ để không bị ngắt kết nối!"
    *   **CTA:** Nạp tiền ngay.

## Tổng kết Nguyên tắc UI/UX cho Widget:
1. **Phân loại mức độ chú ý (Visual Weight):** Các kịch bản cảnh báo (1.2, 3.2, 3.5) cần dùng màu sắc nổi bật (Vàng/Đỏ) và Action ưu tiên. Các kịch bản thông tin (3.3) chỉ cần màu trung tính (Xanh/Trắng).
2. **Action-Oriented (CTA rõ ràng):** Mỗi widget chỉ nên có 1 nút Call-to-Action chính hướng thẳng đến luồng thanh toán hoặc đăng ký.
3. **Smart Fallback:** Nếu người dùng rơi vào nhiều điều kiện cùng lúc (VD: Vừa hết data, vừa không đủ tiền gia hạn), hệ thống cần phân định Rule ưu tiên hiển thị. Thông thường ưu tiên xử lý tình huống "Không đủ tiền gia hạn" (Kịch bản 3.5) vì nó ảnh hưởng đến Business Goal lớn nhất là tỷ lệ giữ chân (Retention).
