#TP_1_sac_a_dos:

listeObjet = [[7,12],[4,11],[3,8],[3,10]]

def tri(objet):
    return objet[0]/objet[1]


listeObjet_trié = sorted(listeObjet, key = tri, reverse = True)
poids_sac = 0
sac = []
'''
for objets in listeObjet_trié:
    if poids_sac + objets[1] <= 30:
        sac.append(objets)
        poids_sac = poids_sac + objets[1]
'''
i = 0 
objet = listeObjet_trié[0]
while poids_sac + objet[1] <= 30 and i < len(listeObjet_trié) :
    sac.append(objet)
    poids_sac = poids_sac + objet[1]
    i = i + 1
    objet = listeObjetTrié[i]       

#TP_2_rendu_monnaie:
    
systeme_pieces = [200, 100, 50, 20, 10, 5, 2, 1]

def rendu_monnaie(a_rendre,systeme_pieces):
    i = 0
    # tant que tes pieces sont = a ce que tu dois rendre
    # renvoie tes pieces en centimes
    # il prend le nombre le plus proche du rendu,
    # rendu = 80 , tes piéces a donner sont = 50,20,10 , donc piece = 80 et rendu = 80
    # fonction reussi
    
    

