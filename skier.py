import random

from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, draw_rectangle, get_time

import game_world
import game_framework

# Skier Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Skier Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8




def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


# class Idle:
#     @staticmethod
#     def enter(skier, e):
#         if skier.dir == -1:
#             skier.action = 2
#         elif skier.dir == 1:
#             skier.action = 3
#         skier.dir=0
#         skier.frame=0
#         skier.wait_time=get_time()
#         pass
#
#     @staticmethod
#     def exit(skier,e):
#         pass
#
#     @staticmethod
#     def do(skier, e):
#         skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#         if get_time() - skier.wait_time > 2:
#             skier.state_machine.handle_event(('TIME_OUT', 0))
#
#     @staticmethod
#     def draw(skier):

class Run:
    @staticmethod
    def enter(skier, e):
        pass

    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier, e):
        pass

    @staticmethod
    def draw(skier, e):
        pass


class BlackOut:
    @staticmethod
    def enter(skier, e):
        pass

    @staticmethod
    def exit(skier, e):
        # 기절한지 3초가 지나면 이 상태에서 나감.
        pass

    @staticmethod
    def do(skier, e):
        # 기절상태가 된다. (3초간 skier이 움직이지 못함.)
        pass

    @staticmethod
    def draw(skier, e):
        pass
        


# class StateMachine:
#     def __init__(self, skier):
#         self.skier = skier
#         self.cur_state = Idle
#         self.transitions = {}
#         Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle},
#         Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
#         Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run}
#
#     def start(self):
#         self.cur_state.enter(self.skier, ('NONE', 0))
#
#     def update(self):
#         self.cur_state.do(self.skier)
#
#     def handle_event(self, e):
#         for check_event, next_state in self.transitions[self.cur_state].items():
#             if check_event(e):
#                 self.cur_state.exit(self.skier, e)
#                 self.cur_state = next_state
#                 self.cur_state.enter(self.skier, e)
#                 return True
#
#         return False
#
#     def draw(self):
#         self.cur_state.draw(self.skier)

class Skier:
    def __init__(self):
        self.x, self.y = 500, 1300
        self.frame = 0
        self.action = 9
        self.frame_width = 58
        self.frame_height = 56
        self.frame_x = self.frame_width
        self.frame_y = 0
        self.dir = 0  # 오른쪽, 왼쪽 방향 구분 위해서 ( 오른쪽 : 1, 왼쪽 : -1)
        self.image = load_image('skier.png')
        self.speed = 2
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
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 25, self.y - 28, self.x + 25, self.y + 28

    def handle_collision(self, group, other):
        pass
