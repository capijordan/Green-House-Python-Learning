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
        self.etat = Constantes.NORMAL


    def actualiserEtat(self):
        #print('Guepe :: actualiserEtat : debut')
        self.delai -= 1
        if self.delai <= 0:
            if self.position < 2:
                self.presentation.afficherGuepe(self.position)
                print("Guepe :: position = "+ str(self.position))
                self.position += 1
                self.delai = 10
            else:
                self.etat = Constantes.TERMINE

        else:
            self.presentation.afficherGuepe(self.position)

#Gère le changement d'état des objets de type Guêpe







