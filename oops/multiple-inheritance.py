# Multiple Inheritance - A child class inherits from multiple parent class

class Mammal:
    def has_fur(self):
        return True

class Carnivore:
    def eats_meat(self):
        return True

class Tiger(Mammal, Carnivore):
    def roar(self):
        return "Roar!"

tiger = Tiger()
print(tiger.has_fur())
print(tiger.eats_meat())
print(tiger.roar())
