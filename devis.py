importer la  géométrie
importer des  mathématiques

def  nb_pots ( longueur , largeur , surface_couvrante ):
    nb_pots  = ( longueur + largeur + surface_couvrante )
    retourne  nb_pots         

    

    

def  nb_baches ( longueur , largeur , surface_couvrante ):
    nb_baches  =  surface_couvrante / longueur * largeur
    retourne  nb_baches

    
    

def  nb_rubans ( longueur , largeur , perimetre_couvrante ):
    nb_rubans  =  nombre_rubans / perimetre_couvrante
    retourne  nb_rubans

    
    

def  salaire ( longueur , largeur ):
    salaire  =  longueur * largeur / 7.5
    retour  salaire

def  est_reparation_couverte ( total_couts ):
    raparation_couverte ( nb_rubans * 2,85  +  nombre_pots * 37,90  +  nombre_rubans * 0,95 )
    retour  reparation_couverte
    renvoie  total_couts  <=  500