from pico2d import *

import game_framework
import infinity_mode
import normal_mode
from mode import StartMenu, ModeSelect


def init():
    global start_menu
    global mode_select

    start_menu = StartMenu()
    mode_select = ModeSelect()

def draw():
    clear_canvas()
    start_menu.image.draw(750, 420)
    start_menu.mode_select.draw()
    start_menu.font.draw(800, 400, 'The SKI', (0, 0, 0))
    update_canvas()


def finish():
    global start_menu
    del start_menu


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif mode_select.handle_event(event):
            if mode_select.selected_mode == 'NORMAL':
                game_framework.change_mode(normal_mode)
            elif mode_select.selected_mode == 'INFINITY':
                game_framework.change_mode(infinity_mode)