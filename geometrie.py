def  aire ( longueur , largeur ): # On definis le nom de notre fonction qui va se nommer "aire"
    aire  = ( longueur * largeur ) / 2  # Ceci va nous permettre de trouver la valeur grace avec "longeur" et "largeur"  
    return  aire

    
def  perimetre ( longueur , largeur ): # On redonne un nom a cette fonction qui est "perimetre"
    perimètre = longueur + largeur * ( 2 ) # même principe comme pour le aire on utilise les variables "longeur" et "largeur"
    return  Perimètre

if  __name__  ==  "__main__" :
    import  doctest
    doctest . testmod ()