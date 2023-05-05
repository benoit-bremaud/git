# coding:utf-8

# zone d'importation des modules externes
import os                       # module qui dispose de variables et fonctions utiles pour dialoguer avec windows
from random import randrange
from tkinter import *
from winsound import PlaySound

# définition des variables globales
couleur = ("c", "d", "h", "s")
valeur = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

# définition des classes


class Carte:

    def __init__(self, val="A", coul="d"):
        self.valeur = val
        self.couleur = coul

    def dessin_carte(self):
        """Renvoi du nom du fichier image de la carte"""
        # les cartes sont dans le répertoire "cartes-gif"
        nom = "cartes-gif/"+self.valeur+self.couleur+".gif"
        return PhotoImage(file=nom)


class Paquet_de_cartes:

    def __init__(self):
        """Construction de la pile des 52 cartes"""
        self.cartes =[]
        for coul in range(4):
            for val in range(13):
                nouvelle_carte = Carte(valeur[val], couleur[coul])
                self.cartes.append(nouvelle_carte)

    def battre(self):
        """Mélanger les cartes"""
        # PlaySound("sons/distrib.wav", 2)
        t = len(self.cartes)
        for i in range(t):
            h1, h2 = randrange(t), randrange(t)
            self.cartes[h1], self.cartes[h2] = self.cartes[2], self.cartes[h1]

    def tirer(self):
        """Tirer la première carte de la pile"""
        # PlaySound("sons/ramass.wav", 1)
        t = len(self.cartes)
        if t>0:
            carte = self.cartes[0] # choisir la première carte du jeu
            del(self.cartes[0]) # et la supprimer du jeu
            return carte
        else:
            return None


def jouer():
    global carte1, lab1
    c = jeu.tirer()
    if c != None:
        carte1 = c.dessin_carte()
        lab1.configure(image=carte1)
def reinit():
    global jeu
    jeu = Paquet_de_cartes()
    jeu.battre()
    jouer()

# fenetre graphique


fenetre = Tk()
fenetre.title("Cartes")
jeu = Paquet_de_cartes()
jeu.battre()
c = jeu.tirer()
carte1 = c.dessin_carte()
lab1 = Label(fenetre, image=carte1)
lab1.grid(row=0, column=0)
bouton1 = Button(fenetre, text="Recommencer", command=reinit)
bouton1.grid(row=0, column=0, sticky=W)
bouton2 = Button(fenetre,text="Recommencer", command=reinit)
bouton2.grid(row=1, column=0, sticky=E)

# demarrage
fenetre.mainloop()