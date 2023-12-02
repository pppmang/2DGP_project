from pico2d import *
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

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)

    def update(self):
        self.window_left = int(server.skier.x) - self.cw // 2
        self.window_bottom = int(server.skier.y) - self.ch // 2

        self.window_left = clamp(0, self.window_left, self.w - self.cw - 1)
        self.window_bottom = clamp(0, self.window_bottom, self.h - self.ch - 1)
        self.score.increase_distance(server.skier.y)


