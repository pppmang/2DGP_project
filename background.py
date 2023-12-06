from pico2d import *

import game_framework
import game_world
from skier import Idle
import title_mode
from game_world import collide
import server


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        # self.obstacle = Obstacle()
        self.y = 0
        self.bgm = load_music('background_music.mp3')
        self.bgm.set_volume(25)
        self.bgm.repeat_play()

    def draw(self):
        image_height = self.image.h
        self.image.draw(500, 750 - self.y)
        if self.y > 0:
            self.image.draw(500, 750 - self.y + image_height)
        # self.obstacle.draw()

    def update(self):
        server.score.increase_distance(self.y)
        self.y -= server.skier.speed * game_framework.frame_time

        if self.y < 0:  # 이미지가 화면 밖으로 나가면 다시 이미지가 위로 이동
            self.y = 1500
        # self.obstacle.update()

    def stop_music(self):
        self.bgm.stop()

    def handle_collision(self, group, other):
        pass


class Life:
    def __init__(self, x, y):
        self.image = load_image('life.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass


class InfinityMode:
    def __init__(self):
        self.background = GameBackground()
        self.life1 = Life(50, 1450)
        self.life2 = Life(130, 1450)
        self.life3 = Life(210, 1450)
        self.lives = [self.life1, self.life2, self.life3]
        self.life_count = 3  # 초기 플레이어 생명 개수

    def draw(self):
        self.background.draw()

        for life in self.lives[:self.life_count]:
            life.draw()

    def update(self):
        self.background.update()

    def remove_life_image(self):
        if self.life_count > 0:
            self.life_count -= 1
            if self.life_count > 0:
                removed_life = self.lives[self.life_count]
                if removed_life in game_world.objects[3]:
                    game_world.remove_object(removed_life)
            elif self.life_count == 0:
                server.game_finish.state = 'draw'

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        if group == 'skier:obstacle':
            obstacle = other.instance
            obstacle_type = obstacle.obstacle_type

            if obstacle_type in ["tree", "rock"]:
                self.remove_life_image()


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
                    StartMenu.start_menu_sound.set_volume(0)

                    # 모드 선택 후 해당 모드로 화면 전환
                    if self.selected_mode == 'NORMAL':
                        return NormalMode()
                    elif self.selected_mode == 'INFINITY':
                        return InfinityMode()


class StartMenu:
    start_menu_sound = None

    def __init__(self):
        self.image = load_image('start_menu_background.png')
        self.mode_select = ModeSelect()
        self.font = load_font('InkFree.TTF', 200)
        if not StartMenu.start_menu_sound:
            StartMenu.start_menu_sound = load_wav('startmenu_music.wav')
            StartMenu.start_menu_sound.set_volume(80)
            StartMenu.start_menu_sound.play()

    def draw(self):
        self.image.draw(750, 420)
        self.mode_select.draw()
        # self.font.draw(590, 610, 'The SKI', (51, 0, 153))
        self.font.draw(600, 600, 'The SKI', (153, 204, 255))
        self.font.draw(610, 590, 'The SKI', (255, 255, 255))

    def update(self):
        pass


class GameFinish:
    def __init__(self, x=500, y=1000):
        self.frame_height = 254
        self.frame_width = 505
        self.mode_select = ModeSelect()
        self.finish_UI = load_image('game_pop_up_UI.png')
        self.button_UI = load_image('game_button_UI.png')
        self.x, self.y = x, y
        self.font_size_main = 55  # 기존 텍스트의 크기
        self.font_size_score = 300  # 점수 텍스트의 크기
        self.font_main = load_font('impact.TTF', self.font_size_main)
        self.font_score = load_font('impact.TTF', self.font_size_score)
        self.state = 'hide'

        # self.menu_buttons = [
        #     {'button': 'P L A Y A G A I N', 'x': 340, 'y': 900},
        #     {'button': 'H      O        M      E', 'x': 340, 'y': 730}
        # ]
        # self.selected_button = None

    def update(self):
        pass

    def draw(self):
        if self.state == 'draw':
            draw_width = int(self.frame_width * 1.0)
            draw_height = int(self.frame_height * 0.6)

            self.finish_UI.draw(self.x, self.y)
            # for button in self.menu_buttons:
            #     self.button_UI.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, button['y'], draw_width,
            #                              draw_height)
            #     self.font_main.draw(button['x'], button['y'], button['button'], (255, 255, 255))

            if server.mode == 'normal_mode' and collide(server.finish_line, server.skier):
                server.score.set_final_score()  # 최종 점수를 설정

            elif server.mode == 'infinity_mode' and server.infinity.life_count == 0:
                server.score.set_final_score()

            server.score.draw_final_score()

    def handle_event(self, event):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

        # if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
        #     for button in self.menu_buttons:
        #         button_x, button_y = self.x + button['x'], self.y - button['y']
        #
        #         if button_x - 570 < event.x < button_x - 120 and button_y + 430 < event.y < button_y + 540:
        #             self.selected_button = button['button']
        #
        #         if self.selected_button is not None:
        #             self.state = 'hide'
        #             # 메뉴 선택 후 해당 화면으로 전환
        #             if self.selected_button == 'P L A Y A G A I N':
        #                 game_framework.restart_current_mode()
        #             elif self.selected_button == 'H      O        M      E':
        #                 game_framework.change_mode(title_mode)
        #                 if server.mode == 'normal_mode':
        #                     server.background.stop_music()  # 음악 중지 추가
        #                 elif server.mode == 'infinity_mode':
        #                     server.infinity.stop.music()
        #                 StartMenu.start_menu_sound.set_volume(80)


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
        self.y = -10000

    def draw(self):
        self.image.clip_draw(0, 0, self.frame_width, self.frame_height, self.x, self.y)

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x, self.y - 120, self.x + 1000, self.y - 50

    def handle_collision(self, group, other):
        match group:
            case 'skier:finishline':
                pass



