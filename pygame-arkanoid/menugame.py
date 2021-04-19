import pygame
from gameconfig import GameConfig
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import os


def on_click_button_1():
    GameConfig.show_menu = False


def on_click_button_2():
    pygame.quit()


def button_create(text, rect, inactive_color, active_color, action):
    font = pygame.font.Font(None, 40)
    button_rect = pygame.Rect(rect)
    text = font.render(text, True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)

    return [text, text_rect, button_rect, inactive_color, active_color, action, False]


def button_draw(screen, info):
    text, text_rect, rect, inactive_color, active_color, action, hover = info
    if hover:
        color = active_color
    else:
        color = inactive_color

    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)


def button_check(info, event):
    text, text_rect, rect, inactive_color, active_color, action, hover = info
    if event.type == pygame.MOUSEMOTION:
        info[-1] = rect.collidepoint(event.pos)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()


button_1 = button_create("GAME", ((SCREEN_WIDTH / 2) - 100, 100, 200, 75), (111, 111, 111), (200, 200, 200),
                         on_click_button_1)
button_2 = button_create("EXIT", ((SCREEN_WIDTH / 2) - 100, 200, 200, 75), (111, 111, 111), (200, 200, 200),
                         on_click_button_2)

mode = 'r' if os.path.exists("./bestScores.txt") else 'w+'
file = open("bestScores.txt", mode)
for score in file:
    GameConfig.bestScores.append(int(score))
file.close()


def generate_menu(screen, events):
    button_draw(screen, button_1)
    button_draw(screen, button_2)

    # Wyświetlanie 5 najlepszych wyników
    if GameConfig.bestScores.__len__() > 0:
        font = pygame.font.Font(None, 34)
        text = font.render("Best Scores", 1, (255, 255, 255))
        screen.blit(text, ((SCREEN_WIDTH / 2 + 30) - 100, 300))

        font = pygame.font.Font(None, 24)
        index = 0
        for score in GameConfig.bestScores:
            text = font.render(str(index + 1) + ".  " + str(score), 1, (255, 255, 255))
            screen.blit(text, ((SCREEN_WIDTH / 2 + 70) - 100, 330 + index * 20))
            index += 1
            if index == 5:
                break

    for event in events:
        button_check(button_1, event)
        button_check(button_2, event)
