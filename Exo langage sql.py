"""1) SELECT titre
   FROM livre

2) SELECT nom
   FROM usager

3) SELECT DISTINCT nom
   FROM usager

4) SELECT titre 
   FROM livre 
   WHERE annee <= 1980

5) SELECT * 
   FROM livre 
   WHERE titre LIKE '%A%'

6) SELECT livre.titre, emprunt.retour , emprunt.isbn , livre.isbn
   FROM emprunt JOIN livre 
                   ON emprunt.isbn = livre.isbn
   WHERE retour = '2020-01-01'

7) SELECT nom
   FROM auteur
   ORDER BY nom ASC

8) SELECT nom , cp
   FROM usager
   WHERE cp = 75012 AND cp = 75013

9)SELECT nom , adresse
  FROM usager
  WHERE not(adresse LIKE '%Rue%')

10) SELECT titre, annee
    FROM livre
    WHERE annee / 4 AND annee / 400"""