import geometrie
import math

def nb_pots(longueur, largeur, surface_couvrante):
    nb_pots = (longueur+largeur)/surface_couvrante
    return nb_pots
   
    

    

def nb_baches(longueur, largeur, surface_couvrante):
    nb_baches = surface_couvrante/longueur*largeur
    return nb_baches
   
    
    

def nb_rubans(longueur, largeur, perimetre_couvrante):
    nb_rubans = nombre_rubans/perimetre_couvrante
    return nb_rubans
    
    
    

def salaire(longueur, largeur):
    salaire = longueur*largeur/7.5
    return salaire

def est_reparation_couverte(total_couts):
    raparation_couverte(nombre_rubans + nombre_pots + nombre_rubans)
    return reparation_couverte
    return total_couts <= 500
