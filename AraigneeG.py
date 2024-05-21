import pygame
import time
from constantes import *
from random import *
from presentation import *

class AraigneeG:
    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 4
        self.position = 0
        self.presentation.afficherAraigneeG(0)
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai -= 1
        if self.delai <= 0:
            if self.position <= 4:
                self.presentation.afficherAraigneeG(self.position)
                print("AraignéeG :: position = " + str(self.position))
                self.position += 1
                self.delai = 4
            else:
                self.etat = Constantes.TERMINE

        else:
            self.presentation.afficherAraigneeG(self.position)

            # Gère le changement d'état des objets de type Arraignée Gauche