---
description: Lệnh chóp bu điều hướng các Use-cases xử lý Email (Report, OTP, Filter).
---

# Mail Tracking Master Workflow

**Mục tiêu:** Workflow tổng rẽ nhánh thông minh dựa trên mong đợi của User để quản lý công việc qua Email.

1. **Khởi Trình:** User gõ lệnh `/mail_tracking_master` kèm theo Use-case mong muốn.

// turbo-all
2. **Định Tuyến Yêu Cầu:**
   - Nếu cần **Tổng hợp Báo cáo Recap (Hàng ngày/Hàng tuần)**: Gọi `/Mail/workflow_mail_recap`.
   - Nếu cần **Kiểm tra nhanh OTP/Trình trạng kết nối**: Gọi lệnh check status của Operations Bot.
   - Nếu cần **Cập nhật quy tắc lọc mail**: Yêu cầu Analyst cập nhật `mail_classification_rules.md`.

3. **Luật Bắt Di Bất Dịch:**
    - Tuyệt đối không lưu trữ OTP hoặc Password trong log file.
    - Không gửi báo cáo ra ngoài nếu chưa có lệnh `Approved` từ BOSS.
