import random
from pico2d import *


class Score:
    def __init__(self):
        self.score = 0
        self.font = load_font('impact.ttf', 36)

    def increase_distance(self, value):
        if value % 5 == 0:
            self.increase_score(30)

    def increase_score(self, value):
        self.score += value

    def obstacle_collision(self, obstacle_type):
        if obstacle_type == "flag":
            self.score += random.randint(20, 100)
        elif obstacle_type == "tree":
            self.score -= random.randint(20, 50)
        elif obstacle_type == "rock":
            self.score -= random.randint(30, 80)

    def update(self):
        pass

    def draw(self):
        score_text = f"{self.score}"
        self.font.draw(500, 1400, score_text, (0, 0, 0))

    def get_score(self):
        return self.score