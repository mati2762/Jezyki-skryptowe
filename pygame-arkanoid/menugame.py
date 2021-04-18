import pygame
from gameconfig import GameConfig

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


button_1 = button_create("GAME", (200, 100, 200, 75), (255, 0, 0), (0, 255, 0), on_click_button_1)
button_2 = button_create("EXIT", (200, 200, 200, 75), (255, 0, 0), (0, 255, 0), on_click_button_2)

def generate_menu(screen, events):
    button_draw(screen, button_1)
    button_draw(screen, button_2)
    for event in events:
        button_check(button_1, event)
        button_check(button_2, event)
