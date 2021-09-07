liste = [50 , 43 , 15 , 60]

def Moyenne(liste):
    moyenne1 = 0
    a = len(liste)
    '''
    description = trouver la moyenne a partir d'un element
    liste = la liste comporte des entiers
    return = une valeur , un entier
    '''
    for i in (liste):
        moyenne1 += i
    moyenne1 = moyenne1 / a
    return moyenne1
print(Moyenne(liste))

def Moyenne2(liste):
    moyenne2 = 0
    b = len(liste)
    '''
    description = trouver la moyenne a partir d'un indice
    liste = la liste comporte des entiers
    return = une valeur , un entier
    '''
    for i in range(len(liste)):
        moyenne2 = moyenne2 + liste[i]
    moyenne2 = moyenne2 / b 
    return moyenne2
print(Moyenne2(liste))

# Moyenne3 par boucle while

l = 0
c = len(liste)
while l != sum(liste):
    l = l + 1
    if l == sum(liste):
        print(l/ len(liste))