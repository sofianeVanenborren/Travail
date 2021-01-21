def  aire ( longueur , largeur ): # On definis le nom de notre fonction qui va se nommer "aire"
    aire  = ( longueur * largeur ) / 2  # Utilisation d'une formule de math pour trouver l'aire 
    return  aire # Ici on trouvera l'aire 

    
def  perimetre ( longueur , largeur ): # On redonne un nom a cette fonction qui est "perimetre"
    perimètre = longueur + largeur * ( 2 ) # Utilisation d'une formule de math pour trouver un perimetre
    return  Perimètre # Ici on trouvera le perimètre 

if  __name__  ==  "__main__" :
    import  doctest
    doctest . testmod ()