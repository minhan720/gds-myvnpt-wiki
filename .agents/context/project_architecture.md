# Project Architecture & Ecosystem

Tài liệu này cung cấp cài nhìn tổng quan về hệ sinh thái các Agent, quy trình (Workflows), và cấu trúc kiến trúc vận hành trong GDS-MyVNPT. 
Vui lòng tham khảo tài liệu này để nắm bắt luồng giao tiếp giữa các thành phần gốc.

## 1. Phân bổ vai trò trong Hệ sinh thái Agent (`.agents/roles`)
- **Nhóm Flow Design / UX:** Đảm nhiệm luồng thao tác, UX Benchmark, phân tích URD & mapping tài liệu. Các Role chính bao gồm UX Designer, Researcher.
- **Nhóm UI/UX Audit:** Chuyên rà soát UI/UX, Cognitive load, WCAG. Làm việc độc lập với nhóm quy trình thiết kế để đảm bảo chất lượng khách quan.
- **Nhóm Jira / Operations:** Quản lý tự động hóa Sync Jira, Push cập nhật, làm báo cáo Weekly Recap. 
- **Nhóm McKinsey (Research & Analysis):** Thu thập dữ liệu cấp độ vĩ mô, phân tích dữ liệu và thiết lập báo cáo định hướng cải tiến chiến lược dài hạn.

## 2. Hệ thống Pipeline & Quy trình (`.agents/workflows`)
Hệ thống tận dụng **Pipeline xuyên mạch** có sự hỗ trợ của **HITL (Human-in-the-loop)**.
- Khi nhận Input từ người dùng (Email, Jira Ticket, Báo cáo URD), hệ thống kích hoạt Workflow tương ứng.
- Agent sẽ lần lượt chạy qua các bước quy định. Giữa các bước nghiêm trọng, Agent sẽ dừng lại để xin phản hồi hoặc chờ duyệt từ User (via /slash commands).

## 3. Hệ sinh thái Dữ liệu (Data Sources)
1. **Atlassian Jira:** Nơi Input của các yêu cầu khởi tạo (PYC, bug, improvements) bắt đầu. Tracker tiến độ.
2. **Google Sheets:** Cơ sở dữ liệu theo dõi dự án gọn nhẹ, thường dùng cho Tracking PhatSinh, Master Data.
3. **Figma:** Nơi thiết kế UI/UX, đóng vai trò là nguồn Input cho các yêu cầu Audit.
4. **Wiki / Knowledge Base:** Nơi xuất bản tư liệu hoàn chỉnh, lưu trữ Design Spec cuối cùng để tổ chức có thể tham chiếu về sau.

## 4. Kiến trúc Hệ sinh thái Giải pháp (Solutions Architecture)
- **VNPT Digital ID (SSO):** Cấu trúc định danh Master dịch chuyển từ mã hóa "Mã thuê bao" sang "Chủ thể Con Người", đóng vai trò cốt lõi để gom luồng dữ liệu khách hàng đa mạng.
- **DigiZone Tri-Hub Ecosystem:** Cấu trúc nền tảng chia làm 3 cực quản lý lõi từ xa: **Family Hub** (Tài chính Di động/Fiber), **DigiHome** (Router Firewall Vành đai điện toán), và **DigiBox** (MyTV Remote thông minh).
