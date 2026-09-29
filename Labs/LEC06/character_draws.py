from pico2d import *
import math

open_canvas()

character = load_image('character.png')


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def draw_circle():
    print('CIRCLE')
    for deg in range(0, 360, 5):
        rad = math.radians(deg)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        draw_character(x, y)
    pass


def draw_top():
    print('TOP')
    for x in range(50, 750 + 1, 5):
        draw_character(x, 550)
    pass


def draw_right():
    print('RIGHT')
    for y in range(550, 90 - 1, -5):
        draw_character(750, y)
    pass


def draw_bottom():
    print('BOTTOM')
    for x in range(750, 50 - 1, -5):
        draw_character(x, 90)
    pass


def draw_left():
    print('LEFT')
    for y in range(90, 550 + 1, 5):
        draw_character(50, y)
    pass


def draw_rectangle():
    print('RECTANGLE')
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass



def draw_triangle_bottom():
    print('TRIANGLE_BOTTOM')
    for x in range(50, 750 + 1, 5):
        draw_character(x, 90)
    pass


def draw_triangle_right_up():
    print('TRIANGLE_RIGHT_UP')
    for t in range(0, 100 + 1, 1):
        x = 750 + (400 - 750) * (t / 100)
        y = 90 + (550 - 90) * (t / 100)
        draw_character(x, y)
    pass


def draw_triangle():
    print('TRIANGLE')
    draw_triangle_bottom()
    draw_triangle_right_up()
    pass


while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    break
    pass

close_canvas()
