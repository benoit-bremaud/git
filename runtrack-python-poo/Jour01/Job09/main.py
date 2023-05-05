class Student:
    """Classe définissant une liste d'élève caractérisés par :
    - son nom
    - son prenom
    - le numéro d'étudiant
    - quantité crédits
    """

    def __init__(self, nom, prenom, no_etudiant, credits=0):
        self.__nom = nom  # Attribut privé
        self.__prenom = prenom  # Attribut privé
        self.__no_etudiant = no_etudiant  # Attribut privé
        self.__credits = credits  # Attribut privé + valeur par défaut
        self.__level = Student.__studentEval

    def studentinfo(self):
        print(f"Nom : {self.__nom}")
        print(f"Niveau : {self.__level}")

    def get_nom(self):  # Méthode type accesseur
        return self.__nom

    def get_prenom(self):  # Méthode type accesseur
        return self.__prenom

    def get_no_etudiant(self):  # Méthode type accesseur
        return self.__no_etudiant

    def get_credits(self):  # Méthode type accesseur
        return self.__credits

    def set_add_credits(self, credits):  # Méthode type mutateur 'set'
        if credits >= 0:
            self.__credits += credits
        else:
            print("Valeur saisie incorrecte !")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très Bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"



etudiant = Student(nom="Doe", prenom="John", no_etudiant=145)
nom = etudiant.get_nom()
prenom = etudiant.get_prenom()
no_etud = etudiant.get_no_etudiant()
credits = etudiant.get_credits()

print(f"Le nombre de crédits de {prenom} {nom} matricule {no_etud} est de {credits} points\n")

print("On va lui rajouter des crédits à trois reprises\n")

for i in range(3):
    etudiant.set_add_credits(10)

credits = etudiant.get_credits()

print(f"Le nombre de crédits de {prenom} {nom} matricule {no_etud} est de {credits} points\n")

etudiant.studentinfo()

