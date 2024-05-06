
class Airplane:
    def __init__(self, wing_span, length, fuel_capacity):
        self.wing_span = wing_span
        self.length = length
        self.fuel_capacity = fuel_capacity

        # Task 1 - Create a method "refuel" which sets the fuel level to highest level (10)
        self.fuel_level = 0

        # Task 2 - Create a method "take_off". 
        # Use the attribute below to perform some checks (fuel tank more than half full)
        self.on_the_ground = True
        
        # Task 3 - Create a method "land". 
        # Use the attribute below to perform some checks
        self.landing_gear_deployed = True

def refuel(self):
    self.fuel_level = 10
    return "The Airplane has been refueled to the highest level"

def take_off(self):
    if self.fuel_level > 5:
        self.on_the_ground = False
        return "The plane has taken off"
    else:
        return "Insufficient fuel for takeoff."

def land(self):
        if self.landing_gear_deployed:
            return "The airplane has landed"
        
        if not self.on_the_ground:
            return "Cannot land. Airplane is still in flight."

my_airplane = Airplane(10,10,10)
print(my_airplane.take_off())

print(my_airplane)
    

