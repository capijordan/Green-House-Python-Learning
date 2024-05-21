import pygame
import time
from constantes import *



class Stanley:
    def __init__(self):
        self.etat = Constantes.BAS
        self.position = 1
        self.action = Constantes.NORMAL
    def actualiserEtat(self, evenement):
        if evenement == pygame.K_SPACE:
            if self.etat == Constantes.BAS:
                if self.position == 0:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")
                elif self.position == 2:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")
                elif self.position == 3:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")

            if self.etat == Constantes.HAUT:
                if self.position == 0:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")
                elif self.position == 1:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")
                elif self.position == 3:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")
                elif self.position == 4:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")
                elif self.position == 5:
                    self.action = Constantes.SPRAY
                    print("Stanley :: Spray Implémenté")


                #Si la touche Espace à été tapée il utilise l'insecticide.
        else:
            if self.action == Constantes.SPRAY:
                time.sleep(0.2)
                self.action = Constantes.NORMAL
            if self.etat == Constantes.BAS:
                if evenement == pygame.K_RIGHT:
                    if self.position < 3:
                        self.position += 1

                elif evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1

                elif evenement == pygame.K_UP:
                    if self.position == 1:
                        self.etat = Constantes.ECHELLE
                        print("Stanley :: Déplacement Implémenté")

            elif self.etat == Constantes.ECHELLE:
                if evenement == pygame.K_DOWN:
                    if self.position == 1:
                        self.etat = Constantes.BAS
                        print("Stanley :: Déplacement Implémenté")

                    else:
                        self.position += 1
                        print("Stanley :: Déplacement Implémenté")
                elif evenement == pygame.K_UP:
                    if self.position == 1:
                        self.position -= 1
                        print("Stanley :: Déplacement Implémenté")
                    else:
                        self.etat = Constantes.HAUT
                        self.position = 2
                        print("Stanley :: Déplacement Implémenté")



            elif self.etat == Constantes.HAUT:
                if evenement == pygame.K_DOWN:
                    if self.position == 2:
                        self.etat = Constantes.ECHELLE
                        self.position = 0
                        print("Stanley :: Déplacement Implémenté")

                if evenement == pygame.K_RIGHT:
                    if self.position < 5:
                        self.position += 1
                        print("Stanley :: Déplacement Implémenté")

                elif evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1
                        print("Stanley :: Déplacement Implémenté")