import pygame
from random import randint, choice
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy-Lezus")

# --- Paths (замени на свои файлы) ---
path_character = 'character_animation/Lezus_1.png'
# Для 2-кадровой анимации можно подготовить список путей:

path_bg = 'character_animation/SFOTH_bg.png'
path_obstacle = 'character_animation/pillar.png'
sound_path_jump =  'sounds/parry-ultrakill.mp3'
sound_path_music = 'sounds/war-without_reason.mp3.mp3'
items_folder_name = 'score_items'
path_items = ['book.png', 'cross.png', 'crown.png', 'noli.png', 'snake.png', 'tragedy_mask.png', 'void_star.png']

path_items = [f"{items_folder_name}/{item_name}" for item_name in path_items]# 'score_items/book.png'
path_character_frames = ['character_animation/Lezus_1.png', 'character_animation/Lezus_2.png']
timer_items = 5000


frames = [pygame.image.load(p).convert_alpha() for p in path_character_frames]
path_loose_screen = 'character_animation/loose_screen.png'

# --- Load assets ---
background_img = pygame.image.load(path_bg).convert()
background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

player_img = pygame.image.load(path_character).convert_alpha()
player_img = pygame.transform.smoothscale(player_img, (65, 65))
player_angle = 0
take_item = True
def rotate_img():
    global player_angle
    player_angle += 1

    if player_angle >= 360:
        # global take_item
        # take_item = False
        player_angle = 0

player_rect = player_img.get_rect()
player_rect.topleft = (100, WINDOW_HEIGHT // 2)

items_img = pygame.image.load(path_bg).convert()
items_img = pygame.transform.smoothscale(player_img, (30, 30))
items_rect = items_img.get_rect()

pillar_img = pygame.image.load(path_obstacle).convert_alpha()
# pillar_img base will be scaled per obstacle to match its rect height/width

loose_screen_img = pygame.image.load(path_loose_screen).convert_alpha()
loose_screen_img = pygame.transform.scale(loose_screen_img, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


# Optional: load jump sound (uncomment if you have file)
jump_sound = pygame.mixer.Sound(sound_path_jump)

# --- Physics & game state ---
speed = 0.0
gravity = 0.6
jump_speed = 7  # positive; when jumping we set speed = -jump_speed

clock = pygame.time.Clock()
runnable = True

font = pygame.font.SysFont('comicsans', 30)

# Obstacles: list of dicts {rect: pygame.Rect, scored: bool}
obstacles = []
obstacle_width = 80
gap_height = 180
min_top = 80
max_top = 420

# Spawning timer (ms)
time_spawned = 3000
speed_obstacle = 5
obstacle_timer = pygame.time.get_ticks()  # start timer from now

score = 0
items = []

def spawn_item():
    random_img = choice(path_items)
    rect_img = pygame.rect.Rect(WINDOW_WIDTH, randint(0,WINDOW_HEIGHT), 100, 100)

def create_obstacle():
    top_h = randint(min_top, max_top)
    bottom_h = WINDOW_HEIGHT - top_h - gap_height

    top_rect = pygame.Rect(WINDOW_WIDTH, 0, obstacle_width, top_h)
    bottom_rect = pygame.Rect(WINDOW_WIDTH, WINDOW_HEIGHT - bottom_h, obstacle_width, bottom_h)

    # We store a pair: top and bottom; only one scored flag per pair
    obstacles.append({"top": top_rect, "bottom": bottom_rect, "scored": False})

def draw_items():
    for item in items:
        screen.blit()

def draw_obstacles():
    for pair in obstacles:
        t = pair["top"]
        b = pair["bottom"]

        # scale pillar image to rect sizes on the fly
        top_img = pygame.transform.smoothscale(pillar_img, (t.width, t.height))
        bottom_img = pygame.transform.smoothscale(pillar_img, (b.width, b.height))

        # For top obstacle we blit at its topleft (0 y is top)
        screen.blit(top_img, t)
        screen.blit(bottom_img, b)

def move_obstacles(step):
    # move each pair left
    for pair in obstacles:
        pair["top"].x -= step
        pair["bottom"].x -= step

    # remove offscreen pairs
    while obstacles and obstacles[0]["top"].right < 0:
        obstacles.pop(0)

def check_collision():
    # check player rect against every obstacle rect
    for pair in obstacles:
        if player_rect.colliderect(pair["top"]) or player_rect.colliderect(pair["bottom"]):
            return True
    return False



def update_scoring():
    global score
    for pair in obstacles:
        # if the pair hasn't been scored and player's x passed the obstacle center
        if not pair["scored"] and player_rect.left > pair["top"].centerx:
            pair["scored"] = True
            score += 1
        if player_rect.colliderect(items_rect):
            score += 5
            global take_item
            take_item = True


# spawn initial obstacle so player has something immediately
create_obstacle()

# def draw_loose_img():
#
#     screen.blit(loose_text, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
#     screen.blit(loose_screen_img)

current_frame = 0
frame_timer = 0
frame_interval = 200  # ms between frames

pygame.mixer.init()
sound_effect = pygame.mixer.music.load("sounds/war-without_reason.mp3 ")
pygame.mixer.music.play(loops=-1)
channel1 = pygame.mixer.Channel(0)


while runnable:
    dt = clock.tick(60)  # keep 60 FPS; dt in ms

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnable = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                runnable = False
            elif event.key in (pygame.K_w, pygame.K_UP, pygame.K_SPACE):
                speed = -jump_speed
                if jump_sound: jump_sound.play()

    if take_item:
        rotate_img()

    rotated_img = pygame.transform.rotate(player_img, player_angle)
    rotated_rect = rotated_img.get_rect(center=player_rect.center)
    # spawn obstacles by timer
    current_time = pygame.time.get_ticks()
    if current_time - obstacle_timer >= time_spawned:
        create_obstacle()
        obstacle_timer = current_time

    # move obstacles
    move_obstacles(speed_obstacle)  # tune speed here

    # physics
    speed += gravity
    player_rect.y += speed

    # floor/cieling collision
    if player_rect.bottom >= WINDOW_HEIGHT:
        player_rect.bottom = WINDOW_HEIGHT
        speed = 0
    if player_rect.top <= 0:
        player_rect.top = 0
        speed = 0
    # scoring (player passed obstacles)
    update_scoring()

    # collision check
    if check_collision():
        # print("Collision! Game over. Score:", score)
        pygame.time.delay(1000)
        sound_effect = False

        # можно остановить или рестартовать игру


    # draw
    screen.blit(background_img, (0, 0))
    draw_obstacles()
    screen.blit(rotated_img, rotated_rect)

    # UI score

    ui_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(ui_text, (WINDOW_WIDTH // 2 - ui_text.get_width() // 2, 10))


    pygame.display.flip()

pygame.quit()

#TODO
#       Something i want to add to my game
 # ✔ i want to add the ability to be able to get point by jumping over/under/between the moving poles
 # ✖ and also, "references" to things and trinkets connected to the character to collect and give additionally 5 points (the void star, comedy mask, tragedy mask, bible, cross, etc)
 # ✖ an animation for my character in 2 frames
 # make my character spin when the 5+ points items on the screen
 # ✔? make my character make parry sounds when he jumps