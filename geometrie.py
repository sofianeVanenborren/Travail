def aire(longueur, largeur):
    aire = (longueur*largeur)/2
    return aire

    
def perimetre(longueur, largeur):
    Perimetre=longueur+largeur*(2)
    return Perimetre

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    