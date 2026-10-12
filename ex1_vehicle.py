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

class Motobike(Vehicule):
    def __init__(self, brand, model,engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size

car = Car("Toyota","Corolla",4)
motobike = Motobike("Yamaha","MT-07", 689)
car.show_info()
motobike.show_info()
#les classes Car et Motorbike peuvent utiliser la méthode show_info() car elles heritent de
# la classe Car où cette dernière à été definie