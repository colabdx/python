# 定义一个函数来计算大选成绩
def calculate_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

# 主程序
print("いらっしゃいませ！えらい人を選びましょう！")
name = input("総理大臣の名前：")
score = float(input("総理大臣の成績："))

# 调用函数计算成绩等级
grade = calculate_score(score)

# 输出成绩报告
print("===================")
print("名前：", name)
print("成績：", score)
print("結果：", grade)
