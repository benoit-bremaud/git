print("""\nProgramme Jour 4 - Job09
      \nÉcrire un programme qui calcule le maximum et le minimum des éléments de la liste
      L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]."""
      )

# Version 1


# trouver le plus grand dans la liste


def biggest_num(X):
    num = X[0]
    for element in X:
        if element > num:
            num = element
    print(str(num) + " est le le plus grand nombre de la liste\n")

def smallest_num(X):
    num = X[0]
    for element in X:
        if element < num:
            num = element
    print(str(num) + " est le le plus petit nombre de la liste\n")

L = [8,24,27,48,2,16,9,102,7,84,91]

smallest_num(L)
biggest_num(L)