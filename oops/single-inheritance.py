# Inheritance - Allows a class to inherit attributes and methods form another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

# Single Inheritance
class Animal: # Parent Class
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"


# Dog class inherits from Animal
class Dog(Animal):
    def make_sound(self):  # Overriding method
        return "Bark!"


dog = Dog("Buddy")
print(dog.name)  # Buddy
print(dog.make_sound())  # Bark
