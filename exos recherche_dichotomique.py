liste = [3 , 5 , 10 , 14 , 20 , 26]
def recherche_dichotomique(liste,valeur):
    droit = len(liste) -1
    gauche = 0
    while gauche <= droit:
        pivot = (gauche + droit)//2
        if liste[pivot] == valeur:
            return True
        if liste[pivot] < valeur:
            gauche = pivot + 1
        if liste[pivot] > valeur:
            droit = pivot - 1
    return False
print(recherche_dichotomique(liste,5))


        
        
    