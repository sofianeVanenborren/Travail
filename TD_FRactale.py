#Exercice 0
"""
import turtle
for i in range(1):
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.circle(30)
"""


# Exercice 1
"""
import turtle

def dessine(n):
    turtle.speed(100)
    if n < 0:
        turtle.penup
    else :
        turtle.forward(n)
        turtle.right(90)        
        dessine(n-2)
print(dessine(500))
"""
"""
import turtle

def dessine(n):
    turtle.speed(100)
    while n > 0:
        turtle.pendown
        turtle.forward(n)
        turtle.right(90)
        n = n - 2
print(dessine(500))
"""
# Exercice 2

"""
import turtle
def koch(n,l):             # # Fractacle de Koch
    if n == 0:
        turtle.forward(l)
    else:
        koch(n-1,l/3)
        turtle.left(60)
        koch(n-1,l/3)
        turtle.right(120)
        koch(n-1,l/3)
        turtle.left(60)
        koch(n-1,l/3)

def flocon(n,l):
    for i in range(3):
        koch(n,l)
        turtle.right(120)
flocon(3,200)
"""
# Exercice 3

import turtle
from math import sqrt
def carre(l,n):
    if n == 0:
        return None
    else:
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(100)
        #3. appel recursif à carre() de coté à calculer avec pythagore
carre(10,5)
        





        
        
        
      
        