import random
from pico2d import *


class Score:
    def __init__(self):
        self.score = 0
        self.final_score = 0
        self.font_score = load_font('impact.ttf', 36)
        self.font_final = load_font('impact.ttf', 150)


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
        self.font_score.draw(500, 1400, score_text, (0, 0, 0))

    def set_final_score(self):
        self.final_score = self.score

    def draw_final_score(self):
        final_score_text = f"{self.final_score}"  # 최종 점수를 출력
        self.font_final.draw(410, 1150, final_score_text, (255, 255, 255))
    def get_score(self):
        return self.score