print("可以输入，再见，拜拜，你好，您好，我是谁，您认识我吗，今天天气怎么样，今天天气，你叫什么，你叫啥，或者按空格键")
def beijing_siri():
    print("您好，北京话Siri来啦！有什么能帮您的？")
    
    while True:
        command = input("您说：").strip().lower()
        
        if command in ["再见", "拜拜"]:
            print("拜拜，有空再来啊！")
            break
        elif command in ["你好", "您好"]:
            print("您好啊！")
        elif command in ["我是谁", "您认识我吗"]:
            print("您是我亲爱的用户，我咋能不认识您呢！")
        elif command in ["今天天气怎么样", "今天天气"]:
            print("今儿个天气不错，阳光明媚！")
        elif command in ["你叫什么", "你叫啥"]:
            print("我是一个北京话Siri，您想叫啥都成！")
        else:
            print("没听懂您说啥，您再说说？")

# 运行北京话Siri
beijing_siri()
