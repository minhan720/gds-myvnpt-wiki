---
description: Pipeline tự động đọc mail, xử lý OTP, phân loại và báo cáo Recap đầu việc (PYC/Support).
---

# Thực thi Quy trình Đọc & Recap Mail Tự Động

**Mục tiêu:** Workflow kết hợp AI Agents để tự động hóa việc theo dõi công việc từ Email cá nhân, có chốt rào chắn OTP bảo mật.

1. **Khởi Trình:** User gọi lệnh `/workflow_mail_recap`.

// turbo-all
2. **Kéo Dữ Liệu & Xác thực (Giai đoạn 1):** (Do **Mail Operations Bot** đảm nhiệm)
    - Yêu cầu thông tin Mail (Email/Pass) từ cấu hình hoặc User.
    - **Trigger OTP:** Gửi câu lệnh xin OTP từ BOSS qua Telegram.
    - Khi nhận được OTP từ BOSS, tiến hành mở Mail.
    - **Lọc & Export:** 
        - Lọc các mail yêu cầu thực hiện task (loại bỏ mail lương, info).
        - Tạo file Excel `mail_task_manager.xlsx` chứa: Đâu việc tồn đọng, đầu việc mới.

3. **Phân Tích & Phân loại (Giai đoạn 2):** (Do **Mail Logic Analyst** đảm nhiệm)
    - Đọc dữ liệu từ file Excel thô.
    - **Phân luồng:** Tách dữ liệu thành 2 luồng độc lập: **Nhánh PYC** và **Nhánh Support** dựa trên quy tắc phân loại.

4. **Khai thác Báo cáo (Recap Builder) (Giai đoạn 3):** (Do **Mail Logic Analyst** đảm nhiệm)
    - Sử dụng template Premium `telegram_report_template_premium.md` để trình bày đẹp và dễ đọc hơn.
    - Đánh giá độ gấp và soi rủi ro (Risk Assessment).
    - Tóm tắt tiến độ so với Deadline (Duedate).

5. **Kiểm soát rào chắn (HITL) (Giai đoạn 4):**
    - **Gửi Bản nháp (Draft):** Bot gửi bản nháp báo cáo lên Telegram cho BOSS duyệt.
    - **Chờ lệnh Approved:** Bot dừng lại cho đến khi BOSS phản hồi `Approved`.

6. **Phân phối thông tin (Giai đoạn 5):** (Do **Mail Operations Bot** đảm nhiệm)
    - Thực thi Push báo cáo lên các nhóm Telegram riêng biệt (Nhóm PYC và Nhóm Support).
    - **Auto-Split:** Tự động cắt tin nhắn nếu vượt quá 4096 ký tự.
