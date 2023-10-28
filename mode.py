from pico2d import *
from background import GameBackground, StartMenu

# # 모드 선택 변수
# selected_mode = None
#
# def mode_selection():
#     global selected_mode
#     selected_mode = None
#
#     while selected_mode is None:
#         clear_canvas()
#         StartMenu()






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
