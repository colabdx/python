import tkinter as tk
from tkinter import messagebox

# 定义岛屿列表
islands = [
    '亚速尔群岛 C',
    '因纽维克岛 G,F',
    '卡亚俄岛 D, bB',
    '鳕鱼角岛 A, Es',
    '圣巴巴拉岛 E, As',
    '迪克森岛 B, Des',
    '纳尔维克岛 Fis, Fes',
    '诺姆岛 Cis, Ces',
    '珀斯岛 Gis, Fes',
    '瓦尔帕莱索岛 Dis, Hesses',
    '费尔维尔岛 Ais, Eses',
    '蒙得维的亚岛 Eis, Ases',
    '勒韦克岛 His, Deses',
    '旺加努依岛 Fises, Geses',
    '欧比岛 D, Ceses',
    '时空岛 A, Fesses'
]

# 存储岛屿的价格
islands_prices = {island: 0 for island in islands}

# 验证价格输入的函数
def validate_price(new_value):
    try:
        price = float(new_value)
        if 0 <= price <= 100:
            return True
        else:
            return False
    except ValueError:
        return False

# 创建主窗口
root = tk.Tk()
root.title("岛屿价格计算器")

# 注册验证函数
validate_command = (root.register(validate_price), '%P')

# 为每个岛屿创建一个输入框和标签
for island in islands:
    label = tk.Label(root, text=f"{island} 的价格:")
    label.pack()
    entry = tk.Entry(root, validate='key', validatecommand=validate_command)
    entry.pack()
    entry.insert(0, str(islands_prices[island]))  # 预设价格为0

# 启动GUI事件循环
root.mainloop()
