"""
과제 #2. AI로 개발
소스코드 이름: character_draws_ai.py
채점 기준: 완성된 코드가 정확히 실행되면 1점

기능:
- 원운동 (run_circle)
- 사각운동 (run_rectangle)
- 삼각운동 (run_triangle)
- 세 운동의 순차적 무한 반복
"""
import math
from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
boy = load_image('character.png')


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()


def render(x, y):
    clear_canvas()
    grass.draw(400, 30)
    boy.draw(x, y)
    update_canvas()
    handle_events()
    delay(0.01)


def run_circle():
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 4):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        render(x, y)


def run_rectangle():
    for x in range(50, 750 + 1, 8):
        render(x, 90)
    for y in range(90, 550 + 1, 8):
        render(750, y)
    for x in range(750, 50 - 1, -8):
        render(x, 550)
    for y in range(550, 90 - 1, -8):
        render(50, y)


def run_triangle():
    for x in range(100, 700 + 1, 8):
        render(x, 90)
    for i in range(101):
        t = i / 100
        x = (1 - t) * 700 + t * 400
        y = (1 - t) * 90 + t * 550
        render(x, y)
    for i in range(101):
        t = i / 100
        x = (1 - t) * 400 + t * 100
        y = (1 - t) * 550 + t * 90
        render(x, y)


while True:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()
