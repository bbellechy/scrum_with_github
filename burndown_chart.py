import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 🔹 ตั้งค่าข้อมูล GitHub
GITHUB_TOKEN = "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"  # 🔺 เปลี่ยนเป็น Token ของคุณ
REPO_OWNER = "bbellechy"
REPO_NAME = "projects"

# 🔹 ดึงข้อมูล Issue จาก GitHub API
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=all"
response = requests.get(url, headers=headers)
issues = response.json()

# 🔹 คำนวณจำนวน Task ที่เหลืออยู่ในแต่ละวัน
start_date = datetime.today() - timedelta(days=7)  # Sprint เริ่ม 7 วันก่อน
end_date = datetime.today()
days = (end_date - start_date).days + 1

remaining_tasks = []
for day in range(days):
    date = start_date + timedelta(days=day)
    remaining = sum(1 for issue in issues if "closed_at" in issue and 
                    (issue["closed_at"] is None or datetime.strptime(issue["closed_at"], "%Y-%m-%dT%H:%M:%SZ") > date))
    remaining_tasks.append(remaining)

# 🔹 สร้าง Burndown Chart
plt.figure(figsize=(8, 5))
plt.plot(range(days), remaining_tasks, marker="o", linestyle="-", color="b", label="Remaining Tasks")
plt.xlabel("Days")
plt.ylabel("Number of Tasks Remaining")
plt.title("Sprint Burndown Chart")
plt.legend()
plt.grid(True)

# 🔹 บันทึกกราฟเป็นไฟล์
