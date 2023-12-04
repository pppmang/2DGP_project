from pico2d import *

import game_framework
from score import Score
import server
from obstacle import Obstacle
from state import RUN_SPEED_PPS


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        self.obstacle = Obstacle()
        self.y = 0
        self.bgm = load_music('background_music.mp3')
        self.bgm.set_volume(30)
        self.bgm.repeat_play()

    def draw(self):
        image_height = self.image.h
        self.image.draw(500, 750 - self.y)
        if self.y > 0:
            self.image.draw(500, 750 - self.y + image_height)
        self.obstacle.draw()

    def update(self):
        server.score.increase_distance(self.y)

        self.y -= server.skier.speed * game_framework.frame_time
        if self.y < 0:  # 이미지가 화면 밖으로 나가면 다시 이미지가 위로 이동
            self.y = 1500

        self.obstacle.update()

    def check_collision(self, obstacle1, obstacle2):
        self.obstacle.check_collision(obstacle1, obstacle2)


class ModeSelect:
    image = None

    def __init__(self, x=200, y=100):
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
    def __init__(self, x=500, y=1000):
        self.frame_height = 254
        self.frame_width = 505
        server.skier.speed = 0
        self.mode_select = ModeSelect()
        self.finish_UI = load_image('game_pop_up_UI.png')
        self.button_UI = load_image('game_button_UI.png')
        self.x, self.y = x, y
        self.font = load_font('impact.TTF', 55)

        self.menu_buttons = [
            {'button': 'P L A Y A G A I N', 'x': self.x - 160, 'y': self.y - 100},
            {'button': 'H   O   M   E', 'x': self.x - 105, 'y': self.y - 270}
        ]
        self.selected_button = None

    def update(self):
        pass

    def draw(self):
        draw_width = int(self.frame_width * 1.0)
        draw_height = int(self.frame_height * 0.6)

        self.finish_UI.draw(self.x, self.y)
        self.button_UI.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, self.y - 100, draw_width,
                                 draw_height)
        self.button_UI.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, self.y - 270, draw_width,
                                 draw_height)

        for button in self.menu_buttons:
            self.font.draw(button['x'], button['y'], button['button'], (255, 255, 255))

    def handle_event(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            for button in self.menu_buttons:
                x, y = button['x'], button['y']

                if x - 30 < event.x < x + 250 and y - 100 < event.y < y + 300:
                    self.selected_button = button['button']

                    # 메뉴 선택 후 해당 화면으로 전환
                    if self.selected_button == 'P L A Y A G A I N':
                        print('PLAY_AGAIN')
                        # return self.mode_select.selected_mode
                    elif self.selected_button == 'H   O   M   E':
                        print('HOME')
                        # return StartMenu()


# def handle_events():
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             game_framework.quit()
#         else:
#             server.skier.handle_event(event)


class NormalMode:
    def __init__(self):
        pass

    def draw(self):
        server.skier.draw()  # Skier 그리기
        server.finish_line.draw()

    def update(self):
        server.skier.update()  # Skier 업데이트
        server.finish_line.update()

    def handle_event(self, event):
        server.skier.handle_event(event)  # Skier 이벤트 처리


class FinishLine:
    def __init__(self):
        self.image = load_image('finish_line.png')
        self.frame_width = 2000
        self.frame_height = 247
        self.x = 0
        self.y = -50

    def draw(self):
        self.image.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x, self.y - 120, self.x + 1000, self.y - 50

    def handle_collision(self, group, other):
        match group:
            case 'skier:finishline':
                pass


class InfinityMode:
    def __init__(self):
        self.life_image = load_image('life.png')
        self.life_count = 3  # 초기 플레이어 생명 개수

    def draw(self):
        server.background.draw()

        for i in range(self.life_count):
            self.life_image.clip_draw(0, 0, 100, 122, 50 + i * 80, 1450)

    def update(self):
        server.background.update()

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle' if other.type in ['rock', 'tree']:
                self.life_count -= 1
                if self.life_count <= 0:
                    server.game_finish()
