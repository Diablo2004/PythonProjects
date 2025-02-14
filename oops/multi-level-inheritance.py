# Multi-level Inheritance - A chain of inheritance where a child class inherits from another child class

class Vehicle:
    def start(self):
        return "Vehicle starting..."

class Car(Vehicle):
    def drive(self):
        return "Car is driving..."

class ElectricCar(Car):
    def charge(self):
        return "Charging the car..."

tesla = ElectricCar()
print(tesla.start())  # Vehicle starting...
print(tesla.drive())  # Car is driving...
print(tesla.charge()) # Charging the car...
