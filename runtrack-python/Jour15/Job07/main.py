class Livre:
    """Classe définissant un livre caractérisé par :
    - son titre
    - son auteur
    - le nombre de page
    """

    def __init__(self, titre, auteur, nb_page):
        self.__titre = titre        # Attribut privé
        self.__auteur = auteur      # Attribut privé
        self.__nb_page = nb_page    # Attribut privé

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_page(self):
        return self.__nb_page

    def set_titre(self, new_titre):
        """On souhaite changer le nom du titre du livre."""
        print(f"Le titre du livre change, il devient : {new_titre}")
        self.__titre = new_titre

    def set_auteur(self, new_auteur):
        """On souhaite changer le nom de l'auteur."""
        print(f"Le nom de l'auteur change, il devient : {new_auteur}")
        self.__auteur = new_auteur

    def set_nb_page(self, new_nb_page):
        """On souhaite changer l'attribut __nb_page

        Note:
        Le nombre spécifié doit être un nombre entier
        """
        if isinstance(new_nb_page, int) and new_nb_page>0:
            print(f"Le nombre de page change, il devient : {new_nb_page}")
            self.__nb_page = new_nb_page
        else:
            print("Saisie incorrecte, veuillez saisir un nombre entier positif !")

livre = Livre(titre="Mon livre", auteur="Benoit Bremaud", nb_page=250)
titre = livre.get_titre()
auteur = livre.get_auteur()
page = livre.get_nb_page()
print(f"Le titre du livre est : {titre}")
print(f"Son auteur est : {auteur}")
print(f"Il fait {page} pages")

livre.set_titre("Mon deuxieme livre")
livre.set_auteur("Aline Berniere")
livre.set_nb_page(275)

titre = livre.get_titre()
auteur = livre.get_auteur()
page = livre.get_nb_page()

print(f"Nouveau titre : {titre}")
print(f"Nouvel Auteur : {auteur}")
print(f"Nouveau nombre de page : {page}")



