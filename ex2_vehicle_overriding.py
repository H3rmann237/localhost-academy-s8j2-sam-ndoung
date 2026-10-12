class Vehicule:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Marque : {self.brand}, modèle : {self.model}")

class Car(Vehicule):
    def __init__(self, brand, model,doors):
        super().__init__(brand, model)
        self.doors = doors

    def show_info(self):
        print(f"Voiture : {self.brand} - {self.doors}")

class Motobike(Vehicule):
    def __init__(self, brand, model,engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size

    def show_info(self):
        print(f"Moto : {self.brand} - {self.engine_size} cc")

vehicles = [
    Car("Toyota","Corolla",4),
    Motobike("Yamaha","MT-07",689),
    Car("Honda","Civic",4)
]

for vehicle in vehicles :
    vehicle.show_info()

#