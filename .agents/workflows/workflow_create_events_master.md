---
description: Tự động đọc URD -> Đăng ký màn hình mới -> Tạo Tab mới trong file Master.
---
# 📁 /workflow_create_events_master [link hoặc file URD]

## 🛠 QUY TRÌNH TÍCH HỢP EVENT VÀO HỆ THỐNG MASTER

Quy trình này áp dụng khi muốn đưa một luồng nghiệp vụ mới vào "Đại bản doanh" [GDS Master File](https://docs.google.com/spreadsheets/d/10PDEoMns5mgP4_FWRUDQ2e9nUWaCNmtkKqnix3dA4ZA/). 

### 1. 🔍 Đọc dữ liệu & 📔 Tra cứu Từ điển
- AI truy cập link URD và đồng thời tra cứu Sheet **[Tên màn hình]** trong Master File.
- Tự động tái sử dụng `screen_name` cũ nếu đã tồn tại; đề xuất đăng ký mới nếu là màn hình hoàn toàn mới.

### 2. 🏗️ Thiết kế Đa tầng & 📐 Chuẩn hóa (Compliance)
// turbo
- **Mạch liên thông:** Ràng buộc `fromFeature` cho hành trình CJM xuyên suốt.
- **Bao phủ 4 tầng:** Display -> Action -> Security -> Operations.
- **Mã hóa:** Gán mã ID duy nhất kèm Prefix cho từng Module (Module-based Prefix).
- **Format:** Dữ liệu Multiline, tham số gốc `partnerName = myvnpt` cho mọi bản ghi.

### 3. 💬 Hội ý & 📁 Thực thi (PO Review & Master Integration)
- AI hiển thị bản Draft tại khung chat để PO duyệt.
- **Sau lệnh "OK" của PO:**
    1. AI tự động cập nhật Từ điển màn hình mới.
    2. AI tạo Tab (Sheet) mới trong file Master đặt tên theo tên luồng URD. 
    3. AI ghi dữ liệu chuẩn vào hệ thống.
- AI gửi link Master File và thông báo danh mục màn hình vừa đăng ký.

---
> 📑 **Tài liệu hướng dẫn:** [Wiki GDS Event Tracking](https://docs.google.com/document/d/1ijlT2MON4Ofm7IwjrEckXUsHqHFsjmVADw6dt1U6pgY/edit?usp=drivesdk)
