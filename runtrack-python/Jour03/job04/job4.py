print("""\nProgramme Jour 3 - Job 4\n\nProgramme qui itère les nombres entiers de 1 à 100.
\nPour les multiples de trois, afficher "Fizz" au lieu du nombre
Pour les multiples de cinq afficher "Buzz".
Pour les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".""")

# Les nombres multiples de 5 finissent par 5 ou par 0 ou calculer le modulo qui doit être égal à 0

# Pour trouver les multiples de 3, il faut additionner tous les chiffres composant le nombre :
# si le total est égal à 3, 6 ou 9, c'est bien un multiple de 3.
# Ex. : si l'on additionne le 1 et le 2 du nombre 12, on trouve  3 (1 + 2 = 3) donc 12 est un multiple de 3 (3 × 4 = 12).
# Ex. : Si l'on additionne les chiffres du nombre 213 840, on trouve 2 + 1 + 3 + 8 + 4 = 18
#   on additionne ensuite les chiffres du nombre 18 : 1 + 8 = 9 ; 213 840 est un multiple de 3

# Boucle avec fonction RANGE + la boucle FOR
print("\nProgramme version - Version 1")
for numb in range(1,100,1):    # Pour les nombres compris entre 1 et 100 avec un incrément de +1
    if numb % 3 and numb % 5 == 0:
        numb = "FizzBuzz"
    elif numb % 3 == 0:
        numb = "Fizz"
    elif numb % 5 == 0:
        numb = "Buzz"
    print(numb)
else:
    print("\nFinisched !!")