import tkinter as tk
import random

# 初始化窗口
root = tk.Tk()
root.geometry("600x600")
root.title("猪柳——无序中的有序")

# 初始化金额
balance = 500

# 更新金额的函数
def update_balance(additional_amount=0):
    global balance
    balance += additional_amount
    balance_label.config(text=f"当前金额: {balance}")

# 抽取元素并检查是否都是"7"
def draw_and_check():
    symbols = ["7", "bar", "葡萄", "铃铛", "樱桃", "jackpot", "any", "one", "two"]
    draw = [random.choice(symbols) for _ in range(100)]
    result_label.config(text=f"抽取结果: {' '.join(draw)}")
    if all(symbol == "7" for symbol in draw):
        update_balance(1000)

# 创建按钮
draw_button = tk.Button(root, text="抽取", command=draw_and_check)
draw_button.pack()

# 创建显示金额的标签
balance_label = tk.Label(root, text=f"当前金额: {balance}")
balance_label.pack()

# 创建显示结果的标签
result_label = tk.Label(root, text="抽取结果:", wraplength=600, justify="left")
result_label.pack()

# 运行主循环
root.mainloop()
