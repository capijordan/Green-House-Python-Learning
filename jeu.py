import time
from presentation import *
from stanley import *
from Ennemis import *
from Guepe import *
from ChenilleG import *
from ChenilleD import *
from AraigneeG import *
from AraigneeD import *
from InsecticideG import *
from InsecticideD import *


class Jeu:
    def __init__(self):
        self.presentation = Presentation()   # attribut pour la couche présentation
        self.stanley = Stanley()             # attribut pour Stanley
        self.listeAmis = [Constantes.FLEUR_HG, Constantes.FLEUR_HD, Constantes.FLEUR_BG, Constantes.FLEUR_BD, Constantes.CHAT]
        self.moobs = Ennemis()
        self.listeEnnemis = []
        self.constanteRetour = 0
        self.guepe = None

        #...                                 # attributs pour les ennemis, le score, ...

    # ----------------------------------------------------------------------------
    # méthode qui contient la boucle principale du jeu

    def demarrer(self):
        while True:
            # le code de gestion du déplacement des ennemis et des collisions va venir ici ...

            # le code de génération des ennemis va venir ici ...
            self.constanteRetour = self.moobs.actualiserEtat()
            # Si il y a une guepe générée, il y aura pas une seconde a la suite
            if self.constanteRetour == Constantes.GUEPE:
                self.gererGuepe()

            elif self.constanteRetour == Constantes.ARAIGNEE_G:
                self.gererAraigneeG()

            elif self.constanteRetour == Constantes.ARAIGNEE_D:
                self.gererAraigneeD()

            elif self.constanteRetour == Constantes.CHENILLE_G:
                self.gererChenilleG()

            elif self.constanteRetour == Constantes.CHENILLE_D:
                self.gererChenilleD()


            # récupérer l'événement du joueur et changer l'état de Stanley
            self.stanley.actualiserEtat(self.presentation.lireEvenement())
            # mettre à jour l'image à l'écran




            self.actualiserEcran()

            # attendre 100 millisecondes (délai de référence)

            time.sleep(0.1)

    # ----------------------------------------------------------------------------
    # méthode qui met à jour l'image du jeu à l'écran

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()
        #Afficher Les amis via une boucle qui voyage dans la liste et qui appelle afficheAmi à chaque tour de boucle
        for ami in self.listeAmis:
            typeAmi = ami
            self.presentation.afficherAmi(typeAmi, Constantes.NORMAL)


        self.presentation.afficherStanley(self.stanley.etat, self.stanley.position,
                                          self.stanley.action)

        for guepePop in self.listeEnnemis:
            guepePop.actualiserEtat()

        self.presentation.actualiserFenetreGraphique()


    def gererGuepe(self):
        if self.guepe != None:
            self.listeEnnemis.append(Guepe(self.presentation))
            # print("Jeu :: Guêpe crée")
            print(self.listeEnnemis)
            self.guepe = None
            print("Une guepe vient d'être générée")
        else:
            print("Il n'y a aucune guepe générée")


    def gererAraigneeG(self):
        self.listeEnnemis.append(AraigneeG(self.presentation))
        # print("Jeu :: araigneeG crée")
        # print(self.listeEnnemis)
        self.guepe = 1

    def gererAraigneeD(self):
        self.listeEnnemis.append(AraigneeD(self.presentation))
        # print("Jeu :: araigneeD crée")
        # print(self.listeEnnemis)
        self.guepe = 1

    def gererChenilleG(self):
        self.listeEnnemis.append(ChenilleG(self.presentation))
        # print("Jeu :: chenilleG crée")
        # print(self.listeEnnemis)
        self.guepe = 1

    def gererChenilleD(self):
        self.listeEnnemis.append(ChenilleD(self.presentation))
        # print("Jeu :: chenilleD crée")
        # print(self.listeEnnemis)
        self.guepe = 1