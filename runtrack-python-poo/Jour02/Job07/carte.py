class Carte:

    valeur = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]
    couleur = ["Pique", "Coeur", "Trefle", "Carreau"]

    def __init__(self, valeur=0, couleur=""):
        self.__valeur = valeur
        self.__couleur = couleur

    def get_carte(self):
        print(f"{self.__valeur} de {self.__couleur}")


