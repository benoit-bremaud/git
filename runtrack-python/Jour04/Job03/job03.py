print("""\nProgramme Jour 4 - Job03
      \nÉcrire une fonction qui contient une liste nommée “fruits” qui contient les strings “pomme”, “cerise”, “orange”.
      \nCette fonction doit à son appel ajouter à la liste “fruits” une String “Melon” à la fin de cette liste.""")

# Version 1
print("\nProgramme version 1 - sans 'fonction'")

my_list = ["pomme","cerise","orange"]   # Création d'une liste et affectation dans la variable 'my_list'
my_list.append("Melon")
print(my_list)   # Affiche les éléments de la liste 'my_list' 

# Version 2 - en utilisant une fonction
print("\nProgramme version 2 - avec 'fonction'")
def add_fruit_end(food): # Déclaration de la fonction (add_fruit_end) avec comme argument string 'food'
    food.append("melon")
    print(food)    # affiche tous les éléments de la liste 'food'

fruit=["pomme","cerise","orange","poire","melon","cassis"]       # définition de la liste 'fruit' et affectation des valeurs (string)

add_fruit_end(fruit) #Appel de la fonction

# Version 3 - en utilisant une fonction + variable 'input()'

print("\nProgramme version 2 - avec 'fonction' + variable 'input()'")

def add_fruit_end(food): # Déclaration de la fonction (add_fruit_end) avec comme argument string 'food'
    
    fruit_to_add=input("Nom du fruit ? :") # Déclaration de la variable 'fruit_to_add' et demander à l'utilisateur de renseigner le fruit avec 'input()'

    food.append(str(fruit_to_add)) # Ajout du nouveau fruit dans la liste à la dernier place '__.append'

    print(food)    # affiche chaque élément de la liste 'food' du premier au dernier (boucle for)

fruit=["pomme","cerise","orange","poire","melon","cassis"]       # définition de la liste 'fruit' et affectation des valeurs (string)

add_fruit_end(fruit) #Appel de la fonction