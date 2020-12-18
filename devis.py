import geometrie
import math

def nombre_pots(longueur, largeur, surface_couvrante):
    nb_pots = (longueur+largeur+surface_couvrante)
    return nb_pots
print    
    

    

def nombre_baches(longueur, largeur, surface_couvrante):
    nb_baches = surface_couvrante/longueur*largeur
    return nb_baches
   
    
    

def nombre_rubans(longueur, largeur, perimetre_couvrante):
    nb_rubans = nombre_rubans/perimetre_couvrante
    return nb_rubans
    
    
    

def salaire(longueur, largeur):
    salaire = longueur*largeur/7.5
    return salaire

def est_reparation_couverte(total_couts):
    raparation_couverte(nombre_rubans + nombre_pots + nombre_rubans)
    return reparation_couverte
    return total_couts <= 500
