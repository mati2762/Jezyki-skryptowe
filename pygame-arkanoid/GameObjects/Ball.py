import pygame
from random import randint
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball(pygame.sprite.Sprite):
    width = 20
    height = 20
    start = False

    def __init__(self, x, y):
        self.image = pygame.image.load("images/58-Breakout-Tiles.png").convert()
        self.surf = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.surf.get_rect(center=(x, y))

    def run_ball(self):
        if (self.start == False):
            self.velocity = [2, 2]
            self.start = True

    def stop_ball(self):
        self.start = False;

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        if self.velocity[1] > 0:
            self.velocity[1] = -randint(2, 4)
        else:
            self.velocity[1] = randint(2, 4)

    def update(self):
        if self.start == True:
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            if self.rect.x >= SCREEN_WIDTH - self.width:
                self.velocity[0] = -self.velocity[0]
            if self.rect.x <= 0:
                self.velocity[0] = -self.velocity[0]
            if self.rect.y < 0:
                self.velocity[1] = -self.velocity[1]
