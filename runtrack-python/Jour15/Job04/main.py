class Personne: # Pour la création de classe, on utilise la convention d'écriture Camel Case
    """Classe définissant une personne caractérisée par :
        - son nom
        - son prenom
    """
    def __init__(self): # Définition du constructeur (Méthode Constructeur)
        """Constructeur de notre classe. Chaque attribut va
            être instancié avec une valeur par défaut
        """
        self.nom = "Bremaud"
        self.prenom = "Benoit"

    def SePresenter(self): # Définition de la méthode "SePresenter"
        """Méthode permettant d'afficher le Prénom
        et le Nom de la personne"""
        print(f"Je suis {self.prenom} {self.nom}")


personne = Personne()
personne.SePresenter() # '.SePresenter' est un attribut de l'objet 'personne'


