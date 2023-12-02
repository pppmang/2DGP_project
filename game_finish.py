from pico2d import load_image, load_font, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT

from selecting_mode import ModeSelect, StartMenu


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
