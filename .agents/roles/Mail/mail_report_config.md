# Mail Report Configuration (Config)

File này chứa cấu hình tham số mặc định cho luồng đọc và xử lý Email.

## 1. Thông tin xác thực (Credentials)
- **Email/Account:** Khi khởi chạy, Bot sẽ yêu cầu nhập qua kênh bảo mật.
- **OTP Auth:** Chờ lệnh nhập từ BOSS qua Telegram.

## 2. Màng lọc nội dung (Email Filters)
- **Keywords cần lấy (Include):** 
  - Yêu cầu, Task, Công việc, Dự án, PYC, Support, Fix bug, Triển khai.
- **Keywords loại trừ (Exclude):**
  - Bảng lương, Tiền lương, Quảng cáo, Thông báo hệ thống, Newsletter.

## 3. Tiêu chí thời gian (Time Metrics)
- **Deadline Alert:** Cảnh báo nếu Task cần hoàn thành trong vòng `3 ngày`.
- **New Task:** Email nhận được trong vòng `12 giờ` qua.

## 4. Cấu hình Telegram (Thông tin kết nối)
- **Token Bot:** `8757329276:AAG5zL8re4xprBhFPuJQ-yr0DS6FxUesWK4` (Dùng chung với bộ Jira nếu cần đồng nhất)
- **Group Chat ID (PYC):** `-4580999681` (Nhóm dự án)
- **Group Chat ID (Support):** `-4580999681` (Nhóm hỗ trợ)
