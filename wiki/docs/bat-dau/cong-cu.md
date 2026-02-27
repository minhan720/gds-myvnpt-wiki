# 🛠️ Bộ Công Cụ Làm Việc (Tool Stack)

Dưới đây là danh sách các công cụ lõi được sử dụng trong hệ sinh thái Agentic AI Workspace của dự án. Mỗi công cụ đều được phân bổ chuyên biệt cho từng vai trò để đảm bảo mọi quy trình diễn ra trơn tru, gọn gàng và hạn chế "loãng" thông tin.

---

## 1. 🤖 Antigravity (Agentic AI Workspace)
- **Gắn liền với Role:** Product Owner (PO), Chuyên gia UI/UX, Quản trị dự án.
- **Mục đích sử dụng:**
  Không gian chỉ huy đầu não. Đây là nơi duy nhất bạn điều phối binh đoàn AI tạo sinh khổng lồ thay vì chỉ lập trình code.
  - **Đối với PO:** PO mở Tool này dùng để "gọi hồn" (kích hoạt) các Agent Teams như đội Nghiên cứu thị trường hay Jira Tracking. PO giao việc (Briefing) qua khung Chat, thực thi quyền sinh sát (Kiểm duyệt `HITL - Human in The Loop`), phê duyệt các Specs/Tài liệu nội dung và đẩy nó thẳng lên hệ thống Website (Wiki) nội bộ bằng lệnh chớp nhoáng `/deploy-website`.
  - **Đối với chuyên gia UI/UX:** Nơi để triệu hồi `ux-design-team` vẽ luồng hành vi dựa trên Phân tích Nỗi đau, và triệu hồi `uiux-audit-team` để "giết rệp" (bắt lỗi Edge Cases) từ Link Figma. Mọi chất xám đều được gọt giũa ở đây trước khi đem ra vẽ tay.

---

## 2. 🎨 Figma
- **Gắn liền với Role:** Chuyên gia UI/UX, Product Owner (Người Review).
- **Mục đích sử dụng:**
  Bàn vẽ thực địa, nơi các luồng suy nghĩ và phân tích từ Antigravity (JTBD Flow) được cụ thể hoá thành Giao diện Tương tác.
  - **Thiết kế & Prototype:** Phác thảo Wireframes thấp đến Màn hình UI độ nét cao. Gắn liên kết tương tác thật (Prototype) cho App MyVNPT.
  - **Kiểm định AI:** Khi màn hình vẽ xong, Link Figma sẽ được cung cấp làm "Thức ăn ngõ vào" (Input) cho `uiux-audit-team` quét độ sai lệch giao diện (UI) và ngữ cảnh chữ nghĩa (UX Writing).

---

## 3. 🎫 Jira (Task Tracking)
- **Gắn liền với Role:** Product Owner (PO), Techlead, Scrum Master.
- **Mục đích sử dụng:**
  Quản lý danh mục Công việc (Backlog) cốt lõi của máy móc và con người.
  - **Điều khiển tiến độ:** PO dùng Jira để tạo các Ticket chẻ nhỏ tính năng lớn, ấn định thời gian Sprint.
  - **Báo cáo không chạm:** Hệ thống AI `jira-tracking-team` sẽ luồn lách vào mỏ dữ liệu Jira mỗi đêm, múc ra những Tickets nào đang bị trễ hạn, ai đang ngâm lâu, mảng nào đang "Bùng cháy" để chắt lọc cảnh báo cho sếp.

---

## 4. ✈️ Telegram
- **Gắn liền với Role:** Toàn bộ thành viên (Cả Người lẫn Bot).
- **Mục đích sử dụng:**
  Kênh Giao tiếp Siêu tốc (Alerting & Trigger).
  - **Báo cáo định kỳ:** Khung cửa sổ telegram nhóm là nơi đội ngũ `jira-tracking-team` xả hàng mỗi sáng, bắn bản tin tóm tắt tiến độ cực xịn do tụi nó gọt dũa xong. PO chỉ cần mở điện thoại lướt nhóm Telegram để nắm đại cuộc dự án lúc 8h sáng.
  - **Văn hoá Handoff:** Telegram không dùng để lưu tài liệu. Chỉ dùng để Tag Ping (Gào thét) gọi nhau vào Review tài liệu: *"Anh zai xem tài liệu Specs tại Wiki nhé"*.
