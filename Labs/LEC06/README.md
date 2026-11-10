# LEC06 / Drill 04: Character Animation

2D 게임프로그래밍 실습 과제: Pico2D를 활용한 캐릭터 궤적 애니메이션 구현

## 📌 기능 소개
1. **원 운동 (Circular Motion)**
   - 삼각함수(`math.cos`, `math.sin`)와 각도 변환(`math.radians`)을 사용하여 (400, 300) 중심, 반지름 200의 원 궤도를 회전합니다.
2. **사각 운동 (Rectangular Motion)**
   - 상단(`draw_top`) ➔ 우측(`draw_right`) ➔ 하단(`draw_bottom`) ➔ 좌측(`draw_left`) 순서로 사각형 경계를 따라 이동합니다.
3. **삼각 운동 (Triangular Motion)**
   - 밑변(`draw_triangle_bottom`) ➔ 우측 상향 대각선(`draw_triangle_right_up`) ➔ 좌측 하향 대각선(`draw_triangle_left_down`) 순서로 선형 보간을 활용해 삼각형 궤도를 이동합니다.
4. **무한 반복 (Infinite Loop)**
   - 원 ➔ 사각 ➔ 삼각 운동을 순차적으로 무한 반복합니다.
5. **이벤트 처리 (Event Handling)**
   - 창 닫기(X) 버튼 또는 `ESC` 키 입력 시 즉시 안전하게 종료됩니다.

## 🚀 실행 방법
```bash
python character_draws.py
```

## 🎮 조작법
- `ESC` 키 또는 창 닫기 버튼: 프로그램 정상 종료
