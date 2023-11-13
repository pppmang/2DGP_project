from pico2d import *

from background import GameBackground, StartMenu, ModeSelect
import game_framework
import game_world

from skier import Skier

# 모드 선택 변수
selected_mode = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            skier.handle_event(event)


def init():
    global startmenu
    global gamebackground
    global skier



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
