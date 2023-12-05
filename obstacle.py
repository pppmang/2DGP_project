import random
from pico2d import load_image, draw_rectangle

import game_framework
import game_world
import server


class Flag:
    def __init__(self, obstacle_type):
        self.instance = self
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
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                server.score.obstacle_collision(obstacle_type="flag")
                if game_world.is_collision_object(self.instance):
                    game_world.remove_collision_object(self.instance)



class Tree:
    def __init__(self, obstacle_type):
        self.instance = self
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
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 45, self.y - 55, self.x + 45, self.y + 55

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                server.score.obstacle_collision(obstacle_type="tree")
                if game_world.is_collision_object(self.instance):
                    game_world.remove_collision_object(self.instance)


class Rock:
    def __init__(self, obstacle_type):
        self.instance = self
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
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.y += server.skier.speed * game_framework.frame_time

    def get_bb(self):
        return self.x - 50, self.y - 25, self.x + 50, self.y + 25

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                server.score.obstacle_collision(obstacle_type="rock")
                if game_world.is_collision_object(self.instance):
                    game_world.remove_collision_object(self.instance)


class Obstacle:
    def __init__(self):
        self.obstacle_type = random.choice(["flag", "tree", "rock"])
        if self.obstacle_type == "flag":
            self.instance = Flag(self.obstacle_type)
        elif self.obstacle_type == "tree":
            self.instance = Tree(self.obstacle_type)
        elif self.obstacle_type == "rock":
            self.instance = Rock(self.obstacle_type)

    def draw(self):
        self.instance.draw()

    def update(self):
        self.instance.update()

    def get_bb(self):
        return self.instance.get_bb()

    def handle_collision(self, group, other):
        match group:
            case 'skier:obstacle':
                self.instance.handle_collision('skier:obstacle', server.skier)

