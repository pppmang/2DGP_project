from pico2d import load_image

from skier import Skier


class StartMenu:
    def __init__(self):
        self.image = load_image('start_menu_background.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')

    def draw(self):
        self.image.draw(500, 750)

    def update(self):
        # self.y -= Skier.speed
        # if self.y < -1500:  # 이미지가 화면 밖으로 나가면 다시 이미지가 위로 이동
        #     self.y = 0
        pass
