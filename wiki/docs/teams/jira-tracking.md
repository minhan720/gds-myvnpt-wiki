# ⏰ Đội Thư Ký Cập Nhật Tiến Độ (Jira Tracking)

## 🎯 Sinh Trưởng Chạy Ngầm
Tự động hóa tuyệt đối nền tảng Quản trị thông tin. Con thoi ngoại giao thay mặt toàn dự án luồn sâu vào mạch dẫn nội bộ Jira (On-premise API), lùng sục rổ Thẻ Task/Ticket, xới lại Tiến Độ Sprint thành Bản Tin Gắn Sao vắn tắt.

## 👥 Cơ Chế Hoạt Động ("Tàng hình & Không Người Lái")
Khác toàn bộ các nhóm Agent trò chuyện đa chiều phía trên, Đội này là sự hiện thân "Mọt Sách" được neo trên 1 tập ngôn ngữ Python duy nhất (`jira_reporter.py`) pha trộn sức mạnh 3 luân xa:

1. **Scraper (Lính đặc công lấy trộm):** Dùng mã bài Access Token đào một đường ngầm chui thẳng qua lỗ hổng hệ thống Jira. Kéo bọc Data định dạng sền sệt nguyên sơ JSON.
2. **Analyst (Lính trinh sát phân hạng):** Soi chiếu mảng nhiễu, gọt tỉa các khối Ticket/Issue đã vứt đi hoặc ngâm (Done/Cancelled). Cán mỏng khối dữ liệu khổng lồ về nhóm Cần Lưu Ý.
3. **Reporter (Phát thanh viên):** Dọn bữa sáng sạch sẽ, vuốt lại khối Data chán chường đó qua dàn format HTML xịn xò/Markdown highlight cục bộ. Điểm mặt đặt tên Thẻ nào đang Nghẽn (Blockers) và Bắn trúng cmn phốc lên đường dải Telegram Group Cty.

## 💡 Mẫu Lệnh Gọi Bất Chợt (Ad-hoc Prompting)
Bình thường, Đội Lính Ngầm này sẽ chạy định kỳ trồi đầu lên gáy qua Đồng Hồ Cát của thiết bị (Cronjob - như kiểu 8h đập lệnh sáng T2 tự bay vào Telegram). Boss chẳng mất sức gọi.

Nhưng đương lúc dở bữa nửa buổi Boss muốn **Dè chừng ép cọc xem Tiến độ ngay Tức khắc**, hãy ban Thánh Chỉ này vào Chat Box:
> *"Lệnh kích ngay `jira-tracking-team`. Dùng thuật dồn nén code chay tập `jira_reporter.py` trong ổ `sample_team` và đập lật ngửa cái Output Tình trạng tiến độ hôi hổi mới cập nhật lên bảng cho trẫm nghía!"*
