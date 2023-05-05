print("""\nProgramme Jour 4 - Job01
      \nÉcrire une fonction qui retourne une liste nommée “fruits” qui contient les string “pomme”, “cerise”, “orange”..""")

# Version 1
print("\nProgramme version 1 - sans utiliser de fonction")
my_list = ["pomme","cerise","orange"]   # Création d'une liste et affectation dans la variable 'my_list'
print(my_list)  # Affiche la liste 'my_list' 

# Version 2 - en utilisant une fonction
print("\nProgramme version 2 - avec fonction")
def list(food): # Déclaration de la fonction (list) avec comme argument string 'food'
        print(food)    # affiche chaque élément de la liste 'food' du premier au dernier (boucle for)

fruit=["pomme","cerise","orange"]       # définition de la liste 'fruit' et affectation des valeurs (string)

list(fruit)                             # Ici on appelle la fonction 'list' définie plus haut, mais enchangeant 'food' par 'fruit'

# Version 3 - définition de plusieurs listes diverses
print("\nProgramme version 3")          # la liste 'fruit' est déjà définie plus haut

legume=["carotte","pomme de terre","haricot"]   # définition d'une nouvelle liste 'legume'
boisson=["eau","bière","soda","eau gazeuse"]    # une autre liste 'boisson'

# maintenant nous allons appeler la fonction 'list(food)' et remplacer 'food' par soit 'legume', 'boisson'...

list(legume)

list(boisson)