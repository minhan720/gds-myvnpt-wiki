---
name: mail_fetch
description: Kỹ năng truy cập Email cá nhân, xử lý OTP và lọc dữ liệu thô.
---

# Mail Fetch Skill

Kỹ năng dành cho `Mail Operations Bot` để lấy dữ liệu từ Inbox.

## Nguyên tắc Vận hành:
1. **Kết nối:** Sử dụng giao thức IMAP/API để truy cập hộp thư.
2. **Xác thực OTP:** 
   - Sau khi gửi User/Pass, Bot phải dừng lại.
   - Gửi yêu cầu "BOSS ơi, cho em xin mã OTP để vào Mail ạ" qua Telegram.
   - Chờ phản hồi từ Telegram có chứa mã số.
3. **Lọc nội dung:**
   - Duyệt danh sách mail mới.
   - Chỉ lấy các mail thỏa mãn bộ quy tắc `mail_classification_rules.md`.
   - Bỏ qua các mail nhạy cảm (Lương) hoặc mail rác.
4. **Đầu ra:** Xuất dữ liệu vào cấu trúc bảng (Excel-ready) để Analyst xử lý.
