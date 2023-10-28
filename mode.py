from pico2d import *
from background import GameBackground, StartMenu, ModeSelect

# 모드 선택 변수
selected_mode = None


def mode_selection():
    global selected_mode
    global normal_modeselect
    global infinity_modeselect

    selected_mode = None

    while selected_mode is None:
        clear_canvas()
        StartMenu()
        normal_modeselect = ModeSelect(200, 300)
        normal_modeselect.text(200, 300, "Normal", (0, 0, 0))
        infinity_modeselect = ModeSelect(400,300)
        infinity_modeselect.text(400, 300, "Infinity", (0, 0, 0))


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
