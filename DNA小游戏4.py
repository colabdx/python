import tkinter as tk
import random

class DNAGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Generator")

        # 创建四个按钮
        self.human_button = tk.Button(self.root, text="制作人类DNA", command=self.generate_human_dna)
        self.human_button.pack()

        self.dog_button = tk.Button(self.root, text="制作狗DNA", command=self.generate_dog_dna)
        self.dog_button.pack()

        self.pig_button = tk.Button(self.root, text="制作猪DNA", command=self.generate_pig_dna)
        self.pig_button.pack()

        self.rabbit_button = tk.Button(self.root, text="制作兔DNA", command=self.generate_rabbit_dna)
        self.rabbit_button.pack()

        # 创建四个标签用于显示生成的DNA序列
        self.human_label = tk.Label(self.root, text="")
        self.human_label.pack()

        self.dog_label = tk.Label(self.root, text="")
        self.dog_label.pack()

        self.pig_label = tk.Label(self.root, text="")
        self.pig_label.pack()

        self.rabbit_label = tk.Label(self.root, text="")
        self.rabbit_label.pack()

    def generate_human_dna(self):
        self.human_label.config(text=self.generate_dna(23), wraplength=400)

    def generate_dog_dna(self):
        self.dog_label.config(text=self.generate_dna(39), wraplength=400)

    def generate_pig_dna(self):
        self.pig_label.config(text=self.generate_dna(19), wraplength=400)

    def generate_rabbit_dna(self):
        self.rabbit_label.config(text=self.generate_dna(22), wraplength=400)
        
    def generate_dna(self, length):
        bases = ["A-T，", "T-A，", "C-G，", "G-C，"]
        return ''.join(random.choice(bases) for _ in range(length))

# 创建窗口并运行应用
root = tk.Tk()
app = DNAGeneratorApp(root)
root.mainloop()
