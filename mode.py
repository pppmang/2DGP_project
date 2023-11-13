from pico2d import *

from background import GameBackground
import game_framework
import game_world

from skier import Skier


class StartMenu:
    def __init__(self):
        self.image = load_image('start_menu_background.png')

    def draw(self):
        self.image.draw(750, 420)

    def update(self):
        pass


class ModeSelect:
    image = None

    def __init__(self, x = 200, y = 100):
        if self.image is None:
            self.image = load_image('mode_select_UI.png')
        self.x, self.y = x, y
        self.font = load_font('GOTHICB.TTF', 55)

        self.mode_buttons = [
            {'mode': 'NORMAL', 'x': self.x - 125, 'y': self.y + 5},
            {'mode': 'INFINITY', 'x': self.x + 200, 'y': self.y + 5}
        ]
        self.selected_mode = None

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 310, self.y)

        for button in self.mode_buttons:
            self.font.draw(button['x'], button['y'], button['mode'], (255, 255, 255))

    def update(self):
        pass

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            for button in self.mode_buttons:
                x, y = button['x'], button['y']

                if x - 30 < event.x < x + 250 and y + 570 < event.y < y + 690:
                    self.selected_mode = button['mode']

                    # 모드 선택 후 해당 모드로 화면 전환
                    if self.selected_mode == 'NORMAL':
                        return NormalMode()
                    elif self.selected_mode == 'INFINITY':
                        return InfinityMode()


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


class NormalMode:
    def __init__(self):
        self.background = GameBackground()

    def draw(self):
        self.background.draw()

    def update(self):
        pass

    def handle_event(self, event):
        pass


class InfinityMode:
    def __init__(self):
        self.background = GameBackground()
        self.life_image = load_image('life.png')
        self.life_count = 3     # 초기 플레이어 생명 개수

    def draw(self):
        self.background.draw()

        for i in range(self.life_count):
            self.life_image.draw(50 + i * 80, 1450)

    def update(self):
        pass

    def handle_event(self, event):
        pass