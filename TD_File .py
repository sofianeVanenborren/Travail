from file import *
from pile import *
# EX 2

def inv_file(file):
    P=pile()
    while not file.est_vide():
        P.empile(file.defile())
    while not P.est_vide():
        file.enfile(P.depile())
    return file

#EX 3

def separe(f):
    pair = File()
    impair = File()
    while not f.est_vide():
        x = f.depile()
        if x % 2 == 0:
            pair.enfile(x)
        else:
            impair.enfile(x)
    return pair,impair

# Ex 4
def taille(file):
    F = file()
    while not F.est_vide():
        for i in range(len(self.data)):
            s = s + str(self.data[i])
        return s
    return file

