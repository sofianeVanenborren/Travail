# Exercice 1: niveau facile
var = "Le Python\nc'est super"
print(len(var))
print(var[9])
print(var[-3])
print(var[3:7])
print(var)
# Le n permet de mettre la suite du texte en dessous
# Le len va me donner en combier de lettres est faite la variable var
# Le 9 va me donner le caractére \
# Le -3 va me donner le caractére p car Python compte a l'envers grâce au -
# Le 3:7 va me donner les caractéres L,e,P,y,t,h mais pas le 7éme car il est exclus
# L'instruction pour trouver 'y' est var[4]
# L'instruction sera var[16] ou var[-4]

# Exercice 2 :  niveau intermédiaire
print(var.find("t"))
print(var.find("e"))
print(var.find(" "))
print(var.find("p"))
print(var.find("c'est"))
print(var.find("z"))

# Exercie 3 : Niveau interédiaire
def commence_par_majuscule(mot):
    lettre = mot[0]
    sortie = lettre.isupper()
    return sortie
print(commence_par_majuscule("Bonjour"))
print(commence_par_majuscule("python"))   

    

