from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, draw_rectangle, clamp

import game_framework
from score import Score

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
RUN_SPEED_KMPH = 35.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 실제 알파인 스키 최고 속도 160 km/h

# Skier Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 11


class Idle:
    @staticmethod
    def enter(skier, e):
        skier.action = 0
        skier.speed = 0
        skier.dir = 0

    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        pass
        # skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

    @staticmethod
    def draw(skier):
        skier.image.clip_draw(int(skier.frame) * skier.frame_width, skier.action * skier.frame_height,
                              skier.frame_width, skier.frame_height, skier.x, skier.y)


class SkiRight:
    @staticmethod
    def enter(skier, e):
        skier.action = 1
        skier.speed = RUN_SPEED_PPS
        skier.dir = 1


    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        skier.x += RUN_SPEED_PPS * game_framework.frame_time
        skier.x = clamp(70, skier.x, 1500 - 70)
        skier.y = 1300
        pass

    @staticmethod
    def draw(skier):
        skier.image.clip_draw(int(skier.frame) * skier.frame_width, skier.action * skier.frame_height,
                              skier.frame_width, skier.frame_height, skier.x, skier.y)


class SkiLeft:
    @staticmethod
    def enter(skier, e):
        skier.action = 1
        skier.speed = RUN_SPEED_PPS
        skier.dir = -1

    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        skier.x -= RUN_SPEED_PPS * game_framework.frame_time
        skier.x = clamp(70, skier.x, 1500 - 70)
        skier.y = 1300
        pass

    @staticmethod
    def draw(skier):
        skier.image.clip_composite_draw(int(skier.frame) * skier.frame_width, skier.action * skier.frame_height,
                                        skier.frame_width, skier.frame_height, 0, 'h',
                                        skier.x, skier.y, skier.frame_width, skier.frame_height)


class BlackOut:
    @staticmethod
    def enter(skier, e):
        skier.action = 2
        skier.speed = 0
        pass

    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

    @staticmethod
    def draw(skier):
        pass


class StateMachine:
    def __init__(self, skier):
        self.skier = skier
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: SkiRight, left_down: SkiLeft, right_up: Idle, left_up: Idle},
            SkiRight: {right_up: Idle, left_down: SkiLeft},
            SkiLeft: {left_up: Idle, right_down: SkiRight}
        }

    def start(self):
        self.cur_state.enter(self.skier, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.skier)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.skier, e)
                self.cur_state = next_state
                self.cur_state.enter(self.skier, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.skier)


class Skier:
    def __init__(self):
        self.x, self.y = 500, 1300
        self.frame = 0
        self.action = 0
        self.frame_width = 80
        self.frame_height = 60
        # self.dir = 0  # 오른쪽, 왼쪽 방향 구분 위해서 ( 오른쪽 : 1, 왼쪽 : -1)
        self.image = load_image('skier.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.score = Score()

    def update(self):
        self.state_machine.update()
        self.score.increase_score(self.y)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 25, self.y - 28, self.x + 25, self.y + 28

    def handle_collision(self, group, other):
        match group:
            case 'skier:finishline':
                print('Finish')

            case 'skier:obstacle':
                print('BlackOut')
                self.score.obstacle_collision(other.type)
