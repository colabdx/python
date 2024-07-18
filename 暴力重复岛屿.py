import random

# 预定义的岛屿名称列表
islands = [
    '亚速尔群岛', '因纽维克岛', '卡亚俄岛', '鳕鱼角岛', '圣巴巴拉岛',
    '迪克森岛', '纳尔维克岛', '诺姆岛', '珀斯岛', '瓦尔帕莱索岛',
    '费尔维尔岛', '蒙得维的亚岛', '勒韦克岛', '旺加努依岛'
]

# 随机抽取一个岛屿名称
def select_island():
    island = random.choice(islands)
    print(f'随机抽取的岛屿名称: {island}')

# 主循环，等待用户按回车键
print("按回车键重复运行...")
input("按下回车键继续...")

# 重复运行
while True:
    select_island()