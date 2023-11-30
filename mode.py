from need import *


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
        self.skier = Skier()  # Skier 객체 생성
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
        self.life_count = 3  # 초기 플레이어 생명 개수
        self.skier = Skier()  # Skier 객체 생성
        self.game_finish = GameFinish()

    def draw(self):
        self.background.draw()

        for i in range(self.life_count):
            self.life_image.clip_draw(0, 0, 100, 122, 50 + i * 80, 1450)

    def update(self):
        self.background.update()

    def handle_collision(self, group, other):
        if group == 'skier:obstacle':
            self.life_count -= 1
            if self.life_count <= 0:
                return self.game_finish




