---
description: Pipeline tự động tạo tài liệu Hướng dẫn sử dụng & Vận hành từ URD, SRS và Design.
---

Để khởi chạy quy trình này, BOSS vui lòng cấp các thông tin sau:
1. **Input:** Link hoặc nội dung của (URD, SRS, Design Flow).
2. **Yêu cầu:** Gộp chung 1 file hay tách riêng 2 file Word/Doc.

**Các bước thực hiện của Antigravity:**
1. **Phân tích:** Đọc kỹ URD (Business), SRS (Technical) và Design (Frontend).
2. **Biên soạn Phần 1 - Hướng dẫn Người dùng (End-User):** 
   - Giới thiệu lợi ích.
   - Hướng dẫn thao tác bằng hình ảnh/text.
   - Các câu hỏi thường gặp (FAQ cho KH).
3. **Biên soạn Phần 2 - Hướng dẫn HTKH & Khiếu nại (Support Playbook):**
   - Các kịch bản lỗi (Error Codes từ SRS).
   - Ma trận xử lý khiếu nại (Root cause & Solution).
   - Danh sách đầu mối phối hợp.
4. **Đồng bộ Drive:** Tự động tạo Google Doc và gửi link cho BOSS.

// turbo
5. Chạy script `export_manual_to_drive.py` để xuất bản.
