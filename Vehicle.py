class Vehicle:

    def __init__(self, color, make, ticket):
        self.color = color
        self.make = make
        self.ticket = ticket


class Car(Vehicle):
    def __init__(self, color, make, ticket):
        Vehicle.__init__(self, color, make, ticket)
    
    def get_type(self):
        return "Car"


class Truck(Vehicle):
    def __init__(self, color, make, ticket):
        Vehicle.__init__(self, color, make, ticket)
    
    def get_type(self):
        return "Truck"

class Motorcycle(Vehicle):
    def __init__(self, color, make, ticket):
        Vehicle.__init__(self, color, make, ticket)
    
    def get_type(self):
        return "Motorcycle"