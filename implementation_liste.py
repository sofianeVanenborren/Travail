from visualisation_arbre import *
from random import randint

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
arbre_du_cours = [2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]]
#show(arbre_du_cours,"arbre_du_cours")

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
arbre_feuille = [1,[],[]]
#show(arbre_feuille,"feuille")

# # PARTIE 2 - CODE ET TESTS A ECRIRE

arbre_vide = []
#show(arbre_vide,"arbre_vide")
def est_vide(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si un arbre est vide
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est vide, False sinon
    
    TESTS :
    >>> est_vide(arbre_du_cours)
    False
    
    >>> est_vide(arbre_feuille)
    False
    
    >>> est_vide(arbre_vide)
    True
    '''
    # return arbre == []
    if arbre == []:
        return True
    else:
        return False 

def est_feuille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si l'arbre est une feuille
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est une feuille, False sinon
    
    TESTS :
    >>> est_feuille(arbre_du_cours)
    False
    
    >>> est_feuille(arbre_feuille)
    True
    
    >>> est_feuille(arbre_vide)
    False
    
    '''
    if est_vide(arbre):
        return False
    elif arbre[1] == [] and arbre[2] == []:
        return True
    else:
        return False

def racine(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie la valeur du noeud racine
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int, str, etc...) : Valeur du noeud racine
    précondition : l'arbre ne doit pas être vide 
    
    TESTS :
    >>> racine(arbre_du_cours)
    2
    
    >>> racine(arbre_feuille)
    1
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert not est_vide(arbre), "l'arbre ne doit pas être vide" # A compléter
    # Code de la fonction à compléter
    return arbre[0]

def SAG(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre gauche
    précondition : le sous-arbre gauche ne doit pas être vide 
    
    TESTS :
    >>> SAG(arbre_du_cours)
    [8, [6, [], []], [9, [], []]]
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert not est_vide(arbre[1]), "le sous arbre gauche ne doit pas être vide" # A compléter
    # Code de la fonction à compléter
    return arbre[1]

def SAD(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre droit de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre droit
    précondition : le sous-arbre droit ne doit pas être vide 
    
    TESTS :
    >>> SAD(arbre_du_cours)
    [1, [7, [], []], []]
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail) 
    assert not est_vide(arbre[2]), "le sous-arbre droit ne doit pas être vide" # A compléter
    # Code de la fonction à compléter
    return arbre[2]

def taille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la taille d'un arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Taille de l'arbre
    
    TESTS :
    >>> taille(arbre_du_cours)
    6
    >>> taille(arbre_feuille)
    1
    >>> taille(arbre_vide)
    0
    '''
    if not est_vide(arbre):
        return 0
    else:
        return 1 + taille(SAG) + taille(SAD)

def hauteur(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
            donnée dans l'énoncé
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Hauteur de l'arbre
    
    TESTS :
    '''
    # A compléter

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def est_egal(arbre1, arbre2):
    '''
    DOCUMENTATION :
    Description de la fontion : détermine si deux arbres sont identiques ou différents
    arbre1 (list) : Arbre implémenté sous forme de listes imbriquées
    arbre2 (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si les deux arbres sont identiques, False sinon 
    
    TESTS :
    '''
    # A compléter

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    
    # PARTIE 2 - Question 3
    
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter
    
    # PARTIE 2 - Question 4 
    # A compléter