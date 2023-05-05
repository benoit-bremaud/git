# coding:utf-8

import hashlib, maskpass

# identifiant = input("Identifiant : ")

special_char = "!@#$%^&*"
test = 0

mot_de_passe = maskpass.askpass(prompt="Password: ", mask="*")

while test == 0:

    if len(mot_de_passe) < 8: # test si longueur > à 8 caractères
        print("Trop court, 8 caractère minimum !")
        continue
    if not any(char.isupper() for char in mot_de_passe): # test si au moins 1 caractère en Majuscule
        print("Il faut au moins une Majuscule")
        continue
    if not any(char.islower() for char in mot_de_passe): # test si au moins 1 caractère en minuscule
        print("Il faut au moins une minuscule")
        continue
    if not any(char.isdigit() for char in mot_de_passe): # test si au moins 1 caractère numérique
        print("Il faut au moins un caractère numérique")
        continue
    if not any(char in special_char for char in mot_de_passe): # test si au moins un caractère spécial
        print("Il faut au moins un caractère spécial : ! @ # $ % ^ & *")
        continue
    else:
        #print("Mot de passe valide\n")
        test=1
          
hashed_password = hashlib.sha256(mot_de_passe.encode("utf-8")).hexdigest()

with open("Jour08/Job01/myfile.txt", "r") as file:
    for i in file.readlines():
        if i.rstrip("\n") == hashed_password:
            print("Ce mot de passe éxiste déjà, veuillez en saisir un autre !!")
            break
    with open("Jour08/Job01/myfile.txt", "a") as file:
        file.write(f"{hashed_password}\n")

print("\tfin !!\n")
