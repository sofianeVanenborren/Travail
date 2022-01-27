from pile import * 
class File:
    def __init__(self): # les éléments sont stockés dans 2 piles
        self.p_entree = Pile()
        self.p_sortie = Pile()

        
    def est_vide(self):

    
    def enfile(self,x):
        self.p_entree.empile(x) # x represente les éléments qui a dans la pile d'entree
        
    def defile(self):
        assert not self.est_vide(), "vous avez essayé de défiler une pile vide"
        while not p_sortie.est_vide():
            self.p_sortie.empiler(x)
