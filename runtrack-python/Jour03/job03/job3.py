print("\nProgramme Jour 3 - Job 3\n\nAffiche tous les nombres de 0 à 100 compris, SAUF 26, 37, 88")

# Boucle avec fonction RANGE + la boucle FOR
print("\nBoucle avec FOR + RANGE - Version 1")
for numb in range(101):
    if numb == 26:
        continue
    if numb == 37:
        continue
    if numb == 88:
        continue
    print(numb)
else:
    print("\nFinisched !!")

print("\nBoucle avec FOR + RANGE - Version 2")
for numb in range(101):
    if numb == 26 or numb == 37 or numb == 88: # Les variables interdites sont dans la boucle FOR
        continue
    print(numb)
else:
    print("\nFinisched !!")

print("\nBoucle avec FOR + RANGE - Version 3")

numbnot = (26,37,88) # Les variables interdites ne sont pas dans la boucle FOR

for numb in range(101):
    if numb not in numbnot: # Si la valeur de num n'est pas une valeur interdite, alors affiche la
        print(numb)
else:
    print("\nFinisched !!")