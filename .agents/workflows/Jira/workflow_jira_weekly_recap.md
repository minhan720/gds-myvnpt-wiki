---
description: Pipeline tổng hợp và tạo báo cáo Recap các Task Jira (Tự động kéo, phân loại và tóm tắt).
---

# Thực thi Tổng hợp Báo cáo (Weekly/Daily Recap) cho Jira

**Mục tiêu:** Workflow này kết hợp hai AI Agents để tự động hóa hoàn toàn quy trình truy xuất và phân loại tiến độ công việc trên hệ thống Jira.

1. **Khởi Trình:** User gọi lệnh phân tích tiến độ, gọi `/Jira/workflow_jira_weekly_recap.md`.

1. **Khởi Trình:** User gọi lệnh phân tích tiến độ, gọi `/Jira/workflow_jira_weekly_recap`.

// turbo-all
2. **Thực thi Script Tự động:** (Do **Jira Operations Bot** đảm nhiệm)
    - Bot sẽ không cần tự phân tích thủ công nữa mà thực thi trực tiếp File Script Python lõi đã được lập trình sẵn.
    - Script này tự động trọn gói: Kéo API Jira -> Phân loại Rule (PYC/Support) -> Sync Google Sheets (PhatSinh) -> Push auto-split Telegram.
    
    Chạy lệnh bash sau:
    ```bash
    python3 .agents/scripts/jira/jira_reporter.py
    ```
