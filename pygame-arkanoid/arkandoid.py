import pygame
from GameObjects.Player import Player
from GameObjects.Klocek import Klocek
from GameObjects.Ball import Ball
from constants import  SCREEN_WIDTH,SCREEN_HEIGHT
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT



pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()

uruchomiona = True


pygame.display.set_caption("Arkanoid UJ")

player = Player(305,450)

klocek = Klocek(20, 20)

ball = Ball(315, 440)  

klocki = pygame.sprite.Group()
klocki.add(klocek)

def generate_level():
    pass

def update_ball_position():
    pass


pygame.mixer.music.load("sounds/intro.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while uruchomiona:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchomiona = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                uruchomiona = False
    
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    
    screen.fill((0,0,0))



    for klocek in klocki:
        screen.blit(klocek.surf, klocek.rect)
    screen.blit(player.surf, player.rect)
    screen.blit(ball.surf, ball.rect)

    if pygame.sprite.spritecollideany(ball, klocki):
        delete_klocek = pygame.sprite.spritecollideany(ball, klocki)
        delete_klocek.kill()
        # usuniecie klocka

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
