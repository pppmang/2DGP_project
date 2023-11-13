from pico2d import *
from obstacle import Rock, Tree, Flag
from background import StartMenu, ModeSelect, GameBackground

open_canvas(1000, 1500)


start_background = StartMenu()
mode_select = ModeSelect()
game_background = GameBackground()
rock = Rock()
tree = Tree()
flag = Flag()


while True:
    clear_canvas()

    game_background.draw()

    update_canvas()
    delay(0.01)


close_canvas()



