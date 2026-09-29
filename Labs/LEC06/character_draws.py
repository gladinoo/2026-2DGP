from pico2d import *
import math

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

LEFT_X, RIGHT_X = 50, 750
BOTTOM_Y, TOP_Y = 90, 550
CENTER_X, CENTER_Y = 400, 300
RADIUS = 200
FRAME_DELAY = 0.01
STEP_SIZE = 5

character = load_image('character.png')


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def draw_circle():
    print('CIRCLE')
    for deg in range(0, 360, STEP_SIZE):
        rad = math.radians(deg)
        x = CENTER_X + RADIUS * math.cos(rad)
        y = CENTER_Y + RADIUS * math.sin(rad)
        draw_character(x, y)
    pass


def draw_top():
    print('TOP')
    for x in range(LEFT_X, RIGHT_X + 1, STEP_SIZE):
        draw_character(x, TOP_Y)
    pass


def draw_right():
    print('RIGHT')
    for y in range(TOP_Y, BOTTOM_Y - 1, -STEP_SIZE):
        draw_character(RIGHT_X, y)
    pass


def draw_bottom():
    print('BOTTOM')
    for x in range(RIGHT_X, LEFT_X - 1, -STEP_SIZE):
        draw_character(x, BOTTOM_Y)
    pass


def draw_left():
    print('LEFT')
    for y in range(BOTTOM_Y, TOP_Y + 1, STEP_SIZE):
        draw_character(LEFT_X, y)
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
    for x in range(LEFT_X, RIGHT_X + 1, STEP_SIZE):
        draw_character(x, BOTTOM_Y)
    pass


def draw_triangle_right_up():
    print('TRIANGLE_RIGHT_UP')
    for t in range(0, 100 + 1, 1):
        x = RIGHT_X + (400 - RIGHT_X) * (t / 100)
        y = BOTTOM_Y + (TOP_Y - BOTTOM_Y) * (t / 100)
        draw_character(x, y)
    pass


def draw_triangle_left_down():
    print('TRIANGLE_LEFT_DOWN')
    for t in range(0, 100 + 1, 1):
        x = 400 + (LEFT_X - 400) * (t / 100)
        y = TOP_Y + (BOTTOM_Y - TOP_Y) * (t / 100)
        draw_character(x, y)
    pass


def draw_triangle():
    print('TRIANGLE')
    draw_triangle_bottom()
    draw_triangle_right_up()
    draw_triangle_left_down()
    pass


while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    pass

close_canvas()
