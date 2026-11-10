from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()


frame = 0

# 4개 동작(action: 0, 1, 2, 3)을 순차적으로 무한 반복
while True:
    for action in range(4):
        # 오른쪽 달리기
        for x in range(5, 750, 5):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(
                frame * 100, action * 100,
                100, 100,
                x, 90
            )
            update_canvas()
            handle_events()
            frame = (frame + 1) % 8
            delay(0.05)

        # 왼쪽 달리기
        for x in range(750, 5, -5):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_composite_draw(
                frame * 100, action * 100,
                100, 100,
                0, 'h',
                x, 90,
                100, 100
            )
            update_canvas()
            handle_events()
            frame = (frame + 1) % 8
            delay(0.05)

close_canvas()
