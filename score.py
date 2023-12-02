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
        self.score = max(0, self.score)

    def obstacle_collision(self, obstacle_type):
        if obstacle_type == "flag":
            increase_value = random.randint(20, 100)
            self.increase_score(increase_value)
        elif obstacle_type == "tree":
            increase_value = random.randint(20, 50)
            self.increase_score(-increase_value)
        elif obstacle_type == "rock":
            increase_value = random.randint(30, 80)
            self.increase_score(-increase_value)

    def update(self):
        pass

    def draw(self):
        score_text = f"{self.score}"
        self.font.draw(500, 1400, score_text, (0, 0, 0))

    def get_score(self):
        return self.score