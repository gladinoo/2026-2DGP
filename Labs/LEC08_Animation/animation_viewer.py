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

# 2. 걷기 동작 (WALK): 6개 프레임, 프레임별 크기가 다른 복잡한 구조
WALK_FRAMES = (
    (0, 200, 95, 100),
    (95, 200, 105, 100),
    (200, 200, 100, 102),
    (300, 200, 98, 98),
    (398, 200, 104, 100),
    (502, 200, 100, 100),
)

# 3. 달리기 동작 (RUN): 8개 프레임, 프레임별 크기가 다른 복잡한 구조
RUN_FRAMES = (
    (0, 100, 100, 100),
    (100, 100, 105, 100),
    (205, 100, 110, 100),
    (315, 100, 95, 100),
    (410, 100, 102, 100),
    (512, 100, 108, 100),
    (620, 100, 95, 100),
    (715, 100, 100, 100),
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


# IDLE 액션 프레임 순환 재생
for frame_data in IDLE_FRAMES:
    clear_canvas()
    grass.draw(400, 30)
    draw_frame(frame_data)
    update_canvas()
    handle_events()
    delay(0.1)

# WALK 액션 프레임 순환 재생
for frame_data in WALK_FRAMES:
    clear_canvas()
    grass.draw(400, 30)
    draw_frame(frame_data)
    update_canvas()
    handle_events()
    delay(0.1)

# RUN 액션 프레임 순환 재생
for frame_data in RUN_FRAMES:
    clear_canvas()
    grass.draw(400, 30)
    draw_frame(frame_data)
    update_canvas()
    handle_events()
    delay(0.08)

close_canvas()
