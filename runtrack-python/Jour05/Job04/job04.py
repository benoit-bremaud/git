print("""Jour 05 - JOb 04
      \nJules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses messages.
      \nSa méthode était assez simple : il décalait les lettres de 3 rangs dans l'alphabet.
      \nCréer une fonction à laquelle on donne un message et un décalage, et la fonction renvoie alors le message
      \ndécalé dans l'alphabet. Il faudra gérer le dépassement ('z') décalé vers la droite revient sur 'a',
      \net 'a' décalé vers la gauche revient sur 'z')."""
      )

text = "abc Jules Cesar general et stratege romain zaze xyz"
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
coded_text = ""
#print("\n" + text + " " + str(len(text)))
#print("\n" + alphabet + " " + str(len(alphabet)) + " " + str(len(alphabet[26:52:])))
#print(alphabet[26:52:])
#print(len(alphabet[26:52:]))
#print(text[1])
n = int(input("Décalage (0 - 25): "))

print(alphabet[n+26:52:])

for i in range(len(text)):
    if text[i].casefold()==" ":
        coded_text += " "
    for j in range(len(alphabet[26:52:])):
        if text[i].casefold()==alphabet[j+26]:
            #print(alphabet[j+26])
            coded_text += alphabet[j+26+n]

print("Text non codé : " + text)
print("Text codé : " + coded_text)
