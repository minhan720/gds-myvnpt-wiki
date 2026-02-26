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

## Bước 4: Đăng tải Tài Liệu Mới (Cần Boss Duyệt)
Để đảm bảo chất lượng tài liệu Public, hệ thống áp dụng quy trình kiểm duyệt (Pull Request). Bạn không được đẩy thẳng nội dung lên trang chính (Branch Main) mà phải tạo "Bản nháp" để Nhóm trưởng (Boss) đánh giá và duyệt trước.

**Quy trình Cập nhật:**
1. Cập nhật mã nguồn mới nhất từ kho:
```bash
git checkout main
git pull
```
2. Tạo một "Nhánh làm việc" mới của riêng bạn (Ví dụ đặt tên là `update-tinh-nang-a`):
```bash
git checkout -b update-tinh-nang-a
```
3. Hãy nhờ AI viết nội dung mới (hoặc tự viết tay) tạo các file `.md` vào đúng thư mục `knowledge base/` và hoàn thiện.
4. Lần lượt gõ các lệnh sau để lưu và đẩy (Push) nhánh của bạn lên GitHub:
```bash
git add .
git commit -m "docs: Cập nhật tài liệu tính năng A"
git push -u origin update-tinh-nang-a
```
5. **Gửi yêu cầu duyệt (Pull Request):** Truy cập vào Link GitHub của dự án, bạn sẽ thấy thông báo tạo nhánh. Bấm nút màu xanh **"Compare & pull request"**. Ở bước này, hệ thống Vercel sẽ tự động render cho bạn một đường link "Web dùng thử" (Preview Website) để bạn tự xem trước thành quả. 
6. Khi thấy Web dùng thử đã xuất hiện đúng như ý mình, hãy Assign (Giao duyệt) Pull Request đó cho Admin/Boss. Ngay sau khi Boss xem đúng chuẩn và bấm **Merge (Gộp)**, bài viết của bạn sẽ lập tức chính thức lên sóng trên trang Public!

---
🍾 **Tất cả đã sẵn sàng.** Chào mừng bạn gia nhập hệ thống Agentic AI. Hãy quay lại [Trang chủ (Onboarding)](index.md) để đọc cách dùng các Team nhé!
