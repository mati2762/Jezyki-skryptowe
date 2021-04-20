from gameconfig import GameConfig
import pygame
from GameObjects.Player import Player
from GameObjects.Ball import Ball
from GameObjects.LevelGenerator import LevelGenerator
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE

pygame.init()
from menugame import generate_menu

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

pygame.display.set_caption("Arkanoid UJ")

player = Player(SCREEN_WIDTH / 2 - 45, 450)
ball = Ball(SCREEN_WIDTH / 2, 435)

klocki = LevelGenerator.generate_level()

pygame.mixer.music.load("sounds/intro.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

lives = GameConfig.lives
score = GameConfig.score
pause = False
uruchomiona = True
level = 1
stopgame = False
while uruchomiona:

    events = pygame.event.get();
    # Eventy , Klawiatura
    for event in events:
        if event.type == pygame.QUIT:
            uruchomiona = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                uruchomiona = False
            if event.key == K_SPACE:
                if stopgame == True:
                    GameConfig.show_menu = True
                else:
                    ball.run_ball()
            if event.key == pygame.K_p and ball.start == True:
                pause = not pause

    # Wyświetlanie Menu
    if GameConfig.show_menu == True:
        try:
            screen.fill((76, 76, 76))
            generate_menu(screen, events)
            clock.tick(60)
            pygame.display.update()
        except:
            uruchomiona = False
        continue;

    # End Game
    if level == 6:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 44)
        text = font.render("You Win", 1, (0, 255, 0))
        screen.blit(text, ((SCREEN_WIDTH / 2) - 70, (SCREEN_HEIGHT / 2) - 30))
        stopgame = True;
        clock.tick(60)
        pygame.display.flip()
        continue;

    # Game Over
    if lives == -1:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 44)
        text = font.render("Game Over", 1, (255, 255, 255))
        screen.blit(text, ((SCREEN_WIDTH / 2) - 90, (SCREEN_HEIGHT / 2) - 30))
        stopgame = True;
        clock.tick(60)
        pygame.display.flip()
        continue;

    # Pauza w grze
    if pause:
        font = pygame.font.Font(None, 44)
        text = font.render("Game Paused", 1, (255, 255, 255))
        screen.blit(text, ((SCREEN_WIDTH / 2) - 100, SCREEN_HEIGHT / 2))
        clock.tick(60)
        pygame.display.flip()
        continue;

    # Aktualizaja obiektów
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    ball.update()
    screen.fill((0, 0, 0))

    # Rysowanie spritów
    for klocek in klocki:
        screen.blit(klocek.surf, klocek.rect)
    screen.blit(player.surf, player.rect)
    screen.blit(ball.surf, ball.rect)

    # Wygrana
    if klocki.__len__() == 0:
        player = Player(SCREEN_WIDTH / 2 - 45, 450)
        ball = Ball(SCREEN_WIDTH / 2, 435)
        level += 1
        klocki = LevelGenerator.generate_level()

    # Kolizja z klockami
    if pygame.sprite.spritecollideany(ball, klocki):
        score += 1
        delete_klocek = pygame.sprite.spritecollideany(ball, klocki)
        delete_klocek.kill()
        ball.bounce()
        # usuniecie klocka

    # Kolizja z graczem
    if pygame.sprite.collide_rect(ball, player):
        ball.velocity[0] = -ball.velocity[0]
        ball.bounce()

    # Restart Gry
    if ball.rect.y > SCREEN_HEIGHT - ball.height:
        player = Player(SCREEN_WIDTH / 2 - 45, 450)
        ball = Ball(SCREEN_WIDTH / 2, 435)
        lives -= 1
        GameConfig.save_score(score)
        score = 0
        klocki = LevelGenerator.generate_level()

    # Rysowanie punktów i życia
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(text, (10, SCREEN_HEIGHT - 20))
    text = font.render("Lives: " + str(lives), 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 70, SCREEN_HEIGHT - 20))

    # Rozpoczecie gry
    if ball.start == False:
        font = pygame.font.Font(None, 44)
        text = font.render("To start click [Space]", 1, (255, 255, 255))
        screen.blit(text, ((SCREEN_WIDTH / 2) - 160, (SCREEN_HEIGHT / 2) + 70))
        text = font.render("Level " + str(level), 1, (255, 255, 255))
        screen.blit(text, ((SCREEN_WIDTH / 2) - 50, (SCREEN_HEIGHT / 2) + 30))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
