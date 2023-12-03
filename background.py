from pico2d import *

import game_framework
import server
from score import Score


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        self.cw = get_canvas_width()    # 화면의 너비
        self.ch = get_canvas_height()   # 화면의 높이
        self.w = self.image.w
        self.h = self.image.h
        self.score = Score()
        self.bg1_y = 0
        self.bg2_y = self.h

    def draw(self):
        int_window_left = int(self.window_left)
        int_bg1_y = int(self.bg1_y)
        self.image.clip_draw_to_origin(0, int_bg1_y, self.w, self.h - int_bg1_y, 0, 0)

        int_bg2_y = int(self.bg2_y)
        self.image.clip_draw_to_origin(0, 0, self.w, int_bg1_y, 0, self.h - int_bg1_y)

    def update(self):
        self.window_left = int(server.skier.x) - self.cw // 2
        self.window_left = clamp(0, self.window_left, self.w - self.cw)

        self.window_bottom = int(server.skier.y) - self.ch // 2
        self.window_bottom = clamp(0, self.window_bottom, self.h - self.ch * 2)

        self.score.increase_distance(server.skier.y)

        # 배경 스크롤
        self.bg1_y = (self.bg1_y - server.skier.speed * game_framework.frame_time) % self.h
        self.bg2_y = (self.bg1_y + self.ch) % self.h


