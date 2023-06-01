import random
from pygame import Vector2
import core


class xp:
    def __init__(self):
        self.xpMass = 3
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.xpPosition = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))

    def show(self):
        core.Draw.circle(self.couleur, self.xpPosition, self.xpMass)