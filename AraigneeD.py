import pygame
import time
from constantes import *
from random import *
from presentation import *

class AraigneeD:
    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 4
        self.position = 4
        self.presentation.afficherAraigneeD(4)
        self.etat = Constantes.NORMAL

    def actualiserEtat(self):
        self.delai -= 1
        if self.delai <= 0:
            if self.position >= 0:
                self.presentation.afficherAraigneeD(self.position)
                print("AraignéeD :: position = " + str(self.position))
                self.position -= 1
                self.delai = 4
            else:
                self.etat = Constantes.TERMINE

        else:
            self.presentation.afficherAraigneeD(self.position)

            #Gère le changement d'état des objets de type Arraignée Droite