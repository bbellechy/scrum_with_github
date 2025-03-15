import requests
import matplotlib.pyplot as plt
from datetime import datetime

# 🔹 ตั้งค่าข้อมูล GitHub
GITHUB_TOKEN = "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"  # 🔺 เปลี่ยนเป็น Token ของคุณ
REPO_OWNER = "bbellechy"
REPO_NAME = "projects"

# 🔹 ดึงข้อมูล Issue จาก GitHub API
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open"
response = requests.get(url, headers=headers)
issues = response.json()

# 🔹 คำนวณจำนวน Issue ที่เปิดอยู่ในวันนี้
today = datetime.today().date()
open_issues = sum(1 for issue in issues if issue.get("created_at"))

# 🔹 สร้างกราฟ (แสดงเฉพาะ 1 วัน)
plt.figure(figsize=(5, 5))
plt.bar([str(today)], [open_issues], color="b", label="Open Issues")

plt.xlabel("Date")
plt.ylabel("Number of Open Issues")
plt.title("Open Issues for Today")
plt.legend()
plt.grid(axis="y")

# 🔹 บันทึกกราฟเป็นไฟล์
plt.savefig("burndown_chart.png")
plt.show()
