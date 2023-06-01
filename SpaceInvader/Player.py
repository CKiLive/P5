from pygame import Vector2

from p5 import core


class Player:
    def __init__(self):
        self.pos = Vector2(200, 200)
        self.vitesse = Vector2(0, 1)
        self.acc = Vector2()

    def control(self):
        if core.getKeyPressList("q"):
            self.vitesse = self.vitesse.rotation

    def show(self):
        p1 = Vector2(self.vitesse)
        p1.scale_to_length(30)
        p1 += self.pos

        p2 = Vector2(self.vitesse)
        p2.scale_to_length(10)
        p2 = p2.rotate(90)
        p2 += self.pos

        p3 = Vector2(self.vitesse)
        p3.scale_to_length(10)
        p3 = p3.rotate(-90)
        p3 += self.pos
