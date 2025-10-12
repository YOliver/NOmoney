#
#   2025/09/25 @yinjianwen@gmail.com
#   模仿小丑牌项目 
#   开发控制台界面
#
import tkinter as tk
import os
import subprocess
import signal

pid = 0

def Click_Button_Test(event):
    os.system("python -B .\\test.py")
def Click_Button_OnOff(event):
    process = subprocess.Popen(['python', '-B', '.\\main.py'])
    pid = process.pid
root = tk.Tk()
root.title("小丑牌开发控制台")
root.geometry("600x400")
# python 测试
button_test = tk.Button(root, text="python测试", width=10, height=5, bg="yellow", fg="black",activebackground='#45a049')
button_test.grid(row=1,column=1, padx=10, pady=10, ipadx=5, ipady=5, sticky="nsew")  
button_test.bind("<Button-1>", Click_Button_Test)
# 游戏启动/关闭按钮
button_onoff = tk.Button(root, text="ON/OFF", width=10, height=5, bg="yellow", fg="black",activebackground='#45a049')
button_onoff.grid(row=1,column=2, padx=10, pady=10, ipadx=5, ipady=5, sticky="nsew")
button_onoff.bind("<Button-1>", Click_Button_OnOff)




root.mainloop()