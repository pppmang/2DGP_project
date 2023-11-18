from pico2d import load_image, draw_rectangle
import random

from skier import Skier


class Flag:
    def __init__(self):
        self.image = load_image('flag.png')
        self.frame_width = 35
        self.frame_height = 50
        self.frame_x = random.randint(0, 10) * self.frame_width
        self.frame_y = 0
        self.x = random.randint(50, 950)
        self.y = random.randint(0, 50)
        self.skier = Skier()

    def draw(self):
        # 나무 크기 조정
        draw_width = int(self.frame_width * 1.2)
        draw_height = int(self.frame_height * 1.2)
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y, draw_width, draw_height)

    def update(self):
        self.y += self.skier.speed


class Tree:
    def __init__(self):
        self.image = load_image('tree.png')
        self.frame_width = 200
        self.frame_height = 240
        self.frame_x = random.randint(0, 3) * self.frame_width
        self.frame_y = random.randint(0, 2) * self.frame_height
        self.x = random.randint(50, 950)
        self.y = random.randint(0, 50)
        self.skier = Skier()

    def draw(self):
        # 나무 크기 조정
        draw_width = int(self.frame_width * 0.5)
        draw_height = int(self.frame_height * 0.5)
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y, draw_width, draw_height)

    def update(self):
        self.y += self.skier.speed


class Rock:
    def __init__(self):
        self.image = load_image('rock.png')
        self.frame_width = 345
        self.frame_height = 344
        self.frame_x = random.randint(0, 4) * self.frame_width
        self.frame_y = 0
        self.x = random.randint(50, 950)
        self.y = random.randint(0, 50)
        self.skier = Skier()

    def draw(self):
        # 돌 크기 조정
        draw_width = int(self.frame_width * 0.3)
        draw_height = int(self.frame_height * 0.3)
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y, draw_width, draw_height)

    def update(self):
        self.y += self.skier.speed


class FinishLine:
    def __init__(self):
        self.image = load_image('finish_line.png')
        self.frame_width = 2000
        self.frame_height = 247
        self.x = 0
        self.y = -100
        self.skier = Skier()

    def draw(self):
        self.image.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.skier.speed

    def get_bb(self):
        return self.x, self.y - 120, self.x + 1000, self.y - 50
