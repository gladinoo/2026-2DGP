"""
Drill #8: 애니메이션 뷰어 (Animation Viewer)
- 과제 기본 요구사항 및 보너스 점수 충족 구현:
  1. 화면 중앙 (400, 300)에 캐릭터 렌더링
  2. 화면 높이(600px)의 50% 이상(320px)으로 확대 렌더링 (SCALE = 3.2)
  3. 각 동작별 5회 반복 재생 후 다음 동작으로 전환
  4. 동작 변경 시 1초 동안 정지 (delay(1.0))
  5. 모든 동작 완료 후 무한 반복 (while True)
  6. 보너스 1 (+2점): 프레임마다 크기가 다른 복잡한 스프라이트 시트 처리 ((left, bottom, width, height) 튜플)
  7. 보너스 2 (+2점): 동작마다 프레임 수가 다름 (대기: 4장, 걷기: 6장, 달리기: 8장, 공격: 5장)
"""

from pico2d import *

# 캔버스 초기화 (800 x 600)
open_canvas(800, 600)

# 리소스 로드
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# 화면 중앙 좌표 및 확대 비율 설정 (100px 기준 320px로 확대하여 화면 높이 50% 이상 차지)
CENTER_X, CENTER_Y = 400, 300
SCALE = 3.2

# ==============================================================================
# 동작별 프레임 데이터 정의: (left, bottom, width, height)
# [보너스 1] 프레임별 너비/높이가 상이한 복합 바운딩 박스 구조 지원
# [보너스 2] 각 동작별 프레임 수가 상이함 (4개, 6개, 8개, 5개)
# ==============================================================================

# 1. 대기 동작 (IDLE): 4개 프레임
IDLE_FRAMES = (
    (0, 300, 100, 100),
    (100, 300, 102, 100),
    (202, 300, 98, 100),
    (300, 300, 100, 100),
)

# 2. 걷기 동작 (WALK): 6개 프레임
WALK_FRAMES = (
    (0, 200, 95, 100),
    (95, 200, 105, 100),
    (200, 200, 100, 102),
    (300, 200, 98, 98),
    (398, 200, 104, 100),
    (502, 200, 100, 100),
)

# 3. 달리기 동작 (RUN): 8개 프레임
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

# 4. 공격 동작 (ATTACK): 5개 프레임
ATTACK_FRAMES = (
    (0, 0, 100, 100),
    (100, 0, 115, 105),
    (215, 0, 120, 110),
    (335, 0, 110, 100),
    (445, 0, 100, 100),
)


def handle_events():
    """사용자 이벤트 처리 (창 닫기 또는 ESC 키 입력 시 안전하게 종료)"""
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()


def draw_frame(frame_data):
    """지정된 바운딩 박스(frame_data)로 화면 중앙에 확대 렌더링"""
    left, bottom, width, height = frame_data
    character.clip_draw(
        left, bottom, width, height,
        CENTER_X, CENTER_Y,
        int(width * SCALE), int(height * SCALE)
    )


def play_action(action_frames, repeat_count=5, frame_delay=0.1):
    """
    한 동작을 지정된 횟수(기본 5회)만큼 반복 재생한 후 1초간 정지하는 함수
    :param action_frames: 동작에 포함된 프레임 좌표 리스트/튜플
    :param repeat_count: 동작 반복 횟수 (과제 요구사항: 5회)
    :param frame_delay: 프레임 간 전환 시간(초)
    """
    for _ in range(repeat_count):
        for frame_data in action_frames:
            clear_canvas()
            grass.draw(400, 30)
            draw_frame(frame_data)
            update_canvas()
            handle_events()
            delay(frame_delay)
    # 한 동작 5회 반복 완료 후, 동작 변경 전 1초 정지 (과제 요구사항)
    delay(1.0)


# 전체 액션 시퀀스 파이프라인 정의 (액션 이름, 프레임 튜플, 프레임 딜레이)
ACTIONS = (
    ('IDLE', IDLE_FRAMES, 0.1),
    ('WALK', WALK_FRAMES, 0.1),
    ('RUN', RUN_FRAMES, 0.08),
    ('ATTACK', ATTACK_FRAMES, 0.12),
)

# 무한 반복 실행 (모든 동작 완료 후 처음부터 다시 시작)
while True:
    for action_name, frames, frame_delay in ACTIONS:
        play_action(frames, repeat_count=5, frame_delay=frame_delay)

close_canvas()
