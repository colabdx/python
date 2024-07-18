# 定义一个函数来计算英语成绩
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
print("欢迎使用英语成绩打分系统！")
name = input("请输入学生姓名：")
score = float(input("请输入英语成绩："))

# 调用函数计算成绩等级
grade = calculate_score(score)

# 输出成绩报告
print("===================")
print("姓名：", name)
print("成绩：", score)
print("等级：", grade)