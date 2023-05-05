#password=input("Saisissez votre mot de passe : ")

a_string = ""
#password = ""
user_name = input("Renseignez votre nom : ")
password = ""


def initialisation_password():
    #boucle_password=0
    
    while boucle_password == 0:
        X = input("Veuillez saisir votre mot de passe : ")
        caracteres_speciaux ="!@#$%^&*"
        #print(X.isprintable())
        if len(X) >= 8:
            print("Le mot de passe contient bien au moins 8 caratères !")
            count=0
            for i in X: # X = "benoit"
                if i.isupper():
                    
                    count += 1
            if count >0:
                print("Le mot de passe contient bien au moins une Majuscule !")
                count=0
                for i in X:
                    if i.islower():
                        count += 1
                if count >0:
                    print("Le mot de passe contient bien au moins une lettre minuscule !")
                    count=0
                    for i in X:
                        if i.isnumeric():
                            count += 1
                    if count > 0:
                        print("Le mot de passe contient bien au moins 1 chiffre !")
                        count=0
                        for i in X:
                            for j in caracteres_speciaux:
                                #print(i,j)
                                if i == j:
                                    count += 1
                        if count > 0:
                            print("Le mot de passe contient bien au moins 1 caractère spécial !")
                            print("\n\tVotre mot de passe est CONFORME !")
                            boucle_password = 1
                            return X
                            
                            #print(password)
                        else:
                            print("Votre mot de passe doit contenir au moins un caractère spécial (! @ # $ % ^ & *)")
                    else:
                        print("Votre mot de passe doit contenir au moins un chiffre !")
                else:
                    print("Votre mot de passe doit contenir au moins une lettre minuscule !")
            else:
                print("Votre mot de passe doit contenir au moins une lettre Majuscule !")
        else:
            print("Mot de passe trop court, 8 caractères minimums, recommencez : ")
                
        #print(type(password))
password=initialisation_password()

# pour la suite faire le même programme avec les fonctions regex (voir tuto aide)

import hashlib
hashed_password = ""
hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

print(str(password))
#print(hashed_password)

# Création d'un fichier "mylist.txt"
"""  
modes d'ouverture   :   r (lecture seule)
                        w (écriture avec remplacement)
                        a (écriture avec ajout en fin de fichier)
                        x (lecture et écriture)
                        r+ (lecture:écriture dans un même fichier)

Lecture             :   read(), readline(), readlines()
"""
"""f = open("Jour06/Job01/myfile.txt", "w")
f.close()
"""

"""
# Permet de lire tout le contenu du fichier text 'myfile.txt'
with open("Jour06/Job01/myfile.txt", "r") as file:
    content = file.read() # Stock le contenu du fichier text dans la variable
    print(content) # Affiche le contenu du fichier txt via la variable 'content'
"""

class User:
    def __init__(self, name, hpass):
        self.name = name
        self.hpass = hpass
    
    def whoami(self):
        print("{} {}".format(self.name, self.hpass))

user1 = User(user_name, hashed_password)
user1.whoami()

# Permet d'écraser le contenu du fichier txt
 

with open("Jour06/Job01/myfile.txt", "a") as file:
    #file.write(user_name)
    #file.write(" | ")
    file.write(hashed_password)
    file.write("\n")
    print("Une nouvelle ligne a été insérée dans le fichier txt\n")

with open("Jour06/Job01/myfile.txt", "r") as file:
    line = file.readline()
    #line = file.readline()
    #line = file.readlines()
    print(line)



