# ⚙️ Nguyên Lý Làm Việc & Cách Vận Hành Workspace

Tài liệu này giải thích cơ chế cốt lõi của không gian làm việc này và cách bạn tương tác với trợ lý Agentic AI để khai phá sức mạnh tối ưu nhất.

## 🏗️ 1. Khái Niệm Cốt Lõi: Nhập Vai Tuần Tự (Sequential Role-Playing)

Trong workspace này, chúng ta sử dụng cơ chế **"Một Siêu Đặc Vụ Đội Nhiều Mũ"**. Tập hợp Agentic ở đây đóng vai trò như một Team ảo làm việc trên Máy Khách của bạn.

Thay vì phải dùng các cấu trúc hạ tầng phức tạp hay giao diện thiết lập nhiều màn hình cửa sổ (như Multi-agents qua Terminal/Tmux truyền thống), trợ lý Antigravity được trang bị khả năng **Tự động thay đổi vai trò** (Nhập vai tuần tự) để xử lý một tiến trình lớn từ đầu đến cuối một cách mượt mà nhất.

Antigravity sẽ tự động đọc các "Sổ tay nhân viên" (Role Prompts) của từng tổ đội (Teams) khai báo sẵn.
> **Ví dụ:** Khi bạn kích hoạt chế độ "ux-design-team", nó sẽ chủ động đóng vai *Quản lý (PM)* để lập kế hoạch -> Đổi mũ thành vòng *UX Researcher (UR)* để cày nghiên cứu người dùng -> Tự đổi mũ sang *UX Designer* để vẽ sơ đồ luồng -> Cuối cùng nhập vai *Technical Writer (TW)* để nhào nặn ra file thuyết minh Docs chuẩn chỉnh!

Bạn sở hữu nguyên tổ chức nhân sự đầy đủ vòng chỉ trên đúng duy nhất 1 luồng chat AI!

---

## � 2. Danh Sách Các Đội Nhóm (Teams)

Dưới đây là sơ bộ các đội nhiệm vụ ảo đang chực chờ lệnh từ bạn. Tùy thuộc bài toán đang gặp, hãy chọn tổ đội phù hợp:

<div class="features-grid">
  <div class="feature-card">
    <div class="icon">✏️</div>
    <h3>UX Design Team</h3>
    <p>Phân tích Insight JTBD, vẽ luồng hành vi và lên Full-stack Specs.</p>
    <a href="../teams/ux-design/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">🔍</div>
    <h3>UI/UX Audit Team</h3>
    <p>Soi xét Cognitive Load, bắt chết Edge Cases và kiểm định ngôn ngữ UI.</p>
    <a href="../teams/uiux-audit/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">📊</div>
    <h3>McKinsey Research Team</h3>
    <p>Nghiên cứu thị trường từ xa, chẻ nhánh bài toán và xuất báo cáo Action.</p>
    <a href="../teams/mckinsey-research/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">❤️</div>
    <h3>PG Insights Team</h3>
    <p>Câu Tensions, đúc kết sợi dây liên kết cảm xúc đắt giá nhất của người dùng.</p>
    <a href="../teams/pg-insights/" class="md-button md-button--primary">Chi tiết</a>
  </div>
  <div class="feature-card">
    <div class="icon">⏰</div>
    <h3>Jira Tracking Team</h3>
    <p>Tự động hoá cào nhặt Ticket chìm nổi bắn lên báo cáo Telegram.</p>
    <a href="../teams/jira-tracking/" class="md-button md-button--primary">Chi tiết</a>
  </div>
</div>

---

## �🛑 3. Nguyên Lý Kiểm Duyệt HITL (Human-in-the-Loop)

Trái với xu hướng hiện tại là quẳng cho AI chạy ngầm toàn bộ từ A đến Z sinh ra "ảo giác" (Hallucination) và lỗi dây chuyền khó soát, một số bộ tổ chức cốt lõi trong workspace này tuân thủ nguyên tắc **Kiểm duyệt chốt chặn tại mọi nút giao (Mandatory HITL)**:

- Khi một "nhân sự AI" hoàn thành xong 1 mốc công việc (Ví dụ: UR cày xong tài liệu gốc). Quản lý PM KHÔNG được tự ý đưa sang cho bộ phận thiết kế UX ngay.
- Tiến trình sẽ **tạm dừng (Pause)** hoàn toàn. Trợ lý sẽ đặt câu hỏi lên màn hình thông báo cho Boss (chính là Bạn) để **Review (Duyệt)** file tài liệu đó.
- Chỉ khi bạn xem qua, nếu bắt lỗi thì yêu cầu sửa liền. Nếu không có gì hỏng, bạn gõ lện `>>> Approved` (Phê duyệt) và ấn gửi, thì PM mới được quyền thả xích cho nhân sự tiếp theo chạy phase kế tiếp.

