class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(Vehicle):
    pass

School_Bus = bus("School Volvo", 180, 12)
print("Name: ", School_Bus.name, "Max Speed: ", School_Bus.max_speed, "Mileage: ", School_Bus.mileage)