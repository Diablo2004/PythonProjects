class Dog:
    """A class representing a dog."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"


dog = Dog("Bruno")
print(dog.speak())


class Company:
    """A class representing a company."""

    company_name = "Google"

    @classmethod
    def change_name(cls, new_name):
        cls.company_name = new_name  # Modifies the class variable


Company.change_name("Microsoft")
print(Company.company_name)


class Math:
    """A class containing utility methods for mathematical operations."""

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(5, 10))
