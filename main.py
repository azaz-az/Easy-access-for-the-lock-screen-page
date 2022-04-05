import tkinter as tk
import tkinter
import tkinter.messagebox
import os

os.system('title 困难使用')
window = tk.Tk()
window.title('困难使用')
window.geometry("800x480")

def cmd():		
    os.system('start cmd')
def tsk():		
    os.system('start taskmgr')
def vscode():		
    os.system('start regedit')
def fangdajing():		
    os.system('start C:\WINDOWS\system32\Magnify.exe')

line = tk.Label(window, text=' ')
line.pack()

tk.Button(window,width=30,height=2,text='命令提示符',command=cmd).pack()

tk.Button(window,width=30,height=2,text='任务管理器',command=tsk).pack()

tk.Button(window,width=30,height=2,text='注册表',command=vscode).pack()

tk.Button(window,width=30,height=2,text='放大镜',command=fangdajing).pack()

window.mainloop()