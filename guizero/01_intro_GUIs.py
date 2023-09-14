# Imports ----------------
# Importation des modules nécessaires depuis la bibliothèque guizero
from guizero import App, Text

# App --------------------
# Création de l'application graphique avec le titre "Hello World!"
app = App(title="Hello World!")

# Widgets ----------------
# Création d'un élément texte avec le texte "Welcome to the app"
message = Text(app, text="Welcome to the app")

# Display ----------------
# Affichage de l'application graphique
app.display()
