import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("我要漂发")

# 设置窗口大小
root.geometry('400x200')

# 定义一个函数来创建新的窗口并显示“同意”
def show_agreement_window():
    agreement_window = tk.Toplevel(root)
    agreement_window.title("同意")
    agreement_window.geometry('200x100')
    tk.Label(agreement_window, text="同意").pack()

# 创建复选框
check_adapt_to_scalp = tk.IntVar()
check_redden = tk.IntVar()
check_克服疼痛 = tk.IntVar()
check_first_time = tk.IntVar()

tk.Checkbutton(root, text="适应头皮", variable=check_adapt_to_scalp).pack()
tk.Checkbutton(root, text="实现红化", variable=check_redden).pack()
tk.Checkbutton(root, text="克服疼痛", variable=check_克服疼痛).pack()
tk.Checkbutton(root, text="承认是第一次做", variable=check_first_time).pack()

# 创建“请给我漂发”按钮，点击时会调用show_agreement_window函数
submit_button = tk.Button(root, text="请给我漂发", command=show_agreement_window)
submit_button.pack(pady=20)

# 运行主循环
root.mainloop()