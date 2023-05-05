class Rectangle: # Pour la création de classe, on utilise la convention d'écriture Camel Case
    """Classe définissant un rectangle caractérisé par :
        - sa longueur
        - sa largeur
    """
    def __init__(self, longueur, largeur): # Définition du constructeur (Méthode Constructeur)
        """Constructeur de notre classe. Chaque attribut est
        configuré en privé
        self.name = name                -> Attribut public
        self._age = age                 -> Attribut protégé
        self.__profession = profession  -> Attribut privé
        """
        self.__longueur = longueur      # Initialisé en privé
        self.__largeur = largeur        # Initialisé en privé

    def get_longueur(self):     # Création d'un accesseur
        return self.__longueur  # Qui affiche l'attribut longueur

    def set_longueur(self, nouvelle_longueur):  # Création d'un mutateur
        self.__longueur = nouvelle_longueur     # Qui permet de changer la valeur de l'attribut longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


# Affectation de valeur pour la longueur et la largeur de notre rectangle
rectangle = Rectangle(longueur = 10, largeur = 5)

# Récupération des valeurs des longueure/largeurs de notre rectangle
long = rectangle.get_longueur()
larg = rectangle.get_largeur()
print(f"Notre rectangle a une longueur de : {long} cm, et une largeur de : {larg} cm")

# Modification des valeurs des longueurs/largeurs de notre rectangle
rectangle.set_longueur(15)
rectangle.set_largeur(7)
print(rectangle.get_longueur())
print(rectangle.get_largeur())

