# Hierarchical Inheritance

class Vehicle:
    def info(self):
        return "This is your vehicle"

class Car:
    def info(self):
        return "This is your car"

class Bicycle:
    def info(self):
        return "This is your bicycle"

C = Car()
print(C.info())

B = Bicycle()
print(B.info())

V = Vehicle()
print(V.info())

