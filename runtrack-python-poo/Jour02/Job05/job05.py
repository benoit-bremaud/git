from math import pi


class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return pi*(self.radius**2)


cercle = Cercle(50)
print(cercle.aire())
