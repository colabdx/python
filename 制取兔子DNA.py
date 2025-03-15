import tkinter as tk
import random

class DNAGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Generator")

        # 创建两个按钮

        self.rabbit_button = tk.Button(self.root, text="制作家兔DNA", command=self.generate_rabbit_dna)
        self.rabbit_button.pack()

        self.hare_button = tk.Button(self.root, text="制作野兔DNA", command=self.generate_hare_dna)
        self.hare_button.pack()

        # 创建两个标签用于显示生成的DNA序列

        self.rabbit_label = tk.Label(self.root, text="")
        self.rabbit_label.pack()

        self.hare_label = tk.Label(self.root, text="")
        self.hare_label.pack()

    def generate_rabbit_dna(self):
        self.rabbit_label.config(text=self.generate_dna(22), wraplength=400)

    def generate_hare_dna(self):
        self.hare_label.config(text=self.generate_dna(24), wraplength=400)
        
    def generate_dna(self, length):
        bases = ["A-T，", "T-A，", "C-G，", "G-C，"]
        return ''.join(random.choice(bases) for _ in range(length))

# 创建窗口并运行应用
root = tk.Tk()
app = DNAGeneratorApp(root)
root.mainloop()
