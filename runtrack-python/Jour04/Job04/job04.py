print("""\nProgramme Jour 4 - Job04
      \nÉcrire une fonction qui contient une liste nommée “fruits” qui contient les strings “pomme”, “cerise”, “orange, Melon”.
      \nCette fonction doit à son appel ajouter à la liste “fruits” une String “Mangue” à l'index 2."""
      )

# Version 1
print("\nProgramme version 1 - sans 'fonction'")

my_list = ["pomme","cerise","orange"]   # Création d'une liste et affectation dans la variable 'my_list'
my_list.insert(1,"Melon") # Ajout à la liste 'my_list' le string 'melon' à la position '1' (integer)
print(my_list)   # Affiche tous les éléments de la liste modifiée 'my_list' 

# Version 2 - en utilisant une fonction
print("\nProgramme version 2 - avec 'fonction'")
def add_fruit_index(food): # Déclaration de la fonction (add_fruit_index) avec comme argument string 'food'
    food.insert(1,"melon")
    print(food)    # affiche chaque élément de la liste 'food' du premier au dernier (boucle for)

fruit=["pomme","cerise","orange","poire","melon","cassis"]       # définition de la liste 'fruit' et affectation des valeurs (string)

add_fruit_index(fruit) #Appel de la fonction

# Version 2 bis - en utilisant une fonction et boucle for
print("\nProgramme version 2 bis - avec 'fonction' et boucle 'for'")
def add_fruit_index(food): # Déclaration de la fonction (add_fruit_index) avec comme argument string 'food'
    food.insert(1,"melon")
    for i in food: 
        print(i)    # affiche chaque élément de la liste 'food' du premier au dernier (boucle for)

fruit=["pomme","cerise","orange","poire","melon","cassis"]       # définition de la liste 'fruit' et affectation des valeurs (string)

add_fruit_index(fruit) #Appel de la fonction

# Version 3 - en utilisant une fonction + variable 'input()'

print("\nProgramme version 3 - avec 'fonction' + 2 variables 'input()' pour FRUIT et INDEX")

def add_fruit_end(x):    # Déclaration de la fonction (add_fruit_end) avec comme argument string 'food'
    fruit_to_add=input("\nNom du fruit ? :")    # Déclaration de la variable 'fruit_to_add' et demander à l'utilisateur de renseigner le fruit avec 'input()'
    index_numb=input("\nNuméro d'index ? (nombre entre 0 et " + str(len(x)) + ") ?:")    # Déclaration de la variable 'index_numb' et demander à l'utilisateur re renseigner un numéro
    x.insert(int(index_numb), str(fruit_to_add))     # Ajout du nouveau fruit dans la liste à la dernier place '__.append'
    print(x)    # affiche chaque élément de la liste 'food' du premier au dernier (boucle for)

fruit=["pomme","cerise","orange","poire","melon","cassis","pasteque","tomate"]       # définition de la liste 'fruit' et affectation des valeurs (string)

add_fruit_end(fruit) #Appel de la fonction