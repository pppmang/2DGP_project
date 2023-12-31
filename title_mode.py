import game_framework
from pico2d import clear_canvas, update_canvas, get_events, SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, get_canvas_width, \
    get_canvas_height, resize_canvas

import infinity_mode
import normal_mode
from background import StartMenu, ModeSelect


def init():
    global start_menu
    global mode_select

    start_menu = StartMenu()
    mode_select = ModeSelect()

def draw():
    clear_canvas()
    # 현재 캔버스 크기를 확인
    current_canvas_width, current_canvas_height = get_canvas_width(), get_canvas_height()

    # 캔버스 크기가 변경되어야 하는 경우에만 크기 조절
    if current_canvas_width != 1500 or current_canvas_height != 840:
        resize_canvas(1500, 840)

    start_menu.draw()
    update_canvas()

def update():
    pass


def finish():
    global start_menu
    start_menu = None


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