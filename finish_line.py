from pico2d import load_image, draw_rectangle

import game_framework
from game_finish import GameFinish
from skier import RUN_SPEED_PPS, Skier


class FinishLine:
    def __init__(self):
        self.game_finish = GameFinish()
        self.image = load_image('finish_line.png')
        self.frame_width = 2000
        self.frame_height = 247
        self.x = 0
        self.y = -1000
        self.skier = Skier()

    def draw(self):
        self.image.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += RUN_SPEED_PPS * game_framework.frame_time

    def get_bb(self):
        return self.x, self.y - 120, self.x + 1000, self.y - 50

    def handle_collision(self, group, other):
        match group:
            case 'skier:finishline':
                return self.game_finish
