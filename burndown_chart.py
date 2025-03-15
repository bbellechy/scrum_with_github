import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 🔹 ตั้งค่าข้อมูล GitHub
GITHUB_TOKEN = "your_github_token"  # 🔺 เปลี่ยนเป็น Token ของคุณ
REPO_OWNER = "bbellechy"
REPO_NAME = "projects"

# 🔹 ดึงข้อมูล Issue จาก GitHub API
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=all&per_page=100"
response = requests.get(url, headers=headers)

# 🔹 ตรวจสอบว่า API ตอบกลับสำเร็จหรือไม่
if response.status_code != 200:
    print(f"❌ Error {response.status_code}: {response.text}")
    exit(1)

try:
    issues = response.json()  # แปลงเป็น JSON
    if not isinstance(issues, list):  # ตรวจสอบว่าเป็น List หรือไม่
        print(f"❌ Unexpected response format: {issues}")
        exit(1)
except Exception as e:
    print(f"❌ JSON decode error: {e}")
    exit(1)

# 🔹 กำหนดช่วง 7 วันล่าสุด
end_date = datetime.today()
start_date = end_date - timedelta(days=6)  # นับย้อนหลัง 6 วัน + 1 วันปัจจุบัน
date_list = [(start_date + timedelta(days=i)).date() for i in range(7)]

# 🔹 นับจำนวน Issue ที่ยังเปิดอยู่ในแต่ละวัน
remaining_tasks = []
for current_date in date_list:
    open_issues = sum(1 for issue in issues if isinstance(issue, dict) and
                      issue.get("created_at") and
                      datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ").date() <= current_date and
                      (not issue.get("closed_at") or datetime.strptime(issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ").date() > current_date))
    
    remaining_tasks.append(open_issues)
    print(f"{current_date}: {open_issues} open issues")  # Debugging

# 🔹 สร้าง Burndown Chart
plt.figure(figsize=(10, 5))
plt.plot(date_list, remaining_tasks, marker="o", linestyle="-", color="b", label="Remaining Tasks")
plt.xlabel("Date")
plt.ylabel("Number of Open Issues")
plt.title("Sprint Burndown Chart")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# 🔹 บันทึกกราฟเป็นไฟล์
plt.savefig("burndown_chart.png")
plt.show()
