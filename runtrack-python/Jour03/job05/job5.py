print("""\nProgramme Jour 3 - Job 5\n\nÉcrire un programme qui affiche les nombres premiers jusqu'à 1000.""")

# Définition d'un nombre premier :
# Un nombre premier est un nombre entier naturel (non nul) qui admet exactement 2 diviseurs distincts : 1 et lui-même.
# En d'autres termes c'est un nombre entier ('sans virgule'), plus grand que 1, et qui ne peut être divisé que par 1
# et par lui-même

# Boucle avec fonction RANGE + la boucle FOR
print("\nProgramme version - Version 1")

for numb in range(0,1001,1):    # Pour les nombres compris entre 0 et 1000 avec un incrément de +1
    if numb > 1:                # si le nombre est inférieur à 1, sauter la boucle for
        for i in range(2,numb): # La variable numb est > 1, alors on le divise par i avec -> 2 < i < numb
            if (numb % i) == 0:
                break
        else:
            print(numb)
print("\nFinisched !!")