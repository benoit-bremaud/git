class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modèle}")
        print(f"Année : {self.année}")
        print(f"Prix : {self.prix} Euros")


class Voiture(Vehicule):
    def __init__(self,marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.portes = 4

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modèle}")
        print(f"Année : {self.année}")
        print(f"Prix : {self.prix} Euros")
        print(f"Nombre de porte : {self.portes}")

class Moto(Vehicule):
    def __init__(self,marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.roue = 2

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modèle}")
        print(f"Année : {self.année}")
        print(f"Prix : {self.prix} Euros")
        print(f"Nombre de roue : {self.roue}")


vehicule = Vehicule("Mercedes", "Classe A", 2020, 18500)
vehicule.informationsVehicule()

voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()

moto = Moto("Yamaha", "1200 Vmax", "1987", "4500")
moto.informationsVehicule()