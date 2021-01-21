import geometrie
import math

def  nb_pots ( longueur , largeur , surface_couvrante ): # On donne le nom de la fonction "nb_pots" 
    nb_pots  = ( longueur + largeur + surface_couvrante ) # Utilisation des variables "longueur , largeur et surface_couvrante"
    retourne  nb_pots # Ici on cherche a savoir le nombre de pots
    
    

def  nb_baches ( longueur , largeur , surface_couvrante ): # Nom de la fonction qui est "nb_baches" avec ses 3 variables 
    nb_baches  =  surface_couvrante / longueur * largeur # Utilisation des 3 variables pour trouver la valeur de nb_baches 
    retourne  nb_baches # Ici on cherche le nombre de baches
    

def  nb_rubans ( longueur , largeur , perimetre_couvrante ): # Nom de lafonction " nb_rubans" avec les même variables
    nb_rubans  =  nombre_rubans / perimetre_couvrante # Utilisations des 3 variables pour trouver la valeur de "nb_rubans"
    retourne  nb_rubans # Ici on cherche le nombre de rubans
    

def salaire(longueur,largeur): # Nom de la fonction "salaire" 
    salaire_peintre = longueur*largeur/7.5 # On multiplie les 2 variables avec le prix que le peintre est payé qui est de 7.5 euros/mois
    return salaire_peintre # Ici on cherche le salaire du peintre 

def reparation_couverte(total,couts):
    cout_total = nb_pots + nb_baches + nb_rubans + salaire_peintre
    return cout_total # On cherche grace au couts de tous se qu'on a depuis le début pour savair si la reparation est couverte 
