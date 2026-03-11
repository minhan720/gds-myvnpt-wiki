# Mail Classification Rules (Bộ lọc nghiệp vụ Email)

Tài liệu này hướng dẫn `Mail Logic Analyst` cách phân loại email vào các nhánh công việc.

## BƯỚC 1: Phân loại Luồng Báo Cáo
Dựa vào tiêu đề (Subject) và nội dung (Body) để tách email thành 2 danh sách riêng:

### 1. Luồng: `PYC` (Phiếu Yêu Cầu)
- **Keywords:** Dự án mới, Phát triển tính năng, Yêu cầu thay đổi, CR, Xây dựng hệ thống.
- **Tính chất:** Công việc có kế hoạch, kéo dài nhiều ngày, thuộc dự án cụ thể.

### 2. Luồng: `Support` (Hỗ trợ/Lỗi)
- **Keywords:** Lỗi, Bug, Không truy cập được, Hỗ trợ xử lý, Khôi phục mật khẩu, Nhờ kiểm tra.
- **Tính chất:** Công việc phát sinh đột xuất, cần xử lý ngay hoặc trong ngày.

---

## BƯỚC 2: Gắn Nhãn Nghiệp Vụ
Phân nhóm để thống kê hiệu suất công việc trong file Excel:
1. **Nhóm dự án VNPT:** Các mail liên quan đến app MyVNPT.
2. **Nhóm Hệ thống:** Các mail về hạ tầng, server.
3. **Nhóm Khác:** Trao đổi chung không thuộc 2 nhóm trên.

---

## BƯỚC 3: Quy trình HITL (Duyệt)
1. Bot gửi bản nháp (Draft) báo cáo.
2. BOSS (Tôi) phản hồi `Approved`.
3. Bot chính thức gửi báo cáo vào các Group Telegram chuyên biệt.
