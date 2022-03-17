import time
import graphviz
from IPython.display import display


WHITE = '#FFFFFF'
BLACK = '#000000'

class Node:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

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

def show_tree(arbre):
    """
    affichage des noeuds dans un notebook
    """
    display(graphviz.Source(to_dot(arbre)))


