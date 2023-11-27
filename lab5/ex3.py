class Vehicle:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(make, model, year)
    
    def calculate_mileage(distance, liters):
        self.mileage = distance / liters
        return self.mileage


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(make, model, year)
    
    def calculate_mileage(distance, liters):
        self.mileage = distance / liters
        return self.mileage

class Truck(Vehicle):
    def __init__(self, make, model, year):
        Vehicle.__init__(make, model, year)
    
    def calculate_mileage(distance, liters):
        self.mileage = distance / liters
        return self.mileage
