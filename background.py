import random

from pico2d import load_image

from obstacle import Rock, Tree, Flag
from skier import Skier


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        self.obstacles = []
        self.y = 0
        self.skier = Skier()

    def draw(self):
        image_height = self.image.h
        self.image.draw(500, 750 - self.y)
        if self.y > 0:
            self.image.draw(500, 750 - self.y + image_height)
        for obstacle in self.obstacles:
            obstacle.draw()

    def generate_obstacle(self):
        obstacle_type = random.choice(["flag", "tree", "rock"])
        if obstacle_type == "flag":
            return Flag()
        elif obstacle_type == "tree":
            return Tree()
        elif obstacle_type == "rock":
            return Rock()

    def update(self):
        self.y -= self.skier.speed
        if self.y < 0:  # 이미지가 화면 밖으로 나가면 다시 이미지가 위로 이동
            self.y = 1500

        if random.random() < 0.007:
            new_obstacle = self.generate_obstacle()
            # 새로운 장애물이 이미 생성된 장애물들과 겹치지 않도록 확인
            while any(self.check_collision(new_obstacle, existing_obstacle) for existing_obstacle in self.obstacles):
                new_obstacle = self.generate_obstacle()

            self.obstacles.append(new_obstacle)

        for obstacle in self.obstacles:
            obstacle.update()
            # 화면에서 벗어난 장애물 제거
            if obstacle.y < -100:
                self.obstacles.remove(obstacle)
                pass

    def check_collision(self, obstacle1, obstacle2):
        # 두 장애물 간의 충돌 여부 확인
        if (obstacle1.x < obstacle2.x + obstacle2.frame_width and
                obstacle1.x + obstacle1.frame_width > obstacle2.x and
                obstacle1.y < obstacle2.y + obstacle2.frame_height and
                obstacle1.y + obstacle1.frame_height > obstacle2.y):
            return True
        return False
