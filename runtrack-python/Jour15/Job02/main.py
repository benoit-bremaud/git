class Operation: # Pour la création de classe, on utilise la convention d'écriture Camel Case
    """Classe de test pour le Job 1 caractérisée par les attributs suivants :
        - nombre1
        - nombre2
    """
    def __init__(self): # Définition du constructeur
        self.nombre1 = 12
        self.nombre2 = 25

    def show(self):
        print("Le nombre 1 est : ", self.nombre1)
        print("Le nombre 2 est : ", self.nombre2)

    def add(self):
        print(self.nombre1 + self.nombre2)

test = Operation()
test.add()


