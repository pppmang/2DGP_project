from pico2d import load_image, SDL_KEYDOWN, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


class Skier:
    def __init__(self):
        self.x, self.y = 400, 600
        self.frame = 0
        self.dir = 0    # 오른쪽, 왼쪽 방향 구분 위해서 ( 오른쪽 : 1, 왼쪽 : -1)
        self.image = load_image('skier.png')

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def draw(self):
        pass