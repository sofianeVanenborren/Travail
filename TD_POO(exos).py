# Exo 2
from math import sqrt

class TriangleRectangle:
    def __init__(self,cote1,cote2):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hypothenuse = sqrt(self.cote1**2 + self.cote2**2)
    
    def get_cote1(self):
        return self.cote1
    def get_cote2(self):
        return self.cote2
    def get_hypothenuse(self):
        return self.hypothenuse
    
    def set_cote1(self,nb):
        self.cote1 = nb
        self.hypothenuse = sqrt(self.cote1**2 + self.cote2**2)
    def set_cote2(self,nb):
        self.cote2 = nb
        self.hypothenuse = sqrt(self.cote1**2 + self.cote2**2)
        

triangle = TriangleRectangle(12,15)
print(triangle.cote1)
print(triangle.cote2)
print(triangle.hypothenuse)

# Exo 4
def nom_de_la_fonction(parametre1,parametre2):
    """
    Description de la fonction : 
    parametre1 (type) : 
    parametre2 (type) :
    return (type) :
    """

