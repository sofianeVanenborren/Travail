# geométrie sur les triangles
import math

def aire(base, hauteur):
    aire = (base*hauteur)/2
    return aire
    pass
    
def perimetre(base, hauteur):
    bc = sqrt (base **2 + hauteur**2)
    peri = bc+base +hauteur
    return peri
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
