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

Mot = len(chaine)
Symbole = chaine.replace(chaine," _")
print(int(Mot) * Symbole)

# Etape n° 3
tentatives = 6
affichage = ""
lettres_trouvees = ""

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in chaine:
      lettres_trouvees = lettres_trouvees + proposition
      print("--> Correct")
  else:
    tentatives = tentatives - 1
    print("-> Dommage\n")
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||        0  ")
    if tentatives<=3:
        print(" ||       /|\ ")
    if tentatives<=4:
        print(" ||       / \ ")
    if tentatives<=5:                    
        print(" ||           ")
    if tentatives<=6:
        print("==============\n")

  affichage = ""
  for x in chaine:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")

    

        
    

    


    