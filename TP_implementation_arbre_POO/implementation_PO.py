from visualisation_arbre_PO import *
from random import randint

# IMPLEMENTATION DE LA CLASSE NOEUD

class Noeud:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

# PARTIE 2 - CODE ET TESTS A ECRIRE

class Arbre:
    def __init__(self, noeud=None):
        self.racine = noeud

    def est_vide(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est vide
        return (bool) : True si l'arbre est vide, False sinon
        
        TESTS :
        >>> arbre_du_cours.est_vide()
        False
        
        >>> arbre_feuille.est_vide()
        False
        
        >>> arbre_vide.est_vide()
        True
        '''
        if self.racine is None:
            return True
        else:
            return False
        
    def est_feuille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Détermine si l'arbre est une feuille
        return (bool) : True si l'arbre est une feuille, False sinon
        
        TESTS :
        >>> arbre_du_cours.est_feuille()
        False
        >>> arbre_feuille.est_feuille()
        True
        >>> arbre_vide.est_feuille()
        False
        '''
        if self.racine == noeud:
            return True
        else:
            return False


    def valeur_racine(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie la valeur de la racine de l'arbre
        return (int, str, etc...) : Valeur de la racine de l'arbre
        précondition : Il ne faut pas que l'arbre soit vide
        
        TESTS :
        >>> arbre_du_cours.valeur_racine()
        2
        >>> arbre_feuille.valeur_racine()
        1
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert not self.est_vide(), "On ne peut pas verifier la racine si l'arbre est vide" 
        # Code de la fonction à compléter
        return self.racine.valeur


    def SAG(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
        return (Arbre) : sous-arbre gauche
        précondition : il faut que l'arbre ne soit pas vide 
        
        TESTS :
        >>> affiche(arbre_du_cours.SAG())
        (8, 6, 9)
        
        >>> affiche(arbre_feuille.SAG())
        ( )
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert not self.est_vide() ,"l'arbre n'a pas de sous-arbre gauche" 
        # Code de la fonction à compléter
        return Arbre(self.racine.gauche)
    
    def SAD(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Renvoie le sous-arbre droit de l'arbre
        return (Arbre) : sous-arbre droit
        précondition : il faut que l'arbre ne soit pas vide
        
        TESTS :
        >>> affiche(arbre_du_cours.SAD())
        (1, 7)
        >>> affiche(arbre_feuille.SAD())
        ( ) 
        '''
        # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
        assert not self.est_vide()," l'arbre ne possede pas de sous-arbre droit " # A compléter
        # Code de la fonction à compléter
        return Arbre(self.racine.droit)
        
    
    def taille(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la taille d'un arbre
        return (int) : Taille de l'arbre
        
        TESTS :
        >>> arbre_du_cours.taille()
        6
        >>> arbre_feuille.taille()
        1
        >>> arbre_vide.taille()
        0
        '''
        if self.est_vide():
            return 0
        else:
            return 1 + Arbre(self.racine).SAG().taille() + Arbre(self.racine).SAD().taille()
        
        

    def hauteur(self):
        '''
        DOCUMENTATION :
        Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
                donnée dans l'énoncé
        return (int) : Hauteur de l'arbre
        
        TESTS :
        >>> arbre_du_cours.hauteur()
        2
        
        >>> arbre_feuille.hauteur()
        0
        
        >>> arbre_vide.hauteur()
        -1
        '''
        

    def est_egal(self, arbre):
        '''
        DOCUMENTATION :
        Description de la fontion : détermine si deux arbres sont identiques ou différents
        arbre (Arbre) : arbre sur lequel on va tester l'égalité
        return (bool) : True si les deux arbres sont identiques, False sinon 
        
        TESTS :
        '''
        #A compléter   

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter   
        
def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (Arbre) : arbre créé
    '''
    #A compléter 

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
noeud = Noeud(2, Noeud(8, Noeud(6, None, None), Noeud(9, None, None)), Noeud(1, Noeud(7, None, None), None))
arbre_du_cours = Arbre(noeud)
#show(arbre_du_cours,"arbre_du_cours")

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
noeud = Noeud(1,None,None)
arbre_feuille = Arbre(noeud)
#show(arbre_feuille,"arbre_feuille")

arbre_vide = Arbre()
#show(arbre_vide,"arbre_vide")
 
# PARTIE 2 - Question 3
        
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter

# PARTIE 2 - Question 4
    # A compléter
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)