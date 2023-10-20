from pico2d import load_image


class Skier:
    def __init__(self):
        self.x, self.y = 400, 600
        self.frame = 0
        self.dir = 0    # 오른쪽, 왼쪽 방향 구분 위해서
        self.image = load_image('skier.png')

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        pass