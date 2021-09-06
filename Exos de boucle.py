liste1 = [5,25,67,54,12]
def recherche1(liste1,valeur1):
    """
    description: la foction recherche va consister a trouver une valeur a partir d'un indice'
    liste:(lst)
    valeur:(int)
    return (bool) = Cela va nous renvoyez vrai si la valeur est dans la liste sinon faux si elle n'est pas dans la liste
    """
    for elements in (liste1):
        if elements == valeur1:
            return True
    return False
print(recherche1(liste1 , 12))

# Recherche 2

liste2 = [15 , 44 , 89 , 7]
def recherche2(liste2 , valeur2):
    """
    description : trouver la valeur a partir d'un indice"
    liste: (lst)
    valeur : un entier (int)
    return : (bool) True ou False
    """
    for i in range(len(liste2)):
        if i == valeur2:
            return True
    return False
print(recherche2(liste2,2))

liste3 = [49 , 6 , 8 , 4]
def recherche3(liste , valeur3):
    i = liste[0]
    while i != len(liste3):
        if i != valeur3 :
            i =+ 1
            return False
    return True
print(recherche3(liste3, 8))
    
    