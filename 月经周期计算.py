from datetime import datetime, timedelta

# 获取用户输入
cycle_length = int(input("请输入你的月经周期长度（天数）："))
period_length = int(input("请输入月经期长度（天数）："))
last_period_start = input("请输入最后一次月经开始日期（格式：YYYY-MM-DD）：")

# 将字符串日期转换为日期对象
last_period_date = datetime.strptime(last_period_start, "%Y-%m-%d")

# 计算排卵期和月经期的开始日期
ovulation_start = last_period_date + timedelta(days=cycle_length - 14)
period_start = last_period_date

# 计算安全期的开始和结束日期
safe_period_start = period_start + timedelta(days=period_length)
safe_period_end = ovulation_start - timedelta(days=1)

# 打印日历和标记
print("日期\t\t状态")
for i in range(28):  # 假设打印一个月的日历
    current_date = last_period_date + timedelta(days=i)
    if current_date >= period_start and current_date < period_start + timedelta(days=period_length):
        status = "月经期"
    elif current_date >= ovulation_start and current_date <= ovulation_start + timedelta(days=1):
        status = "排卵期"
    elif (current_date >= safe_period_start and current_date <= safe_period_end) or \
         (current_date < period_start) or \
         (current_date > safe_period_end + timedelta(days=cycle_length - period_length - 1)):
        status = "安全期"
    else:
        status = "安全期"
    
    print(current_date.strftime("%Y-%m-%d"), "\t", status)

# 注意：这个程序只打印了一个月的日历，实际使用中需要考虑多个月份的情况。
