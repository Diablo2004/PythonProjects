# Abstraction - hiding the implementation details and exposing only necessary parts of an object
# - Improves Security
# - Enhances code maintainability
# - Simplifies complex systems

# Python provides abstraction using abstract classes and abstract methods with the help of the ABC (Abstract Base Class) module.

from abc import ABC, abstractmethod


# Abstract Class
class Vehicle(ABC):
    """An abstract class representing a generic vehicle.

    This class enforces the implementation of `start` and `stop` methods in its subclasses.
    """

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Concrete Class (Subclass implementing abstract methods)
class Car(Vehicle):
    """A concrete class representing a Car, inheriting from Vehicle.

    Implements the `start` and `stop` methods specific to a car.
    """

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


# Creating object
my_car = Car()
my_car.start()
my_car.stop()

from abc import ABC, abstractmethod


# Abstract Class
class Employee(ABC):
    """An abstract class representing an employee.

    Attributes:
        name (str): The name of the employee.
        salary (float): The salary of the employee.
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass


# Concrete Class for Full-Time Employee
class FullTimeEmployee(Employee):
    """A concrete class representing a full-time employee.

    Inherits from Employee and implements the `calculate_bonus` method with a 10% bonus.
    """

    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus


# Concrete Class for Part-Time Employee
class PartTimeEmployee(Employee):
    """A concrete class representing a part-time employee.

    Inherits from Employee and implements the `calculate_bonus` method with a 5% bonus.
    """

    def calculate_bonus(self):
        return self.salary * 0.05  # 5% bonus


# Creating objects
emp1 = FullTimeEmployee("Alice", 5000)
emp2 = PartTimeEmployee("Bob", 3000)

print(f"{emp1.name} Bonus: ${emp1.calculate_bonus()}")
print(f"{emp2.name} Bonus: ${emp2.calculate_bonus()}")
