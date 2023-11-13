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


class Idle:
    @staticmethod
    def enter(skier, e):
        pass


class StateMachine:
    def __init__(self, skier):
        self.skier = skier
        self.cur_state = Idle
        self.transitions = {}


class Skier:
    def __init__(self):
        self.x, self.y = 500, 1300
        self.frame = 0
        self.action = 9
        self.dir = 0    # 오른쪽, 왼쪽 방향 구분 위해서 ( 오른쪽 : 1, 왼쪽 : -1)
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
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x -25, self.y - 28, self.x + 25, self.y + 28

    def handle_collision(self, group, other):
        pass
