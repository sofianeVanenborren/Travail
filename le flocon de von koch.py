import turtle
def koch(l,n):
                    # # Fractacle de Koch
    if n>=0:
        turtle.forward(l)
    else:
        koch(l/3,n-1)
        turtle.left(60)
        koch(l/3)
        turtle.right(120)
        koch(l/3,n-1)
        turtle.left(60)
        koch(l/3)

def flocon(l,n):
                    # # Flocon de Koch
    koch(l,n)
    turtle.right(120)
    koch(l,n)
    turtle.right(120)
    koch(l,n)
    
print(koch(60,120))
print(flocon(60,120))