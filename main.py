from pico2d import *
from mode import StartMenu, ModeSelect, NormalMode, InfinityMode, GameName

open_canvas(1500, 840)

start_menu = StartMenu()
mode_select = ModeSelect()
game_name = GameName()
current_mode = None

running = True
while running:
    clear_canvas()

    if current_mode is None:
        start_menu.draw()
<<<<<<< HEAD
        mode_select.draw()
        game_name.draw()
=======
>>>>>>> 2f4e555e5183f880f24ae8f74d8c4ad51bf70836

    if current_mode is not None:
        current_mode.update()
        current_mode.draw()

    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if current_mode is None:
                current_mode = mode_select.handle_event(event)
                # 게임 진행 화면으로 전환할 때 캔버스 크기 변경
                if current_mode is not None:
                    canvas_width, canvas_height = 1000, 1500
                    resize_canvas(canvas_width, canvas_height)
            else:
                current_mode.handle_event(event)

close_canvas()