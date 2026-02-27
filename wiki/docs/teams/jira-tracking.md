---
hide:
  - toc
---
# ⏰ Đội Cập Nhật Tiến Độ (Jira Tracking Team)

## 🎯 Mục Tiêu
Hỗ trợ Product Owner và Scrum Master tự động hóa quy trình theo dõi tiến độ công việc. Đội sử dụng mã kịch bản Python kết nối Jira API, trích xuất dữ liệu Tickets và tổng hợp báo cáo tình trạng quá hạn/tắc nghẽn trong Sprint.

## 👥 Cơ Chế Hoạt Động
Hệ thống vận hành thông qua script ngầm `jira_reporter.py` với 4 giai đoạn xử lý:

```text
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Phase 1   │   │   Phase 2   │   │   Phase 3   │   │   Phase 4   │
│  Get Data   │──▶│   Scraper   │──▶│   Analyst   │──▶│  Reporter   │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
   API Jira        Tách JSON thô    Lọc trễ/Blockers   Gửi Telegram
```

1. **Scraper:** Tải dữ liệu cấu trúc (JSON) của danh sách Tickets trong Backlog qua Jira API.
2. **Analyst:** Sàng lọc dữ liệu, phân tách task hoàn thành hoặc bị loại bỏ. Xác định khoanh vùng các trường hợp dự kiến quá hạn (Overdue) và điểm tắc nghẽn (Blockers).
3. **Reporter:** Tổng hợp kết quả định dạng báo cáo Markdown và đẩy trực tiếp lên kênh công ty (Telegram) bằng tự động hóa.

## 💡 Hướng Dẫn Kích Hoạt (Ad-hoc Prompting)
Hệ thống được thiết lập chạy tự động (cronjob) và gửi báo cáo về Telegram lúc 8:00 sáng mỗi ngày. Ban quản trị không cần điều hướng trực tiếp.

Để truy xuất báo cáo Blockers tức thời, điều động lệnh sau:
> *"Kích hoạt nhánh `jira-tracking-team` báo cáo tình hình. Chạy script `jira_reporter.py` trong thư mục `sample_team` để rà soát Backlog Jira mới nhất và tổng hợp trạng thái luồng tiến độ ngay tại đây."*
