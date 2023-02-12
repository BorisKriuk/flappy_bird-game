import pygame
import random
from variables import SCREEN_WIDTH, SCREEN_HEIGHT, BG, GROUND, FPS, SCROLL_SPEED, PIPE_FREQUENCY, WHITE, BUTTON_IMG
from bird_class import Bird
from pipe_class import Pipe
from button_class import Button


def draw_text(text, text_font, x, y):
    img = text_font.render(text, True, WHITE)
    screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(SCREEN_HEIGHT // 2)
    score = 0
    return score


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy bird 1.0')

# define font
font = pygame.font.SysFont('Bauhaus 93', 60)

# define game variables
score = 0
pass_pipe = False
ground_scroll = 0
flying = False
game_over = False
pipe_gap = 150
last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(SCREEN_HEIGHT // 2))
bird_group.add(flappy)

# create restart button instance
button = Button(SCREEN_WIDTH // 2-75, SCREEN_HEIGHT // 2 - 100, BUTTON_IMG, screen)

running = True
while running:

    clock.tick(FPS)

    # draw background
    screen.blit(BG, (0, 0))

    bird_group.draw(screen)
    bird_group.update(flying, game_over)

    pipe_group.draw(screen)

    # draw the ground
    screen.blit(GROUND, (ground_scroll, 768))

    # check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left \
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right \
                and not pass_pipe:
            pass_pipe = True
        if pass_pipe:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score), font, int(SCREEN_WIDTH // 2) - 25, 20)

    # look for collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    # check if the bird has hit the ground
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if not game_over and flying:
        # generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > PIPE_FREQUENCY:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT // 2) + pipe_height, -1, pipe_gap)
            top_pipe = Pipe(SCREEN_WIDTH, int(SCREEN_HEIGHT // 2) + pipe_height, 1, pipe_gap)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        # scroll the ground
        ground_scroll -= SCROLL_SPEED
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        pipe_group.update()

    # check for game over and reset
    if game_over:
        if button.draw():
            game_over = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    pygame.display.update()

pygame.quit()
