import doctest

liste1 = [2,4,5,7,9]
liste2 = [6,8,12,21]
def comparer_tableau(liste1,liste2):
    """
    objectif = reussir a comparer un élément d'une liste et voir si elle est présentde dans chacune
    des listes
    paramétres = 2 listes (lst)
    """
    element_commun = []
    for element in liste1:
        if element in liste2:
            element_commun += element
    print(element_commun)
    return
print(comparer_tableau(liste,liste2))