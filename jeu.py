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
        self.listeGuepe = []
        self.listeChenilleG = []
        self.listeChenilleD = []
        self.listeAraigneeG = []
        self.listeAraigneeD = []
        self.constanteRetour = 0
        self.guepe = None
        self.echec = 0
        self.etatChat = Constantes.NORMAL
        self.etatPlanteCG = Constantes.NORMAL
        self.etatPlanteCD = Constantes.NORMAL
        self.etatPlanteAG = Constantes.NORMAL
        self.etatPlanteAD = Constantes.NORMAL
        self.score = 0

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


        if self.guepe != None:
            self.guepe.actualiserEtat()
            '''if self.guepe.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatChat = Constantes.TOUCHE'''
            #Si la guepe pique le chat


        if self.stanley.etat == Constantes.BAS and self.stanley.position == 2 and self.stanley.action == Constantes.SPRAY:
            if self.guepe != None and self.guepe.etat != Constantes.TERMINE:
                self.score += 1
                self.listeGuepe.remove(self.guepe)
                self.guepe = None
                #Si stanley respecte les conditions, il peut tuer la guepe

        for ChenG in self.listeChenilleG:
            ChenG.actualiserEtat()
            if (self.stanley.position == 1 and self.stanley.action == Constantes.SPRAY) and (ChenG.position == 3 or ChenG.position == 2):
                self.score += 1
                self.listeChenilleG.remove(ChenG)
            elif (self.stanley.position == 0 and self.stanley.action == Constantes.SPRAY) and (ChenG.position == 1 or ChenG.position == 0):
                self.score += 1
                self.listeChenilleG.remove(ChenG)
            '''if ChenG.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatPlanteCG = Constantes.TOUCHE'''
            #Si la chenilleG mange la planteG

        for ChenD in self.listeChenilleD:
            ChenD.actualiserEtat()
            if (self.stanley.position == 3 and self.stanley.action == Constantes.SPRAY) and (ChenD.position == 1 or ChenD.position == 2):
                self.score += 1
                self.listeChenilleD.remove(ChenD)
            elif (self.stanley.position == 4 and self.stanley.action == Constantes.SPRAY) and (ChenD.position == 3 or ChenD.position == 4):
                self.score += 1
                self.listeChenilleD.remove(ChenD)
            elif (self.stanley.position == 5 and self.stanley.action == Constantes.SPRAY) and (ChenD.position == 5 or ChenD.position == 6):
                self.score += 1
                self.listeChenilleD.remove(ChenD)
            '''if ChenD.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatPlanteCD = Constantes.TOUCHE'''
            #Si la chenilleD mange la planteD

            for GneeG in self.listeAraigneeG:
                GneeG.actualiserEtat()
                if (self.stanley.position == 0 and self.stanley.action == Constantes.SPRAY) and (GneeG.position >= 0 or GneeG.position <= 4):
                    self.score += 1
                    self.listeAraigneeG.remove(GneeG)
                '''if GneeG.etat == Constantes.TERMINE:
                    self.echec += 1
                    self.etatPlanteBG = Constantes.TOUCHE'''
                # Si l'arraignéeG mange la planteBG

        for ami in self.listeAmis:
            if ami == Constantes.CHAT:
                self.presentation.afficherAmi(Constantes.CHAT, self.etatChat)
                if self.etatChat == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    '''appeler clearListes()'''
                    self.guepe = None
                    self.etatChat = Constantes.NORMAL
                    #Si la guepe a touché le chat, il pique et le jeu continue

            elif ami == Constantes.FLEUR_HG:
                self.presentation.afficherAmi(Constantes.FLEUR_HG, self.etatPlanteCG)
                if self.etatPlanteCG == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.listeChenilleG.clear()
                    '''appeler clearListes()'''
                    self.etatPlanteCG = Constantes.NORMAL
                    #Si la chenilleG a touché la planteG, elle mange la plante et le jeu continue

            elif ami == Constantes.FLEUR_HD:
                self.presentation.afficherAmi(Constantes.FLEUR_HD, self.etatPlanteCD)
                if self.etatPlanteCD == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.listeChenilleD.clear()
                    '''appeler clearListes()'''
                    self.etatPlanteCD = Constantes.NORMAL
                    #Si la chenilleD a touché la planteD, elle mange la plante et le jeu continue

            elif ami == Constantes.FLEUR_BG:
                self.presentation.afficherAmi(Constantes.FLEUR_BG, self.etatPlanteAG)
                if self.etatPlanteAG == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.listeAraigneeG.clear()
                    '''appeler clearListes()'''
                    self.etatPlanteAG = Constantes.NORMAL
                    #Si l'arraignéeG' touche la planteBG, elle mange la plante et le jeu continue

            else:
                self.presentation.afficherAmi(ami, Constantes.NORMAL)




        self.presentation.afficherEchecs(self.echec)
        self.presentation.afficherScore(self.score)

        self.presentation.afficherStanley(self.stanley.etat, self.stanley.position,
                                          self.stanley.action)
        if self.echec == 3:
            self.presentation.actualiserFenetreGraphique()
            self.presentation.attendreFermetureFenetre()




        self.presentation.actualiserFenetreGraphique()


    def gererGuepe(self):
        if self.guepe == None:
            self.guepe = Guepe(self.presentation)
            self.listeGuepe.append(self.guepe)
            print("Une guepe vient d'être générée")
        else:
            print("Il n'y a aucune guepe générée")


    def gererAraigneeG(self):
        self.listeAraigneeG.append(AraigneeG(self.presentation))
        print("Jeu :: araigneeG crée")

    def gererAraigneeD(self):
        self.listeAraigneeD.append(AraigneeD(self.presentation))
        print("Jeu :: araigneeD crée")

    def gererChenilleG(self):
        self.chenilleG = ChenilleG(self.presentation)
        self.listeChenilleG.append(self.chenilleG)
        print("Jeu :: chenilleG crée")

    def gererChenilleD(self):
        self.chenilleD = ChenilleD(self.presentation)
        self.listeChenilleD.append(self.chenilleD)
        print("Jeu :: chenilleD crée")



    def clearListes(self):
        self.guepe.clear()
        self.listeChenilleG.clear()
        self.listeChenilleD.clear()
        self.listeAraigneeG.clear()
        self.listeAraigneeD.clear()
