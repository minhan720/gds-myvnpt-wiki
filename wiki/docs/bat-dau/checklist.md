# ✅ Checklist Tuần Đầu (Getting Started)

Tài liệu này hướng dẫn các thành viên trong dự án cách tải (clone) toàn bộ môi trường làm việc này về máy cá nhân và thiết lập trợ lý **Antigravity** bằng những quy trình (Team Frameworks) đã được cấu hình sẵn. Hãy hoàn thành các dấu tick dưới đây trong tuần đầu gia nhập nhé!

---

## 🛠️ 1. Yêu cầu chuẩn bị
- [ ] Cài đặt sẵn **[Git](https://git-scm.com/)** trên máy tính.
- [ ] Có tài khoản **GitHub**. (Nếu kho lưu trữ này đang ở chế độ Private, hãy gửi Username GitHub của bạn cho Admin để được cấp quyền).
- [ ] Cài đặt phần mềm/IDE lập trình có tích hợp trợ lý **Antigravity AI**.

---

## 📥 2. Bước 1: Tải Workspace về máy tính (Clone)
Thay vì phải tự tạo từng thư mục file, bạn chỉ cần tải toàn bộ "bộ não" của dự án này về máy. Đánh dấu tick khi bạn đã làm xong:

- [ ] Mở Terminal (Mac/Linux) hoặc Command Prompt / Git Bash (Windows).
- [ ] Chạy lệnh tải mã nguồn từ kho lưu trữ GitHub:
  ```bash
  git clone https://github.com/minhan720/gds-myvnpt-wiki.git
  ```
- [ ] Di chuyển vào thư mục dự án vừa tải về:
  ```bash
  cd gds-myvnpt-wiki
  ```

---

## 🤖 3. Bước 2: Kích hoạt Antigravity
Điểm đặc biệt của Workspace này là toàn bộ các **"Sổ tay nhập vai"** (Nằm ở `sample_team/`) và **Bộ não kỹ năng** (Nằm ở `.agents/skills/SKILL.md`) đều đã được thiết lập sẵn. 

- [ ] **Mở dự án:** Khởi động IDE của bạn -> Chọn chức năng **Open Folder** -> Mở cái thư mục `gds-myvnpt-wiki` bạn vừa clone ở bước trên.
- [ ] **Sử dụng ngay:** Bật cửa sổ Chat của Antigravity lên. Hệ thống sẽ tự động rà quét và "hấp thụ" toàn bộ thư mục `.agents`.
- [ ] 💡 **Test AI:** Nhắn câu này vào khung Chat để kiểm tra xem nó đã nhận diện hệ thống chưa:
  > *"Hãy kiểm tra xem trong workspace này có các team nào ở thư mục sample_team, liệt kê chúng ra."*

---

## 💻 4. Bước 3: Phát triển Trang Web Wiki (Dành cho người viết Docs)
Mọi thay đổi mà đồng nghiệp tạo ra trong `knowledge base` đều sẽ được hiển thị trên web. Nếu bạn muốn chạy Web nội bộ (Local) trên máy mình:

- [ ] **Cài đặt thư viện:** Bật Terminal lên, chạy lệnh:
  ```bash
  cd wiki
  pip install -r requirements.txt
  ```
- [ ] **Cắm máy chủ (Local Server):** Tắt chạy lệnh:
  ```bash
  python3 -m mkdocs serve
  ```
- [ ] Trải nghiệm: Truy cập [http://127.0.0.1:8000](http://127.0.0.1:8000) trên trình duyệt.

---

## 🚀 5. Bước 4: Cập Nhật Tài Liệu Lên Vercel (Auto-Deploy)
Khi làm xong nhiệm vụ (VD: Phân tích UI, viết Specs), đây là cách bạn đẩy bài lên mạng:

- [ ] Nhờ AI viết nội dung mới hoặc tự viết `.md` vào đúng thư mục nhóm `knowledge base/`.
- [ ] Chờ Admin (Boss) vào tận nơi rà soát File gốc và phản hồi duyệt (Approved).
- [ ] Gõ duy nhất một câu lệnh Slash Command vào khung chat AI:
  > `/deploy-website`
- [ ] Tựa lưng uống nước 20 giây, F5 tải lại trang Vercel Public của Admin cấp là hoàn tất!

---

🍾 **Chúc mừng bạn đã check xong tuần đầu tiên.** Chào mừng bạn gia nhập dự án! Hãy quay lại [Nguyên lý làm việc](../getting-started/) để học cách điều phối các hệ thống Teams đồ sộ.
