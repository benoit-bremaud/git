# Imports ----------------
# Importation des modules nécessaires
from guizero import App, Text, PushButton
from random import choice

# Functions --------------
# Définition d'une fonction appelée lorsque le bouton est pressé
def choose_name():
    # Liste des prénoms possibles
    first_names = ["Barbara", "Woody", "Tiberius", "Smokey", "Jennifer", "Ruby"]
    # Liste des noms de famille possibles
    last_name = ["Spindleshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath"]
    # Sélection aléatoire d'un prénom et d'un nom de famille
    spy_name = choice(first_names) + " " + choice(last_name)
    # Affichage du nom généré dans l'interface graphique
    name.value = spy_name

# App --------------------
# Création de l'application graphique
app = App("TOP SECRET")

# Widgets ----------------
# Création des éléments graphiques (textes, bouton)
title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text="Tell me!")
button.bg = "red"  # Couleur de fond du bouton en rouge
button.text_size = 30  # Taille du texte du bouton
name = Text(app, text="")  # Zone de texte vide pour afficher le nom généré

# Display ----------------
# Affichage de l'application graphique
app.display()
