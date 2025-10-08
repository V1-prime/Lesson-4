import pygame
pygame.init()


WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

font = pygame.font.SysFont("Arial", 30)
WHITE =  (255,255,255)
score_text = font.render("Тут буде текст", True, WHITE)
BLACK = (0, 0, 0)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(BLACK)
    screen.blit(score_text,(WIDTH/2,0))
    pygame.display.flip()
pygame.quit()