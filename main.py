import pygame
from random import randint
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
background_color = (0, 0, 0)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy-Lezus")
rect_position = pygame.math.Vector2(200, 300)
path_character = 'character_animation/Lezus.png'
path_bg = 'character_animation/SFOTH_bg.png'
path_obstacle = 'character_animation/pillar.png'

background_img = pygame.image.load(path_bg).convert()
background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
background = pygame.sprite.Sprite()

player_img = pygame.image.load(path_character).convert()
player_img = pygame.transform.smoothscale(player_img,(65, 65))
player_rect = player_img.get_rect()
player_rect.topleft = (20,10)
player = pygame.sprite.Sprite()

pillar_img = pygame.image.load(path_obstacle).convert()
pillar_img = pygame.transform.smoothscale(pillar_img,(65, WINDOW_HEIGHT))
# pillar_rect = pillar_img.get_rect()
pillar = pygame.sprite.Sprite()

speed = 0
gravity = 0.2
jump_speed =+  7
clock = pygame.time.Clock()
runnable = True
font = pygame.font.SysFont('comicsans', 30)
ui_text = font.render("Hello ",True,(255,255,255))
obstacle_timer = 0
obstacles = []
obstacle_width = 60
gap_height = 150
min_distance = 250
time_spawned = 1000

def move_obstacle(obstacles):
    # step = 5
    # for obstacle in obstacles:
    #     obstacle.x -= step
    for top_obstacle, bottom_obstacle in obstacles:
        top_obstacle.x -= 5
        bottom_obstacle.x -= 5
        if player.colliderect(top_obstacle) or player.colliderect(bottom_obstacle):
            pygame.quit()
            exit()
        if top_obstacle.x < -obstacle_width:
            obstacles.remove((top_obstacle, bottom_obstacle))

    for top_obstacle, bottom_obstacle in obstacles:
        pygame.draw.rect(screen, top_obstacle)
        pygame.draw.rect(screen, bottom_obstacle)

move_obstacle(obstacles)

while runnable:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnable = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runnable = False
            #Jump
            elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                speed = -jump_speed
    current_time = pygame.time.get_ticks()


    if current_time - obstacle_timer >= time_spawned:
        top_obstacle_height = randint(gap_height, min_distance)
        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height
        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)

        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width,
                                      bottom_obstacle_height)

        obstacles.append((top_obstacle, bottom_obstacle))

        obstacle_timer = 0

    speed += gravity
    player_rect.y += speed
    movement_timer = current_time
    ui_text = font.render(f" {player_rect.y}", True, (255,255,255))


    if player_rect.y > WINDOW_HEIGHT:
        player_rect.y = WINDOW_HEIGHT #Гравця до землі притискаємо
        speed = 0

    screen.fill(background_color)

    # Оновлюємо дисплей
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, player_rect)
    screen.blit(pillar_img, (0, 0))
    screen.blit(ui_text, (WINDOW_WIDTH/2, 0))
    pygame.display.flip()
    clock.tick(60)
# Затримка перед виходом
pygame.time.delay(0)

pygame.quit()
#TODO
#       Something i want to add to my game
 # i want to add the ability to be able to get point by jumping over/under/between the moving poles
 # and also, "references" to things and trinkets connected to the character to collect and give additionally 5 points (the void star, comedy mask, tragedy mask, bible, cross, etc)
 # an animation for my character in 2 frames
 # also randomly add audio i'll choose during the game (like random AND loud (noli chase theme))
 # make my character spin when the music will come on and stop when it stops
 # make my character make bird sounds when he jumps