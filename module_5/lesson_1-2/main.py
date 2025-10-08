import pygame
from random import randint
# Ініціалізуємо Pygame
pygame.init()
# Зберігаємо у змінних розміри вікна (ширина, висота)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
# Зберігаємо у змінній основний колір фону (RGB)
background_color = (15, 128, 5) # Небесно-блакитний
# Створюємо вікно
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Встановлюємо назву вікна
pygame.display.set_caption("Моя перша гра")
# Заповнюємо фон кольором
runnable = True
rect_position = pygame.math.Vector2(200, 300)

direction = pygame.math.Vector2(0, 0)

while runnable:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnable = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runnable = False
            elif event.key == pygame.K_RETURN:
                background_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            elif event.key == pygame.K_s:
                rect_position.y += 10
            elif event.key == pygame.K_w:
                rect_position.y -= 10
            elif event.key == pygame.K_a:
                rect_position.x -= 10
            elif event.key == pygame.K_d:
                rect_position.x += 10

    screen.fill(background_color)
    pygame.draw.rect(screen, (0, 0, 225), (rect_position.x, rect_position.y, 50, 50))
    # Оновлюємо дисплей
    pygame.display.flip()

# Затримка перед виходом
pygame.time.delay(0)

pygame.quit()