import random
from pico2d import load_image, draw_rectangle

import game_framework
import server


class Flag:
    def __init__(self, obstacle_type):
        self.image = load_image('flag.png')
        self.frame_width = 70
        self.frame_height = 50
        self.frame_x = random.randint(0, 9) * self.frame_width
        self.frame_y = 0
        self.x = random.randint(50, 950)
        self.y = random.randint(-10000, 0)
        self.obstacle_type = obstacle_type

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
    def __init__(self, obstacle_type):
        self.image = load_image('tree.png')
        self.frame_width = 200
        self.frame_height = 240
        self.frame_x = random.randint(0, 2) * self.frame_width
        self.frame_y = random.randint(0, 1) * self.frame_height
        self.x = random.randint(50, 950)
        self.y = random.randint(-10000, 0)
        self.obstacle_type = obstacle_type

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


class Rock:
    def __init__(self, obstacle_type):
        self.image = load_image('rock.png')
        self.frame_width = 345
        self.frame_height = 344
        self.frame_x = random.randint(0, 3) * self.frame_width
        self.frame_y = 0
        self.x = random.randint(50, 950)
        self.y = random.randint(-10000, 0)
        self.obstacle_type = obstacle_type

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


class Obstacle:
    def __init__(self):
        self.obstacles = []
        self.num_obstacles = random.randint(50, 100)
        self.generate_obstacle()

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()


    def generate_obstacle(self):
        for _ in range(self.num_obstacles):
            new_obstacle = None
            obstacle_type = random.choice(["flag", "tree", "rock"])
            if obstacle_type == "flag":
                new_obstacle = Flag("flag")
            elif obstacle_type == "tree":
                new_obstacle = Tree("tree")
            elif obstacle_type == "rock":
                new_obstacle = Rock("rock")

            # 생성한 장애물을 리스트에 추가
            self.obstacles.append(new_obstacle)

        # 생성 후 장애물 개수 출력
        print("생성 후:", len(self.obstacles))

    def update(self):
        # 업데이트 전 장애물 개수 출력
        print("업데이트 전:", len(self.obstacles))

        for obstacle in self.obstacles:
            obstacle.update()
            # 화면에서 벗어난 장애물 제거
            if obstacle.y < -100:
                self.obstacles.remove(obstacle)

        # 업데이트 후 장애물 개수 출력
        print("업데이트 후:", len(self.obstacles))

    def check_collision(self, obstacle1, obstacle2):
        # 두 장애물 간의 충돌 여부 확인
        for o1 in obstacle1:
            for o2 in obstacle2:
                if (o1.x < o2.x + o2.frame_width and
                        o1.x + o1.frame_width > o2.x and
                        o1.y < o2.y + o2.frame_height and
                        o1.y + o1.frame_height > o2.y):
                    return True
        return False

    def get_bb(self):
        bounding_boxes = []
        for obstacle in self.obstacles:
            bounding_boxes.append(obstacle.get_bb())
        return bounding_boxes

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                for obstacle in self.obstacles:
                    obstacle.handle_collision('skier:obstacle', server.skier)
