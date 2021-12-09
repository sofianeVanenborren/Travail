
def creer_pile():
    """ Créé une pile vide
    :return: Une pile vide représentée par la liste vide
    """
    return []


def est_vide(p):
    """ Teste si une pile est vide
    :param p: Une pile
    :return: True si p est vide, False sinon
    """
    return p == []
    


def empiler(p, e):
    """ Empile un élément au sommet d'une pile
    :param p: Une pile
    :param e: Un élément
    :return: None
    :Effets: Empile e au sommet de p
    """
    p.append(e)
    

def depiler(p):
    """ Dépile un élément au sommet d'une pile et le renvoie
    :param p: Une pile
    :return: L'élément au sommet de la pile"
    :Précondition: p est non vide
    """
    assert not est_vide(p), "Impossible de dépiler une pile vide"
    return p.pop()
"""
# Exercice 1
def pile_alterne(n):
    p = creer_pile()
    for i in range(n):
        if i % 2 == 0:
            empiler(p,i)
        else:
            empiler(p,-i)
    return p
print(pile_alterne(7))
"""
"""
#Exercice 2
def vider_pile(pile):
    while not est_vide(pile):
        depiler(pile)
    
        
p = creer_pile()
empiler(p,1)
empiler(p,5)
empiler(p,15)
print(p)
vider_pile(p)
print(p)

def sommet_pile(pile):
    if est_vide(pile):
        return None
    else:
        res = depiler(pile)
        empiler(pile,res)
        return res
"""
"""
#Exercice 3
def est_bien_parenthesee(text):
    p = creer_pile()
    for i in text:
        if i == "(":
            empiler(p,"(")
        else:
            if est_vide(p) == False:
                depiler(p)
            else:
                return False
    return est_vide(p)
print(est_bien_parenthesee("((())())"))
print(est_bien_parenthesee("((())"))
print(est_bien_parenthesee("())("))
"""
#Exercie 7
# Partie 1

def est_balise_fermante(txt):
    return txt[0] == "<" and txt[1] == "/" and txt[-1] == ">"

def est_paire_balises(c1,c2):
    if c1[0] == "<" and c1[-1] == ">" and c2[0] == "<" and c2[1] == "/" and c2[-1] == ">":
        return True
    else:
        return False
print(est_balise_fermante("<div>"))
print(est_balise_fermante("</div>"))
print(est_paire_balises("<div>", "</div>"))
print(est_paire_balises("<div>", "</p>"))

# Partie 2

from myhtml_parser import html_to_str,MyHTMLParser

def verifier_html(txt):
    p = creer_pile()
    s = html_to_str("html_ex/ex1.html")
    parser = MyHTMLParser(s)
    while parser.has_tag():
        print(parser.next_tag())
    for i in txt:
        if i == "<":
            empiler(p,"<")
        else:
            if i == "</":
                depiller(p,"</")
            else:
                return False
    return est_vide
print(verifier_html("html_ex/ex1.html"))

        
 

    
            
        
        


        
    
