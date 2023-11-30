from pico2d import *
import game_framework

import game_world
from background import GameBackground
from mode import StartMenu, ModeSelect, InfinityMode
from obstacle import Obstacle
from skier import Skier




def init():
    global skier
    global obstacle
    global game_background
    global infinity_mode

    game_background = GameBackground()
    game_world.add_object(game_background, 0)

    skier = Skier()
    game_world.add_object(skier, 2)
    game_world.add_collision_pair('skier:finish_line', skier, None)
    game_world.add_collision_pair('skier:obstacle', skier, None)

    obstacle = Obstacle()
    for obstacle in obstacle.obstacles:
        game_world.add_object(obstacle, 1)
        game_world.add_collision_pair('skier:obstacle', None, obstacle)

    infinity_mode = InfinityMode()


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()
    handle_events()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass


