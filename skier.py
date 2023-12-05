import random
from time import time
from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, draw_rectangle, clamp, load_wav

import game_framework
import game_world
import server
from obstacle import Obstacle
from state import FRAMES_PER_ACTION, ACTION_PER_TIME, RUN_SPEED_PPS
from background import GameFinish

from score import Score


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def time_out(e):
    return e[0] == 'TIME_OUT'


# skier_turn_sound = load_wav('ski_change_dir.wav')
# skier_ski_sound = load_wav('skiing.wav')
# skier_turn_sound.set_volume(25)
# skier_ski_sound.set_volume(25)


class Idle:
    @staticmethod
    def enter(skier, e):
        skier.action = 0
        skier.speed = skier.speed
        skier.dir = 0
        # skier.skier_ski_sound.play()

    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11

    @staticmethod
    def draw(skier):
        skier.image.clip_draw(int(skier.frame) * skier.frame_width, skier.action * skier.frame_height,
                              skier.frame_width, skier.frame_height, skier.x, skier.y)


class SkiRight:
    @staticmethod
    def enter(skier, e):
        skier.action = 1
        skier.speed = skier.speed
        skier.dir = 1
        # skier.skier_turn_sound.play()


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
        skier.speed = skier.speed
        skier.dir = -1
        # skier.skier_turn_sound.play()

    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        skier.frame = (skier.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 11
        skier.x -= RUN_SPEED_PPS * game_framework.frame_time
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
        skier.action = 3
        skier.speed = 0
        skier.frame = random.choice([0, 1])
        skier.blackout_timer = time() + 3
    @staticmethod
    def exit(skier, e):
        pass

    @staticmethod
    def do(skier):
        if time() > skier.blackout_timer:
            skier.state_machine.handle_event(('TIME_OUT', None))  # 타이머 종료 시 Idle 상태로 전환

    @staticmethod
    def draw(skier):
        skier.image.clip_draw(skier.frame * skier.frame_width, skier.action * skier.frame_height, skier.frame_width,
                              skier.frame_height, skier.x, skier.y)
        pass


class StateMachine:
    def __init__(self, skier):
        self.skier = skier
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: SkiRight, left_down: SkiLeft, right_up: Idle, left_up: Idle, time_out: BlackOut},
            SkiRight: {right_up: Idle, left_down: SkiLeft, time_out: BlackOut},
            SkiLeft: {left_up: Idle, right_down: SkiRight, time_out: BlackOut},
            BlackOut: {time_out: Idle}
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
        self.speed = RUN_SPEED_PPS
        self.frame = 0
        self.action = 0
        self.frame_width = 80
        self.frame_height = 60
        self.image = load_image('skier.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.score = Score()
        self.acceleration_time = time() + 10  # 초기 가속 시간 설정

    def update(self):
        self.state_machine.update()

        # 10초마다 속도를 증가
        if time() > self.acceleration_time:
            self.acceleration_time = time() + 10
            self.accelerate()

    def accelerate(self):
        # 스키어 속도 증가
        self.speed += RUN_SPEED_PPS

    def set_speed(self, speed):
        self.speed = speed

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
                server.game_finish.state = 'draw'

            case 'skier:obstacle':
                for obstacle in server.obstacle.obstacles:
                    obstacle_type = obstacle.obstacle_type
                    if obstacle_type in ["tree", "rock"]:
                        self.state_machine.handle_event(('TIME_OUT', 0))
                        game_world.remove_collision_object(obstacle)
                        if server.infinity.life_count > 0:
                            server.infinity.remove_life_image()
                        if server.infinity.life_count <= 0:
                            server.infinity.life_count = 0
                            server.game_finish()
                    elif obstacle_type in ["flag"]:
                        server.obstacle.handle_collision('skier:obstacle', obstacle)
                        game_world.remove_collision_object(obstacle)

            # case 'skier:obstacle2':
            #     for obstacle in server.obstacle.generate_obstacle().obstacles:
            #         obstacle_type = obstacle.obstacle_type
            #         if obstacle_type in ["tree", "rock"]:
            #             self.state_machine.handle_event(('TIME_OUT', 0))
            #             game_world.remove_collision_object(obstacle)
            #         else:
            #             server.obstacle.handle_collision('skier:obstacle', obstacle)
            #             game_world.remove_collision_object(obstacle)