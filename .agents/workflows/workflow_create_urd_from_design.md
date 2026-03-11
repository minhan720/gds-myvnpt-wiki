---
description: Pipeline tự động bóc tách Thiết kế (Figma/Ảnh) để khởi tạo tài liệu URD chuẩn cấu trúc GDS.
---
# 📁 /workflow_create_urd_from_design [Link Figma hoặc Ảnh]

## 🎯 MỤC ĐÍCH (PURPOSE)
Hệ thống AI sẽ đóng vai trò Product Analyst (PA), tự động quan sát hành trình người dùng trên bản thiết kế (Figma/Ảnh) để chuyển đổi thành tài liệu **Yêu cầu nghiệp vụ (URD - User Requirement Document)** chuyên nghiệp, làm tiền đề cho việc Code và Tracking.

---

## 🛑 QUY TẮC ĐẶC TẢ (SPECIFICATION RULES)

### 1. Kỷ luật Định danh (Naming Convention)
Mọi màn hình được bóc tách phải gán mã `screenName` theo đúng tiền tố:
- `SCR_`: Màn hình giao diện chính (Full screen).
- `POP_`: Cửa sổ nổi (Popup/Modal).
- `BTS_`: Cửa sổ trượt (Bottom Sheet).
- `z_`: Ghi chú / Frame nháp (AI sẽ bỏ qua).

### 2. Cấu trúc tài liệu chuẩn (Standard Structure)
Tài liệu URD xuất ra phải bao gồm các mục:
1. **Thông tin chung:** Tên tính năng, dự án, người thực hiện.
2. **Hành trình người dùng (User Journey):** Mô tả Step-by-step từ điểm chạm đầu đến cuối.
3. **Đặc tả UI/UX:** Bảng liệt kê các thành phần giao diện, mã màn hình và hành vi tương ứng.
4. **Quy tắc nghiệp vụ (Business Rules):** Các điều kiện ràng buộc, logic xử lý lỗi, thời gian chờ (Timeout).
5. **Hướng đo lường (Tracking Strategy):** Đề xuất các nhóm sự kiện cần track (chưa cần chi tiết 8 cột).

---

## 🛠 QUY TRÌNH THỰC THI

### B1. 🔍 Soi thiết kế (Visual Analysis)
- Truy cập Link Figma hoặc phân tích Ảnh chụp màn thiết kế.
- Xác định đâu là màn chính, đâu là popup, đâu là hành động chuyển trang.

### B2. 🏗️ Phác thảo Luồng (Flow Drafting)
- Xây dựng sơ lược các bước người dùng sẽ đi qua.
- Suy luận logic đằng sau các nút bấm (ví dụ: Bấm liên kết thì phải có OTP).

### B3. 📝 Khởi tạo tài liệu (URD Creation)
- Viết tài liệu theo định dạng Markdown.
- Đặt tên file theo chuẩn: `urd_[ten_tinh_nang].md`.

### B4. 💬 Chốt URD (Verification)
- Gửi tài liệu cho PO/BA duyệt trước khi chuyển sang bước thiết kế Event Tracking `/workflow_create_events_standard`.
