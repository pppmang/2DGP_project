from pico2d import *
import game_framework
import server
from game_finish import GameFinish

from score import Score
from skier import RUN_SPEED_PPS


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        self.cw = get_canvas_width()    # 화면의 너비
        self.ch = get_canvas_height()   # 화면의 높이
        self.w = self.image.w
        self.h = self.image.h
        self.score = Score()

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)

    def update(self):
        self.window_left = int(server.skier.x) - self.cw // 2
        self.window_bottom = int(server.skier.y) - self.ch // 2

        self.window_left = clamp(0, self.window_left, self.w - self.cw - 1)
        self.window_bottom = clamp(0, self.window_bottom, self.h - self.ch - 1)
        self.score.increase_distance(RUN_SPEED_PPS * game_framework.frame_time)


class InfinityMode:
    def __init__(self):
        self.background = GameBackground()
        self.life_image = load_image('life.png')
        self.life_count = 3  # 초기 플레이어 생명 개수

    def draw(self):
        self.background.draw()

        for i in range(self.life_count):
            self.life_image.clip_draw(0, 0, 100, 122, 50 + i * 80, 1450)

    def update(self):
        self.background.update()

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle' if other.type in ['rock', 'tree']:
                self.life_count -= 1
                if self.life_count <= 0:
                    return GameFinish()
