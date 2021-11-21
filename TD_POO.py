import random
class Personnage:

    def __init__(self,nom,points_de_vie,capacite):
        self.vie = points_de_vie
        self.nom = nom
        self.power = capacite
          
    def perd_vie(self):
        if random.random() < 0.5:
            nbPoint = 1
        else:
            nbPoint = 2

        self.vie = self.vie - nbPoint
        print(self.nom + " à reçu " +str(nbPoint)+ " dégats!")
        return nbPoint
          
bilbo = Personnage("Bilbo",20)
gollum = Personnage("Gollum",20)
frodon = Personnage("Frodon", 20,)
araignee = Personnage("Araignée", 10)
aragorn = Personnage("Aragorn", 10)
orc = Personnage("Orc", 10)

def game(perso1, perso2):
    while perso1.vie > 0 and perso2.vie > 0:
        perte1 = perso1.perd_vie()
        print(perso1.nom + " perd" + str(perte1) + " points de vie")
        perte2 = perso2.perd_vie()
        print(perso2.nom + " perd " + str(perte2) + " points de vie")

    if perso1.vie <= 0 and perso2.vie > 0:
        msg = perso2.nom + " est vainqueur,il lui reste "+ str(perso2.vie) + " points de vie alors que " + perso1.nom + " est mort"
    elif perso2.vie <= 0 and perso1.vie > 0:
        msg = perso1.nom + " est vainqueur,il lui reste " + str(perso1.vie) + " points de vie alors que " + perso2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"

    return msg
        
