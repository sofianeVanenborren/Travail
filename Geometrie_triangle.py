# geométrie sur les triangles
from math import

def  aire ( base , hauteur ):
    Aire = (base*hauteur/2)
    return Aire

def  périmètre ( base , hauteur ):
   Périmètre = (base+hauteur)/2
   return Périmètre

si  __name__  ==  "__main__" :
    import  doctest
    doctest . testmod ()