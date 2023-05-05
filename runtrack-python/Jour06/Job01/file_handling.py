#coding:utf-8

"""  
modes d'ouverture   :   r (lecture seule)
                        w (écriture avec remplacement)
                        a (écriture avec ajout en fin de fichier)
                        x (lecture et écriture)
                        r+ (lecture:écriture dans un même fichier)

Lecture             :   read(), readline(), readlines()
"""

with open("Jour06/Job01/myfile.txt", "w") as fichier:
    nombre = 15
    fichier.write(str(nombre))
    fichier.write("\nBonjour, je fais des tests\n")
    fichier.write("Et un autre test\n")