from pico2d import *

from background import GameBackground
import game_framework
from obstacle import FinishLine

from skier import Skier


class StartMenu:
    def __init__(self):
        self.image = load_image('start_menu_background.png')
        self.mode_select = ModeSelect()

    def draw(self):
        self.image.draw(750, 420)
        self.mode_select.draw()

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
        self.skier = Skier()    # Skier 객체 생성
        self.finish_line = FinishLine()

    def draw(self):
        self.background.draw()
        self.skier.draw()  # Skier 그리기
        self.finish_line.draw()

    def update(self):
        self.background.update()
        self.skier.update()  # Skier 업데이트
        self.finish_line.update()

    def handle_event(self, event):
        self.skier.handle_event(event)  # Skier 이벤트 처리


class InfinityMode:
    def __init__(self):
        self.background = GameBackground()
        self.life_image = load_image('life.png')
        self.life_count = 3     # 초기 플레이어 생명 개수
        self.skier = Skier()    # Skier 객체 생성

    def draw(self):
        self.background.draw()
        self.skier.draw()  # Skier 그리기

        for i in range(self.life_count):
            self.life_image.clip_draw(50 + i * 80, 1450)

    def update(self):
        self.background.update()
        self.skier.update()  # Skier 업데이트

    def handle_event(self, event):
        self.skier.handle_event(event)  # Skier 이벤트 처리


class GameFinish:
    def __init__(self, x=200, y=200):
        self.mode_select = ModeSelect()
        self.start_menu = StartMenu()
        self.finish_UI = load_image('game_pop_up_UI.png')
        self.button_UI = load_image('game_button_UI.png')
        self.x, self.y = x, y
        self.font =load_font('GOTHICB.TTF', 55)

        self.menu_buttons = [
            {'button': 'PLAY_AGAIN', 'x' : self.x -125, 'y' :self.y },
            {'button' : 'HOME', 'x' : self. x + 200, 'y' : self.y}
        ]
        self.selected_button = None

    def update(self):
        # 화면 갱신 로직 작성
        pass

    def draw(self):
        self.finish_UI.draw(self.x, self.y)
        self.button_UI.draw(self.x, self.y)
        self.button_UI.draw(self.x +310, self.y)

        for button in self.menu_buttons:
            self.font.draw(button['x'], button['y'], button['button'], (255, 255, 255))

    def handle_events(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            for button in self.menu_buttons:
                x, y = button['x'], button['y']

                if x - 30 < event.x < x + 250 and y + 570 < event.y < y + 690:
                    self.selected_button = button['button']

                    # 메뉴 선택 후 해당 화면으로 전환
                    if self.selected_button == 'PLAY_AGAIN':
                        return self.mode_select.selected_mode
                    elif self.selected_button == 'HOME':
                        return self.start_menu
