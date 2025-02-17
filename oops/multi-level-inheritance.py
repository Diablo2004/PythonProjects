class Vehicle:
    """A base class representing a generic vehicle."""

    def start(self):
        return "Vehicle starting..."


class Car(Vehicle):
    """A class representing a car, which is a type of vehicle."""

    def drive(self):
        return "Car is driving..."


class ElectricCar(Car):
    """A class representing an electric car, which inherits from Car and Vehicle."""

    def charge(self):
        return "Charging the car..."


tesla = ElectricCar()
print(tesla.start())  # Vehicle starting...
print(tesla.drive())  # Car is driving...
print(tesla.charge())  # Charging the car...
