# Abstraction - hiding the implementation details and exposing only necessary parts of an object
# Improves Security
# Enhances code maintainability
# Simplifies complex systems

# Python provides abstraction using abstract classes and abstract methods with the help of the ABC (Abstract Base Class) module.

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start(self):  # Abstract method (must be implemented in subclasses)
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete Class (Subclass implementing abstract methods)
class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

# Creating object
my_car = Car()
my_car.start()
my_car.stop()
# Vehicle is an abstract class
# start() and stop() are abstract methods(must be implemented din all subclasses)
# Car inherits from vehicle and implements all abstract methods



from abc import ABC, abstractmethod

# Abstract Class
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):  # Abstract Method
        pass

# Concrete Class for Full-Time Employee
class FullTimeEmployee(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus

# Concrete Class for Part-Time Employee
class PartTimeEmployee(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05  # 5% bonus

# Creating objects
emp1 = FullTimeEmployee("Alice", 5000)
emp2 = PartTimeEmployee("Bob", 3000)

print(f"{emp1.name} Bonus: ${emp1.calculate_bonus()}")
print(f"{emp2.name} Bonus: ${emp2.calculate_bonus()}")
