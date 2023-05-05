print("""\nProgramme Jour 3 - Job 7
\n\nscript qui recopie une chaîne (dans une nouvelle variable) en l'inversant.
Par exemple, « nikana » deviendra « anakin ».""")

print("\nProgramme version - Version 1")

text = str(input("Saisir votre texte :"))

def InversText(text):
    text=text[::-1]
    print(text)

InversText(text)

print("\n\fProgramme version - Version 2")

text = str(input("Saisir votre texte :"))

print(text[::-1])
