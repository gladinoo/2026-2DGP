from pico2d import load_image, get_time, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_RIGHT, SDLK_LEFT
from transitions import Machine


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1  # 1: 우측 바라봄, -1: 좌측 바라봄
        self.dir = 0  # 1: 우측 이동, -1: 좌측 이동, 0: 정지
        self.image = load_image('animation_sheet.png')
        self.start_time = get_time()  # IDLE 상태 시작 시간 기록

        # transitions 라이브러리를 이용한 상태 머신 생성
        # IDLE, SLEEP, RUN 상태를 갖는다.
        self.machine = Machine(
            model=self,
            states=['IDLE', 'SLEEP', 'RUN'],
            initial='IDLE',
            auto_transitions=False,
        )

        # 상태 전이 규칙 정의
        # 1. IDLE -> SLEEP : 5초 경과 시 time_out 발생
        self.machine.add_transition('time_out', 'IDLE', 'SLEEP')
        # 2. SLEEP -> IDLE : SPACE 키 입력 시 space_down 발생
        self.machine.add_transition('space_down', 'SLEEP', 'IDLE')
        # 3. IDLE / SLEEP -> RUN : 방향키 입력 시 run 발생
        self.machine.add_transition('run', ['IDLE', 'SLEEP'], 'RUN')
        # 4. RUN -> IDLE : 방향키를 뗄 때 stop 발생
        self.machine.add_transition('stop', 'RUN', 'IDLE')

    def on_enter_IDLE(self):
        # IDLE 상태로 돌아올 때 5초 타이머를 다시 시작한다.
        self.start_time = get_time()

    def update(self):
        # 애니메이션 프레임 순환 (0~7 프레임)
        self.frame = (self.frame + 1) % 8

        # 상태별 동작
        if self.state == 'IDLE':
            # IDLE 상태에서 5초가 지나면 SLEEP 상태로 전이
            if get_time() - self.start_time > 5.0:
                self.time_out()
        elif self.state == 'SLEEP':
            pass
        elif self.state == 'RUN':
            # 이동 및 화면 밖으로 나가지 않도록 경계 제한
            self.x += self.dir * 5
            self.x = max(25, min(800 - 25, self.x))

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            # SLEEP 상태에서 SPACE 키를 누르면 IDLE 상태로 복귀
            if event.key == SDLK_SPACE:
                if self.state == 'SLEEP':
                    self.space_down()
            # 좌우 방향키를 누르면 RUN 상태로 전이 및 이동 방향 설정
            elif event.key == SDLK_RIGHT:
                self.dir += 1
                self.face_dir = 1
                if self.state in ['IDLE', 'SLEEP']:
                    self.run()
            elif event.key == SDLK_LEFT:
                self.dir -= 1
                self.face_dir = -1
                if self.state in ['IDLE', 'SLEEP']:
                    self.run()

        elif event.type == SDL_KEYUP:
            # 방향키를 떼면 방향값 갱신 및 정지 시 IDLE 상태로 복귀
            if event.key == SDLK_RIGHT:
                self.dir -= 1
                if self.dir == 0:
                    if self.state == 'RUN':
                        self.stop()
                elif self.dir == -1:
                    self.face_dir = -1
            elif event.key == SDLK_LEFT:
                self.dir += 1
                if self.dir == 0:
                    if self.state == 'RUN':
                        self.stop()
                elif self.dir == 1:
                    self.face_dir = 1

    def draw(self):
        if self.state == 'IDLE':
            # 서서 대기하는 모습
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        elif self.state == 'SLEEP':
            # 누워서 자는 모습 (90도 회전하여 출력)
            if self.face_dir == 1:
                self.image.clip_composite_draw(
                    self.frame * 100, 300, 100, 100,
                    3.141592 / 2, '',
                    self.x - 25, self.y - 25, 100, 100
                )
            else:
                self.image.clip_composite_draw(
                    self.frame * 100, 200, 100, 100,
                    -3.141592 / 2, '',
                    self.x + 25, self.y - 25, 100, 100
                )
        elif self.state == 'RUN':
            # 달리는 모습 (우측: y=100, 좌측: y=0)
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


if __name__ == '__main__':
    from pico2d import open_canvas, close_canvas, clear_canvas, update_canvas, delay, get_events, SDL_QUIT, SDLK_ESCAPE

    open_canvas()
    grass = load_image('grass.png')
    boy = Boy()

    running = True
    while running:
        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
            boy.handle_event(event)

        boy.update()

        clear_canvas()
        grass.draw(400, 30)
        boy.draw()
        update_canvas()
        delay(0.05)

    close_canvas()
