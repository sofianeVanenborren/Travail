import time
import graphviz
#import pydot
#from IPython.display import display
#import os

WHITE = '#FFFFFF'
BLACK = '#000000'

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

def to_dot(arb, background_color=WHITE):
    '''
    renvoie une chaîne de caractères contenant la description au format dot de self.
    '''
    LIEN = '\t"N({:s})" -- "N({:s})" [color="{:s}", label="{:s}", fontsize="8"];\n'
    def aux(arbre, prefix=''):
        if is_empty(arbre):
            descr = '\t"N({:s})" [color="{:s}", label=""];\n'.format(prefix, background_color)
        else:
            c = get_root(arbre)
            descr = '\t"N({:s})" [label="{:s}"];\n'.format(prefix, escape_str(c))
            s_a_g = get_left_subtree(arbre)
            label_lien, couleur_lien = ('', BLACK) if not is_empty(s_a_g) else ('', background_color)
            descr = (descr + aux(s_a_g, prefix+'0') +
                     LIEN.format(prefix, prefix+'0', couleur_lien, label_lien))
            s_a_d = get_right_subtree(arbre)
            label_lien, couleur_lien = ('', BLACK) if not is_empty(s_a_d) else ('', background_color)
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
'''.format(time.strftime('%c'), background_color, aux(arb))

# def export(arbre, nom):
#     '''
#     visualise l'arbre et produit deux fichiers : filename et filename.png
#     le premier contenant la description de l'arbre au format dot, 
#     le second contenant l'image au format PNG.
#     Utilise le module pydot
#     '''
#     res = to_dot(arbre)
#     (graph,) = pydot.graph_from_dot_data(res)
#     graph.write_png(nom + '.png')
#     os.system('xdg-open '+nom+'.png')


def show(arbre, nom_fichier, background_color=WHITE):
    '''
    DESCRIPTION DE LA FONCTION :
        Visualise l'arbre et produit deux fichiers :
            * nom_fichier : description de l'arbre au format dot (non utile pour le TP)
            * nom_fichier.png : image de l'arbre au format png
    PARAMETRES :
    arbre : implémentation python de l'arbre à afficher (type : dépend de l'implémentation choisie)
    nom_fichier : nom du fichier sans l'extension (type : str)
    return None
    '''
    graphviz.Source(to_dot(arbre, background_color=background_color),
                    format='png').view(filename=nom_fichier)

# def show_tree(arbre):
#     """
#     affichage des arbres dans un notebook
#     """
#     display(graphviz.Source(to_dot(arbre)))

def is_empty(arbre):
    return arbre == []

def get_root(arbre):
    assert not(is_empty(arbre)) , "impossible : arbre vide"
    return arbre[0]

def get_left_subtree(arbre):
    assert not(is_empty(arbre)) , "impossible : arbre vide"
    return arbre[1]

def get_right_subtree(arbre):
    assert not(is_empty(arbre)) , "impossible : arbre vide"
    return arbre[2]

if __name__ == '__main__':
    # Validation des tests
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    # Arbre du cours
    arbre = [2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]]
    show(arbre, "arbre_main")