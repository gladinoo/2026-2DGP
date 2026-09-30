from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

CENTER_X, CENTER_Y = 400, 300
SCALE = 3.2

# 1. 대기 동작 (IDLE): 4개 프레임, 프레임별 크기가 다른 복잡한 구조
IDLE_FRAMES = (
    (0, 300, 100, 100),
    (100, 300, 102, 100),
    (202, 300, 98, 100),
    (300, 300, 100, 100),
)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()


def draw_frame(frame_data):
    left, bottom, width, height = frame_data
    character.clip_draw(
        left, bottom, width, height,
        CENTER_X, CENTER_Y,
        int(width * SCALE), int(height * SCALE)
    )


# 단일 프레임 렌더링 테스트
clear_canvas()
grass.draw(400, 30)
draw_frame(IDLE_FRAMES[0])
update_canvas()
delay(0.5)

close_canvas()
