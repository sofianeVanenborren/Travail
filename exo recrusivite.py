import timeit
def somme_iteratif(n):
    j = 0
    for j in range(n+1):
        j = j+n
    return j
print(somme_iteratif(4))

def somme_recursif(n):
    if n == 0 :
        return 0
    else : 
        return n + somme_recursif(n-1)

somme_recursif(100)


timeit.timeit("somme_recursif(1000)",number=50, setup="from_main_import somme_recursif")


    

        