# 定义终点站的名称
threshold = "某地点"

# 假设的无人驾驶程序函数，用于演示如何使用终点站变量
def navigate_to_destination(current_location, destination):
    if current_location != destination:
        print(f"从 {current_location} 向 {destination} 行驶...")
        # 这里可以添加无人驾驶的导航逻辑
    else:
        print(f"已经到达终点站：{destination}")

# 示例使用
current_location = "起点站"
navigate_to_destination(current_location, threshold)