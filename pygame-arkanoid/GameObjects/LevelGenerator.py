from constants import SCREEN_WIDTH, BlockType
import pygame
from GameObjects.Klocek import Klocek
import random

class LevelGenerator:

    @staticmethod
    def generate_level() -> pygame.sprite.Group():
        blocks = pygame.sprite.Group();
        for i in range(0, random.randint(6,15)):
            LevelGenerator.generate_layer(i*20,blocks, random.choice(list(BlockType)), random.randint(5,int(SCREEN_WIDTH / 50)))
        return blocks;

    @staticmethod
    def generate_layer(y,blocks, block_type= BlockType.BLUE, block_count=int(SCREEN_WIDTH / 50)):
        start = int(SCREEN_WIDTH - (block_count * 50)) / 2
        for i in range(0,block_count):
            klocek = Klocek(i * 50 + start, y, block_type)
            blocks.add(klocek)
