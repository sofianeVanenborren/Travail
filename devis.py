import geometrie # On importe le code de "geometrie"
from math import # Et on importe le module "math"

def  nb_pots ( longueur , largeur , surface_couvrante ): # On donne le nom de la fonction "nb_pots" 
    nb_pots  = ( longueur + largeur + surface_couvrante ) # Utilisation des variables "longueur , largeur et surface_couvrante"
    retourne  nb_pots # Ici on aura le nombre de pots de peinture         

    

    

def  nb_baches ( longueur , largeur , surface_couvrante ): # Nom de la fonction qui est "nb_baches" avec ses 3 variables 
    nb_baches  =  surface_couvrante / longueur * largeur # Utilisation des 3 variables pour trouver la valeur de nb_baches 
    retourne  nb_baches # Ici on aura le nombre de baches 

    
    

def  nb_rubans ( longueur , largeur , perimetre_couvrante ): # Nom de lafonction " nb_rubans" avec les même variables
    nb_rubans  =  nombre_rubans / perimetre_couvrante # Utilisations des 3 variables pour trouver la valeur de "nb_rubans"
    retourne  nb_rubans # Ici on aura le nombre de rubans

def  salaire ( longueur , largeur ): # Nom de la fonction "salaire"
    salaire  =  longueur * largeur / 7.5  # On multiplie les 2 variables avec le prix que le peintre est payé qui est de 7.5 euros/mois
    retour  salaire # Ici on aura le salaire 

def  est_reparation_couverte ( cout_total ): # Nom de la fonction
    raparation_couverte ( nb_rubans * 2,85  +  nombre_pots * 37,90  +  nombre_rubans * 0,95 ) #On aditionne tous les fonctions qu'on a faite depuis le debut
    return reparation_couverte # Et grace a tous on pourra trouver si la reparation est couverte ou non 
    return cout_total <=  500

    
    

def  salaire ( longueur , largeur ):
    salaire  =  longueur * largeur / 7.5
    retour  salaire

def  est_reparation_couverte ( total_couts ):
    raparation_couverte ( nb_rubans * 2,85  +  nombre_pots * 37,90  +  nombre_rubans * 0,95 )
    retour  reparation_couverte
    renvoie  total_couts  <=  500