

from p5 import core
from p5.Jeu.état import Etat


def setup():
    core.fps = 60
    core.WINDOW_SIZE = [1000, 800]
    core.memory("etat", Etat.MENU)


def run():
    core.cleanScreen()
    if core.memory('etat') == Etat.MENU:
        print.MENU
        if core.getMouseLeftClick():
            core.memory("etat", Etat.JEU)

    if core.memory('etat') == Etat.JEU:
        print.JEU
        if core.getMouseLeftClick():
            core.memory("etat", Etat.MENU)
