print("""\nProgramme Jour 3 - Job 6
\n\nÀ partir de la chaîne "abcdefghijklmnopqrstuvwxyz" * 10, écrivez un programme qui
récupère et affiche autant de caractères que possible de cette chaîne sous forme de
suite pyramidale.""")

print("\nProgramme version - Version 1\n")

def TexteInPyramide(text):  # Définition de la fonction 'TexteInPyramide()' avec comme argument la variable 'text'
    endpos = 1              # initialisation de la variable 'endpos' avec la valeur '1'
    
    while len(text)>endpos: # boucle while (tant que) - tant que la longueur (len) de 'text' est supérieur à 'endpos' (initialement à 1) alors faire :
        print(text[0:endpos:])  # affiche le 'text' en commençant par la position '0' et en finissant par la position 'endpos'
        
        text = text[endpos::]   # réajuste la variable 'text' avec sa nouvelle valeur
        endpos += 1             # incrémente la variable 'endpos' (+1)
        
text = "abcdefghijklmnopqrstuvwxyz" * 10    # initialisation de la variable 'text'

TexteInPyramide(text)      # Appel de la fonction 'TexteInPyramide' pour qu'elle affiche 'text'
