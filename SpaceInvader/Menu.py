from pygame.draw import rect

from p5 import core


def afficherMenu():
    print("Menu")

    # Bouton Start
    bouton = rect(350, 400, 100, 40)
    core.draw.rect((255, 0, 0), bouton)
    core.draw.text((255, 255, 255), "START", (352, 402))

    if core.getMouseLeftClick():
        if bouton.collidepoint(core.getMouseLeftClick()):
            core.memory("etat", 1)
    if core.getKeyPressList("SPACE"):
        core.memory("etat", 1)