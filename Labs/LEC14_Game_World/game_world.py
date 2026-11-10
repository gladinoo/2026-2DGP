# game_world.py

# Layer 0: Background (Grass)
# Layer 1: Foreground (Boy, Ball)
world = [[], []]


# 게임월드에 객체를 담는 함수 (depth가 없으면 기본 0층)
def add_object(o, depth=0):
    world[depth].append(o)


# 게임월드에 객체 리스트를 한꺼번에 담는 함수
def add_objects(ol, depth=0):
    world[depth] += ol


# 게임월드에서 객체 제거
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')


# 게임월드의 모든 객체 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()


# 게임월드의 모든 객체 그리기 (0층 먼저, 그 다음 1층)
def render():
    for layer in world:
        for o in layer:
            o.draw()
