import threading
import tkinter as tk
import time

# 线程1：创建并显示窗口
def create_window():
    window = tk.Tk()
    window.title("线程1的窗口")
    window.geometry("300x200")
    label = tk.Label(window, text="这是由线程1创建的窗口", font=('Arial', 12))
    label.pack(pady=50)
    window.mainloop()

# 线程2：打印消息
def print_message():
    for _ in range(3):
        print("你好")
        time.sleep(1)  # 模拟耗时操作

# 创建并启动线程
thread1 = threading.Thread(target=create_window)
thread2 = threading.Thread(target=print_message)

thread1.start()
thread2.start()

# 等待线程结束（可选）
thread1.join()
thread2.join()
