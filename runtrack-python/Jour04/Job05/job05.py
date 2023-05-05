print("""\nProgramme Jour 4 - Job05
\n\nÉcrire un programme qui créé une liste nommée “L” d'au moins 5 entiers puis successivement :
\t- Afficher la valeur de L[1]
\t- Écrire une fonction qui remplace L[3] par la somme des cases voisines L[2] & L[4]
\t- Puis afficher la valeur du dernier terme de la liste.""")

# Version 1
print("\nProgramme version 1 - sans 'fonction'")
print("\nCréation de la liste nommée 'L'")
L=[1,2,3,4,5] # Création d'une liste nommée 'L' avec 5 nombres entiers
print(L)

print("\nAffiche la valeur de L[1]")
print(L[0]) # La première valeur de la liste se trouve à l'index '0'

print("\nRemplace L[3] par la somme des cases voisines L[2] & L[4]")
L[3]=L[2]+L[4] # 
print(L)

print("\nRemplace L[3] par la somme des cases voisines L[2] & L[4] - version avec fonction")
def replace_add(x):
    x[3]=x[2]+x[4]
    print(x)
replace_add(L)

print("\nAfficher la valeur du dernier terme de la liste.")
print(L[-1])

# Version 2
print("\nProgramme version 2 - avec 'fonction'")
print("\nCréation de la liste nommée 'L'")
def replace_add2(x):
    x[3]=x[2]+x[4]

def new_list(X): # Définition de la fonction d'une liste nommée 'L' d'au moins 5 nombres entiers 'new_list'
    X=[1,2,3,4,5,6,7,8] # Création de la liste avec ses valeurs
    print("\nListe créée : "+ str(X)) # Affiche la liste créée
    print("\nValeur de L[1] : " + str(X[1])) # Affiche la valeur à l'index 1 de la liste
    replace_add2(X) #Appel de la fonction 'replace_add2(x)'
    print("\nL[2]+L[4] --> L[3] : " + str(X[3])) # Affiche la valeur à l'index 3 après avoir appelé la fonction replace_add2
    print("\nLa dernier valeur du tableau est : " + str(X[-1])) # Affiche la dernière valeur de la liste
new_list(L) # Appel de la fonction qui réalise toutes les actions de la fonction 'new_list()'

# Version 3
print("\nProgramme version 3 - avec 'fonction' et génération aléatoire des nombres dans la liste")

# Définition de la fonction qui va créer une liste de 5 nombres aléatoires compri entre 0 et 10
#import random

#def replace_add2(x):
  #  x[3]=x[2]+x[4]

#def new_list(X): # Définition de la fonction d'une liste nommée 'L' d'au moins 5 nombres entiers 'new_list'
 #   X=[1,2,3,4,5,6,7,8] # Création de la liste avec ses valeurs
  #  print("\nListe créée : "+ str(X)) # Affiche la liste créée
#    print("\nValeur de L[1] : " + str(X[1])) # Affiche la valeur à l'index 1 de la liste
#    replace_add2(X) #Appel de la fonction 'replace_add2(x)'
#    print("\nL[2]+L[4] --> L[3] : " + str(X[3])) # Affiche la valeur à l'index 3 après avoir appelé la fonction replace_add2
#    print("\nLa dernier valeur du tableau est : " + str(X[-1])) # Affiche la dernière valeur de la liste
#new_list(L) # Appel de la fonction qui réalise toutes les actions de la fonction 'new_list()'