import math
from pico2d import *

# 캔버스 열기 (800 x 600 해상도)
open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')


def render(x, y):
    """현재 좌표에 캐릭터를 그리는 보조 함수"""
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    get_events()


def move_rectangle():
    print("[운동] 사각운동 시작")
    # 1. 하단 중앙 (400, 90) -> 우측 (750, 90)
    for x in range(400, 750 + 1, 5):
        render(x, 90)

    # 2. 우측 (750, 90) -> 상단 (750, 550)
    for y in range(90, 550 + 1, 5):
        render(750, y)

    # 3. 상단 (750, 550) -> 좌측 (50, 550)
    for x in range(750, 50 - 1, -5):
        render(x, 550)

    # 4. 좌측 (50, 550) -> 하단 (50, 90)
    for y in range(550, 90 - 1, -5):
        render(50, y)

    # 5. 하단 (50, 90) -> 중앙 (400, 90)
    for x in range(50, 400 + 1, 5):
        render(x, 90)


def move_triangle():
    print("[운동] 삼각운동 시작")
    # 1. 밑변 우측 이동: (400, 90) -> (750, 90)
    for x in range(400, 750 + 1, 5):
        render(x, 90)

    # 2. 빗변 상승: 우측 하단 (750, 90) -> 꼭짓점 (400, 550)
    for i in range(101):
        t = i / 100
        x = (1 - t) * 750 + t * 400
        y = (1 - t) * 90 + t * 550
        render(x, y)

    # 3. 빗변 하강: 꼭짓점 (400, 550) -> 좌측 하단 (50, 90)
    for i in range(101):
        t = i / 100
        x = (1 - t) * 400 + t * 50
        y = (1 - t) * 550 + t * 90
        render(x, y)

    # 4. 밑변 복귀: 좌측 하단 (50, 90) -> 중앙 (400, 90)
    for x in range(50, 400 + 1, 5):
        render(x, 90)


def move_circle():
    print("[운동] 원운동 시작")
    cx, cy, r = 400, 300, 210
    # 270도(하단)부터 시작하여 한 바퀴 회전
    for deg in range(270, 630 + 1, 3):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        render(x, y)


# 무한 반복 실행
while True:
    move_triangle()
    move_rectangle()
    move_circle()

close_canvas()