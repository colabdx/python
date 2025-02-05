import tkinter as tk
from tkinter import messagebox

# 完整的岛屿列表
islands = [
    '亚速尔群岛 C', '因纽维克岛 G,F', '卡亚俄岛 D, bB', '鳕鱼角岛 A, Es', '圣巴巴拉岛 E, As', 
    '迪克森岛 B, Des', '纳尔维克岛 Fis, Ges', '诺姆岛 Cis, Ces', '珀斯岛 Gis, Fes', '瓦尔帕莱索岛 Dis, Hesses', 
    '费尔维尔岛 Ais, Eses', '蒙得维的亚岛 Eis, Ases', '勒韦克岛 His, Deses', '旺加努依岛 Fises, Geses', 
    '欧比岛 D, Ceses', '时空岛 A, Fesses', '岛 E, Hesseses', '岛 B, Des', '岛 Fis, Ges', 
    '岛 Cis, Ces', '岛 Gis, Fes', '岛 Dis, Hesses', '岛 Ais, Eses', '岛 Eis, Ases', 'His, Deses', 'Fisis, Geses',
    'D, Ceses', 'A, fesses', 'E, Hesseses', 'B, Des', 'Fis, Ges', 'Cis, Ces'
]

# 创建窗口
root = tk.Tk()
root.title('岛屿价格管理器')

# 创建岛屿价格输入框和标签
price_entries = {}
for island in islands:
    frame = tk.Frame(root)
    frame.pack(fill='x')
    
    label = tk.Label(frame, text=island)
    label.pack(side='left')
    
    entry = tk.Entry(frame, width=5)
    entry.pack(side='left')
    entry.insert(0, 0)  # 默认初始价格为0
    
    price_entries[island] = entry

# 计算总价的函数
def calculate_total():
    total_price = 0
    for entry in price_entries.values():
        try:
            price = float(entry.get())
            if 0 <= price <= 100:
                total_price += price
            else:
                messagebox.showerror("错误", "价格必须在0到100之间")
                return
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return
    messagebox.showinfo("总价", f"所有岛屿的总价为: {total_price}")

# 创建并放置计算总价按钮
total_button = tk.Button(root, text='计算总价', command=calculate_total)
total_button.pack()

# 运行事件循环
root.mainloop()
