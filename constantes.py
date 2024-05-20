class Constantes:
    # différents états de Stanley

    HAUT = 0
    ECHELLE = 1
    BAS = 2

    # quand aucune touche du curseur/espace n'a été pressée

    AUCUN_EVENEMENT = -1

    # action de Stanley quand on a appuyé sur la touche espace

    SPRAY = 1

    # état normal des fleurs, du chat, de la guêpe, de chaque chenille, de Stanley, etc.

    NORMAL = 0

    # état d'un ennemi quand il a terminé son parcours

    TERMINE = 1

    # état d'un ami quand il est touché par un ennemi (ex: le chat est touché par la guêpe)

    TOUCHE = 2

    # types d’ami

    FLEUR_HG = 0
    FLEUR_HD = 1
    FLEUR_BG = 2
    FLEUR_BD = 3
    CHAT = 4

    # types d'ennemi

    GUEPE = 0
    CHENILLE_G = 1
    CHENILLE_D = 2
    ARAIGNEE_G = 3
    ARAIGNEE_D = 4

    # valeur quand aucun ennemi ne doit être générer pour l’instant

    AUCUN_ENNEMI = 5