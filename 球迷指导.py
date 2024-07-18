import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("山东泰山队球迷加油指导")

# 设置窗口大小
root.geometry("400x200")

# 创建一个标签
label = ttk.Label(root, text="山东泰山队球迷加油指导", font=('bold', 16))
label.pack(pady=10)

# 创建一个单选按钮框架
radio_frame = ttk.Frame(root)
radio_frame.pack()

# 创建三个单选按钮
radio_buttons = []
for text in ["音乐生", "体育生", "美术生"]:
    radio = ttk.Radiobutton(radio_frame, text=text, variable=tk.StringVar(), value=text)
    radio.pack(side=tk.LEFT, padx=(5, 10), pady=5)
    radio_buttons.append(radio)

# 创建一个按钮，点击时会弹出欢迎窗口
def greet_user():
    new_window = tk.Toplevel(root)
    new_window.title("欢迎")
    greeting_label = ttk.Label(new_window, text="山东泰山队欢迎你！", font=('bold', 16))
    greeting_label.pack(pady=20)

    # 防止用户关闭欢迎窗口后还能继续点击主窗口的按钮
    root.grab_release()

button = ttk.Button(root, text="加油", command=greet_user)
button.pack(pady=10)

# 启动事件循环
root.mainloop()