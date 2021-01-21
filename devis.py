import geometrie # On importe le code de "geometrie"
from math import # Et on importe le module "math"

def  nb_pots ( longueur , largeur , surface_couvrante ): # On donne le nom de la fonction "nb_pots" 
    nb_pots  = ( longueur + largeur + surface_couvrante ) # Utilisation des variables "longueur , largeur et surface_couvrante"
    retourne  nb_pots         

    

    

def  nb_baches ( longueur , largeur , surface_couvrante ): # Nom de la fonction qui est "nb_baches" avec ses 3 variables 
    nb_baches  =  surface_couvrante / longueur * largeur # Utilisation des 3 variables pour trouver la valeur de nb_baches 
    retourne  nb_baches

    
    

def  nb_rubans ( longueur , largeur , perimetre_couvrante ): # Nom de lafonction " nb_rubans" avec les même variables
    nb_rubans  =  nombre_rubans / perimetre_couvrante # Utilisations des 3 variables pour trouver la valeur de "nb_rubans"
    retourne  nb_rubans

    
    

def  salaire ( longueur , largeur ):
    salaire  =  longueur * largeur / 7.5
    retour  salaire

def  est_reparation_couverte ( total_couts ):
    raparation_couverte ( nb_rubans * 2,85  +  nombre_pots * 37,90  +  nombre_rubans * 0,95 )
    retour  reparation_couverte
    renvoie  total_couts  <=  500