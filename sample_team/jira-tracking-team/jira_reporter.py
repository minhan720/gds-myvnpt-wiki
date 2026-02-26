import requests
import json
import datetime
import urllib3
import html

# Bỏ qua cảnh báo SSL nếu mạng nội bộ chạy chứng chỉ tự cấp (Self-signed)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ==========================================
# CẤU HÌNH THÔNG SỐ JIRA & TELEGRAM
# ==========================================
JIRA_URL = "https://cntt.vnpt.vn"
JIRA_TOKEN = "NTM1MzI4MzUxMzI5OmZW0fEZHynZe41tPaaVTtyXwDN0"

# Boss sẽ điền 2 thông số này sau khi tạo Bot (Xem hướng dẫn trên màn hình Chat)
TELEGRAM_BOT_TOKEN = "8757329276:AAG5zL8re4xprBhFPuJQ-yr0DS6FxUesWK4"
TELEGRAM_CHAT_ID = "-5120994141"

# Lệnh JQL kéo tất cả các Task chưa Đóng/Hủy. 
# (Nếu Boss muốn giới hạn project nào, có thể thay JQL = 'project = TênProject AND ...')
JQL = 'resolution is EMPTY ORDER BY created DESC'

# ==========================================
# 🕵️ SCRAPER: LẤY DỮ LIỆU JIRA
# ==========================================
def get_jira_tasks():
    print("⏳ Đang kết nối mạng nội bộ lấy dữ liệu Jira...")
    url = f"{JIRA_URL}/rest/api/2/search"
    headers = {
        "Authorization": f"Bearer {JIRA_TOKEN}",
        "Content-Type": "application/json"
    }
    
    params = {
        "jql": JQL,
        "maxResults": 50, # Kéo tối đa 50 task mới nhất
        "fields": "summary,status,assignee,duedate" 
    }
    
    try:
        # verify=False cực kỳ cần thiết cho mạng On-premise không có SSL chuẩn Quốc tế
        response = requests.get(url, headers=headers, params=params, verify=False)
        if response.status_code != 200:
            print(f"❌ Lỗi {response.status_code} từ Jira. Chi tiết nguyên nhân:")
            print(response.text)
            return []
            
        data = response.json().get('issues', [])
        print(f"✅ Đã kéo thành công {len(data)} công việc!")
        return data
    except Exception as e:
        print(f"❌ Lỗi hệ thống: {e}")
        return []

# ==========================================
# 🧠 ANALYST: XỬ LÝ & ĐÓNG GÓI BÁO CÁO
# ==========================================
def format_message(issues):
    if not issues:
        return ["🎉 Tuyệt vời! Hiện tại hệ thống không trích xuất được task nào đang tồn đọng (hoặc tất cả đã đóng)."]
    
    today_str = datetime.datetime.now().strftime("%d/%m/%Y")
    header = f"📊 <b>BÁO CÁO TOÀN CẢNH JIRA GDS-MY VNPT ({today_str})</b>\n\n"
    
    chunks = []
    current_chunk = header
    
    for i, issue in enumerate(issues, 1):
        key = issue.get('key')
        fields = issue.get('fields', {})
        summary = html.escape(fields.get('summary', 'Không có tiêu đề'))
        status = html.escape(fields.get('status', {}).get('name', 'N/A'))
        
        assignee = fields.get('assignee')
        assignee_name = html.escape(assignee.get('displayName') if assignee else '⚠️ Chưa gán (Unassigned)')
        
        duedate = fields.get('duedate')
        duedate_str = duedate if duedate else 'Không có hạn'
        
        # Link truy cập thẳng task
        link = f"{JIRA_URL}/browse/{key}"
        
        task_str = f"🔹 {i}. <a href='{link}'>[{key}]</a>: {summary}\n"
        task_str += f"   👤 Phụ trách: {assignee_name}\n"
        task_str += f"   📌 Status: {status} | ⏰ Hạn: {duedate_str}\n\n"
        
        # Nếu cộng thêm task này làm chunk vượt quá giới hạn 3800 ký tự (telegram limit là 4096)
        if len(current_chunk) + len(task_str) > 3800:
            chunks.append(current_chunk)
            current_chunk = task_str
        else:
            current_chunk += task_str
            
    current_chunk += "💡 <i>Thư ký Jira Tracking - Chúc Boss ngày làm việc hiệu quả!</i>"
    chunks.append(current_chunk)
    
    return chunks

# ==========================================
# 📢 REPORTER: BẮN TIN NHẮN LÊN TELEGRAM
# ==========================================
def send_telegram_message(message):
    print("⏳ Đang chuẩn bị bắn tin báo cáo qua Telegram...")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML", 
        "disable_web_page_preview": True # Tắt cái ảnh thu nhỏ link Jira chiếm diện tích
    }
    try:
        req = requests.post(url, json=payload)
        req.raise_for_status()
        print("✅ Đã gửi báo cáo Telegram cho Boss thành công!")
    except Exception as e:
        print(f"❌ Lỗi gửi Telegram: {e}")
        print("Chi tiết lỗi:", req.text if 'req' in locals() else 'Không rõ')

if __name__ == "__main__":
    # Luồng chạy chính (Pipeline)
    tasks = get_jira_tasks()
    if tasks:
        msg_chunks = format_message(tasks)
        if TELEGRAM_BOT_TOKEN == "ĐIỀN_TOKEN_BOT_VÀO_ĐÂY":
            print("⚠️ CẢNH BÁO: Boss chưa điền thông tin Bot Telegram! Dưới đây là nội dung Báo cáo nháp:")
            print("=========================================")
            for msg in msg_chunks:
                print(msg)
            print("=========================================")
        else:
            for idx, msg in enumerate(msg_chunks):
                print(f"Bắn tin nhắn phần {idx+1}/{len(msg_chunks)}...")
                send_telegram_message(msg)
