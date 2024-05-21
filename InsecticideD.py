import pygame
import time
from constantes import *
from random import *

class InsecticideD:
    def __init__(self, presentation):
        self.presentation = presentation
        self.position = 1
        self.presentation.afficherInsecticideD(1)
        self.etat = Constantes.NORMAL
        self.delai = 0

    def actualiserEtat(self):
        if self.delai == 1:
            if self.position <= 4:
                self.presentation.afficherInsecticideD(self.position)
                self.position += 1
            else:
                self.etat = Constantes.TERMINE
        else:
            self.delai += 1

#Gère le changement d'état des objets de type Insecticide Droite