#coding:utf-8

class Personne:
    """Classe définissant une personne caractérisée par les attributs suivants :
    - âge

    """
    def __init__(self): # Définition du constructeur
        """Constructeur de notre classe. Et définition de nos attributs
        self.age = age                -> Attribut public
        self._age = age                 -> Attribut protégé
        self.__profession = profession  -> Attribut privé
        """
        self.age = 14 # Définition de l'attribut public 'age' comme entier et initialisation d'une valeur par défaut
    
    # getters area
    
    def afficherAge(self): # Définition de notre méthode (fonction) 'afficher Age'
        """Méthode qui permet de retourner l'attribut 'age' de la classe 'Personne'
        """
        if self.age > 1:
            print(f"J'ai {self.age} ans")
        else:
            print(f"J'ai {self.age} an")
           
    def bonjour(self): # Définition de notre méthode (fonction) 'afficher bonjour'
        """Méthode qui permet d'afficher sur la console le message 'Hello'
        """
        print("Hello")
        
    # setters area
    
    def modifierAge(self, new_age): # Définition de notre méthode (fonction) 'modifier age'
        """Méthode qui prend en paramètre un attribut 'new_age' de type
        entier positif, puis modifie l'attribut 'age' de la classe 'Personne'
        Il faut vérifier avant que le 'new_age' est bien un entier positif
        """
        if isinstance(new_age, int) and new_age > 0:
            self.age = new_age # Change la valeur de l'attribut 'age' de la classe 'Personne' par la valeur du paramètre 'new_age'
        else:
            print("Valeur saisie incorrecte, veuillez recommencer !")
