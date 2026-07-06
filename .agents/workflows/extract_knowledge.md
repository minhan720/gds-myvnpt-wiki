---
description: Pipeline chiết xuất tri thức - Tổng hợp và cập nhật Context dự án sau mỗi phiên làm việc (3 Bước + HITL)
---

# Extract Knowledge Workflow (/extract_knowledge)

**Mục tiêu:** Kích hoạt thủ công sau khi một dự án hoặc một phiên làm việc (chat session) kết thúc. Workflow này sẽ tự động đọc lại lịch sử làm việc để rà soát "những điều mới học được", phân loại chúng và xin phép User (Boss) để ghi vĩnh viễn vào hệ thống nhớ dài hạn (`.agents/context/`).

## Bước 1: Rà soát & Trích xuất (Knowledge Extraction)
1. **Task:** Agent tự động đọc lại các file kết quả vừa sinh ra (VD: Spec, Report) hoặc nội dung vừa trao đổi trong hội thoại.
2. **Criteria:** Phân tích và lọc ra các yếu tố mới thuộc 3 nhóm sau:
   - **Thuật ngữ (Glossary):** Các từ viết tắt, từ lóng nội bộ, định nghĩa nghiệp vụ mới chưa có trong `glossary_vnpt.md`.
   - **Tiêu chuẩn UI/UX:** Các rule thiết kế mới, component mới hoặc lỗi UX điển hình vừa sửa chưa có trong `ui_ux_guidelines.md`.
   - **Kiến trúc (Architecture):** Tên file mới, luồng chạy mới, hoặc Database mới chưa có trong `project_architecture.md`.
3. **Output:** Lập một bảng tóm tắt trình bày các "Tri thức mới" phát hiện được, ví dụ: 
   | Loại Tri thức | Tên / Khái niệm | Định nghĩa | Target File |

## Bước 2: Báo cáo & Phê duyệt (HITL - Human In The Loop)
1. **Action:** Trình bày bảng tóm tắt trên cho Boss.
2. **Review:** Hỏi ý kiến Boss: *"Boss xem lại danh sách tri thức mới ở trên. Boss có muốn tôi bỏ đi mục nào hoặc chỉnh sửa định nghĩa nào không, hay đồng ý đưa thẳng toàn bộ vào các file Context?"*
3. **Wait:** **DỪNG LẠI HOÀN TOÀN** để chờ lệnh Approve từ Boss. Agent tuyệt đối không tự ý ghi file khi chưa có sự xác nhận ở bước này.

## Bước 3: Cập nhật Hệ thống Context (System Update)
1. **Action:** Khi Boss phê duyệt, Agent sử dụng tool chỉnh sửa text để bổ sung tự động các danh mục này vào đúng vị trí trong 3 file ở thư mục `.agents/context/`.
2. **Constraint:** 
   - Chỉ được NỐI THÊM (Append / Insert) vào đúng đề mục (Heading) hoặc danh sách (Bullet points).
   - Tuyệt đối **KHÔNG XÓA** hoặc thay đổi ý nghĩa các tri thức cũ đã tồn tại, trừ khi Boss dặn chép đè.
3. **Kết thúc:** Xác nhận đã lưu thành công và dự án đã được lưu trữ vào bộ nhớ dài hạn, sẵn sàng cho các Agent khác đọc ở phiên làm việc sau.
