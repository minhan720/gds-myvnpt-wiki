---
description: Tự động đọc URD -> Xuất Sheets lẻ cho từng luồng (Standalone).
---
# 📂 /workflow_create_events [link hoặc file URD]

## 🛠 QUY TRÌNH XUẤT FILE EVENT RIÊNG BIỆT (STANDALONE)

Quy trình này áp dụng khi cần trích xuất Event từ tài liệu URD và tạo ra một file Google Sheets mới hoàn toàn, tách biệt khỏi hệ thống Master.

### 1. 🔍 Đọc tài liệu (Fetch & Analyze)
- AI truy cập Link Google Doc hoặc đọc nội dung File URD được cung cấp.
- AI phân tích bóc tách các điểm chạm (Touchpoints) và quy trình nghiệp vụ.

### 2. 🏗️ Thiết kế Đa tầng & 📝 Định dạng chuẩn
// turbo
- **Cấu trúc 4 tầng:** Display -> Action -> Security -> Operations.
- **Ràng buộc:** Bắt buộc có `fromFeature` cho các sự kiện hiển thị màn hình.
- **Tham số Gốc:** Luôn có `partnerName = myvnpt` và `screenName` cho mọi Event.
- **Format:** Trình bày Multiline, ID Prefix Module duy nhất (VD: GR, MC, RW...).
- **Kỹ thuật:** Cột `Param operator` sử dụng dấu `'=`.

### 3. 💬 Hội ý & ✅ Xuất bản (PO Review & Publish)
- AI hiển thị bản Draft ngay tại khung chat để PO kiểm tra và phản hồi điều chỉnh.
- **Sau lệnh "OK" của PO:** 
    1. AI chạy script `manage_event_sheets.py standalone [URD_ID]`. 
    2. AI ghi dữ liệu vào file Google Sheets mới.
- AI gửi link file kết quả cho PO.

---
> 📑 **Tài liệu hướng dẫn:** [Wiki GDS Event Tracking](https://docs.google.com/document/d/1ijlT2MON4Ofm7IwjrEckXUsHqHFsjmVADw6dt1U6pgY/edit?usp=drivesdk)
