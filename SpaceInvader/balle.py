import time

from pygame import Vector2

from p5 import core


class balle:
    def __init__(self):
        self.pos = Vector2()
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.startTime = time.time()

    def show(self):
        core.draw.circle(255, 255, 255)

    def update(self):
        self.pos = self.pos + self.vitesse

        if time.time() - self.startTime > 0.5:
            return True
        return False
