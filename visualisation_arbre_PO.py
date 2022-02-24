import time
import graphviz
#import pydot
#from IPython.display import display
#import os

WHITE = '#FFFFFF'
BLACK = '#000000'

class File:
    def __init__(self):
        self.liste =[]
    def enfile(self, valeur):
        self.liste.append(valeur)
    def defile(self):
        return self.liste.pop(0)
    def est_vide(self):
        return self.liste == []

class Node:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
class Tree:
    def __init__(self, noeud=None):
        self.racine = noeud

def affiche_noeud(noeud) :
    if noeud is None:
        return
    file = File()
    file.enfile(noeud)
    print("(", end ="")
    while not file.est_vide():
        a = file.defile()
        print(a.valeur, end ="")
        if a.gauche is not None:
            file.enfile(a.gauche)
        if a.droit is not None:
            file.enfile(a.droit)
        if not file.est_vide():
            print(", ", end="")
    print(")")

def affiche(arbre):
    ''' 
    DESCRIPTION DE LA FONCTION :
        Affiche les valeurs des noeuds de l'arbre en la parcourant en largeur
    PARAMETRES :
    arbre : implémentation python de l'arbre à afficher (type : dépend de l'implémentation choisie)
    return None
    '''    
    if is_empty(arbre):
        print("( )")
        return
    affiche_noeud(arbre.racine)

def escape_str(obj):
    '''
    convertit l'objet obj en une chaîne de caractères ASCII
    fct utile pour méthode to_dot des BinaryTree
    '''
    chaine = str(obj)
    chaine_echap = ''
    for c in chaine:
        n = ord(c)
        if 32 <= n <= 126 and c != '"':
            chaine_echap += c
        else:
            chaine_echap += '\\x{:04X}'.format(n)
    return chaine_echap

def to_dot(node, background_color=WHITE):
    '''
    renvoie une chaîne de caractères contenant la description au format dot de self.
    '''
    LIEN = '\t"N({:s})" -- "N({:s})" [color="{:s}", label="{:s}", fontsize="8"];\n'
    def aux(noeud, prefix=''):
        if noeud is None:
            descr = '\t"N({:s})" [color="{:s}", label=""];\n'.format(prefix, background_color)
        else:
            c = noeud.valeur
            descr = '\t"N({:s})" [label="{:s}"];\n'.format(prefix, escape_str(c))
            s_a_g = noeud.gauche
            label_lien, couleur_lien = ('', BLACK) if not (s_a_g is None) else ('', background_color)
            descr = (descr + aux(s_a_g, prefix+'0') +
                     LIEN.format(prefix, prefix+'0', couleur_lien, label_lien))
            s_a_d = noeud.droit
            label_lien, couleur_lien = ('', BLACK) if not (s_a_d is None) else ('', background_color)
            descr = (descr + aux(s_a_d, prefix+'1') +
                     LIEN.format(prefix, prefix+'1', couleur_lien, label_lien))

        return descr
    
    return '''/*
  Binary Tree

  Date: {}

*/

graph G {{
\tbgcolor="{:s}";

{:s}
}}
'''.format(time.strftime('%c'), background_color, aux(node))

# def export(arbre, nom):
#     '''
#     visualise l'Node et produit deux fichiers : filename et filename.png
#     le premier contenant la description de l'Node au format dot, 
#     le second contenant l'image au format PNG.
#     Utilise le module pydot
#     '''
#     res = to_dot(arbre.racine)
#     (graph,) = pydot.graph_from_dot_data(res)
#     graph.write_png(nom + '.png')
#     os.system('xdg-open '+nom+'.png')


def show(arbre, nom_fichier, background_color=WHITE):
    '''
    DESCRIPTION DE LA FONCTION :
        Visualise l'Node et produit deux fichiers :
            * nom_fichier : description de l'arbre au format dot (non utile pour le TP)
            * nom_fichier.png : image de l'Node au format png
    PARAMETRES :
    Node : implémentation python de l'arbre à afficher (type : dépend de l'implémentation choisie)
    nom_fichier : nom du fichier sans l'extension (type : str)
    return None
    '''
    graphviz.Source(to_dot(arbre.racine, background_color=background_color),
                    format='png').view(filename=nom_fichier)

# def show_tree(arbre):
#     """
#     affichage des noeuds dans un notebook
#     """
#     display(graphviz.Source(to_dot(arbre.racine)))

def is_empty(arbre):
    return arbre.racine is None

def get_root(arbre):
    assert not(is_empty(arbre)) , "impossible : arbre vide"
    return arbre.racine.valeur

def get_left_subtree(arbre):
    assert not(is_empty(arbre)) , "impossible : arbre vide"
    return arbre.racine.gauche

def get_right_subtree(arbre):
    assert not(is_empty(arbre)) , "impossible : arbre vide"
    return arbre.racine.droit

if __name__ == '__main__':
    # Validation des tests
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    # arbre du cours
    arbre_vide = Tree()
    noeud = Node(2, Node(8, Node(6, None, None), Node(9, None, None)),
                  Node(1, Node(7, None, None), None))
    arbre = Tree(noeud)
    
    noeud = Node(1, None, None)
    feuille = Tree(noeud)
    
    noeud = Node(1, Node(1, Node(1, None, None), None), None)
    peigne_gauche = Tree(noeud)

    noeud = Node(1, None, Node(1, None, Node(1, None, Node(1, None, None))))
    peigne_droit = Tree(noeud)

    affiche(arbre)
    affiche(arbre_vide)
    affiche(feuille)
    affiche(peigne_gauche)
    affiche(peigne_droit)

    show(arbre, "arbre_main")