import tkinter as tk

def perform_transaction():
    amount_str = amount_entry.get()
    try:
        amount = float(amount_str)
        if amount <= 0:
            result_label.config(text="金额必须大于0。")
        else:
            result_label.config(text=f"交易成功，金额为: {amount}", font=('微软雅黑', 22))
    except ValueError:
        result_label.config(text="请输入有效的金额。")

# 创建主窗口
root = tk.Tk()
root.title("金额交易程序")
root.dpi =96

# 创建输入框并设置默认值
amount_entry = tk.Entry(root, font=('微软雅黑', 22))
amount_entry.pack()
amount_entry.insert(0, "请输入金额")

# 创建显示结果的标签
result_label = tk.Label(root, text="")
result_label.pack()

# 创建确认交易的按钮
confirm_button = tk.Button(root, text="确认交易", command=perform_transaction, font=('微软雅黑', 22))
confirm_button.pack()

# 启动事件循环
root.mainloop()
