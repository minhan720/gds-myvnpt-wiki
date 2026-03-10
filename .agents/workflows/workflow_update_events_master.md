---
description: Cập nhật lại hoặc Chuẩn hóa lại nội dung một tính năng cũ (Bổ sung OTP/Backend...).
---
# 🛠 /workflow_update_events_master [link hoặc file URD]

## 🏗️ QUY TRÌNH CHUẨN HÓA & CẬP NHẬT TÍNH NĂNG CỐ

Quy trình này áp dụng khi cần nâng cấp, sửa đổi hoặc chuẩn hóa lại nội dung cho một tính năng/Tab đã tồn tại trong file Master (VD: Bổ sung OTP, Sửa ID, Thêm API Backend).

### 1. 🔍 Phân tích Thay đổi (Gap Analysis)
- AI đối soát tài liệu yêu cầu mới với nội dung cũ trong Sheet tương ứng.
- Xác định các "lỗ hổng" dữ liệu cần lấp đầy (VD: thiếu sự kiện `ops_receive_be`).

### 2. 📐 Tái cấu trúc theo Quy chuẩn PO 2026
// turbo
- **Chuẩn hóa ID:** Chuyển đổi mã định danh sang Prefix mới (ID duy nhất).
- **Thêm tầng dữ liệu:** Bổ sung lớp Security (OTP) và Operations (API) nếu luồng cũ còn thiếu.
- **Xâu chuỗi:** Hiệu chỉnh `fromFeature` để đảm bảo mạch liên thông.
- **Formatting:** Thiết lập dữ liệu Multiline, `partnerName = myvnpt` và `screenName` chuẩn.

### 3. 💬 Hội ý & 🛠 Thực thi Update (PO Review & Overwrite)
- AI hiển thị bản dự thảo chuẩn hóa để PO kiểm tra.
- **Sau lệnh "OK" của PO:**
    1. AI chạy script `manage_event_sheets.py update [URD_ID]`. 
    2. AI thực hiện ghi đè dữ liệu mới, chuẩn hóa 8 cột vào Tab cũ trong Master File.
- AI gửi link kết quả và báo cáo các lớp dữ liệu vừa được bổ sung.

---
> 📑 **Tài liệu hướng dẫn:** [Wiki GDS Event Tracking](https://docs.google.com/document/d/1ijlT2MON4Ofm7IwjrEckXUsHqHFsjmVADw6dt1U6pgY/edit?usp=drivesdk)
