#Class Method,Instance Method and Static Method

#Instance Method - Works with object instance
class Dog: # Sample class for instance method
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Bruno")
print(dog.speak())

#Class Method - Works with the class itself
class Company: # Sample class for class method
    company_name = "Google"

    @classmethod
    def change_name(cls, new_name):
        cls.company_name = new_name  # Modifies the class variable

Company.change_name("Microsoft")
print(Company.company_name)

#Static Method - Independent Utility

class Math: # Does not modify the class or the instance i.e. completely independent
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 10))

