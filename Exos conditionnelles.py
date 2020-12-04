# Exercice 4 (Niveau intermédiaire)
def bowling(boule1, boule2):
    strike = "X"
    spare = "/"
    if boule1 == 10:
        return strike
    elif boule1 + boule2 == 10:
        return spare
    elif boule2 < 10:
        tt= boule1 + boule2
        return boule1 + boule2
print(bowling(5,0))
    
# Exercice 5 (Niveau intermédiaire)
def croissant(a,b,c):
    if a <= b:
        if b <= c:
            resultat = 'true '
        else :
           resultat = 'false'
    else :
        resultat = 'false'
    return resultat
print(croissant(1,2,6))

# Exercice 6 (Niveau intermédiare)
def annee_bissextile(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0 :
        result=("est une annee bissextile")
    else:
        result=("n'est pas une annee bissextile")
    return result
for i in range (2000,2050):
    print("L/'annee" + str(i) + annee_bissextile(i))






            
                   
    
        
 
 

