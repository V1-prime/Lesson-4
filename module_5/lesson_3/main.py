from dis import disco

import pygame
import random
pygame.init()
import math


background_color = (153, 51, 255)
pygame.display.set_caption("My game")
polygon_position = pygame.math.Vector2(0, 00)
direction = pygame.math.Vector2(50, 50)

SIZE = (700, 600)
screen = pygame.display.set_mode(SIZE)


yellow = (255, 255, 0)

def draw_star(surface, color, position , outer_radius, inner_radius):
    center_x, center_y = position[0],position[1]
    """Draws a five-pointed star."""
    points = []
    score = 0

    for i in range(5):
        # Outer point
        angle_outer = math.pi / 2 + (2 * math.pi * i / 5)
        x_outer = center_x + outer_radius * math.cos(angle_outer)
        y_outer = center_y - outer_radius * math.sin(angle_outer)
        points.append((x_outer, y_outer))

        # Inner point
        angle_inner = math.pi / 2 + (2 * math.pi * i / 5) + (math.pi / 5)
        x_inner = center_x + inner_radius * math.cos(angle_inner)
        y_inner = center_y - inner_radius * math.sin(angle_inner)
        points.append((x_inner, y_inner))

    pygame.draw.polygon(surface, color, points)
WHITE = (255, 255, 255)
def new_position() -> None:
    polygon_position.x = random.randint(0, SIZE[0])
    polygon_position.y = random.randint(0, SIZE[1])

def game():
    font = pygame.font.SysFont('Comic Sans SM', 50)
    font_score = pygame.font.SysFont('Comic Sans SM', 30)
    text_score = font_score.render('0',True,WHITE)
    timer_text = font.render('60', True, WHITE)
    runnable = True
    outer_radius = 30
    inner_radius = 20
    last_move_time = 0
    last_game_time = 0
    game_timer = 60
    score = 0

    while runnable:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnable = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    distance = ((polygon_position.x - mouse_x ) ** 2 + (polygon_position.y - mouse_y)**2) ** 0.5
                    # if distance < outer_radius:
                    #     score += 1
                    #     text_score = font_score.render(f"{score}",True,WHITE)
                    if distance < outer_radius:
                        score += 1
                        text_score = font_score.render(str(score), True, WHITE)
                        new_position()
                        last_move_time = current_time

        if current_time - last_game_time >= 1000:
            game_timer -= 1
            timer_text = font.render(f'Time: {game_timer}', True, WHITE)
            last_game_time = current_time

        if current_time - last_move_time >= 1000: # 1000 мс = 1 секунда
            new_position()# встановили нову позицію у фігури
            last_move_time = current_time

        screen.fill(background_color)
        screen.blit(timer_text, (SIZE[0] / 2 -  timer_text.get_width(), 0))
        screen.blit(text_score, (SIZE[0]- text_score.get_width(), 10))
        draw_star(screen, yellow, polygon_position, outer_radius, inner_radius)
        pygame.display.flip()
    pygame.quit()

game()