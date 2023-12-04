import random
from pico2d import load_image, draw_rectangle

import game_framework
import server


class Flag:
    def __init__(self):
        self.image = load_image('flag.png')
        self.frame_width = 70
        self.frame_height = 50
        self.frame_x = random.randint(0, 9) * self.frame_width
        self.frame_y = 0
        self.x = random.randint(50, 950)
        self.y = random.randint(0, 50)

    def draw(self):
        # 깃발 크기 조정
        draw_width = int(self.frame_width * 1.2)
        draw_height = int(self.frame_height * 1.2)
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y,
                             draw_width, draw_height)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                server.score.obstacle_collision(obstacle_type="flag")


class Tree:
    def __init__(self):
        self.image = load_image('tree.png')
        self.frame_width = 200
        self.frame_height = 240
        self.frame_x = random.randint(0, 2) * self.frame_width
        self.frame_y = random.randint(0, 1) * self.frame_height
        self.x = random.randint(50, 950)
        self.y = random.randint(0, 50)

    def draw(self):
        # 나무 크기 조정
        draw_width = int(self.frame_width * 0.5)
        draw_height = int(self.frame_height * 0.5)
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y,
                             draw_width, draw_height)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 50, self.y - 60, self.x + 50, self.y + 60

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                server.score.obstacle_collision(obstacle_type="tree")
                server.skier.state_machine.handle_event(('TIME_OUT', 0))


class Rock:
    def __init__(self):
        self.image = load_image('rock.png')
        self.frame_width = 345
        self.frame_height = 344
        self.frame_x = random.randint(0, 3) * self.frame_width
        self.frame_y = 0
        self.x = random.randint(50, 950)
        self.y = random.randint(0, 50)

    def draw(self):
        # 돌 크기 조정
        draw_width = int(self.frame_width * 0.3)
        draw_height = int(self.frame_height * 0.3)
        self.image.clip_draw(self.frame_x, self.frame_y, self.frame_width, self.frame_height, self.x, self.y,
                             draw_width, draw_height)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 50, self.y - 30, self.x + 50, self.y + 30

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                server.score.obstacle_collision(obstacle_type="rock")
                server.skier.state_machine.handle_event(('TIME_OUT', 0))


class Obstacle:
    def __init__(self):
        self.obstacles = []
        self.obstacle_type = None

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()

    def generate_obstacle(self):
        self.obstacle_type = random.choice(["flag", "tree", "rock"])
        if self.obstacle_type == "flag":
            return Flag()
        elif self.obstacle_type == "tree":
            return Tree()
        elif self.obstacle_type == "rock":
            return Rock()

    def update(self):
        if random.random() < 0.005:
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

    def check_collision(self, obstacle1, obstacle2):
        # 두 장애물 간의 충돌 여부 확인
        if (obstacle1.x < obstacle2.x + obstacle2.frame_width and
                obstacle1.x + obstacle1.frame_width > obstacle2.x and
                obstacle1.y < obstacle2.y + obstacle2.frame_height and
                obstacle1.y + obstacle1.frame_height > obstacle2.y):
            return True
        return False

    def get_bb(self):
        for obstacle in self.obstacles:
            return obstacle.get_bb()

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                for obstacle in self.obstacles:
                    obstacle.handle_collision()
