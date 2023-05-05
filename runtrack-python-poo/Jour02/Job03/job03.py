class Rectangle:
    """Classe définissant un rectangle caractérisé par les attributs suivants :
        - __longueur (privé)
        - __largeur (privé)
        """
    def __init__(self, longueur, largeur): # Définition du constructeur
        """Constructeur de notre classe. Et définition de nos attributs :
        self.__longueur = longueur  -> Attribut privé
        self.__largeur = largeur  -> Attribut privé
        """
        self.__longueur = longueur
        self.__largeur = largeur

    def get_périmètre(self):
        return (self.__longueur + self.__largeur)*2

    def get_surface(self):
        return self.__longueur * self.__largeur

    def get_long_rect(self):
        return self.__longueur

    def get_larg_rect(self):
        return self.__largeur

    def set_long_rect(self, longueur):
        self.__longueur = longueur

    def set_larg_rect(self, largeur):
        self.__largeur = largeur

class Parallélipipède(Rectangle):
    """Classe définissant un Parallélipipède héritant de la classe
    rectangle, caractérisée par les attributs suivants :
    - hauteur (public)
    """
    def __init__(self, longueur, largeur, hauteur): # Définition du constructeur
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def set_haut_para(self, hauteur):
        self.__hauteur = hauteur

    def get_haut_para(self):
        return self.__hauteur

    def get_volume(self):
        return self.get_surface()*self.get_haut_para()


rect = Rectangle(longueur=50, largeur=40)
para = Parallélipipède(longueur=100, largeur=100, hauteur=100)

# Caractéristiques objet 'rect'
print("\nCaractéristiques rectangle avec valeurs initiales")
print(f"Longueur : {rect.get_long_rect()}")
print(f"Largeur : {rect.get_larg_rect()}")
print(f"Périmètre : {rect.get_périmètre()}")
print(f"Surface : {rect.get_surface()}")

# Caractéristiques objet 'rect' après modifications
print("\nCaractéristiques rectangle avec valeurs modifiés")
rect.set_long_rect(200)
rect.set_larg_rect(100)
print(f"Longueur : {rect.get_long_rect()}")
print(f"Largeur : {rect.get_larg_rect()}")
print(f"Périmètre : {rect.get_périmètre()}")
print(f"Surface : {rect.get_surface()}")

# Caractéristiques objet 'para'
print("\nCaractéristiques parallèlipipède avec valeurs initiales")
print(f"Longueur : {para.get_long_rect()}")
print(f"Largeur : {para.get_larg_rect()}")
print(f"Hauteur : {para.get_haut_para()}")
print(f"Périmètre : {para.get_périmètre()}")
print(f"Surface : {para.get_surface()}")
print(f"Volume : {para.get_volume()}")

# Caractéristiques objet 'rect' après modifications
print("\nCaractéristiques parallèlipipède avec valeurs modifiés")
para.set_long_rect(200)
para.set_larg_rect(100)
para.set_haut_para(50)
print(f"Longueur : {para.get_long_rect()}")
print(f"Largeur : {para.get_larg_rect()}")
print(f"Hauteur : {para.get_haut_para()}")
print(f"Périmètre : {para.get_périmètre()}")
print(f"Surface : {para.get_surface()}")
print(f"Volume : {para.get_volume()}")


