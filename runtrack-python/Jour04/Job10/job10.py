print("""\nProgramme Jour 4 - Job10
      \nÉcrire un programme qui calcule le produit de toutes les valeurs de la liste
      comprises dans l'intervalle [25, 90] L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]."""
      )

# Version 1

# Définition de la variable 'liste' avec ses 'valeurs'
L=[8,24,27,48,2,16,9,102,7,84,91]

produit=1

for valeur in L:
    
    if valeur>=25 and valeur<=90:
        produit *= valeur

print(str(produit) + " est le résultat du produit de toutes les valeurs de la liste comprises entre [25,90]")