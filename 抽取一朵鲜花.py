import tkinter as tk
import random

# 创建主窗口
root = tk.Tk()
root.title("随机抽取花名")
root.geometry("600x400")

# 花名列表
flowers = [
    '梨花', '杏花', '樱花', '梅花', '荷花',
    '睡莲', '牡丹', '芍药', '月季花', '蔷薇',
    '玫瑰花', '雏菊', '水仙', '杜鹃'
]

# 随机抽取花名并更新标签
def get_random_flower():
    random_flower = random.choice(flowers)
    flower_label.config(text=random_flower)
    show_flower_in_new_window(random_flower)

# 创建按钮
flower_button = tk.Button(root, text="抽取花名", command=get_random_flower)
flower_button.pack(pady=20)

# 创建标签
flower_label = tk.Label(root, text="", font=("微软雅黑", 18))
flower_label.pack(pady=20)

# 显示次窗口中的花名
def show_flower_in_new_window(flower_name):
    new_window = tk.Toplevel(root)
    new_window.title("抽取的花名")
    new_window.geometry("300x200")
    flower_name_label = tk.Label(new_window, text=flower_name, font=("微软雅黑", 14))
    flower_name_label.pack(pady=20)

# 运行主循环
root.mainloop()