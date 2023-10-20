from pico2d import load_image


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
        self.image.draw(400, 300)

    def update(self):
        pass
