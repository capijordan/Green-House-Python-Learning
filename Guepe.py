import pygame
import time
from constantes import *
from presentation import *
from random import *

class Guepe:
    def __init__(self, presentation):
        self.presentation = presentation
        self.delai = 10
        self.position = 0
        self.presentation.afficherGuepe(0)
        self.etatChat = Constantes.NORMAL


    def actualiserEtat(self):
        self.delai -= 1
        if self.delai <= 0:
            if self.position >= 0 and self.position != 1:
                self.presentation.afficherGuepe(self.position)
                #print("Guepe :: position = "+ str(self.position))
                self.position += 1
                self.delai = 10
            elif self.position == 2:
                self.presentation.afficherAmi(typeAmi, Constantes.TOUCHE)




