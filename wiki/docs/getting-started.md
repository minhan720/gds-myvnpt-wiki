# 🚀 Hướng Dẫn Cài Đặt Workspace (Getting Started)

Tài liệu này hướng dẫn các thành viên trong dự án cách tải (clone) toàn bộ môi trường làm việc này về máy cá nhân và thiết lập trợ lý **Antigravity** bằng những quy trình (Team Frameworks) đã được cấu hình sẵn.

---

## 🛠️ Yêu cầu chuẩn bị
1. Máy tính đã cài đặt **[Git](https://git-scm.com/)**.
2. (Tùy chọn) Đã có tài khoản **GitHub**. Nếu kho lưu trữ này (repository) đang ở chế độ Private, vui lòng gửi Username GitHub của bạn cho Admin để được cấp quyền truy cập.
3. Phần mềm/IDE lập trình có tích hợp trợ lý **Antigravity AI**.

---

## Bước 1: Tải Workspace về máy tính (Clone)
Thay vì phải tự tạo từng thư mục file, bạn chỉ cần tải toàn bộ "bộ não" của dự án này về máy bằng các thao tác sau:

1. Mở Terminal (Mac/Linux) hoặc Command Prompt / Git Bash (Windows).
2. Di chuyển đến vị trí thư mục bạn muốn lưu dự án (Ví dụ: `cd Documents`).
3. Chạy lệnh tải mã nguồn từ kho lưu trữ GitHub:

```bash
git clone https://github.com/minhan720/gds-myvnpt-wiki.git
```

4. Di chuyển vào thư mục dự án vừa tải về:
```bash
cd gds-myvnpt-wiki
```

---

## Bước 2: Kích hoạt Antigravity
Điểm đặc biệt của Workspace này là toàn bộ các **"Sổ tay nhập vai"** (Nằm ở `sample_team/`) và **Bộ não kỹ năng** (Nằm ở `.agents/skills/SKILL.md`) đều đã được thiết lập sẵn và đóng gói theo chuẩn.

Bạn không cần cấu hình bằng tay, chỉ cần làm đúng 2 thao tác:
1. **Mở dự án:** Khởi động IDE của bạn -> Chọn chức năng **Open Folder** -> Mở cái thư mục `gds-myvnpt-wiki` bạn vừa `cd` vào ở bước trên.
2. **Sử dụng ngay:** Bật cửa sổ Chat của Antigravity lên. Hệ thống Antigravity sẽ tự động rà quét và "hấp thụ" toàn bộ thư mục `.agents`.

💡 **Ví dụ test thử AI:**
Bạn có thể nhắn ngay câu này vào khung Chat của Antigravity để kiểm tra xem nó đã nhận diện không gian làm việc chưa:
> *"Hãy kiểm tra xem trong workspace này có các team nào ở thư mục sample_team, liệt kê chúng ra."*

---

## Bước 3: Phát triển Trang Web Wiki (Dành cho người viết Docs)
Mọi thay đổi mà đồng nghiệp của bạn tạo ra (Thêm file báo cáo, thêm thiết kế...) vào mục `knowledge base` đều sẽ được tự động hiển thị trên web nội bộ này.

Nếu bạn muốn tạo môi trường giống hệt Admin (Chạy thử Web trên máy tính cá nhân):
1. **Cài đặt thư viện:** Bật Terminal của VSCode lên, chạy lệnh sau để tải các plugin làm đẹp cho Web:
```bash
cd wiki
pip install -r requirements.txt
```
2. **Cắm máy chủ (Local Server):** Chạy tiếp lệnh:
```bash
python3 -m mkdocs serve
```
Và bùm 💥! Bạn mở trình duyệt truy cập `http://127.0.0.1:8000` là có thể xem Web của dự án chạy cực nhanh trên chính máy của mình.

---

## Bước 4: Cập Nhật Tài Liệu Lên Vercel (Auto-Deploy)
Website của dự án đã được tích hợp luồng Deploy tự động (CI/CD) với Vercel. Bất kỳ lúc nào bạn cập nhật nội dung, hệ thống Vercel sẽ tự cảm nhận và tự động tạo lại trang Web theo thời gian thực (Real-time).

**Quy trình Cập nhật:**
1. Hãy nhờ AI viết nội dung mới hoặc bạn tự viết thủ công (tạo các file `.md` mới) vào đúng cấu trúc của thư mục `knowledge base/`.
2. **Sau khi tài liệu đã được Admin (Boss) phê duyệt (Approved):** Bạn không cần tự gõ bất kỳ lệnh Git nào. Hãy gọi trợ lý AI và gửi một từ khóa Slash Command duy nhất vào khung chat:

   > `/deploy-website`

3. Trợ lý AI sẽ tự động kích hoạt luồng kiểm duyệt, đóng gói tài liệu và đẩy (Push) thay đổi lên GitHub chỉ trong một chuỗi thao tác. Bạn có thể tranh thủ 10 - 30 giây rảnh tay uống một ngụm nước.
4. Xong! Bạn truy cập vào đường link Vercel của dự án (Link Public do Admin cung cấp), ấn F5 tải lại trang là bài viết/tài liệu mới đã chễm chệ xuất hiện trên website.

---
🍾 **Tất cả đã sẵn sàng.** Chào mừng bạn gia nhập hệ thống Agentic AI. Hãy quay lại [Trang chủ (Onboarding)](index.md) để đọc cách dùng các Team nhé!
