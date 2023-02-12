import pygame

# window parameters
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936
FPS = 60
SCROLL_SPEED = 4
PIPE_FREQUENCY = 1500  # milliseconds

# color
WHITE = (255, 255, 255)

# load images
BG = pygame.image.load('bg.png')
GROUND = pygame.image.load('ground.png')
PIPE_IMG = pygame.image.load('pipe.png')
BUTTON_IMG = pygame.image.load('restart.png')