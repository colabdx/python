import tkinter as tk
from tkinter import messagebox
import random

# 创建主窗口
root = tk.Tk()
root.title("岛屿价格定义")

# 岛屿列表
islands = [
    '亚速尔群岛 C',
    '因纽维克岛 G,F',
    '卡亚俄岛 D, bB',
    '鳕鱼角岛 A, Es',
    '圣巴巴拉岛 E, As',
    '迪克森岛 B, Des',
    '纳尔维克岛 Fis, Ges',
    '诺姆岛 Cis, Ces',
    '珀斯岛  Gis, Fes',
    '瓦尔帕莱索岛 Dis, Hesses',
    '费尔维尔岛 Ais, Eses',
    '蒙得维的亚岛 Eis, Ases',
    '勒韦克岛 His, Deses',
    '旺加努依岛 Fises, Geses',
    '欧比岛 D, Ceses',
    '时空岛 A, Fesses'
]

# 存储输入框和价格的字典
entries = {}
prices = {}

# 创建输入框和标签
for i, island in enumerate(islands):
    label = tk.Label(root, text=island)
    label.grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[island] = entry

# 定义“试试手气”按钮的功能
def random_prices():
    for island in entries:
        price = random.randint(1, 100)
        entries[island].delete(0, tk.END)
        entries[island].insert(0, str(price))
    calculate_total()

# 定义计算总价格的功能
def calculate_total():
    total = 0
    for island in entries:
        try:
            price = int(entries[island].get())
            prices[island] = price
            total += price
        except ValueError:
            messagebox.showerror("错误", f"{island} 的价格输入无效")
            return
    total_label.config(text=f"总价格: {total}")

# 创建“试试手气”按钮
random_button = tk.Button(root, text="试试手气", command=random_prices)
random_button.grid(row=len(islands), column=0, columnspan=2, pady=10)

# 创建总价格标签
total_label = tk.Label(root, text="总价格: 0")
total_label.grid(row=len(islands)+1, column=0, columnspan=2, pady=10)

# 运行主循环
root.mainloop()
