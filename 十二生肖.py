import tkinter as tk
import random

class DNAGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Generator")

        # 创建十二个按钮
        self.mouse_button = tk.Button(self.root, text="鼠DNA", command=self.generate_mouse_dna)
        self.mouse_button.pack(side=tk.LEFT, fill=tk.Y)
        
        self.cow_button = tk.Button(self.root, text="牛DNA", command=self.generate_cow_dna)
        self.cow_button.pack(side=tk.LEFT, fill=tk.Y)
        
        self.tiger_button = tk.Button(self.root, text="虎DNA", command=self.generate_tiger_dna)
        self.tiger_button.pack(side=tk.LEFT, fill=tk.Y)
        
        self.rabbit_button = tk.Button(self.root, text="兔DNA", command=self.generate_rabbit_dna)
        self.rabbit_button.pack(side=tk.LEFT, fill=tk.Y)

        self.dragon_button = tk.Button(self.root, text="龙DNA", command=self.generate_dragon_dna)
        self.dragon_button.pack(side=tk.LEFT, fill=tk.Y)

        self.snake_button = tk.Button(self.root, text="蛇DNA", command=self.generate_snake_dna)
        self.snake_button.pack(side=tk.LEFT, fill=tk.Y)
        
        self.horse_button = tk.Button(self.root, text="马DNA", command=self.generate_horse_dna)
        self.horse_button.pack(side=tk.LEFT, fill=tk.Y)

        self.sheep_button = tk.Button(self.root, text="羊DNA", command=self.generate_sheep_dna)
        self.sheep_button.pack(side=tk.LEFT, fill=tk.Y)

        self.monkey_button = tk.Button(self.root, text="猴DNA", command=self.generate_monkey_dna)
        self.monkey_button.pack(side=tk.LEFT, fill=tk.Y)

        self.rooster_button = tk.Button(self.root, text="鸡DNA", command=self.generate_rooster_dna)
        self.rooster_button.pack(side=tk.LEFT, fill=tk.Y)

        self.dog_button = tk.Button(self.root, text="狗DNA", command=self.generate_dog_dna)
        self.dog_button.pack(side=tk.LEFT, fill=tk.Y)

        self.pig_button = tk.Button(self.root, text="猪DNA", command=self.generate_pig_dna)
        self.pig_button.pack(side=tk.LEFT, fill=tk.Y)



        # 创建十二个标签用于显示生成的DNA序列
        self.mouse_label = tk.Label(self.root, text="")
        self.mouse_label.pack()
        
        self.cow_label = tk.Label(self.root, text="")
        self.cow_label.pack()
        
        self.tiger_label = tk.Label(self.root, text="")
        self.tiger_label.pack()
        
        self.rabbit_label = tk.Label(self.root, text="")
        self.rabbit_label.pack()

        self.dragon_label = tk.Label(self.root, text="")
        self.dragon_label.pack()

        self.snake_label = tk.Label(self.root, text="")
        self.snake_label.pack()

        self.horse_label = tk.Label(self.root, text="")
        self.horse_label.pack()

        self.sheep_label = tk.Label(self.root, text="")
        self.sheep_label.pack()
        
        self.monkey_label = tk.Label(self.root, text="")
        self.monkey_label.pack()

        self.rooster_label = tk.Label(self.root, text="")
        self.rooster_label.pack()

        self.dog_label = tk.Label(self.root, text="")
        self.dog_label.pack()

        self.pig_label = tk.Label(self.root, text="")
        self.pig_label.pack()

    def generate_mouse_dna(self):
        self.mouse_label.config(text=self.generate_dna(20), wraplength=500)

    def generate_cow_dna(self):
        self.cow_label.config(text=self.generate_dna(30), wraplength=500)

    def generate_tiger_dna(self):
        self.tiger_label.config(text=self.generate_dna(19), wraplength=500)

    def generate_rabbit_dna(self):
        self.rabbit_label.config(text=self.generate_dna(22), wraplength=500)

    def generate_dragon_dna(self):
        self.dragon_label.config(text=self.generate_dna(25), wraplength=500)

    def generate_snake_dna(self):
        self.snake_label.config(text=self.generate_dna(23), wraplength=500)

    def generate_horse_dna(self):
        self.horse_label.config(text=self.generate_dna(32), wraplength=500)

    def generate_sheep_dna(self):
        self.sheep_label.config(text=self.generate_dna(30), wraplength=500)

    def generate_monkey_dna(self):
        self.monkey_label.config(text=self.generate_dna(24), wraplength=500)

    def generate_rooster_dna(self):
        self.rooster_label.config(text=self.generate_dna(39), wraplength=500)

    def generate_dog_dna(self):
        self.dog_label.config(text=self.generate_dna(39), wraplength=500)

    def generate_pig_dna(self):
        self.pig_label.config(text=self.generate_dna(19), wraplength=500)


        
    def generate_dna(self, length):
        bases = ["A-T，", "T-A，", "C-G，", "G-C，"]
        return ''.join(random.choice(bases) for _ in range(length))

# 创建窗口并运行应用
root = tk.Tk()
app = DNAGeneratorApp(root)
root.mainloop()
