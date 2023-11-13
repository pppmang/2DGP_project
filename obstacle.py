from pico2d import load_image
import random

from skier import Skier


class Flag:
    def __init__(self):
        self.image = load_image('flag.png')
        self.frame_width = 35
        self.frame_height = 50
        self.frame_x = random.randint(0, 10) * self.frame_width
        self.frame_y = self.frame_height
        self.x = random.randint(50, 950)
        self.y = random.randint(30, 1400)

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y)

    def update(self):
        self.y -= Skier.speed


class Tree:
    def __init__(self):
        self.image = load_image('tree.png')
        self.frame_width = 200
        self.frame_height = 240
        self.frame_x = random.randint(0, 4) * self.frame_width
        self.frame_y = random.randint(0, 2) * self.frame_height
        self.x = random.randint(50, 950)
        self.y = random.randint(30, 1400)

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y)

    def update(self):
        self.y -= Skier.speed


class Rock:
    def __init__(self):
        self.image = load_image('rock.png')
        self.frame_width = 345
        self.frame_height = 344
        self.frame_x = random.randint(0, 4) * self.frame_width
        self.frame_y = self.frame_height
        self.x = random.randint(50, 950)
        self.y = random.randint(30, 1400)

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y)

    def update(self):
        self.y -= Skier.speed