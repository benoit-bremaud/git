# coding:utf-8
# Blackjack
# règles : http://fr.wikipedia.org/wiki.Blackjack_(jeu)

# moduls importations area
# import os # module qui dispose de variables et fonctions utiles pour dialoguer avec windows
import random

# définition des variables globales
couleur = ("c", "d", "h", "s")
valeur = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
jeu_joueur = []
jeu_banque = []
sabot = []
score = 0


# définition des classes
class Carte():
    val = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]
    coul = ["Coeur", "Pique", "Carreau", "Trefle"]

    def __init__(self, valeur, couleur):
        self.__valeur = valeur
        self.__couleur = couleur


# Définition des accesseurs (get.)
    def get_carte(self, valeur, couleur):
        return f"{self.__valeur}{self.__couleur}"


# Définitions des mutateurs (set.)

class Paquet(Carte):
    def __init__(self)
        super().__init__(valeur, couleur)
        self.__paquet_carte = []

    def mélanger_paquet(self):


    # Définition des accesseurs (get.)
    def get_paquet(self):
        return self.__paquet_carte

    # Définitions des mutateurs (set.)
    def set_paquet(self, nom_carte):
        self.__paquet_carte += nom_carte


class Sabot(Paquet):
    def __init__(self):
        self.__cartes_sabot = []

# Définition des méthodes
    def préparer_sabot(self, liste_cartes):
        for i in range(6):
            self.__cartes_sabot += liste_cartes

        random.shuffle(self.__cartes_sabot)
        return self.__cartes_sabot


    def distribuer_une_carte(self): # La distribution d'une carte signifie supprimer une carte du sabot
        carte = self.__cartes_sabot[-1]
        self.__cartes_sabot[-1].pop()
        return carte









class Joueur():
    def __init__(self, nom):
        self.__nom = nom # Il faut définir le nom du joueur
        self.__jeu = [] # Main du joueur est vide
        self.__solde = 100 # Solde par défaut
        self.__score = 0 # Scode au commencement de la partie


# Définition des accesseurs (get.)
    def get_jeu_du_joueur(self): # Récupère les cartes de la main du joueur
        return self.__jeu

    def get_score(self): # Récupère le score du joueur
        return self.__score

    def get_nom(self): # Récupère le nom du joueur
        print(f"Bienvenue dans le jeu {self.__nom}")

# Définitions des mutateurs (set.)
    def set_dans_jeu_joueur(self, nouvelle_carte): # Ajoute une carte à la main du joueur
        self.__jeu += nouvelle_carte

    def set_score(self, valeur_carte): # Mettre à jour le score du joueur
        self.__score += valeur_carte

    def set_name(self, nom_joueur): # Mettre à jour le nom d'un joueur
        self.__nom = nom_joueur




# générer un jeu de 52 cartes





# Fonction générer 6 jeux de 52 cartes soit 312
def init_sabot():
    for i in range(6):  # répéter 6 fois
        for val in list_couleur:
            for col in list_valeur:
                carte = [col + val]  # création d'une carte
                sabot.append(carte)  # création d'un jeu de 52 cartes
    random.shuffle(sabot)
    random.shuffle(sabot)
    return sabot


# Fonction distribuer une carte
def distrib_carte(pile):
    carte = pile[-1]
    pile.pop()
    return carte






# début du jeu
# Mise en place du sabot avec ses 312 cartes mélangées
init_sabot()

# Les joueurs posent leur mise


# Donner une première carte au joueur
jeu_joueur += distrib_carte(sabot)
print(f"Jeu du joueur :\n {jeu_joueur}")
# print(f"Score : {score}")

# donner une carte à la banque
jeu_banque += distrib_carte(sabot)
print(f"Jeu de la banque :\n {jeu_banque}")

# donner une carte au joueur 1, il a maintenant 2 cartes
jeu_joueur += distrib_carte(sabot)
print(f"Jeu du joueur :\n {jeu_joueur}")

# Que souhaite faire le joueur, prendre une autre carte ou arrêter ?
while input("\nSouhaitez-vous prendre une autre carte ? Y/N : \n") == "Y":
    jeu_joueur += distrib_carte(sabot)
    print(f"Jeu du joueur :\n {jeu_joueur}")

while jeu_banque < 17:
    jeu_banque += distrib_carte(sabot)
    print(f"Jeu de la banque :\n {jeu_banque}")

# end of programme
# os.system("pause") # met le programme en pause pour éviter que windows le ferme automatiquement
