import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):


    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/50-Breakout-Tiles.png").convert()
        self.surf = pygame.transform.scale(self.image1, (90, 20))
        self.rect = self.surf.get_rect(center=(x + 45, y + 10))

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH






