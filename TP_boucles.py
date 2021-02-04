# Exercice 1 : Niveau facile

for i in range(2,9):
    print(i)
print('\n')

for i in range(0,28,4):
    print(i)
print('\n')

for maChaine in str('informatique'):
    print(maChaine)
print('\n')
 
# Exercice 2 : Niveau facile

for i in range(10):
    print("Pour progresser en programmation, la pratique est le plus important")
print('\n')

# Exercice 3 : Niveau facile

def tableDeMultiplication(val):
    for i in range(11):
        table = val * i
        print(val ,"*",i,"=",table)
print(tableDeMultiplication(7))
print('\n')

def Multiplication(val):
    for i in range(11):
        table = val * i
        print(val,"*",i,"=",table)
print(Multiplication(9))
print('\n')

def Multiple(val):
    for i in range(10):
        result = str(val) +' * '+str(i+1) +' = '+str((i+1)*val)
        print(result)
Multiple(5)
print('\n')


# Exercie 4 : Niveau intermediaire

def nombreCaracteres(chaine):
    compteur = 0
    for i in chaine:
        compteur += 1
    print(compteur)   
nombreCaracteres("chaine")
print('\n')

# Exercice 9 : Niveau intermediaire

def repetition(chaine,n):
    m = ''
    for c in chaine:
        



