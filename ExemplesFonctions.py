## Définitions des fonctions appelées dans le cours

def dis_bonjour():
    """
    Description de la fonction : Affiche un message de bienvenue au monde entier !
    return (None)
    """
    print("Hello World !!")
    
def tirage_de_6_faces():
    """
    Description de la fonction : Tire au hasard un nombre entre 1 et 6
    return (int)
    """
    from random import randint
    return randint(1,6)

def tirage_de_10_faces():
    """
    Description de la fonction : Tire au hasard un nombre entre 1 et 10
    return (int)
    """
    from random import randint
    return randint(1,6)

def racine(x):
    """
    Description de la fonction : Calcule la racine carrée d'un nombre
    parametre : x (int ou float)
    Préconditions sur les paramètres : x >= 0
    return (float)
    """
    from math import sqrt
    return sqrt(x)

def est_majeur(jour,mois,annee):
    """
    Description de la fonction : Détermine si l'individu dont la date de naissance est passée en paramètre est majeur
    parametre : jour (int)
    parametre : mois (int)
    parametre : annee (int)
    Préconditions sur les paramètres : 1<=jour<=31     1<=mois<=12      1<=annee<=9999
    return (bool)
    """
    import datetime
    return datetime.date.today() - datetime.date(annee,mois,jour) >= datetime.timedelta(days=18*365.25) 
