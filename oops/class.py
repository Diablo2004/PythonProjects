class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.display_info())
print(car2.display_info())


class Person:
    def __init__(self, name="Unknown", age=0):  # Default values
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Object with default values
p1 = Person()
p1.greet()

# Object with provided values
p2 = Person("Alice", 25)
p2.greet()

