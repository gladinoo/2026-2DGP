from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

CENTER_X, CENTER_Y = 400, 300
SCALE = 3.2


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()


close_canvas()
