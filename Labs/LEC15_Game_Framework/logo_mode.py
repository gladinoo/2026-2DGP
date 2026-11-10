from pico2d import (
    load_image, get_time, clear_canvas, update_canvas, get_events,
    open_canvas, close_canvas
)
import game_framework

image = None
logo_start_time = 0.0


def init():
    global image, logo_start_time
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()


def finish():
    global image
    del image


def update():
    global logo_start_time
    # 2초가 지나면 타이틀 모드로 전환 (title_mode가 없으면 게임 종료)
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        try:
            import title_mode
            game_framework.change_mode(title_mode)
        except ImportError:
            game_framework.quit()


def render():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def draw():
    """슬라이드 호환용 render 별칭"""
    render()


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass


# 단독 실행 테스트 (python logo_mode.py)
if __name__ == '__main__':
    open_canvas()
    import logo_mode
    game_framework.run(logo_mode)
    close_canvas()

