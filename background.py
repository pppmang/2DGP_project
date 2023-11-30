from need import *


class GameBackground:
    def __init__(self):
        self.image = load_image('game_background.png')
        self.obstacle = Obstacle()
        self.y = 0
        self.skier = Skier()
        self.score = Score()

    def draw(self):
        image_height = self.image.h
        self.image.clip_draw(0, 0, 1000, 1500, 500, 750 - self.y)
        if self.y > 0:
            self.image.clip_draw(0, 0, 1000, 1500, 500, 750 - self.y + image_height)
        self.obstacle.draw()

    def update(self):
        self.y -= RUN_SPEED_PPS * game_framework.frame_time
        if self.y < 0:  # 이미지가 화면 밖으로 나가면 다시 이미지가 위로 이동
            self.y = 1500

        self.obstacle.update()
        self.score.increase_distance(RUN_SPEED_PPS * game_framework.frame_time)  # 수정된 부분

    def check_collision(self, obstacle1, obstacle2):
        self.obstacle.check_collision(obstacle1, obstacle2)
