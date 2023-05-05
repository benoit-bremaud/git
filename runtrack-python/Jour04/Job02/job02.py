print("""\nProgramme Jour 4 - Job02
    \nÉcrire une fonction qui contient une liste nommée “fruits” qui contient les string “pomme”, “cerise”, “orange”.\nAffichez le 2e éléments de la liste.""")

# Version 1
print("\nProgramme version 1")

my_list = ["pomme","cerise","orange"]   # Création d'une liste et affectation dans la variable 'my_list'
print(my_list[2])  # Affiche le premier élément de la liste 'my_list' 

# Version 2 - en utilisant une fonction
print("\nProgramme version 2")
def list(food): # Déclaration de la fonction (list) avec comme argument string 'food'
        print(food)    # affiche chaque élément de la liste 'food' du premier au dernier (boucle for)

fruit=["pomme","cerise","orange","poire","melon","cassis"]       # définition de la liste 'fruit' et affectation des valeurs (string)

list(fruit)

print("\nCode : list(fruit[0])")
list(fruit[0])      # Appel fonction 'list' + argument 'fruit' - ici il affiche 'pomme' à la verticale

print("\nCode : list(fruit[0:1])")
list(fruit[0:1])    # Appel fonction 'list' + argument 'fruit' - ici il affiche 'pomme' à l'horizontale

print("\nCode : list(fruit[0:2])")
list(fruit[0:2])    # Appel fonction 'list' + argument 'fruit' - ici il affiche 'pomme' et 'cerise'

print("\nCode : list(fruit[0:3])")
list(fruit[0:3])    # Appel fonction 'list' + argument 'fruit' - ici il affiche 'pomme', 'cerise' et 'orange'

print("\nCode : list(fruit[0:4])")
list(fruit[0:4])    # Appel fonction 'list' + argument 'fruit' - ici il affiche 'pomme', 'cerise' et 'orange'

print("\nCode : list(fruit[0::2])")
list(fruit[0::2])    # Appel fonction 'list' + argument 'fruit' - ici il affiche 'pomme', 'cerise' et 'orange'

print("\nCode : list(fruit[1])")
list(fruit[1])

print("\nCode : list(fruit[2])")
list(fruit[2])

print("\nCode : list(fruit[:1])")
list(fruit[:1])

print("\nCode : list(fruit[:2])")
list(fruit[:2])

print("\nCode : list(fruit[0:1])")
list(fruit[0:1])

print("\nCode : list(fruit[1:2])")
list(fruit[1:2])    

print("\nCode : list(fruit[2:3])")
list(fruit[2:3])  