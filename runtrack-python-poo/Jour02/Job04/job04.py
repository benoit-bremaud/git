class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


forme = Forme()
print(forme.aire())

rect = Rectangle(100, 200)
print(rect.aire())
