from pico2d import *
import game_framework

import game_world
from background import GameBackground
from mode import NormalMode
from obstacle import Obstacle
from score import Score
from skier import Skier
from start_menu import ModeSelect


def handle_events():
    mode_select = ModeSelect()
    current_mode = None

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            skier.handle_event(event)


def init():
    global skier
    global obstacle
    global start_menu
    global game_background
    global normal_mode
    global finishline
    global score

    game_background = GameBackground()
    game_world.add_object(game_background, 0)

    skier = Skier()
    game_world.add_object(skier, 2)
    game_world.add_collision_pair('skier:finishline', skier, None)
    game_world.add_collision_pair('skier:obstacle', skier, None)

    obstacle = Obstacle()
    for obstacle in obstacle.obstacles:
        game_world.add_object(obstacle, 1)
        game_world.add_collision_pair('skier:obstacle', None, obstacle)

    normal_mode = NormalMode()
    finishline = normal_mode.finish_line
    game_world.add_object(finishline, 1)
    game_world.add_collision_pair('skier:finishline', None, finishline)

    score = Score()
    game_world.add_object(score, 2)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    # 현재 캔버스 크기를 확인
    current_canvas_width, current_canvas_height = get_canvas_width(), get_canvas_height()

    # 캔버스 크기가 변경되어야 하는 경우에만 크기 조절
    if current_canvas_width != 1000 or current_canvas_height != 1500:
        resize_canvas(1000, 1500)
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass


