import requests
import json
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

JIRA_URL = "https://cntt.vnpt.vn"
JIRA_TOKEN = "NTM1MzI4MzUxMzI5OmZW0fEZHynZe41tPaaVTtyXwDN0"

JQL = 'assignee in ("An Vũ Nhật Minh", "Hồ Phạm Quỳnh Mai", "Nguyễn Việt Hà") AND status NOT IN ("Closed", "Done", "Resolved", "Đóng yêu cầu", "Đã xử lý") ORDER BY duedate DESC'

def fetch_data():
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
        response = requests.get(url, headers=headers, params=params, verify=False)
        if response.status_code != 200:
            print(json.dumps({"error": response.text}))
            return
            
        data = response.json().get('issues', [])
        print(json.dumps(data))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    fetch_data()
