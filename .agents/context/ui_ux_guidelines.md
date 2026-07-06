# UI/UX Evaluation Guidelines

Tài liệu này định nghĩa các tiêu chuẩn đánh giá và thiết kế UI/UX cốt lõi dành cho GDS-MyVNPT. Các Agent (đặc biệt là nhóm UI/UX Audit hoặc Flow Design) cần bám sát các tiêu chuẩn này khi tạo spec hoặc audit bản thiết kế.

## 1. Cognitive Load (Tải trọng nhận thức)
- **Tối giản hóa:** Tránh nhồi nhét quá nhiều thông tin vào một màn hình duy nhất.
- **Phân cấp cấp bậc rõ ràng:** Thông tin chính (Primary) cần nổi bật, thông tin phụ trợ (Secondary, Tertiary) nên được thu gọn hoặc nằm đúng ngữ cảnh cần thiết.
- **Tập trung:** Mỗi màn hình lý tưởng nhất chỉ nên phục vụ thực hiện từ 1 đến 2 Intent (Ý định) cốt lõi của người dùng.

## 2. Visual & Accessibility (WCAG 2.1)
- **Độ tương phản (Contrast Ratio):** Đảm bảo độ tương phản giữa văn bản và nền ít nhất là 4.5:1 (mức AA).
- **Kiểu chữ (Typography):** Sử dụng font chữ và text-styles chuẩn thuộc Design System. Không sử dụng quá 3 kích cỡ chữ trên cùng một nhóm thông tin nhỏ.
- **Layout & Spacing:** Sử dụng spacing theo cấp số nhân cơ bản (vd: 4px, 8px, 16px, 24px) thống nhất trên toàn hệ thống.
- **Màu sắc (Color Palettes):** Tuân thủ hệ thống màu trạng thái mặc định (Success, Warning, Error, Info) nhằm tránh làm người dùng bối rối.

## 3. UX Writing (Copywriting)
- **Rõ ràng, dễ hiểu:** Súc tích, tránh từ ngữ chuyên ngành hẹp quá mức nếu đối tượng là người dùng phổ thông.
- **Call to Action (CTA):** Nút bấm cần thể hiện rõ hành động. Các từ như "Xác nhận", "Tiếp tục", "Hủy" được ưu tiên hơn so với từ "OK" hay "Yes".
- **Thông báo rủi ro:** Nội dung báo lỗi (Error message) cần cho người dùng biết lỗi gì đã xảy ra VÀ cách khắc phục cụ thể.
- **Đại sứ Giao tiếp (Emi Speak-out):** Mọi dòng Text trên giao diện (nút bấm, tiêu đề, thông báo) bắt buộc viết giả lập dưới góc độ trợ lý Emi đang trực tiếp trao đổi 1-1 với khách hàng.
- **Triết lý No-Jargon:** Tuyệt đối dẹp bỏ thuật ngữ kỹ thuật hàn lâm và các mã báo lỗi rập khuôn. Dùng lời trò chuyện thiết thực kết hợp *Hình ảnh mô phỏng trạng thái trực quan* để xoa dịu người mù công nghệ.
