class Vechicle:
    licnseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("turn On : Air")

class Car(Vechicle):
    pass

class Pickup(Vechicle):
    color = ""

class Van(Vechicle):
    pass

class EstateCar(Vechicle):
    pass

car1 = Car()
car1.turnOoAir()