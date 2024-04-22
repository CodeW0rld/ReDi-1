class Airplane:
    def __init__(self, wing_span, lenght, fuel_capacity):
        self.wing_span = wing_span
        self.lenght = lenght
        self.fuel_capacity = fuel_capacity

    def takeOff(self):
        return "The airplane is taking off."
    
    def landing(self):
        return "The airplane is landing."