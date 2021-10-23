#Sujet_9
def moyenne(l):
    a = 0
    b = 0
    for i in l:
        note = i[0]
        coef = i[1]
        a = a + note * coef
        b = b + coef
    return a/b
print(moyenne([(15,2),(9,1),(12,3)]))
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
print(pascal(4))
#sujet_17
def Indice_min(liste):
    minimum = liste[0]
    for x in liste:
        if x < minimum :
            minimum = x
    return minimum
print(Indice_min([5,3,2,2,4]))

def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j:
        if tab[i] == 0:
            i = i+1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j = j-i
    return tab
print(separe([0,1,0,1,1,1,0,0,1]))
