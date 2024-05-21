import pygame
import time
from constantes import *
from InsecticideG import *

class Presentation:
    def __init__(self):
        pygame.init()

        # charger toutes les images

        self.imgFondEcran = pygame.image.load("images/greenhouse.png")

        self.imgStanleyBasNormal0 = pygame.image.load("images/stanley/bas_normal_0.png")
        self.imgStanleyBasNormal1 = pygame.image.load("images/stanley/bas_normal_1.png")
        self.imgStanleyBasNormal2 = pygame.image.load("images/stanley/bas_normal_2.png")
        self.imgStanleyBasNormal3 = pygame.image.load("images/stanley/bas_normal_3.png")
        self.imgStanleyEchelle0 = pygame.image.load("images/stanley/echelle_0.png")
        self.imgStanleyEchelle1 = pygame.image.load("images/stanley/echelle_1.png")
        self.imgStanleyHautNormal0 = pygame.image.load("images/stanley/haut_normal_0.png")
        self.imgStanleyHautNormal1 = pygame.image.load("images/stanley/haut_normal_1.png")
        self.imgStanleyHautNormal2 = pygame.image.load("images/stanley/haut_normal_2.png")
        self.imgStanleyHautNormal3 = pygame.image.load("images/stanley/haut_normal_3.png")
        self.imgStanleyHautNormal4 = pygame.image.load("images/stanley/haut_normal_4.png")
        self.imgStanleyHautNormal5 = pygame.image.load("images/stanley/haut_normal_5.png")

        self.imgStanleyBasSpray0 = pygame.image.load("images/stanley/bas_spray_0.png")
        self.imgStanleyBasSpray2 = pygame.image.load("images/stanley/bas_spray_2.png")
        self.imgStanleyBasSpray3 = pygame.image.load("images/stanley/bas_spray_3.png")
        self.imgStanleyHautSpray0 = pygame.image.load("images/stanley/haut_spray_0.png")
        self.imgStanleyHautSpray1 = pygame.image.load("images/stanley/haut_spray_1.png")
        self.imgStanleyHautSpray3 = pygame.image.load("images/stanley/haut_spray_3.png")
        self.imgStanleyHautSpray4 = pygame.image.load("images/stanley/haut_spray_4.png")
        self.imgStanleyHautSpray5 = pygame.image.load("images/stanley/haut_spray_5.png")

        self.imgInsecticideHaut0 = pygame.image.load("images/insecticide/haut_gauche_0.png")
        self.imgInsecticideHaut1 = pygame.image.load("images/insecticide/haut_gauche_1.png")
        self.imgInsecticideHaut3 = pygame.image.load("images/insecticide/haut_droite_3.png")
        self.imgInsecticideHaut4 = pygame.image.load("images/insecticide/haut_droite_4.png")
        self.imgInsecticideHaut5 = pygame.image.load("images/insecticide/haut_droite_5.png")

        self.imgInsecticideBas0 = pygame.image.load("images/insecticide/bas_0.png")
        self.imgInsecticideBas2 = pygame.image.load("images/insecticide/bas_2.png")
        self.imgInsecticideBas3 = pygame.image.load("images/insecticide/bas_3.png")
        self.imgInsecticideMvtG = pygame.image.load("images/insecticide/bas_gauche_mvt.png")
        self.imgInsecticideMvtD = pygame.image.load("images/insecticide/bas_droite_mvt.png")

        self.imgEchec = pygame.image.load("images/stanley/echec.png")

        self.imgChat0 = pygame.image.load("images/amis/chat_0.png")
        self.imgChat1 = pygame.image.load("images/amis/chat_1.png")

        self.imgFleurHG0 = pygame.image.load("images/amis/haut_gauche_0.png")
        self.imgFleurHG1 = pygame.image.load("images/amis/haut_gauche_1.png")
        self.imgFleurHD0 = pygame.image.load("images/amis/haut_droite_0.png")
        self.imgFleurHD1 = pygame.image.load("images/amis/haut_droite_1.png")
        self.imgFleurBG0 = pygame.image.load("images/amis/bas_gauche_0.png")
        self.imgFleurBG1 = pygame.image.load("images/amis/bas_gauche_1.png")
        self.imgFleurBD0 = pygame.image.load("images/amis/bas_droite_0.png")
        self.imgFleurBD1 = pygame.image.load("images/amis/bas_droite_1.png")

        self.imgChenilleG0 = pygame.image.load("images/ennemis/chenille_gauche_0.png")
        self.imgChenilleG1 = pygame.image.load("images/ennemis/chenille_gauche_1.png")
        self.imgChenilleG2 = pygame.image.load("images/ennemis/chenille_gauche_2.png")
        self.imgChenilleG3 = pygame.image.load("images/ennemis/chenille_gauche_3.png")
        self.imgChenilleD0 = pygame.image.load("images/ennemis/chenille_droite_0.png")
        self.imgChenilleD1 = pygame.image.load("images/ennemis/chenille_droite_1.png")
        self.imgChenilleD2 = pygame.image.load("images/ennemis/chenille_droite_2.png")
        self.imgChenilleD3 = pygame.image.load("images/ennemis/chenille_droite_3.png")

        self.imgGuepe0 = pygame.image.load("images/ennemis/guepe_0.png")
        self.imgGuepe1 = pygame.image.load("images/ennemis/guepe_1.png")

        self.imgAraigneeG0 = pygame.image.load("images/ennemis/araignee_gauche_0.png")
        self.imgAraigneeG1 = pygame.image.load("images/ennemis/araignee_gauche_1.png")
        self.imgAraigneeD0 = pygame.image.load("images/ennemis/araignee_droite_0.png")
        self.imgAraigneeD1 = pygame.image.load("images/ennemis/araignee_droite_1.png")

        self.imgChiffre0 = pygame.image.load("images/chiffres/Zero.png")
        self.imgChiffre1 = pygame.image.load("images/chiffres/Un.png")
        self.imgChiffre2 = pygame.image.load("images/chiffres/Deux.png")
        self.imgChiffre3 = pygame.image.load("images/chiffres/Trois.png")
        self.imgChiffre4 = pygame.image.load("images/chiffres/Quatre.png")
        self.imgChiffre5 = pygame.image.load("images/chiffres/Cinq.png")
        self.imgChiffre6 = pygame.image.load("images/chiffres/Six.png")
        self.imgChiffre7 = pygame.image.load("images/chiffres/Sept.png")
        self.imgChiffre8 = pygame.image.load("images/chiffres/Huit.png")
        self.imgChiffre9 = pygame.image.load("images/chiffres/Neuf.png")

        # créer la fenêtre avec l'image du fond et le titre

        pygame.display.set_caption("Green House")
        pygame.display.set_icon(pygame.image.load("images/iconeFenetre.png"))
        self.ecran = pygame.display.set_mode((1016, 780))
        self.ecran.blit(self.imgFondEcran, (0, 0))
        pygame.display.update()

    # ------------------------------------------------------------------------
    # retourner la touche sur laquelle a appuyé le joueur ou fermer la fenêtre
    # si clic sur la croix

    def lireEvenement(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key in [pygame.K_SPACE, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN,
                                     pygame.K_LEFT]:
                    return evenement.key
        return Constantes.AUCUN_EVENEMENT

    # ------------------------------------------------------------------------
    # Fermer la fenêtre si clic sur la croix

    def attendreFermetureFenetre(self):
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            time.sleep(0.2)

    # ------------------------------------------------------------------------
    # afficher Stanley avec ou sans le spray

    def afficherStanley(self, etat, position, action=Constantes.NORMAL):
        if action == Constantes.NORMAL:
            if etat == Constantes.HAUT:
                if position == 0:
                    self.afficherImage(18, 149, self.imgStanleyHautNormal0)
                elif position == 1:
                    self.afficherImage(128, 149, self.imgStanleyHautNormal1)
                elif position == 2:
                    self.afficherImage(249, 189, self.imgStanleyHautNormal2)
                elif position == 3:
                    self.afficherImage(360, 149, self.imgStanleyHautNormal3)
                elif position == 4:
                    self.afficherImage(470, 149, self.imgStanleyHautNormal4)
                elif position == 5:
                    self.afficherImage(585, 149, self.imgStanleyHautNormal5)
            elif etat == Constantes.ECHELLE:
                if position == 0:
                    self.afficherImage(249, 348, self.imgStanleyEchelle0)
                elif position == 1:
                    self.afficherImage(267, 490, self.imgStanleyEchelle1)
            elif etat == Constantes.BAS:
                if position == 0:
                    self.afficherImage(138, 608, self.imgStanleyBasNormal0)
                elif position == 1:
                    self.afficherImage(252, 608, self.imgStanleyBasNormal1)
                elif position == 2:
                    self.afficherImage(373, 608, self.imgStanleyBasNormal2)
                elif position == 3:
                    self.afficherImage(494, 608, self.imgStanleyBasNormal3)
        elif action == Constantes.SPRAY:
            if etat == Constantes.HAUT:
                if position == 0:
                    self.afficherImage(18, 149, self.imgStanleyHautSpray0)
                    self.afficherImage(57, 22, self.imgInsecticideHaut0)
                elif position == 1:
                    self.afficherImage(128, 149, self.imgStanleyHautSpray1)
                    self.afficherImage(144, 22, self.imgInsecticideHaut1)
                elif position == 3:
                    self.afficherImage(360, 149, self.imgStanleyHautSpray3)
                    self.afficherImage(352, 22, self.imgInsecticideHaut3)
                elif position == 4:
                    self.afficherImage(470, 149, self.imgStanleyHautSpray4)
                    self.afficherImage(459, 22, self.imgInsecticideHaut4)
                elif position == 5:
                    self.afficherImage(585, 149, self.imgStanleyHautSpray5)
                    self.afficherImage(560, 22, self.imgInsecticideHaut5)
            elif etat == Constantes.BAS:
                if position == 0:
                    self.afficherImage(138, 608, self.imgStanleyBasSpray0)
                    self.afficherImage(70, 596, self.imgInsecticideBas0)
                elif position == 2:
                    self.afficherImage(373, 608, self.imgStanleyBasSpray2)
                    self.afficherImage(392, 481, self.imgInsecticideBas2)
                elif position == 3:
                    self.afficherImage(494, 608, self.imgStanleyBasSpray3)
                    self.afficherImage(595, 595, self.imgInsecticideBas3)

    # ------------------------------------------------------------------------
    # afficher l'insecticide à gauche

    def afficherInsecticideG(self, position):
        if position == 0:
            self.afficherImage(24, 413, self.imgInsecticideMvtG)
        elif position == 1:
            self.afficherImage(36, 461, self.imgInsecticideMvtG)
        elif position == 2:
            self.afficherImage(48, 509, self.imgInsecticideMvtG)
        elif position == 3:
            self.afficherImage(60, 555, self.imgInsecticideMvtG)

    # ------------------------------------------------------------------------
    # afficher l'insecticide à droite

    def afficherInsecticideD(self, position):
        if position == 1:
            self.afficherImage(610, 555, self.imgInsecticideMvtD)
        elif position == 2:
            self.afficherImage(620, 509, self.imgInsecticideMvtD)
        elif position == 3:
            self.afficherImage(632, 461, self.imgInsecticideMvtD)
        elif position == 4:
            self.afficherImage(644, 413, self.imgInsecticideMvtD)

    # ------------------------------------------------------------------------
    # afficher un ami (fleur, chat...)

    def afficherAmi(self, typeAmi, etat):
        if typeAmi == Constantes.FLEUR_HG:
            if etat == Constantes.NORMAL:
                self.afficherImage(5, 41, self.imgFleurHG0)
            elif etat == Constantes.TOUCHE:
                self.afficherImage(15, 85, self.imgFleurHG1)
        elif typeAmi == Constantes.FLEUR_HD:
            if etat == Constantes.NORMAL:
                self.afficherImage(665, 41, self.imgFleurHD0)
            elif etat == Constantes.TOUCHE:
                self.afficherImage(659, 85, self.imgFleurHD1)
        elif typeAmi == Constantes.FLEUR_BG:
            if etat == Constantes.NORMAL:
                self.afficherImage(64, 668, self.imgFleurBG0)
            elif etat == Constantes.TOUCHE:
                self.afficherImage(43, 693, self.imgFleurBG1)
        elif typeAmi == Constantes.FLEUR_BD:
            if etat == Constantes.NORMAL:
                self.afficherImage(616, 668, self.imgFleurBD0)
            elif etat == Constantes.TOUCHE:
                self.afficherImage(638, 693, self.imgFleurBD1)
        elif typeAmi == Constantes.CHAT:
            if etat == Constantes.NORMAL:
                self.afficherImage(495, 498, self.imgChat0)
            elif etat == Constantes.TOUCHE:
                self.afficherImage(495, 425, self.imgChat1)

    # ------------------------------------------------------------------------
    # afficher une chenille à gauche

    def afficherChenilleG(self, position):
        if position == 0:
            self.afficherImage(45, 46, self.imgChenilleG0)
        elif position == 1:
            self.afficherImage(85, 48, self.imgChenilleG1)
        elif position == 2:
            self.afficherImage(140, 48, self.imgChenilleG2)
        elif position == 3:
            self.afficherImage(194, 40, self.imgChenilleG1)
        elif position == 4:
            self.afficherImage(234, 16, self.imgChenilleG3)

    # ------------------------------------------------------------------------
    # afficher une chenille à droite

    def afficherChenilleD(self, position):
        if position == 0:
            self.afficherImage(308, 16, self.imgChenilleD0)
        elif position == 1:
            self.afficherImage(353, 40, self.imgChenilleD1)
        elif position == 2:
            self.afficherImage(409, 48, self.imgChenilleD2)
        elif position == 3:
            self.afficherImage(466, 48, self.imgChenilleD1)
        elif position == 4:
            self.afficherImage(522, 48, self.imgChenilleD2)
        elif position == 5:
            self.afficherImage(578, 48, self.imgChenilleD1)
        elif position == 6:
            self.afficherImage(624, 45, self.imgChenilleD3)

    # ------------------------------------------------------------------------
    # afficher une araignee à gauche

    def afficherAraigneeG(self, position):
        if position == 0:
            self.afficherImage(39, 412, self.imgAraigneeG0)
        elif position == 1:
            self.afficherImage(51, 461, self.imgAraigneeG1)
        elif position == 2:
            self.afficherImage(63, 510, self.imgAraigneeG0)
        elif position == 3:
            self.afficherImage(75, 555, self.imgAraigneeG1)
        elif position == 4:
            self.afficherImage(87, 608, self.imgAraigneeG0)

    # ------------------------------------------------------------------------
    # afficher une araignee à droite

    def afficherAraigneeD(self, position):
        if position == 0:
            self.afficherImage(613, 608, self.imgAraigneeD0)
        elif position == 1:
            self.afficherImage(624, 555, self.imgAraigneeD1)
        elif position == 2:
            self.afficherImage(634, 510, self.imgAraigneeD0)
        elif position == 3:
            self.afficherImage(645, 461, self.imgAraigneeD1)
        elif position == 4:
            self.afficherImage(656, 412, self.imgAraigneeD0)

    # ------------------------------------------------------------------------
    # afficher la guêpe

    def afficherGuepe(self, position):
        if position == 0:
            self.afficherImage(410, 511, self.imgGuepe0)
        elif position == 1:
            self.afficherImage(468, 528, self.imgGuepe1)

    # ------------------------------------------------------------------------
    # afficher la tête de Stanley en cas d'échec
    # nbEchecs = (nombre d'échecs) 1, 2 ou 3

    def afficherEchecs(self, nbEchecs):
        for i in range(nbEchecs):
            self.afficherImage(824 + (i * 36), 427, self.imgEchec)

    # ------------------------------------------------------------------------
    # afficher le score

    def afficherScore(self, score):
        self.afficherChiffre(797, 270, int(score / 1000))
        self.afficherChiffre(837, 270, int(score / 100) % 10)
        self.afficherChiffre(877, 270, int(score / 10) % 10)
        self.afficherChiffre(917, 270, score % 10)

    # ------------------------------------------------------------------------
    # afficher un chiffre

    def afficherChiffre(self, x, y, chiffre):
        if chiffre == 0:
            self.afficherImage(x, y, self.imgChiffre0)
        elif chiffre == 1:
            self.afficherImage(x, y, self.imgChiffre1)
        elif chiffre == 2:
            self.afficherImage(x, y, self.imgChiffre2)
        elif chiffre == 3:
            self.afficherImage(x, y, self.imgChiffre3)
        elif chiffre == 4:
            self.afficherImage(x, y, self.imgChiffre4)
        elif chiffre == 5:
            self.afficherImage(x, y, self.imgChiffre5)
        elif chiffre == 6:
            self.afficherImage(x, y, self.imgChiffre6)
        elif chiffre == 7:
            self.afficherImage(x, y, self.imgChiffre7)
        elif chiffre == 8:
            self.afficherImage(x, y, self.imgChiffre8)
        elif chiffre == 9:
            self.afficherImage(x, y, self.imgChiffre9)

    # ------------------------------------------------------------------------
    # afficher une image sur l'image de fond d'écran initiale

    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.ecran.blit(image, rect)

    # ------------------------------------------------------------------------
    # restaurer l'image interne d'origine de l'écran (ceci provoque
    # l’effacement de tous les personnages)

    def effacerImageInterne(self):
        self.ecran.blit(self.imgFondEcran, (0, 0, 1016, 780), (0, 0, 1016, 780))

    # ------------------------------------------------------------------------
    # mettre à jour l'image visible l'écran

    def actualiserFenetreGraphique(self):
        pygame.display.update()