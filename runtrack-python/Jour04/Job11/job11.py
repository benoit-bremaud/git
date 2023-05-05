print("""\nProgramme Jour 4 - Job11
      \nÉcrire un programme qui créer la liste d'entiers L = [7, 11, 42, 39, 2]
      \nvotre programme devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la liste."""
      )

list = [7,11,42,39,2]

new_list = [x+1 for x in list] 

print(new_list)