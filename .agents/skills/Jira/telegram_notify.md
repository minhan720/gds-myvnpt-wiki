---
name: telegram_notify
description: Kỹ năng điều phối Bot Operations gửi tin nhắn văn bản thuần túy (Plain text) hoặc HTML lên Channel Telegram của Team.
---

# Telegram Notification Skill

Kỹ năng gửi báo cáo, thông báo, hoặc bản Draft ý tưởng lên nhóm Telegram để cho Boss và các nhân sự nội bộ cùng nắm tiến độ theo thời gian thực.

## Cách thức hoạt động nội suy:
- Bot sẽ nhận đầu vào là một chuỗi văn bản (String) báo cáo được sinh ra từ quá trình phân tích.
- Nếu chuỗi quá dài (vượt 4000 ký tự), Bot tự động cắt nhỏ và bắn làm nhiều tin theo thứ tự.
- **Quy tắc bảo mật:** Không in Token bot ra màn hình log, chỉ dùng để gọi Request nội bộ.

## Ứng dụng:
- Gửi Daily/Weekly Report Jira.
- Bắn cảnh báo (Warning) các task sắp trễ hạn cho nhóm biết.
- Bắn Draft Comment để nhóm nội bộ cùng thảo luận trước khi Boss duyệt (HITL) bắn lệnh lên hệ thống Jira thực tế.
