import tkinter as tk
import random

# 创建主窗口
root = tk.Tk()
root.geometry("600x400")
root.title("白兔堂岛屿生活")

# 初始金额
balance = 1000

# 岛屿及其价格
islands_price = {
    '亚速尔群岛 C': 10,
    '因纽维克岛 G,F': 20,
    '卡亚俄岛 D, bB': 100,
    '鳕鱼角岛 A, Es': 80,
    '圣巴巴拉岛 E, As': 100,
    '迪克森岛 B, Des': 50,
    '纳尔维克岛 Fis, Ges': 30,
    '诺姆岛 Cis, Ces': 80,
    '珀斯岛  Gis, Fes': 100,
    '瓦尔帕莱索岛 Dis, Hesses': 40,
    '费尔维尔岛 Ais, Eses': 50,
    '蒙得维的亚岛 Eis, Ases': 60,
    '勒韦克岛 His, Deses': 70,
    '旺加努依岛 Fises, Geses': 100,
    '欧比岛 D, Ceses': 20,
    '时空岛 A, Fesses': 70
}

# 抽取岛屿
def draw_island():
    global balance
    island = random.choice(list(islands_price.keys()))
    price = islands_price[island]
    balance += price
    balance_label.config(text=f"我的金额: ${balance}")
    island_label.config(text=f"抽取的岛屿: {island}")



# 创建金额标签
balance_label = tk.Label(root, text=f"我的金额: ${balance}", font=('Helvetica', 16))
balance_label.pack()

# 创建抽取岛屿按钮
draw_button = tk.Button(root, text="抽取岛屿", command=draw_island, font=('Helvetica', 16))
draw_button.pack()

# 创建岛屿标签
island_label = tk.Label(root, text="尚未抽取任何岛屿", font=('Helvetica', 16))
island_label.pack()

from tkinter import ttk

# 定义一个函数，用于在次窗口中显示文本
def show_info():

    # 创建一个次窗口
    new_window = tk.Toplevel(root)
    new_window.title("岛屿信息")
    new_window.geometry("200x300")

    # 定义一个字典，用于存储岛屿和对应的数字
    islands_info = {
    '亚速尔群岛 C': 10,
    '因纽维克岛 G,F': 20,
    '卡亚俄岛 D, bB': 100,
    '鳕鱼角岛 A, Es': 80,
    '圣巴巴拉岛 E, As': 100,
    '迪克森岛 B, Des': 50,
    '纳尔维克岛 Fis, Ges': 30,
    '诺姆岛 Cis, Ces': 80,
    '珀斯岛  Gis, Fes': 100,
    '瓦尔帕莱索岛 Dis, Hesses': 40,
    '费尔维尔岛 Ais, Eses': 50,
    '蒙得维的亚岛 Eis, Ases': 60,
    '勒韦克岛 His, Deses': 70,
    '旺加努依岛 Fises, Geses': 100,
    '欧比岛 D, Ceses': 20,
    '时空岛 A, Fesses': 70
    }

    # 创建一个列表框，用于显示岛屿信息
    listbox = tk.Listbox(new_window)
    listbox.pack(fill="both", expand=True)

    # 遍历字典，将岛屿信息添加到列表框中
    for island, info in islands_info.items():
        listbox.insert(tk.END, f"{island}: {info}")


# 在主窗口中添加一个按钮，用于打开次窗口
button = ttk.Button(root, text="显示岛屿信息", command=show_info)
button.pack(pady=20)

# 创建一个标签用于显示公司名称
company_label = tk.Label(root, text="©2024-2026 青岛耶胡迪梅纽因音乐学校", font=("微软雅黑", 12))
company_label.pack(side="bottom", anchor="sw")  # 将标签放置在窗口底部

# 运行主循环
root.mainloop()


