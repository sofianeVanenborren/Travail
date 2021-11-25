# Exo 2
"""
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
"""
# Exo 4
"""
import math
class Point:
    def __init__(self,coord):
    self.abscisse = coord[0]
    self.ordonnee = coord[1]
    
    def __repr__(self):
        return "(" + str(self.abscisse) + "," + str(self.ordonnee) + ")"
    def distance(self):
        return math.sqrt(self.abscisse**2) + (self.ordonnee**2)
    
a = Point(-2,5)
b = Point(5,5)
c = Point(-2,2)
d = Point(5,-2)
"""
# Exo 5

class Fraction:
    def __init__(self,numera,denumera):
        self.numera = numera
        self.denumera = denumera
    
    def __repr__(self):
        if self.denumera == 1:
            return str(self.numera)
        else:
            return str(self.numera) + "/" + str(self.denumera)
        
    def __eq__(self,fract2):
        return self.numera/self.denumera == fract2.numera/fract2.denumera
    
    def __lt__(self,fract2):
        return self.numera/self.demunera < fract2.numera/fract2.denumera
    
    def __add__(self,fract2):
        return self.numera/self.denumera + fract2.numera/fract2.denumera
    
    def __mul__(self,fract2):
        return (self.numera * fract2.numera)/(self.denumera * fract2.denumera)
def pgcd(a,b):
    if b == 0:
        return a
    else:
        return pgcd (b,b%a)
    
        
    
f1 = Fraction(5,8)
f2 = Fraction(12, 35)
f1 == f2
f1 + f2
f1 * f2 
    

