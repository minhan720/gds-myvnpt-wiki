# GLOBAL WORKSPACE RULES

## OUTPUT RULE (Bắt buộc với tất cả các Team / Agents)
Từ nay, sản phẩm phân tích, file thiết kế, và tài liệu (Output) của TẤT CẢ CÁC AGENTS (UR, UX, TW, CR,...) trong mọi team (ux-design-team, scrum-team, pg-insights-team,...) KHÔNG được lưu ở thư mục cục bộ `docs/` của từng team nữa, mà **BẮT BUỘC** phải được lưu tập trung vào thư mục `knowledge base/` nằm ở thư mục gốc của dự án.

Cấu trúc lưu trữ ví dụ như sau:
- UR Research: `knowledge base/[team-name]-output/research/`
- UX Flows: `knowledge base/[team-name]-output/ux/`
- TW Docs & Specs: `knowledge base/[team-name]-output/docs/`
- CR Reviews: `knowledge base/[team-name]-output/reviews/`

*Các agent khi giao tiếp `tm-send` cũng phải báo cáo lại đường dẫn theo cấu trúc mới này.*

## SPECIFICATION TEMPLATE RULE (Quy Chuẩn Viết Spec)
Từ nay về sau, khi Boss yêu cầu viết/làm Docs/Specs/URD cho bất kỳ tính năng nào, TẤT CẢ các Agent (như TW, PM, UR, BA...) đều **phải mô tả theo định dạng chuẩn "Full-stack Product Spec"**.
Không được tự ý chế form hoặc viết đặc tả nghèo nàn. Bản Spec phải đạt tiêu chuẩn gồm đủ 5 mảng:
1. Bối cảnh & Mục tiêu (Business)
2. Trải nghiệm người dùng & Copy (UX/UI)
3. Quy trình Step-by-step
4. Đặc tả Nghiệp vụ & Rule hệ thống ngầm (Backend)
5. Vận hành & Testing

**Template gốc (File mẫu) nằm tại:** 
`knowledge base/templates/full-stack-spec-template.md`

(*Agent phải đọc file template này để lấy form điền thông tin khi được giao task viết tài liệu Specs*).

## CONTINUOUS APPROVAL RULE (Quy tắc Xác nhận Từng Bước)
Từ nay về sau, khi làm việc THEO CHUỖI ROLE (Ví dụ: chạy luồng PM -> UR -> UX -> TW), AI (Antigravity hoặc các Agents) **BẮT BUỘC KHÔNG ĐƯỢC TỰ Ý CHẠY MỘT MẠCH HẾT CÁC BƯỚC**.
Sau khi hoàn thành xong phần việc của *MỖI MỘT ROLE* (ví dụ: UR vừa làm xong báo cáo Research), AI phải **DỪNG LẠI và hỏi ý kiến (permission) của Boss**.
- **Nếu Boss yêu cầu chỉnh sửa:** Phải tiến hành sửa đổi, căn chỉnh tài liệu của Role hiện tại ngay lập tức cho đến khi Boss thực sự hài lòng.
- **Nếu Boss "Duyệt" hoặc "OK":** AI mới được phép thay mũ, chuyển qua đóng vai Role tiếp theo để làm tiến trình công việc kế tiếp.
