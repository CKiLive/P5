import core
from agario.experience import xp
from agario.partie import Partie


def setup():
    core.fps=60
    core.WINDOW_SIZE=[1000,800]

    core.memory("MaPartie",Partie())
    core.memory("MonXP", xp())
    core.memory("MaPartie").addJoueur(False)


def run():
    core.cleanScreen()
    core.memory("MaPartie").addJoueur(True)
    core.memory("MaPartie").show()
    core.memory("MaPartie").update()
    core.memory("MaPartie").addXp()
    core.memory("MonXP").show()
    core.memory("MaPartie").updateXp()
core.main(setup, run)