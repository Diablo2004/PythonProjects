# Multiple Inheritance - A child class inherits from multiple parent class
class Mammal:
    """A class representing mammals, which typically have fur."""

    def has_fur(self):
        return True


class Carnivore:
    """A class representing carnivores, which primarily eat meat."""

    def eats_meat(self):
        return True


class Tiger(Mammal, Carnivore):
    """A class representing a tiger, which is a type of mammal and carnivore."""

    def roar(self):
        return "Roar!"

tiger = Tiger()
print(tiger.has_fur())  # True
print(tiger.eats_meat())  # True
print(tiger.roar())  # Roar!
