def  aire ( longueur , largeur ):
    aire  = ( longueur * largeur ) / 2
    retour  aire

    
def  perimetre ( longueur , largeur ):
    Périmètre = longueur + largeur * ( 2 )
    retour  Périmètre

si  __name__  ==  "__main__" :
    import  doctest
    doctest . testmod ()