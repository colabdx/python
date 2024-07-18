import random

# 花名列表
flowers = ['梨花', '杏花', '樱花', '梅花', '荷花',
           '睡莲', '牡丹', '芍药', '月季花', '蔷薇',
           '玫瑰花', '雏菊', '水仙', '杜鹃']

# 随机抽取一种花
selected_flower = random.choice(flowers)
print(f"抽到的花是：{selected_flower}")

# 重复程序
while True:
    # 随机抽取一种花
    selected_flower = random.choice(flowers)
    print(f"重复抽到的花是：{selected_flower}")