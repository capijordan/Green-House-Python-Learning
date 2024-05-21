import pygame
import time
from constantes import *
from random import *

class Ennemis:
    def __init__(self):
        self.delai = 16
        #delai initial a 1.5 sec
        self.compteurTemps = 0
        self.difficulteDelais = 16
        #delai variable selon la difficulté

    def actualiserEtat(self):
        self.delai -= 1
        self.compteurTemps += 0.1
        #print("Delais : "+str(self.delai))
        if self.compteurTemps == 10:
            self.difficulteDelais = random(10, 15)
            #Difficulté variable en variant delai de génération entre 0.1 * 10 (1 sec) et 0.1 * 15 (1.5 sec)
            self.delai = self.difficulteDelais
            #print("Ennemis :: Changement de délai " + str(self.delai))

        if self.delai > 0:
            return Constantes.AUCUN_ENNEMI
        else:

            self.tirage = randint(0, 4)
            if self.tirage == 0:
                #print("Ennemis :: Type Guepe")
                self.delai = self.difficulteDelais
                return Constantes.GUEPE
            elif self.tirage == 1:
                #print("Ennemis :: Type Chenille Gauche")
                self.delai = self.difficulteDelais
                return Constantes.CHENILLE_G
            elif self.tirage == 2:
                #print("Ennemis :: Type Chenille Droite")
                self.delai = self.difficulteDelais
                return Constantes.CHENILLE_D
            elif self.tirage == 3:
                #print("Ennemis :: Type Araignée Gauche")
                self.delai = self.difficulteDelais
                return Constantes.ARAIGNEE_G
            elif self.tirage == 4:
                #print("Ennemis :: Type Araignée Droite")
                self.delai = self.difficulteDelais
                return Constantes.ARAIGNEE_D


#Gère le changement d'état des objets de type Ennemis ainsi que faire varier la difficulté (délais de génération variable)