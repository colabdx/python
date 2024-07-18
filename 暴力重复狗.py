import random

# 预定义的狗名称列表
dogs = [
    '泰迪', '京巴', '柴犬', '拉布拉多', '哈士奇',
    '马尔济斯', '博美', '法斗', '', '金毛',
    '柯基', '萨摩耶', '雪纳瑞', '德牧'
]

# 随机抽取一个狗名称
def select_dog():
    dog = random.choice(dogs)
    print(f'随机抽取的狗名称: {dog}')

# 主循环，等待用户按回车键
print("按回车键重复运行...")
input("请按回车键开始抽取狗名称...")

# 重复运行
while True:
    select_dog()
