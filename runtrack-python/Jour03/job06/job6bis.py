print("""\nProgramme Jour 3 - Job 6 bis
\n\nÀ partir de la chaîne "abcdefghijklmnopqrstuvwxyz" * 10, écrivez un programme qui
récupère et affiche autant de caractères que possible de cette chaîne sous forme de
suite pyramidale.""")

print("\nProgramme version - Version 1\n")
       
s = "abcdefghijklmnopqrstuvwxyz" * 10    # initialisation de la variable 'text'
n = len(s)
rows = 0

while rows*(rows+1)//2 <= n:
    rows += 1
rows -= 1 # Adjust for overshooting the number of caracters
k = 0
for i in range(rows):
    spaces = " " * (rows-i-1)
    print(spaces + " ".join(s[k:k+i+1]))
    k += i+1
print(" " * (rows-1) + s[k:])
