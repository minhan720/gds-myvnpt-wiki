# 📑 HƯỚNG DẪN VẬN HÀNH PIPELINE EVENT TRACKING TỰ ĐỘNG (GDS STANDARD 2026)

Tài liệu này đặc tả quy trình sử dụng trợ lý AI (Antigravity) để tự động hóa việc thiết kế và quản trị dữ liệu Event Tracking cho dự án GDS VNPT.

---

## Ⅰ. MỤC ĐÍCH CỦA PIPELINE (PURPOSE) 🎯

Hệ thống được thiết kế nhằm tối ưu hóa quy trình làm việc của đội ngũ Product/BA qua các mục tiêu:
*   **Tăng tốc hiệu suất:** Giảm 90% thời gian soạn thảo thủ công bảng Event từ các tài liệu yêu cầu (URD/SRS).
*   **Quản trị tập trung:** Tự động đồng bộ hóa các định danh mới vào "Từ điển hệ thống" và duy trì file Master luôn cập nhật.
*   **Liên thông hành trình:** Đảm bảo mọi sự kiện đều có tính kết nối để phục vụ báo cáo hành trình khách hàng (CJM) chuyên sâu.

---

## Ⅱ. CÁC LỆNH ĐIỀU KHIỂN (COMMANDS) 🚀

Người dùng sử dụng các lệnh điều hướng sau kèm theo link Google Doc hoặc file nội dung URD:

| Câu lệnh (Slash Command) | Chức năng chính | Output mong đợi |
| :--- | :--- | :--- |
| **`/workflow_create_events [link hoặc file URD]`** | **Trích xuất File lẻ:** Tự động đọc URD và xuất dữ liệu tracking ra file Google Sheets riêng lẻ cho từng luồng. | File Sheets Standalone (cho đối tác/Dev). |
| **`/workflow_create_events_master [link hoặc file URD]`** | **Tích hợp File Master:** Tự động đọc URD -> Đăng ký màn hình mới -> Tạo Tab mới trong file GDS Master tổng. | Cập nhật hệ thống Master File tập trung. |
| **`/workflow_update_events_master [link hoặc file URD]`** | **Chuẩn hóa & Nâng cấp:** Cập nhật lại hoặc Chuẩn hóa lại nội dung một tính năng cũ (Bổ sung OTP, API Backend...). | Ghi đè/Cập nhật dữ liệu chuẩn vào Tab cũ. |

---

## Ⅲ. CƠ CHẾ HOẠT ĐỘNG: AI SẼ LÀM GÌ? (PROCESSING FLOW) 🤖

Hạ tầng AI thực hiện quy trình xử lý khép kín qua 6 bước chi tiết:

1.  **🔍 Đọc tài liệu (Fetch & Analyze):** 
    - AI truy cập vào Link Google Doc được cung cấp hoặc đọc trực tiếp nội dung File URD.
    - Phân tích các phân đoạn nghiệp vụ, bóc tách các bước hành động của người dùng (User Steps) và các phản hồi của hệ thống để xác định các điểm chạm (Touchpoints).
2.  **📔 Tra cứu Từ điển (Dictionary Lookup):** 
    - AI tự động truy cập vào file Master, tra cứu Sheet **[Tên màn hình]**.
    - Đối soát nội dung URD với từ điển để tái sử dụng chính xác các `screen_name` đã có, đảm bảo tính nhất quán của định danh.
3.  **🏗️ Thiết kế đa tầng (Multi-layer Design):** 
    - AI cấu trúc hóa các sự kiện theo 4 tầng tương tác bắt buộc: **Display** (Hiển thị màn hình/vùng) -> **Action** (Thao tác người dùng) -> **Security** (Xác thực/OTP) -> **Operations** (Lệnh gọi & Phản hồi API Backend).
4.  **📝 Chuẩn hóa định dạng (Formatting):** 
    - Trình bày dữ liệu theo phong cách Multiline (mỗi tham số 1 dòng).
    - Tự động gán mã ID duy nhất kèm Prefix định danh cho từng Module (VD: MC01, VPC01...).
    - Chèn các tham số gốc hệ thống và xử lý toán tử hiển thị (`'=`) để bảo toàn dữ liệu trên Sheets.
5.  **💬 Hội ý & Hiệu chỉnh (Review):** 
    - AI hiển thị bảng dự thảo (Draft) ngay tại giao diện chat.
    - BA/PO thực hiện kiểm tra và phản hồi yêu cầu điều chỉnh (VD: *"Thêm event cho nút X"*, *"Sửa lại ID thành MC"*).
6.  **✅ Xuất bản (Publish):** 
    - Ngay khi người dùng xác nhận **"OK"**, AI tự động thực hiện ghi dữ liệu trực tiếp vào Google Drive hoặc cập nhật vào Tab tương ứng trong Master File.

---

## Ⅳ. QUY CHUẨN TUÂN THU (COMPLIANCE STANDARDS) 📐

Mọi dữ liệu xuất bản bắt buộc phải tuân thủ Tuyệt đối các nguyên tắc quản trị sau:

*   **🆔 Tính Duy nhất (Uniqueness):** Mỗi sự kiện (Event) được cấp một mã ID duy nhất trong toàn bộ hệ thống để tránh xung đột dữ liệu.
*   **🔗 Mạch liên thông (Continuity):** 
    - Cấu trúc hóa sự kiện theo đúng 4 tầng: **Display -> Action -> Security -> Operations**.
    - Ràng buộc tham số `fromFeature` cho tất cả các sự kiện hiển thị màn hình để đảm bảo hành trình khách hàng được xâu chuỗi xuyên suốt.
*   **📔 Kỷ luật Tên màn (Screen Name):** 
    - Tuyệt đối chỉ sử dụng định danh từ **Từ điển màn hình** của dự án.
    - Thực hiện bổ sung và cập nhật ngay tên màn hình mới vào Từ điển khi phát hiện các màn hình chưa có trong danh mục.
*   **🛡️ Tham số Gốc (Root Parameters):** Mọi sự kiện luôn bao gồm đầy đủ cặp tham số bắt buộc: `partnerName = myvnpt` và `screenName`.

---
> 💡 *Sản phẩm được tối ưu bởi Đội ngũ Antigravity AI Implementation Team phục vụ GDS Standard 2026.*
