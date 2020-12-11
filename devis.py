import geometrie
import math

def nombre_pots(longueur, largeur, surface_couvrante):
    aire= (longueur*largeur)/2
    return aire
    
    

    

def nombre_baches(longueur, largeur, surface_couvrante):
    nombre_baches = surface_couvrante/longueur*largeur
    return nombre_baches
   
    
    

def nombre_rubans(longueur, largeur, perimetre_couvrante):
    rubans_necessaire = nombre_rubans/perimetre_couvrante
    return rubans_necessaire
    
    
    

def salaire(longueur, largeur):
    salaire = 
    
    
    
    
    

def est_reparation_couverte(total_couts):
    """
    Indique si les réparations sont couvertes
    paramètre total_couts (float) ; valeur totale des coûuts
    retour (bool) : True si le forfait couvre l'ensemble des coûts
    pré-conditions : le total des coûts est strictement positif
    post-conditions : Néant
    """
    return total_couts <= 500