import tkinter as tk
import random

# 岛屿列表
islands = [
    '亚速尔群岛 C',
    '因纽维克岛 G,F',
    '卡亚俄岛 D, bB',
    '鳕鱼角岛 A, Es',
    '圣巴巴拉岛 E, As',
    '迪克森岛 B, Des',
    '纳尔维克岛 Fis, Fes',
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

# 初始化岛屿价格
island_prices = {island: random.randint(0, 100) for island in islands}

# 更新岛屿价格的函数
def update_prices():
    for island in islands:
        island_prices[island] = random.randint(0, 100)
    # 更新显示的价格
    for label in labels:
        label.config(text=f'{label.cget("text").split(": ")[0]}: {island_prices[label.cget("text").split(": ")[0]]}')

# 创建窗口
root = tk.Tk()
root.title('岛屿价格更新器')

# 创建并放置岛屿价格标签
labels = []
for island in islands:
    label = tk.Label(root, text=f'{island}: {island_prices[island]}')
    label.pack()
    labels.append(label)

# 创建并放置更新按钮
update_button = tk.Button(root, text='更新价格', command=update_prices)
update_button.pack()

# 运行事件循环
root.mainloop()