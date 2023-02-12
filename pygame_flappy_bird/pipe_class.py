import pygame
from variables import PIPE_IMG, SCROLL_SPEED


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, pipe_gap):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_gap = pipe_gap
        self.image = PIPE_IMG
        self.rect = self.image.get_rect()
        # position 1 is from the top, position 2 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y-int(pipe_gap) / 2]
        elif position == -1:
            self.rect.topleft = [x, y+int(pipe_gap) / 2]

    def update(self):
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()