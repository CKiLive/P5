from enum import Enum

from p5 import core


class Etat(Enum):
    Menu = 0
    Jeu = 1


def setup():
    core.fps = 60
    core.WINDOW_SIZE = [800, 800]
    core.memory()


def run():
    core.cleanScreen()


core.main
