# geométrie sur les triangles
from math import # On importe le module "math"

def  aire ( base , hauteur ): # Nom ce la fonction qui se nomme "aire"
    Aire = (base*hauteur/2) # Re utilisation de la formule de mathematique pour trouver une aire 
    return Aire

def  périmètre ( base , hauteur ): # Nom de lafonction qui se nomme "périmètre"
   Périmètre = (base+hauteur)/2 # Re utilisation d'une formule de mathematique pour trouver un périmètre
   return Périmètre

si  __name__  ==  "__main__" :
    import  doctest
    doctest . testmod ()