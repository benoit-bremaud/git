print("""\nProgramme Jour 4 - Job07
\nÉcrire un programme qui compte le nombre de multiples de 3 présents dans la liste L = [8, 24,48,2,16].""")

# Version 1
print("\nProgramme version 1")
L = [8,24,48,2,16]
n = 0
#print(L)
#print(len(L))
for i in range(len(L)):
    if (L[i]%3) == 0:
        n += 1
    #print(L[i])
print(n)  

# Version 2
print("\nProgramme version 2 - avec 'function'")
L = [8,24,48,2,16,30]

#print(L)
#print(len(L))
def list_modulo_3(X):
    n = 0
    for i in range(len(X)):
        if (X[i]%3) == 0:
            n += 1
        #print(L[i])
    print(n)

list_modulo_3(L)

# Version 3
print("\nProgramme version 3 - avec 'function' + choix du multiple")
L = [8,24,48,2,16,30]

def list_modulo_3(X):
    n = 0
    m=int(input("Valeur du multiple ? : "))
    for i in range(len(X)):
        if (X[i]%m) == 0:
            n += 1
    print(n)

list_modulo_3(L)