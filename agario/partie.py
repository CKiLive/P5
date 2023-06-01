import random
from pygame import Vector2
import core
from agario.experience import xp
from agario.joueur import Joueur




class Partie:
    def __init__(self):
        self.timer = 0
        self.nbJoueur = 20
        self.joueurs = []
        self.piege = []
        self.nbXp = 100
        self.xp = []
        self.couleur = (255,255,255)
        self.taille = Vector2(1000,800)
    def start(self):
        pass
    def end(self):
        pass
    def restart(self):
        pass
    def addJoueur(self,bot):
        if len(self.joueurs) < self.nbJoueur:
            self.joueurs.append( Joueur(bot) )

    def delJoueur(self):
        pass

    def show(self):
        for j in self.joueurs:
            j.show()

    def update(self):
        for j in self.joueurs:
            j.deplacement()

        self.edge()

    def edge(self):
        for j in self.joueurs:
            if j.position.x < 0:
                j.position.x = core.WINDOW_SIZE[0]
            if j.position.x > core.WINDOW_SIZE[0]:
                j.position.x = 0
            if j.position.y < 0:
                j.position.y = core.WINDOW_SIZE[1]
            if j.position.y > core.WINDOW_SIZE[1]:
                j.position.y = 0

    def addXp(self):
        if len(self.xp) < self.nbXp:
            self.xp.append(xp)

    def updateXp(self):
        for j in self.joueurs:
            for xp in self.xp:
                if j.manger(xp):
                    xp.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))

