import random
import tkinter as tk
from tkinter import messagebox
import webbrowser

class SlotGame:
    def __init__(self, master):
        self.master = master
        master.geometry("900x600")
        master.title("slot777")
        master.configure(background='#FF0000')
        
        self.balance = 500
        self.total_winnings = 0
        
        # 主界面组件
        self.draw_button = tk.Button(master, text="抽取", font=('微软雅黑', 32), bg='yellow', command=self.draw_and_check)
        self.draw_button.pack()
        
        self.balance_label = tk.Label(master, text=f"当前金额: ￥{self.balance}", font=('微软雅黑', 32))
        self.balance_label.pack()
        
        self.result_label = tk.Label(master, text="抽取结果:", font=('微软雅黑', 32))
        self.result_label.pack()
        
        # 结算按钮
        self.settle_button = tk.Button(master, text="结算", font=('微软雅黑', 32), bg='green', command=self.open_settle_window)
        self.settle_button.pack()
        
        # 公司信息
        company_info = [
            "©2025-2026 山东美祥印数码科技有限公司",
            "777是1000元",
            "1个葡萄是100元",
            "2个铃铛是200元"
        ]
        
        for info in company_info:
            tk.Label(master, text=info, font=("微软雅黑", 18 if info.startswith("©") else 32)).pack(side="bottom", anchor="sw")
    
    def update_balance(self, additional_amount=0):
        self.balance += additional_amount
        self.total_winnings += additional_amount
        self.balance_label.config(text=f"当前金额: ￥{self.balance}")
    
    def draw_and_check(self):
        symbols = ["7", "bar", "葡萄", "铃铛", "樱桃", "jackpot", "any", "one", "two"]
        draw = [random.choice(symbols) for _ in range(3)]
        self.result_label.config(text=f"抽取结果: {' '.join(draw)}")
        
        if all(symbol == "7" for symbol in draw):
            self.update_balance(1000)
        if '葡萄' in draw:
            self.update_balance(100)
        if draw.count("铃铛") == 2:
            self.update_balance(200)
    
    def open_settle_window(self):
        settle_window = tk.Toplevel(self.master)
        settle_window.title("结算窗口")
        settle_window.geometry("600x400")
        
        # 显示总金额
        tk.Label(settle_window, text=f"本次游戏总金额: ￥{self.total_winnings}", font=('微软雅黑', 24)).pack(pady=20)
        
        # 显示当前余额
        tk.Label(settle_window, text=f"当前余额: ￥{self.balance}", font=('微软雅黑', 24)).pack(pady=20)
        
        # 扫码支付按钮
        qr_button = tk.Button(settle_window, text="扫码结算", font=('微软雅黑', 24), 
                             command=lambda: webbrowser.open("https://cn-python.com/slot%E7%BB%93%E7%AE%97"))
        qr_button.pack(pady=40)
        
        # 确认结算按钮
        confirm_button = tk.Button(settle_window, text="确认结算", font=('微软雅黑', 24), 
                                 command=lambda: self.confirm_settlement(settle_window))
        confirm_button.pack()
    
    def confirm_settlement(self, window):
        messagebox.showinfo("结算成功", f"已成功结算 ￥{self.total_winnings}!")
        self.total_winnings = 0
        window.destroy()

root = tk.Tk()
game = SlotGame(root)
root.mainloop()
