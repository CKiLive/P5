import random
from pygame import Vector2
import core
from agario.experience import xp


class Joueur:
    def __init__(self,bot):
        self.nom = " "
        self.bot = bot
        self.mass = 10
        self.score = 0
        self.vitesse = Vector2(0,0)
        self.vMax = 4
        self.acc = Vector2(0,0)
        self.accMax = 5
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))

    def deplacement(self):
        if self.bot:
            self.acc = Vector2(random.randint(-1,1),random.randint(-1,1))
        else:
            if core.getMouseLeftClick():
                k = 0.01
                u=Vector2(core.getMouseLeftClick() - self.position)
                l = u.length()
                l0 = 10
                u = Vector2(core.getMouseLeftClick()-self.position)
                u.scale_to_length(abs(l-l0)*k)
                self.acc = u

        if self.acc.length() > self.accMax:
            self.acc.scale_to_length(self.accMax)

        self.vitesse = (self.vitesse + self.acc)*(10/self.mass)
        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position = self.position + self.vitesse

        self.acc=Vector2(0,0)
    def manger(self, xp):
        distance = Vector2(self.position - xpPosition)
        if self.mass + self.xpMass > distance.length():
            print('hit')
            return True
        return False
    def seDiviser(self):
        pass
    def show(self):
        core.Draw.circle(self.couleur, self.position, self.mass)

