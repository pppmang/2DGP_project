import random

from pico2d import load_image

from obstacle import Rock, Tree, Flag
from skier import Skier


class StartMenu:
    def __init__(self):
        self.image = load_image('start_menu_background.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass


class ModeSelect:
    image = None

    def __init__(self, x = 400, y = 300): # 생성좌표 (400, 300), 속도는 1
        if ModeSelect.image == None:
            ModeSelect.image = load_image('mode_select_UI.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def text(self, param, param1, param2, param3):
        pass    # 아직 미완성.


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        self.obstacles = []

    def draw(self):
        self.image.draw(500, 750)
        for obstacle in self.obstacles:
            obstacle.draw()

    def update(self):
        self.y -= Skier.speed
        if self.y < -1500:  # 이미지가 화면 밖으로 나가면 다시 이미지가 위로 이동
            self.y = 0

        if random.random() < 0.01:
            obstacle_type = random.choice(["flag", "tree", "rock"])
            if obstacle_type == "flag":
                self.obstacles.append(Flag())
            elif obstacle_type == "tree":
                self.obstacles.append(Tree())
            elif obstacle_type == "rock":
                self.obstacles.append(Rock())

        for obstacle in self.obstacles:
            obstacle.update()
            # 화면에서 벗어난 장애물 제거
            if obstacle.y < -100:
                self.obstacles.remove(obstacle)
        pass
