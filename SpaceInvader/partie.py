from datetime import time

from p5 import core
from p5.pong.balle import Balle
from p5.pong.player import Player


class Partie:

    def __init__(self):
        self.player = Player()
        self.balles = []

    def update(self):
        self.player.control()

        for b in self.balles:
            if b.update():
                self.balles.remove(b)

        if core.getKeyPressList("space"):
            if len (self.balles) > 0:
                if time.time() - self.balles[-1].start > 0.5:
                    balle = Balle()
                    balle.pos=self.player.vitesse
                    balle.vitesse.scale_to_lenght(10)
                    self.balles.append(balle)
            else:
                balle = Balle()
                balle.pos = self.player.pos
                balle.vitesse.scale_to
                self.balles.append(balle)