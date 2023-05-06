#coding:utf-8

class Professeur:
    """Classe définissant 'Professeur' caractérisée par attributs :
    - matiereEnseignée : attribut privé
    """
    def __init__(self, matiereEnseignee): # Définition du constructeur
        """Constructeur de notre classe. Et définition de nos attributs
        self.__matiereEnseignée = matiere  -> Attribut privé
        """
        self._matiereEnseignee = matiereEnseignee # Définition de l'attribut privé

    def enseigner(self):
        """Méthode qui affiche le message 'Le cours va commencer'
        """
        print("Le cours va commencer")