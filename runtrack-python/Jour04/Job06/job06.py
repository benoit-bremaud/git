print("""\nProgramme Jour 4 - Job06
\nÉcrire un programme qui échange les valeurs de la première et de la dernière case d'une
liste quelconque non vide.""")

# Version 1
print("\nProgramme version 1")

list = [1,2,3,4,5,6,7,8,9]
print("\nListe avant swap :")
print(list)

def swapPositions(X):
     
    X[0], X[-1] = X[-1], X[0]
    return X

print("Liste après swap :") 
swapPositions(list)
print(list)
