"""
def nombre_de_chiffre(x):
    if x < 10:
        return 1
    else:
        return nombre_de_chiffre(x//10) + 1

print(nombre_de_chiffre(34639))


def appartient(v,t,i):
    if v == t[i]:
        return True
    elif t[-1] == t[i]:
        return False
    else:
        return appartient(v,t,i +1)
ma_liste = ['foo', 'bar', 'spam', 'ham', 'eggs']
print(appartient('spam', ma_liste, 1))
print(appartient('spam', ma_liste, 2))
print(appartient('spam', ma_liste, 3))
"""
# Exercice 9

def est_palindrome


        
        
