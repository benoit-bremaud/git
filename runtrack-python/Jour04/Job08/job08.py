print("""\nProgramme Jour 4 - Job08
      \nÉcrire un programme qui calcule la somme de toutes les valeurs paires de la liste L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91].""")

L = [8,24,27,48,2,16,9,7,84,91]
som = 0
print(L)
#print(len(L))
for i in range(len(L)):
    
    if L[i]%2 == 0:
        som = som + L[i]
print(som)

# Autre version
somme=0
for valeur in L:
    if valeur%2==0:
        somme += valeur
print(somme)