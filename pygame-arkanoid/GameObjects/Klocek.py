import pygame
from constants import BlockType

class Klocek(pygame.sprite.Sprite):

    def __init__(self, x, y, type = BlockType.BLUE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(type.value).convert()
        self.surf = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.surf.get_rect(center=(x+25, y+10))


    def set_kolor(self, color):
        self.surf.fill(color)