Điều này biến AI thành một "đội ngũ trợ lý tạo nháp liên hoàn", còn quyền Lắp ráp, Đánh giá (Decision Making) vẫn phải thuộc về tư duy của Con người. Chất lượng đầu ra nhờ vậy mà sát cực độ với kỳ vọng nghiệp vụ.

---

## 🛠️ 4. Thao Tác Cơ Bản Vận Hành Các Team

Bạn không cần bấm nhấp nháy chuyển tab phức tạp, các thao tác "ra lệnh cấm - gỡ phong ấn" đều nằm tại một box lệnh:

### Bước 1: Ra Lệnh & Giao Việc Định Hướng (Briefing)
Hãy gửi vào khung chat màn hình nội dung Yêu cầu - Đóng khung Team muốn chọn - Giao mốc chốt:
> *"Đây là bài toán: Thiết kế luồng Mua Gói Cước 4G trên MyVNPT. Ý tưởng của tôi là A, B, C.*
> *Hãy kích hoạt quy trình của `ux-design-team` để thi công nhiệm vụ này. Bạn hãy lần lượt nhập vai qua tuần tự: PM -> UR -> UX -> TW -> CR. Nhớ báo cáo chờ tôi duyệt chốt giữa các khâu nha!"*

### Bước 2: Quan Sát Siêu Đặc Vụ "Chế biến"
- AI Antigravity sẽ vạch ra "Chuỗi tư duy" của nó trên màn hình. Nó đọc rành rọt luật của team vừa gọi, bắt tay tạo các loại files từ Draft tới Final.
- Nó sẽ lần lượt ném ra màn hình: "Báo cáo: Tôi đang xong khâu UX flow rồi, xin sếp Review File này..."

### Bước 3: Ép Sửa Lỗi (Feedback Loops)
Khi Antigravity trình bản nháp mớ vừa làm, bạn đọc nhanh và đưa ngay Feedback:
> *"Sửa chỗ bước Màn hình xác thực (OTP), luồng nó đang bị thiếu bước xác minh Email. Fix ngay"*
> -> AI lập tức vá luồng. Giữ vòng lặp phản hồi này cho tới khi bạn hoàn toàn chốt Sprint.

---

## 📁 5. Các file Cốt Lõi Bạn Cần Cầm Chắc

- `/sample_team`: Kho chứa các "Sổ tay nhập vai, luật cấm" (System/Role Prompts) cực chi tiết của các Team (Nghiên cứu thị trường, Thiết kế UIUX, Jira Tracking,...). Lưu ý **khu vực cấm đụng chạm xoá bớt**.
- `/.agents/skills/SKILL.md`: Đây là "Sách Khải Huyền". File danh mục tổng phổ biến mọi ngóc ngách hệ sinh thái để Antigravity tra cứu.
- `/knowledge base`: Kho tàng tri thức (Output Zone) dùng chung. Tất tật File thiết kế, thông số nghiên cứu, báo cáo Audit thành phẩm đều lưu tại đây để đồng bộ xuất bản.

---

## 🌐 6. Cập Nhật Tài Liệu Lên Website (Auto-Deploy)

Website (Wiki) nội bộ của dự án đã được tích hợp luồng Vercel CI/CD mở rộng tại máy chủ. **TUYỆT ĐỐI** AI không có quyền tự tiện đẩy code lên mạng nếu tài liệu chưa được Human (Boss) đồng ý xác minh.

Khi bạn muốn Cập nhật/Phát hành (Publish) phiên bản tài liệu mới nhất từ Kho `/knowledge base` trôi lên Website chính thức:

1. Bạn không cần tự gõ bất kỳ lệnh Code / Terminal Git loằng ngoằng nào.
2. Vẫn tại giao diện Khung Chat AI hàng ngày, bạn gửi đúng 1 lệnh kích hoạt **Slash Command (Workflow)** sau cho nó:

   > `/deploy-website`

3. Trợ lý Antigravity sẽ đọc ngay workflow deploy, tiến hành dò tìm tài liệu nào vừa tạo, thực thi đóng gói tự động Commit mã nguồn lên GitHub. Tầm 20-30 giây sau Vercel Cloud Server sẽ nạp Database mới và trang Wiki Live của bạn đã có bài mới!
