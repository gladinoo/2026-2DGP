# 🌐 Lecture 14: 게임 월드(Game World) 완벽 대비 가이드

인터넷이 차단된 상태에서도 바로 참고하여 과제와 실습을 막힘없이 해결할 수 있도록 핵심 개념, 구조, 코드 패턴 및 예상 과제 구현을 총정리한 문서입니다.

---

## 1. 핵심 아키텍처: 왜 `game_world` 모듈인가?

기존 방식에서는 `main.py`에 모든 객체 리스트(`world = []`)를 두고 관리했습니다. 이 경우 소년(`Boy`)이 축구공(`Ball`)을 발사하거나 아이템을 생성할 때, `main.py`에 있는 전역 변수에 접근하기 어렵고 상호 참조(Circular Import) 문제가 발생합니다.

### 해결책: 게임 월드 전담 모듈 (`game_world.py`)
- 모든 게임 객체의 수명 주기(생성, 업데이트, 렌더링, 소멸)를 전담하는 단일 진실 공급원(Single Source of Truth).
- 어느 객체(예: `boy.py`)에서든 `import game_world` 후 `game_world.add_object(...)`, `game_world.remove_object(...)`를 호출할 수 있음.

---

## 2. 렌더링 레이어 (Depth) 개념

객체가 화면에 그려지는 순서를 제어하기 위해 2차원 리스트 구조를 사용합니다.

```python
# layer 0: 배경 객체 (Grass 등)
# layer 1: 전경/상호작용 객체 (Boy, Ball 등)
world = [[], []]
```

- **Update**: 모든 레이어의 객체 순차 업데이트
- **Render**: Layer 0부터 순서대로 그려서 배경 위에 캐릭터/투사체가 자연스럽게 덮이도록 처리

---

## 3. `game_world.py` 표준 완성 코드

```python
# game_world.py

# Layer 0: Background (Grass, Background Images)
# Layer 1: Foreground (Boy, Ball, Enemies, Items)
world = [[], []]


def add_object(o, depth=0):
    """지정한 depth 레이어에 객체 1개 추가"""
    world[depth].append(o)


def add_objects(ol, depth=0):
    """지정한 depth 레이어에 객체 리스트 추가"""
    world[depth] += ol


def remove_object(o):
    """게임 월드에서 해당 객체를 찾아 안전하게 제거"""
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')


def update():
    """모든 레이어의 모든 객체 update() 호출"""
    for layer in world:
        for o in layer:
            o.update()


def render():
    """레이어 순환하며 draw() 호출 (Layer 0 먼저, 그 다음 Layer 1)"""
    for layer in world:
        for o in layer:
            o.draw()
```

---

## 4. `Ball` 클래스 구현 패턴 (실제 투사체 발사)

슬라이드 9~14페이지의 핵심인 축구공(`Ball`) 클래스입니다.

```python
# ball.py
from pico2d import load_image, get_canvas_width
import game_world


class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')  # 또는 ball41x41.png
        self.x = x
        self.y = y
        self.velocity = velocity  # 음수면 왼쪽, 양수면 오른쪽으로 이동

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        # 화면 밖으로 나가면 메모리 누수를 방지하기 위해 game_world에서 제거!
        if self.x < -25 or self.x > get_canvas_width() + 25:
            game_world.remove_object(self)
```

---

## 5. 소년의 볼 발사 (`boy.py` 연동)

### 1) 텍스트 출력 단계 (슬라이드 p.5)
스페이스 키를 눌렀을 때 실제로 볼을 생성하지 않고 콘솔에만 출력:
```python
# boy.py 의 handle_event 내부
if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
    if self.state in ('IDLE', 'RUN'):
        if self.face_dir == 1:
            print("[FIRE BALL] 오른쪽으로 볼을 발사합니다!")
        else:
            print("[FIRE BALL] 왼쪽으로 볼을 발사합니다!")
```

### 2) 실제 객체 생성 단계 (슬라이드 p.14)
```python
# boy.py 상단에 import
from ball import Ball
import game_world

# Boy 클래스 내 메서드 추가
def fire_ball(self):
    # 소년의 손/발 위치(self.x, self.y)와 바라보는 방향에 맞춰 볼 생성
    ball = Ball(self.x, self.y, self.face_dir * 10)
    # 레이어 1(전경)에 추가
    game_world.add_object(ball, 1)

# handle_event 에서 SPACE 키 처리
if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
    if self.state in ('IDLE', 'RUN'):
        self.fire_ball()
    elif self.state == 'SLEEP':
        self.wake_up()
```

---

## 6. 메인 루프 연동 (`main.py`)

기존의 `world.append()` 대신 `game_world`의 함수들을 호출하도록 수정:

```python
# main.py
from pico2d import open_canvas, close_canvas, clear_canvas, update_canvas, delay, get_events, SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE
from boy import Boy
from grass import Grass
import game_world


def reset_world():
    global boy
    grass = Grass()
    game_world.add_object(grass, 0)  # 레이어 0: 배경

    boy = Boy()
    game_world.add_object(boy, 1)    # 레이어 1: 전경


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


running = True
open_canvas()
reset_world()

while running:
    handle_events()
    game_world.update()
    
    clear_canvas()
    game_world.render()
    update_canvas()
    
    delay(0.01)

close_canvas()
```

---

## 7. 오늘 수업/실습 예상 체크리스트

| 번호 | 실습 과제 예상 항목 | 핵심 구현 포인트 |
|:---:|:---|:---|
| 1 | `game_world.py` 완성 | `world = [[], []]`, `add_object(o, depth)`, `remove_object(o)`, `update()`, `render()` |
| 2 | `main.py` 리팩토링 | 자체 리스트 순회 대신 `game_world.update()`, `game_world.render()` 사용 |
| 3 | 스페이스바로 볼 발사 | `SLEEP` 상태에서는 기상, `IDLE`/`RUN` 상태에서는 `fire_ball()` 호출 |
| 4 | `Ball` 클래스 제작 | `ball.py` 분리, `self.x += self.velocity`, 화면 밖 나갈 시 `game_world.remove_object(self)` |
| 5 | 공의 크기 또는 종류 선택 | `ball21x21.png`(작은 공) vs `ball41x41.png`(큰 공) 또는 파워 조절 |
| 6 | 여러 개의 배경 레이어 | 잔디 앞/뒤 레이어 또는 원경/근경 레이어 분리 |

---

## 💡 오프라인 환경 팁
- `game_world.remove_object(self)` 호출 시 루프 도중 리스트 삭제 이슈를 방지하려면 `game_world.remove_object`가 안전하게 동작해야 합니다.
- 클래스 변수 `image = None` 패턴을 사용하여 공을 100개 쏴도 이미지는 1번만 로드되도록 최적화하는 것이 점수 포인트입니다.

