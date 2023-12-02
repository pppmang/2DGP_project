from pico2d import *
import game_framework
import server
from finish_line import FinishLine
from game_finish import GameFinish
from skier import WinningPose


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
        if isinstance(server.skier.state_machine.cur_state, WinningPose):
            return GameFinish()







