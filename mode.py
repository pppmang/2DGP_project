from pico2d import load_image
from background import GameBackground


class NormalMode:
    def __init__(self):
        self.background = GameBackground()

    def draw(self):
        self.background.draw()

    def update(self):
        pass


class InfinityMode:
    def __init__(self):
        self.background = GameBackground()

    def draw(self):
        self.background.draw()

    def update(self):
        pass
