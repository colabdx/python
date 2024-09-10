from datetime import datetime, timedelta

# 获取用户输入的周期和月经期长度
cycle_length = int(input("请输入月经周期长度（天数）："))
period_length = int(input("请输入月经期长度（天数）："))

# 确定安全期的开始和结束日期
safe_period_start = period_length + 1
safe_period_end = cycle_length - period_length

# 创建一个月经周期日历
calendar = ["安全期"] * cycle_length

# 标记月经期
for i in range(period_length):
    calendar[i] = "月经期"

# 标记安全期
for i in range(safe_period_start, safe_period_end):
    calendar[i] = "安全期"

# 打印日历
for day, status in enumerate(calendar, 1):
    print(f"第{day}天: {status}")

# 如果需要与实际日期关联，可以获取当前日期，并计算周期内每天的日期
current_date = datetime.now()
for day, status in enumerate(calendar, 1):
    # 计算周期内每天的日期
    cycle_date = current_date + timedelta(days=day - 1)
    print(f"{cycle_date.strftime('%Y-%m-%d')}: {status}")