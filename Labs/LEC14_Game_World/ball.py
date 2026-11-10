from pico2d import load_image
import game_world


class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = x
        self.y = y
        self.velocity = velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        # 화면 밖으로 나가면 game_world에서 안전하게 삭제!
        if self.x < -25 or self.x > 825:
            game_world.remove_object(self)

