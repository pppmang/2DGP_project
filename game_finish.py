from pico2d import *

import game_framework
import server
from finish_line import FinishLine
# from background import InfinityMode
from mode import ModeSelect


class StartMenu:
    def __init__(self):
        self.image = load_image('start_menu_background.png')
        self.mode_select = ModeSelect()
        self.font = load_font('InkFree.TTF', 120)

    def draw(self):
        self.image.draw(750, 420)
        self.mode_select.draw()
        self.font.draw(800, 400, 'The SKI', (255, 255, 255))

    def update(self):
        pass


class GameFinish:
    def __init__(self, x=200, y=200):
        self.mode_select = ModeSelect()
        self.finish_UI = load_image('game_pop_up_UI.png')
        self.button_UI = load_image('game_button_UI.png')
        self.x, self.y = x, y
        self.font = load_font('GOTHICB.TTF', 55)

        self.menu_buttons = [
            {'button': 'PLAY_AGAIN', 'x': self.x - 125, 'y': self.y},
            {'button': 'HOME', 'x': self.x + 200, 'y': self.y}
        ]
        self.selected_button = None

    def update(self):
        # 화면 갱신 로직 작성
        pass

    def draw(self):
        self.finish_UI.draw(self.x, self.y)
        self.button_UI.draw(self.x, self.y)
        self.button_UI.draw(self.x + 310, self.y)

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
                        return StartMenu()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.skier.handle_event(event)


class NormalMode:
    def __init__(self):
        self.finish_line = FinishLine()

    def draw(self):
        server.skier.draw()  # Skier 그리기
        self.finish_line.draw()

    def update(self):
        server.skier.update()  # Skier 업데이트
        self.finish_line.update()

    def handle_event(self, event):
        server.skier.handle_event(event)  # Skier 이벤트 처리
