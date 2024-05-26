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
        #Ennemi instancié
        self.listeChenilleG = []
        self.listeChenilleD = []
        self.listeAraigneeG = []
        self.listeAraigneeD = []
        #Listes d'ennemis
        self.constanteRetour = 0
        #Là ou'est retourné la constante de l'ennemi à générer
        self.guepe = None
        #Présence de guêpe ou non
        self.echec = 0
        self.etatChat = Constantes.NORMAL
        self.etatPlanteCG = Constantes.NORMAL
        self.etatPlanteCD = Constantes.NORMAL
        self.etatPlanteAG = Constantes.NORMAL
        self.etatPlanteAD = Constantes.NORMAL
        # Etat initial des amis
        self.score = 0
        self.ListeInsectiG = []
        self.ListeInsectiD = []
        #Listes d'insecticides (Bonus)

        #...                                 # attributs pour les ennemis, le score, ...

    # ----------------------------------------------------------------------------
    # méthode qui contient la boucle principale du jeu

    def demarrer(self):
        while True:

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
            #Types d'ennemis générés

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
        if self.stanley.etat == Constantes.BAS:
            if self.stanley.action == Constantes.SPRAY and self.stanley.position == 0:
                self.ListeInsectiG.append(InsecticideG(self.presentation))
        #Génération de l'insecticide Gauche

            elif self.stanley.action == Constantes.SPRAY and self.stanley.position == 3:
                self.ListeInsectiD.append(InsecticideD(self.presentation))
        # Génération de l'insecticide Droite
        for InscG in self.ListeInsectiG:
            InscG.actualiserEtat()
            if InscG.etat == Constantes.TERMINE:
                self.ListeInsectiG.remove(InscG)
        #Disparition des Insecticides Gauche une fois leurs trajet terminé
        for InscD in self.ListeInsectiD:
            InscD.actualiserEtat()
            if InscD.etat == Constantes.TERMINE:
                self.ListeInsectiD.remove(InscD)
        # Disparition des Insecticides Droite une fois leurs trajet terminé
        if self.guepe != None:
            self.guepe.actualiserEtat()
            if self.guepe.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatChat = Constantes.TOUCHE
            #Si la guepe pique le chat


        if self.stanley.etat == Constantes.BAS and self.stanley.position == 2 and self.stanley.action == Constantes.SPRAY:
            if self.guepe != None and self.guepe.etat != Constantes.TERMINE:
                self.score += 1
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
            #Si Stanley attaque 1 ou 2 Chenilles Gauche
            if ChenG.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatPlanteCG = Constantes.TOUCHE
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
            # Si Stanley attaque 1 ou 2 Chenilles Droite
            if ChenD.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatPlanteCD = Constantes.TOUCHE
            #Si la chenilleD mange la planteD

        for GneeG in self.listeAraigneeG:
            GneeG.actualiserEtat()
            if (self.stanley.position == 0 and self.stanley.action == Constantes.SPRAY):
                self.score += 1
                self.listeAraigneeG.remove(GneeG)
            #Si Stanley utilise son spray sur une arraignée Gauche
            if GneeG.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatPlanteAG = Constantes.TOUCHE
            # Si l'arraignéeG mange la planteBG

        for GneeD in self.listeAraigneeD:
            GneeD.actualiserEtat()
            if (self.stanley.position == 3 and self.stanley.action == Constantes.SPRAY):
                self.score += 1
                self.listeAraigneeD.remove(GneeD)
            # Si Stanley utilise son spray sur une araignée Droite
            if GneeD.etat == Constantes.TERMINE:
                self.echec += 1
                self.etatPlanteAD = Constantes.TOUCHE
            # Si l'arraignéeD mange la planteBD



        for ami in self.listeAmis:
            if ami == Constantes.CHAT:
                self.presentation.afficherAmi(Constantes.CHAT, self.etatChat)
                if self.etatChat == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.clearListes()
                    self.guepe = None
                    self.etatChat = Constantes.NORMAL
                    #Si la guepe a touché le chat, il pique et le jeu continue

            elif ami == Constantes.FLEUR_HG:
                self.presentation.afficherAmi(Constantes.FLEUR_HG, self.etatPlanteCG)
                if self.etatPlanteCG == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.clearListes()
                    self.etatPlanteCG = Constantes.NORMAL
                    #Si la chenilleG a touché la planteG, elle mange la plante et le jeu continue

            elif ami == Constantes.FLEUR_HD:
                self.presentation.afficherAmi(Constantes.FLEUR_HD, self.etatPlanteCD)
                if self.etatPlanteCD == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.clearListes()
                    self.etatPlanteCD = Constantes.NORMAL
                    #Si la chenilleD a touché la planteD, elle mange la plante et le jeu continue

            elif ami == Constantes.FLEUR_BG:
                self.presentation.afficherAmi(Constantes.FLEUR_BG, self.etatPlanteAG)
                if self.etatPlanteAG == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.clearListes()
                    self.etatPlanteAG = Constantes.NORMAL
                    #Si l'arraignéeG touche la planteAG, elle mange la plante et le jeu continue

            elif ami == Constantes.FLEUR_BD:
                self.presentation.afficherAmi(Constantes.FLEUR_BD, self.etatPlanteAD)
                if self.etatPlanteAD == Constantes.TOUCHE:
                    self.presentation.actualiserFenetreGraphique()
                    time.sleep(1.5)
                    self.clearListes()
                    self.etatPlanteAD = Constantes.NORMAL
                    #Si l'arraignéeD touche la planteAD, elle mange la plante et le jeu continue
            else:
                self.presentation.afficherAmi(ami, Constantes.NORMAL)
            #Si les amis n'ont pas été touchés



        self.presentation.afficherEchecs(self.echec)
        self.presentation.afficherScore(self.score)

        self.presentation.afficherStanley(self.stanley.etat, self.stanley.position,
                                          self.stanley.action)
        if self.echec == 3:
            self.presentation.actualiserFenetreGraphique()
            self.presentation.attendreFermetureFenetre()
        #Si 3 échecs, le jeu se stoppe, affiche le score et les échecs et attends la fermeture par la croix




        self.presentation.actualiserFenetreGraphique()


    def gererGuepe(self):
        if self.guepe == None:
            self.guepe = Guepe(self.presentation)
            print("Une guepe vient d'être générée")
        else:
            print("Il n'y a aucune guepe générée")
    #Méthode qui décide de générer ou pas une guêpe

    def gererAraigneeG(self):
        self.listeAraigneeG.append(AraigneeG(self.presentation))
        print("Jeu :: araigneeG crée")
    #Méthode qui génère une arraignée gauche à la liste
    def gererAraigneeD(self):
        self.listeAraigneeD.append(AraigneeD(self.presentation))
        print("Jeu :: araigneeD crée")
    # Méthode qui génère une arraignée droite à la liste
    def gererChenilleG(self):
        self.listeChenilleG.append(ChenilleG(self.presentation))
        print("Jeu :: chenilleG crée")
    # Méthode qui génère une Chenille gauche à la liste
    def gererChenilleD(self):
        self.listeChenilleD.append(ChenilleD(self.presentation))
        print("Jeu :: chenilleD crée")
        # Méthode qui génère une Chenille droite à la liste
    def clearListes(self):
        self.listeChenilleG.clear()
        self.listeChenilleD.clear()
        self.listeAraigneeG.clear()
        self.listeAraigneeD.clear()
        self.guepe = None
        ##Méthode qui vide les liste d'ennemis pour une réapparition gérable pour Stanley dans la partie