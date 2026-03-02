import requests
import json
import urllib3
import datetime
import html
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configs
JIRA_URL = "https://cntt.vnpt.vn"
JIRA_TOKEN = "NTM1MzI4MzUxMzI5OmZW0fEZHynZe41tPaaVTtyXwDN0"
TELEGRAM_BOT_TOKEN = "8757329276:AAG5zL8re4xprBhFPuJQ-yr0DS6FxUesWK4"
TELEGRAM_CHAT_ID = "-5120994141"

# Step 1: Kéo dữ liệu (Operations Bot)
def fetch_jira_tasks():
    print("⏳ [Operations Bot] Đang kéo dữ liệu từ Jira...")
    JQL = 'assignee in ("An Vũ Nhật Minh", "Hồ Phạm Quỳnh Mai", "Nguyễn Việt Hà") AND status NOT IN ("Closed", "Done", "Resolved", "Đóng yêu cầu", "Đã xử lý") ORDER BY duedate DESC'
    url = f"{JIRA_URL}/rest/api/2/search"
    headers = {
        "Authorization": f"Bearer {JIRA_TOKEN}",
        "Content-Type": "application/json"
    }
    params = {
        "jql": JQL,
        "maxResults": 50,
        "fields": "summary,status,assignee,duedate,created,issuetype,description"
    }
    try:
        res = requests.get(url, headers=headers, params=params, verify=False)
        return res.json().get('issues', [])
    except Exception as e:
        print(f"Lỗi fetch Jira: {e}")
        return []

# Step 2: Phân loại theo Group (Logic Analyst)
def classify_business(description, summary):
    text = (str(description) + " " + str(summary)).lower()
    
    # Keyword list
    mobile_kws = ["di động", "vinaphone", "vnp", "sim", "esim", "cước di động", "gói cước vnp", "4g", "5g", "mạng di động"]
    broadband_kws = ["cố định", "băng rộng", "fiber", "ftth", "internet", "wifi", "mytv", "cáp quang", "đường truyền cố định"]
    payment_kws = ["thanh toán", "vnpt money", "vnpt pay", "mobile money", "vnpay", "nạp thẻ", "payment", "cổng thanh toán", "đối soát"]
    
    for kw in mobile_kws:
        if kw in text: return "📱 Di động"
    
    for kw in broadband_kws:
        if kw in text: return "🌐 Băng rộng cố định"
        
    for kw in payment_kws:
        if kw in text: return "💳 Thanh toán"
        
    return "📦 Khác"

# Step 3: Khai thác template (Logic Analyst)
def build_report_for_type(tasks, type_name):
    # Tổng hợp metrics
    total = len(tasks)
    if total == 0: return None
    
    assignees_count = {}
    biz_count = {"📱 Di động": 0, "🌐 Băng rộng cố định": 0, "💳 Thanh toán": 0, "📦 Khác": 0}
    
    warnings = []
    news = []
    
    now = datetime.datetime.now()
    
    for issue in tasks:
        key = issue.get('key')
        fields = issue.get('fields', {})
        summary = html.escape(fields.get('summary', 'No summary'))
        
        assignee = fields.get('assignee')
        uname = assignee.get('displayName') if assignee else 'Unassigned'
        assignees_count[uname] = assignees_count.get(uname, 0) + 1
        
        biz = classify_business(fields.get('description'), summary)
        biz_count[biz] += 1
        
        # Deadlines < 7 ngày
        duedate_str = fields.get('duedate')
        if duedate_str:
            try:
                due_obj = datetime.datetime.strptime(duedate_str, "%Y-%m-%d")
                delta = (due_obj - now).days
                if delta < 7:
                    warnings.append(f"- `<a href='{JIRA_URL}/browse/{key}'>[{key}]</a>` {summary} - Phụ trách: {uname} - <i>Due: {delta if delta>=0 else 'Quá hạn'} ngày nữa</i>")
            except: pass
            
        # Mới nhận < 24h
        created_str = fields.get('created')
        if created_str:
            try:
                # 2025-06-18T08:54:24.000+0700
                created_obj = datetime.datetime.strptime(created_str[:19], "%Y-%m-%dT%H:%M:%S")
                if (now - created_obj).total_seconds() < 86400:
                    news.append(f"- `<a href='{JIRA_URL}/browse/{key}'>[{key}]</a>` {summary} - Phụ trách: {uname}")
            except: pass

    # Build msg
    msg = f"🚀 <b>BÁO CÁO CÔNG VIỆC {type_name.upper()}</b>\n\n"
    msg += f"Thân gửi Team, báo cáo tiến độ các hạng mục {type_name.upper()} hiện tại như sau:\n\n"
    msg += f"<b>1. 🗂 Trạng thái Tổng Quan (Đang thụ lý)</b>\n"
    msg += f"- Tổng số Task đang mở: {total}\n"
    msg += f"- Phân bổ theo Nhóm Nghiệp vụ:\n"
    for k, v in biz_count.items():
        if v > 0: msg += f"  - {k}: <b>{v}</b> tasks\n"
        
    msg += f"\n- Phân bổ theo Assignee:\n"
    for k, v in assignees_count.items():
        msg += f"  - {k}: <b>{v}</b> tasks\n"
        
    msg += f"\n<b>2. 🚨 Báo Động Đỏ (Gần Deadline < 7 ngày)</b>\n"
    if warnings:
        msg += "\n".join(warnings) + "\n"
    else:
        msg += "Trống / Mọi thứ an toàn\n"
        
    msg += f"\n<b>3. 🆕 Nhiệm Vụ Mới Nhận (< 24H)</b>\n"
    if news:
        msg += "\n".join(news) + "\n"
    else:
        msg += "Chưa có task mới phát sinh\n"
        
    msg += "\n<i>(Bot tự hào đồng hành cùng VNPT Tracking)</i>"
    return msg

# Step 4: Gửi Telegram (Operations Bot)
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    try:
        requests.post(url, json=payload).raise_for_status()
        print("✅ Đã gửi Telegram thành công!")
    except Exception as e:
        print(f"❌ Lỗi gửi Tele: {e}")

if __name__ == "__main__":
    tasks = fetch_jira_tasks()
    print(f"📦 Đã kéo về tổng cộng {len(tasks)} tasks.")
    
    # Phân nhóm PYC và Support
    pyc_tasks = []
    support_tasks = []
    
    for t in tasks:
        itype = t.get("fields", {}).get("issuetype", {}).get("name", "")
        if "CR" in itype or "PYC" in itype:
            pyc_tasks.append(t)
        elif "SR" in itype or "Support" in itype:
            support_tasks.append(t)
            
    print(f"🔍 Phân loại: {len(pyc_tasks)} PYC tasks, {len(support_tasks)} Support tasks.")
    
    # Xây dựng & gửi report
    pyc_report = build_report_for_type(pyc_tasks, "PYC")
    if pyc_report:
        print("\n=== DRAFT PYC ===")
        print(pyc_report)
        print("⏳ Đang gửi PYC lên Tele...")
        send_telegram(pyc_report)
        
    support_report = build_report_for_type(support_tasks, "Support")
    if support_report:
        print("\n=== DRAFT SUPPORT ===")
        print(support_report)
        print("⏳ Đang gửi Support lên Tele...")
        send_telegram(support_report)

