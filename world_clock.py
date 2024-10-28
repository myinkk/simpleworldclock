import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
from PIL import Image, ImageTk

# ฟังก์ชันสำหรับอัปเดตเวลา
def update_time():
    timezone = timezone_var.get()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    time_label.config(text=current_time)

# ฟังก์ชันที่ถูกเรียกเมื่อกดปุ่ม Refresh
def refresh_time():
    update_time()  # เรียกใช้ฟังก์ชันอัปเดตเวลา
    root.after(1000, refresh_time)  # ตั้งเวลาให้ทำงานทุกๆ 1 วินาที

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("World Clock")
root.geometry("600x400")  # ขนาดหน้าต่าง

# เพิ่มภาพพื้นหลัง
bg_image = Image.open("images/public/download.jpg")  # ใช้เส้นทางที่ถูกต้อง
bg_image = bg_image.resize((1600, 1200), Image.LANCZOS)  # ปรับขนาดภาพให้เข้ากับหน้าต่าง
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # ทำให้ภาพเติมเต็มหน้าต่าง

# ตัวแปรสำหรับเก็บ timezone ที่เลือก
timezone_var = tk.StringVar(value='Asia/Bangkok')

# สร้าง dropdown สำหรับเลือก timezone
timezone_label = ttk.Label(root, text="Select Timezone:", font=("Helvetica", 16, 'bold'), foreground="#ffffff", background="black")
timezone_label.pack(pady=10)

timezones = pytz.all_timezones  # รายชื่อเขตเวลาทั้งหมด
timezone_dropdown = ttk.Combobox(root, textvariable=timezone_var, values=timezones, width=60)
timezone_dropdown.pack(pady=10)

# สร้างกรอบสำหรับแสดงเวลา
time_frame = tk.Frame(root, bg="black")  # กรอบสีดำ
time_frame.pack(pady=20, padx=10)  # เพิ่มระยะห่างรอบกรอบ

# สร้าง label สำหรับแสดงเวลาในกรอบ
time_label = ttk.Label(time_frame, font=('Helvetica', 42, 'bold'), background="black", foreground="#ffffff")  # ฟอนต์ขาวบนพื้นหลังดำ
time_label.pack()

# สร้างปุ่มเพื่อรีเฟรชเวลา
refresh_button = ttk.Button(root, text="Refresh Time", command=refresh_time)
refresh_button.pack(pady=10)

# สร้างข้อความอธิบาย
description_label = tk.Label(root, text="Choose a timezone to see the current time!", font=("Helvetica", 12), background="black", foreground="#ffffff")
description_label.pack(pady=10)

# เรียกใช้งานฟังก์ชัน update_time
update_time()

# เริ่มต้น GUI loop
root.mainloop()
