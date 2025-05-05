import speech_recognition as sr
import pygame
import time

# 初始化积分
score = 0
target_score = 1000
button_active = False

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("金发成就系统")
font = pygame.font.SysFont('helvetica', 24)

# 初始化语音识别
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def listen_for_onze():
    """监听并识别语音中的'onze'"""
    global score, button_active
    
    print("正在监听...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # 使用Google语音识别
        text = recognizer.recognize_google(audio, language='fr-FR')  # 法语识别
        print("识别结果:", text)
        
        if "11" in text.lower():
            score += 500
            print(f"检测到'onze'! 当前积分: {score}/{target_score}")
            
            if score >= target_score and not button_active:
                button_active = True
                print("Score reached 1000! Press the button!")
    
    except sr.UnknownValueError:
        print("无法识别语音")
    except sr.RequestError as e:
        print(f"语音识别服务错误: {e}")

def draw_screen():
    """绘制屏幕界面"""
    screen.fill((255, 255, 255))
    
    # 显示积分
    score_text = font.render(f"Score: {score}/{target_score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))
    
    # 显示按钮
    button_color = (0, 255, 0) if button_active else (200, 200, 200)
    pygame.draw.rect(screen, button_color, (100, 100, 200, 80))
    
    button_text = font.render("bleach", True, (0, 0, 0))
    screen.blit(button_text, (180, 130))
    
    # 如果按钮激活，显示提示
    if button_active:
        hint_text = font.render("You can be a blonde!", True, (255, 0, 0))
        screen.blit(hint_text, (100, 200))
    
    pygame.display.flip()

def main():
    """主程序循环"""
    global button_active
    
    running = True
    last_listen_time = 0
    
    while running:
        current_time = time.time()
        
        # 每3秒监听一次语音
        if current_time - last_listen_time > 3:
            listen_for_onze()
            last_listen_time = current_time
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查是否点击了按钮
                    if button_active:
                        print("漂发按钮被按下! 你可以成为金发!")
                        # 这里可以添加更多的效果或功能
        
        # 绘制界面
        draw_screen()
        pygame.time.delay(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
