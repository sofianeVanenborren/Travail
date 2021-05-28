def recherche(liste, valeur):
    if valeur in liste:
        return True
    else:
        return False


#def recherche_indice(liste, valeur):


def recherche_minimum(liste):
    print(min(liste))
    return

def recherche_maximum(liste):
    print(max(liste))
    return

def moyenne(liste):
    print(sum(liste)/len(liste))

    
from random import randrange
liste = []
for i in range(100):
    liste.append(randrange(500))

print(liste)