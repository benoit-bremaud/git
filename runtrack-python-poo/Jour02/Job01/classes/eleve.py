#coding:utf-8

from classes.personne import Personne

class Eleve(Personne): # Définition d'une classe fille nommée 'Eleve'
    """CLasse définissant un 'Eleve'. Elle n'a pas d'attributs propres,
     mais elle est caractérisée par les attributs hérités de sa classe
     mère définit précédemment.

    """
    def __init__(self):
        super().__init__()
    # getters area
    
    def allerEnCours(self):
        """Méthode qui affiche le texte : 'Je vais en cours'
        """
        print("Je vais en cours !")
        
    def affichageAge(self):
        if self.age > 1:
            print(f"J'ai {self.age} ans")
        else:
            print(f"J'ai {self.age} an")
