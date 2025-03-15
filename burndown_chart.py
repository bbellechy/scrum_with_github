import pandas as pd
import matplotlib.pyplot as plt

# 🔹 โหลดข้อมูลจาก Excel
file_path = "burndown.xlsx"  # 🔺 เปลี่ยนเป็นชื่อไฟล์ของคุณ
df = pd.read_excel(file_path)

# 🔹 แปลงคอลัมน์วันที่ให้อยู่ในรูปแบบ datetime
df["Date"] = pd.to_datetime(df["Date"])

# 🔹 สร้างกราฟ Burndown Chart
plt.figure(figsize=(8, 5))
plt.plot(df["Date"], df["Remaining Issues"], marker="o", linestyle="-", color="b", label="Remaining Tasks")

# 🔹 ตั้งค่ากราฟ
plt.xlabel("Date")
plt.ylabel("Number of Issues Remaining")
plt.title("Sprint Burndown Chart")
plt.xticks(rotation=45)  # หมุนวันที่ให้เห็นชัดขึ้น
plt.legend()
plt.grid(True)

# 🔹 บันทึกเป็นรูปภาพ
plt.savefig("burndown_chart.png")
plt.show()
