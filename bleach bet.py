import pygame
import sys
import math
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hydrogen Permanganate Game")

# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# 设置字体
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 60)

# 玩家状态
player_life = 100
player_gold = 10000
player_score = 0

# 双氧奶按钮状态
hydrogen_permanganate_concentrations = [6, 9, 12, 24]
selected_concentration = None
last_select_time = 0
effect_duration = 1200  # 毫秒

# 特效参数
bubble_timer = 0
bubbles = []

# 旋转动画参数
alchemic_angle = 0

clock = pygame.time.Clock()

# 按钮参数
button_width, button_height = 100, 100
button_y = 100
button_gap = 40
button_start_x = (screen_width - (button_width * len(hydrogen_permanganate_concentrations) + button_gap * (len(hydrogen_permanganate_concentrations)-1))) // 2

def get_button_rect(idx):
    button_x = button_start_x + idx * (button_width + button_gap)
    return pygame.Rect(button_x, button_y, button_width, button_height)

def draw_rotating_alchemy_circle(surface, center, radius, angle):
    pygame.draw.circle(surface, WHITE, center, radius, 3)
    for i in range(3):
        a1 = math.radians(angle + i*120)
        a2 = math.radians(angle + (i+1)*120)
        x1 = center[0] + math.cos(a1) * radius
        y1 = center[1] + math.sin(a1) * radius
        x2 = center[0] + math.cos(a2) * radius
        y2 = center[1] + math.sin(a2) * radius
        pygame.draw.line(surface, WHITE, (x1, y1), (x2, y2), 2)
    for i in range(6):
        a = math.radians(angle + i*60)
        x = center[0] + math.cos(a) * (radius-30)
        y = center[1] + math.sin(a) * (radius-30)
        pygame.draw.circle(surface, GOLD, (int(x), int(y)), 10)

def spawn_bubbles(center, num=6):
    new_bubbles = []
    for _ in range(num):
        x, y = center
        dx = random.uniform(-2, 2)
        dy = random.uniform(-3, -1)
        r = random.randint(8, 20)
        new_bubbles.append({'x': x + random.randint(-20, 20), 'y': y, 'dx': dx, 'dy': dy, 'r': r})
    return new_bubbles

# 游戏主循环
running = True
game_over = False
win = False

while running:
    dt = clock.tick(60)
    now = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            for idx, concentration in enumerate(hydrogen_permanganate_concentrations):
                btn_rect = get_button_rect(idx)
                if btn_rect.collidepoint(mouse_x, mouse_y):
                    selected_concentration = concentration
                    last_select_time = now
                    # 生命值和金币逻辑
                    player_life -= 5.76
                    player_gold -= int(100 * (concentration/6))
                    player_score += int(10 * concentration)
                    # 生成气泡/金色特效
                    bubbles.clear()
                    if concentration == 6:
                        bubble_timer = now
                        bubbles = spawn_bubbles((screen_width//2, screen_height//2), num=8)
                    # 结束条件
                    if player_life <= 0 or player_gold < 0:
                        game_over = True
                        win = False
                    if player_score >= 2000:
                        game_over = True
                        win = True

    # 清屏
    screen.fill(WHITE)

    # 绘制顶部状态栏
    pygame.draw.rect(screen, GREY, (0, 0, screen_width, 50))
    # 绘制生命值血条
    life_bar_length = 300
    life_bar_x = (screen_width - life_bar_length) // 2
    life_bar_y = 10
    life_bar_width = max(0, life_bar_length * (player_life / 100))
    pygame.draw.rect(screen, RED, (life_bar_x, life_bar_y, life_bar_width, 30))
    # 绘制剩余金币数
    gold_text = font.render(f'Gold: {max(0,player_gold)}', True, BLACK)
    screen.blit(gold_text, (10, 10))
    # 绘制分数
    score_text = font.render(f'Score: {player_score}', True, BLACK)
    screen.blit(score_text, (screen_width-180, 10))

    # 绘制双氧奶按钮
    for idx, concentration in enumerate(hydrogen_permanganate_concentrations):
        btn_rect = get_button_rect(idx)
        pygame.draw.rect(screen, BLACK, btn_rect, 3)
        if concentration == selected_concentration and (now-last_select_time < effect_duration):
            pygame.draw.circle(screen, GOLD, btn_rect.center, 10)
        concentration_text = font.render(f'{concentration}%', True, BLACK)
        text_rect = concentration_text.get_rect(center=btn_rect.center)
        screen.blit(concentration_text, text_rect)

    # 显示特效
    if selected_concentration and (now-last_select_time < effect_duration):
        if selected_concentration == 24:
            # 金色闪光和炼金阵
            screen.fill(GOLD)
            alchemic_angle += 3
            draw_rotating_alchemy_circle(screen, (screen_width//2, screen_height//2), 100, alchemic_angle)
        elif selected_concentration == 6:
            # 蓝色气泡动画
            if not bubbles:
                bubbles = spawn_bubbles((screen_width//2, screen_height//2), num=8)
            for bubble in bubbles:
                bubble['x'] += bubble['dx']
                bubble['y'] += bubble['dy']
                bubble['dy'] += 0.05 # 重力
                alpha = max(0, 255-int((bubble['y']-screen_height//2)*6))
                bubble_surf = pygame.Surface((bubble['r']*2, bubble['r']*2), pygame.SRCALPHA)
                pygame.draw.circle(bubble_surf, (0, 180, 255), (bubble['r'], bubble['r']), bubble['r'])
                screen.blit(bubble_surf, (bubble['x']-bubble['r'], bubble['y']-bubble['r']))
        elif selected_concentration == 9:
            # 绿色闪烁
            for i in range(10):
                pygame.draw.circle(screen, (0,255,0,50), (screen_width//2, screen_height//2), 40+i*10, 2)
        elif selected_concentration == 12:
            # 紫色粒子雨
            for i in range(40):
                px = random.randint(100, 700)
                py = random.randint(120, 580)
                pygame.draw.circle(screen, (160, 32, 240), (px, py), random.randint(2, 6))
    else:
        selected_concentration = None

    # 失败或胜利界面
    if game_over:
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0,0))
        result_text = "You Win!" if win else "Game Over"
        color = GOLD if win else RED
        text = big_font.render(result_text, True, color)
        screen.blit(text, (screen_width//2 - text.get_width()//2, screen_height//2 - 60))
        tip = font.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(tip, (screen_width//2 - tip.get_width()//2, screen_height//2 + 10))
        pygame.display.flip()
        # 等待玩家操作
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # 重置游戏
                        player_life = 100
                        player_gold = 10000
                        player_score = 0
                        selected_concentration = None
                        bubbles = []
                        game_over = False
                        win = False
                        waiting = False
                    elif event.key == pygame.K_q:
                        running = False
                        waiting = False

    # 更新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
sys.exit()
