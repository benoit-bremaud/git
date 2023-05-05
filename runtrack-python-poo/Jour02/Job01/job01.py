class Personne():
    """Classe définissant une personne caractérisée par les attributs suivants :
    - âge (entier initialisé à 14)

    """
    def __init__(self): # Définition du constructeur
        """Constructeur de notre classe. Et définition de nos attributs
        self.age = age                -> Attribut public
        self._age = age                 -> Attribut protégé
        self.__profession = profession  -> Attribut privé
        """
        self.age = 14 # Définition de l'attribut public 'age' et initialisation d'une valeur par défaut
    def afficherAge(self): # Définition de notre méthode (fonction) 'afficher Age'
        """Méthode qui permet de retourner l'attribut 'age' de la classe 'Personne'
        """
        print(self.age)
    def bonjour(self): # Définition de notre méthode (fonction) 'afficher bonjour'
        """Méthode qui permet d'afficher sur la console le message 'Hello'
        """
        print("Hello")
    def modifierAge(self, new_age): # Définition de notre méthode (fonction) 'modifier age'
        """Méthode qui prend en paramètre un attribut 'new_age' de type
        entier positif, puis modifie l'attribut 'age' de la classe 'Personne'
        Il faut vérifier avant que le 'new_age' est bien un entier positif
        """
        if isinstance(new_age, int) and new_age > 0:
            self.age = new_age # Change la valeur de l'attribut 'age' de la classe 'Personne' par la valeur du paramètre 'new_age'
        else:
            print("Valeur saisie incorrecte, veuillez recommencer !")

class Eleve(Personne): # Définition d'une classe fille nommée 'Eleve'
    """CLasse définissant un 'Eleve'. Elle n'a pas d'attributs propres,
     mais elle est caractérisée par les attributs hérités de sa classe
     mère définit précédemment.

    """
    def allerEnCours(self):
        """Méthode qui affiche le texte : 'Je vais en cours'
        """
        print("Je vais en cours !")
    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur():
    """Classe définissant 'Professeur' caractérisée par attributs :
    - matiereEnseignée : attribut privé
    """
    def __init__(self, matiereEnseignée): # Définition du constructeur
        """Constructeur de notre classe. Et définition de nos attributs
        self.__matiereEnseignée = matiere  -> Attribut privé
        """
        self.__matiereEnseignée = matiereEnseignée # Définition de l'attribut privé

    def enseigner(self):
        """Méthode qui affiche le message 'Le cours va commencer'
        """
        print("Le cours va commencer")



personne = Personne()

eleve = Eleve()

professeur = Professeur(matiereEnseignée="Math")

eleve.allerEnCours()
eleve.affichageAge()
eleve.afficherAge()

personne.afficherAge()

eleve.bonjour()

professeur.enseigner()






