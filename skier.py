import random

from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, draw_rectangle

import game_world


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

# Skier Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Skier Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 11

elapsed_time = 0.0

class Idle:
    @staticmethod
    def enter(skier, e):
        if skier.action == 0:
            skier.action = 2
class StateMachine:
    def __init__(self, skier):
        self.skier = skier
        self.cur_state = Idle
        self.transitions = {}


class Skier:
    def __init__(self):
        self.x, self.y = 500, 1300
        self.frame = 0
        self.action = 0
        self.frame_width = 80
        self.frame_height = 60
        self.dir = 0    # 오른쪽, 왼쪽 방향 구분 위해서 ( 오른쪽 : 1, 왼쪽 : -1)
        self.image = load_image('skier.png')
        # self.state_machine = StateMachine(self)
        # self.state_machine.start()

    def update(self):
        pass
        # self.state_machine.update()
        # self.x += self.dir * 5      # skier 이동 속도 (일단 고정)

    def handle_event(self, event):
        # self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
        # self.state_machine.draw()
        self.image.clip_draw(int(self.frame) * self.frame_width, self.action * self.frame_height, self.frame_width, self.frame_height)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x -25, self.y - 28, self.x + 25, self.y + 28

    # def handle_collision(self, group, other):
    #     match group:
    #         case 'skier:finishline':
