# Exercie 6 : NIveau intermédiaire

#(1) On est rentré dans la boucle for 2 fois
#(2) Ici on rentre dans la boucle 1 fois pour afficher false car le prenom Richard ne posséde pas de b
#(3) L'instruction du code qui réalise cette différence if lettre == c:

def rechercheIndice(chaine,c):
    cpt =0
    for lettre in chaine:
        if lettre == c:
            return cpt
        cpt +=1
    return False        
print(rechercheIndice("Stallmann","a"))
print(rechercheIndice("Richard","b"))


# Exercice 7 : Niveau intermédiaire
# Cette fonction aditionne les 2 valeurs a la fin

def mystere(n):
    s = 1
    n = str(n)
    for i in range(len(n)):
        s = s * int(n[i])
    return s
print(mystere(4132))
print(mystere(9045))
print('\n')

# Exercie 10 : Niveau intermédiaire

def est_premier(nombre):
    nb =1
    cpt =0
    while nb <= nombre:
        if nombre % nb == 0:
            cpt += 1
        nb += 1
    if cpt <= 2:
        return ("c'est un nombre premier")
    else:
        return ("raté")
print(est_premier(11))
    
    
    
        