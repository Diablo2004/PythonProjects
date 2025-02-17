# Inheritance - Allows a class to inherit attributes and methods form another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

# Single Inheritance
class Animal:
    """Represents an animal with a name and a sound."""

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    """Represents a dog, a subclass of Animal, with a custom sound."""

    def make_sound(self):
        return "Bark!"


dog = Dog("Buddy")
print(dog.name)  # Buddy
print(dog.make_sound())  # Bark

