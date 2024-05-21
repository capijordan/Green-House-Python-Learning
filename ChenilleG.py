import pygame
import time
from constantes import *
from random import *
from presentation import *

class ChenilleG:
    def __init__(self,presentation):
        self.presentation = presentation
        self.delai = 6
        self.position = 4
        self.presentation.afficherChenilleG(4)
        self.etat = Constantes.NORMAL


    def actualiserEtat(self):
        self.delai -= 1
        if self.delai <= 0:
            if self.position > 0:
                self.presentation.afficherChenilleG(self.position)
                print("ChenilleG :: position = " + str(self.position))
                self.position -= 1
                self.delai = 6
            else:
                self.etat = Constantes.TERMINE

        else:
            self.presentation.afficherChenilleG(self.position)