import pygame
import time
from constantes import *
from random import *
from presentation import *

class ChenilleD:
    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 6
        self.position = 0
        self.presentation.afficherChenilleD(0)
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai -= 1
        if self.delai <= 0:
            if self.position < 6:
                self.presentation.afficherChenilleD(self.position)
                print("ChenilleD :: position = " + str(self.position))
                self.position += 1
                self.delai = 6
            else:
                self.etat = Constantes.TERMINE

        else:
            self.presentation.afficherChenilleD(self.position)

            # Gère le changement d'état des objets de type Chenille Droite