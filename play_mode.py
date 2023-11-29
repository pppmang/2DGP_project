from pico2d import *
import game_framework

import game_world
from background import GameBackground
from mode import StartMenu, ModeSelect, NormalMode, InfinityMode
from skier import Skier


def handle_events():
    mode_select = ModeSelect()
    current_mode = None

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif current_mode is None:
            current_mode = mode_select.handle_event(event)
            # 게임 진행 화면으로 전환할 때 캔버스 크기 변경
            if current_mode is not None:
                canvas_width, canvas_height = 1000, 1500
                resize_canvas(canvas_width, canvas_height)
        else:
            skier.handle_event(event)


def init():
    global skier
    global start_menu
    global game_background

    start_menu = StartMenu()

    skier = Skier()
    game_world.add_object(skier, 2)
    game_world.add_collision_pair('skier:finish_line', skier, None)

    game_background = GameBackground()
    game_world.add_object(game_background, 0)
