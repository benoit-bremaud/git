# Imports ----------------
# Importation des modules nécessaires depuis la bibliothèque guizero
from guizero import App, Text, Picture

# App --------------------
# Création de l'application graphique avec le titre "Wanted!"
app = App("Wanted!")
app.bg = "#FBFBD0"  # Définition de la couleur de fond de l'application en jaune pâle

# Widgets ----------------
# Création d'un élément texte pour afficher "WANTED" dans une grande taille de police
wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50  # Réglage de la taille du texte à 50 points

# Création d'un élément image (photo) affichant un fichier nommé "Profil.png"
# La largeur de l'image est définie à 400 pixels et la hauteur à 550 pixels
cat = Picture(app, image="Profil.png", width=400, height=550)

# Display ----------------
# Affichage de l'application graphique
app.display()
