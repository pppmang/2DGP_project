import game_world
import game_framework
from pico2d import *

import server
from background import ModeSelect, GameFinish, InfinityMode
from obstacle import Obstacle
from skier import Skier
from score import Score

from background import GameBackground as Background


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
            server.skier.handle_event(event)
            server.game_finish.handle_event(event)


def init():
    server.background = Background()
    game_world.add_object(server.background, 0)

    infinity_mode = InfinityMode()
    life_images = infinity_mode.life_images
    for life in life_images:
        game_world.add_object(life, 2)

    server.skier = Skier()
    game_world.add_object(server.skier, 2)
    game_world.add_collision_pair('skier:obstacle', server.skier, None)

    server.obstacle = Obstacle()
    for obstacle in server.obstacle.obstacles:
        game_world.add_object(obstacle, 3)
        game_world.add_collision_pair('skier:obstacle', None, obstacle)

    server.score = Score()
    game_world.add_object(server.score, 3)

    server.game_finish = GameFinish()
    game_world.add_object(server.game_finish, 4)


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


