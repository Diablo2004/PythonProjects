# str - The __str__() method defines how an object is represented as a string
class Laptop:
    """
    Represents a Laptop with a brand and price.
    """
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"Laptop Brand: {self.brand}, Price: ${self.price}"

# Creating an object
laptop1 = Laptop("Dell", 1000)

# Printing the object
print(laptop1)  # Calls laptop1.__str__()

# repr - The __repr__() method defines the official string representation of an object
class Car:
    """
    Represents a Car with a model and price.
    """
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __repr__(self):
        return f"Car('{self.model}', {self.price})"

# Creating an object
car1 = Car("Tesla Model 3", 45000)

print(repr(car1))  # Calls __repr__()
print(car1)        # If __str__() is not defined, __repr__() is used

# Using both __str__ and __repr__
class Car:
    """
    Represents a Car with a model and price.
    Provides both a string representation (__str__) and an official representation (__repr__).
    """
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"Car Model: {self.model}, Price: ${self.price}"

    def __repr__(self):
        return f"Car('{self.model}', {self.price})"

car1 = Car("Tesla Model 3", 45000)

print(str(car1))  # Calls __str__()
print(repr(car1))  # Calls __repr__()

# len - __len__ allows custom classes to work with len().
class BookCollection:
    """
    Represents a collection of books.
    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

# Creating an object
collection = BookCollection()
collection.add_book("Harry Potter")
collection.add_book("The Hobbit")

print(len(collection))  # Calls __len__() method

# __len__() with an empty object
class Cart:
    """
    Represents a shopping cart.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

cart = Cart()
print(len(cart))  # Output: 0
cart.add_item("Laptop")
print(len(cart))  # Output: 1
