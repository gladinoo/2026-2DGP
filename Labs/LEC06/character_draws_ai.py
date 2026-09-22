import math
from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
boy = load_image('character.png')


def render(x, y):
    clear_canvas()
    grass.draw(400, 30)
    boy.draw(x, y)
    update_canvas()
    delay(0.01)
    get_events()


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
        render(x, 100)
    for i in range(101):
        t = i / 100
        x = (1 - t) * 700 + t * 400
        y = (1 - t) * 100 + t * 550
        render(x, y)
    for i in range(101):
        t = i / 100
        x = (1 - t) * 400 + t * 100
        y = (1 - t) * 550 + t * 100
        render(x, y)


while True:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()
