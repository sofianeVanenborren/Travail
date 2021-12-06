# Exo 2

velo = {"id" : 1210, "typ" : "électrique" , "station" : "place d'italie" , "statut" : "en panne"}
velo["statut"] = "en déplacement"
print("dispo" in  velo.values())

#Exo2 bis:

velo1 = {"id" : 100, "typ" : "classique", "statut" : "en panne", "station" : "Chatelet"}
velo2 = {"id" : 230, "typ" : "électrique", "statut" : "en déplacement" , "station" : "place d'Acadie"}
velo3 = {"id" : 520, "typ" : "VTT" , "statut" : "en déplacemnt" , "station" : "Place Basse"}

parc_velib = []
parc_velib.append(velo1)
parc_velib.append(velo2)
parc_velib.append(velo3)

print(parc_velib)

def recherche_velo(parc_velib):
    for velo in parc_velib:
        if velo["statut"] == "en déplacemnt":
            return velo
print(recherche_velo(velo1))

def recherche_velo_bis(parc_velib):
    for velo in parc_velib:
        if velo["statut"] == "en déplacemnent":
            return velo["station"]
        

    
       
