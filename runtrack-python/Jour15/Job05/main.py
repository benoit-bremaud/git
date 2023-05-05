class Animal: # Pour la création de classe, on utilise la convention d'écriture Camel Case
    """Classe définissant un animal caractérisé par :
        - son prenom
        - son age
    """
    def __init__(self, prenom="", age=0): # Définition du constructeur (Méthode Constructeur)
        """Constructeur de notre classe. Chaque attribut va
            être instancié avec une valeur par défaut
        """
        self.prenom = prenom
        self.age = age

    def vieillir(self):
        self.age += 1

    def nommer(self):
        self.prenom = "Luna"


animal = Animal()
age = animal.age
print(f"L'age de l'animal est : {age} ans")

animal.vieillir()
age = animal.age

print(f"L'age de l'animal est : {age} ans")

animal.nommer()
prenom = animal.prenom

print(f"L'animal se nomme : {prenom}")

