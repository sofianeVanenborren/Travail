# Etape n°1
import random
nb = random.randint(0,22740)

fichier = open('fichier.md','r')
for i in range(nb):
    chaine = fichier.readline() #Chaine vaut 'Aaron\n
print(chaine)
fichier.close()

# Etape n°2

chaine = chaine.replace("é","e")
chaine = chaine.replace("è","e")
chaine = chaine.replace("ê","e")
chaine = chaine.replace("à","a")
chaine = chaine.replace("ù","u")
chaine = chaine.replace("û","u")
chaine = chaine.replace("î","i")
chaine = chaine.replace("ô","o")
print("-->",chaine)

Mot = len(chaine)-1
Symbole = chaine.replace(chaine," _")
print(Mot * Symbole)

# Etape n° 3

lettre=input("Mettre une lettre: ")
if lettre == chaine:
    print("Bravo , vous avez trouvé une lettre")
else:
    print("Dommage !!!")
while lettre == chaine:
    cpt = 10
    if lettre != chaine:
        cpt -= 1
        print("Il vous reste " + str(cpt) + " point de vie")
    break 



    
    
    

