from pico2d import *
from mode import StartMenu, ModeSelect, NormalMode, InfinityMode

open_canvas(1500, 840)

start_menu = StartMenu()
mode_select = ModeSelect()
current_mode = None

running = True
while running:
    clear_canvas()

    start_menu.draw()
    mode_select.draw()

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
            else:
                current_mode.handle_event(event)

close_canvas()