import tkinter as tk

class ZodiacApp:
    def __init__(self, root):
        self.root = root
        self.root.title("生肖星座查询")
        
        # 生肖与星座对应关系
        self.zodiac_map = {
            "鼠": "双鱼座 Pisces",
            "牛": "白羊座 Aries",
            "虎": "金牛座 Taurus",
            "兔": "双子座 Gemini",
            "龙": "巨蟹座 Cancer",
            "蛇": "狮子座 Leo",
            "马": "处女座 Virgo",
            "羊": "天秤座 Libra",
            "猴": "天蝎座 Scorpio",
            "鸡": "射手座 Sagittarius",
            "狗": "魔羯座 Capricorn",
            "猪": "水瓶座 Aquarius"
        }
        
        # 创建显示标签
        self.result_label = tk.Label(root, text="请选择生肖", font=('Arial', 14))
        self.result_label.pack(pady=20)
        
        # 创建按钮框架
        button_frame = tk.Frame(root)
        button_frame.pack()
        
        # 创建12个生肖按钮
        animals = ["鼠","牛","虎","兔","龙","蛇","马","羊","猴","鸡","狗","猪"]
        for i, animal in enumerate(animals):
            row = i // 4
            col = i % 4
            btn = tk.Button(button_frame, text=animal, width=5, height=2,
                           command=lambda a=animal: self.show_zodiac(a))
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def show_zodiac(self, animal):
        zodiac = self.zodiac_map.get(animal, "未知星座")
        self.result_label.config(text=f"{animal}对应: {zodiac}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ZodiacApp(root)
    root.mainloop()
