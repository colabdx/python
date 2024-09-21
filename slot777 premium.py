import random
import tkinter as tk

# 初始化窗口
root = tk.Tk()
root.geometry("800x500")
root.title("slot777")
root.configure(background='#FF0000')

# 初始化金额
balance = 500

# 更新金额的函数
def update_balance(additional_amount=0):
    global balance
    balance += additional_amount
    balance_label.config(text=f"当前金额: ${balance}")

# 抽取元素并检查是否都是"7"
def draw_and_check():
    symbols = ["7", "bar", "葡萄", "铃铛", "樱桃", "jackpot", "any", "one", "two"]
    draw = [random.choice(symbols) for _ in range(3)]
    result_label.config(text=f"抽取结果: {' '.join(draw)}")
    if all(symbol == "7" for symbol in draw):
        update_balance(1000)
    # 检查是否抽中了葡萄
    if '葡萄' in draw:
        update_balance(1000)

# 创建按钮
draw_button = tk.Button(root, text="抽取",  font=('微软雅黑', 32) ,bg='yellow', command=draw_and_check)
draw_button.pack()

# 创建显示金额的标签
balance_label = tk.Label(root, text=f"当前金额: ${balance}", font=('微软雅黑', 32))
balance_label.pack()

# 创建显示结果的标签
result_label = tk.Label(root, text="抽取结果:", font=('微软雅黑', 32))
result_label.pack()

# 创建一个标签用于显示公司名称
company_label = tk.Label(root, text="©2024-2025 山东美祥印数码科技有限公司", font=("微软雅黑", 18))
company_label.pack(side="bottom", anchor="sw")  # 将标签放置在窗口底部

# 运行主循环
root.mainloop()
